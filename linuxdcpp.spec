
%define		snap	061114

Summary:	Linux DC++ client port
Summary(pl):	Linuksowy port klienta DC++
Name:		linuxdcpp
Version:	0.%{snap}
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	3a6d0774504d1121dde539dad8bb82d6
URL:		http://linuxdcpp.berlios.de/
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel
BuildRequires:	glib-devel
BuildRequires:	libglade2-devel
BuildRequires:	pkgconfig
BuildRequires:	scons
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux port of the DC++ Direct Connect client.

%description -l pl
Linuksowy port klienta Direct Connect DC++.

%prep
%setup -q -n %{name}

%build
export CXXFLAGS="%{rpmcflags}"
scons \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

export CXXFLAGS="%{rpmcflags}"
scons install \
	FAKE_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt Credits.txt Readme.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
