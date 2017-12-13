Name: lxqt-l10n
Version: 0.12.0
Release: 2
Source0: https://github.com/lxde/%{name}/archive/%{version}.tar.gz
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
Obsoletes: lxqt-common

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
# This is also packaged in lxqt-globalkeys
rm -f %{buildroot}%{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_tr.qm
%find_lang %{name} --all-name --with-qt

%files -f %{name}.lang
