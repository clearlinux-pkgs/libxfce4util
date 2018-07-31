#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libxfce4util
Version  : 4.13.2
Release  : 20
URL      : http://archive.xfce.org/src/xfce/libxfce4util/4.13/libxfce4util-4.13.2.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/libxfce4util/4.13/libxfce4util-4.13.2.tar.bz2
Summary  : Utility library for the Xfce 4 desktop environment
Group    : Development/Tools
License  : LGPL-2.0
Requires: libxfce4util-bin
Requires: libxfce4util-lib
Requires: libxfce4util-license
Requires: libxfce4util-locales
Requires: libxfce4util-data
BuildRequires : docbook-xml
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
Patch1: 0001-Account-for-usr-share-xdg-xfce4.patch

%description
$Id$
Basic utility library for Xfce4.
Installation:
-------------
Simply run
./configure
make
make install
For a list of available configure options, see the list as returned
by

%package bin
Summary: bin components for the libxfce4util package.
Group: Binaries
Requires: libxfce4util-data
Requires: libxfce4util-license

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
Requires: libxfce4util-lib
Requires: libxfce4util-bin
Requires: libxfce4util-data
Provides: libxfce4util-devel

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
Requires: libxfce4util-data
Requires: libxfce4util-license

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
%setup -q -n libxfce4util-4.13.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533057675
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1533057675
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libxfce4util
cp COPYING %{buildroot}/usr/share/doc/libxfce4util/COPYING
%make_install
%find_lang libxfce4util

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-kiosk-query

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/libxfce4util-1.0.typelib
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
%defattr(-,root,root,-)
/usr/share/doc/libxfce4util/COPYING

%files locales -f libxfce4util.lang
%defattr(-,root,root,-)

