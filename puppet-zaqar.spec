%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x4c29ff0e437f3351fd82bdf47c5a3bc787dc7035
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-zaqar
Version:        19.4.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Zaqar
License:        ASL 2.0

URL:            https://launchpad.net/puppet-zaqar

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet-openstacklib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Zaqar

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Thu Oct 07 2021 RDO <dev@lists.rdoproject.org> 19.4.0-1
- Update to 19.4.0



