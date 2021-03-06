# Created by pyp2rpm-3.3.2
%global pypi_name coreschema

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        1%{?dist}
Summary:        Core Schema

License:        BSD
URL:            https://github.com/core-api/python-coreschema
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(jinja2)
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/coreschema/encodings
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 0.0.4-1
- Initial package.