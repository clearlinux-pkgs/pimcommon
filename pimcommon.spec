#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : pimcommon
Version  : 23.08.2
Release  : 75
URL      : https://download.kde.org/stable/release-service/23.08.2/src/pimcommon-23.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.2/src/pimcommon-23.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.2/src/pimcommon-23.08.2.tar.xz.sig
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
%setup -q -n pimcommon-23.08.2
cd %{_builddir}/pimcommon-23.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697403962
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697403962
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
/usr/include/KPim5/PimCommon/PimCommon/AbstractGenericPlugin
/usr/include/KPim5/PimCommon/PimCommon/AbstractGenericPluginInterface
/usr/include/KPim5/PimCommon/PimCommon/BroadcastStatus
/usr/include/KPim5/PimCommon/PimCommon/ConfigureImmutableWidgetUtils
/usr/include/KPim5/PimCommon/PimCommon/ConfigurePluginDialog
/usr/include/KPim5/PimCommon/PimCommon/ConfigurePluginsListWidget
/usr/include/KPim5/PimCommon/PimCommon/ConfigurePluginsWidget
/usr/include/KPim5/PimCommon/PimCommon/CustomLogWidget
/usr/include/KPim5/PimCommon/PimCommon/CustomToolsPlugin
/usr/include/KPim5/PimCommon/PimCommon/CustomToolsPluginManager
/usr/include/KPim5/PimCommon/PimCommon/CustomToolsViewInterface
/usr/include/KPim5/PimCommon/PimCommon/CustomToolsWidgetng
/usr/include/KPim5/PimCommon/PimCommon/CustomTreeView
/usr/include/KPim5/PimCommon/PimCommon/EmailValidator
/usr/include/KPim5/PimCommon/PimCommon/GenericPlugin
/usr/include/KPim5/PimCommon/PimCommon/GenericPluginManager
/usr/include/KPim5/PimCommon/PimCommon/KActionMenuChangeCase
/usr/include/KPim5/PimCommon/PimCommon/LineEditWithAutoCorrection
/usr/include/KPim5/PimCommon/PimCommon/LineEditWithCompleterNg
/usr/include/KPim5/PimCommon/PimCommon/MigrateApplicationFiles
/usr/include/KPim5/PimCommon/PimCommon/MigrateFileInfo
/usr/include/KPim5/PimCommon/PimCommon/NetworkManager
/usr/include/KPim5/PimCommon/PimCommon/PimUtil
/usr/include/KPim5/PimCommon/PimCommon/PluginUtil
/usr/include/KPim5/PimCommon/PimCommon/PurposeMenuWidget
/usr/include/KPim5/PimCommon/PimCommon/RenameFileDialog
/usr/include/KPim5/PimCommon/PimCommon/ShareServiceUrlManager
/usr/include/KPim5/PimCommon/PimCommon/SimpleStringListEditor
/usr/include/KPim5/PimCommon/PimCommon/SpellCheckLineEdit
/usr/include/KPim5/PimCommon/PimCommon/TemplateListWidget
/usr/include/KPim5/PimCommon/PimCommon/TemplateManager
/usr/include/KPim5/PimCommon/config-pimcommon.h
/usr/include/KPim5/PimCommon/pimcommon/abstractgenericplugin.h
/usr/include/KPim5/PimCommon/pimcommon/abstractgenericplugininterface.h
/usr/include/KPim5/PimCommon/pimcommon/broadcaststatus.h
/usr/include/KPim5/PimCommon/pimcommon/configureimmutablewidgetutils.h
/usr/include/KPim5/PimCommon/pimcommon/configureplugindialog.h
/usr/include/KPim5/PimCommon/pimcommon/configurepluginslistwidget.h
/usr/include/KPim5/PimCommon/pimcommon/configurepluginswidget.h
/usr/include/KPim5/PimCommon/pimcommon/customlogwidget.h
/usr/include/KPim5/PimCommon/pimcommon/customtoolsplugin.h
/usr/include/KPim5/PimCommon/pimcommon/customtoolspluginmanager.h
/usr/include/KPim5/PimCommon/pimcommon/customtoolsviewinterface.h
/usr/include/KPim5/PimCommon/pimcommon/customtoolswidgetng.h
/usr/include/KPim5/PimCommon/pimcommon/customtreeview.h
/usr/include/KPim5/PimCommon/pimcommon/emailvalidator.h
/usr/include/KPim5/PimCommon/pimcommon/genericplugin.h
/usr/include/KPim5/PimCommon/pimcommon/genericpluginmanager.h
/usr/include/KPim5/PimCommon/pimcommon/imapresourcesettings.h
/usr/include/KPim5/PimCommon/pimcommon/kactionmenuchangecase.h
/usr/include/KPim5/PimCommon/pimcommon/lineeditwithautocorrection.h
/usr/include/KPim5/PimCommon/pimcommon/lineeditwithcompleterng.h
/usr/include/KPim5/PimCommon/pimcommon/migrateapplicationfiles.h
/usr/include/KPim5/PimCommon/pimcommon/migratefileinfo.h
/usr/include/KPim5/PimCommon/pimcommon/networkmanager.h
/usr/include/KPim5/PimCommon/pimcommon/pimcommon_export.h
/usr/include/KPim5/PimCommon/pimcommon/pimutil.h
/usr/include/KPim5/PimCommon/pimcommon/pluginutil.h
/usr/include/KPim5/PimCommon/pimcommon/purposemenuwidget.h
/usr/include/KPim5/PimCommon/pimcommon/renamefiledialog.h
/usr/include/KPim5/PimCommon/pimcommon/shareserviceurlmanager.h
/usr/include/KPim5/PimCommon/pimcommon/simplestringlisteditor.h
/usr/include/KPim5/PimCommon/pimcommon/spellchecklineedit.h
/usr/include/KPim5/PimCommon/pimcommon/templatelistwidget.h
/usr/include/KPim5/PimCommon/pimcommon/templatemanager.h
/usr/include/KPim5/PimCommon/pimcommon_version.h
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/AddresseeLineEdit
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/AnnotationDialog
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/CheckedCollectionWidget
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/CollectionAclPage
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/CollectionTypeUtil
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/CompletionConfigureDialog
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/CompletionOrderEditor
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/ContentTypeWidget
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/CreateResource
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/GenericPluginInterface
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/ImapAclAttribute
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/ImapResourceCapabilitiesManager
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/IncidencesForWidget
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/LdapSearchDialog
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/MailUtil
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/ManageServerSideSubscriptionJob
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/PluginInterface
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/ProgressManagerAkonadi
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/RecentAddresses
/usr/include/KPim5/PimCommonAkonadi/PimCommonAkonadi/SelectMultiCollectionDialog
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/addresseelineedit.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/annotationdialog.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/checkedcollectionwidget.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/collectionaclpage.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/collectiontypeutil.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/completionconfiguredialog.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/completionordereditor.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/contenttypewidget.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/createresource.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/genericplugininterface.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/imapaclattribute.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/imapresourcecapabilitiesmanager.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/incidencesforwidget.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/ldapsearchdialog.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/mailutil.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/manageserversidesubscriptionjob.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/pimcommonakonadi_export.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/plugininterface.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/progressmanagerakonadi.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/recentaddresses.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi/selectmulticollectiondialog.h
/usr/include/KPim5/PimCommonAkonadi/pimcommonakonadi_version.h
/usr/lib64/cmake/KPim5PimCommon/KPim5PimCommonConfig.cmake
/usr/lib64/cmake/KPim5PimCommon/KPim5PimCommonConfigVersion.cmake
/usr/lib64/cmake/KPim5PimCommon/KPim5PimCommonTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5PimCommon/KPim5PimCommonTargets.cmake
/usr/lib64/cmake/KPim5PimCommonAkonadi/KPim5PimCommonAkonadiConfig.cmake
/usr/lib64/cmake/KPim5PimCommonAkonadi/KPim5PimCommonAkonadiConfigVersion.cmake
/usr/lib64/cmake/KPim5PimCommonAkonadi/KPim5PimCommonAkonadiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5PimCommonAkonadi/KPim5PimCommonAkonadiTargets.cmake
/usr/lib64/libKPim5PimCommon.so
/usr/lib64/libKPim5PimCommonAkonadi.so
/usr/lib64/qt5/mkspecs/modules/qt_PimCommon.pri
/usr/lib64/qt5/mkspecs/modules/qt_PimCommonAkonadi.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5PimCommon.so.5.24.2
/V3/usr/lib64/libKPim5PimCommonAkonadi.so.5.24.2
/V3/usr/lib64/qt5/plugins/designer/pimcommon5akonadiwidgets.so
/V3/usr/lib64/qt5/plugins/designer/pimcommon5widgets.so
/usr/lib64/libKPim5PimCommon.so.5
/usr/lib64/libKPim5PimCommon.so.5.24.2
/usr/lib64/libKPim5PimCommonAkonadi.so.5
/usr/lib64/libKPim5PimCommonAkonadi.so.5.24.2
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

