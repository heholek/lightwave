/*
 * Copyright © 2017-2018 VMware, Inc.  All Rights Reserved.
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

#ifndef VMCOMMON_STRUCTS_H
#define VMCOMMON_STRUCTS_H

/* threading */
typedef struct _VM_MUTEX
{
    BOOLEAN         bInitialized;
    pthread_mutex_t critSect;
} VM_MUTEX, *PVM_MUTEX;

typedef struct _VM_COND
{
    BOOLEAN         bInitialized;
    pthread_cond_t  cond;
} VM_COND, *PVM_COND;

typedef struct _VM_RWLOCK
{
    BOOLEAN             bInitialized;
    pthread_rwlock_t    lock;
} VM_RWLOCK, *PVM_RWLOCK;

/*
 * Counter metrics data
 */
typedef struct _VM_METRICS_COUNTER
{
    PSTR                            pszName;
    PSTR                            pszLabel;
    PSTR                            pszDescription;
    int64_t                         value;

} VM_METRICS_COUNTER, *PVM_METRICS_COUNTER;

/*
 * Gauge metrics data
 */
typedef struct _VM_METRICS_GAUGE
{
    PSTR                            pszName;
    PSTR                            pszLabel;
    PSTR                            pszDescription;
    int64_t                         value;

} VM_METRICS_GAUGE, *PVM_METRICS_GAUGE;

/*
 * Histogram metrics data
 */
typedef struct _VM_METRICS_HISTOGRAM
{
    PSTR                            pszName;
    PSTR                            pszLabel;
    PSTR                            pszDescription;
    DWORD                           bucketSize;
    int64_t*                        pBucketKeys;
    int64_t*                        pBucketValues;
    int64_t                         count;
    int64_t                         sum;

} VM_METRICS_HISTOGRAM, *PVM_METRICS_HISTOGRAM;

/*
 * Enumerator for Metrics Type
 */
typedef enum
{
    VM_METRICS_TYPE_COUNTER,
    VM_METRICS_TYPE_GAUGE,
    VM_METRICS_TYPE_HISTOGRAM

} VM_METRICS_TYPE;

/*
 * Linked List Entry
 */
typedef struct _VM_METRICS_LIST_ENTRY
{
    PVOID                           pData;
    VM_METRICS_TYPE                 type;
    struct _VM_METRICS_LIST_ENTRY*  pNext;

} VM_METRICS_LIST_ENTRY, *PVM_METRICS_LIST_ENTRY;

/*
 * Metrics context structure
 */
typedef struct _VM_METRICS_CONTEXT
{
    PVM_METRICS_LIST_ENTRY          pMetrics;
    pthread_rwlock_t                rwLock;

} VM_METRICS_CONTEXT, *PVM_METRICS_CONTEXT;

/* httpclient */
typedef struct _VM_HTTP_CLIENT
{
    CURL* pCurl;
    struct curl_slist *pHeaders;
    PLW_HASHMAP pQueryParamsMap;
    PSTR  pszCAPath;
    PSTR  pszBody;
    long nStatus;
    PSTR pszResult;
    size_t nResultLen;
} VM_HTTP_CLIENT, *PVM_HTTP_CLIENT;

/* json result */
typedef struct _VM_JSON_RESULT
{
    json_t *pJsonRoot;
    int nJsonErrorLine;
    PSTR pszJsonErrorText;
}VM_JSON_RESULT, *PVM_JSON_RESULT;

/* vmregconfig */
typedef struct _VM_REGCONFIG_LIST_KV
{
    PSTR    pszKey;
    PSTR    pszValue;
    size_t  iValueSize;

    struct _VM_REGCONFIG_LIST_KV*  pNext;
} VM_REGCONFIG_LIST_KV, *PVM_REGCONFIG_LIST_KV;

typedef struct _VM_REGCONFIG_LIST_ENTRY
{
    // synchronize access among threads in a process
    PVM_MUTEX       pMutex;

    // config file name
    PSTR            pszFileName;
    // dummy file locking for cross processes write synchronization
    PSTR            pszLockFileName;

    PSTR            pszTopKey;
    struct stat     fileStat;
    BOOLEAN         bReadOnly;

    PVM_REGCONFIG_LIST_KV pListKV;

    struct _VM_REGCONFIG_LIST_ENTRY*  pNext;
} VM_REGCONFIG_LIST_ENTRY, *PVM_REGCONFIG_LIST_ENTRY;

typedef struct _VM_REGCONFIG_CONTEXT
{
    // No concurrent protection for pListEntry for now
    // all config files should be loaded during startup time.
    PVM_REGCONFIG_LIST_ENTRY pListEntry;

} VM_REGCONFIG_CONTEXT;

#endif //VMCOMMON_STRUCTS_H