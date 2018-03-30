﻿/*
 * Copyright © 2012-2016 VMware, Inc.  All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the “License”); you may not
 * use this file except in compliance with the License.  You may obtain a copy
 * of the License at http://www.apache.org/licenses/LICENSE-2.0
 *·
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an “AS IS” BASIS, without
 * warranties or conditions of any kind, EITHER EXPRESS OR IMPLIED.  See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */
namespace VMwareMMCIDP.UI.Common.Utilities
            byte[] certBytes = cert.Export(X509ContentType.Cert);
            return sb.ToString();
        public static string GetKeyUsage(this X509Certificate2 cert)
                    break;
        public static string GetFormattedThumbPrint(this X509Certificate2 cert)
        public static void ShowX509Certificate(this string certString)

        public static string GetDisplayString(this X509Certificate2 cert)
        {
            if (cert != null)
            {
                return string.Format("Subject:{0}, Issuer:{1}, Expires:{2}",
                    cert.SubjectName.Name,
                    cert.IssuerName.Name,
                    cert.NotAfter.ToString("MM-dd-yyyy hh:mm:ss"));
            }
            return "Invalid certificate";
        }
        public static string GetDisplayString(this string certString)
        public static X509Certificate2 GetX509Certificate2FromString(this string certString)