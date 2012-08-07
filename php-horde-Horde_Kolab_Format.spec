%define		status		stable
%define		pearname	Horde_Kolab_Format
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - A package for reading/writing Kolab data formats
Name:		php-horde-Horde_Kolab_Format
Version:	1.1.2
Release:	2
License:	LGPL 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	6e70f274702ecc9a8ddecac70e729a9f
URL:		http://pear.horde.org/package/Horde_Kolab_Format/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(dom)
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-pear
Suggests:	php-horde-Horde_Date
Suggests:	php-horde-Horde_Support
Suggests:	php-horde-Horde_Test
Suggests:	php-mbstring
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows to convert Kolab data objects from XML to hashes.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/Horde_Kolab_Format/examples .
mv docs/Horde_Kolab_Format/TODO .
mv docs/Horde_Kolab_Format/usage.txt .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc TODO usage.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Kolab/Format
%{php_pear_dir}/Horde/Kolab/Format.php
%{_examplesdir}/%{name}-%{version}
