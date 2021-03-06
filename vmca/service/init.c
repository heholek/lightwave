/*
 * Copyright © 2012-2018 VMware, Inc.  All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the “License”); you may not
 * use this file except in compliance with the License.  You may obtain a copy
 * of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an “AS IS” BASIS, without
 * warranties or conditions of any kind, EITHER EXPRESS OR IMPLIED.  See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */
#include "includes.h"

static
DWORD
InitializeDatabase(
    VOID
    );

static
DWORD
InitializeLog(
    BOOL overrideLogLevel,
    BOOL overrideLogType
    );

static
DWORD
InitializeEventLog(
    VOID
    );

static
VOID
VMCAEnableSuidDumpable(
    VOID
    );
// init global/static in single thread mode during server startup
DWORD
VMCAInitialize(
    BOOL overrideLogLevel,
    BOOL overrideLogType
    )
{
    DWORD dwError = 0;

    VMCAEnableSuidDumpable();

    dwError = VMCACommonInit();
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = InitializeLog(FALSE, FALSE);
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = InitializeEventLog();
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = InitializeDatabase();
    BAIL_ON_VMCA_ERROR(dwError);

    // Don't bail on Error , this just sets up the current state
    dwError = VMCASrvInitCA();

#if defined(REST_ENABLED) || defined(REST_V2_ENABLED)
    dwError = OidcClientGlobalInit();
    BAIL_ON_VMCA_ERROR(dwError);
#endif

    dwError = VMCASrvDirSyncInit();
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = VMCARPCInit();
    BAIL_ON_VMCA_ERROR(dwError);

#ifdef REST_V2_ENABLED
    dwError = VMCARestServerInit();
    BAIL_ON_VMCA_ERROR(dwError);
#endif

error:

    return dwError;
}

VOID
VMCAShutdown(
    VOID
    )
{
    VMCARPCShutdown();
    VMCAServiceShutdown();
    VMCASrvDirSyncShutdown();
    VMCATerminateLogging();
    VMCASrvCleanupGlobalState();
#if defined(REST_ENABLED) || defined(REST_V2_ENABLED)
    OidcClientGlobalCleanup();
#endif
    VMCACommonShutdown();

#ifdef REST_V2_ENABLED
    if (VMCARestServerStop() == 0)
    {
        VMCARestServerShutdown();
    }
#endif
}

static
DWORD
InitializeDatabase(
    VOID
    )
{
    DWORD dwError = 0 ;
    PSTR pszCertDBPath = NULL;

    dwError = VMCACreateDataDirectory();
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = VMCAGetCertsDBPath(&pszCertDBPath);
    BAIL_ON_VMCA_ERROR(dwError);

    VMCA_LOG_INFO(
            "Initializing database: [%s]",
            VMCA_SAFE_STRING(pszCertDBPath));

    dwError = VmcaDbInitialize(pszCertDBPath);
    BAIL_ON_VMCA_ERROR(dwError);

error:

    VMCA_SAFE_FREE_STRINGA(pszCertDBPath);

    return dwError;
}

static
DWORD
InitializeLog(
    BOOL overrideLogLevel,
    BOOL overrideLogType
    )
{
    return VMCAInitLog();
}

static
DWORD
InitializeEventLog(
    VOID
    )
{
    return 0;
}

DWORD
VMCASrvInitCA(
    VOID
    )
{
    DWORD dwError = 0;
    PVMCA_CERTIFICATE pRootCACert = NULL;
    PVMCA_KEY pPrivateKey = NULL;
    PSTR pszRootCertFile = NULL;
    PSTR pszPrivateKeyFile = NULL;
    PSTR pszPasswordFile = NULL;
    PVMCA_X509_CA pCA = NULL;
    PVMCA_POLICY *ppPolicies = NULL;
    DWORD dwCRLNumberCurrent = 0;
    BOOL bIsHoldingMutex = FALSE;
    PVMCA_JSON_OBJECT pJsonConfig = NULL;

    dwError = VMCAConfigLoadFile(VMCA_CONFIG_FILE_PATH, &pJsonConfig);
    if (dwError == VMCA_JSON_FILE_LOAD_ERROR)
    {
        VMCA_LOG_INFO(
                "[%s,%d] Failed to open VMCA config file (%s). Service starting without it...",
                __FUNCTION__,
                __LINE__,
                VMCA_CONFIG_FILE_PATH);
        dwError = 0;
    }
    BAIL_ON_VMCA_ERROR(dwError);

#ifdef SECURITY_PLUGIN_ENABLED
    dwError = VMCASecurityInitCtx(pJsonConfig);
    BAIL_ON_VMCA_ERROR(dwError);
#endif

    dwError = VMCAPolicyInit(VMCA_POLICY_FILE_PATH, &ppPolicies);
    if (dwError == VMCA_JSON_FILE_LOAD_ERROR)
    {
        VMCA_LOG_INFO(
                "[%s,%d] Failed to load policy config file, will not enforce policies...",
                __FUNCTION__,
                __LINE__);
        dwError = 0;
    }
    else if (dwError != 0)
    {
        VMCA_LOG_INFO(
                "[%s,%d] Failed to initialize policy context. Error: %d",
                __FUNCTION__,
                __LINE__,
                dwError);
    }
    BAIL_ON_VMCA_ERROR(dwError);

    gVMCAServerGlobals.gppPolicies = ppPolicies;

    dwError = VMCAGetRootCertificateFilePath(&pszRootCertFile);
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = VMCAGetPrivateKeyPath(&pszPrivateKeyFile);
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = VMCAGetPrivateKeyPasswordPath(&pszPasswordFile);
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = VMCAReadCertificateChainFromFile(pszRootCertFile,&pRootCACert);
    BAIL_ON_VMCA_ERROR(dwError);

    //
    // TODO : Support Passwords for private key
    //
    dwError =  VMCAReadPrivateKeyFromFilePrivate(
                    pszPrivateKeyFile,
                    NULL,
                    &pPrivateKey);
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = VMCAValidateCACertificatePrivate(
                    (LPSTR) pRootCACert,
                    NULL,
                    pPrivateKey);
    BAIL_ON_VMCA_ERROR(dwError);

    dwError = VMCACreateCA( pRootCACert, pPrivateKey, NULL, &pCA);
    BAIL_ON_VMCA_ERROR(dwError);

    if (BN_num_bits(pCA->pKey->pkey.rsa->n) < VMCA_MIN_CA_CERT_PRIV_KEY_LENGTH)
    {
        dwError = VMCA_ERROR_INVALID_KEY_LENGTH;
        BAIL_ON_VMCA_ERROR(dwError);
    }

    dwError = VMCASrvSetCA(pCA);
    BAIL_ON_VMCA_ERROR(dwError);

    pthread_mutex_lock (&gVMCAServerGlobals.mutexCRL);

    bIsHoldingMutex = TRUE;

    dwError = VmcaDbGetCurrentCRLNumber(&dwCRLNumberCurrent);

    if (dwError == ERROR_OBJECT_NOT_FOUND)
    {
        dwError = 0;
        dwCRLNumberCurrent = 0;
    }
    BAIL_ON_VMCA_ERROR (dwError);

    gVMCAServerGlobals.dwCurrentCRLNumber = dwCRLNumberCurrent;

    pthread_mutex_unlock (&gVMCAServerGlobals.mutexCRL);

    bIsHoldingMutex = FALSE;

error:

    VMCAJsonCleanupObject(pJsonConfig);
    if (pPrivateKey != NULL)
    {
        VMCAFreeKey(pPrivateKey);
    }
    if (pRootCACert != NULL)
    {
        VMCAFreeCertificate(pRootCACert);
    }
    if (bIsHoldingMutex)
    {
        pthread_mutex_unlock(&gVMCAServerGlobals.mutexCRL);
    }
    VMCA_SAFE_FREE_STRINGA(pszRootCertFile);
    VMCA_SAFE_FREE_STRINGA(pszPrivateKeyFile);
    VMCA_SAFE_FREE_STRINGA(pszPasswordFile);

    if (pCA)
    {
        VMCAReleaseCA(pCA);
    }

    return dwError;
}

/*
 * Any process which has changed privilege levels will not be dumped.
 * Enable it explicitly
 */
static
VOID
VMCAEnableSuidDumpable(
    VOID
    )
{
    if (prctl(PR_SET_DUMPABLE, 1, 0, 0, 0) == -1)
    {
        VMCA_LOG_ERROR(
            "%s: coredumps will not be generated error: %d",
            __FUNCTION__,
            errno);
    }
}
