%{?scl:%scl_package nodejs-rimraf}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-imurmurhash

%global npm_name imurmurhash
%{?nodejs_find_provides_and_requires}

Name:		%{?scl_prefix}nodejs-imurmurhash
Version:	0.1.4
Release:	1%{?dist}
Summary:	An incremental implementation of MurmurHash3
Url:		https://github.com/jensyt/imurmurhash-js
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%description
An incremental implementation of MurmurHash3

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json imurmurhash.js imurmurhash.min.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%files
%{nodejs_sitelib}/imurmurhash

%doc README.md
#%doc LICENSE license is included in README

%changelog
* Thu Apr 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.4-1
- Initial build

