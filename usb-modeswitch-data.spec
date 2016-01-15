Summary:	Data for USB Modeswitch tool which gets 4G cards in operational mode
Summary(de.UTF-8):	USB Modeswitch aktiviert UMTS-Karten
Summary(pl.UTF-8):	Dane dla narzędzia USB Modeswitch przełączającego karty 4G w tryb operacyjny
Name:		usb-modeswitch-data
Version:	20160112
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.draisberghof.de/usb_modeswitch/%{name}-%{version}.tar.bz2
# Source0-md5:	040d11138fc0a61b980d704ac3b4547f
URL:		http://www.draisberghof.de/usb_modeswitch/
# NOTE: tcl is used in udev code 
Requires:	tcl >= 8.4
Requires:	usb-modeswitch >= 2.3.0
Suggests:	udev-core
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

%description -l pl.UTF-8
USB Modeswitch potrafi przełączyć pewne urządzenia komunikacyjne w
tryb operacyjny. Takie urządzenia po podłączeniu identyfikują się jako
CD-ROM i oferują jedynie niezgodne z Linuksem pliki instalacyjne. To
narzędzie wyłącza emulację CD i włącza prawdziwe urządzenie
komunikacjne. Obsługuje większość urządzeń wytworzonych i oferowanych
przez firmy Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

Ten pakiet zawiera pliki z danymi potrzebnymi do działania programu
usb_modeswitch.

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
if [ -x /sbin/udevadm ]; then
	/sbin/udevadm control --reload-rules
fi

%postun
if [ -x /sbin/udevadm ]; then
	/sbin/udevadm control --reload-rules
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_datadir}/usb_modeswitch
/lib/udev/rules.d/40-usb_modeswitch.rules
