Summary:	USB Modeswitch gets 4G cards in operational mode
Summary(de.UTF-8):	USB Modeswitch aktiviert UMTS-Karten
Name:		usb-modeswitch-data
Version:	20100826
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.draisberghof.de/usb_modeswitch/%{name}-%{version}.tar.bz2
# Source0-md5:	85c16bb87a6f05c2d04b93a22fe87e91
URL:		http://www.draisberghof.de/usb_modeswitch/
# NOTE: tcl is used in udev code 
Requires:	tcl
Requires:	udev
Requires:	usb-modeswitch >= 1.1.4
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/usb_modeswitch.d/*
/lib/udev/rules.d/40-usb_modeswitch.rules
