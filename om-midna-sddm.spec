%define name om-midna-sddm
%define version 0.5
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Graphical desktop/KDE
Summary: SDDM Login theme adapted for OpenMandriva based on KaOS Midna
Url: http://kaosx.us
Source:%{name}-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
SDDM Login theme adapted for OpenMandriva based on KaOS Midna

%files
%{_datadir}/sddm/themes/om-midna-sddm

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/sddm/themes/om-midna-sddm
cp -rf * %{buildroot}%{_datadir}/sddm/themes/om-midna-sddm/
