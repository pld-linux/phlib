Summary:	Common netFluid Technology Function Set
Summary(pl):	Wspólny zestaw funkcji netFluid Technology
Name:		phlib
Version:	1.20
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://www.nfluid.com/download/src/%{name}-%{version}.tgz
# Source0-md5:	521c93a461a58ab808187abbc54a39a7
Patch0:		%{name}-soname.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phlib provides the core function set used by netFluid Technology. It
provides such things as a universal double linked list, very efficient
constant memory string parsing and building, fixed memory relocatable.

%description -l pl
phlib udostêpnia podstawowy zestaw funkcji wykorzystywanych przez
netFluid Technology. Udostêpnia takie rzeczy jak uniwersalne podwójne
listy, bardzo efektywn± analizê sk³adniow± i tworzenie ³añcuchów w
pamiêci, sta³± relokacjê pamiêci.

%package devel
Summary:	Common netFluid Technology Function Set - development files
Summary(pl):	Wspólny zestaw funkcji netFluid Technology - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for phlib.

%description devel -l pl
Pliki dla programistów do phlib.

%package static
Summary:	Common netFluid Technology Function Set - static libraries
Summary(pl):	Wspólny zestaw funkcji netFluid Technology - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
phlib static libraries.

%description static -l pl
Statyczne biblioteki phlib.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -fPIC"
%configure \
	cflags=our
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpxtra.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpxtra.so
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libpxtra.a
