Name: guidelines-support-library
Summary: Guidelines Support Library
# update breaks telegram-desktop
Version:	3.0.1
Release:	1

License: MIT
URL: https://github.com/Microsoft/GSL
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n GSL-%{version}

%build
# Nothing to build. Header-only library.

%install
# Installing headers...
mkdir -p "%{buildroot}%{_includedir}/"
cp -ra include/gsl %{buildroot}%{_includedir}/

%files devel
%doc README.md CONTRIBUTING.md
%license LICENSE ThirdPartyNotices.txt
%{_includedir}/gsl/
