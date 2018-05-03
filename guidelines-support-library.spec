# Set Git revision of library...
%global commit0 c9e423d7cf2afb88672e31f55e4b30c53be7aae3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20180305

Name: guidelines-support-library
Summary: Guidelines Support Library
Version: 0
Release: 3.%{date}git%{shortcommit0}%{?dist}

License: MIT
URL: https://github.com/Microsoft/GSL
Source0: %{url}/archive/%{commit0}.tar.gz
BuildArch: noarch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -n GSL-%{commit0}

%build
# Nothing to build. Header-only library.

%install
# Installing headers...
mkdir -p "%{buildroot}%{_includedir}/%{name}/gsl"
cp -a include/gsl %{buildroot}%{_includedir}/%{name}

%files devel
%doc README.md CONTRIBUTING.md
%{_includedir}/%{name}
