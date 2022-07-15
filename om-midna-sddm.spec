Name: om-midna-sddm
Version: 0.5
Release: 4
License: GPL
Group: Graphical desktop/KDE
Summary: SDDM Login theme adapted for OpenMandriva based on KaOS Midna
Url: http://kaosx.us
# https://github.com/KaOSx/midna/tree/master/sddm/midna
Source:%{name}-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

Requires:	google-raleway-fonts

%description
SDDM Login theme adapted for OpenMandriva based on KaOS Midna

%prep
%autosetup -p1 -c %{name}
find . -type f | xargs chmod 0644

%install
mkdir -p %{buildroot}%{_datadir}/sddm/themes/om-midna-sddm
cp -rf * %{buildroot}%{_datadir}/sddm/themes/om-midna-sddm/

%files
%{_datadir}/sddm/themes/om-midna-sddm
