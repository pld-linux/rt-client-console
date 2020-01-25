%define	rsvn	58
Summary:	ncurses based Request Tracker client
Name:		rt-client-console
Version:	0.1
Release:	0.%{rsvn}1
License:	GPL v2
Group:		Applications
Source0:	%{name}-%{rsvn}.tar.gz
# Source0-md5:	b1183a4fb034d8f68b6b05ccefbbbef8
URL:		http://code.google.com/p/rt-client-console/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is a ncurses client providing a full featured text based
interface to RT, the acclaimed request tracker (
http://bestpractical.com/rt/ ) . It uses the REST interface to
retrieve data, and POE to provide a multitask non synchronous
interface

%prep
%setup -q -n %{name}

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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/RT
%{_mandir}/man1/rtconsole.1*
%{_mandir}/man3/*.3*
