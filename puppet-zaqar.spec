%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-zaqar
Version:        XXX
Release:        XXX
Summary:        Puppet module for OpenStack Zaqar
License:        ASL 2.0

URL:            https://launchpad.net/puppet-zaqar

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet-openstacklib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Zaqar

%prep
%setup -q -n openstack-zaqar-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/zaqar/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/zaqar/



%files
%{_datadir}/openstack-puppet/modules/zaqar/


%changelog


# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/puppet-zaqar/commit/?id=afbc7455bb579f58781c38652b8a5d552853a6de
