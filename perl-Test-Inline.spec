%define module Test-Inline
%define name    perl-%{module}
%define version 2.212
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Inlining your tests next to the code being tested
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl-prefork
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(File::Slurp) >= 9999.04
BuildRequires:  perl(File::Find::Rule) >= 0.26
BuildRequires:  perl(File::Flat) >= 0.95
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::chmod)
BuildRequires:  perl(List::Util) >= 1.11
BuildRequires:  perl(Getopt::Long) >= 2.34
BuildRequires:  perl(Class::Autouse) >= 1.15
BuildRequires:  perl(Algorithm::Dependency) >= 1.02
BuildRequires:  perl(Config::Tiny) >= 2.00
BuildRequires:  perl(Pod::Tests) >= 0.18
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(Test::ClassAPI) >= 1.02
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Embedding tests allows tests to be placed near the code it's
testing. This is a nice supplement to the traditional .t files.
It's like XUnit, Perl-style.

%prep
%setup -q -n %{module}-%{version} 

%build
chmod 644 Changes README
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/inline2test
%{perl_vendorlib}/Test
%{_mandir}/*/*


