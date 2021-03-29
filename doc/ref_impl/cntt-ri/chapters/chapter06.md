[<< Back](../)

# 6. Installer Requirements
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 Installer requirements](#6.2)
   * [6.2.1 General](#6.2.1)
   * [6.2.2 Additional](#6.2.2)
* [6.3 Descriptor file definition](#6.3)
   * [6.3.1 Resource Pool information](#6.3.1)
   * [6.3.2 Global Settings](#6.3.2)
   * [6.3.3 Parameters for network virtualization](#6.3.3)
   * [6.3.4 Server information](#6.3.4)
   * [6.3.5 Network Device information](#6.3.5)
   * [6.3.6 Port mapping information](#6.3.6)
   * [6.3.7 Network planning information](#6.3.7)
   * [6.3.8 TOR VLAN configuration information](#6.3.8)
   * [6.3.9 TOR VLAN configuration information](#6.3.9)
   * [6.3.10 Host Aggregate information](#6.3.10)
   * [6.3.11 VIM Nodes](#6.3.11)
   * [6.3.12 SDNC Nodes](#6.3.12)
   * [6.3.13 Storage cluster information](#6.3.13)
   * [6.3.14 Software integration information](#6.3.14)
   * [6.3.15 Device Management information](#6.3.15)

* [6.4 Installer prerequisite ](#6.4)
   * [6.4.1 Hardware validation ](#6.4.1)
   * [6.4.2 Network configuration ](#6.4.2)

<a name="6.1"></a>
## 6.1 Introduction

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference implementation and implemented by installer. The same applies to _must not_.

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

<a name="6.2"></a>
## 6.2 Installer requirements 

<a name="6.2.1"></a>
### 6.2.1 General
The Descriptor File defines the unique configuration required by installer in a common schema.
It would specialize the installer type per user's implementation requirements.
It would be validated at the very beginning of the deployment.
It's the installer's responsibility to translate the descriptor file to adapt with its own configuration.
Thanks to the descriptor file, the NFVi infrastructure deployment could be completed in one step run.

| Ref #            | sub-category | Description                                                                              |
|------------------|--------------|------------------------------------------------------------------------------------------|
| `req.gen.ins.01` | Installer    | Installer **may** accept a descriptor file to finish deployment.                        |
| `req.gen.ins.02` | Installer    | Installer implementation **must** validate the descriptor file with schema.              |
| `req.gen.ins.03` | Installer    | Any existing installer implementation **may** need adaption for the descriptor file.     |
| `req.gen.ins.04` | Installer    | Installer **may** support reporting the deployment progress status.                      |
| `req.gen.des.01` | Descriptor   | Descriptor file **must** include hardware resource configuration, software configuration.|
| `req.gen.des.02` | Descriptor   | Descriptor file **may** include additional extending configuration.                      |

<p align="center"><b>Table 6-2-1:</b> Installer requirements </p>

<a name="6.2.2"></a>
### 6.2.2 Additional
Depends xxx.

<a name="6.3"></a>
## 6.3 Descriptor file definition specification
There must be a Descriptor File definition, which used by installer as input of necessary configuration.
Mandatory and optional definition shall be defined.  
All the required definition for description file is listed in this specification session, there's no restrictions on how to use it,
there could be multiple ways to implement PDF, the implementation will be in next session

<a name="6.3.1"></a>
### 6.3.1 Resource Pool information
This table is the description of the resource pool, it contains only 2 parameters: name and type of the resource pool.

Only one instance per resource pool.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RES_POOL_NAME | String | Yes | This is the unique name of the resource pool, could be refered by other parameters |
| RES_POOL_TYPE | String | Yes | User defined value to identify different hardware or software configuration requirements. |

<p align="center"><b>Table 6-3-1:</b> Resource Pool Information.</p>


<a name="6.3.2"></a>
### 6.3.2 Global Settings
The Global settings are provided by the user, contains data like like IP_Type, VLAN_Type, etc.

Only one instance per resource pool.
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IP_TYPE | String | Yes | IPV4 or IPV6 |
| NETWORK_TYPE | String | Yes | VLAN or VXLAN  |
| TIMEZONE | String | Yes | The timezone where VIM deployed, like UTC+8  |
| STORAGE_TYPE | String | Yes |  The Storage type, for example "ceph" |
| HUGEPAGE_ENABLE | String | Yes | TRUE or FALSE  |
| HUGEPAGE_SIZE | String | Yes | The storage size that hypervisor set for VM, for example "1GB" |
| QINQ_ENABLE | List | Yes | TRUE or FALSE |
| HYPERVISOR_CORES | List | Yes | number of CPU bounded for Hypervisor |
| EXTERNAL_NTP_SERVER_IP | List | Yes | IP list of NTP server, seperated by comma, for example: primariy_IP;second_IP |

<p align="center"><b>Table 6-3-2:</b> Global Settings </p>


<a name="6.3.3"></a>
### 6.3.3 Parameters for network virtualization
MTU value for network virtualization should be defined, this is usually standard value that defined by user.

3 instances are expected for Manage Service and storage,  they may have different MTU requirement.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NIC_PORT_TYPE | String | Yes | Type for nic port, Manage, Service or Storage |
| MTU | String | Yes | This describes the row where rack located |

<p align="center"><b>Table 6-3-3:</b> Network Virtualization parameter .</p>


<a name="6.3.4"></a>
### 6.3.4 server information
Server information should be provided for installer, including full detail info. for each server, nic mapping etc.

#### 6.3.4.1 server information
First, a table describes the information for each server in the resource pool should be provided.

Multiple instances are expected, one instance for each server.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME | String | Yes | Server name should be aligned with naming rule, this is the unique ID for each device to be referred for identify device |
| VENDOR | String | Yes | Vendor of device |
| SKU | String | Yes | The SKU of device, can be referred by other table NIC connection table, to identify slot-port mapping for device  |
| MODEL | String | Yes | This is the model for different service type, this value is defined from design document of resource pool, example NC1, NC1-S |
| SN | String | Yes | Serial Number |
| RES_POOL | String | Yes | Resource pool name |
| RACK | String | Yes | rack name where device located |
| POS | String | Yes | the position of device in rack, like 2-3U,4-5U |
| BMC_IP | String | Yes |  |
| BMC_GATEWAY | String | Yes |  |
| BMC_MASK | String | Yes |  |
| BMC_SUBNET | String | Yes |  |
| BMC_USR | String | Yes | BMC user |
| BMC_PWD | String | Yes | BMC password |
| INTERNAL_IP | String | Yes | It is an internal IP  configured and used by hardware integration tools, it will be removed after hardware integration verification |
| INTERNAL_GATEWAY | String | Yes |  |
| INTERNAL_MASK | String | Yes |  |
| GROUP_NAME | String | Yes | the usage of server, Manage or Storaage or Service  |
| BMC_PRE_CONFIGURED | String | Yes | YES or NO |
| HW_REGION | String | Yes | hardware region that divided by design documents, like A area or B area |
| MODULE_NAME | String | Yes | hardware model that divided within each region, Like "Model 3 in Region A", usually contains certain number of racks |

<p align="center"><b>Table 6-3-4-1:</b> Server Information.</p>

#### 6.3.4.2 server nic information
This table is describing the slot and port mapping relationship for NIC in each model of server. 

Multiple entries are expected, one entry for each slot of each type of server, so, multiple entries for each type of server, and there's maybe multiple types of server.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VENDOR | String | Yes | Vendor of server |
| SKU | String | Yes | SKU of server |
| MODEL | String | Yes | server service type defined by provider/user, same definition as in above table, example: NC1 or NC2  |
| SLOT | String | Yes | Slot number in server for each NIC, for example, PCIeSlot2  |
| PORTS | String | Yes | Ports number for the above NIC, for example: 1_1;1_2 2 ports for one NIC  |
| SLOT | String | Yes | Slot number in server for each NIC, for example, PCIeSlot2  |

<p align="center"><b>Table 6-3-4-2:</b> Server NIC Information.</p>

#### 6.3.4.3 Port BDF information for each type pf server
Port BDF information need to be provided for each port on server, 
it will be used to identify the logical port name after OS is installed. 

Multiple entries are expected, 1 instance for each port, BDF info for all server SKU should be included.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SKU | String | Yes | SKU of server |
| MODEL | String | Yes | server service type defined by provider/user, same definition as in above table, example: NC1 or NC2  |
| NETWORK_PLANE | String | Yes | Network plane for each nic, Manage or Storage or Service  |
| PORT | String | Yes | Ports number for example: 1_1  |
| PORT_BDF | String | Yes | Port BDF value for above port  |

<p align="center"><b>Table 6-3-4-3:</b> Port BDF Information.</p>

<a name="6.3.5"></a>
### 6.3.5 Network Device information
This table describes each network device, it can be used for network configuration and verification.

Multiple instances are expected, one instance for each network device.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME | String | Yes | Name of network device |
| VENDOR | String | Yes | Vendor name for network device  |
| SKU | String | Yes | SKU |
| MODEL | String | Yes | Type of switch, like TOR or EOR |
| SN | String | Yes | Serial number |
| HW_RES_POOL | String | Yes | Resource pool name for hardware |
| RACK | List | Yes | rack number where switch is placed |
| POS | List | Yes | position in rack |
| BMC_IP | List | Yes |  |
| BMC_GATEWAY | List | Yes |  |
| BMC_MASK | List | Yes |  |
| BMC_USR | List | Yes | BMC login user |
| BMC_PWD | List | Yes | password for BMC login user |
| ENABLE_PWD | List | Yes | Enable password |
| GROUP_NAME | List | Yes | Manage or storage or service |
| HW_REGION | List | Yes | Hardware region |
| MODULE_NAME | List | Yes | Hardware module which is devided by location, like area A module 1 |

<p align="center"><b>Table 6-3-5:</b> Network device information.</p>


<a name="6.3.6"></a>
### 6.3.6 Port mapping information
Wiremap defines the port mapping between server/switch and switch for each line, 
we will need this information to trace the connected server and port, so we can extrapolate the required network configuration for the port.

Multiple instances are expected, one instance for each physical cable.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME | String | Yes | Name of network device |
| LOCAL_RACK | String | Yes | the rack info for local device   |
| LOCAL_NAME | String | Yes | local device name |
| LOCAL_TYPE | String | Yes | Local device type, switch or server |
| LOCAL_PORT | String | Yes | connected port in local device |
| REMOTE_RACK | String | Yes |  |
| REMOTE_NAME | List | Yes | connected remote device name |
| REMOTE_TYPE | List | Yes | remote device type |
| REMOTE_PORT | List | Yes | connected port in remote device  |
| LINE_TYPE | List | Yes | line type to describe local device type and remote device type |

<p align="center"><b>Table 6-3-6:</b> Port mapping information.</p>


<a name="6.3.7"></a>
### 6.3.7 Network planning information
Network planning info for resource pool needs to be defined, which should include Vlan ID, allocated IP range, the applied node set.

Multiple instances are expected, one instance for each network plane.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APPLICATION_LAYER | String | Yes |   |
| DOMAIN | String | Yes |  |
| VENDOR_NETWORK_PLANE | String | Yes |  |
| NETWORK_PLANE | String | Yes |  |
| VENDOR | String | Yes |  |
| VLAN_ID | List | Yes |  |
| IP_SEGMENT | List | Yes |  |
| GATEWAY | List | Yes |  |
| SWITCH_CONFIG_TYPE | List | Yes |   |

<p align="center"><b>Table 6-3-7:</b> Network planning information.</p>


<a name="6.3.8"></a>
### 6.3.8 TOR VLAN configuration information
Multiple instances are expected, one instance for each TOR. 

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEVICE_NAME | String | Yes |   |
| VENDOR | String | Yes |  |
| DEVICE_MODEL | String | Yes |  |
| DEVICE_SN | String | Yes |  |
| BMC_IP | String | Yes |  |
| SSH_USER | List | Yes |  |
| SSH_PASSWORD | List | Yes |  |
| ENABLE_PASSWORD | List | Yes |  |
| PORT | List | Yes |  group multiple ports with same VLAN configuration, and separate different port group with ";" |
| VLAN_TYPE | List | Yes | tag or untag |
| VLAN_ID | List | Yes |  group multiple VLAN with same configuration requirements, and separate different VLAN group with ";" |
| PORT_TYPE | List | Yes | trunk or access or hybrid  |

<p align="center"><b>Table 6-3-8:</b> TOR VLAN information.</p>


<a name="6.3.9"></a>
### 6.3.9 EOR VLAN configuration information
Multiple instances are expected, one instance for each EOR. 

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEVICE_NAME | String | Yes |   |
| VENDOR | String | Yes |  |
| DEVICE_MODEL | String | Yes |  |
| DEVICE_SN | String | Yes |  |
| BMC_IP | String | Yes |  |
| SSH_USER | List | Yes |  |
| SSH_PASSWORD | List | Yes |  |
| ENABLE_PASSWORD | List | Yes |  |
| PORT | List | Yes |   group a list of ports with same VLAN configuration, and separate different port group with ";" |
| VLAN_ID | List | Yes |  group multiple VLAN with same configuration requirements, and separate different VLAN group with ";" |
| VLANIF_ADDRESS | List | Yes |   |
| NETWORK_MASK | List | Yes |   |

<p align="center"><b>Table 6-3-9:</b> EOR VLAN information.</p>


<a name="6.3.10"></a>
### 6.3.10 Host Aggregate
Servers in the resource pool are divided to multiple HAs according to the difference from service or different hardware requirements.  
One HA could belong to multiple AZ   
It is the definition of each HA in the resource pool. it should contain the server list for each HA, and also the HA meta data.

####  6.3.10.1 Host HA Mapping 
Multiple instances are expected, defines all servers in HA
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HA_NAME | String | Yes |  |
| DEVICE_NAME | String | Yes | server name list in HA |

<p align="center"><b>Table 6-3-10-1:</b> Host HA Information.</p>

#### 6.3.10.2 HA metadata 
Multiple instances are expected, service, management and DMZ.
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HA_NAME | String | Yes |  |
| HA_METADATA | String | Yes | properties for each HA, for example: type=TrustPlane,ovs=C-plane,sriov=false |
| AZ_NAME | String | Yes | AZ name that HA belongs to |

<p align="center"><b>Table 6-3-10-2:</b> HA meta Information.</p>

<a name="6.3.11"></a>
### 6.3.11 VIM Nodes
There's a list of servers that was defined as control/management nodes according to resource pool plan

Multiple instances are expected, defines all management servers.
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEVICE_NAME | String | Yes | The server name  |

<p align="center"><b>Table 6-3-11:</b> VIM Nodes Information.</p>

<a name="6.3.12"></a>
### 6.3.12 SDNC Nodes

Multiple instances are expected, defines all SDN controllers
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEVICE_NAME | String | Yes | The server name  |
<p align="center"><b>Table 6-3-12:</b> SDNC Nodes Information.</p>

<a name="6.3.13"></a>
### 6.3.13 Storage cluster information 
Definition of storage cluster and storage pool, 

#### 6.3.13.1 Storage pool plan
Storage pool name in each storage cluster, and nodes in Storage pool should be defined, so the storage installer will know which nodes are installing.

Multiple instances are expected, each instance defines one storage node
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STORAGE_CLUSTER_NAME | String | Yes |   |
| STORAGE_POOL_NAME | String | Yes |  |
| DEVICE_NAME | String | Yes |  |

<p align="center"><b>Table 6-3-13-1:</b> Storage Pool Plan </p>

#### 6.3.13.2 Distribution storage pool info
Storage pool information, defines the management account and network information

Multiple instances are expected, each instance defines one storage pool
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STORAGE_CLUSTER_NAME | String | Yes |   |
| NODE_POOL | String | Yes |  |
| DISK_POOL_NAME | String | Yes |  |
| STORAGE_POOL_NAME | String | Yes |  |
| HA_NAME_LIST | String | Yes |  |
| AZ_NAME | List | Yes |  |
| STORAGE_POOL_NODE_ACCOUNT | List | Yes |  |
| MAX_QUOTA_CAPACITY | List | Yes |  |
| STORAGE_POOL_MANAGEMENT_IP | List | Yes |   |
| NETWORK_MASK | List | Yes |   |
| GATEWAY | List | Yes |   |
| VIM_USER | List | Yes |   |
| VIM_PASSWORD | List | Yes |   |
| PIM_USER | List | Yes |   |
| PIM_PASSWORD | List | Yes |   |
| STORAGE_CLUSTER_SERVICE_IP | List | Yes |   |
| STORAGE_CLUSTER_SERVICE_GW | List | Yes |   |
| STORAGE_CLUSTER_BACKEND_IP | List | Yes |   |
| STORAGE_CLUSTER_BACKEND_GW | List | Yes |   |
| BACKUP_POLICY | List | Yes |   |

<p align="center"><b>Table 6-3-13-2:</b> Distribution storage pool info.</p>


<a name="6.3.14"></a>
### 6.3.14 Software integration information
After VIM and Storage software installation finished, parameters willl be needed in integration process of VIM and Storage,
the parameters should be defined in advance.

#### 6.3.14.1 VIM Context
Parameters from VIM vendor for integration.

Only one entry is expected.
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VENDOR | String | Yes |  |
| AUTHORIZATION | String | Yes | One-way or Two-way authentication |
| VIM_CERTIFICATES_PATH | String | Yes | Full path for certificates that used for integration |

<p align="center"><b>Table 6-3-14-1:</b> VIM context Information.</p>

#### 6.3.14.2 Storage Context
Parameters from storage vendor for integration.

Only one entry is expected.
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VENDOR | String | Yes |  |
| AUTHORIZATION | String | Yes | One-way or Two-way authentication |
| JOINT_WAY | String | Yes | by ISCSI or client |
| DRIVER_FULL_NAME | String | Yes | Full path for storage driver |
| CEPH_CONFIG_PATH | String | Yes | Full path for ceph.conf storage |
| IS_PIM_JOINT | String | Yes | whether integrate with PIM, usaually "YES" for this value |
| STORAGE_SOFTWARE_VERSION | String | Yes |  |

<p align="center"><b>Table 6-3-14-2:</b> Storage context Information.</p>

#### 6.3.14.3 Storage Client context
This table defines the parameters for integration with storage client

Multiple entries are expected, one entry for each authorization user.
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JOINT_WAY | String | Yes | integration method for storage client, for example, RBD  |
| COMPONENT_TYPE | String | Yes | for example: cinder, glance or nova |
| AUTHORIZATION_USER | String | Yes | match with the component type |
| KEYRING_FILENAME | String | Yes | Full path for keyring file, this should match the authentication user, |

<p align="center"><b>Table 6-3-14-3:</b> Storage client context.</p>

<a name="6.3.15"></a>
### 6.3.15 Device Management information

#### 6.3.15.1 SERVER PIM ACCOUNT
Servers are managed by redfish, credentials should be the same for same type of device  

Multiple entries are expected, one entry for each server model.
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VENDOR | String | Yes |  |
| SERVER_MODEL | String | Yes | MODEL for each type of server |
| REDFISH_USER | String | Yes |  |
| REDFISH_PASSWD | String | Yes |  |

<p align="center"><b>Table 6-3-15-1:</b> SERVER PIM ACCOUNT Information.</p>

#### 6.3.15.2 Switch PIM Account
Servers are managed by SNMP, credentials should be the same for same type of device  

Multiple entries are expected, one entry for each device model.
| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VENDOR | String | Yes |  |
| DEVICE_MODEL | String | Yes | MODEL for each type of switch |
| SNMP_VERSION | String | Yes | v3 by default |
| SNMP_USER | String | Yes |  |
| AUTHENTICATION_METHOD | String | Yes | for example: MD5 or SHA1 |
| VERIFICATION_CODE | String | Yes |  |
| ENCRYPTION_METHOD | String | Yes |  |
| ENCRYPTION_KEY | String | Yes |  |

<p align="center"><b>Table 6-3-15-2:</b> Switch PIM Account.</p>

*[·-·]:previous content are retained as backup, if the aboved 6.3.1 - 6.3.15 are reviewed and agreed, will delete redundant content in below and adjust accordingly.

<a name="6.3.1"></a>
### 6.3.1 Hardware resource information
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

<p align="center"><b>Table 6-3-1:</b> Hardware resource description.</p>

<a name="6.3.2"></a>
### 6.3.2 Server template
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

<p align="center"><b>Table 6-3-2-1:</b> Server template.</p>

This is the network interface definition. Generally, there are a list of interfaces included in server template.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port_name | String | Yes | port name, e.g ens0,ens1 |

<p align="center"><b>Table 6-3-2-2:</b> Network Card Bond information.</p>

In some case, interface would be bonded together. This is the network interface bond definition.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bond_name | String | Yes | new bonded name. e.g bond 0 is the new name after bond eno0,eno1.|
| bond_type | String | Yes | dvs,sr-iov,ovs |
| bond_mode | String | Yes | balance-tcp,balance-slb,balance-backup |
| bond_members | String | Yes | members of interface name to bond in together, e.g eno0,eno1. |

<p align="center"><b>Table 6-3-2-3:</b> Network Card Bond information.</p>

<a name="6.3.3"></a>
### 6.3.3 Server information
Server will reference a server template, i.e, inherting all configuration of server template,
Besides it may include additional information pim username, password, rack_name,position etc.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| template_name | String | Yes | template referenced |
| device_name | String | Yes | e.g NFV-D-HDBNJ-02A-3503-G-02-M-SRV-01 |
| system_diskname | String | No | system disk name |
| system_disksize | String | No | system disk size |
| role | String | No | computer,controller,storage |
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

<p align="center"><b>Table 6-3-3:</b> Server information.</p>

<a name="6.3.4"></a>
### 6.3.4 Software configuration definition
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

<p align="center"><b>Table 6-3-4:</b> Software configuration.</p>

<a name="6.3.5"></a>
### 6.3.5 Network information
List of NIC definitions which are referenced by various roles of node, control/compute/network/storage node.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | device name which the network interface belongs to |
| ip_address | String | Yes | ip address |
| sub_network | String | Yes | subnet in CIDR format. e.g: 2409:8086:8412:100::/64|
| gateway | String | No | gateway|
| vlan_id | String | Yes | vlan id for current network |
| network_plane_type | String | Yes | distinguish network type: e.g MANAGEMENT,STORAGEDATA,COMPUTE |

<p align="center"><b>Table 6-3-5:</b> Network information.</p>

<a name="6.3.6"></a>
### 6.3.6 Controller information
List of controller nodes that designed for current VIM deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | must be the device_name defined in server_information(###6.3.3), which would be set on Server from BMC|
| node_name | String | Yes | node name for the controller to deploy, e.g: controller01 |

<p align="center"><b>Table 6-3-6:</b> Controller information.</p>

<a name="6.3.7"></a>
### 6.3.7 Compute information
List of compute nodes that designed for current VIM deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| device_name | String | Yes | must be the device_name defined in server_information(###6.3.3), which would be set on Server from BMC|
| node_name | String | Yes | node name for the compute to deploy, e.g: compute01 |
| az_name | String | Yes | availability zone name which this node belongs to |
| ha_name | List | Yes | HA name(s) which this node assigned to.|
| vnic_type | String | Yes | VIM verification needs know compute node type: OVS,DPDK_OVS or SR-IOV node.|
| os_reserved_cores | String | No | Designed and planned by provider itself, may be none|
| ovs_reserved_cores | String | No | Designed and planned by provider itself, may be none |

<p align="center"><b>Table 6-3-7:</b> Compute information.</p>

<a name="6.3.8"></a>
### 6.3.8 Distributed storage information
List of storage nodes that designed for current VIM deployment.

| Field #      | type   | mandatory | Instruction      |
|--------------|--------|-----------|------------------|
| cluster_name | String | Yes       | cluster name     |
| device_infos | List   | Yes       | a list of device |

<p align="center"><b>Table 6-3-8-1:</b> Cluster information.</p>


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

<p align="center"><b>Table 6-3-8-2:</b> Storage device information.</p>

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attribute_name | String | Yes | specific attribute name required by the storage type |
| attribute_value | String | Yes | attribute value |
<p align="center"><b>Table 6-3-8-3:</b> Additional storage attribute.</p>


<a name="6.3.9"></a>
### 6.3.9 NTP server information
primary and backup NTP server information.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| master_server_ip | String | Yes | |
| master_server_timezone | String | Yes | |
| backup_server_ip | String | No | |
| backup_server_timezone | String | No | |

<p align="center"><b>Table 6-3-9:</b> NTP server information.</p>

<a name="6.3.10"></a>
### 6.3.10 DNS server information
DNS server informmation if VIM deployment requires.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dns_network | String | No | DNS information if VIM deployment needed. |
| dns_ip | String | No | |

<p align="center"><b>Table 6-3-10:</b> DNS server information.</p>

<a name="6.3.11"></a>
### 6.3.11 Deployment host information
Deployment host setting, which must have the access for the openstack nodes network.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ip_address | String | No | Ip address of debug host |
| mask | String | No | mask of debug host|
| gateway | String | No |gateway of debug host |

<p align="center"><b>Table 6-3-11:</b> Deployment host information.</p>

<a name="6.3.12"></a>
### 6.3.12 Deployment control information
Used to control if VIM will be automatically deployment.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auto_deploy | String | Yes | Flag of enabling or disabling automatically deploy VIM. |

<p align="center"><b>Table 6-3-12:</b> Auto deployment control information.</p>

<a name="6.3.13"></a>
### 6.3.13 Proxy information
Proxy information, this section could be empty if not needed.

| Field # | type | mandatory | Instruction |
|----|--------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| proxyAddress | String | Yes | Proxy address |
| port | String | Yes | port |
| user | String | Yes | user |
| password | String | Yes | password |

<p align="center"><b>Table 6-3-13:</b> Proxy information.</p>


<a name="6.4"></a>
## 6.4 Installer prerequisite

<a name="6.4.1"></a>
### 6.4.1 Hardware validation
Before the installation, the user has to check if each server meets the deployment requirements:
 - BIOS settings: RAID configuration, PXE boot order and boot mode, disk capacity, CPU, and memory settings,
 - remote management accessibility (for example, IPMI, iLO, BMC),
 - NIC quantity and configuration.

<a name="6.4.2"></a>
### 6.4.2 Network configuration
The necessary prerequisite settings must be ready before the deployment, for example:
 - the VLAN must be configured on the switch,
 - the IP address ranges to be used must be allocated.

<a name="6.5"></a>
## 6.5 PDF implementation
When we use PDF for installer or verification tools, all the required data described in 6.3 should be included.
There's no limitation on how to implement PDF, like the file type of PDF could be csv or json, 
and also you can adjust the file structure, whichever is more readable to the tools.
Taking servers information for example, you can use flat version to include all parameters in 6.3.4 for each device,
or you can group servers with same properties like same Vendor, same model, or same usage. 
You can refer anuket PDF pages for details about how to implement: https://wiki.anuket.io/pages/viewpage.action?pageId=4406598