Summary:	USB Modeswitch gets 4G cards in operational mode
Summary(de.UTF-8):	USB Modeswitch aktiviert UMTS-Karten
Name:		usb-modeswitch-data
Version:	20110619
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.draisberghof.de/usb_modeswitch/%{name}-%{version}.tar.bz2
# Source0-md5:	d8bf9d0a3aac11ed26f1645413b8d6a5
URL:		http://www.draisberghof.de/usb_modeswitch/
# NOTE: tcl is used in udev code 
Requires:	tcl >= 8.4
Requires:	udev
Requires:	usb-modeswitch >= 1.1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
USB Modeswitch brings up your datacard into operational mode. When
plugged in they identify themselves as cdrom and present some
non-Linux compatible installation files. This tool deactivates this
cdrom-devices and enables the real communication device. It supports
most devices built and sold by Huawei, T-Mobile, Vodafone, Option,
ZTE, Novatel.

This package contains the data files needed for usb_modeswitch to
function.

%description -l de.UTF-8
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

%{__make} files-install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} db-install  \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/udevadm control --reload-rules

%postun
/sbin/udevadm control --reload-rules

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING README
%{_datadir}/usb_modeswitch
/lib/udev/rules.d/40-usb_modeswitch.rules
