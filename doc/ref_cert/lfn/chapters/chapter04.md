[<< Back](../)

# 4. NFVI Testing Cookbook
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Relevant Community Projects and Initiatives](#4.2)
   * [4.2.1 Functest](#4.2.1)
   * [4.2.2 Yardstick](#4.2.2)
   * [4.2.3 Bottlenecks](#4.2.3)
   * [4.2.4 Test Tools](#4.2.4)
   * [4.2.5 Scenario Descriptor File (SDF)](#4.2.5)
* [4.3 NFVI Testing Cookbook](#4.3)
  * [4.3.1 NFVI API testing configuration](#4.3.1)
  * [4.3.2 Run NFVI Testing](#4.3.2)

<a name="4.1"></a>
## 4.1 Introduction

Define the purpose of the chapter which is to:
-	Identify Framework Needs, Goals, and Dependencies
- Define Opensource Integration (OPNFV, OVP, Functest, CVC, others)
- Provide Automation Toolchain (list, topology, flow)


<a name="4.2"></a>
## 4.2 Relevant Community Projects and Initiatives

<a name="4.2.1"></a>
### 4.2.1 Functest

[Functest](https://functest.readthedocs.io/en/stable-iruya/) was initially
created to verify OPNFV Installers and Scenarios and then to publish fair,
trustable and public results regarding the status of the different opensource
technologies, especially for Neutron backends (e.g. Neutron agents,
OpenDaylight, OVN, etc.). It has been continuously updated to offer the best
testing coverage for any kind of OpenStack and Kubernetes deployments
including production environments. It also ensures that the platforms meet
Network Functions Virtualization requirements by running and testing VNFs
amongst all tests available.

Functest is driven by a true verification of the platform under test as opposed
to the interoperability programs such as
[RefStack](https://refstack.openstack.org/) or
[OPNFV Verification Program](https://www.opnfv.org/verification) which select
a small subset of Functional tests passing in many different
opensource software combinations:
- tests are skipped if an optional support is missing (e.g.
  [Barbican](https://docs.openstack.org/barbican/latest/) or networking
  features such as
  [BGPVPN interconnection](https://docs.openstack.org/networking-bgpvpn/latest/)
  or
  [Service Function Chaining](https://docs.openstack.org/networking-sfc/latest/))
- tests are parameterized (e.g. shared vs non-shared live migration)
- blacklist mechanisms are available if needed

It should be noted that
[the RefStack lists](https://refstack.openstack.org/#/guidelines) are included
as they are in Functest in the next 3 dedicated testcases:
- refstack_compute (OpenStack Powered Compute)
- refstack_object (OpenStack Powered Object Storage)
- refstack_platform (OpenStack Powered Platform)

Functest also integrates
[Kubernetes End-to-end tests](https://kubernetes.io/blog/2019/03/22/kubernetes-end-to-end-testing-for-everyone/) and allows verifying Kubernetes Conformance (see
[k8s-conformance](https://build.opnfv.org/ci/job/functest-kubernetes-opnfv-functest-kubernetes-smoke-iruya-k8s_conformance-run/206/console)).

Dovetail (OVP) mostly leverages on Functest but only runs a small part of
Functest (~15% of all functional tests, no benchmarking tests, no VNF
deployment and testing). It's worth mentioning that Functest is patched to
[disable API verification](https://github.com/opnfv/dovetail/tree/master/etc/patches/functest/disable-api-validation) which has differed from OpenStack rules for
years.

Then Functest conforms with the upstream rules (versions, code quality, etc.)
and especially their
[gates](https://docs.openstack.org/infra/system-config/devstack-gate.html)
(a.k.a. the automatic verification prior to any code review)
to preserve the quality between code and deployment.
In that case, Functest can be considered as a smooth and lightweight
integration of tests developed upstream (and the Functest team directly
contributes in these projects:
[Rally](https://github.com/openstack/rally-openstack),
[Tempest](https://github.com/openstack/tempest), etc.).
It's worth mentioning that, as opposed to the OpenStack Gates leveraging on
[DevStack](https://docs.openstack.org/devstack/latest/), it can check the same
already deployed SUT over and over even from a
[Raspberry PI](https://www.raspberrypi.org/). Here the testcases can be
executed in parallel vs the same deployment instead of being executed vs
different pools of virtual machines.

Here are the functional tests (>2000) running in OpenStack gates integrated in
Functest Smoke (see
[Functest daily jobs](https://build.opnfv.org/ci/job/functest-hunter-daily/392/)
for more details):

| Testcases                  | Gates              |
| :------------------------- | :----------------- |
| neutron-tempest-plugin-api | Neutron            |
| tempest_cinder             | Cinder             |
| tempest_keystone           | Keystone           |
| rally_sanity               | General            |
| refstack_defcore           | General            |
| tempest_full               | General            |
| tempest_slow               | General            |
| tempest_scenario           | General            |
| neutron_trunk              | Neutron            |
| patrole                    | Patrole            |
| barbican                   | Barbican           |
| networking-bgpvpn          | Networking BGP VPN |
| networking-sfc             | Networking SFC     |

To complete functional testing, Functest also integrates a few
[performance tools](https://docs.openstack.org/developer/performance-docs/methodologies/tools.html)
(2-3 hours) as proposed by OpenStack:

| Testcases  | Benchmarking                |
| :--------- | :-------------------------- |
| rally_full | Control Plane (API) testing |
| rally_jobs | Control Plane (API) testing |
| vmtp       | Data Plane testing          |
| shaker     | Data Plane testing          |

And VNFs automatically deployed and tested :

| Testcases    | Benchmarking                        |
| :----------- | :---------------------------------- |
| cloudify     | Cloudify deployment                 |
| cloudify_ims | Clearwater IMS deployed via Coudify |
| heat_ims     | Clearwater IMS deployed via Heat    |
| vyos_vrouter | VyOS deployed via Cloudify          |
| juju_epc     | OAI deployed via Juju               |

Functest should be considered as a whole as it meets multiple objectives about
the reference implementation:
- verify all APIs (services, advances, features, etc.) exposed by the reference
  implementation
- compare the reference implementation and local deployments from a functional
  standpoint and from OpenStack control plane and dataplane capabilities

It's worth mentioning that Functest already takes into account the first CNTT
[profiles](https://git.opnfv.org/functest/tree/functest/ci/config_patch.yaml#n2).
CNTT should simply add the next Functest inputs according the reference
implementation:
- [Functest inputs](https://github.com/opnfv/functest/blob/stable/iruya/functest/utils/env.py#L17)
- [tempest specific configuration](https://github.com/opnfv/functest/blob/stable/iruya/functest/opnfv_tests/openstack/tempest/custom_tests/tempest_conf.yaml)

Additional links:
- [Homepage](https://functest.readthedocs.io/en/stable-iruya/)
- [Run Alpine Functest containers (Iruya)](https://wiki.opnfv.org/pages/viewpage.action?pageId=35291769)
- [Deploy your own Functest CI/CD toolchains](https://wiki.opnfv.org/pages/viewpage.action?pageId=32015004)
- [Functest gates](https://build.opnfv.org/ci/view/functest/)

<a name="4.2.2"></a>
### 4.2.2 Yardstick

<a name="4.2.3"></a>
### 4.2.3 Bottlenecks

<a name="4.2.4"></a>
### 4.2.4 Test Tools
1. Shaker:  https://pyshaker.readthedocs.io/en/latest/ (The distributed data-plane testing tool built for OpenStack)
2. Sonubuoy: https://sonobuoy.io/ It is a diagnostic tool that makes it easier to understand the state of a Kubernetes cluster by running a set of plugins (including Kubernetes conformance tests) in an accessible and non-destructive manner.

<a name="4.2.5"></a>
### 4.2.5 Scenario Descriptor File (SDF)
As defined by OPNFV, Scenarnio Descriptor File's (SDF) will be utilized to relay information from the Scenario Designer (or Test Manager), to Release Managers, CI Pipeline Owners, and Installer Agents, to define test scenario content, and specifications.

SDF's will contain, but not limited to, the following Metadata, Components, Deployment Options, Deployment Tools, and Hardware prerequistes:

- **Metadata**
  - Name
  - History
  - Purpose
  - Owner
- **Components**
  - e.g. SDN controllers
  - Versions
  - Optional features, e.g. NFV features
- **Deployment Options**
  - Hardware types
  - Virtual deploy
  - HA, NUMA
- **Deployment Tools**
  - Supporting installers.
  - Valid options per installer.

<a name="4.3"></a>
## 4.3 NFVI Testing Cookbook

> using existing testing framework, proposal of an E2E integrated one to be used fir NFVI testing.

<p align="center"><img src="../figures/rc1_cookbook_nfvi.png" alt="nfvi_cookbook" title="NFVI Cookbook" width="60%"/></p>
<p align="center"><b>Figure 1-2:</b> NFVI Testing Integrated Framework.</p>

[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) leverages on the
common test case execution proposed by Xtesting. Thanks to a simple test case
list, this tool deploys anywhere plug-and-play
[CI/CD toolchains in a few commands](https://wiki.opnfv.org/pages/viewpage.action?pageId=32015004).
In addition of this teaching capability needed by the Network Automation
journey, it supports multiple components such as Jenkins and Gitlab CI (test
schedulers) and
[multiple deployment models](https://lists.opnfv.org/g/opnfv-tsc/message/5702)
such as all-in-one or centralized services.

[Xtesting](https://xtesting.readthedocs.io/en/latest/) and
[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) combined meet the
CNTT requirements about verification, compliance and certification:
- smoothly assemble multiple heterogeneous test cases
- generate the Jenkins jobs in
  [OPNFV Releng](https://git.opnfv.org/releng/tree/jjb/airship/cntt.yaml) to
  verify CNTT RI
- deploy local CI/CD toolchains everywhere to check compliance with CNTT
- [dump all test case results and logs](http://artifacts.opnfv.org/functest/9ID39XK47PMZ.zip)
  for third-party certification review

[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) only requires
GNU/Linux as Operating System and asks for a few dependencies as described in
[Deploy your own Xtesting CI/CD toolchains](https://wiki.opnfv.org/pages/viewpage.action?pageId=32015004):
- python-virtualenv
- docker.io
- git

Please note the next two points depending on the GNU/Linux distributions and
the network settings:
- SELinux: you may have to add -\-system-site-packages when creating the
  virtualenv ("Aborting, target uses selinux but python bindings
  (libselinux-python) aren't installed!")
- Proxy: you may set your proxy in env for Ansible and in systemd for Docker
  https://docs.docker.com/config/daemon/systemd/#httphttps-proxy

At the time of writing, the CI description file is hosted in Functest and only
runs the containers listed in RM/RA-1 Requirements. It will be completed by the
next CNTT mandatory test cases and then a new CI description file will be
proposed in CIRV tree.

To deploy your own CI toolchain running CNTT Compliance:
```bash
virtualenv functest
. functest/bin/activate
pip install ansible
ansible-galaxy install collivier.xtesting
git clone https://gerrit.opnfv.org/gerrit/functest functest-src
(cd functest-src && git checkout -b stable/hunter origin/stable/hunter)
ansible-playbook functest-src/ansible/site.cntt.yml
```

<a name="4.3.1"></a>
### 4.3.1 NFVI API testing configuration

Here is the default Functest tree as proposed in
[Run Alpine Functest containers (Hunter)](https://wiki.opnfv.org/pages/viewpage.action?pageId=29098314):
- /home/opnfv/functest/openstack.creds
- /home/opnfv/functest/images

Download the images and fill /home/opnfv/functest/openstack.creds as proposed
in
[Run Alpine Functest containers (Hunter)](https://wiki.opnfv.org/pages/viewpage.action?pageId=29098314)

You may have to modify a few Functest env vars according to the SUT (see env in
[Run Alpine Functest containers (Hunter)](https://wiki.opnfv.org/pages/viewpage.action?pageId=29098314)).
Be free to modify functest-src/ansible/host_vars/127.0.0.1 at your convenience
and then to reconfigure the toolchain:
```bash
ansible-playbook functest-src/ansible/site.cntt.yml
```

<a name="4.3.2"></a>
### 4.3.2 Run CNTT NFVI Testing

Open http://127.0.0.1:8080/job/functest-hunter-daily/ in a web browser, login
as admin/admin and click on "Build with Parameters" (keep the default build_tag
value).

If the System under test (SUT) is CNTT compliant, a link to the full archive
containing all test results and artifacts will be printed in
functest-hunter-zip's console. Be free to download it and then to send it to
any reviewer committee.

To clean your working dir:
```bash
deactivate
rm -rf functest-src functest
```