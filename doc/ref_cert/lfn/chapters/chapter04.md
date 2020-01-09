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
  * [4.3.6 Dataplane Benchmarking](#4.3.6)
  * [4.3.7 opensource VNF onboarding and testing](#4.3.7)
  * [4.3.8 Tenants](#4.3.8)
  * [4.3.9 LCM](#4.3.9)
  * [4.3.10 Assurance](#4.3.10)
  * [4.3.11 Security](#4.3.11)

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

The [OpenStack Gates](https://opendev.org/openstack/devstack-gate) verify all
changes proposed mostly by running thousands of Tempest tests completed by
Rally scenarios in a few cases. Skipping tests is allowed in all OpenStack
Gates and only failures rate the review -1 because of the multiple capabilities
and backends selected in the different Gate jobs. The classical
[Functest containers](https://wiki.opnfv.org/pages/viewpage.action?pageId=29098314)
conform to this model which also fits the heterogeneous user deployments.

From a CNTT Compliance state point, the capabilities are well described in
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
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
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})

According to Hunter (the oldest OPNFV active release), the following software
versions are considered here to verify OpenStack Pike selected by CNTT:

| software                | version |
|-------------------------|---------|
| Functest                | hunter  |
| Cinder Tempest plugin   | 0.2.0   |
| Keystone Tempest plugin | 0.1.0   |
| Neutron                 | rocky   |
| Neutron Tempest plugin  | 0.3.0   |
| Rally OpenStack         | 1.5.0   |
| Tempest                 | 21.0.0  |

#### 4.3.4.1 Identity - Keystone

Keystone API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) and
[keystone-tempest-plugin](https://opendev.org/openstack/keystone-tempest-plugin)
as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml).

According to
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
the following test names must not be executed:

| test rejection regular expressions        | reasons    |
|-------------------------------------------|------------|
| .\*scenario.test_federated_authentication | federation |
| .\*identity.admin.v2                      | API v2     |
| .\*identity.v2                            | API v2     |

Keystone API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml):
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

#### 4.3.4.2 Image - Glance

Glance API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml).

According to
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
the following test names must not be executed:

| test rejection regular expressions | reasons |
|------------------------------------|---------|
| .\*image.v1                        | API v1  |

Glance API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml):
- Authenticate.validate_glance
- GlanceImages.create_and_delete_image
- GlanceImages.create_and_list_image
- GlanceImages.list_images
- GlanceImages.create_image_and_boot_instances

#### 4.3.4.3 Block Storage - Cinder

Cinder API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) and
[cinder-tempest-plugin](https://opendev.org/openstack/cinder-tempest-plugin)
as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml).

According to
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
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
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml):
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

#### 4.3.4.4 Object Storage - Swift

Swift API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml).

According to
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
the following test names must not be executed:

| test rejection regular expressions                                      | reasons                            |
|-------------------------------------------------------------------------|------------------------------------|
| .\*test_container_sync.ContainerSyncTest.test_container_synchronization | https://launchpad.net/bugs/1317133 |

Swift API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml):
- SwiftObjects.create_container_and_object_then_list_objects
- SwiftObjects.list_objects_in_containers
- SwiftObjects.create_container_and_object_then_download_object
- SwiftObjects.create_container_and_object_then_delete_all
- SwiftObjects.list_and_download_objects_in_containers

#### 4.3.4.5 Networking - Neutron

Neutron API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) and
[neutron-tempest-plugin](https://opendev.org/openstack/neutron-tempest-plugin)
as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml).

According to
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
the following test names must not be executed:

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

Nova API is covered in the OpenStack Gates via
[Tempest](https://opendev.org/openstack/tempest) as integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml).

According to
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
the following test names must not be executed:

| test rejection regular expressions                                                                                        | reasons                            |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| .\*test_fixed_ips                                                                                                         | neutron                            |
| .\*test_fixed_ips_negative                                                                                                | neutron                            |
| .\*test_auto_allocate_network                                                                                             | shared networks                    |
| .\*test_floating_ips_bulk                                                                                                 | nova-network                       |
| .\*test_live_migration.LiveAutoBlockMigrationV225Test.test_iscsi_volume                                                   | block live migration               |
| .\*test_live_migration.LiveAutoBlockMigrationV225Test.test_volume_backed_live_migration                                   | volume-backed live migration       |
| .\*test_live_migration.LiveMigrationTest.test_iscsi_volume                                                                | block live migration               |
| .\*test_live_migration.LiveMigrationTest.test_volume_backed_live_migration                                                | volume-backed live migration       |
| .\*test_live_migration.LiveMigrationRemoteConsolesV26Test                                                                 | serial_console                     |
| .\*certificates.test_certificates                                                                                         | cert                               |
| .\*test_quotas_negative.QuotasSecurityGroupAdminNegativeTest                                                              | https://launchpad.net/bugs/1186354 |
| .\*test_novnc                                                                                                             | vnc_console                        |
| .\*test_server_personality                                                                                                | personality                        |
| .\*test_servers.ServerShowV263Test.test_show_update_rebuild_list_server                                                   | certified_image_ref                |
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
| .\*test_stamp_pattern.TestStampPattern.test_stamp_pattern                                                                 | https://launchpad.net/bugs/1664793 |
| .\*test_volume_migrate_attached                                                                                           | https://launchpad.net/bugs/1664793 |
| .\*test_minbw_allocation_placement                                                                                        | microversion                       |

Nova API is also covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml):
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

#### 4.3.4.7 Orchestration - Heat

Heat API is not covered in the OpenStack Gates neither via
[Tempest](https://opendev.org/openstack/tempest) nor
[heat-tempest-plugin](https://opendev.org/openstack/heat-tempest-plugin).

Heat API is covered by [Rally](https://opendev.org/openstack/rally).

Here are the mainline tasks integrated in
[Functest Smoke CNTT](https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml):
- Authenticate.validate_heat
- HeatStacks.create_update_delete_stack
- HeatStacks.create_check_delete_stack
- HeatStacks.create_suspend_resume_delete_stack
- HeatStacks.list_stacks_and_resources

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
[RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
which would have asked for an update of the default SLA (maximum failure rate
of 0%) proposed in
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
### 4.3.6 Dataplane benchmarking

[Functest Benchmarking CNTT](https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml)
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
[Functest Benchmarking CNTT](https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml)

### 4.3.6.1 VMTP

Here are the
[scenarios](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-vmtp-run-328/vmtp/vmtp.json)
executed by
[Functest vmtp](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-vmtp-run-328/vmtp/vmtp.html):
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

### 4.3.6.2 Shaker

Here are the
[scenarios](http://artifacts.opnfv.org/functest/IR6NYE2BYC8W/functest-opnfv-functest-benchmarking-hunter-shaker-run-329/shaker/report.json)
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

<a name="4.3.7"></a>
### 4.3.7 opensource VNF onboarding and testing

Running opensource VNFs is a key technical solution to ensure that the
platforms meet Network Functions Virtualization requirements.
[Functest VNF](https://git.opnfv.org/functest/tree/docker/vnf/testcases.yaml)
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

<a name="4.3.8"></a>
### 4.3.8 Tenants

<a name="4.3.9"></a>
### 4.3.9 LCM

<a name="4.3.10"></a>
### 4.3.10 Assurance

<a name="4.3.11"></a>
### 4.3.11 Security
