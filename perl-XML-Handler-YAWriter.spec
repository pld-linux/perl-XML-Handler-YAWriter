#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Handler-YAWriter
Summary:	XML::Handler::YAWriter perl module
Summary(pl):	Modu³ perla XML::Handler::YAWriter
Name:		perl-XML-Handler-YAWriter
Version:	0.23
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c7ba2a828a284d6a13ea6fbbfec2b162
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl(IO::File) >= 1.06
BuildRequires:	perl-libxml >= 0.06
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAWriter implements Yet Another XML::Handler::Writer. The reasons for
this one are that I needed a flexible escaping technique, and want
some kind of pretty printing.

%description -l pl
YAWriter to jeszcze jedna implementacja (Yet Another)
XML::Handler::Writer. Powsta³a dlatego, ¿e autor potrzebowa³
elastycznej techniki cytowania i chcia³ pewnego rodzaju ³adnego
drukowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/Handler/*
%{_mandir}/man[13]/*
