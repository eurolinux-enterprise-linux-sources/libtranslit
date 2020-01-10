Name:		libtranslit
Version:	0.0.2
Release:	4%{?dist}
Summary:	ASCII to Unicode transliteration library with multiple backends

License:	GPLv3+
Group:		System Environment/Libraries
URL:		http://github.com/ueno/libtranslit
Source0:	http://cloud.github.com/downloads/ueno/libtranslit/%{name}-%{version}.tar.gz

BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool

%description
ASCII to Unicode transliteration library with multiple backends.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	m17n
Summary:	Transliteration module using m17n-lib for %{name}
BuildRequires:	pkgconfig(m17n-shell)
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	m17n
The %{name}-m17n package contains a transliteration module using
m17n-lib for %{name}.

%package	icu
Summary:	Transliteration module using m17n-lib for %{name}
BuildRequires:	pkgconfig(icu-io)
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	icu
The %{name}-icu package contains a transliteration module using
ICU for %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_libdir}/*.so.*
%dir %{_libdir}/libtranslit/modules
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir

%files m17n
%{_libdir}/libtranslit/modules/*m17n.so*

%files icu
%{_libdir}/libtranslit/modules/*icu.so*


%changelog
* Tue Jan 29 2013 Daiki Ueno <ueno@gnu.org> - 0.0.2-4
- rebuild with new icu

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Daiki Ueno <dueno@redhat.com> - 0.0.2-2
- rebuild with new icu

* Mon Mar  5 2012 Daiki Ueno <dueno@redhat.com> - 0.0.2-1
- initial packaging for Fedora
