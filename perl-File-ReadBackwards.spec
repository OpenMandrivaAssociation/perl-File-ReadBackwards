%define upstream_name    File-ReadBackwards
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl extension for reading a file backwards by lines
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module reads a file backwards line by line. It is simple to use,
memory efficient and fast. It supports both an object and a tied handle
interface.

It is intended for processing log and other similar text files which
typically have their newest entries appended to them. By default files are
assumed to be plain text and have a line ending appropriate to the OS. But
you can set the input record separator string on a per file basis.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 684743
- update to new version 1.05

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.40.0-3
+ Revision: 654327
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 624745
- Add a summary
- import perl-File-ReadBackwards

