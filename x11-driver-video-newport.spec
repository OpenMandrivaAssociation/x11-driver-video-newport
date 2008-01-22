Name: x11-driver-video-newport
Version: 0.2.1
Release: %mkrel 3
Summary: The X.org video driver for SGI Indy's and Indigo2's Newport video cards
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-newport  xorg/drivers/xf86-video-newport
# cd xorg/drivers/xf86-video/newport
# git-archive --format=tar --prefix=xf86-video-newport-0.2.1/ xf86-video-newport-0.2.1 | bzip2 -9 > xf86-video-newport-0.2.1.tar.bz2
########################################################################
Source0: xf86-video-newport-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-newport-0.2.1..origin/mandriva+gpl
Patch1: 0001-Define-NEWPORT_-_VERSION-using-PACKAGE_VERSION_.patch
Patch2: 0002-Rename-.cvsignore-to-.gitignore.patch
Patch3: 0003-Add-to-.gitignore-to-skip-patch-emacs-droppings.patch
Patch4: 0004-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch5: 0005-Don-t-need-to-check-for-dri-headers-runtime.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org video driver for SGI Indy's and Indigo2's Newport video cards.

%prep
%setup -q -n xf86-video-newport-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/newport_drv.so
%{_mandir}/man4/newport.*
