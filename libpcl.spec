Summary:	Portable Coroutine Library (PCL)
Summary(pl.UTF-8):	Przenośna biblioteka korutyn
Name:		libpcl
Version:	1.12
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://xmailserver.org/libpcl.html
Source0:	http://www.xmailserver.org/pcl-%{version}.tar.gz
# Source0-md5:	816d394743d8ab1b3e20af1efebb093d
URL:		http://www.xmailserver.org/libpcl.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Portable Coroutine Library implementation written in ANSI C.

Coroutines can be used to implement co-operative threading among many
tasks without overloading the OS with threads/processes. Since context
switch between coroutines is very fast, certain applications might
have performance gain in using this type of threading.

%description -l pl.UTF-8
PCL (Portable Couroutine Library) to implementacja przenośnej
biblioteki korutyn napisana w ANSI C.

Korutyny mogą być użyte do zaimplementowania współpracujących wątków
wśród wielu zadań bez obciążania systemu operacyjnego wątkami czy
procesami. Ponieważ przełączanie kontekstu między korutynami jest
bardzo szybkie, pewne aplikacje mogą zyskać na wydajności dzieki
zastosowaniu tego rodzaju wątkowania.

%package devel
Summary:	Header files for libpcl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpcl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libpcl library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libpcl.

%package static
Summary:	Static libpcl library
Summary(pl.UTF-8):	Statyczna biblioteka libpcl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpcl library.

%description static -l pl.UTF-8
Statyczna biblioteka libpcl.

%prep
%setup -q -n pcl-%{version}

%build
%configure
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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libpcl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcl.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcl.so
%{_libdir}/libpcl.la
%{_includedir}/pcl.h
%{_mandir}/man3/pcl.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpcl.a
