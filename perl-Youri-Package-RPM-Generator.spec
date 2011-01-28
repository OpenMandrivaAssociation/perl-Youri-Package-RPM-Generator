%define upstream_name       Youri-Package-RPM-Generator
%define upstream_version    0.1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Template-based rpm generator
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source0:	http://youri.zarb.or/download/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(URPM)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl-version
Requires:       perl-version
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*


