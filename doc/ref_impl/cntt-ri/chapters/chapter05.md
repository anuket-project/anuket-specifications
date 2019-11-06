[<< Back](../)

# 5. Installer Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 Introduction](#5.1)
* [5.2 Installer requirements](#5.2)
* [5.3 Descriptor file definition](#5.3)

<a name="5.1"></a>
## 5.1 Introduction

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference implementation and implemented by installer. The same applies to _must not_.

**should**: Requirements that are marked as _should_ are expected to be fulfilled by the reference implementation but it is up to each installer to accept an implementation targeting this reference implementation that is not reflecting on any of those requirements. The same applies to _should not_.

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

<a name="5.2"></a>
## 5.2 Installer requirements
<a name="5.2.1"></a>
### 5.2.1 General
The Descriptor File defines the unique configuration required by installer in a common schema. 
It would specialize the installer type per user's implementation requirements.
It would be validated at the very beginning of the deployment.
It's installer's responsibility to translate the descriptor file to adapt with its own configuration. 
Thanks to the descriptor file, the NFVi infrastructure deployment could be completed in one step run.

| Ref # | sub-category | Description |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.gen.ins.01` | Installer | Installer **should** accept a descriptor file to finish deployment.|
| `req.gen.ins.02` | Installer | Installer implementation **must** validate the descriptor file with schema.|
| `req.gen.ins.03` | Installer | Any existing installer implementation **may** need adaption for the descriptor file. |
| `req.gen.ins.04` | Installer | Installer **may** support reporting the deployment progress status.|
| `req.gen.des.01` | Descriptor | Descriptor file **should** include hardware resource configuration, software configuration.|
| `req.gen.des.02` | Descriptor | Descriptor file **may** include additional extending configuration.|
<p align="center"><b>Table 5-2-1:</b> Installer requirements </p>

<a name="5.2.2"></a>
### 5.2.2 Additional
Depends xxx.

<a name="5.3"></a>
## 5.3 Descriptor definition
There should be a Descriptor File definition, which used by installer as input of necessary configuration.
Mandatory and optional definition should be defined.
 
<a name="5.3.1"></a>
### 5.3.1 Hardware resource information
The support of different workload types, each with different compute, storage, network requirements which needs kinds of hardware configuration template, we name this as server template.
Besides it may include optional information such area name, data center name etc.

| Field # | type | mandatory | Instruction |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| area_name | String | Yes | data center area name |
| area_center_name | String | Yes | data center name, may compliance with a naming rule.  |
| room_name | String | Yes | rome static data, helpful in locating issue occurred. |
| city | String | Yes |  |
| resource_pool_name | String | Yes |  |
| outband_network_segment | String | Yes |  |
| server_templates | List | Yes |  |
| server_infos | List | Yes |  |

<p align="center"><b>Table 5-3-1:</b> Hardware resource description.</p>

### 5.3.2 Server template
The server template describes the capability of the host like processor, memory, harddrive, raid, NIC/NIC binding, manufacturer, model etc.
Server template would be assigned to multiple servers, i.e physicalhosts.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| template_name | String | Yes |  |
| manufacturer | String | Yes |  |
| model | String | Yes |  |
| processor | String | Yes |  |
| memory | String | Yes |  |
| hard_drive | String | Yes |  |
| raid | String | Yes |  |
| network_controller_infos | List | Yes |  |
| network_card_bond_infos | List | Yes |  |

<p align="center"><b>Table 5-3-2:</b> Server template.</p>

### 5.3.3 Server information
Server will reference a server template, i.e, inherting all configuration of server template,
Besides it may include additional information pim username, password, rack_name,position etc.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| template_name | String | Yes | template referenced |
| device_name | String | Yes | e.g NFV-D-HDBNJ-02A-3503-G-02-M-SRV-01 |
| outband_ip | String | Yes |  |
| outband_subnet_mask | String | Yes |  |
| pim_username | String | Yes |  |
| pim_password | String | Yes |  |
| rack_name | String | Yes |  |
| position | String | Yes |  |
| network_controller_infos | List | Yes |  |

<p align="center"><b>Table 5-3-3:</b> Server information.</p>


### 5.3.4 Software configuration definition
It includes Virtualized Infrastructure Manager configurations,

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vim_name | String | Yes | vim name |
| vim_id | String | No | a name VIM Resource pool naming rule |
| vendor | String | Yes | VIM Provider information, e.g. ZTE,Huawei,Ericsson,NOKIA|
| version | String | Yes | e.g NFV-D-HDBNJ-02A-3503-G-02-M-SRV-01 |
| ip_version | String | Yes | Ipaddress type: IPV6 or IPV4 |
| az_info | List | Yes | list of availability zone name designed for this VIM |
| ha_name | List | No | HA name  if provided|
| network_infos | List | Yes | List of NICs used in VIM deployment |
| controller_nodes | List | Yes | List of controllers designed in VIM deployment |
| compute_nodes | List | Yes | List of compute nodes designed in VIM deployment |

<p align="center"><b>Table 5-3-4:</b> Software configuration.</p>


### 5.3.5 Network informations
List of All designed NIC definitions which are referenced by various roles of node, control/compute/network/storage node.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| network_plane_type | String | Yes | distinguish network type: e.g MANAGEMENT,STORAGEDATA |
| usage | String | Yes | used for compute/control: value is one of [manage,storage,service], for distribute storage  value if one of [storage_front,storage_backend] |
| network_plane_infos | List | Yes | vlan_id,sub_network(CIDR),gateway(could be null)|

<p align="center"><b>Table 5-3-5:</b> Network information.</p>



### 5.3.6 Controller informations
List of controller nodes that designed for current VIM deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | must be the device_name defined in server_information(###5.3.3), which would be set on Server from BMC|
| node_name | String | Yes | node name for the controller to deploy, e.g: controller01 |
| az_name | String | Yes | availability zone name which this node belongs to |
| ha_name | List | Yes | HA name which this node assigned to, could be more than one HA it belongs.|
| manage_vlan_id | String | Yes | may multiple vlan_id for management plane. Setting the dedicated vlan id assigned.|
| storage_vlan_id | String | Yes | may multiple vlan_id for storage plane. Setting the dedicated vlan id assigned.|

<p align="center"><b>Table 5-3-6:</b> Controller information.</p>

### 5.3.7 Compute informations
List of compute nodes that designed for current VIM deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | must be the device_name defined in server_information(###5.3.3), which would be set on Server from BMC|
| node_name | String | Yes | node name for the compute to deploy, e.g: compute01 |
| az_name | String | Yes | availability zone name which this node belongs to |
| ha_name | List | Yes | HA name which this node assigned to, could be more than one HA it belongs.|
| manage_vlan_id | String | Yes | may multiple vlan_id for management plane. Setting the dedicated vlan id assigned.|
| storage_vlan_id | String | Yes | may multiple vlan_id for storage plane. Setting the dedicated vlan id assigned.|
| vnic_type | String | Yes | VIM verification needs know compute node type: OVS,DPDK_OVS or SR-IOV node.|
| os_reserved_cores | String | No | Designed and planned by provider itself, may be none|
| ovs_reserved_cores | String | No | Designed and planned by provider itself, may be none |

<p align="center"><b>Table 5-3-7:</b> Compute information.</p>

### 5.3.8 Distributed storage informations
List of compute nodes that designed for current VIM deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cluster_infos | List | Yes | a list of cluster information|
<p align="center"><b>Table 5-3-8-1:</b> Storage information.</p>

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cluster_name | String | Yes | indicate the cluster name|
| ceph_iscsi_gateway | String | Yes | splitted by semicolon if more than one. e.g 2409:8086:8412:10a::1;2409:8086:8412:10a::2|
| ceph_manage_plane_address_segment | String | Yes | The address segment of ceph management plane. e.g 2409:8086:8412:100::/64|
| ceph_storage_plane_address_segment | String | Yes | The address segment of ceph storage plane. e.g 2409:8086:8412:100::/64|
| ceph_os_user | String | Yes | the user of ceph OS. |
| ceph_os_password | String | Yes | the user's password of ceph OS. |
| ceph_manage_plane_float_ip | String | Yes |  |
| ceph_network_manage_plane_float_ip | String | Yes |  |
| zms_network_manage_admin_password | String | Yes |  |
| ceph_device_name | String | Yes |  |
| ceph_iscsi_device_name | String | Yes |  |
| glance_pool_name | String | Yes |  |
| nova_pool_name | String | Yes |  |
| belong_to_az_one | String | Yes |  |
| cinder_infos | List | Yes |a list of cinder infos which are cinder pool name and backend info |

<p align="center"><b>Table 5-3-8-2:</b> Cluster information.</p>

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cinder_pool_name | String | Yes | cinder pool name|
| cinder_backend_name | String | Yes | backend name cinder connected|
<p align="center"><b>Table 5-3-8-3:</b> Cinder information.</p>

### 5.3.9 NTP server informations
primary and backup NTP server information.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| master_server_ip | String | Yes | |
| master_server_timezone | String | Yes | |
| backup_server_ip | String | No | |
| backup_server_timezone | String | No | |

<p align="center"><b>Table 5-3-9:</b> NTP server information.</p>

### 5.3.10 DNS server informations
DNS server informmation if VIM deployment requires.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| external_dns_network | String | No | DNS information if VIM deployment needed. |
| external_dns_ip | String | No | |

<p align="center"><b>Table 5-3-7:</b> DNS server information.</p>

### 5.3.10 Deployment host informations
Deployment host setting, which should have the access for the openstack nodes network.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ip_address | String | No | Ip address of debug PC |
| mask | String | No | mask of debug PC|
| gateway | String | No |gateway of debug PC |

<p align="center"><b>Table 5-3-7:</b> Deployment pc information.</p>

### 5.3.11 Deployment control informations
Used to control if VIM will be automatically deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auto_deploy | String | Yes | Flag of enabling or disabling automatically deploy VIM. |

<p align="center"><b>Table 5-3-7:</b> Auto deployment control information.</p>