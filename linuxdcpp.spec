Summary:	Linux DC++ client port
Summary(pl.UTF-8):	Linuksowy port klienta DC++
Name:		linuxdcpp
Version:	1.1.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://launchpad.net/linuxdcpp/1.1/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	037de708bdb1e5dd7ac6c359b0e2c1a0
Source1:	%{name}.desktop
URL:		https://launchpad.net/linuxdcpp/
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	libglade2-devel >= 1:2.4
BuildRequires:	libnotify >= 0.4.1
BuildRequires:	libstdc++-devel >= 4.1
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	scons >= 0.98.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Suggests:	xdg-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux port of the DC++ Direct Connect client.

%description -l pl.UTF-8
Linuksowy port klienta Direct Connect DC++.

%prep
%setup -q

%build
export CXXFLAGS="%{rpmcflags}"
scons \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/man1}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

export CXXFLAGS="%{rpmcflags}"
scons install \
	FAKE_ROOT=$RPM_BUILD_ROOT

install data/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install icons/%{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

rm -rf $RPM_BUILD_ROOT%{_docdir}/linuxdcpp

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog.txt Credits.txt Readme.txt data/magnet.protocol
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_pixmapsdir}/%{name}.xpm
%{_mandir}/man1/%{name}.1*
