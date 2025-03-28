#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : libxfce4util
Version  : 4.20.1
Release  : 42
URL      : https://archive.xfce.org/src/xfce/libxfce4util/4.20/libxfce4util-4.20.1.tar.bz2
Source0  : https://archive.xfce.org/src/xfce/libxfce4util/4.20/libxfce4util-4.20.1.tar.bz2
Summary  : Utility library for the Xfce 4 desktop environment
Group    : Development/Tools
License  : LGPL-2.0
Requires: libxfce4util-bin = %{version}-%{release}
Requires: libxfce4util-data = %{version}-%{release}
Requires: libxfce4util-lib = %{version}-%{release}
Requires: libxfce4util-license = %{version}-%{release}
Requires: libxfce4util-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : vala
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Account-for-usr-share-xdg-xfce4.patch

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/xfce/libxfce4util/COPYING)

%package bin
Summary: bin components for the libxfce4util package.
Group: Binaries
Requires: libxfce4util-data = %{version}-%{release}
Requires: libxfce4util-license = %{version}-%{release}

%description bin
bin components for the libxfce4util package.


%package data
Summary: data components for the libxfce4util package.
Group: Data

%description data
data components for the libxfce4util package.


%package dev
Summary: dev components for the libxfce4util package.
Group: Development
Requires: libxfce4util-lib = %{version}-%{release}
Requires: libxfce4util-bin = %{version}-%{release}
Requires: libxfce4util-data = %{version}-%{release}
Provides: libxfce4util-devel = %{version}-%{release}
Requires: libxfce4util = %{version}-%{release}

%description dev
dev components for the libxfce4util package.


%package doc
Summary: doc components for the libxfce4util package.
Group: Documentation

%description doc
doc components for the libxfce4util package.


%package lib
Summary: lib components for the libxfce4util package.
Group: Libraries
Requires: libxfce4util-data = %{version}-%{release}
Requires: libxfce4util-license = %{version}-%{release}

%description lib
lib components for the libxfce4util package.


%package license
Summary: license components for the libxfce4util package.
Group: Default

%description license
license components for the libxfce4util package.


%package locales
Summary: locales components for the libxfce4util package.
Group: Default

%description locales
locales components for the libxfce4util package.


%prep
%setup -q -n libxfce4util-4.20.1
cd %{_builddir}/libxfce4util-4.20.1
%patch -P 1 -p1
pushd ..
cp -a libxfce4util-4.20.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742827982
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742827982
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libxfce4util
cp %{_builddir}/libxfce4util-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libxfce4util/3cc956929ff9e4c1c89a2c826cdc7fec5e0b21ab || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang libxfce4util
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xfce4-kiosk-query
/usr/bin/xfce4-kiosk-query

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Libxfce4util-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/xfce4/libxfce4util/libxfce4util-config.h
/usr/include/xfce4/libxfce4util/libxfce4util.h
/usr/include/xfce4/libxfce4util/xfce-consolekit.h
/usr/include/xfce4/libxfce4util/xfce-debug.h
/usr/include/xfce4/libxfce4util/xfce-fileutils.h
/usr/include/xfce4/libxfce4util/xfce-generics.h
/usr/include/xfce4/libxfce4util/xfce-gio-extensions.h
/usr/include/xfce4/libxfce4util/xfce-i18n.h
/usr/include/xfce4/libxfce4util/xfce-kiosk.h
/usr/include/xfce4/libxfce4util/xfce-license.h
/usr/include/xfce4/libxfce4util/xfce-miscutils.h
/usr/include/xfce4/libxfce4util/xfce-posix-signal-handler.h
/usr/include/xfce4/libxfce4util/xfce-rc.h
/usr/include/xfce4/libxfce4util/xfce-resource.h
/usr/include/xfce4/libxfce4util/xfce-string.h
/usr/include/xfce4/libxfce4util/xfce-systemd.h
/usr/include/xfce4/libxfce4util/xfce-utf8.h
/usr/lib64/libxfce4util.so
/usr/lib64/pkgconfig/libxfce4util-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libxfce4util/XfceConsolekit.html
/usr/share/gtk-doc/html/libxfce4util/XfceSystemd.html
/usr/share/gtk-doc/html/libxfce4util/annotation-glossary.html
/usr/share/gtk-doc/html/libxfce4util/api-index-full.html
/usr/share/gtk-doc/html/libxfce4util/ch01.html
/usr/share/gtk-doc/html/libxfce4util/home.png
/usr/share/gtk-doc/html/libxfce4util/index.html
/usr/share/gtk-doc/html/libxfce4util/left-insensitive.png
/usr/share/gtk-doc/html/libxfce4util/left.png
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-File-Utilities.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-GIO-Extensions.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Internationalisation.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Miscellaneous-Utilities.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-POSIX-Signal-Handling.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Resource-Config-File-Support.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Resource-lookup-functions.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Software-Licenses.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Unicode-Support-Functions.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Version-Information.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Xfce-Generics.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Xfce-Kiosk-functions.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-Xfce-String-Functions.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util.devhelp2
/usr/share/gtk-doc/html/libxfce4util/object-tree.html
/usr/share/gtk-doc/html/libxfce4util/right-insensitive.png
/usr/share/gtk-doc/html/libxfce4util/right.png
/usr/share/gtk-doc/html/libxfce4util/style.css
/usr/share/gtk-doc/html/libxfce4util/up-insensitive.png
/usr/share/gtk-doc/html/libxfce4util/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libxfce4util.so.7.0.0
/usr/lib64/libxfce4util.so.7
/usr/lib64/libxfce4util.so.7.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libxfce4util/3cc956929ff9e4c1c89a2c826cdc7fec5e0b21ab

%files locales -f libxfce4util.lang
%defattr(-,root,root,-)

