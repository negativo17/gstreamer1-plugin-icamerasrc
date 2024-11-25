%global commit 0019b5d8af9d558aa7888218dfeeafef6104277a
%global date 20241121
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gstreamer1-plugin-icamerasrc
Summary:        GStreamer 1.0 Intel IPU6 camera plug-in
Version:        0
Release:        5.%{date}git%{shortcommit}%{?dist}
License:        LGPL-2.1-only
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/icamerasrc/archive/%{commit}/icamerasrc-%{shortcommit}.tar.gz
Patch0:         %{name}-videoformat.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(gstreamer-va-1.0)
BuildRequires:  pkgconfig(libcamhal)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-controller-1.0) >= 1.0.0

%description
This package provides the GStreamer 1.0 plug-in for MIPI camera.

%package devel
Summary:        GStreamer plug-in development files for Intel IPU6 camera
Requires:       gstreamer1-devel
Requires:       ipu6-camera-bins-devel
Requires:       ipu6-camera-hal-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This provides the necessary header files for IPU6 GStreamer plugin development.

%prep
%autosetup -p1 -n icamerasrc-%{commit}
autoreconf -vif

%build
export CHROME_SLIM_CAMHAL=ON
export STRIP_VIRTUAL_CHANNEL_CAMHAL=ON
%configure --enable-gstdrmformat
%make_build

%install
%make_install

%files
%license LICENSE
%{_libdir}/gstreamer-1.0/*
%{_libdir}/libgsticamerainterface-1.0.so.1
%{_libdir}/libgsticamerainterface-1.0.so.1.0.0

%files devel
%{_libdir}/libgsticamerainterface-1.0.so
%{_includedir}/gstreamer-1.0/gst/*
%{_libdir}/pkgconfig/*

%changelog
* Mon Nov 25 2024 Simone Caronni <negativo17@gmail.com> - 0-5.20241121git0019b5d
- Update to latest snapshot.

* Sun Oct 27 2024 Simone Caronni <negativo17@gmail.com> - 0-4.20240929git154fecf
- Update to latest snapshot.

* Thu Jul 04 2024 Simone Caronni <negativo17@gmail.com> - 0-3.20240606git1baecb1
- Use hal_adaptor for building and not the specific HALs:
  https://pkgs.rpmfusion.org/cgit/nonfree/gstreamer1-plugins-icamerasrc.git/commit/?id=00f24232d34443b62646f922d19fc798e6c7df5e
  Damn, that was the issue!

* Tue Jun 18 2024 Simone Caronni <negativo17@gmail.com> - 0-2.20240606git1baecb1
- Update to latest snapshot.

* Tue May 07 2024 Simone Caronni <negativo17@gmail.com> - 0-1.20240411git9b2f7e3
- First build.
