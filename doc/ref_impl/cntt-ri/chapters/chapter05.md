[<< Back](../)

# 5. Hardware Delivery and Configuration Requirements
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 Introduction](#5.1)
* [5.2 Requirements](#5.2)
   * [5.2.1 General](#5.2.1)
   * [5.2.2 Check point](#5.2.2)
* [5.3 Descriptor file definition](#5.3)
   * [5.3.1 Resource pool](#5.3.1)
   * [5.3.2 NIC template](#5.3.2)
   * [5.3.3 Cabinet](#5.3.3)
   * [5.3.4 Server](#5.3.4)
   * [5.3.5 Network device](#5.3.5)
   * [5.3.6 EOR card](#5.3.6)
   * [5.3.7 Cabling](#5.3.7) 
* [5.4 Appendix](#5.4)
   * [5.4.1 HDV Original collection.](#5.4.1)
   
<a name="5.1"></a>
## 5.1 Introduction

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference implementation and implemented by installer. The same applies to _must not_.

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

<a name="5.2"></a>
## 5.2 Requirements
Before deployment of software, a set of hardware delivery and related parameter should be validated. 
Automated tool is also expected for checking if hardware settings match with the requirement for NFVi and VNF.
First release, focus on the "readable" hardware parameter, in future release, "writable" parameter might add also.
It's expected that a basic set of information should be prepared, for example, remote access configuration, IPMI ipaddress and credentials, or redfish interface.
Further more, in production case of large scale to check, those basic information can be automated from user defined rule.
All the check point should be configurable for the check tool.

<a name="5.2.1"></a>
### 5.2.1 General
A Descriptor File defines the configuration required by the checking tool in a common schema. 
This file can be used as the input of checking tool(let's call it "checker") to validate the hardware settings meeting the requirement.
Thanks to the descriptor file, user can validate if hardware matching requirement, and outcome the failure reason for invalid hardware.
The failure reason would guide user for the correctness and after then user can have another round of validation after that.
Hardware integration validation stage must happen before the software stack deployment. 

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.gen.chk.01` | Checker | Checker **must** accept a descriptor file to finish hardware delivery validation.|
| `req.gen.chk.02` | Checker | Checker **must** report the checking result of success or failure with reason.|
| `req.gen.chk.03` | Checker | Checker **may** accept the configurable checkpoint file as input |
| `req.gen.des.01` | Descriptor | Descriptor file **must** include neccessary information to remote access hardware resource|
| `req.gen.des.02` | Descriptor | Descriptor file **may** be automated to generated from a user defined rule, how to generate asset name, IP address, gateways, VLAN ID, etc|
<p align="center"><b>Table 5-2-1:</b> Check tool requirements </p>

<a name="5.2.2"></a>
### 5.2.2 Check point
There are many hardware check points which initially drafted at (#5.4.1)

| Test Type # | Purpose | Example | Check when |
|----|---------------|-----------|-----------|
| BIOS Settings | Verifies all applicable BIOS settings per hardware model.| Boot mode/Boot Sequence Retry/AC Power Recovery/Power Setting (balanced / performance)/Virt. Technology/Hyper Threading/Trusted platform module||
| Firmware Settings | Verifies all applicable Firmware settings.| BIOS/Storage Array Controller/NIC (e.g.Intel X710)/PXE Enabled Ports||
| Boot Order | Verifies applicable boot order settings.|First boot, Second boot.||
| Hardware Health | Queries Intelligent Platform Management Interface (IPMI) is for all hardware components and their health status.| Raid/System Board/CPU temp/Power Supply ||
| PCI Slot Status & MAC | Which cards are in which slot, which slot is assigned to which CPU, slot type | card(s) in slot/port/PCI partition /Slot speed / type / CPU / Slot assignment ||
| NIC | Validates that all NICs are in the correct slots, with a healthy status (per IPMI), have correct MAC addresses, and are detecting a cable connection (or not). |Correct LLDP neighbor MAC Addresses.||
| IPMI Logs | Check for existence of logs.| Physical event logged.  E.g. chassis open on power up.||
| IPMI Users | Check for existence of user accounts.| Check if IPMI is availabile,if IPMI account is existing, if IPMI default credentials.||
| Hardware Inventory | Inventory of h/w on platform.| CPU and count, NUMA topology, CPU Freq, RAM, speed, size, model, etc.||
| Physical Disk Configuration | Verifies storage / disk config (type, size)|Physical disk type, card/port location,capacity||
| SRIOV Port Validation | Verifies global and NIC level enabled.|Confirm setting is enabled (or none)||
| Hardware Check | Verifies basic OS config attributes (i.e. Linux running on the host and reporting these values).|RAM size/number of cores.||
<p align="center"><b>Table 5-2-2:</b> Hardware check point.</p>

<a name="5.3"></a>
## 5.3 Descriptor file definition
There must be a Descriptor File definition for the hardware validation, at beginning only focus-on readable parameter, after then extend on writable parameters in future release.
The entry information must be included in the description file , which are the remote access parameter settings。
 
<a name="5.3.1"></a>
### 5.3.1 Resource pool
Resource pool is the conception which a NFV resource is planned to build up. It consists hardware server device, network device and cabling among them.
It is referenced by other resource type to introduce later.

| Field # | type | mandatory | Instruction |
|----|--------------------|-----------------|-------------------------|
| serial_no | String | Yes |  |
| resource_pool_name | String | Yes | resource name, e.g: NFV-RP-HZZZ-03A_0 |
| type | String | Yes | TOCHECK: OTHER |

<p align="center"><b>Table 5-3-1:</b> Resource pool.</p>
 
<a name="5.3.2"></a>
### 5.3.2 NIC template
NIC Template defines network interface card parameters, it includes the crucial port number on the NIC, which is used as the reference in the cabling data and check.

| Field # | type | mandatory | Instruction |
|----|--------------------|-----------------|-------------------------|
| serial_no | String | Yes |  |
| vendor | String | Yes | vendor name: ZTE,HUAWEI |
| server_type | String | Yes | ZTE "R5300 G4", HUAWEI "TaiShan200-2280" |
| customized_model | String | No | customized model: C2,C21 |
| nic_vendor | String | Yes | nework interface card vendor: intel |
| nic_type | String | Yes | Intel "x520" |
| rootbdf | String | Yes | e.g "00:03:01:00" |
| slot_id | String | Yes | the slot id number of card plugged-in |
| connect_type | String | Yes | plugin |
| port_quantity | Number | Yes | port quantity on the card. e.g. 2 |
| port_bandwith | String | Yes | bandwith of port. e.g. 10G |
| cabling_ports | Number | Yes | port name used in the cabing data. corresponding the quantity e.g: 1_1;1_2 or Slot3/Port1;Slot3/Port2 |

<p align="center"><b>Table 5-3-2:</b> NIC template.</p>

<a name="5.3.3"></a>
### 5.3.3 Cabinet
Cabinet is the rack holder for the server and network devices. The data will be referenced by server and network device data.

| Field # | type | mandatory | Instruction |
|----|--------------------|-----------------|-------------------------|
| serial_no | String | Yes |  |
| room | String | Yes | room number, e.g: 2201 |
| column | String | Yes | column number in the room: e.g. "J" |
| cabinet | String | Yes | cabinet number in the column: e.g. "01" |

<p align="center"><b>Table 5-3-3:</b> Cabinet.</p>

<a name="5.3.4"></a>
### 5.3.4 Server
Server device data defines the key information about how to access the server remotely, i.e. remote ip, user, credentials.
Hardware validation consists of BMC validation, interface verifcation etc. 
Once the server have started up from PXE, in order to invoke remote interface(e.g. BMC) of the server from server OS.
inband ip address is temporally configured and used, the inband ip is connective with remote BMC ip.

| Field # | type | mandatory | Instruction |
|----|--------------------|-----------------|-------------------------|
| serial_no | String | Yes |  |
| server_name | String | Yes | server name, e.g: NFV-D-HZZZ-03A-2201-0J01-M-SRV-01 |
| vendor | String | Yes | vendor name "ZTE","HUAWEI" etc |
| server_type | String | Yes | ZTE "R5300 G4", HUAWEI "TaiShan200-2280" |
| customized_model | String | No | customized model: C2,C21 |
| server_sn | String | Yes | server serial number |
| resource_pool_name | String | Yes | resource pool name which belongs to |
| cabinet | String | Yes | cabinet which belongs to, in format room-column-cabinet, e.g. "2201-J-01" |
| position | String | Yes | the server position located in the cabinet.|
| remote_ip | String | Yes | BMC/iLO/IPMI ip for remote access, e.g "2409:8086:8313:81::1"|
| gateway | String | Yes | gateway of remote ip, e.g "2409:8086:8313:81::ffff"|
| outband_netmask | String | Yes | e.g. "64"|
| subnet | String | Yes | e.g. "2409:8086:8313:81"|
| remote_user | String | Yes | e.g. "Administrator"|
| remote_password | String | Yes | e.g. "password"|
| inband_ip | String | Yes | temporary inband_ip e.g "2409:8086:8313:f::24"|
| inband_gateway | String | Yes | gateway of inband ip, e.g "2409:8086:8313:f::ffff"|
| inband_netmask | String | Yes | e.g. "64"|
| group | String | Yes | network assignment "service/management/storage"|
| is_bmc_configured | String | Yes | TOCHECK|

<p align="center"><b>Table 5-3-4:</b> Server.</p>

<a name="5.3.5"></a>
### 5.3.5 Network device
network device data defines the key data about how to remote access the network device, such as switches and routers.

| Field # | type | mandatory | Instruction |
|----|--------------------|-----------------|-------------------------|
| serial_no | String | Yes |  |
| device_name | String | Yes | device name, e.g: "NFV-D-HZZZ-03A-2201-0F01-DM-TOR-01" |
| vendor | String | yes | vendor name "ZTE","HUAWEI" etc |
| device_model | String | Yes | maipu "S4320", HUAWEI "CE6856" |
| device_sn | String | No | vendor name "ZTE","HUAWEI" etc |
| device_type | String | Yes | "EOR","TOR" |
| resource_pool_name | String | Yes | resource pool name which belongs to , e.g. "NFV-RP-HZZZ-03A_0" |
| cabinet | String | Yes | cabinet which belongs to, in format room-column-cabinet, e.g. "2201-J-01" |
| position | String | Yes | the server position located in the cabinet.|
| remote_ip | String | Yes | BMC/iLO/IPMI ip for remote access, e.g "2409:8086:8313:81::1"|
| gateway | String | Yes | gateway of remote ip, e.g "2409:8086:8313:81::ffff"|
| netmask | String | Yes | e.g. "64"|
| mac_address | String | Yes | mac address|
| ssh_user | String | Yes | e.g. "Administrator"|
| ssh_password | String | Yes | e.g. "password"|
| enable_password | String | Yes | e.g. "password"|
| group | String | Yes | network assignment "service/management/storage"|

<p align="center"><b>Table 5-3-5:</b> Network device.</p>

<a name="5.3.6"></a>
### 5.3.6 EOR card
EOR card data.

| Field # | type | mandatory | Instruction |
|----|--------------------|-----------------|-------------------------|
| serial_no | String | Yes |  |
| eor_device_name | String | Yes | EOR device name |
| card_model | String | Yes | card model |
| slot | String | Yes | slot e.g. "01" |

<p align="center"><b>Table 5-3-6:</b> EOR Card.</p>

<a name="5.3.7"></a>
### 5.3.7 Cabling
Cabling records the physical cable connection information between the ports of server and switch, or switches.
Check tool will verify the correctness according to the cabling data.

| Field # | type | mandatory | Instruction |
|----|--------------------|-----------------|-------------------------|
| serial_no | String | Yes |  |
| source_cabinet | String | Yes | source cabinet which belongs to, in format room-column-cabinet, e.g. "2201-J-01" |
| source_device_name | String | yes | server,switch device name e.g "NFV-D-HZZZ-03A-2201-0G12-DM-TOR-01"|
| source_device_type | String | Yes | switch or server|
| source_port | String | Yes | e.g "gigabitethernet0/2" |
| target_cabinet | String | Yes | source cabinet which belongs to, in format room-column-cabinet, e.g. "2201-J-02" |
| target_device_name | String | yes | server,switch device name e.g "NFV-D-HZZZ-03A-2201-0G12-DM-TOR-01"|
| target_device_type | String | Yes | switch or server|
| target_port | String | Yes | e.g "gigabitethernet0/2" |
| cabling_type | String | Yes | e.g "SV-TOR","TOR-TOR","ST_TOR-ST_EOR","S_TOR-S_EOR","S_TOR-M_EOR","M_TOR-M_EOR","EOR-EOR" |

<p align="center"><b>Table 5-3-7:</b> Cabling.</p>

<a name="5.4"></a>
## 5.4 Appendix
<a name="5.4.1"></a>
### 5.4.1 HDV Original collection.
[CNTT Hardware Delivery Validation (01-2020 DDF)](#https://wiki.lfnetworking.org/pages/viewpage.action?pageId=27525908).