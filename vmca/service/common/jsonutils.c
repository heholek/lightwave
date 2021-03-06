/*
 * Copyright © 2018 VMware, Inc.  All Rights Reserved.
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

#include <includes.h>

DWORD
VMCAJsonLoadObjectFromFile(
    PCSTR                   pcszFilePath,
    PVMCA_JSON_OBJECT       *ppJsonConfig
    )
{
    DWORD                   dwError = 0;
    json_error_t            jsonError = {0};
    PVMCA_JSON_OBJECT       pJsonConfig = NULL;
    size_t                  szJsonFlags = JSON_DECODE_ANY;

    if (IsNullOrEmptyString(pcszFilePath) || !ppJsonConfig)
    {
        dwError = ERROR_INVALID_PARAMETER;
        BAIL_ON_VMCA_ERROR(dwError);
    }

    if (!(pJsonConfig = json_load_file(pcszFilePath, szJsonFlags, &jsonError)))
    {
        VMCA_LOG_ERROR(
                "[%s,%d] Failed to open config file (%s). Error: %s:%d",
                __FUNCTION__,
                __LINE__,
                pcszFilePath,
                jsonError.text,
                jsonError.line);
        dwError = VMCA_JSON_FILE_LOAD_ERROR;
        BAIL_ON_VMCA_ERROR(dwError);
    }

    *ppJsonConfig = pJsonConfig;


cleanup:

    return dwError;

error:

    VMCAJsonCleanupObject(pJsonConfig);
    if (ppJsonConfig)
    {
        *ppJsonConfig = NULL;
    }

    goto cleanup;
}

DWORD
VMCAJsonGetObjectFromKey(
    PVMCA_JSON_OBJECT       pJson,
    PCSTR                   pcszKey,
    PVMCA_JSON_OBJECT       *ppJsonValue
    )
{
    DWORD                   dwError = 0;
    PVMCA_JSON_OBJECT       pJsonValue = NULL;

    if (!pJson || IsNullOrEmptyString(pcszKey) || !ppJsonValue)
    {
        dwError = ERROR_INVALID_PARAMETER;
        BAIL_ON_VMCA_ERROR(dwError);
    }

    if (!(pJsonValue = json_object_get(pJson, pcszKey)))
    {
        dwError = VMCA_JSON_PARSE_ERROR;
        BAIL_ON_JSON_PARSE_ERROR(dwError);
    }

    *ppJsonValue = pJsonValue;

cleanup:

    return dwError;

error:

    if (ppJsonValue)
    {
        *ppJsonValue = NULL;
    }

    goto cleanup;
}

DWORD
VMCAJsonGetStringFromKey(
    PVMCA_JSON_OBJECT       pJson,
    PCSTR                   pcszKey,
    PSTR                    *ppszValue
    )
{
    DWORD                   dwError = 0;
    PVMCA_JSON_OBJECT       pJsonValue = NULL;
    PCSTR                   pcszValue = NULL;

    if (!pJson || IsNullOrEmptyString(pcszKey) || !ppszValue)
    {
        dwError = ERROR_INVALID_PARAMETER;
        BAIL_ON_VMCA_ERROR(dwError);
    }

    dwError = VMCAJsonGetObjectFromKey(pJson, pcszKey, &pJsonValue);
    BAIL_ON_VMCA_ERROR(dwError);

    pcszValue = json_string_value(pJsonValue);
    if (IsNullOrEmptyString(pcszValue))
    {
        dwError = VMCA_JSON_PARSE_ERROR;
        BAIL_ON_VMCA_ERROR(dwError);
    }

    dwError = VMCAAllocateStringA(pcszValue, ppszValue);
    BAIL_ON_VMCA_ERROR(dwError);

cleanup:

    return dwError;

error:

    if (ppszValue)
    {
        *ppszValue = NULL;
    }

    goto cleanup;
}

VOID
VMCAJsonCleanupObject(
    PVMCA_JSON_OBJECT       pJson
    )
{
    if (pJson)
    {
        json_decref(pJson);
    }
}
