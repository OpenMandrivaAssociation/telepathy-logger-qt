%define major 1
%define libname %mklibname %{name} 4 %{major}
%define libdev %mklibname %{name} -d

Summary:	Telepathy Logging for Qt
Name:		telepathy-logger-qt
Version:	0.5.1
Release:	3
Url:		https://projects.kde.org/projects/extragear/network/telepathy/%{name}
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%{version}/src/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Networking/Instant messaging 
BuildRequires:	pkgconfig(python-2.7)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(QtGLib-2.0)
BuildRequires:	pkgconfig(telepathy-logger-0.2)
BuildRequires:	pkgconfig(TelepathyQt4) >= 0.9.1
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	qt4-devel
BuildRequires:	boost-devel
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	flex

%description
Telepathy Logging for Qt.

#------------------------------------------------------------------------------

%package -n %{libname}
Summary:	Telepathy Logging for Qt
Group:		System/Libraries

%description -n %{libname}
Telepathy Logging for Qt.

%files -n %{libname}
%{_libdir}/libtelepathy-logger-qt4.so.%{major}*

#------------------------------------------------------------------------------

%package -n %{libdev}
Summary:	Header files, libraries and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}4-devel = %{version}-%{release}

%description -n %{libdev}
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using 
%{name}, you will need to install %{name}-devel.

%files -n %{libdev}
%{_includedir}/telepathy-logger-0.2/TelepathyLoggerQt4
%{_libdir}/pkgconfig/TelepathyLoggerQt4.pc
%{_libdir}/libtelepathy-logger-qt4.so

#------------------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_qt4 -DBUILD_SHARED_LIBS=ON
#cmake -DBUILD_SHARED_LIBS=ON
%make

%install
%makeinstall_std -C build
