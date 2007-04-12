%define module	Youri-Package-RPM-Generator
%define name	perl-%{module}
%define version 0.1.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Template-based rpm generator
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{module}-v%{version}.tar.bz2
Url:		http://youri.zarb.org
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:  perl(URPM)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This module generates rpm packages from a spec file template, for testing
purposes.

%prep
%setup -q -n %{module}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*


