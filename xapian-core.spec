#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x18147B073BAD2B07 (olly@debian.org)
#
Name     : xapian-core
Version  : 1.4.20
Release  : 13
URL      : https://oligarchy.co.uk/xapian/1.4.20/xapian-core-1.4.20.tar.xz
Source0  : https://oligarchy.co.uk/xapian/1.4.20/xapian-core-1.4.20.tar.xz
Source1  : https://oligarchy.co.uk/xapian/1.4.20/xapian-core-1.4.20.tar.xz.asc
Summary  : The Xapian Search Engine Library
Group    : Development/Tools
License  : GPL-2.0
Requires: xapian-core-bin = %{version}-%{release}
Requires: xapian-core-data = %{version}-%{release}
Requires: xapian-core-lib = %{version}-%{release}
Requires: xapian-core-license = %{version}-%{release}
Requires: xapian-core-man = %{version}-%{release}
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)

%description
Xapian is a highly adaptable toolkit which allows developers to easily
add advanced indexing and search facilities to their own applications.
It has built-in support for several families of weighting models and
also supports a rich set of boolean query operators.

%package bin
Summary: bin components for the xapian-core package.
Group: Binaries
Requires: xapian-core-data = %{version}-%{release}
Requires: xapian-core-license = %{version}-%{release}

%description bin
bin components for the xapian-core package.


%package data
Summary: data components for the xapian-core package.
Group: Data

%description data
data components for the xapian-core package.


%package dev
Summary: dev components for the xapian-core package.
Group: Development
Requires: xapian-core-lib = %{version}-%{release}
Requires: xapian-core-bin = %{version}-%{release}
Requires: xapian-core-data = %{version}-%{release}
Provides: xapian-core-devel = %{version}-%{release}
Requires: xapian-core = %{version}-%{release}

%description dev
dev components for the xapian-core package.


%package doc
Summary: doc components for the xapian-core package.
Group: Documentation
Requires: xapian-core-man = %{version}-%{release}

%description doc
doc components for the xapian-core package.


%package lib
Summary: lib components for the xapian-core package.
Group: Libraries
Requires: xapian-core-data = %{version}-%{release}
Requires: xapian-core-license = %{version}-%{release}

%description lib
lib components for the xapian-core package.


%package license
Summary: license components for the xapian-core package.
Group: Default

%description license
license components for the xapian-core package.


%package man
Summary: man components for the xapian-core package.
Group: Default

%description man
man components for the xapian-core package.


%prep
%setup -q -n xapian-core-1.4.20
cd %{_builddir}/xapian-core-1.4.20

%build
## build_prepend content
# Avoid detection of zlib invalid read by not running test suite through valgrind.
# Reference: https://github.com/jtkukunas/zlib/pull/32
export VALGRIND=""
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657041972
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1657041972
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xapian-core
cp %{_builddir}/xapian-core-1.4.20/COPYING %{buildroot}/usr/share/package-licenses/xapian-core/4d1d37f306ed270cda5b2741fac3abf0a7b012e5
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/copydatabase
/usr/bin/quest
/usr/bin/simpleexpand
/usr/bin/simpleindex
/usr/bin/simplesearch
/usr/bin/xapian-check
/usr/bin/xapian-compact
/usr/bin/xapian-config
/usr/bin/xapian-delve
/usr/bin/xapian-metadata
/usr/bin/xapian-pos
/usr/bin/xapian-progsrv
/usr/bin/xapian-replicate
/usr/bin/xapian-replicate-server
/usr/bin/xapian-tcpsrv

%files data
%defattr(-,root,root,-)
/usr/share/xapian-core/stopwords/arabic.list
/usr/share/xapian-core/stopwords/danish.list
/usr/share/xapian-core/stopwords/dutch.list
/usr/share/xapian-core/stopwords/english.list
/usr/share/xapian-core/stopwords/finnish.list
/usr/share/xapian-core/stopwords/french.list
/usr/share/xapian-core/stopwords/german.list
/usr/share/xapian-core/stopwords/hungarian.list
/usr/share/xapian-core/stopwords/indonesian.list
/usr/share/xapian-core/stopwords/italian.list
/usr/share/xapian-core/stopwords/norwegian.list
/usr/share/xapian-core/stopwords/portuguese.list
/usr/share/xapian-core/stopwords/russian.list
/usr/share/xapian-core/stopwords/spanish.list
/usr/share/xapian-core/stopwords/swedish.list

%files dev
%defattr(-,root,root,-)
/usr/include/xapian.h
/usr/include/xapian/attributes.h
/usr/include/xapian/compactor.h
/usr/include/xapian/constants.h
/usr/include/xapian/constinfo.h
/usr/include/xapian/database.h
/usr/include/xapian/dbfactory.h
/usr/include/xapian/deprecated.h
/usr/include/xapian/derefwrapper.h
/usr/include/xapian/document.h
/usr/include/xapian/enquire.h
/usr/include/xapian/error.h
/usr/include/xapian/errorhandler.h
/usr/include/xapian/eset.h
/usr/include/xapian/expanddecider.h
/usr/include/xapian/geospatial.h
/usr/include/xapian/intrusive_ptr.h
/usr/include/xapian/iterator.h
/usr/include/xapian/keymaker.h
/usr/include/xapian/matchspy.h
/usr/include/xapian/mset.h
/usr/include/xapian/positioniterator.h
/usr/include/xapian/postingiterator.h
/usr/include/xapian/postingsource.h
/usr/include/xapian/query.h
/usr/include/xapian/queryparser.h
/usr/include/xapian/registry.h
/usr/include/xapian/stem.h
/usr/include/xapian/termgenerator.h
/usr/include/xapian/termiterator.h
/usr/include/xapian/types.h
/usr/include/xapian/unicode.h
/usr/include/xapian/valueiterator.h
/usr/include/xapian/valuesetmatchdecider.h
/usr/include/xapian/version.h
/usr/include/xapian/visibility.h
/usr/include/xapian/weight.h
/usr/lib64/cmake/xapian/xapian-config-version.cmake
/usr/lib64/cmake/xapian/xapian-config.cmake
/usr/lib64/libxapian.so
/usr/lib64/pkgconfig/xapian-core.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/xapian\-core/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxapian.so.30
/usr/lib64/libxapian.so.30.12.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xapian-core/4d1d37f306ed270cda5b2741fac3abf0a7b012e5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/copydatabase.1
/usr/share/man/man1/quest.1
/usr/share/man/man1/xapian-check.1
/usr/share/man/man1/xapian-compact.1
/usr/share/man/man1/xapian-config.1
/usr/share/man/man1/xapian-delve.1
/usr/share/man/man1/xapian-metadata.1
/usr/share/man/man1/xapian-pos.1
/usr/share/man/man1/xapian-progsrv.1
/usr/share/man/man1/xapian-replicate-server.1
/usr/share/man/man1/xapian-replicate.1
/usr/share/man/man1/xapian-tcpsrv.1
