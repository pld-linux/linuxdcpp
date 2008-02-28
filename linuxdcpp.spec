
Summary:	Linux DC++ client port
Summary(pl.UTF-8):	Linuksowy port klienta DC++
Name:		linuxdcpp
Version:	1.0.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://prdownload.berlios.de/linuxdcpp/%{name}-%{version}.tar.bz2
# Source0-md5:	5ead00a1c4d07958c784b2f365b7c395
Source1:	%{name}.desktop
URL:		http://linuxdcpp.berlios.de/
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	gtk+2-devel >= 2:2.6
BuildRequires:	libglade2-devel >= 1:2.4
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	scons >= 0.96
BuildRequires:	zlib-devel
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
install -d $RPM_BUILD_ROOT%{_desktopdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

export CXXFLAGS="%{rpmcflags}"
scons install \
	FAKE_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt Credits.txt Readme.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/linuxdcpp
%{_desktopdir}/*
