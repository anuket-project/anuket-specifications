[<< Back](../../openstack)

# 5. Interfaces and APIs
<p align="right"><img src="../figures/bogo_dfp.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 Introduction](#5.1)
* [5.2 Core OpenStack Services APIs](#5.2)
* [5.3 Consolidated Set of APIs](#5.3)

<a name="5.1"></a>
## 5.1 Introduction

This chapter presents a consolidated set of OpenStack Service APIs corresponding to the ETSI NFV Nf-Vi, Vi-Vnfm and Or-Vi interfaces.
The OpenStack Train version is used as the baseline for these APIs and CLIs in this Reference Architecture (RA-1) version. Any Cloud Infrastructure + VIM reference
implementations that **get certified by RC** can be considered as CNTT RA Conformant.

The Chapter presents the APIs for the core OpenStack services defined in Chapter 3 and a
consolidated view of these and other APIs that are of interest.

OpenStack is a multi-project framework composed of services evolving independently. It is not enough to rely only on the
OpenStack release to characterise the capabilities supported by these services. Regarding OpenStack services APIs,
an "API version" is associated to each OpenStack service.
In addition to major API versions, some OpenStack services (Nova, Glance, Keystone, Cinder...) support microversions.
The microversions allow to introduce new features over time.
In this chapter, the **major version** and **microversion** are specified per service.
The mentioned microversion is the minimal microversion that supports the features requested for CNTT.
For the purpose of conformance tests, this chapter also identifies the set of the features, offered by a service, that are mandatory for CNTT compliant implementation.

<a name="5.2"></a>
## 5.2. Core OpenStack Services APIs

Please note that OpenStack provides a maximum microversion to be used with an OpenStack release. In the following sections the "Maximal API Version" refers to this maximum microversion specified for the OpenStack Train release. Please note that in Reference Conformance (RC-1) testing, the System Under Test (SUT) can utilise newer microversions because of the OpenStack microversion policies. As per multiple OpenStack services documentation, for example the [Compute Service](https://docs.openstack.org/api-guide/compute/microversions.html), "A cloud that is upgraded to support newer microversions will still support all older microversions to maintain the backward compatibility for those users who depend on older microversions."

### 5.2.1. Keystone

| **OpenStack Service** | **API Version** | **Maximal API Microversion** |
|-----------------------|-----------------|------------------------------|
| Identity: Keystone    | v3              | 3.13                         |

| **Keystone Features**   | **Mandatory** |
|-------------------------|:-------------:|
| application_credentials | X             |
| external_idp            |               |
| federation              |               |
| oauth1                  |               |
| project_tags            | X             |
| security_compliance     | X             |
| trust                   | X             |

Identity API v3: https://docs.openstack.org/api-ref/identity/v3/index.html

Identity API v3 extensions: https://docs.openstack.org/api-ref/identity/v3-ext/

Security compliance and PCI-DSS: https://docs.openstack.org/keystone/train/admin/configuration.html#security-compliance-and-pci-dss

### 5.2.2 Glance

| **OpenStack Service** | **API Version** | **Maximal API Microversion** |
|-----------------------|-----------------|------------------------------|
| Image: Glance         | v2              | 2.9                          |

Image Service Versions: https://docs.openstack.org/api-ref/image/versions/index.html#version-history

### 5.2.3. Cinder

| **OpenStack Service** | **API Version** | **Maximal API Microversion** |
|-----------------------|-----------------|------------------------------|
| Block Storage: Cinder | v3              | 3.59                         |

| **Cinder Features**    | **Mandatory** |
|------------------------|:-------------:|
| backup                 | X             |
| clone                  | X             |
| consistency_group      |               |
| extend_attached_volume |               |
| manage_snapshot        | X             |
| manage_volume          | X             |
| multi_backend          |               |
| snapshot               | X             |
| volume_revert          | X             |

Block Storage API: https://docs.openstack.org/api-ref/block-storage/

REST API Version History: https://docs.openstack.org/cinder/latest/contributor/api_microversion_history.html

### 5.2.4. Swift

| **OpenStack Service** | **API Version** |
|-----------------------|-----------------|
| Object Storage: Swift | v1              |

| **Swift Features** | **Mandatory** |
|--------------------|:-------------:|
| account_quotas     | X             |
| bulk_delete        | X             |
| bulk_upload        | X             |
| container_quotas   | X             |
| container_sync     |               |
| crossdomain        | X             |
| discoverability    | X             |
| form_post          | X             |
| ratelimit          | X             |
| s3api              |               |
| slo                | X             |
| staticweb          | X             |
| symlink            | X             |
| temp_url           | X             |
| tempauth           | X             |
| versioned_writes   | X             |

Object Storage API: https://docs.openstack.org/api-ref/object-store/index.html

Discoverability: https://docs.openstack.org/swift/latest/api/discoverability.html

### 5.2.5. Neutron

| **OpenStack Service** |  **API Version**  |
|-----------------------|-------------------|
| Networking: Neutron   | v2.0              |

| **Neutron Extensions**         | **Mandatory** |
|--------------------------------|:-------------:|
| address-scope                  | X             |
| agent                          | X             |
| allowed-address-pairs          | X             |
| auto-allocated-topology        | X             |
| availability_zone              | X             |
| availability_zone_filter       | X             |
| binding                        | X             |
| binding-extended               | X             |
| default-subnetpools            | X             |
| dhcp_agent_scheduler           |               |
| dns-domain-ports               |               |
| dns-integration                |               |
| dvr                            |               |
| empty-string-filtering         | X             |
| ext-gw-mode                    | X             |
| external-net                   | X             |
| extra_dhcp_opt                 | X             |
| extraroute                     | X             |
| extraroute-atomic              |               |
| flavors                        | X             |
| filter-validation              |               |
| fip-port-details               |               |
| floating-ip-port-forwarding    |               |
| floatingip-pools               |               |
| ip-substring-filtering         | X             |
| l3_agent_scheduler             |               |
| l3-flavors                     |               |
| l3-ha                          |               |
| logging                        |               |
| metering                       |               |
| multi-provider                 | X             |
| net-mtu                        | X             |
| net-mtu-writable               | X             |
| network_availability_zone      | X             |
| network-ip-availability        | X             |
| network-segment-range          |               |
| pagination                     | X             |
| port-mac-address-regenerate    |               |
| port-resource-request          |               |
| port-security                  | X             |
| port-security-groups-filtering | X             |
| project-id                     | X             |
| provider                       | X             |
| rbac-policies                  | X             |
| router                         | X             |
| router_availability_zone       | X             |
| qos                            | X             |
| qos-bw-limit-direction         | X             |
| qos-bw-minimum-ingress         | X             |
| qos-default                    | X             |
| qos-fip                        | X             |
| qos-gateway-ip                 | X             |
| qos-rule-type-details          | X             |
| qos-rules-alias                | X             |
| quotas                         | X             |
| quota_details                  | X             |
| revision-if-match              | X             |
| rbac-security-groups           |               |
| router-interface-fip           |               |
| security-group                 | X             |
| service-type                   | X             |
| sorting                        | X             |
| standard-attr-description      | X             |
| standard-attr-revisions        | X             |
| standard-attr-tag              | X             |
| standard-attr-timestamp        | X             |
| subnet_allocation              | X             |
| subnet-service-types           | X             |
| subnetpool-prefix-ops          |               |
| tag-ext                        |               |
| trunk                          | X             |
| trunk-details                  | X             |
| uplink-status-propagation      |               |

| **Neutron Type Drivers** | **Mandatory** |
|--------------------------|:-------------:|
| geneve                   |               |
| gre                      |               |
| vlan                     | X             |
| vxlan                    |               |

Networking Service APIs: https://docs.openstack.org/api-ref/network/

The exhaustive list of extensions is available at https://docs.openstack.org/api-ref/network/v2/

### 5.2.6. Nova

| **OpenStack Service** | **API Version** | **Maximal API Microversion** |
|-----------------------|-----------------|------------------------------|
| Compute: Nova         | v2.1            | 2.79                         |

| **Nova Features**        | **Mandatory** |
|--------------------------|:-------------:|
| attach_encrypted_volume  |               |
| cert                     |               |
| change_password          |               |
| cold_migration           | X             |
| console_output           | X             |
| disk_config              | X             |
| instance_password        | X             |
| interface_attach         | X             |
| live_migration           | X             |
| metadata_service         | X             |
| pause                    | X             |
| personality              |               |
| rdp_console              |               |
| rescue                   | X             |
| resize                   | X             |
| serial_console           |               |
| shelve                   | X             |
| snapshot                 | X             |
| spice_console            |               |
| suspend                  | X             |
| swap_volume              |               |
| vnc_console              |               |
| volume_multiattach       |               |

Compute API: https://docs.openstack.org/api-ref/compute/

REST API Version History: https://docs.openstack.org/nova/latest/reference/api-microversion-history.html

### 5.2.7. Placement

|**OpenStack Service** |  **API Version** | **Maximal API Microversion** |
|----------------------|------------------|------------------------------|
| Placement            | v1               | 1.36                         |

Placement API: https://docs.openstack.org/api-ref/placement/

REST API Version History: https://docs.openstack.org/placement/latest/placement-api-microversion-history.html

### 5.2.8. Heat

|**OpenStack Service** | **API Version** | **Maximal Template Version** |
|----------------------|-----------------|------------------------------|
| Orchestration: Heat  | v1              | 2018-08-31                   |

Orchestration Service API: https://docs.openstack.org/api-ref/orchestration/

Template version history: https://docs.openstack.org/heat/latest/template_guide/hot_spec.html

Heat Orchestration Template (HOT) specification: https://docs.openstack.org/heat/latest/template_guide/hot_spec.html#rocky

<a name="5.3"></a>
## 5.3. Consolidated Set of APIs

### 5.3.1. OpenStack Interfaces
This section illustrates some of the Interfaces provided by OpenStack; the exhaustive list of APIs is available
at https://docs.openstack.org/api-ref/.

OpenStack REST APIs are simple to interact with using either of two options. Clients can either call the APIs
directly using the HTTP or REST library, or they can use one of the many programming language specific cloud
libraries.

**APIs**

| **OpenStack Service** | Link for API list                                    | **API Version** | **Maximal API Microversion** |
|-----------------------|------------------------------------------------------|-----------------|------------------------------|
| Identity: Keystone    | https://docs.openstack.org/api-ref/identity/v3/      | v3              | 3.13                         |
| Compute: Nova         | https://docs.openstack.org/api-ref/compute/          | v2.1            | 2.79                         |
| Networking: Neutron   | https://docs.openstack.org/api-ref/network/v2/       | v2.0            |                              |
| Image: Glance         | https://docs.openstack.org/api-ref/image/v2/         | v2              | 2.9                          |
| Block Storage: Cinder | https://docs.openstack.org/api-ref/block-storage/v3/ | v3              | 3.59                         |
| Object Storage: Swift | https://docs.openstack.org/api-ref/object-store/     | v1              |                              |
| Placement             | https://docs.openstack.org/api-ref/placement/        | v1              | 1.36                         |
| Orchestration: Heat   | https://docs.openstack.org/api-ref/orchestration/v1/ | v1              |                              |
<!--
| Acceleration: Cyborg  | https://docs.openstack.org/api-ref/accelerator/v2/ | v2    |
-->

### 5.3.2. Kubernetes Interfaces
The Kubernetes APIs are available at https://kubernetes.io/docs/concepts/overview/kubernetes-api/.

### 5.3.3. KVM Interfaces
The KVM APIs are documented in Section 4 of the document https://www.kernel.org/doc/Documentation/virtual/kvm/api.txt.

#### 5.3.3.1. Libvirt Interfaces
The Libvirt APIs are documented in https://libvirt.org/html/index.html.

### 5.3.4. Barbican

| **OpenStack Service**           | **API Version** |
|---------------------------------|-----------------|
| Key Manager: Barbican           | v1              |

Barbican API Documentation: https://docs.openstack.org/barbican/latest/api/
