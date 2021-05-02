[<< Back](../)

# 3. Cloud Infrastructure Test Cases and Traceability to CNTT Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 Selection Criteria](#3.2)
* [3.3 Traceability Matrix](#3.3)
  * [3.3.1 Architecture and OpenStack Based](#3.3.1)
  * [3.3.2 Infrastructure](#3.3.2)
  * [3.3.3 VIM](#3.3.3)
  * [3.3.4 Interfaces & APIs](#3.3.4)
  * [3.3.5 Dashboard](#3.3.5)
  * [3.3.6 OpenStack API benchmarking](#3.3.6)
  * [3.3.7 Dataplane Benchmarking](#3.3.7)
  * [3.3.8 Opensource VNF onboarding and testing](#3.3.8)
  * [3.3.9 Tenants](#3.3.9)
  * [3.3.10 LCM](#3.3.10)
  * [3.3.11 Assurance](#3.3.11)
  * [3.3.12 Security](#3.3.12)
  * [3.3.13 Resilience](#3.3.13)
  * [3.3.14 Bare-metal validations](#3.3.14)
* [3.4 Test Cases Traceability to Requirements](#3.4)
  * [3.4.1 Test Cases Traceability](#3.4.1)

<a name="3.1"></a>
## 3.1 Introduction

The scope of this chapter is to identify and list down test cases based on requirements defined in [Reference Architecture-1 (RA-1)](../../../ref_arch/openstack/README.md). This will serve as traceability between test cases and requirements.

Note that each requirement may have one or more test cases associated with it.

**must**: Test Cases that are marked as must are considered mandatory and must pass successfully.

**should**: Test Cases that are marked as should are expected to be fulfilled by NFVI but it is up to each service provider to accept an NFVI targeting reference architecture that is not reflecting on any of those requirements. The same applies to should not.

**may**: Test cases that are marked as may are considered optional. The same applies to may not.

<a name="3.2"></a>
## 3.2 Selection Criteria
> Test cases below are selected based on available test cases in open-source tools like OPNFV FuncTest, YardStick, DoveTail etc.

<a name="3.3"></a>
## 3.3 Traceability Matrix

The following is a Requirements Traceability Matrix (RTM) mapping Test Case, and/or Test Case Coverage, to RM and RA-1 requirements (config and deployment).

The RTM contains RM config (i.e. .conf) requirements listed “per profile”, followed by RA-1 requirements.  Requirements fall into 8 domains: general(gen), infrastructure(inf), VIM(vim), Interface & API(int), Tenants(tnt), LCM(lcm), Assurance(asr), Security(sec).

For detailed information on RM & RA-1 NFVI and VNF requirements, please refer to [RI-1 Chapter 3](https://github.com/cntt-n/CNTT/blob/master/doc/ref_impl/cntt-ri/chapters/chapter03.md).

<a name="3.3.1"></a>
### 3.3.1 Architecture and OpenStack Requirements

<!--
|#|Requirement|Description|Catalog|Status|MUST|Category|RI-1 Implemented (Yes/No)|RC-1 Coverage (project)|RC-1 Project To On-board|
|--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
|1|req.gen.ost.01|must use OpenStack APIs.|General|in Functest|Must|Functional||Functest||
|2|req.gen.ost.02|must support dynamic request and configuration of virtual resources through APIs.|General|in Functest|Must|Functional||Functest||
|3|req.gen.cnt.01|should consist of stateless service components. However, where state is required it must be kept external to the components.|General|||||||
|4|req.gen.cnt.02|should consist of service components implemented as microservices that are individually dynamically scalable.|General|||||||
|5|req.gen.scl.01|should support policy driven auto-scaling.|General|||||||
|6|req.gen.rsl.01|must support resilient OpenStack components that are required for the continued availability of running workloads.|General - Resiliency testing|missing|Must|NFR||||
|7|req.gen.rsl.02|should support resilient OpenStack service components that are not subject to req.gen.rsl.01.|General - Resiliency testing|missing||||||
|8|req.gen.avl.01|must provide High Availability for OpenStack components.|General - HA|missing|Must|NFR||||
|9|req.inf.com.01|must provide compute resources for VM instances.|Infrastructure|in Functest|Must|Functional||Functest||
|10|req.inf.com.02|should include industry standard hardware management systems at both HW device and platform level|Infrastructure - baremental testing|missing in Functest. Captured in Telco TCs Baremetal - validations.||||||
|11|req.inf.com.03|should support symmetrical CPU multi-processing with shared memory access as well as multi-threading.|Infrastructure|in Functest||||Functest||
|12|req.inf.com.04|must be able to support multiple CPU SKU options to support Base, Network Intensive, and Compute Intensive infrastructure profiles.|Infrastructure||Must|NFR||||
|13|req.inf.com.05|must support Hardware Platforms with NUMA capabilities.|Infrastructure - baremental testing|missing or incomplete in Functest. Captured in Telco TCs Baremetal - validations.|Must|Functional||||
|14|req.inf.com.06|must support CPU Pinning.|Infrastructure - baremental testing|missing or incomplete in Functest. Captured in Telco TCs Baremetal - validations.|Must|Functional||||
|15|req.inf.com.07|must support different hardware configurations to support Base, Network Intensive, and Compute Intensive infrastructure profiles.|Infrastructure - baremental testing|missing or incomplete in Functest. Captured in Telco TCs Baremetal - validations.|Must|Functional||||
|16|req.inf.stg.01|must provide shared Block storage for VM Instances.|Infrastructure|in Functest|Must|Functional||Functest||
|17|req.inf.stg.02|must provide shared Object storage for VM Instances.|Infrastructure|in Functest|Must|Functional||Functest||
|18|req.inf.stg.03|may provide local file system storage solution for VM Instances.|Infrastructure - baremental testing|missing||||||
|19|req.inf.stg.04|may support Software Defined Storage (SDS) that seamlessly supports shared block storage, object storage and flat files.|Infrastructure - baremental testing|missing||||||
|20|req.inf.stg.05|should be able to accommodate VNFs that store back into its image through use of hypervisor attached volumes.|Infrastructure|in Functest||||Functest||
|21|req.inf.stg.06|should make the immutable images available via location independent means.|Infrastructure|in Functest||||Functest||
|22|req.inf.stg.07|should provide high-performance and horizontally scalable VM storage.|Infrastructure - performance testing|missing||||||
|23|req.inf.stg.08|should allow use of externally provided large archival storage for its Backup / Restore / Archival needs.|Infrastructure - baremental testing|missing in Functest. Captured in Telco TCs Baremetal - validations.||||||
|24|req.inf.stg.09|should make available all non-host OS / Hypervisor / Host systems storage as network-based Block, File or Object Storage for tenant/management consumption.|Infrastructure|in Functest||||Functest||
|25|req.inf.ntw.01|must provide virtual network interfaces to VM instances.|Infrastructure|in Functest|Must|Functional||Functest||
|26|req.inf.ntw.02|must include capabilities for integrating SDN controllers to support provisioning of network services, from the OpenStack Neutron service, such as networking of VTEPs to the Border Edge based VRFs.|Infrastructure|in Functest|Must|Functional||Functest||
|27|req.inf.ntw.03|must support low latency and high throughput traffic needs.|performance testing|missing|Must|NFR|||NFVBenchPROX|
|28|req.inf.ntw.04|should support service function chaining.|Infrastructure|missing||||||
|29|req.inf.ntw.05|must allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve).|Infrastructure|missing|Must|Functional||||
|30|req.inf.ntw.06|should support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently.|Infrastructure|missing||||||
|31|req.inf.ntw.07|must support network resiliency.|Infrastructure - resiliency testing|missing|Must|NFR||||
|32|req.inf.ntw.08|The NFVI Network Fabric should embrace the concepts of open networking and disaggregation using commodity networking hardware and disaggregated Network Operating Systems.|Infrastructure|missing||||||
|33|req.inf.ntw.09|The NFVI Network Fabric should embrace open-based standards and technologies.|Infrastructure|missing||||||
|34|req.inf.ntw.10|The NFVI Network Fabric must be capable of supporting highly available (Five 9’s or better) VNF workloads.|Infrastructure - performance testing|missing|Must|NFR||||
|35|req.inf.ntw.11|The NFVI Network Fabric should be architected to provide a standardised, scalable, and repeatable deployment model across all applicable NFVI sites.|Infrastructure|missing||||||
|36|req.inf.ntw.12|The SDN solution should be configurable via orchestration or VIM systems in an automated manner using openly published API definitions.|Infrastructure - SDN|missing or incomplete. All captured in ODL?||||||
|37|req.inf.ntw.13|The SDN solution should be able to support federated networks.|Infrastructure - SDN|missing or incomplete. All captured in ODL?||||||
|38|req.inf.ntw.14|The SDN solution should be able to be centrally administrated and configured.|Infrastructure - SDN|missing or incomplete. All captured in ODL?||||||
|39|req.inf.ntw.15|must support multiple networking options for NFVI to support Base, Network Intensive, and Compute Intensive infrastructure profiles.|Infrastructure|missing or incomplete|Must|Functional||||
|40|req.inf.ntw.16|must support dual stack IPv4 and IPv6 for tenant networks and workloads.|Infrastructure|missing or incomplete|Must|Functional||||
|41|req.inf.ntw.17|should use dual stack IPv4 and IPv6 for NFVI internal networks.|Infrastructure|missing or incomplete||||||
|42|req.inf.acc.01|should support Application Specific Acceleration (exposed to VNFs).|Infrastructure|missing in Functest. Captured in Telco TCs Openstack - VNF Interoperability - validations||||||
|43|req.inf.acc.02|should support NFVI Acceleration (such as SmartNICs).|Infrastructure|missing||||||
|44|req.inf.acc.03|should not rely on SR-IOV PCI-Pass through to provide acceleration to VNFs.|Infrastructure|missing||||||
|45|req.vim.01|must allow infrastructure resource sharing.|VIM|in Functest|Must|Functional||Functest||
|46|req.vim.02|should support deployment of OpenStack components in containers.|VIM|in Functest||||Functest||
|47|req.vim.03|must allow VIM to discover and manage NFVI resources.|VIM|in Functest|Must|Functional||Functest||
|48|req.vim.04|must support Enhanced Platform Awareness (EPA).|VIM|in Functest|Must|Functional||Functest||
|49|req.vim.05|must include image repository management.|VIM|in Functest|Must|Functional||Functest||
|50|req.vim.06|must allow orchestration solutions to be integrated with VIM.|VIM|in Functest|Must|Functional||Functest||
|51|req.vim.07|must support a multi-tenanted environment.|VIM|in Functest|Must|Functional||Functest||
|52|req.vim.08|must support resource tagging.|VIM|in Functest|Must|Functional||Functest||
|53|req.vim.09|must support horizontal scaling.|VIM - performance testing|missing|Must|NFR|||NFVBench|
|54|req.int.api.01|must provide Control API endpoints to cloud platform core services.|Interface & API|in Functest|Must|Functional||Functest||
|55|req.int.api.02|must provide GUI access to tenant facing cloud platform core services.|Interface & API|in Functest|Must|Functional||Functest||
|56|req.int.api.03|must provide APIs needed to discover and manage NFVI resources.|Interface & API|in Functest|Must|Functional||Functest||
|57|req.int.acc.01|should provide an open and standard acceleration interface to VNFs.|Interface & API|in Functest||||Functest||
|58|req.int.acc.02|should not rely on SR-IOV PCI-Pass through for acceleration interface exposed to VNFs.|Interface & API|missing||||||
|59|req.tnt.gen.01|must support multi-tenancy.|Tenants|in Functest|Must|Functional||Functest||
|60|req.tnt.gen.02|must support self-service dashboard (GUI) and APIs for users to deploy, configure and manage their workloads.|Tenants|in Functest|Must|Functional||Functest||
|61|req.lcm.gen.01|must support zero downtime expansion/change of physical capacity (compute hosts, storage increase/replacement).|LCM - performance testing|missing|Must|NFR||||
|62|req.lcm.adp.01|should allow for “cookie cutter” automated deployment, configuration, provisioning and management of multiple NFVI sites.|LCM|use airship||||||
|63|req.lcm.adp.02|must support hitless upgrades of software provided by the cloud provider so that the availability of running workloads is not impacted.|LCM - performance testing|missing or incomplete. Use airship?|Must|NFR||||
|64|req.lcm.adp.03|should support hitless upgrade of all software provided by the cloud provider that are not covered by req.lcm.adp.02. Whenever hitless upgrades are not feasible, attempt should be made to minimize the duration and nature of impact.|LCM|use airship||||||
|65|req.lcm.adp.04|should support declarative specifications of hardware and software assets for automated deployment, configuration, maintenance and management.|LCM|use airship||||||
|66|req.lcm.adp.05|should support automated process for Deployment and life-cycle management of VIM Instances.|LCM|use airship||||||
|67|req.lcm.cid.02|should support integrating with CI/CD Toolchain for NFVI and VIM components Automation.|LCM|use Xtesting||||||
|68|req.asr.mon.01|must include integration with various infrastructure components to support collection of telemetry for assurance monitoring and network intelligence.|Assurance|in Functest|Must|Functional||Functest||
|69|req.asr.mon.02|should support Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from VNF workloads.|Assurance - operation|missing||||||
|70|req.asr.mon.03|must allow for the collection and dissemination of performance and fault information.|Assurance - operation|missing|Must|NFR||||
|71|req.asr.mon.04|The NFVI Network Fabric and Network Operating System must provide network operational visibility through alarming and streaming telemetry services for operational management, engineering planning, troubleshooting, and network performance optimisation.|Assurance - operation|missing|Must|NFR||||
|72|req.sec.gen.01|must provide tenant isolation.|security|in Functest|Must|Functional||Functest||
|73|req.sec.gen.02|must support policy based RBAC.|security|in Functest|Must|Functional||Functest||
|74|req.sec.gen.03|must support a centralised authentication and authorisation mechanism.|security|in Functest|Must|Functional||Functest||
|75|req.sec.zon.01|must support identity management (specific roles and permissions assigned to a domain or tenant).|security|in Functest|Must|Functional||Functest||
|76|req.sec.zon.02|must support password encryption.|security|in Functest|Must|Functional||Functest||
|77|req.sec.zon.03|must support data, at-rest and in-flight, encryption.|security|missing|Must|Functional||||
|78|req.sec.zon.04|must support integration with Corporate Identity Management systems.|security|missing|Must|NFR||||
|79|req.sec.cmp.02|must comply with all applicable standards and regulations.|security|missing in Functest. Captured in Telco TCs Security|Must|NFR||||
|80|req.sec.cmp.03|must comply with all applicable regional standards and regulations.|security|missing|Must|NFR||||
|81|req.sec.ntw.01|must have the underlay network include strong access controls that comply with ISO 27001 and adhere to the V1.1 NIST Cybersecurity Framework.|security|missing|Must|NFR||||
|82|req.sec.ntw.02|must have all security logs stored in accordance with ISO27001.|security|missing|Must|NFR||||
|83|req.sec.ntw.03|must have the underlay network incorporate encrypted and/or private communications channels to ensure its security.|security|missing|Must|Functional||||
|84|req.sec.ntw.04|must configure all of the underlay network components to ensure the complete separation from the overlay customer deployments.|security|missing|Must|NFR||||
-->

<a name="3.3.2"></a>
### 3.3.2 Infrastructure

<a name="3.3.3"></a>
### 3.3.3 VIM

<a name="3.3.4"></a>
### 3.3.4 Interfaces & APIs

The [OpenStack Gates](https://opendev.org/openstack/devstack-gate) verify all
changes proposed mostly by running thousands of Tempest tests completed by
Rally scenarios in a few cases. Skipping tests is allowed in all OpenStack
Gates and only failures rate the review -1 because of the multiple capabilities
and backends selected in the different Gate jobs. The classical
[Functest containers](https://wiki.opnfv.org/pages/viewpage.action?pageId=29098314)
conform to this model which also fits the heterogeneous user deployments.

From a CNTT Compliance state point, the capabilities are well described in
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
which allows tuning the test configurations and the test lists to avoid
skipping any test. It results that all tests covering optional capabilities and
all upstream skipped tests due to known bugs are not executed. All remaining
tests must be executed and must pass successfully.

New [Functest containers](https://lists.opnfv.org/g/opnfv-tsc/message/5717)
have been proposed for CNTT Compliance which simply override the default test
configurations and the default test lists. Any optional capability or services
(e.g. Barbican) can be still verified by the classical Functest containers.

The next subsections only detail the Tempest tests which must not be executed
from a Compliance state point. The remaining tests have to pass successfully.
They cover all together the API testing requirements as asked by
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)

According to Jerma, the following software versions are considered here to
verify OpenStack Train selected by CNTT:

| software                | version     |
|-------------------------|-------------|
| Functest                | jerma       |
| Horizon Tempest plugin  | 0.2.0       |
| Cinder Tempest plugin   | 0.3.0       |
| Keystone Tempest plugin | 0.3.0       |
| Heat Tempest plugin     | 1.0.0       |
| Neutron Tempest plugin  | 0.6.0       |
| Rally OpenStack         | 1.7.1.dev21 |
| Tempest                 | 22.0.0      |

#### 3.3.4.1 Identity - Keystone

Keystone API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) and
[keystone-tempest-plugin](https://opendev.org/openstack/keystone-tempest-plugin)
as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma).

According to
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
the following test names must not be executed:

| test rejection regular expressions        | reasons    |
|-------------------------------------------|------------|
| .\*api.identity.v3.test_oauth1_tokens     | oauth1     |
| .\*scenario.test_federated_authentication | federation |
| .\*identity.admin.v2                      | API v2     |
| .\*identity.v2                            | API v2     |

Keystone API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma):
- Authenticate.keystone
- KeystoneBasic.add_and_remove_user_role
- KeystoneBasic.create_add_and_list_user_roles
- KeystoneBasic.create_and_list_tenants
- KeystoneBasic.create_and_delete_role
- KeystoneBasic.create_and_delete_service
- KeystoneBasic.get_entities
- KeystoneBasic.create_update_and_delete_tenant
- KeystoneBasic.create_user
- KeystoneBasic.create_tenant
- KeystoneBasic.create_and_list_users
- KeystoneBasic.create_tenant_with_users

#### 3.3.4.2 Image - Glance

Glance API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml).

According to
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
the following test names must not be executed:

| test rejection regular expressions | reasons |
|------------------------------------|---------|
| .\*image.v1                        | API v1  |

Glance API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma):
- Authenticate.validate_glance
- GlanceImages.create_and_delete_image
- GlanceImages.create_and_list_image
- GlanceImages.list_images
- GlanceImages.create_image_and_boot_instances

#### 3.3.4.3 Block Storage - Cinder

Cinder API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) and
[cinder-tempest-plugin](https://opendev.org/openstack/cinder-tempest-plugin)
as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma).

According to
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
the following test names must not be executed:

| test rejection regular expressions                                                                   | reasons                               |
|------------------------------------------------------------------------------------------------------|---------------------------------------|
| .\*test_incremental_backup                                                                           | https://gerrit.opnfv.org/gerrit/68881 |
| .\*test_consistencygroups                                                                            | consistency_group                     |
| .\*test_group_snapshots.GroupSnapshotsV319Test.test_reset_group_snapshot_status                      | https://launchpad.net/bugs/1770179    |
| .\*test_multi_backend                                                                                | multi-backend                         |
| .\*test_volume_retype.VolumeRetypeWithMigrationTest                                                  | multi-backend                         |
| .\*test_volume_delete_cascade.VolumesDeleteCascade.test_volume_from_snapshot_cascade_delete          | https://launchpad.net/bugs/1677525    |
| .\*test_volumes_backup.VolumesBackupsTest.test_volume_backup_create_get_detailed_list_restore_delete | ceph                                  |
| .\*test_volumes_extend.VolumesExtendAttachedTest.test_extend_attached_volume                         | extend_attached_volume                |
| .\*tempest.scenario.test_volume_migrate_attached                                                     | multi-backend                         |

Cinder API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma):
- Authenticate.validate_cinder
- CinderVolumes.create_and_delete_snapshot
- CinderVolumes.create_and_delete_volume
- CinderVolumes.create_and_extend_volume
- CinderVolumes.create_from_volume_and_delete_volume
- CinderQos.create_and_list_qos
- CinderQos.create_and_set_qos
- CinderVolumeTypes.create_and_list_volume_types
- CinderVolumeTypes.create_volume_type_and_encryption_type
- Quotas.cinder_update_and_delete
- Quotas.cinder_update

#### 3.3.4.4 Object Storage - Swift

Swift API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma).

According to
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
the following test names must not be executed:

| test rejection regular expressions                                                           | reasons                            |
|----------------------------------------------------------------------------------------------|------------------------------------|
| .\*test_container_sync.ContainerSyncTest.test_container_synchronization                      | https://launchpad.net/bugs/1317133 |
| .\*test_container_sync_middleware.ContainerSyncMiddlewareTest.test_container_synchronization | container_sync                     |

Swift API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma):
- SwiftObjects.create_container_and_object_then_list_objects
- SwiftObjects.list_objects_in_containers
- SwiftObjects.create_container_and_object_then_download_object
- SwiftObjects.create_container_and_object_then_delete_all
- SwiftObjects.list_and_download_objects_in_containers

#### 3.3.4.5 Networking - Neutron

Neutron API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) and
[neutron-tempest-plugin](https://opendev.org/openstack/neutron-tempest-plugin)
as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma).

According to
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
the following test names must not be executed:

| test rejection regular expressions                                                                              | reasons                               |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------|
| .\*admin.test_agent_availability_zone                                                                           | DHCP agent and L3 agent               |
| .\*admin.test_dhcp_agent_scheduler                                                                              | dhcp_agent_scheduler                  |
| .\*admin.test_l3_agent_scheduler                                                                                | l3_agent_scheduler                    |
| .\*admin.test_logging                                                                                           | logging                               |
| .\*admin.test_logging_negative                                                                                  | logging                               |
| .\*admin.test_network_segment_range                                                                             | network-segment-range                 |
| .\*admin.test_ports.PortTestCasesAdmin.test_regenerate_mac_address                                              | port-mac-address-regenerate           |
| .\*admin.test_ports.PortTestCasesResourceRequest                                                                | port-resource-request                 |
| .\*admin.test_routers_dvr                                                                                       | dvr                                   |
| .\*admin.test_routers_flavors                                                                                   | l3-flavors                            |
| .\*admin.test_routers_ha                                                                                        | l3-ha                                 |
| .\*test_floating_ips.FloatingIPPoolTestJSON                                                                     | floatingip-pools                      |
| .\*test_floating_ips.FloatingIPTestJSON.test_create_update_floatingip_port_details                              | fip-port-details                      |
| .\*test_metering_extensions                                                                                     | metering                              |
| .\*test_metering_negative                                                                                       | metering                              |
| .\*test_networks.NetworksSearchCriteriaTest.test_list_validation_filters                                        | filter-validation                     |
| .\*test_networks.NetworksTestAdmin.test_create_tenant_network_vxlan.                                            | vxlan                                 |
| .\*test_networks.NetworksTestJSON.test_create_update_network_dns_domain                                         | dns-integration                       |
| .\*test_port_forwardings                                                                                        | floating-ip-port-forwarding           |
| .\*test_ports.PortsTestJSON.test_create_port_with_propagate_uplink_status                                       | uplink-status-propagation             |
| .\*test_ports.PortsTestJSON.test_create_port_without_propagate_uplink_status                                    | uplink-status-propagation             |
| .\*test_ports.PortsTestJSON.test_create_update_port_with_dns_domain                                             | dns-domain-ports                      |
| .\*test_ports.PortsTestJSON.test_create_update_port_with_dns_name                                               | dns-integration                       |
| .\*test_ports.PortsTestJSON.test_create_update_port_with_no_dns_name                                            | dns-integration                       |
| .\*test_revisions.TestRevisions.test_update_dns_domain_bumps_revision                                           | dns-integration                       |
| .\*test_revisions.TestRevisions.test_update_router_extra_attributes_bumps_revision                              | l3-ha                                 |
| .\*test_router_interface_fip                                                                                    | router-interface-fip                  |
| .\*test_routers.DvrRoutersTest                                                                                  | dvr                                   |
| .\*test_routers.HaRoutersTest                                                                                   | l3-ha                                 |
| .\*test_routers.RoutersIpV6Test.test_extra_routes_atomic                                                        | extraroute-atomic                     |
| .\*test_routers.RoutersTest.test_extra_routes_atomic                                                            | extraroute-atomic                     |
| .\*test_routers_negative.DvrRoutersNegativeTest                                                                 | dvr                                   |
| .\*test_routers_negative.DvrRoutersNegativeTestExtended                                                         | dvr                                   |
| .\*test_routers_negative.HaRoutersNegativeTest                                                                  | l3-ha                                 |
| .\*test_security_groups.RbacSharedSecurityGroupTest                                                             | rbac-security-groups                  |
| .\*test_subnetpool_prefix_ops                                                                                   | subnetpool-prefix-ops                 |
| .\*test_subnetpools.SubnetPoolsSearchCriteriaTest.test_list_validation_filters                                  | filter-validation                     |
| .\*test_subnets.SubnetsSearchCriteriaTest.test_list_validation_filters                                          | filter-validation                     |
| .\*test_timestamp.TestTimeStamp.test_segment_with_timestamp                                                     | standard-attr-segment                 |
| .\*test_trunk.TrunkTestInheritJSONBase.test_add_subport                                                         | https://launchpad.net/bugs/1863707    |
| .\*test_trunk.TrunkTestMtusJSON                                                                                 | vxlan                                 |
| .\*test_trunk_negative.TrunkTestJSON.test_create_subport_invalid_inherit_network_segmentation_type              | vxlan                                 |
| .\*test_trunk_negative.TrunkTestMtusJSON                                                                        | vxlan                                 |
| .\*test_qos.QosMinimumBandwidthRuleTestJSON                                                                     | https://gerrit.opnfv.org/gerrit/69105 |
| .\*network.test_tags                                                                                            | tag-ext                               |
| .\*test_routers.RoutersIpV6Test.test_create_router_set_gateway_with_fixed_ip                                    | https://launchpad.net/bugs/1676207    |
| .\*test_routers.RoutersTest.test_create_router_set_gateway_with_fixed_ip                                        | https://launchpad.net/bugs/1676207    |
| .\*test_network_basic_ops.TestNetworkBasicOps.test_router_rescheduling                                          | l3_agent_scheduler                    |
| .\*test_network_advanced_server_ops.TestNetworkAdvancedServerOps.test_server_connectivity_cold_migration_revert | https://launchpad.net/bugs/1836595    |

Neutron API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma):
- Authenticate.validate_neutron
- NeutronNetworks.create_and_delete_networks
- NeutronNetworks.create_and_delete_ports
- NeutronNetworks.create_and_delete_routers
- NeutronNetworks.create_and_delete_subnets
- NeutronNetworks.create_and_list_networks
- NeutronNetworks.create_and_list_ports
- NeutronNetworks.create_and_list_routers
- NeutronNetworks.create_and_list_subnets
- NeutronSecurityGroup.create_and_delete_security_groups
- NeutronSecurityGroup.create_and_delete_security_group_rule
- NeutronNetworks.set_and_clear_router_gateway
- Quotas.neutron_update

#### 3.3.4.6 Compute - Nova

Nova API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma).

According to
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
the following test names must not be executed:

| test rejection regular expressions                                                                                        | reasons                            |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| .\*test_fixed_ips                                                                                                         | neutron                            |
| .\*test_fixed_ips_negative                                                                                                | neutron                            |
| .\*test_auto_allocate_network                                                                                             | shared networks                    |
| .\*test_flavors_microversions.FlavorsV255TestJSON                                                                         | max_microversion: 2.53             |
| .\*test_flavors_microversions.FlavorsV261TestJSON                                                                         | max_microversion: 2.53             |
| .\*test_floating_ips_bulk                                                                                                 | nova-network                       |
| .\*test_live_migration.LiveAutoBlockMigrationV225Test.test_iscsi_volume                                                   | block live migration               |
| .\*test_live_migration.LiveAutoBlockMigrationV225Test.test_volume_backed_live_migration                                   | volume-backed live migration       |
| .\*test_live_migration.LiveMigrationTest.test_iscsi_volume                                                                | block live migration               |
| .\*test_live_migration.LiveMigrationTest.test_volume_backed_live_migration                                                | volume-backed live migration       |
| .\*test_live_migration.LiveMigrationRemoteConsolesV26Test                                                                 | serial_console                     |
| .\*test_quotas.QuotasAdminTestV257                                                                                        | max_microversion: 2.53             |
| .\*certificates.test_certificates                                                                                         | cert                               |
| .\*test_quotas_negative.QuotasSecurityGroupAdminNegativeTest                                                              | https://launchpad.net/bugs/1186354 |
| .\*test_novnc                                                                                                             | vnc_console                        |
| .\*test_server_personality                                                                                                | personality                        |
| .\*test_servers.ServerShowV263Test.test_show_update_rebuild_list_server                                                   | certified_image_ref                |
| .\*test_servers_microversions.ServerShowV254Test                                                                          | max_microversion: 2.53             |
| .\*test_servers_microversions.ServerShowV257Test                                                                          | max_microversion: 2.53             |
| .\*test_servers_negative.ServersNegativeTestJSON.test_personality_file_contents_not_encoded                               | personality                        |
| .\*test_server_actions.ServerActionsTestJSON.test_change_server_password                                                  | change_password                    |
| .\*test_server_actions.ServerActionsTestJSON.test_get_vnc_console                                                         | vnc_console                        |
| .\*test_server_actions.ServerActionsTestJSON.test_reboot_server_soft                                                      | https://launchpad.net/bugs/1014647 |
| .\*test_security_group_default_rules                                                                                      | https://launchpad.net/bugs/1311500 |
| .\*test_security_groups_negative.SecurityGroupsNegativeTestJSON.test_security_group_create_with_duplicate_name            | neutron                            |
| .\*test_security_groups_negative.SecurityGroupsNegativeTestJSON.test_security_group_create_with_invalid_group_description | https://launchpad.net/bugs/1161411 |
| .\*test_security_groups_negative.SecurityGroupsNegativeTestJSON.test_security_group_create_with_invalid_group_name        | https://launchpad.net/bugs/1161411 |
| .\*test_security_groups_negative.SecurityGroupsNegativeTestJSON.test_update_security_group_with_invalid_sg_des            | neutron                            |
| .\*test_security_groups_negative.SecurityGroupsNegativeTestJSON.test_update_security_group_with_invalid_sg_id             | neutron                            |
| .\*test_security_groups_negative.SecurityGroupsNegativeTestJSON.test_update_security_group_with_invalid_sg_name           | neutron                            |
| .\*test_list_server_filters.ListServerFiltersTestJSON.test_list_servers_filtered_by_ip_regex                              | https://launchpad.net/bugs/1540645 |
| .\*servers.test_virtual_interfaces                                                                                        | nova-network                       |
| .\*compute.test_virtual_interfaces_negative                                                                               | nova-network                       |
| .\*compute.test_networks                                                                                                  | nova-network                       |
| .\*test_attach_volume.AttachVolumeMultiAttach                                                                             | volume_multiattach                 |
| .\*test_volume_boot_pattern.TestVolumeBootPattern.test_boot_server_from_encrypted_volume_luks                             | attach_encrypted_volume            |
| .\*test_volume_swap                                                                                                       | swap_volume                        |
| .\*test_encrypted_cinder_volumes                                                                                          | attach_encrypted_volume            |
| .\*test_minbw_allocation_placement                                                                                        | microversion                       |

Nova API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma):
- Authenticate.validate_nova
- NovaServers.boot_and_live_migrate_server
- NovaServers.boot_server_attach_created_volume_and_live_migrate
- NovaServers.boot_server_from_volume_and_live_migrate
- NovaKeypair.boot_and_delete_server_with_keypair
- NovaServers.boot_server_from_volume_and_delete
- NovaServers.pause_and_unpause_server
- NovaServers.boot_and_migrate_server
- NovaServers.boot_server_and_list_interfaces
- NovaServers.boot_server_associate_and_dissociate_floating_ip
- NovaServerGroups.create_and_delete_server_group
- Quotas.nova_update

#### 3.3.4.7 Orchestration - Heat

Heat API is covered in the OpenStack Gates via
[heat-tempest-plugin](https://opendev.org/openstack/heat-tempest-plugin) as
integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma)

According to
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
the following test names must not be executed:

| test rejection regular expressions                         | reasons                                            |
|------------------------------------------------------------|----------------------------------------------------|
| .\*functional.test_lbaasv2                                 | lbaasv2                                            |
| .\*functional.test_encryption_vol_type                     | https://storyboard.openstack.org/#!/story/2007804  |
| .\*RemoteStackTest.test_stack_create_with_cloud_credential | https://gerrit.opnfv.org/gerrit/c/functest/+/69926 |
| .\*scenario.test_aodh_alarm                                | aodh                                               |
| .\*tests.scenario.test_autoscaling_lb                      | lbaas                                              |
| .\*scenario.test_autoscaling_lbv2                          | lbaasv2                                            |
| .\*scenario.test_server_software_config                    | https://gerrit.opnfv.org/gerrit/c/functest/+/69926 |
| .\*test_volumes.VolumeBackupRestoreIntegrationTest         | https://gerrit.opnfv.org/gerrit/c/functest/+/69931 |
| .\*scenario.test_octavia_lbaas                             | octavia                                            |
| .\*scenario.test_server_cfn_init                           | https://gerrit.opnfv.org/gerrit/c/functest/+/70004 |

Heat API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fjerma):
- Authenticate.validate_heat
- HeatStacks.create_update_delete_stack
- HeatStacks.create_check_delete_stack
- HeatStacks.create_suspend_resume_delete_stack
- HeatStacks.list_stacks_and_resources

<a name="3.3.5"></a>
### 3.3.5 Dashboard

Horizon is covered in the OpenStack Gates via
[tempest-horizon](https://github.com/openstack/tempest-horizon) as integrated
in [Functest Healthcheck](https://git.opnfv.org/functest/tree/docker/healthcheck/testcases.yaml?h=stable%2Fjerma).

<a name="3.3.6"></a>
### 3.3.6 OpenStack API benchmarking

[Rally](https://opendev.org/openstack/rally) is tool and framework that allows
to perform OpenStack API benchmarking.

Here are the Rally-based test cases proposed by
[Functest Benchmarking CNTT](https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml?h=stable%2Fjerma)
- [rally_full](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_full_cntt-run-61/rally_full_cntt/rally_full_cntt.html):
  Functest scenarios iterating 10 times the mainline Rally scenarios
- [rally_jobs](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_jobs_cntt-run-60/rally_jobs_cntt/rally_jobs_cntt.html):
  Neutron scenarios executed in the OpenStack gates

At the time of writing, no KPI is defined in
[RA1 Core OpenStack Services APIs](../../../ref_arch/openstack/chapters/chapter05.md)
which would have asked for an update of the default SLA (maximum failure rate
of 0%) proposed in
[Functest Benchmarking CNTT](https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml?h=stable%2Fjerma)

#### 3.3.6.1 Identity - Keystone

[Functest rally_full_cntt](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_full_cntt-run-61/rally_full_cntt/rally_full_cntt.html):

| Scenarios                                     | Iterations |
|-----------------------------------------------|:----------:|
| Authenticate.keystone                         | 10         |
| KeystoneBasic.add_and_remove_user_role        | 10         |
| KeystoneBasic.create_add_and_list_user_roles  | 10         |
| KeystoneBasic.create_and_list_tenants         | 10         |
| KeystoneBasic.create_and_delete_role          | 10         |
| KeystoneBasic.create_and_delete_service       | 10         |
| KeystoneBasic.get_entities                    | 10         |
| KeystoneBasic.create_update_and_delete_tenant | 10         |
| KeystoneBasic.create_user                     | 10         |
| KeystoneBasic.create_tenant                   | 10         |
| KeystoneBasic.create_and_list_users           | 10         |
| KeystoneBasic.create_tenant_with_users        | 10         |

#### 3.3.6.2 Image - Glance

[Functest rally_full_cntt](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_full_cntt-run-61/rally_full_cntt/rally_full_cntt.html):

| Scenarios                                    | Iterations |
|----------------------------------------------|:----------:|
| Authenticate.validate_glance                 | 10         |
| GlanceImages.create_and_delete_image         | 10         |
| GlanceImages.create_and_list_image           | 10         |
| GlanceImages.list_images                     | 10         |
| GlanceImages.create_image_and_boot_instances | 10         |
| GlanceImages.create_and_deactivate_image     | 10         |
| GlanceImages.create_and_download_image       | 10         |
| GlanceImages.create_and_get_image            | 10         |
| GlanceImages.create_and_update_image         | 10         |

#### 3.3.6.3 Block Storage - Cinder

[Functest rally_full_cntt](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_full_cntt-run-61/rally_full_cntt/rally_full_cntt.html):

| Scenarios                                                     | Iterations |
|---------------------------------------------------------------|:----------:|
| Authenticate.validate_glance                                  | 10         |
| CinderVolumes.create_and_attach_volume                        | 10         |
| CinderVolumes.create_and_list_snapshots                       | 10         |
| CinderVolumes.create_and_list_volume                          | 10         |
| CinderVolumes.create_and_upload_volume_to_image               | 10         |
| CinderVolumes.create_nested_snapshots_and_attach_volume       | 10         |
| CinderVolumes.create_snapshot_and_attach_volume               | 10         |
| CinderVolumes.create_volume                                   | 10         |
| CinderVolumes.list_volumes                                    | 10         |
| CinderVolumes.create_and_delete_snapshot                      | 10         |
| CinderVolumes.create_and_delete_volume                        | 10         |
| CinderVolumes.create_and_extend_volume                        | 10         |
| CinderVolumes.create_from_volume_and_delete_volume            | 10         |
| CinderQos.create_and_get_qos                                  | 10         |
| CinderQos.create_and_list_qos                                 | 10         |
| CinderQos.create_and_set_qos                                  | 10         |
| CinderVolumeTypes.create_and_get_volume_type                  | 10         |
| CinderVolumeTypes.create_and_list_volume_types                | 10         |
| CinderVolumeTypes.create_and_update_volume_type               | 10         |
| CinderVolumeTypes.create_volume_type_and_encryption_type      | 10         |
| CinderVolumeTypes.create_volume_type_add_and_list_type_access | 10         |
| Quotas.cinder_update_and_delete                               | 10         |
| Quotas.cinder_update                                          | 10         |

#### 3.3.6.4 Object Storage - Swift

[Functest rally_full_cntt](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_full_cntt-run-61/rally_full_cntt/rally_full_cntt.html):

| Scenarios                                                     | Iterations |
|---------------------------------------------------------------|:----------:|
| SwiftObjects.create_container_and_object_then_list_objects    | 10         |
| SwiftObjects.list_objects_in_containers                       | 10         |
| SwiftObjects.create_container_and_object_then_download_object | 10         |
| SwiftObjects.create_container_and_object_then_delete_all      | 10         |
| SwiftObjects.list_and_download_objects_in_containers          | 10         |

#### 3.3.6.5 Networking - Neutron

[Functest rally_full_cntt](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_full_cntt-run-61/rally_full_cntt/rally_full_cntt.html):

| Scenarios                                                  | Iterations |
|------------------------------------------------------------|:----------:|
| Authenticate.validate_neutron                              | 10         |
| NeutronNetworks.create_and_update_networks                 | 10         |
| NeutronNetworks.create_and_update_ports                    | 10         |
| NeutronNetworks.create_and_update_routers                  | 10         |
| NeutronNetworks.create_and_update_subnets                  | 10         |
| NeutronNetworks.create_and_delete_networks                 | 10         |
| NeutronNetworks.create_and_delete_ports                    | 10         |
| NeutronNetworks.create_and_delete_routers                  | 10         |
| NeutronNetworks.create_and_delete_subnets                  | 10         |
| NeutronNetworks.create_and_list_networks                   | 10         |
| NeutronNetworks.create_and_list_ports                      | 10         |
| NeutronNetworks.create_and_list_routers                    | 10         |
| NeutronNetworks.create_and_list_subnets                    | 10         |
| NeutronSecurityGroup.create_and_delete_security_groups     | 10         |
| NeutronSecurityGroup.create_and_delete_security_group_rule | 10         |
| NeutronSecurityGroup.create_and_list_security_group_rules  | 10         |
| NeutronSecurityGroup.create_and_show_security_group        | 10         |
| NeutronNetworks.set_and_clear_router_gateway               | 10         |
| NeutronNetworks.create_and_show_ports                      | 10         |
| NeutronNetworks.create_and_show_routers                    | 10         |
| NeutronNetworks.create_and_show_subnets                    | 10         |
| Quotas.neutron_update                                      | 10         |

[Functest rally_jobs_cntt](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_jobs_cntt-run-60/rally_jobs_cntt/rally_jobs_cntt.html):

| Scenarios                                  | Iterations |
|--------------------------------------------|:----------:|
| NeutronNetworks.create_and_delete_networks | 40         |
| NeutronNetworks.create_and_delete_ports    | 40         |
| NeutronNetworks.create_and_delete_routers  | 40         |
| NeutronNetworks.create_and_delete_subnets  | 40         |
| NeutronNetworks.create_and_list_networks   | 100        |
| NeutronNetworks.create_and_list_ports      | 8          |
| NeutronNetworks.create_and_list_routers    | 40         |
| NeutronNetworks.create_and_list_subnets    | 40         |
| NeutronNetworks.create_and_update_networks | 40         |
| NeutronNetworks.create_and_update_ports    | 40         |
| NeutronNetworks.create_and_update_routers  | 40         |
| NeutronNetworks.create_and_update_subnets  | 100        |
| NeutronTrunks.create_and_list_trunks       | 4          |
| Quotas.neutron_update                      | 40         |

#### 3.3.6.6 Compute - Nova

[Functest rally_full_cntt](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_full_cntt-run-61/rally_full_cntt/rally_full_cntt.html):

| Scenarios                                                      | Iterations |
|----------------------------------------------------------------|:----------:|
| Authenticate.validate_nova                                     | 10         |
| NovaKeypair.create_and_delete_keypair                          | 10         |
| NovaKeypair.create_and_list_keypairs                           | 10         |
| NovaServers.boot_and_bounce_server                             | 10         |
| NovaServers.boot_and_delete_server                             | 10         |
| NovaServers.boot_and_list_server                               | 10         |
| NovaServers.boot_and_rebuild_server                            | 10         |
| NovaServers.snapshot_server                                    | 10         |
| NovaServers.boot_server_from_volume                            | 10         |
| NovaServers.boot_server                                        | 10         |
| NovaServers.list_servers                                       | 10         |
| NovaServers.resize_server                                      | 10         |
| NovaServers.boot_and_live_migrate_server                       | 10         |
| NovaServers.boot_server_attach_created_volume_and_live_migrate | 10         |
| NovaServers.boot_server_from_volume_and_live_migrate           | 10         |
| NovaKeypair.boot_and_delete_server_with_keypair                | 10         |
| NovaServers.boot_server_from_volume_and_delete                 | 10         |
| NovaServers.pause_and_unpause_server                           | 10         |
| NovaServers.boot_and_migrate_server                            | 10         |
| NovaServers.boot_server_and_list_interfaces                    | 10         |
| NovaServers.boot_and_get_console_url                           | 10         |
| NovaServers.boot_server_and_attach_interface                   | 10         |
| NovaServers.boot_server_attach_volume_and_list_attachments     | 10         |
| NovaServers.boot_server_associate_and_dissociate_floating_ip   | 10         |
| NovaServers.boot_and_associate_floating_ip                     | 10         |
| NovaServerGroups.create_and_delete_server_group                | 10         |
| NovaServerGroups.create_and_get_server_group                   | 10         |
| NovaServerGroups.create_and_list_server_groups                 | 10         |
| Quotas.nova_update                                             | 10         |

#### 3.3.6.7 Orchestration - Heat

[Functest rally_full_cntt](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-cntt-jerma-rally_full_cntt-run-61/rally_full_cntt/rally_full_cntt.html):

| Scenarios                                     | Iterations |
|-----------------------------------------------|:----------:|
| Authenticate.validate_heat                    | 10         |
| HeatStacks.create_and_delete_stack            | 10         |
| HeatStacks.create_and_list_stack              | 10         |
| HeatStacks.create_update_delete_stack         | 10         |
| HeatStacks.create_check_delete_stack          | 10         |
| HeatStacks.create_suspend_resume_delete_stack | 10         |
| HeatStacks.list_stacks_and_resources          | 10         |

<a name="3.3.7"></a>
### 3.3.7 Dataplane benchmarking

[Functest Benchmarking CNTT](https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml?h=stable%2Fjerma)
offers two benchmarking dataplane test cases leveraging on:
- [VMTP](http://vmtp.readthedocs.io/en/latest)
- [Shaker](http://pyshaker.readthedocs.io/en/latest/)

[VMTP](http://vmtp.readthedocs.io/en/latest) is a small python application that
will automatically perform ping connectivity, round trip time measurement
(latency) and TCP/UDP throughput measurement on any OpenStack deployment.

[Shaker](http://pyshaker.readthedocs.io/en/latest/) wraps around popular system
network testing tools like iperf, iperf3 and netperf (with help of flent).
[Shaker](http://pyshaker.readthedocs.io/en/latest/) is able to deploy OpenStack
instances and networks in different topologies.
[Shaker](http://pyshaker.readthedocs.io/en/latest/) scenario specifies the
deployment and list of tests to execute.

At the time of writing, no KPI is defined in CNTT chapters which would have
asked for an update of the default SLA proposed in
[Functest Benchmarking CNTT](https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml?h=stable%2Fjerma)

Industry Standard-based Benchmarking Projects

In addition to the dataplane testing described in Functest, two projects have integrated industry standard benchmarking test as described in [ETSI GS NFV-TST 009: Specification of Networking Benchmarks and Measurement Methods for NFVI](https://www.etsi.org/deliver/etsi_gs/NFV-TST/001_099/009/03.04.01_60/gs_NFV-TST009v030401p.pdf), and other IETF standards as well. 
- [SampleVNF](https://wiki.anuket.io/display/HOME/Sample+VNF)
- [ViNePERF](https://wiki.anuket.io/display/HOME/ViNePERF)

This type of testing is better suited to measure the networking capabilities of a compute node. The [rapid scripts](https://wiki.opnfv.org/display/SAM/Rapid+scripting) in conjunction with the [PROX tool](https://wiki.opnfv.org/pages/viewpage.action?pageId=12387840) offers an open source implementation for this type of testing.

The test automation in [ViNePERF](https://wiki.anuket.io/display/HOME/ViNePERF) includes many Industry Standard and customized tests in the [test list](https://wiki.anuket.io/display/HOME/Test+List). This open source tool allows use of several types of traffic generators (both hardware and several open source software types), and automated data plane path deployment on a baremetal host or use of Openstack and Kubernetes to instantiate the data plane. Also, configurations can allocate same + cross-NUMA cores, PMD core assignments, and Noisy-neighbor configuration.

### 3.3.7.1 VMTP

Here are the
[scenarios](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-jerma-vmtp-run-123/vmtp/vmtp.json)
executed by
[Functest vmtp](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-jerma-vmtp-run-123/vmtp/vmtp.html):
- VM to VM same network fixed IP (intra-node)
- VM to VM different network fixed IP (intra-node)
- VM to VM different network floating IP (intra-node)
- VM to VM same network fixed IP (inter-node)
- VM to VM different network fixed IP (inter-node)
- VM to VM different network floating IP (inter-node)

Here are all results per scenario:

| protocol | pkt_size | results          |
|----------|----------|------------------|
| ICMP     | 64       | rtt_avg_ms       |
| ICMP     | 64       | rtt_max_ms       |
| ICMP     | 64       | rtt_min_ms       |
| ICMP     | 64       | rtt_stddev       |
| ICMP     | 391      | rtt_avg_ms       |
| ICMP     | 391      | rtt_max_ms       |
| ICMP     | 391      | rtt_min_ms       |
| ICMP     | 391      | rtt_stddev       |
| ICMP     | 1500     | rtt_avg_ms       |
| ICMP     | 1500     | rtt_max_ms       |
| ICMP     | 1500     | rtt_min_ms       |
| ICMP     | 1500     | rtt_stddev       |
| UDP      | 128      | loss_rate        |
| UDP      | 128      | throughput_kbps  |
| UDP      | 1024     | loss_rate        |
| UDP      | 1024     | throughput_kbps  |
| UDP      | 8192     | loss_rate        |
| UDP      | 8192     | throughput_kbps  |
| TCP      | 65536    | rtt_ms           |
| TCP      | 65536    | throughput_kbps  |

### 3.3.7.2 Shaker

Here are the
[scenarios](http://artifacts.opnfv.org/functest/QQFD8QDOLI20/functest-opnfv-functest-benchmarking-jerma-shaker-run-124/shaker/report.json)
executed by Shaker:
- OpenStack L2
- OpenStack L3 East-West
- OpenStack L3 North-South
- OpenStack L3 North-South Performance

Here are all samples:

| test           | samples                |
|----------      |------------------------|
| Bi-directional | ping_icmp (ms)         |
| Bi-directional | tcp_download (Mbits/s) |
| Bi-directional | tcp_upload (Mbits/s)   |
| Download       | ping_icmp (ms)         |
| Download       | tcp_download (Mbits/s) |
| Upload         | ping_icmp (ms)         |
| Upload         | tcp_upload (Mbits/s)   |
| Ping           | ping_icmp (ms)         |
| Ping           | ping_udp (ms)          |
| TCP            | bandwidth (bit/s)      |
| TCP            | retransmits            |
| UDP            | packets (pps)          |

### 3.3.7.3 PROX

The generator used with the rapid scripts is PROX with a specific generator configuration file.
When multiple flows are requested, the generator starts randomizing bits in the source and destination UDP ports.
The number of flows to be generated during each run of the test is specified in the test files (e.g. TST009_Throughput.test).
Packet size used during the test is also defined in the test file. IMIX is not supported yet, but you could take the average packet size of the IMIX for now.
When defining n packet sizes with m different flow sizes, the test will run n x m times and will produce the results for these n x m combinations.
All throughput benchmarking is done by a generator sending packets to a reflector. This results in bidirectional traffic which should be identical (src and dest IP and ports swapped) if all traffic goes through.
The VMs or containers use only 1 vNIC for incoming and outgoing traffic. Multiple queues can be used.
Multiple VMs or containers can be deployed prior to running any tests. This allows to use generator-reflector pairs on the same or different compute nodes, on the same or different NUMA nodes.

### 3.3.7.4 ViNePERF

Similar to PROX (described above), the ViNePERF tool excels in automating tests and collecting the specific benchmarking results that allow clear comparison between a reference implementation's benchmark performance and an NFVI under test.

Deployments include the 
- phy2phy, 
- PVP, and 
- PVVP 
baremetal scenarios, and the Internal-Internal or External-External scenarios using Openstack or Kubernetes for data plane and network function configuration. See clause 6.2 of [ETSI GS NFV-TST 009: Specification of Networking Benchmarks and Measurement Methods for NFVI](https://www.etsi.org/deliver/etsi_gs/NFV-TST/001_099/009/03.04.01_60/gs_NFV-TST009v030401p.pdf).

<p align="center"><b>Table :</b> ViNePERF Test Results</p>

| protocol | pkt_size | results            |
|----------|----------|--------------------|
| UDP      | 64       | delay_avg_ms       |
| UDP      | 64       | delay_max_ms       |
| UDP      | 64       | delay_min_ms       |
| UDP      | 64       | throughput_Mbps    |
| UDP      | 128      | delay_avg_ms       |
| UDP      | 128      | delay_max_ms       |
| UDP      | 128      | delay_min_ms       |
| UDP      | 128      | throughput_Mbps    |
| UDP      | 256      | delay_avg_ms       |
| UDP      | 256      | delay_max_ms       |
| UDP      | 256      | delay_min_ms       |
| UDP      | 256      | throughput_Mbps    |
| UDP      | 512      | delay_avg_ms       |
| UDP      | 512      | delay_max_ms       |
| UDP      | 512      | delay_min_ms       |
| UDP      | 512      | throughput_Mbps    |
| UDP      | 1024     | delay_avg_ms       |
| UDP      | 1024     | delay_max_ms       |
| UDP      | 1024     | delay_min_ms       |
| UDP      | 1024     | throughput_Mbps    |
| UDP      | 1500     | delay_avg_ms       |
| UDP      | 1500     | delay_max_ms       |
| UDP      | 1500     | delay_min_ms       |
| UDP      | 1500     | throughput_Mbps    |

<a name="3.3.8"></a>
### 3.3.8 Opensource VNF onboarding and testing

Running opensource VNFs is a key technical solution to ensure that the
platforms meet Network Functions Virtualization requirements.
[Functest VNF](https://git.opnfv.org/functest/tree/docker/vnf/testcases.yaml?h=stable%2Fjerma)
offers 5 test cases which automatically onboard and test the following 3
opensource VNFs:
- [Clearwater IMS](https://clearwater.readthedocs.io/en/stable/)
- [VyOS vRouter](https://www.vyos.io/)
- [OpenAirInterface vEPC](https://www.openairinterface.org/)

Here are the full list of orchestrators used for all these deployments:
- [Cloudify](https://cloudify.co/)
- [Heat](https://wiki.openstack.org/wiki/Heat)
- [Juju](https://jaas.ai/)

The VNF are covered by upstream tests when possible (see
[clearwater-live-test](https://github.com/Metaswitch/clearwater-live-test)) and
by Functest VNF tests in the other cases.

<a name="3.3.9"></a>
### 3.3.9 Tenants

<a name="3.3.10"></a>
### 3.3.10 LCM

<a name="3.3.11"></a>
### 3.3.11 Assurance

<a name="3.3.12"></a>
### 3.3.12 Security

<a name="3.3.13"></a>
### 3.3.13 Resilience

<a name="3.3.14"></a>
### 3.3.14 Bare-metal validations

<a name="3.4"></a>
## 3.4 Test Cases Traceability to Requirements

<a name="3.4.1"></a>
### 3.4.1 RM/RA-1 Requirements

According to [RC1 Chapter04](chapter04.md)
the following test cases must pass as they are for CNTT NFVI
Conformance:

| container                              | test case             | criteria |
|----------------------------------------|-----------------------|:--------:|
| opnfv/functest-healthcheck:jerma       | tempest_horizon       | PASS     |
| opnfv/functest-smoke-cntt:jerma        | tempest_neutron_cntt  | PASS     |
| opnfv/functest-smoke-cntt:jerma        | tempest_cinder_cntt   | PASS     |
| opnfv/functest-smoke-cntt:jerma        | tempest_keystone_cntt | PASS     |
| opnfv/functest-smoke-cntt:jerma        | rally_sanity_cntt     | PASS     |
| opnfv/functest-smoke-cntt:jerma        | tempest_full_cntt     | PASS     |
| opnfv/functest-smoke-cntt:jerma        | tempest_scenario_cntt | PASS     |
| opnfv/functest-smoke-cntt:jerma        | tempest_slow_cntt     | PASS     |
| opnfv/functest-benchmarking-cntt:jerma | rally_full_cntt       | PASS     |
| opnfv/functest-benchmarking-cntt:jerma | rally_jobs_cntt       | PASS     |
| opnfv/functest-benchmarking-cntt:jerma | vmtp                  | PASS     |
| opnfv/functest-benchmarking-cntt:jerma | shaker                | PASS     |
| opnfv/functest-vnf:jerma               | cloudify              | PASS     |
| opnfv/functest-vnf:jerma               | cloudify_ims          | PASS     |
| opnfv/functest-vnf:jerma               | heat_ims              | PASS     |
| opnfv/functest-vnf:jerma               | vyos_vrouter          | PASS     |
| opnfv/functest-vnf:jerma               | juju_epc              | PASS     |

<a name="3.4.2"></a>
### 3.4.2 TC Mapping to Requirements

| test case             | requirements                                                             |
|-----------------------|--------------------------------------------------------------------------|
| tempest_horizon       | Horizon testing                                                      |
| tempest_neutron_cntt  | Neutron API testing                                                      |
| tempest_cinder_cntt   | Cinder API testing                                                       |
| tempest_keystone_cntt | Keystone API testing                                                     |
| rally_sanity_cntt     | Keystone, Glance, Cinder, Swift, Neutron, Nova and Heat API testing      |
| tempest_full_cntt     | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| tempest_scenario_cntt | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| tempest_slow_cntt     | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| rally_full_cntt       | Keystone, Glance, Cinder, Swift, Neutron, Nova and Heat API benchmarking |
| rally_jobs_cntt       | Neutron API benchmarking                                                 |
| vmtp                  | Dataplane benchmarking                                                   |
| shaker                | Dataplane benchmarking                                                   |
| cloudify              | opensource VNF onboarding and testing                                    |
| cloudify_ims          | opensource VNF onboarding and testing                                    |
| heat_ims              | opensource VNF onboarding and testing                                    |
| vyos_vrouter          | opensource VNF onboarding and testing                                    |
| juju_epc              | opensource VNF onboarding and testing                                    |
