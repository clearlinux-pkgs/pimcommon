#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : pimcommon
Version  : 20.12.0
Release  : 29
URL      : https://download.kde.org/stable/release-service/20.12.0/src/pimcommon-20.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.0/src/pimcommon-20.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.0/src/pimcommon-20.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0
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
BuildRequires : grantleetheme-dev
BuildRequires : karchive-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcmutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcontacts-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kimap-dev
BuildRequires : kimap-staticdev
BuildRequires : kio-dev
BuildRequires : kitemmodels-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kldap-dev
BuildRequires : kmime-dev
BuildRequires : knewstuff-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kservice-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : libkdepim-dev
BuildRequires : purpose-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n pimcommon-20.12.0
cd %{_builddir}/pimcommon-20.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607912759
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1607912759
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pimcommon
cp %{_builddir}/pimcommon-20.12.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/pimcommon/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/pimcommon-20.12.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pimcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/pimcommon-20.12.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/pimcommon/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/pimcommon-20.12.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pimcommon/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/pimcommon-20.12.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/pimcommon/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/pimcommon-20.12.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/pimcommon/7d9831e05094ce723947d729c2a46a09d6e90275
pushd clr-build
%make_install
popd
%find_lang libpimcommon

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/pimcommon.categories
/usr/share/qlogging-categories5/pimcommon.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/PimCommon/AbstractGenericPlugin
/usr/include/KF5/PimCommon/AbstractGenericPluginInterface
/usr/include/KF5/PimCommon/AutoCorrection
/usr/include/KF5/PimCommon/AutoCorrectionLanguage
/usr/include/KF5/PimCommon/AutoCorrectionWidget
/usr/include/KF5/PimCommon/BroadcastStatus
/usr/include/KF5/PimCommon/ConfigureImmutableWidgetUtils
/usr/include/KF5/PimCommon/ConfigurePluginDialog
/usr/include/KF5/PimCommon/ConfigurePluginsListWidget
/usr/include/KF5/PimCommon/ConfigurePluginsWidget
/usr/include/KF5/PimCommon/CustomLogWidget
/usr/include/KF5/PimCommon/CustomToolsPlugin
/usr/include/KF5/PimCommon/CustomToolsPluginManager
/usr/include/KF5/PimCommon/CustomToolsViewInterface
/usr/include/KF5/PimCommon/CustomToolsWidgetng
/usr/include/KF5/PimCommon/CustomTreeView
/usr/include/KF5/PimCommon/EmailValidator
/usr/include/KF5/PimCommon/GenericPlugin
/usr/include/KF5/PimCommon/GenericPluginManager
/usr/include/KF5/PimCommon/KActionMenuChangeCase
/usr/include/KF5/PimCommon/KPimPrintPreviewDialog
/usr/include/KF5/PimCommon/LineEditWithAutoCorrection
/usr/include/KF5/PimCommon/LineEditWithCompleterNg
/usr/include/KF5/PimCommon/LogActivitiesManager
/usr/include/KF5/PimCommon/MigrateApplicationFiles
/usr/include/KF5/PimCommon/MigrateFileInfo
/usr/include/KF5/PimCommon/NetworkManager
/usr/include/KF5/PimCommon/PimCommonSettings
/usr/include/KF5/PimCommon/PimUtil
/usr/include/KF5/PimCommon/PluginUtil
/usr/include/KF5/PimCommon/PurposeMenuWidget
/usr/include/KF5/PimCommon/RenameFileDialog
/usr/include/KF5/PimCommon/RichTexteditWithAutoCorrection
/usr/include/KF5/PimCommon/ShareServiceUrlManager
/usr/include/KF5/PimCommon/SimpleStringListEditor
/usr/include/KF5/PimCommon/SpellCheckLineEdit
/usr/include/KF5/PimCommon/TemplateListWidget
/usr/include/KF5/PimCommon/TemplateManager
/usr/include/KF5/PimCommon/TranslatorWidget
/usr/include/KF5/PimCommonAkonadi/AddresseeLineEdit
/usr/include/KF5/PimCommonAkonadi/AnnotationDialog
/usr/include/KF5/PimCommonAkonadi/CheckedCollectionWidget
/usr/include/KF5/PimCommonAkonadi/CollectionAclPage
/usr/include/KF5/PimCommonAkonadi/CollectionAnnotationsAttribute
/usr/include/KF5/PimCommonAkonadi/CollectionTypeUtil
/usr/include/KF5/PimCommonAkonadi/CompletionConfigureDialog
/usr/include/KF5/PimCommonAkonadi/CompletionOrderEditor
/usr/include/KF5/PimCommonAkonadi/ContentTypeWidget
/usr/include/KF5/PimCommonAkonadi/CreateResource
/usr/include/KF5/PimCommonAkonadi/GenericPluginInterface
/usr/include/KF5/PimCommonAkonadi/ImapAclAttribute
/usr/include/KF5/PimCommonAkonadi/ImapResourceCapabilitiesManager
/usr/include/KF5/PimCommonAkonadi/IncidencesForWidget
/usr/include/KF5/PimCommonAkonadi/LdapSearchDialog
/usr/include/KF5/PimCommonAkonadi/MailUtil
/usr/include/KF5/PimCommonAkonadi/ManageServerSideSubscriptionJob
/usr/include/KF5/PimCommonAkonadi/PluginInterface
/usr/include/KF5/PimCommonAkonadi/ProgressManagerAkonadi
/usr/include/KF5/PimCommonAkonadi/RecentAddresses
/usr/include/KF5/PimCommonAkonadi/SelectMultiCollectionDialog
/usr/include/KF5/pimcommon/abstractgenericplugin.h
/usr/include/KF5/pimcommon/abstractgenericplugininterface.h
/usr/include/KF5/pimcommon/autocorrection.h
/usr/include/KF5/pimcommon/autocorrectionlanguage.h
/usr/include/KF5/pimcommon/autocorrectionwidget.h
/usr/include/KF5/pimcommon/broadcaststatus.h
/usr/include/KF5/pimcommon/configureimmutablewidgetutils.h
/usr/include/KF5/pimcommon/configureplugindialog.h
/usr/include/KF5/pimcommon/configurepluginslistwidget.h
/usr/include/KF5/pimcommon/configurepluginswidget.h
/usr/include/KF5/pimcommon/customlogwidget.h
/usr/include/KF5/pimcommon/customtoolsplugin.h
/usr/include/KF5/pimcommon/customtoolspluginmanager.h
/usr/include/KF5/pimcommon/customtoolsviewinterface.h
/usr/include/KF5/pimcommon/customtoolswidgetng.h
/usr/include/KF5/pimcommon/customtreeview.h
/usr/include/KF5/pimcommon/emailvalidator.h
/usr/include/KF5/pimcommon/genericplugin.h
/usr/include/KF5/pimcommon/genericpluginmanager.h
/usr/include/KF5/pimcommon/imapresourcesettings.h
/usr/include/KF5/pimcommon/kactionmenuchangecase.h
/usr/include/KF5/pimcommon/kpimprintpreviewdialog.h
/usr/include/KF5/pimcommon/lineeditwithautocorrection.h
/usr/include/KF5/pimcommon/lineeditwithcompleterng.h
/usr/include/KF5/pimcommon/logactivitiesmanager.h
/usr/include/KF5/pimcommon/migrateapplicationfiles.h
/usr/include/KF5/pimcommon/migratefileinfo.h
/usr/include/KF5/pimcommon/networkmanager.h
/usr/include/KF5/pimcommon/pimcommon_export.h
/usr/include/KF5/pimcommon/pimcommonsetting_base.h
/usr/include/KF5/pimcommon/pimcommonsettings.h
/usr/include/KF5/pimcommon/pimutil.h
/usr/include/KF5/pimcommon/pluginutil.h
/usr/include/KF5/pimcommon/purposemenuwidget.h
/usr/include/KF5/pimcommon/renamefiledialog.h
/usr/include/KF5/pimcommon/richtexteditwithautocorrection.h
/usr/include/KF5/pimcommon/shareserviceurlmanager.h
/usr/include/KF5/pimcommon/simplestringlisteditor.h
/usr/include/KF5/pimcommon/spellchecklineedit.h
/usr/include/KF5/pimcommon/templatelistwidget.h
/usr/include/KF5/pimcommon/templatemanager.h
/usr/include/KF5/pimcommon/translatorwidget.h
/usr/include/KF5/pimcommon_version.h
/usr/include/KF5/pimcommonakonadi/addresseelineedit.h
/usr/include/KF5/pimcommonakonadi/annotationdialog.h
/usr/include/KF5/pimcommonakonadi/checkedcollectionwidget.h
/usr/include/KF5/pimcommonakonadi/collectionaclpage.h
/usr/include/KF5/pimcommonakonadi/collectionannotationsattribute.h
/usr/include/KF5/pimcommonakonadi/collectiontypeutil.h
/usr/include/KF5/pimcommonakonadi/completionconfiguredialog.h
/usr/include/KF5/pimcommonakonadi/completionordereditor.h
/usr/include/KF5/pimcommonakonadi/contenttypewidget.h
/usr/include/KF5/pimcommonakonadi/createresource.h
/usr/include/KF5/pimcommonakonadi/genericplugininterface.h
/usr/include/KF5/pimcommonakonadi/imapaclattribute.h
/usr/include/KF5/pimcommonakonadi/imapresourcecapabilitiesmanager.h
/usr/include/KF5/pimcommonakonadi/incidencesforwidget.h
/usr/include/KF5/pimcommonakonadi/ldapsearchdialog.h
/usr/include/KF5/pimcommonakonadi/mailutil.h
/usr/include/KF5/pimcommonakonadi/manageserversidesubscriptionjob.h
/usr/include/KF5/pimcommonakonadi/pimcommonakonadi_export.h
/usr/include/KF5/pimcommonakonadi/plugininterface.h
/usr/include/KF5/pimcommonakonadi/progressmanagerakonadi.h
/usr/include/KF5/pimcommonakonadi/recentaddresses.h
/usr/include/KF5/pimcommonakonadi/selectmulticollectiondialog.h
/usr/include/KF5/pimcommonakonadi_version.h
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
/usr/lib64/libKF5PimCommon.so.5
/usr/lib64/libKF5PimCommon.so.5.16.0
/usr/lib64/libKF5PimCommonAkonadi.so.5
/usr/lib64/libKF5PimCommonAkonadi.so.5.16.0
/usr/lib64/qt5/plugins/designer/pimcommoniakonadiwidgets.so
/usr/lib64/qt5/plugins/designer/pimcommonwidgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pimcommon/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/pimcommon/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/pimcommon/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/pimcommon/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/pimcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libpimcommon.lang
%defattr(-,root,root,-)

