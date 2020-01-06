[<< Back](../)

# 9. NFVI Tests Traceability to TC Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [9.1 Introduction](#9.1)
* [9.2 RM/RA-1 Requirements](#9.2)
* [9.3 TC Mapping to Requirements](#9.3)
* [9.4 CNTT Compliance Cookbook](#9.4)
  * [9.4.1 NFVI API testing configuration](#9.4.1)
  * [9.4.2 Run CNTT Compliance](#9.4.1)

<a name="9.1"></a>
## 9.1 Introduction

Define, and describe the purpose of this chapter to be:

- Define RM/RA-1 Openstack requirements
- Map Framework to Requirements

<a name="9.2"></a>
## 9.2 RM/RA-1 Requirements

According to [RC1 Chapter04](/doc/ref_cert/lfn/chapters/chapter04.html) the next
test cases must pass as they are for CNTT NFVI Conformance/Certification:

| container                               | test case                  | criteria |
|-----------------------------------------|----------------------------|:--------:|
| opnfv/functest-smoke-cntt:hunter        | neutron-tempest-plugin-api | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_cinder             | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_keystone           | PASS     |
| opnfv/functest-smoke-cntt:hunter        | rally_sanity               | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_full               | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_scenario           | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_slow               | PASS     |
| opnfv/functest-benchmarking-cntt:hunter | rally_full                 | PASS     |
| opnfv/functest-benchmarking-cntt:hunter | rally_jobs                 | PASS     |
| opnfv/functest-benchmarking-cntt:hunter | vmtp                       | PASS     |
| opnfv/functest-benchmarking-cntt:hunter | shaker                     | PASS     |
| opnfv/functest-vnf:hunter               | cloudify                   | PASS     |
| opnfv/functest-vnf:hunter               | cloudify_ims               | PASS     |
| opnfv/functest-vnf:hunter               | heat_ims                   | PASS     |
| opnfv/functest-vnf:hunter               | vyos_vrouter               | PASS     |
| opnfv/functest-vnf:hunter               | juju_epc                   | PASS     |

<a name="9.3"></a>
## 9.3 TC Mapping to Requirements

| test case                  | requirements                                                             |
|----------------------------|--------------------------------------------------------------------------|
| neutron-tempest-plugin-api | Neutron API testing                                                      |
| tempest_cinder             | Cinder API testing                                                       |
| tempest_keystone           | Keystone API testing                                                     |
| rally_sanity               | Keystone, Glance, Cinder, Swift, Neutron, Nova and Heat API testing      |
| tempest_full               | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| tempest_scenario           | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| tempest_slow               | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| rally_full                 | Keystone, Glance, Cinder, Swift, Neutron, Nova and Heat API benchmarking |
| rally_jobs                 | Neutron API benchmarking                                                 |
| vmtp                       | Dataplane benchmarking                                                   |
| shaker                     | Dataplane benchmarking                                                   |
| cloudify                   | opensource VNF onboarding and testing                                    |
| cloudify_ims               | opensource VNF onboarding and testing                                    |
| heat_ims                   | opensource VNF onboarding and testing                                    |
| vyos_vrouter               | opensource VNF onboarding and testing                                    |
| juju_epc                   | opensource VNF onboarding and testing                                    |

<a name="9.4"></a>
## 9.4 CNTT Compliance Cookbook

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

<a name="9.4.1"></a>
### 9.4.1 NFVI API testing configuration

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

<a name="9.4.2"></a>
### 9.4.2 Run CNTT Compliance

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
