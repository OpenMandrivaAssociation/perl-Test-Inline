%define module Test-Inline

Name:		perl-%{module}
Version:	2.212
Release:	2
Summary:	Inlining your tests next to the code being tested
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-prefork
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(File::Slurp) >= 9999.04
BuildRequires:	perl(File::Find::Rule) >= 0.26
BuildRequires:	perl(File::Flat) >= 0.95
BuildRequires:	perl(File::Remove)
BuildRequires:	perl(File::chmod)
BuildRequires:	perl(List::Util) >= 1.11
BuildRequires:	perl(Getopt::Long) >= 2.34
BuildRequires:	perl(Class::Autouse) >= 1.15
BuildRequires:	perl(Algorithm::Dependency) >= 1.02
BuildRequires:	perl(Config::Tiny) >= 2.00
BuildRequires:	perl(Pod::Tests) >= 0.18
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Script)
BuildRequires:	perl(Test::ClassAPI) >= 1.02
BuildArch:	noarch

%description
Embedding tests allows tests to be placed near the code it's
testing. This is a nice supplement to the traditional .t files.
It's like XUnit, Perl-style.

%prep
%setup -q -n %{module}-%{version} 

%build
chmod 644 Changes README
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/inline2test
%{perl_vendorlib}/Test
%{_mandir}/*/*




%changelog
* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.212-1mdv2011.0
+ Revision: 602392
- update to new version 2.212

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.211-1mdv2010.0
+ Revision: 396225
- update to new version 2.211

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.210-1mdv2010.0
+ Revision: 378239
- update to new version 2.210

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.209-1mdv2010.0
+ Revision: 370200
- update to new version 2.209

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.208-4mdv2009.0
+ Revision: 258515
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.208-3mdv2009.0
+ Revision: 246536
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.208-1mdv2008.1
+ Revision: 119229
- update to new version 2.208

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.207-1mdv2008.0
+ Revision: 69249
- update to new version 2.207

* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.205-1mdv2008.0
+ Revision: 65330
- new version


* Thu Jan 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.201-1mdv2007.0
+ Revision: 110177
- fix buildrequires
- new version

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.105-1mdv2007.1
+ Revision: 84320
- new release
- Import perl-Test-Inline

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.103-3mdv2007.0
- Rebuild

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.103-2mdk
- Fix SPEC according to Perl Policy
    - BuildRequires
    - Source URL
- use mkrel

* Fri Sep 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.103-1mdk
- New release 2.103
- fix directory ownership

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.102-2mdk
- Fix file permissions

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.102-1mdk
- New version 2.102

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.101-1mdk
- New release 2.101

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.16-1mdk
- initial Mandriva package

