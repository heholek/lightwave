/*
 * Copyright © 2012-2015 VMware, Inc.  All Rights Reserved.
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



VOID
VmKdcFreeKeySet(
    PVMKDC_KEYSET pKeySet);

VOID
VmKdcFreeEncKey(
    PVMKDC_ENCKEY pEncKey);

VOID
VmKdcFreeSalt(
    PVMKDC_SALT pSalt);

DWORD
VmKdcMakeSalt(
    VMKDC_SALTTYPE type,
    DWORD length,
    PUCHAR data,
    PVMKDC_SALT *ppRetSalt);

DWORD
VmKdcDecodeKeySet(
    PVMKDC_DATA pData,
    PVMKDC_KEYSET *ppRetKeySet);

DWORD
VmKdcDecryptKeySet(
    PVMKDC_CONTEXT pContext,
    PVMKDC_KEY pKey,
    PVMKDC_KEYSET pKeySet);

VOID
VmKdcPrintKeySet(
    PVMKDC_KEYSET pKeySet);
