
Name: lxqt-l10n
Version: 0.11.0
Release: 1
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
BuildArch: noarch

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
%{_datadir}/*/translations/*/*.qm
