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

#include "build-version.h"
#ifndef MAKESTR
#define MAKESTR(x) #x
#define XSTR(x) MAKESTR(x)
#endif

#ifdef VERSION_MAJOR
#define PROD_MAJOR VERSION_MAJOR
#else
#define PROD_MAJOR 6
#endif

#ifdef VERSION_MINOR
#define PROD_MINOR VERSION_MINOR
#else
#define PROD_MINOR 6
#endif

#ifdef VERSION_MAINT
#define FILE_MAJOR VERSION_MAINT
#else
#define FILE_MAJOR 0
#endif

#if !defined(BUILD_NUMBER)
#define FILE_MINOR 1
#else
#define FILE_MINOR BUILD_NUMBER
#endif

#if !defined(PRODUCT_BUILD_NUMBER)
#define PRODUCT_FILE_MINOR 1
#else
#define PRODUCT_FILE_MINOR PRODUCT_BUILD_NUMBER
#endif

#define FILE_VERSION           PROD_MAJOR,PROD_MINOR,FILE_MAJOR,PRODUCT_FILE_MINOR
#define FILE_VERSION_STRING    XSTR(PROD_MAJOR) "." XSTR(PROD_MINOR) "." XSTR(FILE_MAJOR) "." XSTR(PRODUCT_FILE_MINOR)

/*
 * Not a typo, VERSIONINFO->PRODUCTVERSION uses PRODUCT_BUILD_NUMBER intentionally
 */
#define PRODUCT_VERSION        PROD_MAJOR,PROD_MINOR,FILE_MAJOR,PRODUCT_FILE_MINOR
#define PRODUCT_VERSION_STRING XSTR(PROD_MAJOR) "." XSTR(PROD_MINOR) "." XSTR(FILE_MAJOR) " build-" XSTR(FILE_MINOR)
