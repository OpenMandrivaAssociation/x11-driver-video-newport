Name: x11-driver-video-newport
Version: 0.2.4
Release: 1
Summary: The X.org video driver for SGI Indy's and Indigo2's Newport video cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-newport-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-newport is the X.org video driver for SGI Indy's and
Indigo2's Newport video cards.

%prep
%setup -qn xf86-video-newport-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/newport_drv.so
%{_mandir}/man4/newport.*
