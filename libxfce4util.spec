#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libxfce4util
Version  : 4.16.0
Release  : 35
URL      : http://archive.xfce.org/src/xfce/libxfce4util/4.16/libxfce4util-4.16.0.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/libxfce4util/4.16/libxfce4util-4.16.0.tar.bz2
Summary  : Utility library for the Xfce 4 desktop environment
Group    : Development/Tools
License  : LGPL-2.0
Requires: libxfce4util-bin = %{version}-%{release}
Requires: libxfce4util-data = %{version}-%{release}
Requires: libxfce4util-lib = %{version}-%{release}
Requires: libxfce4util-license = %{version}-%{release}
Requires: libxfce4util-locales = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : vala
Patch1: 0001-Account-for-usr-share-xdg-xfce4.patch

%description
TBD!!

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
%setup -q -n libxfce4util-4.16.0
cd %{_builddir}/libxfce4util-4.16.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609173885
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1609173885
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libxfce4util
cp %{_builddir}/libxfce4util-4.16.0/COPYING %{buildroot}/usr/share/package-licenses/libxfce4util/83ba6546e00f890f3a26a9bedd264084f8527d5e
%make_install
%find_lang libxfce4util

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-kiosk-query

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Libxfce4util-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/xfce4/libxfce4util/libxfce4util-config.h
/usr/include/xfce4/libxfce4util/libxfce4util.h
/usr/include/xfce4/libxfce4util/xfce-debug.h
/usr/include/xfce4/libxfce4util/xfce-fileutils.h
/usr/include/xfce4/libxfce4util/xfce-generics.h
/usr/include/xfce4/libxfce4util/xfce-i18n.h
/usr/include/xfce4/libxfce4util/xfce-kiosk.h
/usr/include/xfce4/libxfce4util/xfce-license.h
/usr/include/xfce4/libxfce4util/xfce-miscutils.h
/usr/include/xfce4/libxfce4util/xfce-posix-signal-handler.h
/usr/include/xfce4/libxfce4util/xfce-rc.h
/usr/include/xfce4/libxfce4util/xfce-resource.h
/usr/include/xfce4/libxfce4util/xfce-utf8.h
/usr/lib64/libxfce4util.so
/usr/lib64/pkgconfig/libxfce4util-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libxfce4util/annotation-glossary.html
/usr/share/gtk-doc/html/libxfce4util/home.png
/usr/share/gtk-doc/html/libxfce4util/index.html
/usr/share/gtk-doc/html/libxfce4util/left-insensitive.png
/usr/share/gtk-doc/html/libxfce4util/left.png
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-File-Utilities.html
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
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-core.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-datatypes.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-fundamentals.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util-utilities.html
/usr/share/gtk-doc/html/libxfce4util/libxfce4util.devhelp2
/usr/share/gtk-doc/html/libxfce4util/reference.html
/usr/share/gtk-doc/html/libxfce4util/right-insensitive.png
/usr/share/gtk-doc/html/libxfce4util/right.png
/usr/share/gtk-doc/html/libxfce4util/style.css
/usr/share/gtk-doc/html/libxfce4util/up-insensitive.png
/usr/share/gtk-doc/html/libxfce4util/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxfce4util.so.7
/usr/lib64/libxfce4util.so.7.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libxfce4util/83ba6546e00f890f3a26a9bedd264084f8527d5e

%files locales -f libxfce4util.lang
%defattr(-,root,root,-)

