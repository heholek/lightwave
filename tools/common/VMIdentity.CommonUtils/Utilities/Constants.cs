﻿/*

using System.Configuration;
using System.IO;
using System.Text;
namespace VMIdentity.CommonUtils
    {
        public const int SECRET_KEY_LENGTH = 256;
        public const string CONFIRM_SELECTED_DELETE = "Are you sure, you want to delete selected {0} ({1}) ?";

		// Error messages
		public const string INVALID_CREDENTIAL = "Invalid credentials or server is not reachable!";
		public const string CORRECT_PWD = "Password is correct.";
		public const string INVALID_PWD = "Password is invalid";
		public const string SERVER_TIMEOUT = "Server timed out.";
		public const string CONFIG_NOT_FOUND = "Configuration xml is invalid/missing. Try reinstalling application.";

		public const int TEN_SEC = 10000;

        //key names in configuration xml file
        public const string TENANT = "tenant";
        public const string CA_ROOT = "caRoot";
        public const string CS_ROOT = "csRoot";
        public const string DIR_ROOT = "dirRoot";
        public const string RAFT_ROOT = "raftRoot";
        public const string PSC_ROOT = "pscRoot";
        public const string SSO_ROOT = "ssoRoot";
        public const string DNS_ROOT = "dnsRoot";

        public static string GetDeleteMsg(string obj, string value)
        {
            return string.Format(CONFIRM_DELETE, obj, value);
        }

        public static string GetSelectedDeleteMsg(string obj, int count)
        {
            return string.Format(CONFIRM_SELECTED_DELETE, obj, count);
        }

        public static string GetDNFormat(string tenant)
        {
            string[] strArr = tenant.Split('.');
            StringBuilder sb = new StringBuilder();
            foreach (var str in strArr)
            {
                sb.Append("dc=" + str + ",");
            }
            if (sb.Length != 0)
                sb.Remove(sb.Length - 1, 1);
            return sb.ToString();
        }

        public static string GetConfigValue(string key)
        {
            var assemblyLoc=System.Reflection.Assembly.GetExecutingAssembly().Location;
            var filePath=Path.Combine(Path.GetDirectoryName(assemblyLoc),"VMIdentity.CommonUtils.dll.config");
            ConfigurationFileMap fileMap=new ConfigurationFileMap(filePath);
            System.Configuration.Configuration configuration=System.Configuration.ConfigurationManager.OpenMappedMachineConfiguration(fileMap);
            return configuration.AppSettings.Settings[key].Value;
        }
    }
}