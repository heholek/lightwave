bin_PROGRAMS = testmutentcaapi

check_PROGRAMS = testmutentcaapi
TESTS = testmutentcaapi

SUBDIRS = \
    test-mutentca-config

testmutentcaapi_SOURCES = \
    ca.c \
    main.c

testmutentcaapi_CPPFLAGS = \
    -I$(top_srcdir)/mutentca/include \
    -I$(top_srcdir)/mutentca/include/public \
    -I$(top_srcdir)/mutentca/server/include \
    @LW_INCLUDES@

testmutentcaapi_LDADD = \
    $(top_builddir)/mutentca/common/libcommon.la \
    $(top_builddir)/mutentca/server/common/libmutentcasrvcommon.la \
    $(top_builddir)/mutentca/server/db/libmutentcadb.la \
    $(top_builddir)/mutentca/server/authz/libmutentcaauthz.la \
    $(top_builddir)/mutentca/server/policy/libmutentcapolicy.la \
    $(top_builddir)/mutentca/server/api/libmutentcaapi.la \
    $(top_builddir)/mutentca/server/metrics/libmutentcametrics.la \
    @PTHREAD_LIBS@ \
    @JANSSON_LIBS@ \
    @CRYPTO_LIBS@ \
    @CMOCKA_LIBS@

testmutentcaapi_LDFLAGS = \
    @OPENSSL_LDFLAGS@ \
    @LW_LDFLAGS@ \
    @JANSSON_LDFLAGS@ \
    -Wl,--wrap,LwCADbAddCA \
    -Wl,--wrap,LwCADbCheckCA \
    -Wl,--wrap,LwCADbGetCACertificates \
    -Wl,--wrap,LwCADbGetCA \
    -Wl,--wrap,LwCASecurityAddKeyPair \
    -Wl,--wrap,LwCASecurityCreateKeyPair \
    -Wl,--wrap,LwCASecurityGetEncryptedKey \
    -Wl,--wrap,LwCASecuritySignX509Cert \
    -Wl,--wrap,LwCASecuritySignX509Request \
    -Wl,--wrap,LwCASecuritySignX509Crl \
    -Wl,--wrap,LwCADbCheckCertData \
    -Wl,--wrap,LwCADbGetCAStatus \
    -Wl,--wrap,LwCADbGetCAAuthBlob \
    -Wl,--wrap,LwCADbGetCACRLNumber \
    -Wl,--wrap,LwCADbLockCA \
    -Wl,--wrap,LwCADbUnlockCA \
    -Wl,--wrap,LwCADbLockCert \
    -Wl,--wrap,LwCADbUnlockCert \
    -Wl,--wrap,LwCADbUpdateCA \
    -Wl,--wrap,LwCADbAddCertData \
    -Wl,--wrap,LwCADbGetCertData \
    -Wl,--wrap,LwCADbGetParentCAId \
    -Wl,--wrap,LwCADbUpdateCAStatus \
    -Wl,--wrap,LwCAPolicyValidate \
    -Wl,--wrap,LwCAAuthZCheckAccess \
    -Wl,--wrap,LwCAPolicyGetCertDuration
