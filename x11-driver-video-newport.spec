Name: x11-driver-video-newport
Version: 0.2.4
Release: 2
Summary: The X.org video driver for SGI Indy's and Indigo2's Newport video cards
Group: System/X11
License: MIT
URL: https://xorg.freedesktop.org
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



%changelog
* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.2.3-10
+ Revision: 787236
- Rebuild for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.2.3-9
+ Revision: 748429
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.3-8
+ Revision: 703703
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.2.3-7
+ Revision: 683579
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-6
+ Revision: 671156
- mass rebuild

* Tue Jan 18 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.2.3-5
+ Revision: 631510
- Rebuild since some files were eaten by the build system

* Mon Dec 13 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.2.3-4mdv2011.0
+ Revision: 620651
- Add patch to stop using obsolete functions.
  Without it, X fails with "unresolved symbol" error.

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.2.3-3mdv2011.0
+ Revision: 595734
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.2.3-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.2.3-1mdv2010.1
+ Revision: 464264
- New version: 0.2.3

* Wed May 20 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.2.2-1mdv2010.0
+ Revision: 378070
- New version 0.2.2

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 0.2.1-7mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

  + Thierry Vignaud <tv@mandriva.org>
    - fix group

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 0.2.1-6mdv2009.1
+ Revision: 308272
- rebuild for new X server

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - improved description

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.2.1-4mdv2008.1
+ Revision: 165572
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.2.1-3mdv2008.1
+ Revision: 156612
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.2.1-2mdv2008.1
+ Revision: 154856
- Don't need to check for dri headers and runtime.
  Addition of check was in error.
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Propert use existing tag xf86-video-newport-0.2.1 and generate patches from
  that tag.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.2.1-1mdv2008.1
+ Revision: 98653
- new upstream version: 0.2.1
- minor spec cleanup

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdv2008.0
+ Revision: 75783
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 15:39:01 (31704)
- fill in summary & descriptions for all video drivers

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 19:59:30 (31594)
- Updated drivers for X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

