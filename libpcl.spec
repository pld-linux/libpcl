Summary:	Portable Coroutine Library (PCL)
Name:		libpcl
Version:	1.6
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.xmailserver.org/pcl-%{version}.tar.gz
# Source0-md5:	67f63b02e94ab1775f26bc5463817f09
URL:		http://www.xmailserver.org/libpcl.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Portable Coroutine Library implementation written in ANSI C.

Coroutines can be used to implement co-operative threading among many
tasks without overloading the OS with threads/processes. Since context
switch between coroutines is very fast, certain applications might
have performance gain in using this type of threading.

%package devel
Summary:	Header files for libpcl library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libpcl library.

%package static
Summary:	Static libpcl library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpcl library.

%prep
%setup -q

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
%attr(755,root,root) %{_prefix}/lib64/libpcl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pcl.h
%{_libdir}/libpcl.la
%{_mandir}/man3/pcl.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpcl.a
