Name: lxqt-l10n
Version: 0.11.1
Release: 2
Source0: https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
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

Conflicts:	lxqt-about < 0.11.0
Conflicts:	lxqt-config < 0.11.0
Conflicts:	lxqt-panel < 0.11.0
Conflicts:	lxqt-session < 0.11.0
Conflicts:  lxqt-admin < 0.11.0
Conflicts:  task-lxqt < 0.11.0

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

%files
%{_datadir}/*/translations/*.qm
%{_datadir}/*/translations/*/*.qm
%{_datadir}/*/translations/*/*/*.qm
