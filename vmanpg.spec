Summary:	SVGAlib pager for man pages
Summary(pl):	Przegladarka podrecznika systemowego dla SVGAlib
Name:		vmanpg
Version:	1.1
Release:	2
License:	GPL
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	http://www.svgalib.org/rus/vmanpg/%{name}-%{version}.tar.gz
BuildRequires:	svgalib-devel
Exclusivearch:	%{ix86} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vmanpg is a man pager, working in fullscreen SVGA mode.

%description -l pl
vmanpg jest przegl±dark± manuali, pracuj±c± w pe³noekranowym trybie
SVGA.

%prep
%setup -q

%build
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS -s}%{?debug:-O -g -s}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install vmanpg $RPM_BUILD_ROOT%{_bindir}
install vman.sh $RPM_BUILD_ROOT%{_bindir}/vman
install vmanpg.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so vmanpg.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vman.1

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/vman
%attr(755,root,root) %{_bindir}/vmanpg
%{_mandir}/man1/*
