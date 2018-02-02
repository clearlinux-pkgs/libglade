#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libglade
Version  : 2.6.4
Release  : 2
URL      : http://ftp.gnome.org/pub/GNOME/sources/libglade/2.6/libglade-2.6.4.tar.bz2
Source0  : http://ftp.gnome.org/pub/GNOME/sources/libglade/2.6/libglade-2.6.4.tar.bz2
Summary  : libglade library
Group    : Development/Tools
License  : LGPL-2.0
Requires: libglade-bin
Requires: libglade-lib
Requires: libglade-doc
Requires: libglade-data
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

%package bin
Summary: bin components for the libglade package.
Group: Binaries
Requires: libglade-data

%description bin
bin components for the libglade package.


%package data
Summary: data components for the libglade package.
Group: Data

%description data
data components for the libglade package.


%package dev
Summary: dev components for the libglade package.
Group: Development
Requires: libglade-lib
Requires: libglade-bin
Requires: libglade-data
Provides: libglade-devel

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
Requires: libglade-data

%description lib
lib components for the libglade package.


%prep
%setup -q -n libglade-2.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508451013
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1508451013
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libglade-convert

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
%defattr(-,root,root,-)
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
