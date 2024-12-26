#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : pimcommon
Version  : 24.08.2
Release  : 107
URL      : https://download.kde.org/stable/release-service/24.08.2/src/pimcommon-24.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.2/src/pimcommon-24.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.2/src/pimcommon-24.08.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
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
BuildRequires : gnupg
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
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n pimcommon-24.08.2
cd %{_builddir}/pimcommon-24.08.2
pushd ..
cp -a pimcommon-24.08.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728755781
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
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1728755781
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pimcommon
cp %{_builddir}/pimcommon-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/pimcommon/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pimcommon/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pimcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/pimcommon-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pimcommon/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/pimcommon-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/pimcommon/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libpimcommon6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/pimcommon.categories
/usr/share/qlogging-categories6/pimcommon.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/PimCommon/PimCommon/AbstractGenericPlugin
/usr/include/KPim6/PimCommon/PimCommon/AbstractGenericPluginInterface
/usr/include/KPim6/PimCommon/PimCommon/BroadcastStatus
/usr/include/KPim6/PimCommon/PimCommon/ConfigureImmutableWidgetUtils
/usr/include/KPim6/PimCommon/PimCommon/ConfigurePluginDialog
/usr/include/KPim6/PimCommon/PimCommon/ConfigurePluginsListWidget
/usr/include/KPim6/PimCommon/PimCommon/ConfigurePluginsWidget
/usr/include/KPim6/PimCommon/PimCommon/CustomLogWidget
/usr/include/KPim6/PimCommon/PimCommon/CustomToolsPlugin
/usr/include/KPim6/PimCommon/PimCommon/CustomToolsPluginManager
/usr/include/KPim6/PimCommon/PimCommon/CustomToolsViewInterface
/usr/include/KPim6/PimCommon/PimCommon/CustomToolsWidgetng
/usr/include/KPim6/PimCommon/PimCommon/CustomTreeView
/usr/include/KPim6/PimCommon/PimCommon/GenericPlugin
/usr/include/KPim6/PimCommon/PimCommon/GenericPluginManager
/usr/include/KPim6/PimCommon/PimCommon/KActionMenuChangeCase
/usr/include/KPim6/PimCommon/PimCommon/LineEditWithAutoCorrection
/usr/include/KPim6/PimCommon/PimCommon/LineEditWithCompleterNg
/usr/include/KPim6/PimCommon/PimCommon/NeedUpdateVersionUtils
/usr/include/KPim6/PimCommon/PimCommon/NeedUpdateVersionWidget
/usr/include/KPim6/PimCommon/PimCommon/NetworkManager
/usr/include/KPim6/PimCommon/PimCommon/PimUtil
/usr/include/KPim6/PimCommon/PimCommon/PluginUtil
/usr/include/KPim6/PimCommon/PimCommon/PurposeMenuMessageWidget
/usr/include/KPim6/PimCommon/PimCommon/PurposeMenuWidget
/usr/include/KPim6/PimCommon/PimCommon/RenameFileDialog
/usr/include/KPim6/PimCommon/PimCommon/ShareServiceUrlManager
/usr/include/KPim6/PimCommon/PimCommon/SimpleStringListEditor
/usr/include/KPim6/PimCommon/PimCommon/SpellCheckLineEdit
/usr/include/KPim6/PimCommon/PimCommon/TemplateListWidget
/usr/include/KPim6/PimCommon/PimCommon/TemplateManager
/usr/include/KPim6/PimCommon/pimcommon/abstractgenericplugin.h
/usr/include/KPim6/PimCommon/pimcommon/abstractgenericplugininterface.h
/usr/include/KPim6/PimCommon/pimcommon/broadcaststatus.h
/usr/include/KPim6/PimCommon/pimcommon/configureimmutablewidgetutils.h
/usr/include/KPim6/PimCommon/pimcommon/configureplugindialog.h
/usr/include/KPim6/PimCommon/pimcommon/configurepluginslistwidget.h
/usr/include/KPim6/PimCommon/pimcommon/configurepluginswidget.h
/usr/include/KPim6/PimCommon/pimcommon/customlogwidget.h
/usr/include/KPim6/PimCommon/pimcommon/customtoolsplugin.h
/usr/include/KPim6/PimCommon/pimcommon/customtoolspluginmanager.h
/usr/include/KPim6/PimCommon/pimcommon/customtoolsviewinterface.h
/usr/include/KPim6/PimCommon/pimcommon/customtoolswidgetng.h
/usr/include/KPim6/PimCommon/pimcommon/customtreeview.h
/usr/include/KPim6/PimCommon/pimcommon/genericplugin.h
/usr/include/KPim6/PimCommon/pimcommon/genericpluginmanager.h
/usr/include/KPim6/PimCommon/pimcommon/imapresourcesettings.h
/usr/include/KPim6/PimCommon/pimcommon/kactionmenuchangecase.h
/usr/include/KPim6/PimCommon/pimcommon/lineeditwithautocorrection.h
/usr/include/KPim6/PimCommon/pimcommon/lineeditwithcompleterng.h
/usr/include/KPim6/PimCommon/pimcommon/needupdateversionutils.h
/usr/include/KPim6/PimCommon/pimcommon/needupdateversionwidget.h
/usr/include/KPim6/PimCommon/pimcommon/networkmanager.h
/usr/include/KPim6/PimCommon/pimcommon/pimcommon_export.h
/usr/include/KPim6/PimCommon/pimcommon/pimutil.h
/usr/include/KPim6/PimCommon/pimcommon/pluginutil.h
/usr/include/KPim6/PimCommon/pimcommon/purposemenumessagewidget.h
/usr/include/KPim6/PimCommon/pimcommon/purposemenuwidget.h
/usr/include/KPim6/PimCommon/pimcommon/renamefiledialog.h
/usr/include/KPim6/PimCommon/pimcommon/shareserviceurlmanager.h
/usr/include/KPim6/PimCommon/pimcommon/simplestringlisteditor.h
/usr/include/KPim6/PimCommon/pimcommon/spellchecklineedit.h
/usr/include/KPim6/PimCommon/pimcommon/templatelistwidget.h
/usr/include/KPim6/PimCommon/pimcommon/templatemanager.h
/usr/include/KPim6/PimCommon/pimcommon_version.h
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/AddresseeLineEdit
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/CheckedCollectionWidget
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/CollectionAclPage
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/CollectionTypeUtil
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/CompletionConfigureDialog
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/CompletionOrderEditor
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/ContentTypeWidget
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/CreateResource
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/GenericPluginInterface
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/ImapAclAttribute
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/ImapResourceCapabilitiesManager
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/IncidencesForWidget
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/LdapSearchDialog
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/MailUtil
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/ManageServerSideSubscriptionJob
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/PluginInterface
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/ProgressManagerAkonadi
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/RecentAddresses
/usr/include/KPim6/PimCommonAkonadi/PimCommonAkonadi/SelectMultiCollectionDialog
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/addresseelineedit.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/checkedcollectionwidget.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/collectionaclpage.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/collectiontypeutil.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/completionconfiguredialog.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/completionordereditor.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/contenttypewidget.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/createresource.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/genericplugininterface.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/imapaclattribute.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/imapresourcecapabilitiesmanager.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/incidencesforwidget.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/ldapsearchdialog.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/mailutil.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/manageserversidesubscriptionjob.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/pimcommonakonadi_export.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/plugininterface.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/progressmanagerakonadi.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/recentaddresses.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi/selectmulticollectiondialog.h
/usr/include/KPim6/PimCommonAkonadi/pimcommonakonadi_version.h
/usr/lib64/cmake/KPim6PimCommon/KPim6PimCommonConfig.cmake
/usr/lib64/cmake/KPim6PimCommon/KPim6PimCommonConfigVersion.cmake
/usr/lib64/cmake/KPim6PimCommon/KPim6PimCommonTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6PimCommon/KPim6PimCommonTargets.cmake
/usr/lib64/cmake/KPim6PimCommonAkonadi/KPim6PimCommonAkonadiConfig.cmake
/usr/lib64/cmake/KPim6PimCommonAkonadi/KPim6PimCommonAkonadiConfigVersion.cmake
/usr/lib64/cmake/KPim6PimCommonAkonadi/KPim6PimCommonAkonadiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6PimCommonAkonadi/KPim6PimCommonAkonadiTargets.cmake
/usr/lib64/libKPim6PimCommon.so
/usr/lib64/libKPim6PimCommonAkonadi.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6PimCommon.so.6.2.2
/V3/usr/lib64/libKPim6PimCommonAkonadi.so.6.2.2
/V3/usr/lib64/qt6/plugins/designer/pimcommon6akonadiwidgets.so
/V3/usr/lib64/qt6/plugins/designer/pimcommon6widgets.so
/usr/lib64/libKPim6PimCommon.so.6
/usr/lib64/libKPim6PimCommon.so.6.2.2
/usr/lib64/libKPim6PimCommonAkonadi.so.6
/usr/lib64/libKPim6PimCommonAkonadi.so.6.2.2
/usr/lib64/qt6/plugins/designer/pimcommon6akonadiwidgets.so
/usr/lib64/qt6/plugins/designer/pimcommon6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pimcommon/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/pimcommon/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/pimcommon/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/pimcommon/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/pimcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libpimcommon6.lang
%defattr(-,root,root,-)

