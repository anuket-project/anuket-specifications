[<< Back](../../ref_model)
# 8 Annex
<!--<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>-->
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction.](#8.1)
* [8.2 Generic Test Cases.](#8.2)
* [8.3 Architecture specific test cases (if needed).](#8.3)
  * [8.3.1 OpenStack (OS).](#8.3.1)
  * [8.3.2 Kubernetes (K8s).](#8.3.2)

<a name="8.1"></a>
## 8.1 Introduction

This Chapter 8 Annex contains test cases to be executed during NFVI validations to ensure a Reference Implementation of CNTT Reference Architecture is in compliance.  The Linux Foundation Networking (LFN) OPNFV Verified Program (OVP), in partnership with the Compliance Verification Committee (CVC), will provide tracking and governance for RM/RA/RI verifications.

<a name="8.2"></a>
## 8.2 Generic Test Cases

The following test projects, and their respective test cases, must be executed with each reference implementation. More specific test cases are listed below, which may be a subset of test cases run within these test suites listed.

<a name="8.3"></a>
## 8.3 Architecture Specific Test Cases (if needed)

<a name="8.3.1"></a>
### 8.3.1 OpenStack (OS)

**FuncTest**

FuncTest test suites must be run as part of NFVi validation against all OpenStack based reference implementations. At a minimum, FuncTest executions will include execution of the functest-smoke and functional-benchmarking test suites.

Additional Resources for FuncTest:
- [Project Description](https://wiki.opnfv.org/display/functest/Opnfv+Functional+Testing#OpnfvFunctionalTesting-Testcases)
- [User Guide](https://opnfv-functest.readthedocs.io/en/stable-hunter/testing/user/userguide/index.html)
- [Test Suite Overview](https://opnfv-functest.readthedocs.io/en/stable-hunter/testing/user/userguide/test_overview.html)

Example, or Reference, Functest Status Reporting Artifacts:
- [Rally Verification](http://artifacts.opnfv.org/functest/functest-opnfv-functest-smoke-iruya-tempest_full-run-259/results/tempest_full/tempest-report.html)
- [Rally Tasks](http://artifacts.opnfv.org/functest/functest-opnfv-functest-benchmarking-iruya-rally_full-run-169/results/rally_full/rally_full.html)

**Baremetal**

**SUMMARY:** Control and compute node hardware, bios, firmware, network interfaces, and base operating system configuration must be validated.
- Interface - Validate nic status for all member in bond1 group
- Interface - MTU speed for bond1 interface
- Grub - SR-IOV is enabled
- Numa - Validate numa configuration on each node
- Numa - Validate total memory available is distributed equally across numa boundaries
- VFs - Validate VF creation on each PCI SYS Interface.
- Modules - Validate necessary kernel modules are loaded
- OS: IPTables are enabled.
- OS: System time on all hosts is synchronized to a common set of NTP servers
- OS: Dedicate mount point for following file system
  - /var/log
  - /var/lib/nova
- OS: Validate Huge Pages are configured and enabled based on target infrastructure. (not available for all flavours)
  - Validate Hugepage size configuration
  - Validate Hugepage total number configuration
- OS: Validate proxy/iptables implementation
- Validate proxy configuration after server reboot
- Validate routing table after server reboot
- BIOS: Validate Boot order
- Validate Kernel version against Reference Implementation
- Validate BIOS version against Reference Implementation
- Validate Firmware version against Reference Implementation
- CPU Performance mode validation
- Compare CPU verification server specs

**VNF Interoperability**

**SUMMARY:** Validation of end to end openstack resources, including: Tenant, Network (L2/L3), CPU Pinning, Security Policies, Affinity/Anti-Affinity, Roles, Flavours, etc.

- Validate security profiles against a reference VNF
  - Validate blocking ICMP traffic blocks two reference VNFs from pinging each other
  - Validate allowing ICMP traffic allows two reference VNFs from pinging each other
- Validate image upload to glance
- Validate host aggregate creation
- Validate assignment of nodes to host aggregate
- Provider Network - SRIOV - VLAN (where applicable, allowing a device, such as a network adapter, to separate access to its resources among various PCIe hardware functions)
- OAM Network
- Create routers across 2 tenant network (optional - i.e. create virtual router on two different tenants and validate the network connectivity between the two)
- Validate anti-affinity and affinity rules
- Validate user ability to force VM landing on given hypervisor host
- Create VMs using flavour defined above and Attached ceph storage
- Validate VM is able to extract meta data
- Validate VM connectivity between SR-IOV Network
- Validate SRIOV Port mapping to OS/VF (where applicable)
- Validate VM connectivity between L3/Tenant network
- Validate VM connectivity between L3/Network traffic passing through router
- Validate user-data script gets execute as part of POST VM creation in your stack
- Delete all Heat stack created as part of this testing
- Validate VM host-dev mapping to physical host
- Validate hairpinning Solution -- Communication between 2 VMs residing on same compute should not go over wire

**Compute Component**

**SUMMARY:** Validate/Document VMs status and connectivity result after performing each of listed steps.
- Restart libvirt pod
- Restart nova-compute pod
- Restart openvswitch-db pod
- Restart openvswitch-vswitchd pod
- Restart neutron-ovs-agent pod
- Restart neutron-sriov-agent pod (where applicable)

**Control Plane Components**

**SUMMARY:** Validate RabbitMQ, Ceph, Mariadb and Openstack components, including: Nova, Glance, Heat, and Keystone. Resiliancy is validated by shutting down service under test in one or more pods, making API calls against that service, and validating service is still working as expected.
- Validate RabbitMQ resiliency
- Validate nova-api resiliency
- Validate nova-api-metadata
- Validate nova-conductor
- Validate nova-scheduler
- Validate nova-placement-api
- Validate nova-console-auth
- Validate nova-novnc-proxy
- Validate nova-rabbitmq
- Validate glance-api
- Validate glance-registry
- Validate glance-rabbitmq
- Validate heat-api
- Validate heat-cfn
- Validate heat-engine
- Validate heat-rabbitmq
- Validate keystone-api
- Validate keystone-rabbitmq
- Validate keystone-rabbitmq
- Validate mariadb cluster is in sync
- Studown mariadb and upon restart ensure its sync up with masterdb
- Validate ceph (if including in implementation)
- Restart ceph-osd (if including in implementation)
- Validate VNF is working as expected following ceph service restart

**Security**

**SUMMARY:** See [chapter 7](./chapter07.md) for security requirements

<a name="8.3.2"></a>
### 8.3.2 Kubernetes (K8s)

TBD
