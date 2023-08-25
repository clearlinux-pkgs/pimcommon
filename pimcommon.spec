#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : pimcommon
Version  : 23.04.3
Release  : 68
URL      : https://download.kde.org/stable/release-service/23.04.3/src/pimcommon-23.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.3/src/pimcommon-23.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.3/src/pimcommon-23.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0
Requires: pimcommon-data = %{version}-%{release}
Requires: pimcommon-lib = %{version}-%{release}
Requires: pimcommon-license = %{version}-%{release}
Requires: pimcommon-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-search-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kimap-dev
BuildRequires : kimap-staticdev
BuildRequires : kldap-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : ktextaddons-dev
BuildRequires : libkdepim-dev
BuildRequires : purpose-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the pimcommon package.
Group: Data

%description data
data components for the pimcommon package.


%package dev
Summary: dev components for the pimcommon package.
Group: Development
Requires: pimcommon-lib = %{version}-%{release}
Requires: pimcommon-data = %{version}-%{release}
Provides: pimcommon-devel = %{version}-%{release}
Requires: pimcommon = %{version}-%{release}

%description dev
dev components for the pimcommon package.


%package lib
Summary: lib components for the pimcommon package.
Group: Libraries
Requires: pimcommon-data = %{version}-%{release}
Requires: pimcommon-license = %{version}-%{release}

%description lib
lib components for the pimcommon package.


%package license
Summary: license components for the pimcommon package.
Group: Default

%description license
license components for the pimcommon package.


%package locales
Summary: locales components for the pimcommon package.
Group: Default

%description locales
locales components for the pimcommon package.


%prep
%setup -q -n pimcommon-23.04.3
cd %{_builddir}/pimcommon-23.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688876130
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1688876130
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pimcommon
cp %{_builddir}/pimcommon-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/pimcommon/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pimcommon/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/pimcommon/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pimcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/pimcommon/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pimcommon/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/pimcommon/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/pimcommon/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/pimcommon-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/pimcommon/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libpimcommon
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/pimcommon.categories
/usr/share/qlogging-categories5/pimcommon.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/PimCommon/PimCommon/AbstractGenericPlugin
/usr/include/KF5/PimCommon/PimCommon/AbstractGenericPluginInterface
/usr/include/KF5/PimCommon/PimCommon/BroadcastStatus
/usr/include/KF5/PimCommon/PimCommon/ConfigureImmutableWidgetUtils
/usr/include/KF5/PimCommon/PimCommon/ConfigurePluginDialog
/usr/include/KF5/PimCommon/PimCommon/ConfigurePluginsListWidget
/usr/include/KF5/PimCommon/PimCommon/ConfigurePluginsWidget
/usr/include/KF5/PimCommon/PimCommon/CustomLogWidget
/usr/include/KF5/PimCommon/PimCommon/CustomToolsPlugin
/usr/include/KF5/PimCommon/PimCommon/CustomToolsPluginManager
/usr/include/KF5/PimCommon/PimCommon/CustomToolsViewInterface
/usr/include/KF5/PimCommon/PimCommon/CustomToolsWidgetng
/usr/include/KF5/PimCommon/PimCommon/CustomTreeView
/usr/include/KF5/PimCommon/PimCommon/EmailValidator
/usr/include/KF5/PimCommon/PimCommon/GenericPlugin
/usr/include/KF5/PimCommon/PimCommon/GenericPluginManager
/usr/include/KF5/PimCommon/PimCommon/KActionMenuChangeCase
/usr/include/KF5/PimCommon/PimCommon/LineEditWithAutoCorrection
/usr/include/KF5/PimCommon/PimCommon/LineEditWithCompleterNg
/usr/include/KF5/PimCommon/PimCommon/MigrateApplicationFiles
/usr/include/KF5/PimCommon/PimCommon/MigrateFileInfo
/usr/include/KF5/PimCommon/PimCommon/NetworkManager
/usr/include/KF5/PimCommon/PimCommon/PimUtil
/usr/include/KF5/PimCommon/PimCommon/PluginUtil
/usr/include/KF5/PimCommon/PimCommon/PurposeMenuWidget
/usr/include/KF5/PimCommon/PimCommon/RenameFileDialog
/usr/include/KF5/PimCommon/PimCommon/ShareServiceUrlManager
/usr/include/KF5/PimCommon/PimCommon/SimpleStringListEditor
/usr/include/KF5/PimCommon/PimCommon/SpellCheckLineEdit
/usr/include/KF5/PimCommon/PimCommon/TemplateListWidget
/usr/include/KF5/PimCommon/PimCommon/TemplateManager
/usr/include/KF5/PimCommon/pimcommon/abstractgenericplugin.h
/usr/include/KF5/PimCommon/pimcommon/abstractgenericplugininterface.h
/usr/include/KF5/PimCommon/pimcommon/broadcaststatus.h
/usr/include/KF5/PimCommon/pimcommon/config-pimcommon.h
/usr/include/KF5/PimCommon/pimcommon/configureimmutablewidgetutils.h
/usr/include/KF5/PimCommon/pimcommon/configureplugindialog.h
/usr/include/KF5/PimCommon/pimcommon/configurepluginslistwidget.h
/usr/include/KF5/PimCommon/pimcommon/configurepluginswidget.h
/usr/include/KF5/PimCommon/pimcommon/customlogwidget.h
/usr/include/KF5/PimCommon/pimcommon/customtoolsplugin.h
/usr/include/KF5/PimCommon/pimcommon/customtoolspluginmanager.h
/usr/include/KF5/PimCommon/pimcommon/customtoolsviewinterface.h
/usr/include/KF5/PimCommon/pimcommon/customtoolswidgetng.h
/usr/include/KF5/PimCommon/pimcommon/customtreeview.h
/usr/include/KF5/PimCommon/pimcommon/emailvalidator.h
/usr/include/KF5/PimCommon/pimcommon/genericplugin.h
/usr/include/KF5/PimCommon/pimcommon/genericpluginmanager.h
/usr/include/KF5/PimCommon/pimcommon/imapresourcesettings.h
/usr/include/KF5/PimCommon/pimcommon/kactionmenuchangecase.h
/usr/include/KF5/PimCommon/pimcommon/lineeditwithautocorrection.h
/usr/include/KF5/PimCommon/pimcommon/lineeditwithcompleterng.h
/usr/include/KF5/PimCommon/pimcommon/migrateapplicationfiles.h
/usr/include/KF5/PimCommon/pimcommon/migratefileinfo.h
/usr/include/KF5/PimCommon/pimcommon/networkmanager.h
/usr/include/KF5/PimCommon/pimcommon/pimcommon_export.h
/usr/include/KF5/PimCommon/pimcommon/pimutil.h
/usr/include/KF5/PimCommon/pimcommon/pluginutil.h
/usr/include/KF5/PimCommon/pimcommon/purposemenuwidget.h
/usr/include/KF5/PimCommon/pimcommon/renamefiledialog.h
/usr/include/KF5/PimCommon/pimcommon/shareserviceurlmanager.h
/usr/include/KF5/PimCommon/pimcommon/simplestringlisteditor.h
/usr/include/KF5/PimCommon/pimcommon/spellchecklineedit.h
/usr/include/KF5/PimCommon/pimcommon/templatelistwidget.h
/usr/include/KF5/PimCommon/pimcommon/templatemanager.h
/usr/include/KF5/PimCommon/pimcommon_version.h
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/AddresseeLineEdit
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/AnnotationDialog
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/CheckedCollectionWidget
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/CollectionAclPage
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/CollectionAnnotationsAttribute
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/CollectionTypeUtil
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/CompletionConfigureDialog
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/CompletionOrderEditor
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/ContentTypeWidget
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/CreateResource
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/GenericPluginInterface
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/ImapAclAttribute
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/ImapResourceCapabilitiesManager
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/IncidencesForWidget
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/LdapSearchDialog
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/MailUtil
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/ManageServerSideSubscriptionJob
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/PluginInterface
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/ProgressManagerAkonadi
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/RecentAddresses
/usr/include/KF5/PimCommonAkonadi/PimCommonAkonadi/SelectMultiCollectionDialog
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/addresseelineedit.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/annotationdialog.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/checkedcollectionwidget.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/collectionaclpage.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/collectionannotationsattribute.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/collectiontypeutil.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/completionconfiguredialog.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/completionordereditor.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/contenttypewidget.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/createresource.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/genericplugininterface.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/imapaclattribute.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/imapresourcecapabilitiesmanager.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/incidencesforwidget.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/ldapsearchdialog.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/mailutil.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/manageserversidesubscriptionjob.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/pimcommonakonadi_export.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/plugininterface.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/progressmanagerakonadi.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/recentaddresses.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi/selectmulticollectiondialog.h
/usr/include/KF5/PimCommonAkonadi/pimcommonakonadi_version.h
/usr/lib64/cmake/KF5PimCommon/KF5PimCommonConfig.cmake
/usr/lib64/cmake/KF5PimCommon/KF5PimCommonConfigVersion.cmake
/usr/lib64/cmake/KF5PimCommon/KF5PimCommonTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5PimCommon/KF5PimCommonTargets.cmake
/usr/lib64/cmake/KF5PimCommonAkonadi/KF5PimCommonAkonadiConfig.cmake
/usr/lib64/cmake/KF5PimCommonAkonadi/KF5PimCommonAkonadiConfigVersion.cmake
/usr/lib64/cmake/KF5PimCommonAkonadi/KF5PimCommonAkonadiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5PimCommonAkonadi/KF5PimCommonAkonadiTargets.cmake
/usr/lib64/libKF5PimCommon.so
/usr/lib64/libKF5PimCommonAkonadi.so
/usr/lib64/qt5/mkspecs/modules/qt_PimCommon.pri
/usr/lib64/qt5/mkspecs/modules/qt_PimCommonAkonadi.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5PimCommon.so.5.23.3
/V3/usr/lib64/libKF5PimCommonAkonadi.so.5.23.3
/V3/usr/lib64/qt5/plugins/designer/pimcommon5akonadiwidgets.so
/V3/usr/lib64/qt5/plugins/designer/pimcommon5widgets.so
/usr/lib64/libKF5PimCommon.so.5
/usr/lib64/libKF5PimCommon.so.5.23.3
/usr/lib64/libKF5PimCommonAkonadi.so.5
/usr/lib64/libKF5PimCommonAkonadi.so.5.23.3
/usr/lib64/qt5/plugins/designer/pimcommon5akonadiwidgets.so
/usr/lib64/qt5/plugins/designer/pimcommon5widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pimcommon/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/pimcommon/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/pimcommon/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/pimcommon/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/pimcommon/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/pimcommon/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/pimcommon/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/pimcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libpimcommon.lang
%defattr(-,root,root,-)

