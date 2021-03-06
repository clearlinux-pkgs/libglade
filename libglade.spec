#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libglade
Version  : 2.6.4
Release  : 8
URL      : http://ftp.gnome.org/pub/GNOME/sources/libglade/2.6/libglade-2.6.4.tar.bz2
Source0  : http://ftp.gnome.org/pub/GNOME/sources/libglade/2.6/libglade-2.6.4.tar.bz2
Summary  : libglade library
Group    : Development/Tools
License  : LGPL-2.0
Requires: libglade-data = %{version}-%{release}
Requires: libglade-lib = %{version}-%{release}
Requires: libglade-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libxml-2.0)

%description
This library allows you to load user interfaces in your program, which are
stored externally.  This allows alteration of the interface without
recompilation of the program.

The interfaces can also be edited with GLADE.

%package data
Summary: data components for the libglade package.
Group: Data

%description data
data components for the libglade package.


%package dev
Summary: dev components for the libglade package.
Group: Development
Requires: libglade-lib = %{version}-%{release}
Requires: libglade-data = %{version}-%{release}
Provides: libglade-devel = %{version}-%{release}
Requires: libglade = %{version}-%{release}

%description dev
dev components for the libglade package.


%package doc
Summary: doc components for the libglade package.
Group: Documentation

%description doc
doc components for the libglade package.


%package lib
Summary: lib components for the libglade package.
Group: Libraries
Requires: libglade-data = %{version}-%{release}
Requires: libglade-license = %{version}-%{release}

%description lib
lib components for the libglade package.


%package license
Summary: license components for the libglade package.
Group: Default

%description license
license components for the libglade package.


%prep
%setup -q -n libglade-2.6.4
cd %{_builddir}/libglade-2.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604624184
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1604624184
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libglade
cp %{_builddir}/libglade-2.6.4/COPYING %{buildroot}/usr/share/package-licenses/libglade/5fb362ef1680e635fe5fb212b55eef4db9ead48f
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/libglade-convert

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xml/libglade/glade-2.0.dtd

%files dev
%defattr(-,root,root,-)
/usr/include/libglade-2.0/glade/glade-build.h
/usr/include/libglade-2.0/glade/glade-init.h
/usr/include/libglade-2.0/glade/glade-parser.h
/usr/include/libglade-2.0/glade/glade-xml.h
/usr/include/libglade-2.0/glade/glade.h
/usr/lib64/libglade-2.0.so
/usr/lib64/pkgconfig/libglade-2.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libglade/GladeXML.html
/usr/share/gtk-doc/html/libglade/home.png
/usr/share/gtk-doc/html/libglade/index.html
/usr/share/gtk-doc/html/libglade/index.sgml
/usr/share/gtk-doc/html/libglade/left.png
/usr/share/gtk-doc/html/libglade/libglade-Libglade-Build.html
/usr/share/gtk-doc/html/libglade/libglade-Libglade-Initialisation.html
/usr/share/gtk-doc/html/libglade/libglade-Libglade-SAX-Parser.html
/usr/share/gtk-doc/html/libglade/libglade-dtd-exceptions.html
/usr/share/gtk-doc/html/libglade/libglade-dtd.html
/usr/share/gtk-doc/html/libglade/libglade-embedding.html
/usr/share/gtk-doc/html/libglade/libglade-extending.html
/usr/share/gtk-doc/html/libglade/libglade-i18n.html
/usr/share/gtk-doc/html/libglade/libglade-lib.html
/usr/share/gtk-doc/html/libglade/libglade-modules.html
/usr/share/gtk-doc/html/libglade/libglade-notes.html
/usr/share/gtk-doc/html/libglade/libglade.devhelp
/usr/share/gtk-doc/html/libglade/libglade.devhelp2
/usr/share/gtk-doc/html/libglade/right.png
/usr/share/gtk-doc/html/libglade/style.css
/usr/share/gtk-doc/html/libglade/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libglade-2.0.so.0
/usr/lib64/libglade-2.0.so.0.0.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libglade/5fb362ef1680e635fe5fb212b55eef4db9ead48f
