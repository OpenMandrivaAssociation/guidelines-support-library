Name: guidelines-support-library
Summary: Guidelines Support Library
Version:	4.2.2
Release:	1

License: MIT
URL: https://github.com/Microsoft/GSL
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: ninja
BuildRequires: cmake

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n GSL-4.2.2 -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGSL_TEST:BOOL=OFF \

%ninja_build

%install
%ninja_install -C build

%files devel
%doc README.md CONTRIBUTING.md
%license LICENSE ThirdPartyNotices.txt
%{_datadir}/cmake/Microsoft.GSL/
%{_includedir}/gsl/
