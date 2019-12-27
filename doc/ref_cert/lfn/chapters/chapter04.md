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
  * [4.3.5 OpenStack API benchmarking](#4.3.5)
  * [4.3.6 opensource VNF onboarding and testing](#4.3.6)
  * [4.3.7 Tenants](#4.3.7)
  * [4.3.8 LCM](#4.3.8)
  * [4.3.9 Assurance](#4.3.9)
  * [4.3.10 Security](#4.3.10)

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
It covers the test cases against networking management operations.


#### 4.3.4.6 Compute - Nova
It covers the test cases against compute management operations.

#### 4.3.4.7 Orchestration - Heat
It covers the test cases against orchestration operations.

<a name="4.3.5"></a>
### 4.3.5 OpenStack API benchmarking

[Rally](https://opendev.org/openstack/rally) is tool and framework that allows
to perform OpenStack API benchmarking.

Here are the Rally-based test cases proposed by
[Functest Benchmarking CNTT](https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml)
- [rally_full](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_full-run-324/rally_full/rally_full.html):
  Functest scenarios iterating 10 times the mainline Rally scenarios
- [rally_jobs](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_jobs-run-328/rally_jobs/rally_jobs.html):
  Neutron scenarios executed in the OpenStack gates

At the time of writing, no KPI is defined in
[RA1 Core OpenStack Services APIs](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter05.md)
which would have asked for an update of the default SLA proposed in
[Functest Benchmarking CNTT](https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml)

#### 4.3.5.1 Identity - Keystone

[Functest rally_full](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_full-run-324/rally_full/rally_full.html):

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

#### 4.3.5.2 Image - Glance

[Functest rally_full](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_full-run-324/rally_full/rally_full.html):

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

#### 4.3.5.3 Block Storage - Cinder

[Functest rally_full](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_full-run-324/rally_full/rally_full.html):

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

#### 4.3.5.4 Object Storage - Swift

[Functest rally_full](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_full-run-324/rally_full/rally_full.html):

| Scenarios                                                     | Iterations |
|---------------------------------------------------------------|:----------:|
| SwiftObjects.create_container_and_object_then_list_objects    | 10         |
| SwiftObjects.list_objects_in_containers                       | 10         |
| SwiftObjects.create_container_and_object_then_download_object | 10         |
| SwiftObjects.create_container_and_object_then_delete_all      | 10         |
| SwiftObjects.list_and_download_objects_in_containers          | 10         |

#### 4.3.5.5 Networking - Neutron

[Functest rally_full](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_full-run-324/rally_full/rally_full.html):

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

[Functest rally_jobs](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_jobs-run-328/rally_jobs/rally_jobs.html):

| Scenarios                                    | Iterations |
|----------------------------------------------|:----------:|
| NeutronNetworks.create_and_delete_networks   | 40         |
| NeutronNetworks.create_and_delete_ports      | 40         |
| NeutronNetworks.create_and_delete_routers    | 40         |
| NeutronNetworks.create_and_delete_subnets    | 40         |
| NeutronNetworks.create_and_list_networks     | 100        |
| NeutronNetworks.create_and_list_ports        | 8          |
| NeutronNetworks.create_and_list_routers      | 40         |
| NeutronNetworks.create_and_list_subnets      | 40         |
| NeutronNetworks.create_and_update_networks   | 40         |
| NeutronNetworks.create_and_update_ports      | 40         |
| NeutronNetworks.create_and_update_routers    | 40         |
| NeutronNetworks.create_and_update_subnets    | 100        |
| NeutronTrunks.create_and_list_trunk_subports | 4          |
| Quotas.neutron_update                        | 40         |

#### 4.3.5.6 Compute - Nova

[Functest rally_full](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_full-run-324/rally_full/rally_full.html):

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

#### 4.3.5.7 Orchestration - Heat

[Functest rally_full](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-rally_full-run-324/rally_full/rally_full.html):

| Scenarios                                     | Iterations |
|-----------------------------------------------|:----------:|
| Authenticate.validate_heat                    | 10         |
| HeatStacks.create_and_delete_stack            | 10         |
| HeatStacks.create_and_list_stack              | 10         |
| HeatStacks.create_update_delete_stack         | 10         |
| HeatStacks.create_check_delete_stack          | 10         |
| HeatStacks.create_suspend_resume_delete_stack | 10         |
| HeatStacks.list_stacks_and_resources          | 10         |

<a name="4.3.6"></a>
### 4.3.6 opensource VNF onboarding and testing

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

<a name="4.3.7"></a>
### 4.3.7 Tenants

<a name="4.3.8"></a>
### 4.3.8 LCM

<a name="4.3.9"></a>
### 4.3.9 Assurance

<a name="4.3.10"></a>
### 4.3.10 Security
