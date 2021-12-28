Hardware Delivery and Configuration Requirements
================================================

Introduction
------------

**must**: Requirements that are marked as *must* are considered mandatory and must exist in the reference implementation and implemented by installer. The same applies to *must not*.

**may**: Requirements that are marked as *may* are considered optional. The same applies to *may not*.

Requirements
------------

As we known, the NFVi software builds upon a set of hardware resources. For the operator(user) having a set of hardware resources, there is an inevitable step to examine it before deployment of the software.
If there is only limited nodes for lab demonstration or something like this, it's acceptable to do it manually, however it would be a time consuming process especially there are large scale of hardware nodes, for example 1000 node.
Also,adding the different provider's factor, that's much complicated to validate it and a headache thing if doing it in manual.
In order to resolve this issue of how to validate hardware efficiently , we call on here to build up a common data model for describing the hardware data, which is extensible to large scale and can be recognized by some automated check tool (Let's call it checker).
Let's also name it to description file, which is align with the one for software deployment definition already commited in another chapter.
The description file defines the same information data model accross the hardware vendor provider.
At present, in the first release,only the "readable" hardware parameter can be focused, in future release, "writable" parameter might add also.
Besides, we also collect the common hardware check requiremnt here, most of which are origially from Prague meeting.
We are expecting that by utilizing the common hardware description file, the check tool will perform all the neccessary hardware check point automatically.
We believe this is a mutual interest for all operators having such needs.

General
~~~~~~~

A Descriptor File defines the configuration required by the checker in a common schema.
The "checker tool" validates the current hardware against the descriptor file, listing mismatches or differences, as failures, allowing the user to quickly identify and correct any errors in hardware, network wiring, or configuration.
If failures are detected, the process can be rerun after corrective actions are taken.
This checking process must be completed before the software stack deployment.

================== ============ =======================================================================================================================================
Ref #              sub-category Description
================== ============ =======================================================================================================================================
``req.gen.chk.01`` Checker      Checker **must** accept a descriptor file to finish hardware delivery validation.
``req.gen.chk.02`` Checker      Checker **must** report the checking result of success or failure with reason.
``req.gen.des.01`` Descriptor   Descriptor file **must** include neccessary information to remote access hardware resource
``req.gen.des.02`` Descriptor   Descriptor file **may** automate to generate from a user defined rule of how to generate asset name, IP address, gateways, VLAN ID, etc
================== ============ =======================================================================================================================================

Table 5-2-1: Check tool requirements

Check point
~~~~~~~~~~~

Till now, following the check point requirements are collected: (#5.4.1)

+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Test Type #                 | Purpose                                                                   | Example                                                                   | Check when |
+=============================+===========================================================================+===========================================================================+============+
| BIOS Settings               | Verifies all applicable BIOS settings per hardware model.                 | Boot mode/Boot Sequence Retry/AC Power Recovery/Power Setting (balanced / |            |
|                             |                                                                           | performance)/Virt. Technology/Simultaneous Multithreading/Trusted         |            |
|                             |                                                                           | platform module                                                           |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Firmware Settings           | Verifies all applicable Firmware settings.                                | BIOS/Storage Array Controller/NIC (e.g.Intel X710)/PXE Enabled Ports      |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Boot Order                  | Verifies applicable boot order settings.                                  | First boot, Second boot.                                                  |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Hardware Health             | Queries Intelligent Platform Management Interface (IPMI) is for all       | Raid/System Board/CPU temp/Power Supply                                   |            |
|                             | hardware components and their health status.                              |                                                                           |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| PCI Slot Status & MAC       | Which cards are in which slot, which slot is assigned to which CPU, slot  | card(s) in slot/port/PCI partition /Slot speed / type / CPU / Slot        |            |
|                             | type                                                                      | assignment                                                                |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| NIC                         | Validates that all NICs are in the correct slots, with a healthy status   | Correct LLDP neighbor MAC Addresses.                                      |            |
|                             | (per IPMI), have correct MAC addresses, and are detecting a cable         |                                                                           |            |
|                             | connection (or not).                                                      |                                                                           |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| IPMI Logs                   | Check for existence of logs.                                              | Physical event logged. E.g. chassis open on power up.                     |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| IPMI Users                  | Check for existence of user accounts.                                     | Check if IPMI is available, if IPMI account is existing, if IPMI default  |            |
|                             |                                                                           | credentials.                                                              |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Hardware Inventory          | Inventory of h/w on platform.                                             | CPU and count, NUMA topology, CPU Freq, RAM, speed, size, model, etc.     |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Physical Disk Configuration | Verifies storage / disk config (type, size)                               | Physical disk type, card/port location,capacity                           |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| SRIOV Port Validation       | Verifies global and NIC level enabled.                                    | Confirm setting is enabled (or none)                                      |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Hardware Check              | Verifies basic OS config attributes (i.e. Linux running on the host and   | RAM size/number of cores.                                                 |            |
|                             | reporting these values).                                                  |                                                                           |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Cabling Connection check    | Verifies the wired connection between server NIC port and switch port, or | Check if cabling is plugin correct as expected design data                |            |
|                             | the between switches.                                                     |                                                                           |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+
| Redfish interface           | Verifies that support classic interface.                                  | system service/Manager                                                    |            |
|                             |                                                                           | service/ChassisService/SessionService/AccountService/EventService etc.    |            |
+-----------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+------------+

Table 5-2-2: Hardware check point.

Descriptor file definition
--------------------------

As mentioned at the beginning, the description file is used to define the common hardware data which are used by the checker implementation
The entry information must be included in the description file,which are the remote access parameter settings.

Resource pool
~~~~~~~~~~~~~

Resource pool is the conception which a NFV resource is planned to build up. It consists hardware server device, network device and cabling among them.
It is referenced by other resource type to introduce later.

================== ====== ========= =====================================
Field #            type   mandatory Instruction
================== ====== ========= =====================================
serial_no          String Yes
resource_pool_name String Yes       resource name, e.g: NFV-RP-HZZZ-03A_0
type               String Yes       TOCHECK: OTHER
================== ====== ========= =====================================

Table 5-3-1: Resource pool.

NIC template
~~~~~~~~~~~~

NIC Template defines network interface card parameters, it includes the crucial port number on the NIC, which is used as the reference in the cabling data and check.

================ ====== ========= =====================================================================================================
Field #          type   mandatory Instruction
================ ====== ========= =====================================================================================================
serial_no        String Yes
vendor           String Yes       vendor name: ZTE,HUAWEI
server_type      String Yes       ZTE "R5300 G4", HUAWEI "TaiShan200-2280"
customized_model String No        customized model: C2,C21
nic_vendor       String Yes       nework interface card vendor: intel
nic_type         String Yes       Intel "x520"
rootbdf          String Yes       e.g "00:03:01:00"
slot_id          String Yes       the slot id number of card plugged-in
connect_type     String Yes       plugin
port_quantity    Number Yes       port quantity on the card. e.g. 2
port_bandwith    String Yes       bandwith of port. e.g. 10G
cabling_ports    Number Yes       port name used in the cabing data. corresponding the quantity e.g: 1_1;1_2 or Slot3/Port1;Slot3/Port2
================ ====== ========= =====================================================================================================

Table 5-3-2: NIC template.

Cabinet
~~~~~~~

Cabinet is the rack holder for the server and network devices. The data will be referenced by server and network device data.

========= ====== ========= =======================================
Field #   type   mandatory Instruction
========= ====== ========= =======================================
serial_no String Yes
room      String Yes       room number, e.g: 2201
column    String Yes       column number in the room: e.g. "J"
cabinet   String Yes       cabinet number in the column: e.g. "01"
========= ====== ========= =======================================

Table 5-3-3: Cabinet.

Server
~~~~~~

The server device data defines key information about how to access the server remotely, for example remote IP address, user, and credentials.
There are many ways to validate the hardware by remote interface verification, for example IPMI and redfish.
Considering the number of servers, the user can choose to validate the server interface in a distributed way or in a centralized way.
Distributed validation means that the server connects to the hardware management device (for example, BMC and IPMI) to validate the connection.
Centralized validation means that the hardware management device connects to the server to validate the connection.
The best practice is to use centralized validation when the number of servers is small (for example, storage servers), and use distributed validation when the number of servers is large (for example, generic servers).

================== ====== ========= =========================================================================
Field #            type   mandatory Instruction
================== ====== ========= =========================================================================
serial_no          String Yes
server_name        String Yes       server name, e.g: NFV-D-HZZZ-03A-2201-0J01-M-SRV-01
vendor             String Yes       vendor name "ZTE","HUAWEI" etc
server_type        String Yes       ZTE "R5300 G4", HUAWEI "TaiShan200-2280"
customized_model   String No        customized model: C2,C21
server_sn          String Yes       server serial number
resource_pool_name String Yes       resource pool name which belongs to
cabinet            String Yes       cabinet which belongs to, in format room-column-cabinet, e.g. "2201-J-01"
position           String Yes       the server position located in the cabinet.
remote_ip          String Yes       BMC/iLO/IPMI ip for remote access, e.g "2409:8086:8313:81::1"
gateway            String Yes       gateway of remote ip, e.g "2409:8086:8313:81::ffff"
outband_netmask    String Yes       e.g. "64"
subnet             String Yes       e.g. "2409:8086:8313:81"
remote_user        String Yes       e.g. "Administrator"
remote_password    String Yes       e.g. "password"
inband_ip          String No        temporary inband_ip e.g "2409:8086:8313:f::24"
inband_gateway     String No        gateway of inband ip, e.g "2409:8086:8313:f::ffff"
inband_netmask     String No        e.g. "64"
group              String Yes       network assignment "service/management/storage"
is_bmc_configured  String Yes       TOCHECK
================== ====== ========= =========================================================================

Table 5-3-4: Server.

Network device
~~~~~~~~~~~~~~

network device data defines the key data about how to remote access the network device, such as switches and routers.

================== ====== ========= =========================================================================
Field #            type   mandatory Instruction
================== ====== ========= =========================================================================
serial_no          String Yes
device_name        String Yes       device name, e.g: "NFV-D-HZZZ-03A-2201-0F01-DM-TOR-01"
vendor             String yes       vendor name "ZTE","HUAWEI" etc
device_model       String Yes       maipu "S4320", HUAWEI "CE6856"
device_sn          String No        vendor name "ZTE","HUAWEI" etc
device_type        String Yes       "EOR","TOR"
resource_pool_name String Yes       resource pool name which belongs to , e.g. "NFV-RP-HZZZ-03A_0"
cabinet            String Yes       cabinet which belongs to, in format room-column-cabinet, e.g. "2201-J-01"
position           String Yes       the server position located in the cabinet.
remote_ip          String Yes       BMC/iLO/IPMI/redfish ip for remote access, e.g "2409:8086:8313:81::1"
gateway            String Yes       gateway of remote ip, e.g "2409:8086:8313:81::ffff"
netmask            String Yes       e.g. "64"
mac_address        String Yes       mac address
protocol           String Yes       ssh/telnet/redfish etc.
user               String Yes       e.g. "Administrator"
password           String Yes       e.g. "password"
enable_password    String Yes       e.g. "password"
group              String Yes       network assignment "service/management/storage"
================== ====== ========= =========================================================================

Table 5-3-5: Network device.

EOR card
~~~~~~~~

EOR card data.

=============== ====== ========= ===============
Field #         type   mandatory Instruction
=============== ====== ========= ===============
serial_no       String Yes
eor_device_name String Yes       EOR device name
card_model      String Yes       card model
slot            String Yes       slot e.g. "01"
=============== ====== ========= ===============

Table 5-3-6: EOR Card.

Cabling
~~~~~~~

Cabling records the physical cable connection information between the ports of server and switch, or switches.
Check tool will verify the correctness according to the cabling data.

================== ====== ========= ==========================================================================================
Field #            type   mandatory Instruction
================== ====== ========= ==========================================================================================
serial_no          String Yes
source_cabinet     String Yes       source cabinet which belongs to, in format room-column-cabinet, e.g. "2201-J-01"
source_device_name String yes       server,switch device name e.g "NFV-D-HZZZ-03A-2201-0G12-DM-TOR-01"
source_device_type String Yes       switch or server
source_port        String Yes       e.g "gigabitethernet0/2"
target_cabinet     String Yes       source cabinet which belongs to, in format room-column-cabinet, e.g. "2201-J-02"
target_device_name String yes       server,switch device name e.g "NFV-D-HZZZ-03A-2201-0G12-DM-TOR-01"
target_device_type String Yes       switch or server
target_port        String Yes       e.g "gigabitethernet0/2"
cabling_type       String Yes       e.g "SV-TOR","TOR-TOR","ST_TOR-ST_EOR","S_TOR-S_EOR","S_TOR-M_EOR","M_TOR-M_EOR","EOR-EOR"
================== ====== ========= ==========================================================================================

Table 5-3-7: Cabling.

Server model
~~~~~~~~~~~~

The server model describes processor, memory, harddrive, raid,manufacturer, model etc.
server model will be referenced by servers.

======================= ====== ========= ==========================================
Field #                 type   mandatory Instruction
======================= ====== ========= ==========================================
name                    String Yes       model name will referenced by server
manufacturer            String Yes
model                   String Yes
processor               String Yes
memory                  String Yes
hard_drive              String Yes
raid                    String Yes
network_card_infos      List   No        interface list definition
network_card_bond_infos List   No        NIC bonding, might not be always the case.
======================= ====== ========= ==========================================

Table 5-3-8: Server model.

Network device model
~~~~~~~~~~~~~~~~~~~~

The network device model describes processor, memory,manufacturer, model etc.
network device model will be referenced by network device.

============= ====== ========= ============================================
Field #       type   mandatory Instruction
============= ====== ========= ============================================
name          String Yes       model name will referenced by network device
manufacturer  String Yes
model         String Yes
processor     String Yes
port_type     String Yes       port type
port_quantity String Yes       total number of port
memory        String Yes
version       String Yes
============= ====== ========= ============================================

Table 5-3-9: Network device model.

Appendix
--------

HDV original collection.
~~~~~~~~~~~~~~~~~~~~~~~~

`CNTT Hardware Delivery Validation (01-2020 DDF) <https://wiki.lfnetworking.org/pages/viewpage.action?pageId=27525908>`__
