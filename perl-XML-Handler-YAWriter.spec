%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Handler-YAWriter
Summary:	XML-Handler-YAWriter perl module
Summary(pl):	Modu³ perla XML-Handler-YAWriter
Name:		perl-XML-Handler-YAWriter
Version:	0.23
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAWriter implements Yet Another XML::Handler::Writer. The
reasons for this one are that I needed a flexible escaping
technique, and want some kind of pretty printing.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/XML/*
%{_mandir}/man[3]/*
