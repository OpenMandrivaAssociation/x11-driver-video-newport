Name: x11-driver-video-newport
Version: 0.2.1
Release: %mkrel 4
Summary: The X.org video driver for SGI Indy's and Indigo2's Newport video cards
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-newport-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
The X.org video driver for SGI Indy's and Indigo2's Newport video cards.

%prep
%setup -q -n xf86-video-newport-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/newport_drv.la
%{_libdir}/xorg/modules/drivers/newport_drv.so
%{_mandir}/man4/newport.*
