%define		orgname kdeextragear-network
%define		snap	886255	
Summary:	kdeextragear-network
Summary(pl.UTF-8):	kdeextragear-network
Name:		kde4-kdeextragear-network
Version:	4.1.73
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/unstable/snapshots/%{orgname}-%{snap}.tar.bz2
# Source0-md5:	8795a64360a279a41643e446c573faad
URL:		http://extragear.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdeextragear-network.

%description -l pl.UTF-8
kdeextragear-network.

%package -n kde4-kwlan
Summary:	KDE frontend for WPA Supplicant
Summary(pl.UTF-8):	Frontend KDE dla programu WPA Supplicant
Group:		X11/Applications/Networking

%description -n kde4-kwlan
Allows you to configure different network profiles using all
encryptions wpa_supplicant provides (WEP, WPA, WPA2 etc). Systray icon
shows connection status. Based on wpa_gui by Jouni Malinen.

%description -n kde4-kwlan -l pl.UTF-8
kwlan pozwala na konfigurację różnych profili sieciowych przy użyciu
wszystkich metod szyfrowania udostępnianych przez program
wpa_supplicant (WEP, WPA, WPA2 itp.). Ikona w zasobniku systemowym
pokazuje status połączenia. kwlan jest oparty na wpa_gui Jouni
Malinena.

%package -n kde4-kftpgrabber
Summary:	A graphical FTP client for KDE
Summary(pl.UTF-8):	Graficzny klient FTP dla KDE
Group:		X11/Applications/Networking

%description -n kde4-kftpgrabber
KFTPGrabber is a graphical FTP client for KDE. It provides a nice GUI
for all file transfer operations, it supports encrypted connections
(both SSL and SFTP), site-to-site (FXP) transfers and complete
bookmark system.

%description -n kde4-kftpgrabber -l pl.UTF-8
KFTPGrabber jest graficznym klientem FTP dla KDE. Wyposażony jest w
miły dla oka GUI, obsługuje szyfrowane połączenia (SSL i SFTP),
przesyłanie site-to-site (FXP) oraz posiada zakładki.

%package -n kde4-ktorrent
Summary:	Native KDE BitTorrent client
Summary(pl.UTF-8):	Natywny klient BitTorrenta dla KDE
Group:		X11/Applications/Networking

%description -n kde4-ktorrent
KTorrent is a BitTorrent program for KDE.

Its main features are:
- Downloads torrent files
- Upload speed capping, seeing that most people can't upload infinite
  amounts of data.
- Internet searching using various search engines, you can even add
  your own.
- UDP Trackers.

%description -n kde4-ktorrent -l pl.UTF-8
KTorrent to klient BitTorrenta dla KDE.

Główne cechy to:
- ściąganie plików torrent
- ograniczanie szybkości uploadu, baczące żeby większość ludzi nie
  przesyłała nieograniczonej ilości danych
- przeszukiwanie Internetu przy użyciu różnych wyszukiwarek, można
  nawet dodać własną
- trackery UDP

KTorrent to klient BitTorrenta dla KDE.

%package -n kde4-kmldonkey
Summary:	A client for the mldonkey P2P network
Summary(pl.UTF-8):	Klient dla sieci P2P mldonkey
Group:		X11/Applications/Networking

%description -n kde4-kmldonkey
KMLDonkey is a client for the mldonkey P2P network.

%description -n kde4-kmldonkey -l pl.UTF-8
KMLDonkey to klient dla sieci P2P mldonkey.

%prep
%setup -q -n %{orgname}-%{snap}

%build
install -d build
cd build
%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		-LCMS_DIR=%{_libdir} \
		../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

#cd kwlan
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

#%find_lang kmldonky	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde4-kwlan
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwlan
%{_desktopdir}/kde4/kwlan.desktop
%{_datadir}/apps/kwlan
%{_iconsdir}/hicolor/*/apps/kwlan-*.png
%{_iconsdir}/hicolor/*/apps/kwlan.png
%{_iconsdir}/hicolor/*/apps/kwlanmain.png

%files -n kde4-kftpgrabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kftpgrabber
%{_libdir}/kde4/kftpimportplugin_filezilla3.so
%{_libdir}/kde4/kftpimportplugin_gftp.so
%{_libdir}/kde4/kftpimportplugin_kftp.so
%{_libdir}/kde4/kftpimportplugin_ncftp.so
%{_libdir}/libkftpinterfaces.so
%attr(755,root,root) %{_libdir}/libkftpinterfaces.so.4
%attr(755,root,root) %{_libdir}/libkftpinterfaces.so.4.2.0
%{_desktopdir}/kde4/kftpgrabber.desktop
%{_datadir}/apps/kftpgrabber
%{_iconsdir}/hicolor/*/apps/kftpgrabber.png
%{_datadir}/kde4/services/kftpbookmarkimportplugin.desktop
%{_datadir}/kde4/services/kftpimportplugin_filezilla3.desktop
%{_datadir}/kde4/services/kftpimportplugin_gftp.desktop
%{_datadir}/kde4/services/kftpimportplugin_kftp.desktop
%{_datadir}/kde4/services/kftpimportplugin_ncftp.desktop

%files -n kde4-kmldonkey
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmldonkey
%attr(755,root,root) %{_libdir}/liblibkmldonkey.so
%attr(755,root,root) %{_libdir}/liblibkmldonkey.so.?
%attr(755,root,root) %{_libdir}/liblibkmldonkey.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_kmldonkey.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kmldonkey.so
%{_desktopdir}/kde4/kmldonkey.desktop
%{_datadir}/apps/kmldonkey
%{_datadir}/kde4/services/plasma-engine-kmldonkey.desktop
%{_datadir}/kde4/services/plasma-applet-kmldonkey.desktop
%{_iconsdir}/hicolor/*/apps/kmldonkey.png
#%{_includedir}/kmldonkey

%attr(755,root,root) %{_libdir}/kde4/kio_gopher.so
%{_datadir}/kde4/services/gopher.protocol

##############################
#knewsticker-scripts
%{_datadir}/apps/knewsticker

%files -n  kde4-ktorrent
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktorrent
%attr(755,root,root) %{_bindir}/ktupnptest
%attr(755,root,root) %{_libdir}/libktupnp.so
%attr(755,root,root) %{_libdir}/libktupnp.so.?
%attr(755,root,root) %{_libdir}/libktupnp.so.*.*.*
%attr(755,root,root) %{_libdir}/libktcore.so
%attr(755,root,root) %{_libdir}/libbtcore.so.?
%attr(755,root,root) %{_libdir}/libbtcore.so.*.*.*
%attr(755,root,root) %{_libdir}/libbtcore.so
%attr(755,root,root) %{_libdir}/libktcore.so.?
%attr(755,root,root) %{_libdir}/libktcore.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/ktlogviewerplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktsearchplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktstatsplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktwebinterfaceplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktupnpplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktscanfolderplugin.so
#%attr(755,root,root) %{_libdir}/kde4/ktbitfinderplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktipfilterplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktbwschedulerplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktmediaplayerplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktinfowidgetplugin.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_ktorrent.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_ktorrent.so

%{_datadir}/kde4/services/plasma-applet-ktorrent.desktop
%{_datadir}/kde4/services/plasma-dataengine-ktorrent.desktop
%{_datadir}/apps/ktorrent
%{_desktopdir}/kde4/ktorrent.desktop

%{_datadir}/kde4/services/ktlogviewerplugin.desktop
%{_datadir}/kde4/services/ktsearchplugin.desktop
%{_datadir}/kde4/services/ktstatsplugin.desktop
%{_datadir}/kde4/services/ktwebinterfaceplugin.desktop
%{_datadir}/kde4/services/ktupnpplugin.desktop
%{_datadir}/kde4/services/ktscanfolderplugin.desktop
#%{_datadir}/kde4/services/ktbitfinderplugin.desktop
%{_datadir}/kde4/services/ktipfilterplugin.desktop
%{_datadir}/kde4/services/ktbwschedulerplugin.desktop
%{_datadir}/kde4/services/ktmediaplayerplugin.desktop
%{_datadir}/kde4/services/ktinfowidgetplugin.desktop
%{_datadir}/kde4/servicetypes/ktorrentplugin.desktop

%{_iconsdir}/hicolor/*/actions/kt-*.png
%{_iconsdir}/hicolor/*/apps/ktorrent.png
%{_includedir}/libbtcore
