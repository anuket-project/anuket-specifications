Installer Requirements
======================

Introduction
------------

**must**: Requirements that are marked as *must* are considered mandatory and must exist in the reference implementation and implemented by installer. The same applies to *must not*.

**may**: Requirements that are marked as *may* are considered optional. The same applies to *may not*.

Requirements
------------

General
~~~~~~~

The Descriptor File defines the unique configuration required by installer in a common schema.
It would specialize the installer type per user's implementation requirements.
It would be validated at the very beginning of the deployment.
It's the installer's responsibility to translate the descriptor file to adapt with its own configuration.
Thanks to the descriptor file, the NFVi infrastructure deployment could be completed in one step run.

================== ============ =========================================================================================
Ref #              sub-category Description
================== ============ =========================================================================================
``req.gen.ins.01`` Installer    Installer **may** accept a descriptor file to finish deployment.
``req.gen.ins.02`` Installer    Installer implementation **must** validate the descriptor file with schema.
``req.gen.ins.03`` Installer    Any existing installer implementation **may** need adaption for the descriptor file.
``req.gen.ins.04`` Installer    Installer **may** support reporting the deployment progress status.
``req.gen.des.01`` Descriptor   Descriptor file **must** include hardware resource configuration, software configuration.
``req.gen.des.02`` Descriptor   Descriptor file **may** include additional extending configuration.
================== ============ =========================================================================================

Table 6-2-1: Installer requirements

Additional
~~~~~~~~~~

Depends xxx.

Descriptor file definition specification
----------------------------------------

There must be a Descriptor File definition, which used by installer as input of necessary configuration.
Mandatory and optional definition shall be defined, there's no restrictions on how to use it,
there could be multiple ways to implement PDF, the implementation will be in next section.

Resource Pool information
~~~~~~~~~~~~~~~~~~~~~~~~~

This table is the description of the resource pool, it contains only 2 parameters: name and type of the resource pool.

A resource pool maps to only one instance of below parameters.

============= ====== ========= =========================================================================================
Field #       type   mandatory Instruction
============= ====== ========= =========================================================================================
RES_POOL_NAME String Yes       This is the unique name of the resource pool, could be refered by other parameters
RES_POOL_TYPE String No        User defined value to identify different hardware or software configuration requirements.
============= ====== ========= =========================================================================================

Table 6-3-1: Resource Pool Information.

Global Settings
~~~~~~~~~~~~~~~

The Global settings are provided by the user, contains data like like IP_Type, VLAN_Type, etc.

A resource pool maps to only one instance of below parameters.

====================== ====== ========= =============================================================================
Field #                type   mandatory Instruction
====================== ====== ========= =============================================================================
IP_TYPE                String Yes       IPV4 or IPV6
NETWORK_TYPE           String Yes       VLAN or VXLAN
TIMEZONE               String Yes       The timezone where VIM deployed, like UTC+8
STORAGE_TYPE           String Yes       The Storage type, for example "ceph"
HUGEPAGE_ENABLE        String Yes       TRUE or FALSE
HUGEPAGE_SIZE          String Yes       The storage size that hypervisor set for VM, for example "1GB"
QINQ_ENABLE            String Yes       TRUE or FALSE
HYPERVISOR_CORES       String Yes       number of vCPU (CPU cores or hardware threads) assigned to the Hypervisor
EXTERNAL_NTP_SERVER_IP List   Yes       IP list of NTP server, seperated by comma, for example: primariy_IP;second_IP
====================== ====== ========= =============================================================================

Table 6-3-2: Global Settings

Parameters for network virtualization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MTU(Maximum Transmission Unit) configuration in switch is different depends on the which network plane it belongs to, this is usually standard value that defined by user.

3 instances of the parameters are expected(Manage Storage and Service), they may have different MTU requirement.

=========== ====== ========= ===============================================================================================
Field #     type   mandatory Instruction
=========== ====== ========= ===============================================================================================
SWITCH_TYPE String Yes       There should be 3 type of switch based on the network plane: Manage, Storage, and User Services
MTU         String Yes       Maximum transmission unit
=========== ====== ========= ===============================================================================================

Table 6-3-3: Network Virtualization parameter.

server information
~~~~~~~~~~~~~~~~~~

Server information should be provided for installer, including full detail info. for each server, NIC mapping etc.

server information
^^^^^^^^^^^^^^^^^^

A table describing information for each server in the resource pool shall be provided

Multiple instances are expected, one instance of all the parameters for each server.

================== ====== ========= ==================================================================================================================================
Field #            type   mandatory Instruction
================== ====== ========= ==================================================================================================================================
NAME               String Yes       Server name should be aligned with naming rule, this is the unique ID for each device to be referred for identify device
VENDOR             String No        Vendor of device
SKU                String Yes       The SKU of device, can be referred by other table NIC connection table, to identify slot-port mapping for device
MODEL              String Yes       This is the model for different service type, this value is defined from design document of resource pool, example NC1, NC1-S
SN                 String Yes       Serial Number, each server has a unique SN
RES_POOL           String Yes       Resource pool name
RACK               String Yes       rack name where device located
POS                String Yes       the position of device in rack, like 2-3U,4-5U
BMC_IP             String Yes
BMC_GATEWAY        String Yes
BMC_MASK           String Yes
BMC_SUBNET         String Yes
BMC_USR            String Yes       BMC user
BMC_PWD            String Yes       BMC password, Instead of clear-text password, password encryption is recommended for security consideration
INTERNAL_IP        String Yes       It is an internal IP configured and used by hardware integration tools, it will be removed after hardware integration verification
INTERNAL_GATEWAY   String Yes
INTERNAL_MASK      String Yes
GROUP_NAME         String Yes       Usage of server, Manage or Storage or Service
BMC_PRE_CONFIGURED String Yes       YES or NO
HW_REGION          String No        Hardware region divided by room or area, this is need when pod needs to build on more than one lab, For example: Lab01 or Lab02
MODULE_NAME        String Yes       hardware model that divided within each region, Like "Model 3 in Region A", usually contains certain number of racks
================== ====== ========= ==================================================================================================================================

Table 6-3-4-1: Server Information.

server NIC information
^^^^^^^^^^^^^^^^^^^^^^

This table is describing the slot and port mapping for NICs in each type of server.
Port BDF(`Bus:Device.Function (BDF) Notation <https://wiki.xenproject.org/wiki/Bus:Device.Function_(BDF)_Notation>`__) information is also needed for each port,
it will be used to identify the logical port name after OS is installed.
Multiple entries per server type are expected for describing all NIC slots, 1 entry for each port.
Information for all server types in pool should be included.

============= ====== ========= ===================================================================================================================
Field #       type   mandatory Instruction
============= ====== ========= ===================================================================================================================
VENDOR        String Yes       Vendor of server
SKU           String Yes       SKU of server
SERVICE MODEL String Yes       server service type defined by provider/user, same definition as in above table, example: NC1 or NC2
SLOT          String Yes       Slot number in server for each NIC, for example, PCIeSlot2
NETWORK_PLANE String Yes       Network plane for each nic, Manage or Storage or Service
PORT          List   Yes       Ports number for the above NIC, for example: 1_1 or 1_2, 2 ports for one NIC, so 2 entries are needed for same slot
PORT_BDF      String Yes       Port BDF value for above port
============= ====== ========= ===================================================================================================================

Table 6-3-4-2: Server NIC Information.

Network Device information
~~~~~~~~~~~~~~~~~~~~~~~~~~

This table describes each network device, it can be used for network configuration and verification.

Multiple instances are expected, one instance for each network device.

=========== ====== ========= ==========================================================================================================================
Field #     type   mandatory Instruction
=========== ====== ========= ==========================================================================================================================
NAME        String Yes       Name of network device
VENDOR      String Yes       Vendor name for network device
SKU         String Yes       SKU
MODEL       String Yes       Type of switch, like Access Switch or Aggregation Switch
SN          String Yes       Serial number
HW_RES_POOL String Yes       Resource pool name for hardware
RACK        String Yes       rack number where switch is placed
POS         String Yes       position in rack
BMC_IP      String Yes
BMC_GATEWAY String Yes
BMC_MASK    String Yes
BMC_USR     String Yes       BMC login user
BMC_PWD     String Yes       password for BMC login user. Instead of clear-text password, password encryption is recommended for security consideration
ENABLE_PWD  String Yes       Enable password. Instead of clear-text password, password encryption is recommended for security consideration
GROUP_NAME  String Yes       Manage or storage or service
HW_REGION   String Yes       Hardware region
MODULE_NAME String Yes       Hardware module which is devided by location, like area A module 1
=========== ====== ========= ==========================================================================================================================

Table 6-3-5: Network device information.

Port mapping information
~~~~~~~~~~~~~~~~~~~~~~~~

Wiremap defines the port mapping between server/switch and switch for each line,
we will need this information to trace the connected server and port, so we can extrapolate the required network configuration for the port.

Multiple instances are expected, one instance for each physical cable.

+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field #     | type   | mandatory | Instruction                                                                                                                                                    |
+=============+========+===========+================================================================================================================================================================+
| NAME        | String | Yes       | Name of network device                                                                                                                                         |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LOCAL_RACK  | String | Yes       | the rack info for local device                                                                                                                                 |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LOCAL_NAME  | String | Yes       | local device name, LOCAL_NAME must reference either "Network Device Name" from table 6.3.5                                                                     |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LOCAL_TYPE  | String | Yes       | Local device type, switch or server                                                                                                                            |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LOCAL_PORT  | String | Yes       | connected port in local device                                                                                                                                 |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REMOTE_RACK | String | Yes       |                                                                                                                                                                |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REMOTE_NAME | String | Yes       | connected remote device name, REMOTE_NAME must reference either "Network Device Name" from table 6.3.5 or "Server Name" from table 6.3.4.1                     |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REMOTE_TYPE | String | Yes       | remote device type, it can be switch or server                                                                                                                 |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REMOTE_PORT | String | Yes       | connected port in remote device. When describing port for remote servers, we use port number like 1_1, or 1_2, instead of PCIeslot number, because the server  |
|             |        |           | NIC mapping is already defined in 6.3.4.2                                                                                                                      |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LINE_TYPE   | String | Yes       | Line type to describe local device type and remote device type, how each line is connected. For example "S-SRV-C_S-TOR" means this line is connecting a        |
|             |        |           | service server in compute module to service TOR, and another example "ST-SRV-S_M-TOR" means storage server connecting to a manage TOR in storage module. The   |
|             |        |           | line type can be customized defined, as long as it's unified in end user.                                                                                      |
+-------------+--------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Table 6-3-6: Port mapping information.

Network planning information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Network planning information for the resource pool of each node needs to be defined which should include VLAN ID an allocated IP range.

Multiple instances are expected, one instance for each network plane.

==================== ====== ========= =======================================================================
Field #              type   mandatory Instruction
==================== ====== ========= =======================================================================
APPLICATION_LAYER    String Yes       VIM or storage
DOMAIN               String Yes       name of VIM/storage software product
VENDOR_NETWORK_PLANE String Yes       network plane designed/needed by software product
NETWORK_PLANE        String Yes       corresponding network plane in user view, like Manage, Storage, service
VENDOR               String Yes       vendor of software product
VLAN_ID              List   Yes       designed VLAN id or id list for each network plane
IP_SEGMENT           String Yes       assigned IP segments
GATEWAY              String Yes       gateway IP for each IP range
SWITCH_CONFIG_TYPE   String Yes
==================== ====== ========= =======================================================================

Table 6-3-7: Network planning information.

TOR(Access switch) VLAN configuration information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple instances are expected, one instance for each TOR.

=============== ====== ========= ====================================================================================================
Field #         type   mandatory Instruction
=============== ====== ========= ====================================================================================================
DEVICE_NAME     String Yes
VENDOR          String Yes
DEVICE_MODEL    String Yes
DEVICE_SN       String Yes
BMC_IP          String Yes
SSH_USER        String Yes
SSH_PASSWORD    String Yes       Instead of clear-text password, password encryption is recommended for security consideration
ENABLE_PASSWORD String Yes       Instead of clear-text password, password encryption is recommended for security consideration
PORT            List   Yes       group multiple ports with same VLAN configuration, and separate different port group with ";"
VLAN_TYPE       List   Yes       tag or untag
VLAN_ID         List   Yes       group multiple VLAN with same configuration requirements, and separate different VLAN group with ";"
PORT_TYPE       List   Yes       trunk or access or hybrid
=============== ====== ========= ====================================================================================================

Table 6-3-8: TOR VLAN information.

VLAN configuration for Aggregation Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple instances are expected, one instance for each Aggregation Switch.

=============== ====== ========= ====================================================================================================
Field #         type   mandatory Instruction
=============== ====== ========= ====================================================================================================
DEVICE_NAME     String Yes
VENDOR          String Yes
DEVICE_MODEL    String Yes
DEVICE_SN       String Yes
BMC_IP          String Yes
SSH_USER        String Yes
SSH_PASSWORD    String Yes       Instead of clear-text password, password encryption is recommended for security consideration
ENABLE_PASSWORD String Yes       Instead of clear-text password, password encryption is recommended for security consideration
PORT            List   Yes       group a list of ports with same VLAN configuration, and separate different port group with ";"
VLAN_ID         List   Yes       group multiple VLAN with same configuration requirements, and separate different VLAN group with ";"
VLANIF_ADDRESS  List   Yes       Vlanif addresses that need to be configured on Aggregation Switch
NETWORK_MASK    List   Yes
=============== ====== ========= ====================================================================================================

Table 6-3-9: Aggregation Switch VLAN information.

Host Aggregate information
~~~~~~~~~~~~~~~~~~~~~~~~~~

Servers in the resource pool are usually divided to multiple groups, will use HA(Host Aggregation) to represent host group.
One HA could belong to multiple AZ(Availability Zone)
It is the definition of each HA in the resource pool. it should contain the server list for each HA, and also the HA meta data.

Host HA Mapping
^^^^^^^^^^^^^^^

Multiple instances are expected, defines all servers in HA

=========== ====== ========= ===========================================
Field #     type   mandatory Instruction
=========== ====== ========= ===========================================
HA_NAME     String Yes       HA name, which will following naming rules.
DEVICE_NAME String Yes       server name in current HA
=========== ====== ========= ===========================================

Table 6-3-10-1: Host HA Information.

HA metadata
^^^^^^^^^^^

Multiple instances are expected, service, management and DMZ.

=========== ====== ========= ============================================================================
Field #     type   mandatory Instruction
=========== ====== ========= ============================================================================
HA_NAME     String Yes
HA_METADATA String Yes       properties for each HA, for example: type=TrustPlane,ovs=C-plane,sriov=false
AZ_NAME     String Yes       AZ name that HA belongs to
=========== ====== ========= ============================================================================

Table 6-3-10-2: HA meta Information.

VIM Nodes
~~~~~~~~~

There's a list of servers that was defined as control/management nodes according to resource pool plan

Multiple instances are expected, defines all management servers.

=========== ====== ========= ===============
Field #     type   mandatory Instruction
=========== ====== ========= ===============
DEVICE_NAME String Yes       The server name
=========== ====== ========= ===============

Table 6-3-11: VIM Nodes Information.

SDNC Nodes
~~~~~~~~~~

Multiple instances are expected, defines all SDN controllers

=========== ====== ========= ===============
Field #     type   mandatory Instruction
=========== ====== ========= ===============
DEVICE_NAME String Yes       The server name
=========== ====== ========= ===============

Table 6-3-12: SDNC Nodes Information.

Storage cluster information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Definition of storage cluster and storage pool,

Storage pool plan
^^^^^^^^^^^^^^^^^

Storage pool name in each storage cluster, and nodes in Storage pool should be defined, so the storage installer will know which nodes are installing.

Multiple instances are expected, each instance defines one storage node

==================== ====== ========= =========================================================
Field #              type   mandatory Instruction
==================== ====== ========= =========================================================
STORAGE_CLUSTER_NAME String Yes       Storage cluster name, which needs to follow naming rules.
STORAGE_POOL_NAME    String Yes       Storage pool name, which needs to follow naming rules.
DEVICE_NAME          String Yes       Storage servers in each storage pool
==================== ====== ========= =========================================================

Table 6-3-13-1: Storage Pool Plan

Distribution storage pool info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Storage pool information, defines the management account and network information

Multiple instances are expected, each instance defines one storage pool

========================== ====== ========= =============================================================================================
Field #                    type   mandatory Instruction
========================== ====== ========= =============================================================================================
STORAGE_CLUSTER_NAME       String Yes
NODE_POOL                  String No
DISK_POOL_NAME             String No
STORAGE_POOL_NAME          String Yes
HA_NAME_LIST               List   Yes       The corresponding HA lists for current storage pool
AZ_NAME                    String Yes       The corresponding AZ for current storage pool
STORAGE_POOL_NODE_CCOUNT   String Yes       How many nodes for current storage pool
MAX_QUOTA_CAPACITY         String Yes
STORAGE_POOL_MANAGEMENT_IP String Yes       Designed virtural IP for storage pool management
NETWORK_MASK               String Yes
GATEWAY                    String Yes
VIM_USER                   String Yes       VIM credential
VIM_PASSWORD               String Yes       Instead of clear-text password, password encryption is recommended for security consideration
PIM_USER                   String Yes       PIM credential
PIM_PASSWORD               String Yes       Instead of clear-text password, password encryption is recommended for security consideration
STORAGE_CLUSTER_SERVICE_IP String Yes
STORAGE_CLUSTER_SERVICE_GW String Yes
STORAGE_CLUSTER_BACKEND_IP String Yes
STORAGE_CLUSTER_BACKEND_GW String Yes
BACKUP_POLICY              String Yes
========================== ====== ========= =============================================================================================

Table 6-3-13-2: Distribution storage pool info.

Software integration information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After VIM and Storage software installation finished, parameters willl be needed in integration process of VIM and Storage,
the parameters should be defined in advance.

VIM Context
^^^^^^^^^^^

Parameters from VIM vendor for integration.

Only one entry is expected.

===================== ====== ========= ====================================================
Field #               type   mandatory Instruction
===================== ====== ========= ====================================================
VENDOR                String Yes
AUTHORIZATION         String Yes       One-way or Two-way authentication
VIM_CERTIFICATES_PATH String Yes       Full path for certificates that used for integration
===================== ====== ========= ====================================================

Table 6-3-14-1: VIM context Information.

Storage Context
^^^^^^^^^^^^^^^

Parameters from storage vendor for integration.

Only one entry is expected.

======================== ====== ========= =========================================================
Field #                  type   mandatory Instruction
======================== ====== ========= =========================================================
VENDOR                   String Yes
AUTHORIZATION            String Yes       One-way or Two-way authentication
JOINT_WAY                String Yes       by ISCSI or client
DRIVER_FULL_NAME         String Yes       Full path for storage driver
CEPH_CONFIG_PATH         String Yes       Full path for ceph.conf storage
IS_PIM_JOINT             String Yes       whether integrate with PIM, usaually "YES" for this value
STORAGE_SOFTWARE_VERSION String Yes
======================== ====== ========= =========================================================

Table 6-3-14-2: Storage context Information.

Storage Client context
^^^^^^^^^^^^^^^^^^^^^^

This table defines the parameters for integration with storage client

Multiple entries are expected, one entry for each authorization user.

================== ====== ========= ======================================================================
Field #            type   mandatory Instruction
================== ====== ========= ======================================================================
JOINT_WAY          String Yes       integration method for storage client, for example, RBD
COMPONENT_TYPE     String Yes       for example: cinder, glance or nova
AUTHORIZATION_USER String Yes       match with the component type
KEYRING_FILENAME   String Yes       Full path for keyring file, this should match the authentication user,
================== ====== ========= ======================================================================

Table 6-3-14-3: Storage client context.

Device Management information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SERVER PIM(Physical Infrastructure Manager) ACCOUNT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This table is not mandatory because not all installer require redfish.
It is only requried when servers managed by PIM through redfish, credentials should be the same for same type of device.

Multiple entries are expected, one entry for each server model.

============== ====== ========= =============================================================================================
Field #        type   mandatory Instruction
============== ====== ========= =============================================================================================
VENDOR         String No
SERVER_MODEL   String No        MODEL for each type of server
REDFISH_USER   String No
REDFISH_PASSWD String No        Instead of clear-text password, password encryption is recommended for security consideration
============== ====== ========= =============================================================================================

Table 6-3-15-1: SERVER PIM ACCOUNT Information.

Switch PIM Account
^^^^^^^^^^^^^^^^^^

Servers are managed by SNMP, credentials should be the same for same type of device

Multiple entries are expected, one entry for each device model.

===================== ====== ========= =============================
Field #               type   mandatory Instruction
===================== ====== ========= =============================
VENDOR                String Yes
DEVICE_MODEL          String Yes       MODEL for each type of switch
SNMP_VERSION          String Yes       v3 by default
SNMP_USER             String Yes
AUTHENTICATION_METHOD String Yes       for example: MD5 or SHA1
VERIFICATION_CODE     String Yes
ENCRYPTION_METHOD     String Yes
ENCRYPTION_KEY        String Yes
===================== ====== ========= =============================

Table 6-3-15-2: Switch PIM Account.

Installer prerequisite
----------------------

Hardware validation
~~~~~~~~~~~~~~~~~~~

Before the installation, the user has to check if each server meets the deployment requirements:

-  BIOS settings: RAID configuration, PXE boot order and boot mode, disk capacity, CPU, and memory settings,
-  remote management accessibility (for example, IPMI, iLO, BMC),
-  NIC quantity and configuration.

Network configuration
~~~~~~~~~~~~~~~~~~~~~

The necessary prerequisite settings must be ready before the deployment, for example:

-  the VLAN must be configured on the switch,
-  the IP address ranges to be used must be allocated.

PDF implementation
------------------

When we use PDF for installer or verification tools, all the required data described in 6.3 should be included.
There's no limitation on how to implement PDF, like the file type of PDF could be csv or json,
and also you can adjust the file structure, whichever is more readable to the tools.
Taking servers information for example, you can use flat version to include all parameters in 6.3.4 for each device,
or you can group servers with same properties like same Vendor, same model, or same usage.
You can refer anuket PDF pages for details about how to implement: https://wiki.anuket.io/pages/viewpage.action?pageId=4406598
