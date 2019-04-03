#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-isort
Version  : 4.3.16
Release  : 41
URL      : https://files.pythonhosted.org/packages/08/d2/bbbb582ea75a3237e16e7d1f37fa3bda72e9690097d7a24dfd7d80f899d0/isort-4.3.16.tar.gz
Source0  : https://files.pythonhosted.org/packages/08/d2/bbbb582ea75a3237e16e7d1f37fa3bda72e9690097d7a24dfd7d80f899d0/isort-4.3.16.tar.gz
Summary  : A Python utility / library to sort Python imports.
Group    : Development/Tools
License  : MIT
Requires: deprecated-isort-bin = %{version}-%{release}
Requires: deprecated-isort-license = %{version}-%{release}
Requires: deprecated-isort-python = %{version}-%{release}
Requires: appdirs
Requires: futures
Requires: pip
Requires: pipreqs
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : futures

%description
.. image:: https://raw.github.com/timothycrosley/isort/master/logo.png
:alt: isort

%package bin
Summary: bin components for the deprecated-isort package.
Group: Binaries
Requires: deprecated-isort-license = %{version}-%{release}

%description bin
bin components for the deprecated-isort package.


%package legacypython
Summary: legacypython components for the deprecated-isort package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-isort package.


%package license
Summary: license components for the deprecated-isort package.
Group: Default

%description license
license components for the deprecated-isort package.


%package python
Summary: python components for the deprecated-isort package.
Group: Default

%description python
python components for the deprecated-isort package.


%prep
%setup -q -n isort-4.3.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554321347
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-isort
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-isort/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isort

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-isort/LICENSE

%files python
%defattr(-,root,root,-)
