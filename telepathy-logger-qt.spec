%define major 0
%define libname %mklibname telepathy-logger-qt %{major}
%define devname %mklibname telepathy-logger-qt -d
%define _disable_lto 1

Name: telepathy-logger-qt
Version:	17.09.0
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/telepathy-logger-qt/%(echo %{version}|cut -d. -f1-2)/src/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: Qt bindings to Telepathy IM logging
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(TelepathyQt5)
BuildRequires: boost-devel
BuildRequires: pkgconfig(telepathy-logger-0.2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(telepathy-glib)
BuildRequires: pkgconfig(farstream-0.2) pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-plugins-base-1.0) pkgconfig(telepathy-farstream) pkgconfig(telepathy-glib)

%description
Qt bindings to Telepathy IM logging

%package -n %{libname}
Summary: KDE library for accessing MBOX mail files
Group: System/Libraries

%description -n %{libname}
KDE library for accessing MBOX mail files

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
ln -s %{_bindir}/python2 python
export PATH=$(pwd):$PATH
%cmake_kde5

%build
export PATH=$(pwd):$PATH
%ninja -C build -j1

%install
export PATH=$(pwd):$PATH
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.5

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
