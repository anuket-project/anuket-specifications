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

This Chapter 8 Annex contains standard test cases to be executed during NFVI validations to ensure a Reference Implementation of CNTT Reference Model Architecture complies with industry-driven standards.  The OPNFV Verified Program (OVP), by Linux Foundation Networking (LFN), in partnership with the Compliance Verification Committee (CVC), will provide tracking and governance for RM/RA/RI verifications.

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
- VFs - Validate VFs are availablebeing created on each PCI SYS Interface.
- Modules - Validate the following modules are loaded
  - bonding
  - 8021q
  - i40e
- OS: IPTables are enabled.
- OS: ntp is enabled and configured to sync system time
- OS: Dedicate mount point for following file system
  - /var/log
  - /var/lib/nova
- OS: Validate Huge Pages are configured and enabled based on target infrastructure. (not available for all flavours)
  - Validate Hugepage size configuration
  - Validate Hugepage total number configuration
- OS: Validate proxy/iptables implementation
- OS: Validate proxy/iptables implementation
- Validate proxy configuration after server reboot
- Validate routing table after server reboot
- BIOS: Validate Boot order
- Validate Kernel version</li>
- Validate BIOS version
- Validate Firmware version
- CPU Performance mode validation
- Compare CPU verification server specs

**VNF Interoperability - validations**
**SUMMARY:** After VNF onboarding, we are validating end to end openstack resources like Tenant, Network (L2/L3), CPU Pining, security policies, Affinity anti-affinity roles and flavours etc.

- Validate security profiles against a reference VNF
  - Validate blocking ICMP traffic blocks two reference VNFs from pinging each other
  - Validate allowing ICMP traffic allows two reference VNFs from pinging each other
- Validate image upload to glance
- Validate host aggregate creation
- Validate assignment of nodes to host aggregate
- Provider Network - SRIOV - VLAN (where applicable, allowing a device, such as a network adapter, to separate access to its resources among various PCIe hardware functions)
- OAM Network
- Create routers across 2 tenant network (optional - i.e. create virtual router on two different tenants and validate the network connectivity between the two)</li>
Validate anti-affinity and affinity rules</li>
Validate user ability to force VM landing on given hypervisor host</li>
Create VMs using flavour defined above and Attached ceph storage
Validate VM is able to extract meta data</li>
Validate VM connectivity between SR-IOV Network</li>
Validate SRIOV Port mapping to OS/VF (where applicable)</li>
Validate VM connectivity between L3/Tenant network</li>
Validate VM connectivity between L3/Network traffic passing through router.</li>
Validate user-data script gets execute as part of POST VM creation in your stack</li>
<li>Assuming all above task is perform using heat template</li>
<li>Delete all Heat stack created as part of this testing</li>
<li>Validate VM&rsquo;s host-dev mapping to physical host</li>
</ul>
</li>
<li>Validate hairpinning Solution -- Communication between 2 VMs residing on same compute should not go over wire</li>
<li>Validate hairpinning Solution -- Communication between 2 VMs residing on same compute should not go over wire&nbsp;</li>
</ul>
</li>
</ul>
<ul>
<li><span style="text-decoration: underline;"><strong>Compute Component - validations</strong></span>
<ul>
<li>**SUMMARY:** Validate/Document VMs status and connectivity result after performing each of listed steps. Best candidate for this testing would be identify compute node that holds VMs which has l2 and l3 connectivity. Lag time between Shutdown and Startup should be no more than 10 minute
- Restart libvirt pod</li>
- Restart nova-compute pod</li>
- Restart openvswitch-db pod</li>
- Restart openvswitch-vswitchd pod</li>
- Restart neutron-ovs-agent pod</li>
- Restart neutron-sriov-agent pod (where applicable)
**Control Plane Components**
**SUMMARY:** We are validating RabbitMQ, Ceph, Mariadb and Openstack components like nova, glance, heat, keystone API and resillency test.
<li>Validate RabbitMQ resiliency by shutting down 1 or more pods. Make nova/openstack API call to see system result <br />(expected results is BAU)"</li>
<li>Validate nova-api resilency by shutting down 1 or more pods. Document API call results. (expected results is BAU)</li>
<li>Run similar resiliency test for each of listed services and expected result is BAU &ndash; No impact to VNF
<ul>
<li>nova-api-metadaa</li>
<li>nova-conductor</li>
<li>nova-scheduler</li>
<li>nova-placement-api</li>
<li>nova-console-auth</li>
<li>nova-novnc-proxy</li>
<li>nova-rabbitmq</li>
<li>glance-api</li>
<li>glance-registry</li>
<li>glance-rabbitmq</li>
<li>heat-api</li>
<li>heat-cfn</li>
<li>heat-engine</li>
<li>heat-rabbitmq</li>
<li>keystone-api</li>
<li>keystone-rabbitmq</li>
<li>keystone-rabbitmq</li>
</ul>
</li>
<li>Validate maridb cluster is insync
<ul>
<li>Studown mariadb and upon restart ensure its sync up with masterdb.</li>
<li>Maria DB is single point of failure</li>
</ul>
</li>
<li>Validate ceph
<ul>
<li>Restart ceph-osd</li>
<li>Document VNF impact while ceph is unavailable and once ceph service is restoredbeing restored.</li>
</ul>
</li>
</ul>
</li>
<ul>
<li><span style="text-decoration: underline;"><strong>Security - see Ch 7 for complete list</strong></span>
<ul>
<li>Validation above is performed using both RBAC Roles and User group policies, both of Admin and User Roles.
</ul>
<li>**SUMMARY:** Validate User Role to ensure it allow user to perform all designated task and prohibits user performing any unassigned task.</li>
<li>Validate Security Policy/Rules are enforced</li>
</ul>
</li>
</ul>
</ul>

<a name="8.3.2"></a>
### 8.3.2 Kubernetes (K8s)

TBD
