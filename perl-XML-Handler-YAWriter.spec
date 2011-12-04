#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Handler-YAWriter
Summary:	XML::Handler::YAWriter Perl module - yet another Perl SAX XML Writer
Summary(pl.UTF-8):	Moduł Perla XML::Handler::YAWriter - jeszcze jeden perlowy SAX XML Writer
Name:		perl-XML-Handler-YAWriter
Version:	0.23
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c7ba2a828a284d6a13ea6fbbfec2b162
URL:		http://search.cpan.org/dist/XML-Handler-YAWriter/
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

%description -l pl.UTF-8
YAWriter to jeszcze jedna implementacja (Yet Another)
XML::Handler::Writer. Powstała dlatego, że autor potrzebował
elastycznej techniki cytowania i chciał pewnego rodzaju ładnego
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
%doc Changes README
%attr(755,root,root) %{_bindir}/xmlpretty
%{perl_vendorlib}/XML/Handler/YAWriter.pm
%{_mandir}/man1/xmlpretty.1p*
%{_mandir}/man3/XML::Handler::YAWriter.3pm*
