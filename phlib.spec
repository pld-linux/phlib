Summary:	Common netFluid Technology Function Set
Summary(pl):	Wsp�lny zestaw technologii netFluid
Name:		phlib
Version:	1.18
Release:	2
Source0:	http://www.nfluid.com/download/src/%{name}-%{version}.tgz
# Source0-md5:	c7ba6fd365fcd60fc4431a907126674e
License:	GPL
Group:		Libraries
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phlib provides the core function set used by netFluid Technology. It
provides such things as a universal double linked list, very efficient
constant memory string parsing and building, fixed memory relocatable.

%description -l pl
phlib udost�pnia podstawowy zestaw funkcji wykorzystywanych przez
netFluid technologi�. Udost�pnia takie rzeczy jak uniwersalne podw�jne
listy, bardzo efektywn� analiz� sk�adniow� i tworzenie �a�cuch�w w
pami�ci, sta�� relokacj� pami�ci.

%package devel
Summary:	Common netFluid Technology Function Set - development
Summary(pl):	Wsp�lny zestaw technologii netFluid - dla programist�w
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for phlib.

%description devel -l pl
Pliki dla programist�w do phlib.

%package static
Summary:	Common netFluid Technology Function Set - static
Summary(pl):	Wsp�lny zestaw technologii netFluid - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static development files for phlib.

%description static -l pl
Statyczne pliki dla programist�w dla phlib.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=${RPM_BUILD_ROOT}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpxtra.so*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpxtra.a*
