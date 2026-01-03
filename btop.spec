# Don't add random optimizations

%define _empty_manifest_terminate_build 0

Name:           btop
Version:        1.4.6
Release:        1
Summary:        Usage and stats for processor, memory, disks, network and processes
Group:          Monitoring
License:        Apache 2.0
URL:            https://github.com/aristocratos/btop
Source:         https://github.com/aristocratos/btop/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:  coreutils

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
C++ version and continuation of bashtop and bpytop.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*
