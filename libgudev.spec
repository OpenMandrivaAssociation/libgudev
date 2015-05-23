Summary:	GObject bidings to libudev
Name:		libgudev
Version:	219
Release:	1
License:	MIT
Group:		System/Libraries
URL:		https://wiki.gnome.org/Projects/libgudev
Source0:	https://download.gnome.org/sources/libgudev/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libudev) >= 199
BuildRequires:	pkgconfig(glib-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gio-2.0)

%track
prog %{name} = {
	url = https://download.gnome.org/sources/libgudev/(__VER__)
	regex = "%{name}-(__VER__)\.tar\.xz"
	version = %{version}
}

%description
This library provides GObject bindings for libudev.
It was originally part of udev-extras, then udev, then systemd.
It's now a project on its own.

%prep
%setup -q

%build
%configure \
    --enable-instrospecion=yes

%make

%install
%makeinstall_std

%files
