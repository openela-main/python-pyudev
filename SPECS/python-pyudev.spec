%global srcname pyudev

%if 0%{?rhel} == 8
%bcond_with python2
%bcond_with qt4
%else
%bcond_without python2
%bcond_without qt4
%endif

Name:             python-%{srcname}
Version:          0.21.0
Release:          7%{?dist}
Summary:          A libudev binding

License:          LGPLv2+
URL:              http://pypi.python.org/pypi/pyudev
Source0:          https://pypi.io/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:        noarch

%description
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%if %{with python2}
%package -n python2-%{srcname}
Summary:          A libudev binding
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:    python2-devel
BuildRequires:    python2-setuptools

# Dependencies for libraries loaded through ctypes
# glibc is needed for pipe2. This is not needed in the python3 package.
Requires:         glibc

# Needed for libudev
Requires:         systemd-libs

# Used for python2/3 compatibility
Requires:         python2-six

%description -n python2-%{srcname}
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%package -n python2-%{srcname}-glib
Summary:          GLib integration for pyudev

Requires:         pygobject2
Requires:         python2-%{srcname} = %{version}-%{release}

%description -n python2-%{srcname}-glib
GLib integration for pyudev.

This package provides a module pyudev.glib that contains classes for
integrating a pyudev monitor with the GLib main loop.

%if %{with qt4}
%package -n python2-%{srcname}-qt4
Summary:          Qt4 integration for pyudev

Requires:         PyQt4
Requires:         python2-%{srcname} = %{version}-%{release}

%description -n python2-%{srcname}-qt4
Qt4 integration for pyudev.

This package provides a module pyudev.pyqt4 that contains classes for
integrating a pyudev monitor with the Qt4 main loop.
%endif

%package -n python2-%{srcname}-qt5
Summary:          Qt5 integration for pyudev

Requires:         python-qt5
Requires:         python2-%{srcname} = %{version}-%{release}

%description -n python2-%{srcname}-qt5
Qt5 integration for pyudev.

This package provides a module pyudev.pyqt5 that contains classes for
integrating a pyudev monitor with the Qt4 main loop.

%package -n python2-%{srcname}-pyside
Summary:           PySide integration for pyudev

Requires:          python-pyside
Requires:          python2-%{srcname} = %{version}-%{release}

%description -n python2-%{srcname}-pyside
PySide integration for pyudev.

This package provides a module pyudev.pyside that contains classes for
integrating a pyudev monitor with the PySide main loop.

%package -n python2-%{srcname}-wx
Summary:            wxPython integration for pyudev

Requires:           wxPython
Requires:           python2-%{srcname} = %{version}-%{release}

%description -n python2-%{srcname}-wx
wxPython integration for pyudev.

This package provides a module pyudev.wx that contains classes for
integrating a pyudev montior with the wxPython main loop.
%endif

%package -n python3-%{srcname}
Summary:          A libudev binding
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools

# Needed for libudev, loaded through ctypes
Requires:         systemd-libs

# Used for python2/3 compatibility
Requires:         python3-six

%description -n python3-%{srcname}
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%if %{with qt4}
%package -n python3-%{srcname}-qt4
Summary:          Qt4 integration for pyudev

Requires:         python3-PyQt4
Requires:         python3-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}-qt4
Qt4 integration for pyudev.

This package provides a module pyudev.pyqt4 that contains classes for
integrating a pyudev monitor with the Qt4 main loop.
%endif

%package -n python3-%{srcname}-qt5
Summary:          Qt5 integration for pyudev

Requires:         python3-qt5
Requires:         python3-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}-qt5
Qt5 integration for pyudev.

This package provides a module pyudev.pyqt5 that contains classes for
integrating a pyudev monitor with the Qt5 main loop.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf pyudev.egg-info

%build
%if %{with python2}
%py2_build
%endif

%py3_build

%install
%if %{with python2}
%py2_install
%endif

%py3_install

%if %{with python2}
%files -n python2-%{srcname}
%license COPYING
%doc README.rst CHANGES.rst
%{python2_sitelib}/pyudev/
%{python2_sitelib}/pyudev-%{version}-*.egg-info
%exclude %{python2_sitelib}/pyudev/glib.py*
%exclude %{python2_sitelib}/pyudev/pyqt4.py*
%exclude %{python2_sitelib}/pyudev/pyqt5.py*
%exclude %{python2_sitelib}/pyudev/pyside.py*
%exclude %{python2_sitelib}/pyudev/wx.py*

%files -n python2-%{srcname}-glib
%license COPYING
%{python2_sitelib}/pyudev/glib.py*

%if %{with qt4}
%files -n python2-%{srcname}-qt4
%license COPYING
%{python2_sitelib}/pyudev/pyqt4.py*
%endif

%files -n python2-%{srcname}-qt5
%license COPYING
%{python2_sitelib}/pyudev/pyqt5.py*

%files -n python2-%{srcname}-pyside
%license COPYING
%{python2_sitelib}/pyudev/pyside.py*

%files -n python2-%{srcname}-wx
%license COPYING
%{python2_sitelib}/pyudev/wx.py*
%endif

%files -n python3-%{srcname}
%license COPYING
%doc README.rst CHANGES.rst
%{python3_sitelib}/pyudev
%{python3_sitelib}/pyudev-%{version}-*.egg-info
%exclude %{python3_sitelib}/pyudev/glib.py
%exclude %{python3_sitelib}/pyudev/__pycache__/glib.*
%exclude %{python3_sitelib}/pyudev/pyqt4.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt4.*
%exclude %{python3_sitelib}/pyudev/pyqt5.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt5.*
%exclude %{python3_sitelib}/pyudev/pyside.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyside.*
%exclude %{python3_sitelib}/pyudev/wx.py
%exclude %{python3_sitelib}/pyudev/__pycache__/wx.*

%if %{with qt4}
%files -n python3-%{srcname}-qt4
%license COPYING
%{python3_sitelib}/pyudev/pyqt4.py
%{python3_sitelib}/pyudev/__pycache__/pyqt4.*
%endif

%files -n python3-%{srcname}-qt5
%license COPYING
%{python3_sitelib}/pyudev/pyqt5.py
%{python3_sitelib}/pyudev/__pycache__/pyqt5.*

%changelog
* Thu Jun 14 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 0.21.0-7
- Dropped qt4 from RHEL-8 (#1591123)

* Thu May 17 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.21.0-6
- Bumped release to fix conflict caused by automerge

* Mon Apr 30 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.21.0-5
- Dropped python2 from RHEL-8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Kevin Fenzi <kevin@scrye.com> - 0.21.0-2
- Rebuild for Python 3.6

* Fri Jul 29 2016 mulhern <amulhern@redhat.com> - 0.21.1
- Deprecate use of Device object as mapping from udev property names to values
- Add a Properties class and a Device.properties() method for udev properties
- Fix places where Device object was incorrectly used in a boolean context
- Return an empty string, not None, if the property value is an empty string
- Exceptions re-raised from libudev calls now have a message string
- Insert a warning about using a Device in a boolean context in docs
- Infrastructure for vagrant tests is removed
- Various internal refactorings
- Extensive test improvements
- Numerous documentation fixes

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 2 2016 mulhern <amulhern@redhat.com> - 0.20.0
- Remove parsing code added in previous release
- No longer do CI for Python 2.6
- Eliminate all wildcard imports and __all__ statements
- No longer use deprecated Device.from_sys_path() method
- Minor pylint induced changes
- Documentation fixes

* Mon Feb 08 2016 mulhern <amulhern@redhat.com> - 0.19.0
- Never raise a DeviceNotFoundError when iterating over a device enumeration
- Device.subsystem() now returns None if device has no subsystem
- Add DeprecationWarnings to deprecated Device methods
- Replace "/" with "!" in Device.from_name() sys_name parameter
- Add some unstable classes for parsing some kinds of values
- Make version info more like Python's including micro numbers and levels
- Refactor some internal modules into subdirectories
- Work on tests and reproducers

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 mulhern <amulhern@redhat.com> - 0.18.1
- Restore raising KeyError in astring, asint, asbool methods in Attributes
- Add dependency on six package
- pyudev sources now in src directory
- Added support for pyqt5 monitor observer
- Added discover module, which looks up a device on limited information
- DeviceNotFoundError is no longer a subtype of LookupError
- Attributes class no longer extends Mapping class
- Attributes class no longer inherits [] operator and other Mapping methods
- Attributes class object are no longer iterable or indexable and have no length
- Attributes.available_attributes property added
- Attributes.get() method, with usual semantics explicitly defined
- Device.from_* methods are deprecated, use Devices.from_* methods instead
- Device.from_device_number() now raises DeviceNotFoundByNumberError
- Devices.from_interface_index() method added
- Devices.from_kernel_device() method added

* Thu Dec  3 2015 David Shea <dshea@redhat.com> - 0.17-4
- Add requires for things that are required
- Split the main-loop integration modules into separate packages

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 0.17-3
- Rebuilt for Python3.5 rebuild

* Wed Sep 15 2015 David Shea <dshea@redhat.com> - 0.17.1-2
- Fix a typo in the python3-pyudev Provides

* Mon Sep 14 2015 David Shea <dshea@redhat.com> - 0.17.1-1
- Really start the monitor on pyudev.Monitor.poll()
- Force non-blocking IO in pyudev.Monitor to avoid blocking on receiving the device
- Set proper flags on pipe fs
- Handle irregular polling events properly
- Rename MonitorObserver GUI classes and deprecate the old ones
- Remove patches for #1170337 and #1230773 that are now part of upstream
- Switch to new packaging guidelines which renames python-pyudev to python2-pyudev

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 David Shea <dshea@redhat.com> - 0.16.1-3
- Retry interrupted system calls (#1230773)
- Rearrange the build process to match current packaging recommendations

* Wed Jan 28 2015 David Shea <dshea@redhat.com> - 0.16.1-2
- Use %%license for the license file

* Wed Dec 10 2014 David Shea <dshea@redhat.com> - 0.16.1-1
- Update to pyudev-0.16.1 (#880644)
- Apply a patch from upstream to remove a global reference to libudev (#1170337)

* Wed Dec 10 2014 David Shea <dshea@redhat.com> - 0.15-7
- Fix license tag (LGPL -> LGPLv2+) (#990579)
- Remove rst tags from description
- Remove unnecessary requires and buildrequires (#1095459)
- Avoid packaging upstream egg-info files
- Add a python3 package
- Drop the Group tag which wasn't even the right group

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Chris Lockfort <clockfort@redhat.com> 0.15-3
- Reflect rawhide merging udev into systemd
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Mon Jun 18 2012 Chris Lockfort <clockfort@redhat.com> 0.15-1
- initial package
