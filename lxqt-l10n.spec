Name: lxqt-l10n
Version: 0.13.0
Release: 1
Source0: https://github.com/lxqt/%{name}/archive/%{version}.tar.gz
Summary: Translations of LXQt
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/Other
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(lxqt-build-tools)
BuildArch: noarch

Conflicts: lxqt-about < 0.11.0
Conflicts: lxqt-config < 0.11.0
Conflicts: lxqt-panel < 0.11.0
Conflicts: lxqt-session < 0.11.0
Conflicts: lxqt-common < 0.12.0

%description
This package is providing translations ("localization") in
terms of the Qt TS files of all components maintained by the LXQt project.

%prep
%setup -q

%cmake_qt5 -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
# These are also packaged in their respective lxqt packages
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-sudo/*.qm
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-powermanagement/*.qm
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-admin-time/*.qm
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-admin-user/*qm
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-config-notificationd/*.qm
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-config-powermanagement/*.qm
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-policykit-agent/*.qm
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts/*.qm
rm -f %{buildroot}%{_datadir}/lximage-qt/translations/*.qm
rm -f %{buildroot}%{_datadir}/libfm-qt/translations/*.qm
#Leave for future changes
#rm -f %{buildroot}%{_datadir}/
#rm -f %{buildroot}%{_datadir}/lxqt/translations/
%find_lang %{name} --all-name --with-qt

%files -f %{name}.lang
