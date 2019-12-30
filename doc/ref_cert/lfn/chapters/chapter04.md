[<< Back](../)

# 4. NFVI Test Case Traceability to Architecture Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Selection Criteria](#4.2)
* [4.3 Traceability Matrix](#4.3)
  * [4.3.1 Architecture and OpenStack Based](#4.3.1)
  * [4.3.2 Infrastructure](#4.3.2)
  * [4.3.3 VIM](#4.3.3)
  * [4.3.4 Interfaces & APIs](#4.3.4)
  * [4.3.5 opensource VNF onboarding and testing](#4.3.5)
  * [4.3.6 Tenants](#4.3.6)
  * [4.3.7 LCM](#4.3.7)
  * [4.3.8 Assurance](#4.3.8)
  * [4.3.9 Security](#4.3.9)

<a name="4.1"></a>
## 4.1 Introduction

The scope of this chapter is to identify and list down test cases based on requirements defined in [Reference Architecture-1 (RA-1)](../../../ref_arch/openstack/README.md). This will serve as traceability between test cases and requirements.

Note that each requirement may have one or more test cases associated with it.

**must**: Test Cases that are marked as must are considered mandatory and must pass succesfully.

**should**: Test Cases that are marked as should are expected to be fulfilled by NFVI but it is up to each service provider to accept an NFVI tagetting reference architecture that is not reflecting on any of those requirements. The same applies to should not.

**may**: Test cases that are marked as may are considered optional. The same applies to may not.

<a name="4.2"></a>
## 4.2 Selection Criteria
> Test cases below are selected based on available test cases in open-source tools like OPNFV FuncTest, YardStick, DoveTail etc.

<a name="4.3"></a>
## 4.3 Traceability Matrix

- Write content that explains this section defines the mapping, or traceability of RM/RA-1 requirements to test cases.

<a name="4.3.1"></a>
### 4.3.1 Architecture and OpenStack Requirements

- Describe and define in detail, RM/RA-1 OpenStack requirements.

<a name="4.3.2"></a>
### 4.3.2 Infrastructure


| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.test.inf.01` | Compute | Create a virtual machine with CPU pinning and 2 NUMA nodes. | `req.inf.com.05` |
| `cert.test.inf.02` | Compute | Create a virtual machine with CPU pinning enabled. | `req.inf.com.06` |
| `cert.test.inf.03` | Compute | Create 2 virtual machines and associate block storage to it. | `req.inf.stg.01	` |
| `cert.test.inf.04` | Compute | Create 2 virtual machines which are booted from block storage. | `req.inf.stg.01	` |

<a name="4.3.3"></a>
### 4.3.3 VIM


| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.test.vim.01` | VIM | Create a virtual machine with CPU pinning, HugePages and 2 NUMA nodes. | `req.vim.04` |
| `cert.test.vim.02` | VIM | Upload an image to image repository and download it back. | `req.vim.05` |
| `cert.test.vim.03` | VIM | Deploy a heat stack having 2 virtual machines with associated network. | `req.vim.06` |
| `cert.test.vim.04` | VIM | Create 2 tenants and then create virtual machine in each tenant. | `req.vim.07` |

<a name="4.3.4"></a>
### 4.3.4 Interfaces & APIs
This defines the test cases around the functionality that are exposed by OpenStack APIs. All the defined OpenStack
service APIs in RA-1's [chapter 05](../../../ref_arch/openstack/chapters/chapter05.md) will be the scope here.

Note: It will only target the functionality that are exposed by standard OpenStack APIs.  

#### 4.3.4.1 Identity - Keystone

It covers the test cases against identity management operations like user management, project management, multi-tenancy etc.

| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.test.vim.01` | API | Show API endpoint catalog. It *must* have endpoint for each Core service. | `req.int.api.01` |

#### 4.3.4.2 Image - Glance
It covers the test cases against image management operations.


#### 4.3.4.3 Block Storage - Cinder
It covers the test cases against volume management operations.

#### 4.3.4.4 Object Storage - Swift
It covers the test cases against object management operations.


#### 4.3.4.5 Networking - Neutron

Neutron API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) and
[neutron-tempest-plugin](https://opendev.org/openstack/neutron-tempest-plugin)
as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml).

According to
[RA1 Core OpenStack Services APIs](/doc/ref_arch/openstack/chapters/chapter05.html)
the next test names must not be executed:

| test rejection regular expressions                                           | reasons                               |
|------------------------------------------------------------------------------|---------------------------------------|
| .\*test_logging                                                              | logging                               |
| .\*test_logging_negative                                                     | logging                               |
| .\*test_network_segment_range                                                | network-segment-range                 |
| .\*test_ports.PortTestCasesResourceRequest                                   | port-resource-request                 |
| .\*test_floating_ips.FloatingIPPoolTestJSON                                  | floatingip-pools                      |
| .\*test_metering_extensions                                                  | metering                              |
| .\*test_metering_negative                                                    | metering                              |
| .\*test_networks.NetworksTestJSON.test_create_update_network_dns_domain      | dns-integration                       |
| .\*test_ports.PortsTestJSON.test_create_port_with_propagate_uplink_status    | uplink-status-propagation             |
| .\*test_ports.PortsTestJSON.test_create_port_without_propagate_uplink_status | uplink-status-propagation             |
| .\*test_ports.PortsTestJSON.test_create_update_port_with_dns_domain          | dns-domain-ports                      |
| .\*test_ports.PortsTestJSON.test_create_update_port_with_dns_name            | dns-integration                       |
| .\*test_ports.PortsTestJSON.test_create_update_port_with_no_dns_name         | dns-integration                       |
| .\*test_revisions.TestRevisions.test_update_dns_domain_bumps_revision        | dns-integration                       |
| .\*test_router_interface_fip                                                 | router-interface-fip                  |
| .\*test_security_groups.RbacSharedSecurityGroupTest                          | rbac-security-groups                  |
| .\*test_timestamp.TestTimeStamp.test_segment_with_timestamp                  | standard-attr-segment                 |
| .\*test_qos.QosMinimumBandwidthRuleTestJSON                                  | https://gerrit.opnfv.org/gerrit/69105 |
| .\*network.test_tags                                                         | tag-ext                               |
| .\*test_routers.RoutersIpV6Test.test_create_router_set_gateway_with_fixed_ip | https://launchpad.net/bugs/1676207    |
| .\*test_routers.RoutersTest.test_create_router_set_gateway_with_fixed_ip     | https://launchpad.net/bugs/1676207    |
| .\*test_network_v6                                                           | https://gerrit.opnfv.org/gerrit/69105 |

Neutron API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml):
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

#### 4.3.4.6 Compute - Nova
It covers the test cases against compute management operations.

#### 4.3.4.7 Orchestration - Heat
It covers the test cases against orchestration operations.

<a name="4.3.5"></a>
### 4.3.5 opensource VNF onboarding and testing

Running opensource VNFs is a key technical solution to ensure that the
platforms meet Network Functions Virtualization requirements.
[Functest VNF](https://git.opnfv.org/functest/tree/docker/vnf/testcases.yaml)
offers 5 test cases which automatically onboard and test the next 3 opensource
VNFs:
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

<a name="4.3.6"></a>
### 4.3.6 Tenants

<a name="4.3.7"></a>
### 4.3.7 LCM

<a name="4.3.8"></a>
### 4.3.8 Assurance

<a name="4.3.9"></a>
### 4.3.9 Security
