%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Handler-YAWriter
Summary:	XML::Handler::YAWriter perl module
Summary(pl):	Modu� perla XML::Handler::YAWriter
Name:		perl-XML-Handler-YAWriter
Version:	0.23
Release:	2
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl(IO::File) >= 1.06
BuildRequires:	perl-libxml >= 0.06
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAWriter implements Yet Another XML::Handler::Writer. The reasons for
this one are that I needed a flexible escaping technique, and want
some kind of pretty printing.

%description -l pl
YAWriter to jeszcze jedna implementacja (Yet Another)
XML::Handler::Writer. Powsta�a dlatego, �e autor potrzebowa�
elastycznej techniki cytowania i chcia� pewnego rodzaju �adnego
drukowania.

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
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/XML/Handler/*
%{_mandir}/man[13]/*
