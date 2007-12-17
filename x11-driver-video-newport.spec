Name: x11-driver-video-newport
Version: 0.2.1
Release: %mkrel 2
Summary: The X.org video driver for SGI Indy's and Indigo2's Newport video cards
Group: Development/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-newport  xorg/drivers/xf86-video-newport
# cd xorg/drivers/xf86-video/newport
# git-archive --format=tar --prefix=xf86-video-newport-0.2.1/ master | bzip2 -9 > xf86-video-newport-0.2.1.tar.bz2
########################################################################
Source0: xf86-video-newport-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
The X.org video driver for SGI Indy's and Indigo2's Newport video cards.

%prep
%setup -q -n xf86-video-newport-%{version}

%patch1 -p1

%build
autoreconf -ifs
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
