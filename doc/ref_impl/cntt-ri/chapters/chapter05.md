[<< Back](../)

# 5. Installer Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 Introduction](#5.1)
* [5.2 Installer requirements](#5.2)
   * [5.2.1 General](#5.2.1)
   * [5.2.2 Additional](#5.2.2)
* [5.3 Descriptor file definition](#5.3)
   * [5.3.1 Hardware resource information](#5.3.1)
   * [5.3.2 Server template](#5.3.2)
   * [5.3.3 Server information](#5.3.3)
   * [5.3.4 Software configuration definition](#5.3.4)
   * [5.3.5 Network information](#5.3.5)
   * [5.3.6 Controller information](#5.3.6)
   * [5.3.7 Compute information](#5.3.7)
   * [5.3.8 Distributed storage information](#5.3.8)
   * [5.3.9 NTP server information](#5.3.9)
   * [5.3.10 DNS server information](#5.3.10)
   * [5.3.11 Deployment host information](#5.3.11)
   * [5.3.12 Deployment control information](#5.3.12)
   * [5.3.13 Proxy information](#5.3.13)   

<a name="5.1"></a>
## 5.1 Introduction

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference implementation and implemented by installer. The same applies to _must not_.

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

<a name="5.2"></a>
## 5.2 Installer requirements

<a name="5.2.1"></a>
### 5.2.1 General
The Descriptor File defines the unique configuration required by installer in a common schema. 
It would specialize the installer type per user's implementation requirements.
It would be validated at the very beginning of the deployment.
It's the installer's responsibility to translate the descriptor file to adapt with its own configuration. 
Thanks to the descriptor file, the NFVi infrastructure deployment could be completed in one step run.

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.gen.ins.01` | Installer | Installer **must** accept a descriptor file to finish deployment.|
| `req.gen.ins.02` | Installer | Installer implementation **must** validate the descriptor file with schema.|
| `req.gen.ins.03` | Installer | Any existing installer implementation **may** need adaption for the descriptor file. |
| `req.gen.ins.04` | Installer | Installer **may** support reporting the deployment progress status.|
| `req.gen.des.01` | Descriptor | Descriptor file **must** include hardware resource configuration, software configuration.|
| `req.gen.des.02` | Descriptor | Descriptor file **may** include additional extending configuration.|
<p align="center"><b>Table 5-2-1:</b> Installer requirements </p>

<a name="5.2.2"></a>
### 5.2.2 Additional
Depends xxx.

<a name="5.3"></a>
## 5.3 Descriptor file definition
There must be a Descriptor File definition, which used by installer as input of necessary configuration.
Mandatory and optional definition shall be defined.
 
<a name="5.3.1"></a>
### 5.3.1 Hardware resource information
The support of different workload types, each with different compute, storage, network requirements which needs kinds of hardware configuration template, we name this as server template.
Besides it may include optional information such area name, data center name etc.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| area_name | String | Yes | data center area name |
| area_center_name | String | Yes | data center name, may compliance with a naming rule.  |
| room_name | String | Yes | rome static data, helpful in locating issue occurred. |
| city | String | Yes |  |
| resource_pool_name | String | Yes |  |
| outband_network_segment | String | Yes |  |
| server_templates | List | Yes | server template list included in the resource pool |
| server_infos | List | Yes | server information list included in the resource pool |

<p align="center"><b>Table 5-3-1:</b> Hardware resource description.</p>

<a name="5.3.2"></a>
### 5.3.2 Server template
The server template describes the capability of the host like processor, memory, harddrive, raid, NIC/NIC binding, manufacturer, model etc.
Server template would be assigned to multiple servers, i.e physical hosts.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| template_name | String | Yes | template name will referenced by dedicated server |
| manufacturer | String | Yes |  |
| model | String | Yes |  |
| processor | String | Yes |  |
| memory | String | Yes |  |
| hard_drive | String | Yes |  |
| raid | String | Yes |  |
| network_card_infos | List | No | interface list definition|
| network_card_bond_infos | List | No | NIC bonding, might not be always the case.|

<p align="center"><b>Table 5-3-2-1:</b> Server template.</p>

This is the network interface definition. Generally, there are a list of interfaces included in server template.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port_name | String | Yes | port name, e.g ens0,ens1 |

<p align="center"><b>Table 5-3-2-2:</b> Network Card Bond information.</p>

In some case, interface would be bonded together. This is the network interface bond definition.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bond_name | String | Yes | new bonded name. e.g bond 0 is the new name after bond eno0,eno1.|
| bond_type | String | Yes | dvs,sr-iov,ovs |
| bond_mode | String | Yes | balance-tcp,balance-slb,balance-backup |
| bond_members | String | Yes | members of interface name to bond in together, e.g eno0,eno1. |

<p align="center"><b>Table 5-3-2-3:</b> Network Card Bond information.</p>

<a name="5.3.3"></a>
### 5.3.3 Server information
Server will reference a server template, i.e, inherting all configuration of server template,
Besides it may include additional information pim username, password, rack_name,position etc.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| template_name | String | Yes | template referenced |
| device_name | String | Yes | e.g NFV-D-HDBNJ-02A-3503-G-02-M-SRV-01 |
| system_diskname | String | No | system disk name |
| system_disksize | String | No | system disk size |
| pim_ip_address | String | Yes | PIM ip address |
| pim_netmask | String | Yes | PIM netmask |
| pim_username | String | Yes | PIM user |
| pim_password | String | Yes | PIM password |
| hugepage_number | String | No | huge page quantity |
| rack_name | String | Yes |  |
| position | String | Yes |  |
| remote_management_ip | String | Yes | remote management ip, e.g. iLO,iDRAC, BMC |
| remote_user | String | Yes | remote user  |
| remote_password | String | Yes | remote password |
| nic_info | List | Yes | network interface information |

<p align="center"><b>Table 5-3-3:</b> Server information.</p>

<a name="5.3.4"></a>
### 5.3.4 Software configuration definition
It includes Virtualized Infrastructure Manager configurations,

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vim_name | String | Yes | vim name |
| vim_id | String | No | a name VIM Resource pool naming rule |
| vendor | String | Yes | VIM Provider information, e.g. ZTE,Huawei,Ericsson,NOKIA|
| version | String | Yes | e.g NFV-D-HDBNJ-02A-3503-G-02-M-SRV-01 |
| ip_version | String | Yes | Ipaddress type: IPV6 or IPV4 |
| time_zone | String | Yes | timezone settings, e.g GMT+08:00 Asia/Shanghai |
| controller_nodes | List | Yes | List of controllers designed in VIM deployment |
| compute_nodes | List | Yes | List of compute nodes designed in VIM deployment |

<p align="center"><b>Table 5-3-4:</b> Software configuration.</p>

<a name="5.3.5"></a>
### 5.3.5 Network information
List of NIC definitions which are referenced by various roles of node, control/compute/network/storage node.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | device name which the network interface belongs to |
| ip_address | String | Yes | ip address |
| sub_network | String | Yes | subnet in CIDR format. e.g: 2409:8086:8412:100::/64|
| gateway | String | No | gateway|
| vlan_id | String | Yes | vlan id for current network |
| network_plane_type | String | Yes | distinguish network type: e.g MANAGEMENT,STORAGEDATA,COMPUTE |

<p align="center"><b>Table 5-3-5:</b> Network information.</p>

<a name="5.3.6"></a>
### 5.3.6 Controller information
List of controller nodes that designed for current VIM deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | must be the device_name defined in server_information(###5.3.3), which would be set on Server from BMC|
| node_name | String | Yes | node name for the controller to deploy, e.g: controller01 |

<p align="center"><b>Table 5-3-6:</b> Controller information.</p>

<a name="5.3.7"></a>
### 5.3.7 Compute information
List of compute nodes that designed for current VIM deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | must be the device_name defined in server_information(###5.3.3), which would be set on Server from BMC|
| node_name | String | Yes | node name for the compute to deploy, e.g: compute01 |
| az_name | String | Yes | availability zone name which this node belongs to |
| ha_name | List | Yes | HA name(s) which this node assigned to.|
| vnic_type | String | Yes | VIM verification needs know compute node type: OVS,DPDK_OVS or SR-IOV node.|
| os_reserved_cores | String | No | Designed and planned by provider itself, may be none|
| ovs_reserved_cores | String | No | Designed and planned by provider itself, may be none |

<p align="center"><b>Table 5-3-7:</b> Compute information.</p>

<a name="5.3.8"></a>
### 5.3.8 Distributed storage information
List of storage nodes that designed for current VIM deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cluster_name | String | Yes | cluster name|
| device_infos | List | Yes | a list of device|
<p align="center"><b>Table 5-3-8-1:</b> Cluster information.</p>


| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | indicate the device name|
| storage_type | String | Yes | Ceph/HDFS/Swift/GFS/Luster, etc |
| storage_os_user | String | No | storage os user|
| storage_os_password | String | No | storage os password|
| storage_network_address | String | Yes | storage access address|
| storage_network_mask | String | Yes | mask for the network|
| az_name | String | Yes | availabile zone which belongs to |
| additional_attributes | List | Yes | specific attribute(key value pairs) list, decided by the storage_type. e.g: For example, Ceph would specific storage pool name, while HDFS would need replication options |

<p align="center"><b>Table 5-3-8-2:</b> Storage device information.</p>

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attribute_name | String | Yes | specific attribute name required by the storage type |
| attribute_value | String | Yes | attribute value |
<p align="center"><b>Table 5-3-8-3:</b> Additional storage attribute.</p>


<a name="5.3.9"></a>
### 5.3.9 NTP server information
primary and backup NTP server information.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| master_server_ip | String | Yes | |
| master_server_timezone | String | Yes | |
| backup_server_ip | String | No | |
| backup_server_timezone | String | No | |

<p align="center"><b>Table 5-3-9:</b> NTP server information.</p>

<a name="5.3.10"></a>
### 5.3.10 DNS server information
DNS server informmation if VIM deployment requires.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dns_network | String | No | DNS information if VIM deployment needed. |
| dns_ip | String | No | |

<p align="center"><b>Table 5-3-10:</b> DNS server information.</p>

<a name="5.3.11"></a>
### 5.3.11 Deployment host information
Deployment host setting, which must have the access for the openstack nodes network.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ip_address | String | No | Ip address of debug host |
| mask | String | No | mask of debug host|
| gateway | String | No |gateway of debug host |

<p align="center"><b>Table 5-3-11:</b> Deployment host information.</p>

<a name="5.3.12"></a>
### 5.3.12 Deployment control information
Used to control if VIM will be automatically deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auto_deploy | String | Yes | Flag of enabling or disabling automatically deploy VIM. |

<p align="center"><b>Table 5-3-12:</b> Auto deployment control information.</p>

<a name="5.3.13"></a>
### 5.3.13 Proxy information
Proxy information, this section could be empty if not needed.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| proxyAddress | String | Yes | Proxy address |
| port | String | Yes | port |
| user | String | Yes | user |
| password | String | Yes | password |

<p align="center"><b>Table 5-3-13:</b> Proxy information.</p>
