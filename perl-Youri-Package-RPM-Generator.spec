%define upstream_name       Youri-Package-RPM-Generator
%define upstream_version    0.1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3
Summary:	Template-based rpm generator
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source0:	http://youri.zarb.or/download/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(URPM)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl-version
BuildRequires:  perl-devel
Requires:       perl-version
BuildArch:	    noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This module generates rpm packages from a spec file template, for testing
purposes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*




%changelog
* Fri Jan 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 633675
- new version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.0-6mdv2010.0
+ Revision: 430675
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0-5mdv2009.0
+ Revision: 258924
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0-4mdv2009.0
+ Revision: 246825
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.0-2mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-2mdv2008.0
+ Revision: 17229
- force dependency on perl-version


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2007.1
+ Revision: 138890
- Imported perl-Youri-Package-RPM-Generator-0.1.0-1mdv2007.1 into SVN repository.

* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2007.1
- first mdv release

