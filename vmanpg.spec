Summary:	SVGAlib pager for man pages
Summary(pl):	Przegl±darka podrêcznika systemowego dla SVGAlib
Name:		vmanpg
Version:	1.1
Release:	5
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.svgalib.org/rus/vmanpg/%{name}-%{version}.tar.gz
# Source0-md5:	417fcdfccd10752ea79aee273a128830
Source1:	%{name}-fonts.tar.bz2
# Source1-md5:	851d1a61d70852e64c568a297de16640
Patch0:		%{name}-Polish.patch
BuildRequires:	svgalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vmanpg is a man pager, working in fullscreen SVGA mode.

%description -l pl
vmanpg jest przegl±dark± manuali, pracuj±c± w pe³noekranowym trybie
SVGA.

%prep
%setup -q -a1
%patch -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install vmanpg $RPM_BUILD_ROOT%{_bindir}
install vman.sh $RPM_BUILD_ROOT%{_bindir}/vman
install vmanpg.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so vmanpg.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vman.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/vman
%attr(755,root,root) %{_bindir}/vmanpg
%{_mandir}/man1/*
