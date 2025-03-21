%define gudev_api 1.0
%define gudev_major 0
%define libgudev %mklibname gudev %{gudev_api} %{gudev_major}
%define libgudev_devel %mklibname gudev %{gudev_api} -d
%define girgudev %mklibname gudev-gir %{gudev_api}

Summary:	GObject bidings to libudev
Name:		libgudev
Version:	238
Release:	6
License:	MIT
Group:		System/Libraries
URL:		https://wiki.gnome.org/Projects/libgudev
Source0:	https://download.gnome.org/sources/libgudev/%{version}/%{name}-%{version}.tar.xz
Patch0:		https://gitlab.gnome.org/GNOME/libgudev/-/merge_requests/30.patch

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:	pkgconfig(libudev) >= 199
BuildRequires:	pkgconfig(glib-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)

%description
This library provides GObject bindings for libudev.
It was originally part of udev-extras, then udev, then systemd.
It's now a project on its own.

%package -n %{libgudev}
Summary:	Libraries for adding libudev support to applications that use glib
Group:		System/Libraries
Provides:	libgudev = %{EVRD}

%description -n %{libgudev}
This package contains the libraries that make it easier to use libudev
functionality from applications that use glib.

%package -n %{girgudev}
Summary:	GObject Introspection interface library for gudev
Group:		System/Libraries
Conflicts:	%{_lib}gudev1.0_0 < 182-5
Obsoletes:	%{_lib}udev-gir1.0

%description -n %{girgudev}
GObject Introspection interface library for gudev.

%package -n %{libgudev_devel}
Summary:	Header files for adding libudev support to applications that use glib
Group:		Development/C
Requires:	%{libgudev} = %{EVRD}

%description -n %{libgudev_devel}
This package contains the header and pkg-config files for developing
glib-based applications using libudev functionality.

%prep
%autosetup -p1
# tests require umockdev, which in turn requires libgudev, causing a nasty
# circular build dependency -- so disable tests
%meson \
	-Dtests=disabled

%build
%meson_build

%install
%meson_install

%files -n %{libgudev}
%{_libdir}/libgudev-%{gudev_api}.so.%{gudev_major}*

%files -n %{libgudev_devel}
%{_libdir}/libgudev-%{gudev_api}.so
%{_includedir}/gudev-%{gudev_api}
%{_datadir}/gir-1.0/GUdev-%{gudev_api}.gir
%{_libdir}/pkgconfig/gudev-%{gudev_api}.pc
%{_datadir}/vala/vapi/gudev-1.0.deps
%{_datadir}/vala/vapi/gudev-1.0.vapi

%files -n %{girgudev}
%{_libdir}/girepository-1.0/GUdev-%{gudev_api}.typelib
