Summary:	Userland driver for IPP-over-USB printers
Name:		ippusbxd
Version:	1.30
Release:	1
Source0:	https://github.com/tillkamppeter/ippusbxd/archive/%{version}/%{name}-%{version}.tar.gz
License:	GPL
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	cmake

%description
Userland driver for IPP-over-USB printers

%prep
%autosetup -p1
mkdir exe
cd exe
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ../src

%build
%make_build

%install
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}/lib/udev/rules.d
mkdir -p %{buildroot}/lib/systemd/system
install -m 755 exe/ippusbxd %{buildroot}%{_sbindir}/
install -m 644 systemd-udev/55-ippusbxd.rules %{buildroot}/lib/udev/rules.d/
install -m 644 systemd-udev/ippusbxd@.service %{buildroot}/lib/systemd/system/


%files
%{_sbindir}/ippusbxd
/lib/udev/rules.d/*
/lib/systemd/system/*.service
