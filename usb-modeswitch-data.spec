Summary:	USB Modeswitch gets 4G cards in operational mode
Summary(de.UTF-8):	USB Modeswitch aktiviert UMTS-Karten
Name:		usb-modeswitch-data
Version:	20100418
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.draisberghof.de/usb_modeswitch-data/%{name}-%{version}.tar.bz2
# Source0-md5:	659c9633513fa2f84465244a50c351b3
URL:		http://www.draisberghof.de/usb_modeswitch/
Requires:	udev
Requires:	usb-modeswitch >= 1.1.2
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
udevadm control --reload-rules

%postun
udevadm control --reload-rules

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/usb_modeswitch.d/*
/lib/udev/rules.d/40-usb_modeswitch.rules
