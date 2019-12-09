Name:    lightwave
Summary: VMware Lightwave
Version: %{_version}
Release: %{_patch}%{_dist}
Group:   Applications/System
Vendor:  VMware, Inc.
License: VMware
URL:     http://www.vmware.com
BuildArch: x86_64

Requires: openssl >= 1.0.2, coreutils >= 8.22, cyrus-sasl >= 2.1, c-rest-engine >= 1.1, gawk >= 4.1.3, lightwave-server = %{_version}, lightwave-client = %{_version}
BuildRequires: openssl-devel >= 1.0.2, libyaml-devel >= 0.1.7, coreutils >= 8.22, likewise-open-devel >= 6.2.11, python2-devel >= 2.7.8, c-rest-engine-devel >= 1.1

%if 0%{?fedora} >= 21
Requires: likewise-open >= 6.2.11, boost = 1.60.0, java-1.8.0-openjdk >= 1.8.0.131, krb5-libs >= 1.14, sqlite >= 3.14, tomcat >= 8.5.31, apache-commons-daemon >= 1.0.15, apache-commons-daemon-jsvc >= 1.0.15
BuildRequires: boost-devel = 1.60.0, java-1.8.0-openjdk >= 1.8.0.131, ant >= 1.9.4, maven >= 3.3.9
%else
Requires: apache-tomcat >= 8.5.31, commons-daemon >= 1.0.15
BuildRequires: apache-ant >= 1.9.4, apache-maven >= 3.3.9
%if "%{_dist}" == ".lwph2"
Requires:  shadow >= 4.2.1, likewise-open = 6.2.11, boost = 1.63.0,  openjre8 >= 1.8.0.152, krb5 >= 1.16, sqlite-devel >= 3.19.3
BuildRequires: shadow >= 4.2.1, boost-devel = 1.63.0 , openjdk8 >= 1.8.0.152, cmocka >= 1.1
%else
Requires: shadow >= 4.2.1, likewise-open >= 6.2.11, boost = 1.60.0, openjre >= 1.8.0.131, krb5 >= 1.14, sqlite-autoconf >= 3.14
BuildRequires: shadow >= 4.2.1, boost-devel = 1.60.0,  openjdk >= 1.8.0.131
%endif
%endif

%description
VMware Lightwave Server

#
# The _unpackaged_files_terminate_build macro, if set to 1,
# tells rpmbuild to exit if it finds files that are in the
# $RPM_BUILD_ROOT directory but not listed as part of the
# package.
#
# Set this macro to 0 to turn off the Fascist build policy
#
%define _unpackaged_files_terminate_build 0

%define _jarsdir %{_prefix}/jars
%define _bindir %{_prefix}/bin
%define _vmdirtestdir %{_prefix}/test/vmdir
%define _vmdirtestbindir %{_vmdirtestdir}/bin
%define _vmdirtestlibdir %{_vmdirtestdir}/lib64
%define _stsdir %{_prefix}/vmware-sts
%define _stssampledir %{_prefix}/vmware-sts-sample
%define _webappsdir %{_stsdir}/webapps
%define _webappssampledir %{_stssampledir}/webapps
%define _stsconfdir %{_stsdir}/conf
%define _stsbindir %{_stsdir}/bin
%define _stssampleconfdir %{_stssampledir}/conf
%define _stssamplebindir %{_stssampledir}/bin
%define _stslogsdir %{_stsdir}/logs
%define _lightwavelogsdir /var/log/vmware/sso
%define _configdir %{_datadir}/config
%define _servicedir /lib/systemd/system
%define _stsdbdir %{_localstatedir}/vmware-sts
%define _lwuser lightwave
%define _lwgroup lightwave
%define _machinecertdir /etc/vmware/vmware-vmafd

%if 0%{?_likewise_open_prefix:1} == 0
%define _likewise_open_prefix /opt/likewise
%endif

%define _likewise_open_bindir %{_likewise_open_prefix}/bin
%define _likewise_open_sbindir %{_likewise_open_prefix}/sbin

%if 0%{?_javahome:1} == 0
%define _javahome %{_javahome}
%endif

%if 0%{?_vmdir_prefix:1} == 0
%define _vmdir_prefix /opt/vmware
%endif

%if 0%{?_vmafd_prefix:1} == 0
%define _vmafd_prefix /opt/vmware
%endif

%if 0%{?_vmca_prefix:1} == 0
%define _vmca_prefix /opt/vmware
%endif

%if 0%{?_mutentca_prefix:1} == 0
%define _mutentca_prefix /opt/vmware
%endif

%if 0%{?_vmdns_prefix:1} == 0
%define _vmdns_prefix /opt/vmware
%endif

%if 0%{?_vmsts_prefix:1} == 0
%define _vmsts_prefix /opt/vmware
%endif

%if 0%{?_sasl_prefix:1} == 0
%define _sasl_prefix /usr
%endif

%if 0%{?_krb5_prefix:1} == 0
%define _krb5_prefix /usr
%endif

%if 0%{?_vmevent_prefix:1} == 0
%define _vmevent_prefix /opt/vmware
%endif

%if 0%{?_jansson_prefix:1} == 0
%define _jansson_prefix /usr
%endif

%if 0%{?_copenapi_prefix:1} == 0
%define _copenapi_prefix /usr
%endif

%if 0%{?_oidc_prefix:1} == 0
%define _oidc_prefix /opt/vmware
%endif

%if 0%{?_lwsts_sbindir:1} == 0
%define _lwsts_sbindir %{_prefix}/sbin
%endif

%if 0%{?_lwsts_bindir:1} == 0
%define _lwsts_bindir %{_prefix}/bin
%endif

%if 0%{?_lwsts_exe_ext:1} == 0
%define _lwsts_exe_ext %{nil}
%endif

%define _sasl2dir %{_sasl_prefix}/lib64/sasl2
%define _krb5_lib_dir %{_krb5_prefix}/lib64
%define _krb5_gss_conf_dir /etc/gss
%define _logdir /var/log/lightwave
%define _integchkdir %{_logdir}/integrity
%define _logconfdir /etc/syslog-ng/lightwave.conf.d
%define _pymodulesdir /opt/vmware/site-packages/identity
%define _jreextdir /usr/java/packages/lib/ext

%define _post_dbdir         %{_localstatedir}/post
%define _vmca_dbdir         %{_localstatedir}/vmca
%define _mutentca_dbdir     %{_localstatedir}/mutentca
%define _vmdir_dbdir        %{_localstatedir}/vmdir
%define _vmafd_dbdir        %{_localstatedir}/vmafd
%define _vmsts_dbdir        %{_localstatedir}/vmsts
%define _rpcdir             %{_localstatedir}/rpc
%define _ipcdir             %{_localstatedir}/ipc
%define _lw_tmp_dir         %{_localstatedir}/lightwave_tmp

%define _vecsdir %{_vmafd_dbdir}/vecs
%define _crlsdir %{_vmafd_dbdir}/crl

%package client
Summary: Lightwave Client

Requires: openssl >= 1.0.2, coreutils >= 8.22, cyrus-sasl >= 2.1, gawk >= 4.1.3, libyaml >= 0.1.7
%if 0%{?fedora} >= 21
Requires: krb5-libs >= 1.14, sqlite >= 3.14, boost = 1.60.0, likewise-open >= 6.2.11
%else
Requires: krb5 >= 1.14
%if "%{_dist}" == ".lwph2"
Requires:  boost = 1.63.0, likewise-open = 6.2.11, sqlite-devel >= 3.19.3
%else
Requires:  boost = 1.60.0, likewise-open >= 6.2.11, sqlite-autoconf >= 3.14
%endif
%endif

%description client
Client libraries to communicate with Lightwave services

%package server
Summary: Lightwave Server
Requires: lightwave-client = %{_version}
%description server
Lightwave services

%package devel
Summary: Lightwave Client Development Library
Requires: lightwave-client = %{_version}
%description devel
Development libraries to communicate with Lightwave services

%package post
Summary: Lightwave POST Service
Requires: lightwave-client >= %{_version}
%description post
Lightwave POST service

%package mutentca
Summary: Lightwave MutentCA Service
Requires: lightwave-client >= %{_version}
%description mutentca
Lightwave MutentCA Service

%package sts
Summary: Lightwave Secure Token Server
Requires: lightwave-client >= %{_version}
%description sts
Lightwave Secure Token Server

%package test
Summary: Lightwave Test
Requires: lightwave-client >= %{_version}
%description test
Lightwave Test

%package casecurity-aws-kms
Summary: Lightwave CA security plugin using Aws KMS
Requires: aws-kms-libs >= 1.4.33
Requires: lightwave-client >= %{_version}
BuildRequires: aws-sdk-kms >= 1.4.33
%description casecurity-aws-kms
Security plugin implementing Aws KMS based envelope
encryption for private keys. This implementation
encapsulates encryption and allows key creation, sign
and verify while hiding plain text private keys from
users.

%debug_package
%build
%install

%pre server

    # First argument is 1 => New Installation
    # First argument is 2 => Upgrade

    case "$1" in
        1)
            #
            # New Installation
            #

            ;;

        2)
            #
            # Upgrade
            #
            mv %{_datadir}/config/vmdircfg.yaml %{_lw_tmp_dir}/vmdircfg.yaml
            mv %{_datadir}/config/vmcacfg.yaml  %{_lw_tmp_dir}/vmcacfg.yaml
            mv %{_datadir}/config/vmdnscfg.yaml %{_lw_tmp_dir}/vmdnscfg.yaml

            if [ ! -f /.dockerenv ]; then
                /bin/systemctl stop vmware-vmdnsd.service
                /bin/systemctl stop vmware-vmcad.service
                /bin/systemctl stop vmware-vmdird.service
                /bin/systemctl stop vmware-vmafdd.service
            fi
            ;;

    esac

%pre client
    # First argument is 1 => New Installation
    # First argument is 2 => Upgrade

    getent group lightwave >/dev/null || groupadd lightwave
    getent passwd lightwave >/dev/null || useradd -g lightwave -d / -s /sbin/nologin -c "Lightwave User" lightwave

    case "$1" in
        1)
            #
            # New Installation
            #

            ;;

        2)
            #
            # Upgrade
            #
            mv %{_datadir}/config/vmafdcfg.yaml %{_lw_tmp_dir}/vmafdcfg.yaml
            mv %{_datadir}/config/vmdircfg.yaml %{_lw_tmp_dir}/vmdircfg.yaml

            if [ ! -f /.dockerenv ]; then
                /bin/systemctl stop vmware-vmafdd.service
            fi
            ;;
    esac

%pre post

    # First argument is 1 => New Installation
    # First argument is 2 => Upgrade

    case "$1" in
        1)
            #
            # New Installation
            #

            ;;

        2)
            #
            # Upgrade
            #
            ;;
    esac

%pre mutentca

    # First argument is 1 => New Installation
    # First argument is 2 => Upgrade

    case "$1" in
        1)
            #
            # New Installation
            #
            ;;

        2)
            #
            # Upgrade
            #
            ;;
    esac

%post server

    # First argument is 1 => New Installation
    # First argument is 2 => Upgrade

    /sbin/ldconfig

    if [ ! -f /.dockerenv ]; then
        # Not in container
        # start the firewall service
        /bin/systemctl restart firewall.service
        if [ $? -ne 0 ]; then
            echo "Firewall service not restarted"
        fi
    fi

    # common
    /bin/install -d %{_logdir} -o lightwave -g lightwave -m 755
    /bin/mkdir -m 755 -p %{_logconfdir}

    lw_uid="$(id -u lightwave)"
    lw_gid="$(id -g lightwave)"

    # vmdir
    /bin/install -d %{_vmdir_dbdir} -o lightwave -g lightwave -m 700
    /bin/install -d %{_integchkdir}/reports -o lightwave -g lightwave -m 755
    /bin/install -d %{_integchkdir}/archive -o lightwave -g lightwave -m 755

    if [ -a %{_sasl2dir}/vmdird.conf ]; then
        /bin/rm %{_sasl2dir}/vmdird.conf
    fi

    # add vmdird.conf to sasl2 directory
    /bin/ln -s %{_datadir}/config/saslvmdird.conf %{_sasl2dir}/vmdird.conf

    if [ -a %{_logconfdir}/vmdird-syslog-ng.conf ]; then
        /bin/rm %{_logconfdir}/vmdird-syslog-ng.conf
    fi
    /bin/ln -s %{_datadir}/config/vmdird-syslog-ng.conf %{_logconfdir}/vmdird-syslog-ng.conf

    # vmdns
    if [ -a %{_logconfdir}/vmdnsd-syslog-ng.conf ]; then
        /bin/rm %{_logconfdir}/vmdnsd-syslog-ng.conf
    fi
    /bin/ln -s %{_datadir}/config/vmdnsd-syslog-ng.conf %{_logconfdir}/vmdnsd-syslog-ng.conf

    # vmca
    /bin/install -d %{_vmca_dbdir} -o lightwave -g lightwave -m 700

    if [ -a %{_logconfdir}/vmcad-syslog-ng.conf ]; then
        /bin/rm %{_logconfdir}/vmcad-syslog-ng.conf
    fi
    /bin/ln -s %{_datadir}/config/vmcad-syslog-ng.conf %{_logconfdir}/vmcad-syslog-ng.conf

    setcap cap_dac_read_search,cap_sys_nice,cap_sys_resource,cap_net_bind_service+ep %{_sbindir}/vmdird
    setcap cap_sys_resource,cap_net_bind_service+ep %{_sbindir}/vmdnsd
    setcap cap_dac_read_search+ep %{_sbindir}/vmcad

    case "$1" in
        1)
            #
            # New Installation
            #

            if [ ! -f /.dockerenv ]; then
                /bin/systemctl enable vmware-vmafdd.service
                /bin/systemctl enable vmware-vmdird.service
                /bin/systemctl enable vmware-vmcad.service
                /bin/systemctl enable vmware-vmdnsd.service

                /bin/systemctl daemon-reload
                # start vmdir the first time under MdbEnabelWal 0 is much faster
                %{_bindir}/lwcommon-cli regcfg set-key /vmdir/parameters/MdbEnableWal 0
                /bin/systemctl start vmware-vmdird.service
                /bin/systemctl stop vmware-vmdird.service
                # set MdbEnable 1 default state
                %{_bindir}/lwcommon-cli regcfg set-key /vmdir/parameters/MdbEnableWal 1
            fi
            ;;

        2)
            #
            # Upgrade
            #

            # Note: Upgrades are not handled in container

            mv %{_datadir}/config/vmdircfg.yaml %{_lw_tmp_dir}/vmdircfg.yaml.%{_version}.%{_patch}%{_dist}
            mv %{_datadir}/config/vmcacfg.yaml  %{_lw_tmp_dir}/vmcacfg.yaml.%{_version}.%{_patch}%{_dist}
            mv %{_datadir}/config/vmdnscfg.yaml %{_lw_tmp_dir}/vmdnscfg.yaml.%{_version}.%{_patch}%{_dist}

            cp %{_lw_tmp_dir}/vmdircfg.yaml %{_datadir}/config/vmdircfg.yaml
            cp %{_lw_tmp_dir}/vmcacfg.yaml  %{_datadir}/config/vmcacfg.yaml
            cp %{_lw_tmp_dir}/vmdnscfg.yaml %{_datadir}/config/vmdnscfg.yaml

            %{_bindir}/lwcommon-cli regcfg merge-file %{_lw_tmp_dir}/vmdircfg.yaml.%{_version}.%{_patch}%{_dist} %{_datadir}/config/vmdircfg.yaml
            %{_bindir}/lwcommon-cli regcfg merge-file %{_lw_tmp_dir}/vmcacfg.yaml.%{_version}.%{_patch}%{_dist} %{_datadir}/config/vmcacfg.yaml
            %{_bindir}/lwcommon-cli regcfg merge-file %{_lw_tmp_dir}/vmdnscfg.yaml.%{_version}.%{_patch}%{_dist} %{_datadir}/config/vmdnscfg.yaml

            chown lightwave:lightwave /var/log/lightwave/vmca.log.* >/dev/null 2>&1

            ;;
    esac

    chown -R lightwave:lightwave %{_vmca_dbdir}
    chown -R lightwave:lightwave %{_vmdir_dbdir}
    chown -R lightwave:lightwave %{_datadir}/config
    find %{_vmdir_dbdir} -type f -exec chmod 600 {} \;
    chown -R lightwave:lightwave %{_integchkdir}

    if [ ! -f /.dockerenv ]; then
        /bin/systemctl daemon-reload
        /bin/systemctl start vmware-vmafdd.service
        /bin/systemctl start vmware-vmdird.service
        /bin/systemctl start vmware-vmcad.service
        /bin/systemctl start vmware-vmdnsd.service
    fi

%post client

    # First argument is 1 => New Installation
    # First argument is 2 => Upgrade

    chown -R lightwave:lightwave %{_configdir}

    # config firewall service for server/post

    if [ ! -f /.dockerenv ]; then
        # Not in container
        /bin/systemctl enable firewall.service
        /bin/systemctl daemon-reload
        /bin/systemctl restart firewall.service
        if [ $? -ne 0 ]; then
            echo "Firewall service not restarted"
        fi
    fi

    /bin/install -d %{_logdir} -o lightwave -g lightwave -m 755

    SRP_MECH_OID="1.2.840.113554.1.2.10"
    UNIX_MECH_OID="1.3.6.1.4.1.6876.11711.2.1.2"

    # add libgssapi_srp.so to GSSAPI plugin directory
    if [ ! -h %{_krb5_lib_dir}/gss/libgssapi_srp.so ]; then
        /bin/ln -s %{_lib64dir}/libgssapi_srp.so %{_krb5_lib_dir}/gss/libgssapi_srp.so
    fi

    # Add GSSAPI SRP plugin configuration to GSS mech file
    if [ -f %{_krb5_gss_conf_dir}/mech ]; then
        if [ `grep -c  "$SRP_MECH_OID" %{_krb5_gss_conf_dir}/mech` -lt 1 ]; then
            echo "srp $SRP_MECH_OID libgssapi_srp.so" >> %{_krb5_gss_conf_dir}/mech
        fi
    fi

    # Add GSSAPI UNIX plugin configuration to GSS mech file
    if [ -f %{_krb5_gss_conf_dir}/mech ]; then
        if [ `grep -c  "$UNIX_MECH_OID" %{_krb5_gss_conf_dir}/mech` -lt 1 ]; then
            echo "#unix  $UNIX_MECH_OID libgssapi_unix.so" >> %{_krb5_gss_conf_dir}/mech
        fi
    fi

    # Restore commented out NTLM mech oid if found
    if [ `grep -c  "#ntlm " %{_krb5_gss_conf_dir}/mech` -ge 1 ]; then
        /bin/mv %{_krb5_gss_conf_dir}/mech %{_krb5_gss_conf_dir}/mech-$$
        /bin/cat %{_krb5_gss_conf_dir}/mech-$$ | sed 's|^#ntlm|ntlm|' > %{_krb5_gss_conf_dir}/mech
        if [ -s %{_krb5_gss_conf_dir}/mech ]; then
            /bin/rm %{_krb5_gss_conf_dir}/mech-$$
        fi
    fi
    chmod 644 %{_krb5_gss_conf_dir}/mech

    /bin/mkdir -m 700 -p %{_vmafd_dbdir}
    /bin/mkdir -m 700 -p %{_vecsdir}
    /bin/mkdir -m 700 -p %{_crlsdir}

    /bin/mkdir -m 700 -p %{_machinecertdir}
    chown %{_lwuser}:%{_lwgroup} %{_machinecertdir} >/dev/null 2>&1

    /bin/mkdir -m 755 -p %{_logconfdir}
    if [ -a %{_logconfdir}/vmafdd-syslog-ng.conf ]; then
        /bin/rm %{_logconfdir}/vmafdd-syslog-ng.conf
    fi
    /bin/ln -s %{_datadir}/config/vmafdd-syslog-ng.conf %{_logconfdir}/vmafdd-syslog-ng.conf

    lw_uid="$(id -u lightwave)"
    lw_gid="$(id -g lightwave)"
    lw_user_sid="S-1-22-1-$lw_uid"

    /bin/install -d %{_rpcdir} -o lightwave -g lightwave -m 755
    /bin/install -d %{_ipcdir} -o lightwave -g lightwave -m 755

    # create lightwave_tmp directory
    if [ ! -d %{_lw_tmp_dir} ]; then
        /bin/mkdir -m 700 -p %{_lw_tmp_dir}
    fi
    chown %{_lwuser}:%{_lwgroup} %{_lw_tmp_dir} >/dev/null 2>&1

    if [ ! -f /.dockerenv ]; then
        /bin/systemctl daemon-reload
    fi

    case "$1" in
        1)
            #
            # New Installation
            #

            if [ ! -f /.dockerenv ]; then
                /bin/systemctl start vmware-vmafdd.service
                /bin/systemctl restart vmware-vmafdd.service
                #sleep 2
                %{_bindir}/vecs-cli store permission --name MACHINE_SSL_CERT --user lightwave --grant read >/dev/null
            fi

            ;;

        2)
            #
            # Upgrade
            #
            mv %{_datadir}/config/vmafdcfg.yaml %{_lw_tmp_dir}/vmafdcfg.yaml.%{_version}.%{_patch}%{_dist}
            mv %{_datadir}/config/vmdircfg.yaml %{_lw_tmp_dir}/vmdircfg.yaml.%{_version}.%{_patch}%{_dist}

            cp %{_lw_tmp_dir}/vmafdcfg.yaml %{_datadir}/config/vmafdcfg.yaml
            cp %{_lw_tmp_dir}/vmdircfg.yaml %{_datadir}/config/vmdircfg.yaml

            %{_bindir}/lwcommon-cli regcfg merge-file %{_lw_tmp_dir}/vmafdcfg.yaml.%{_version}.%{_patch}%{_dist} %{_datadir}/config/vmafdcfg.yaml
            %{_bindir}/lwcommon-cli regcfg merge-file %{_lw_tmp_dir}/vmdircfg.yaml.%{_version}.%{_patch}%{_dist} %{_datadir}/config/vmdircfg.yaml

            if [ ! -f /.dockerenv ]; then
                /bin/systemctl start vmware-vmafdd.service
                /bin/systemctl restart vmware-vmafdd.service
                #sleep 2
                %{_bindir}/vecs-cli store permission --name MACHINE_SSL_CERT --user lightwave --grant read >/dev/null
            fi

            ;;
    esac

%post post

    # start the firewall service
    if [ ! -f /.dockerenv ]; then
        # Not in container
        /bin/systemctl restart firewall.service
        if [ $? -ne 0 ]; then
            echo "Firewall service not restarted"
        fi
    fi

    # make post db directory
    /bin/mkdir -m 700 -p %{_post_dbdir}

    if [ -a %{_sasl2dir}/postd.conf ]; then
        /bin/rm %{_sasl2dir}/postd.conf
    fi

    # add postd.conf to sasl2 directory
    /bin/ln -s %{_datadir}/config/saslpostd.conf %{_sasl2dir}/postd.conf

    /bin/mkdir -m 755 -p %{_logconfdir}
    if [ -a %{_logconfdir}/postd-syslog-ng.conf ]; then
        /bin/rm %{_logconfdir}/postd-syslog-ng.conf
    fi
    /bin/ln -s %{_datadir}/config/postd-syslog-ng.conf %{_logconfdir}/postd-syslog-ng.conf

    case "$1" in
        1)
            #
            # New Installation
            #
            ;;

        2)
            #
            # Upgrade
            #
            ;;
    esac

%post mutentca

    # start the firewall service
    if [ ! -f /.dockerenv ]; then
        # Not in container
        /bin/systemctl restart firewall.service
        if [ $? -ne 0 ]; then
            echo "Firewall service not restarted"
        fi
    fi

    /bin/install -d %{_mutentca_dbdir} -o lightwave -g lightwave -m 700

    if [ -a %{_logconfdir}/mutentcad-syslog-ng.conf ]; then
        /bin/rm %{_logconfdir}/mutentcad-syslog-ng.conf
    fi
    /bin/ln -s %{_datadir}/config/mutentcad-syslog-ng.conf %{_logconfdir}/mutentcad-syslog-ng.conf

    case "$1" in
        1)
            #
            # New Installation
            #
            ;;

        2)
            #
            # Upgrade
            #
            chown lightwave:lightwave /var/log/lightwave/mutentca.log.* >/dev/null 2>&1

            ;;
    esac

    chown -R lightwave:lightwave %{_mutentca_dbdir}

    setcap cap_dac_read_search+ep %{_sbindir}/mutentcad

%preun server

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

    case "$1" in
        0)
            #
            # Uninstall
            #

            /bin/systemctl >/dev/null 2>&1
            if [ $? -eq 0 ]; then
                 if [ -f /etc/systemd/system/vmware-vmdnsd.service ]; then
                     /bin/systemctl stop vmware-vmdnsd.service
                     /bin/systemctl disable vmware-vmdnsd.service
                     /bin/rm -f /etc/systemd/system/multi-user.target.wants/vmware-vmdnsd.service
                     /bin/rm -f /etc/systemd/system/vmware-vmdnsd.service
                 fi

                 if [ -f /etc/systemd/system/vmware-vmcad.service ]; then
                     /bin/systemctl stop vmware-vmcad.service
                     /bin/systemctl disable vmware-vmcad.service
                     /bin/rm -f /etc/systemd/system/multi-user.target.wants/vmware-vmcad.service
                     /bin/rm -f /etc/systemd/system/vmware-vmcad.service
                 fi

                 if [ -f /etc/systemd/system/vmware-vmdird.service ]; then
                     /bin/systemctl stop vmware-vmdird.service
                     /bin/systemctl disable vmware-vmdird.service
                     /bin/rm -f /etc/systemd/system/multi-user.target.wants/vmware-vmdird.service
                     /bin/rm -f /etc/systemd/system/vmware-vmdird.service
                 fi

                 /bin/systemctl daemon-reload
            fi

            if [ -h %{_logconfdir}/vmdird-syslog-ng.conf ]; then
                /bin/rm -f %{_logconfdir}/vmdird-syslog-ng.conf
            fi
            if [ -h %{_logconfdir}/vmcad-syslog-ng.conf ]; then
                /bin/rm -f %{_logconfdir}/vmcad-syslog-ng.conf
            fi
            if [ -h %{_logconfdir}/vmdnsd-syslog-ng.conf ]; then
                /bin/rm -f %{_logconfdir}/vmdnsd-syslog-ng.conf
            fi
            ;;

        1)
            #
            # Upgrade
            #
            ;;
    esac

%preun client

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

    case "$1" in
        0)
            #
            # Uninstall
            #
            /bin/systemctl >/dev/null 2>&1
            if [ $? -eq 0 ]; then
                 if [ -f /etc/systemd/system/vmware-vmafdd.service ]; then
                     /bin/systemctl stop vmware-vmafdd.service
                     /bin/systemctl disable vmware-vmafdd.service
                     /bin/rm -f /etc/systemd/system/multi-user.target.wants/vmware-vmafdd.service
                     /bin/rm -f /etc/systemd/system/vmware-vmafdd.service
                 fi

                 if [ -f /etc/systemd/system/firewall.service ]; then
                     /bin/systemctl stop firewall.service
                     /bin/systemctl disable firewall.service
                     /bin/rm -f /etc/systemd/system/multi-user.target.wants/firewall.service
                 fi

                 /bin/systemctl daemon-reload
            fi

            if [ -h %{_logconfdir}/vmafdd-syslog-ng.conf ]; then
                /bin/rm -f %{_logconfdir}/vmafdd-syslog-ng.conf
            fi
            ;;

        1)
            #
            # Upgrade
            #
            ;;
    esac

%preun post

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

    case "$1" in
        0)
            #
            # Uninstall
            #
            ;;

        1)
            #
            # Upgrade
            #
            ;;
    esac

%preun mutentca

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

    case "$1" in
        0)
            #
            # Uninstall
            #

            if [ -h %{_logconfdir}/mutentcad-syslog-ng.conf ]; then
                /bin/rm -f %{_logconfdir}/mutentcad-syslog-ng.conf
            fi
            ;;

        1)
            #
            # Upgrade
            #
            ;;
    esac

%postun server

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

    /sbin/ldconfig

    case "$1" in
        0)
            #
            # Uninstall
            #
            if [ -f %{_vmdir_dbdir}/data.mdb ]; then
                # backup db if exists
                mv %{_vmdir_dbdir}/data.mdb %{_vmdir_dbdir}/data.mdb.bak
            fi

            echo "Existing database files kept at [%{_vmdir_dbdir}]."

            ;;

        1)
            #
            # Upgrade
            #
            ;;
    esac

    if [ -a %{_sasl2dir}/vmdird.conf ]; then
        /bin/rm %{_sasl2dir}/vmdird.conf
    fi

%postun client

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

    /sbin/ldconfig

    case "$1" in
        0)
            #
            # Uninstall
            #

            # Un-configure SRP/UNIX mech authentication plugins
            SRP_MECH_OID="1.2.840.113554.1.2.10"
            UNIX_MECH_OID="1.3.6.1.4.1.6876.11711.2.1.2"

            # Cleanup GSSAPI SRP symlink
            if [ -h %{_libdir}/gss/libgssapi_srp.so ]; then
                rm -f %{_libdir}/gss/libgssapi_srp.so
            fi

            # Cleanup GSSAPI UNIX symlink
            if [ -h %{_libdir}/gss/libgssapi_unix.so ]; then
                rm -f %{_libdir}/gss/libgssapi_unix.so
            fi

            # Remove GSSAPI SRP plugin configuration from GSS mech file
            if [ -f %{_krb5_gss_conf_dir} ]; then
                if [ `grep -c  "$SRP_MECH_OID" %{_krb5_gss_conf_dir}` -gt 0 ]; then
                    cat %{_krb5_gss_conf_dir} | sed "/$SRP_MECH_OID/d" > "/tmp/mech-$$"
                    if [ -s /tmp/mech-$$ ]; then
                        mv "/tmp/mech-$$" %{_krb5_gss_conf_dir}
                    fi
                fi
            fi

            # Remove GSSAPI UNIX plugin configuration from GSS mech file
            if [ -f %{_krb5_gss_conf_dir} ]; then
                if [ `grep -c  "$UNIX_MECH_OID" %{_krb5_gss_conf_dir}` -gt 0 ]; then
                    cat %{_krb5_gss_conf_dir} | sed "/$UNIX_MECH_OID/d" > "/tmp/mech-$$"
                    if [ -s /tmp/mech-$$ ]; then
                        mv "/tmp/mech-$$" %{_krb5_gss_conf_dir}
                    fi
                fi
            fi

            # Cleanup vmafd db and files
            if [ -d %{_vmafd_dbdir} ]; then
                rm -rf %{_vmafd_dbdir}
            fi

            ;;

        1)
            #
            # Upgrade
            #
            ;;
    esac

%postun post

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

    /sbin/ldconfig

    case "$1" in
        0)
            #
            # Uninstall
            #
            echo "Existing database files kept at [%{_post_dbdir}]."
            ;;

        1)
            #
            # Upgrade
            #
            ;;
    esac

    if [ -a %{_sasl2dir}/postd.conf ]; then
        /bin/rm %{_sasl2dir}/postd.conf
    fi

%files server

%defattr(-,lightwave,lightwave,0755)

%{_bindir}/ic-promote
%{_bindir}/configure-lightwave-server
%{_bindir}/vdcadmintool
%{_bindir}/vdcrepadmin
%{_bindir}/unix_srp
%{_bindir}/vmkdc_admin
%{_bindir}/vdcmetric
%{_bindir}/run_backup.sh
%{_bindir}/lw_backup.sh
%{_bindir}/aws_backup_common.sh
%{_bindir}/lw_mdb_walflush
%{_bindir}/lw_restore.sh
%{_bindir}/aws_restore_common.sh
%{_bindir}/mdb_compact.sh
%{_bindir}/mdb_verify_checksum

%{_sbindir}/vmcad
%{_sbindir}/vmware-vmcad.sh
%{_sbindir}/vmdird
%{_sbindir}/vmware-vmdird.sh
%{_sbindir}/vmdnsd
%{_sbindir}/vmware-vmdnsd.sh

%{_lib64dir}/libvmkdcserv.so*
%{_lib64dir}/sasl2/libsaslvmdirdb.so*
%{_lib64dir}/libvmdirmdb.so*

%{_datadir}/config/vmcacfg.yaml
%{_datadir}/config/vmcad-syslog-ng.conf
%{_datadir}/config/vmca-rest-v2.json
%{_datadir}/config/vmca-telegraf.conf

%{_datadir}/config/saslvmdird.conf
%{_datadir}/config/vmdircfg.yaml
%{_datadir}/config/vmdirschema.ldif
%{_datadir}/config/vmdird-syslog-ng.conf
%{_datadir}/config/vmdir-rest.json
%{_datadir}/config/vmdir-rest-api.json
%{_datadir}/config/vmdir-telegraf.conf

%{_datadir}/config/vmdnscfg.yaml
%{_datadir}/config/vmdns-rest.json
%{_datadir}/config/vmdnsd-syslog-ng.conf
%{_datadir}/config/vmdns-telegraf.conf

%{_configdir}/lw-firewall-server.json

%{_servicedir}/vmware-vmdird.service
%{_servicedir}/vmware-vmafdd.service
%{_servicedir}/vmware-vmcad.service
%{_servicedir}/vmware-vmdnsd.service

%files client

%defattr(-,lightwave,lightwave)

%{_bindir}/ic-join
%{_bindir}/lightwave
%{_bindir}/cdc-cli
%{_bindir}/certool
%{_bindir}/dir-cli
%{_bindir}/domainjoin
%{_bindir}/domainjoin.sh
%{_bindir}/lw-certool
%{_bindir}/lw-support-bundle.sh
%{_bindir}/sl-cli
%{_bindir}/vmafd-cli
%{_bindir}/vmdns-cli
%{_bindir}/vdcaclmgr
%{_bindir}/vdcpromo
%{_bindir}/vdcschema
%{_bindir}/postschema
%{_bindir}/vecs-cli
%{_bindir}/lwcommon-cli
%{_lib64dir}/libkrb5crypto.so*
%{_lib64dir}/libcsrp.so*

%{_sbindir}/vmafdd
%{_sbindir}/vmware-vmafdd.sh

%{_lib64dir}/libvecsjni.so*
%{_lib64dir}/libcdcjni.so*
%{_lib64dir}/libheartbeatjni.so*
%{_lib64dir}/libvmafcfgapi.so*
%{_lib64dir}/libvmafdclient.so*
%{_lib64dir}/libvmeventclient.so*
%{_lib64dir}/libvmcaclient.so*
%{_lib64dir}/libvmdirclient.so*
%{_lib64dir}/libgssapi_ntlm.so*
%{_lib64dir}/libgssapi_srp.so*
%{_lib64dir}/libgssapi_unix.so*
%{_lib64dir}/libvmdnsclient.so*
%{_lib64dir}/libcfgutils.so*
%{_lib64dir}/libpostclient.so*
%{_lib64dir}/libssoafdclient.so*
%{_lib64dir}/libssocommon.so*
%{_lib64dir}/libssocoreclient.so*
%{_lib64dir}/libssoidmclient.so*
%{_lib64dir}/libssooidc.so*
%{_lib64dir}/libssovmdirclient.so*
%{_lib64dir}/libvmcommon.so*

%{_datadir}/config/java.security.linux
%{_datadir}/config/certool.cfg
%{_datadir}/config/vmafdcfg.yaml
%{_datadir}/config/vmdircfg.yaml
%{_datadir}/config/vmcacfg.yaml
%{_datadir}/config/vmdnscfg.yaml
%{_datadir}/config/vmafdd-syslog-ng.conf
%{_datadir}/config/telegraf.conf
%{_datadir}/config/vmafd-telegraf.conf

%{_jreextdir}/vmware-endpoint-certificate-store.jar
%{_jreextdir}/client-domain-controller-cache.jar
%{_jreextdir}/afd-heartbeat-service.jar

%{_jarsdir}/authentication-framework.jar
%{_jarsdir}/vmware-vmca-client.jar

%{_configdir}/lw-firewall-client.json
%{_configdir}/setfirewallrules.py
%{_configdir}/lightwave-syslog-logrotate.conf

%{_servicedir}/firewall.service
%{_servicedir}/vmware-vmafdd.service

%{_sysconfdir}/vmware/java/vmware-override-java.security

%files post

%defattr(-,root,root)

%{_sbindir}/postd

%{_bindir}/postadmintool
%{_bindir}/postaclmgr
%{_bindir}/post-cli
%{_bindir}/mdb_stat
%{_bindir}/mdb_verify_checksum
%{_bindir}/mdb_walflush
%{_bindir}/run_backup.sh
%{_bindir}/lw_backup.sh
%{_bindir}/aws_backup_common.sh
%{_bindir}/post_aws_restore_common.sh
%{_bindir}/post_restore.sh

%{_lib64dir}/sasl2/libsaslpostdb.so*
%{_lib64dir}/libvmdirmdb.so*

%{_datadir}/config/saslpostd.conf
%{_datadir}/config/postschema.ldif
%{_datadir}/config/post-rest.json
%{_datadir}/config/post.reg
%{_datadir}/config/postd-syslog-ng.conf
%{_datadir}/config/post-client.reg
%{_datadir}/config/post-telegraf.conf

%{_configdir}/lw-firewall-post.json

%config %attr(750, root, root) %{_datadir}/config/refresh-resolve-conf.sh
%config %attr(750, root, root) %{_datadir}/config/post-demote-deads.sh
%config %attr(750, root, root) %{_datadir}/config/monitor-core-dump.sh

%files mutentca

%defattr(-,root,root)

%{_sbindir}/mutentcad

%{_datadir}/config/mutentca.reg
%{_datadir}/config/mutentcaconfig.json
%{_datadir}/config/mutentca-policy.json
%{_datadir}/config/mutentca-rest.json
%{_datadir}/config/mutentca-metrics-rest.json
%{_datadir}/config/mutentca-post.json
%{_datadir}/config/mutentca-schema.ldif
%{_datadir}/config/mutentcad-syslog-ng.conf
%{_datadir}/config/mutentca-telegraf.conf
%{_lib64dir}/libmutentcasrvpluginpost.so
%{_configdir}/lw-firewall-mutentca.json

%files devel

%defattr(-,root,root)

%{_includedir}/vmafd.h
%{_includedir}/vmafdtypes.h
%{_includedir}/vmafdclient.h
%{_includedir}/vecsclient.h
%{_includedir}/cdcclient.h
%{_includedir}/vmsuperlogging.h
%{_includedir}/vmca.h
%{_includedir}/vmcatypes.h
%{_includedir}/vmdir.h
%{_includedir}/vmdirauth.h
%{_includedir}/vmdirclient.h
%{_includedir}/vmdirerrors.h
%{_includedir}/vmdirtypes.h
%{_includedir}/vmdns.h
%{_includedir}/vmdnstypes.h
%{_includedir}/vmmetrics.h
%{_includedir}/vmhttpclient.h
%{_includedir}/vmmemory.h
%{_includedir}/vmutil.h
%{_includedir}/mutentca.h
%{_includedir}/mutentcadb.h
%{_includedir}/mutentcaauthz.h

%{_lib64dir}/libcdcjni.a
%{_lib64dir}/libcdcjni.la
%{_lib64dir}/libvecsjni.a
%{_lib64dir}/libvecsjni.la
%{_lib64dir}/libheartbeatjni.a
%{_lib64dir}/libheartbeatjni.la
%{_lib64dir}/libvmafdclient.a
%{_lib64dir}/libvmafdclient.la
%{_lib64dir}/libvmafcfgapi.a
%{_lib64dir}/libvmafcfgapi.la
%{_lib64dir}/libvmeventclient.a
%{_lib64dir}/libvmeventclient.la
%{_lib64dir}/libvmcaclient.a
%{_lib64dir}/libvmcaclient.la
%{_lib64dir}/libvmdirclient.a
%{_lib64dir}/libvmdirclient.la
%{_lib64dir}/libvmdnsclient.a
%{_lib64dir}/libvmdnsclient.la
%{_lib64dir}/libvmcommon.a
%{_lib64dir}/libvmcommon.la

%{_includedir}/oidc.h
%{_includedir}/oidc_types.h
%{_includedir}/ssoafdclient.h
%{_includedir}/ssocoreclient.h
%{_includedir}/ssoerrors.h
%{_includedir}/ssoidmclient.h
%{_includedir}/ssotypes.h
%{_includedir}/ssocommon.h
%{_includedir}/ssovmdirclient.h
%{_includedir}/vmevent.h

%exclude %{_bindir}/vdcvmdirpromo
%exclude %{_bindir}/vmdirclienttest
%exclude %{_bindir}/*test

%exclude %{_lib64dir}/*.la
%exclude %{_lib64dir}/*.a
%exclude %{_lib64dir}/sasl2/*.a
%exclude %{_lib64dir}/sasl2/*.la
%exclude %{_lib64dir}/libcommonunittests.*

%exclude %{_prefix}/site-packages/identity/*
%exclude %{_webappsdir}/openidconnect-sample-rp.war

%files sts
%defattr(-,root,root,0750)

%{_lwsts_sbindir}/stssrv%{_lwsts_exe_ext}
%{_lwsts_bindir}/stssetup%{_lwsts_exe_ext}

%config %attr(0750, root, root) %{_lwsts_sbindir}/stssrv%{_lwsts_exe_ext}
%config %attr(0750, root, root) %{_lwsts_bindir}/stssetup%{_lwsts_exe_ext}

%files test

%defattr(-,root,root)
%{_vmdirtestbindir}/vmdir_test_runner
%{_vmdirtestlibdir}/libsecuritydescriptortests.*
%{_vmdirtestlibdir}/libmisctests.*
%{_vmdirtestlibdir}/libmultitenancytests.*
%{_vmdirtestlibdir}/libpasswordapistests.*
%{_vmdirtestlibdir}/libsearchtests.*
%{_vmdirtestlibdir}/libppolicytests.*

%files casecurity-aws-kms
%defattr(-,root,root)
%{_lib64dir}/liblwca_security_aws_kms.so
%{_datadir}/config/casecurity-aws-kms.json

# %doc ChangeLog README COPYING

%changelog
