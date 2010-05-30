%define source_name	usb-modeswitch-data

Summary:	USB Modeswitch gets 4G cards in operational mode
Summary(de):	USB Modeswitch aktiviert UMTS-Karten
Name:		usb_modeswitch-data
Version:	20100418
Release:	1
License:	GPL v2+
Group:		Applications/System
URL:		http://www.draisberghof.de/usb_modeswitch/
Source0:	http://www.draisberghof.de/usb_modeswitch-data/usb-modeswitch-data-%{version}.tar.bz2
Requires:	tcl
Requires:	udev
Requires:	usb-modeswitch >= 1.1.2
BuildArch:	noarch

%description
USB Modeswitch brings up your datacard into operational mode. When
plugged in they identify themselves as cdrom and present some
non-Linux compatible installation files. This tool deactivates this
cdrom-devices and enables the real communication device. It supports
most devices built and sold by Huawei, T-Mobile, Vodafone, Option,
ZTE, Novatel.

This package contains the data files needed for usb_modeswitch to
function.

%description	-l de
USB Modeswitch deaktiviert die CDROM-Emulation einiger UMTS-Karten.
Dadurch erkennt Linux die Datenkarte und kann damit Internet-
Verbindungen aufbauen. Die gängigen Karten von Huawei, T-Mobile,
Vodafone, Option, ZTE und Novatell werden unterstützt.

Dieses Paket enthält die Dateien für usb_modeswitch benötigt um zu
funktionieren.


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/usb_modeswitch.d/
install -d $RPM_BUILD_ROOT/lib/udev/rules.d/

install -p  usb_modeswitch.d/* $RPM_BUILD_ROOT%{_sysconfdir}/usb_modeswitch.d/
install -p 40-usb_modeswitch.rules $RPM_BUILD_ROOT/lib/udev/rules.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
udevadm control --reload-rules

%postun
udevadm control --reload-rules

%files
%defattr(644,root,root,755)
/lib/udev/rules.d/40-usb_modeswitch.rules
%{_sysconfdir}/usb_modeswitch.d/
%doc ChangeLog COPYING README
