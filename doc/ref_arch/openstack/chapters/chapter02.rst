Architecture Requirements
=========================

Introduction
------------

**must**: Requirements that are marked as *must* are considered
mandatory and must exist in the reference architecture and reflected in
any implementation targeting this reference architecture. The same
applies to *must not*.

**should**: Requirements that are marked as *should* are expected to be
fulfilled by the reference architecture but it is up to each service
provider to accept an implementation targeting this reference
architecture that is not reflecting on any of those requirements. The
same applies to *should not*. > RFC2119

**may**: Requirements that are marked as *may* are considered optional.
The same applies to *may not*.

This chapter includes both “Requirements” that must be satisifed in an
RA-1 conformant implementation and “Recommendations” that are optional
for implementation.

Reference Model Requirements
----------------------------

The tables below contain the requirements from the Reference Model to
cover the Basic and High-Performance profiles.

To ensure alignment with the infrastructure profile catalogue, the
following requirements are referenced through:

-  Those relating to Cloud Infrastructure Software Profiles
-  Those relating to Cloud Infrastructure Hardware Profiles
-  Those relating to Cloud Infrastructure Management
-  Those relating to Cloud Infrastructure Security

Cloud Infrastructure Software Profile Requirements for Compute (source `RM 5.2 <../../../ref_model/chapters/chapter05.md#5.2>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Requirement | Requirement | Sp          |
|             |             | for Basic   | for High    | ecification |
|             |             | Profile     | Performance | Reference   |
|             |             |             | Profile     |             |
+=============+=============+=============+=============+=============+
| e.cap.001   | Max number  | At least 16 | At least 16 |             |
|             | of vCPU     |             |             |             |
|             | that can be |             |             |             |
|             | assigned to |             |             |             |
|             | a single    |             |             |             |
|             | instance by |             |             |             |
|             | the Cloud   |             |             |             |
|             | Inf         |             |             |             |
|             | rastructure |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.002   | Max memory  | at least 32 | at least 32 |             |
|             | that can be | GB          | GB          |             |
|             | assigned to |             |             |             |
|             | a single    |             |             |             |
|             | instance by |             |             |             |
|             | the Cloud   |             |             |             |
|             | Inf         |             |             |             |
|             | rastructure |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.003   | Max storage | at least    | at least    |             |
|             | that can be | 320 GB      | 320 GB      |             |
|             | assigned to |             |             |             |
|             | a single    |             |             |             |
|             | instance by |             |             |             |
|             | the Cloud   |             |             |             |
|             | Inf         |             |             |             |
|             | rastructure |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.004   | Max number  | 6           | 6           |             |
|             | of          |             |             |             |
|             | connection  |             |             |             |
|             | points that |             |             |             |
|             | can be      |             |             |             |
|             | assigned to |             |             |             |
|             | a single    |             |             |             |
|             | instance by |             |             |             |
|             | the Cloud   |             |             |             |
|             | Inf         |             |             |             |
|             | rastructure |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.005   | Max storage | Up to 16TB1 | Up to 16TB1 |             |
|             | that can be |             |             |             |
|             | attached /  |             |             |             |
|             | mounted to  |             |             |             |
|             | an instance |             |             |             |
|             | by the      |             |             |             |
|             | Cloud       |             |             |             |
|             | Inf         |             |             |             |
|             | rastructure |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.006/  | CPU pinning | Not         | Must        |             |
| infra.      | support     | required    | support     |             |
| com.cfg.003 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.007/  | NUMA        | Not         | Must        |             |
| infra.      | support     | required    | support     |             |
| com.cfg.002 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.018/  | S           | Must        | Optional    |             |
| infra.      | imultaneous | support     |             |             |
| com.cfg.005 | Mul         |             |             |             |
|             | tithreading |             |             |             |
|             | (SMT)       |             |             |             |
|             | enabled     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| i.cap.018/  | Huge pages  | Not         | Must        |             |
| infra.      | configured  | required    | support     |             |
| com.cfg.004 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-1a: Reference Model Requirements: Cloud Infrastructure Software
Profile Capabilities

   **1** Defined in the ``.bronze`` configuration in `RM section 4.2.6
   Storage
   Extensions <../../../ref_model/chapters/chapter04.md#4.2.6>`__\ 

Cloud Infrastructure Software Profile Extensions Requirements for Compute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Profile     | Profile     | Sp          |
|             |             | Extensions  | Extra-Specs | ecification |
|             |             |             |             | Reference   |
+=============+=============+=============+=============+=============+
| e.cap.008/  | IPSec       | Compute     |             |             |
| infra.com.  | A           | Intensive   |             |             |
| acc.cfg.001 | cceleration | GPU         |             |             |
|             | using the   |             |             |             |
|             | v           |             |             |             |
|             | irtio-ipsec |             |             |             |
|             | interface   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.010/  | Transcoding | Compute     | Video       |             |
| infra.com.  | A           | Intensive   | Transcoding |             |
| acc.cfg.002 | cceleration | GPU         |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.011/  | P           | Firmware-p  | Accelerator |             |
| infra.com.  | rogrammable | rogrammable |             |             |
| acc.cfg.003 | A           | adapter     |             |             |
|             | cceleration |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.012   | Enhanced    | E           | E           |             |
|             | Cache       |             |             |             |
|             | Management: |             |             |             |
|             | L=Lean;     |             |             |             |
|             | E=Equal;    |             |             |             |
|             | X=eXpanded  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.014/  | Hardware    | Compute     |             |             |
| infra.com.  | coprocessor | Intensive   |             |             |
| acc.cfg.004 | support     | GPU         |             |             |
|             | (GPU/NPU)   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.016/  | FPGA/other  | Firmware-p  |             |             |
| infra.com.  | A           | rogrammable |             |             |
| acc.cfg.005 | cceleration | adapter     |             |             |
|             | H/W         |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-1b: Cloud Infrastructure Software Profile Extensions
Requirements for Compute

Cloud Infrastructure Software Profile Requirements for Networking (source `RM 5.2.3 <../../../ref_model/chapters/chapter05.md#5.2.3>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The features and configuration requirements related to virtual
networking for the two (2) types of Cloud Infrastructure Profiles are
specified below followed by networking bandwidth requirements.

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Requirement | Requirement | Sp          |
|             |             | for Basic   | for         | ecification |
|             |             | Profile     | High-       | Reference   |
|             |             |             | Performance |             |
|             |             |             | Profile     |             |
+=============+=============+=============+=============+=============+
| infra.      | IO          | Must        | Must        |             |
| net.cfg.001 | vir         | support     | support     |             |
|             | tualisation |             |             |             |
|             | using       |             |             |             |
|             | virtio1.1   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.      | The overlay | Must        | *No         |             |
| net.cfg.002 | network     | support     | requirement |             |
|             | en          | VXLAN,      | specified*  |             |
|             | capsulation | MPLSoUDP,   |             |             |
|             | protocol    | GENEVE,     |             |             |
|             | needs to    | other       |             |             |
|             | enable ECMP |             |             |             |
|             | in the      |             |             |             |
|             | underlay to |             |             |             |
|             | take        |             |             |             |
|             | advantage   |             |             |             |
|             | of the      |             |             |             |
|             | scale-out   |             |             |             |
|             | features of |             |             |             |
|             | the network |             |             |             |
|             | fabric      |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.      | Network     | Must        | Must        |             |
| net.cfg.003 | Address     | support     | support     |             |
|             | Translation |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.      | Security    | Must        | Must        |             |
| net.cfg.004 | Groups      | support     | support     |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.      | SFC support | Not         | Must        |             |
| net.cfg.005 |             | required    | support     |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.      | Traffic     | Must        | Must        |             |
| net.cfg.006 | patterns    | support     | support     |             |
|             | symmetry    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-2a: Reference Model Requirements - Virtual Networking

The required number of connection points to an instance is described in
``e.cap.004`` `above <#2.2.1>`__. The table below specifies the required
bandwidth of those connection points.

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Requirement | Requirement | Sp          |
|             |             | for Basic   | for High    | ecification |
|             |             | Profile     | Performance | Reference   |
|             |             |             | Profile     |             |
+=============+=============+=============+=============+=============+
| n1, n2, n3, | 1, 2, 3, 4, | Must        | Must        |             |
| n4, n5, n6  | 5, 6 Gbps   | support     | support     |             |
+-------------+-------------+-------------+-------------+-------------+
| n10, n20,   | 10, 20, 30, | Must        | Must        |             |
| n30, n40,   | 40, 50, 60  | support     | support     |             |
| n50, n60    | Gbps        |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| n25, n50,   | 25, 50, 75, | Optional    | Must        |             |
| n75, n100,  | 100, 125,   |             | support     |             |
| n125, n150  | 150 Gbps    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| n50, n100,  | 50, 100,    | Optional    | Must        |             |
| n150, n200, | 150, 200,   |             | support     |             |
| n250, n300  | 250, 300    |             |             |             |
|             | Gbps        |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| n100, n200, | 100, 200,   | Optional    | Must        |             |
| n300, n400, | 300, 400,   |             | support     |             |
| n500, n600  | 500, 600    |             |             |             |
|             | Gbps        |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-2b: Reference Model Requirements - Network Interface
Specifications

Cloud Infrastructure Software Profile Extensions Requirements for Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Requirement | Requirement | Sp          |
|             |             | for Basic   | for         | ecification |
|             |             | Profile     | High-       | Reference   |
|             |             |             | Performance |             |
|             |             |             | Profile     |             |
+=============+=============+=============+=============+=============+
| e.cap.013/  | SR-IOV over | N           | Y           |             |
| infra.hw.   | PCI-PT      |             |             |             |
| nac.cfg.004 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.019/  | vSwitch     | N           | Y           |             |
| infra.net.  | o           |             |             |             |
| acc.cfg.001 | ptimisation |             |             |             |
|             | (DPDK)      |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.015/  | SmartNIC    | N           | Optional    |             |
| infra.net.  | (for HW     |             |             |             |
| acc.cfg.002 | Offload)    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.009/  | Crypto      | N           | Optional    |             |
| infra.net.  | a           |             |             |             |
| acc.cfg.003 | cceleration |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.net.  | Crypto      | N           | Optional    |             |
| acc.cfg.004 | A           |             |             |             |
|             | cceleration |             |             |             |
|             | Interface   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-2c: Cloud Infrastructure Software Profile Extensions
Requirements for Networking

Cloud Infrastructure Software Profile Requirements for Storage (source `RM 5.2 <../../../ref_model/chapters/chapter05.md#5.2>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Requirement | Requirement | Sp          |
|             |             | for Basic   | for         | ecification |
|             |             | Profile     | High-       | Reference   |
|             |             |             | Performance |             |
|             |             |             | Profile     |             |
+=============+=============+=============+=============+=============+
| infra.      | Storage     | Must        | Must        |             |
| stg.cfg.002 | Block       | support     | support     |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.      | Storage     | Not         | Must        |             |
| stg.cfg.003 | with        | required    | support     |             |
|             | replication |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.      | Storage     | Must        | Must        |             |
| stg.cfg.004 | with        | support     | support     |             |
|             | encryption  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.stg.  | Storage     | Not         | Must        |             |
| acc.cfg.001 | IOPS        | required    | support     |             |
|             | oriented    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.stg.  | Storage     | Not         | Not         |             |
| acc.cfg.002 | capacity    | required    | required    |             |
|             | oriented    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-3a: Reference Model Requirements - Cloud Infrastructure Software
Profile Requirements for Storage

Cloud Infrastructure Software Profile Extensions Requirements for Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Profile     | Profile     | Sp          |
|             |             | Extensions  | Extra-Specs | ecification |
|             |             |             |             | Reference   |
+=============+=============+=============+=============+=============+
| infra.stg.  | Storage     | Storage     |             |             |
| acc.cfg.001 | IOPS        | Intensive   |             |             |
|             | oriented    | High-       |             |             |
|             |             | performance |             |             |
|             |             | storage     |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.stg.  | Storage     | High        |             |             |
| acc.cfg.002 | capacity    | Capacity    |             |             |
|             | oriented    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-3b: Reference Model Requirements - Cloud Infrastructure Software
Profile Extensions Requirements for Storage

Cloud Infrastructure Hardware Profile Requirements (source `RM 5.4 <../../../ref_model/chapters/chapter05.md#5.4>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Requirement | Requirement | Sp          |
|             |             | for Basic   | for         | ecification |
|             |             | Profile     | High-       | Reference   |
|             |             |             | Performance |             |
|             |             |             | Profile     |             |
+=============+=============+=============+=============+=============+
| i           | CPU         |             |             |             |
| nfra.hw.001 | A           |             |             |             |
|             | rchitecture |             |             |             |
|             | (Values     |             |             |             |
|             | such as     |             |             |             |
|             | x64, ARM,   |             |             |             |
|             | etc.)       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | Minimum     | 2           | 2           |             |
| cpu.cfg.001 | number of   |             |             |             |
|             | CPU         |             |             |             |
|             | (Sockets)   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | Minimum     | 20          | 20          |             |
| cpu.cfg.002 | number of   |             |             |             |
|             | Cores per   |             |             |             |
|             | CPU         |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | NUMA        | Not         | Must        |             |
| cpu.cfg.003 |             | required    | support     |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | S           | Must        | Optional    |             |
| cpu.cfg.004 | imultaneous | support     |             |             |
|             | Mu          |             |             |             |
|             | ltithreadin |             |             |             |
|             | g/Symmetric |             |             |             |
|             | Mult        |             |             |             |
|             | iprocessing |             |             |             |
|             | (SMT/SMP)   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| in          | Local       | *No         | *No         |             |
| fra.hw.stg. | Storage HDD | requirement | requirement |             |
| hdd.cfg.001 |             | specified*  | specified*  |             |
+-------------+-------------+-------------+-------------+-------------+
| in          | Local       | Should      | Should      |             |
| fra.hw.stg. | Storage SSD | support     | support     |             |
| ssd.cfg.002 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | Total       | 4           | 4           |             |
| nic.cfg.001 | Number of   |             |             |             |
|             | NIC Ports   |             |             |             |
|             | available   |             |             |             |
|             | in the host |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | Port speed  | 10          | 25          |             |
| nic.cfg.002 | specified   |             |             |             |
|             | in Gbps     |             |             |             |
|             | (minimum    |             |             |             |
|             | values)     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | Number of   | 8           | 8           |             |
| pci.cfg.001 | PCIe slots  |             |             |             |
|             | available   |             |             |             |
|             | in the host |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | PCIe speed  | Gen 3       | Gen 3       |             |
| pci.cfg.002 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | PCIe Lanes  | 8           | 8           |             |
| pci.cfg.003 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | Compression | *No         | *No         |             |
| nac.cfg.003 |             | requirement | requirement |             |
|             |             | specified*  | specified*  |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-4a: Reference Model Requirements - Cloud Infrastructure Hardware
Profile Requirements

Cloud Infrastructure Hardware Profile-Extensions Requirements (source `RM 5.4 <../../../ref_model/chapters/chapter05.md#5.4>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-------------+-------------+-------------+-------------+-------------+
| Reference   | Description | Requirement | Requirement | Sp          |
|             |             | for Basic   | for         | ecification |
|             |             | Profile     | High-       | Reference   |
|             |             |             | Performance |             |
|             |             |             | Profile     |             |
+=============+=============+=============+=============+=============+
| e.cap.014/  | GPU         | N           | Optional    |             |
| infra.hw.   |             |             |             |             |
| cac.cfg.001 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.016/  | FPGA/other  | N           | Optional    |             |
| infra.hw.   | A           |             |             |             |
| cac.cfg.002 | cceleration |             |             |             |
|             | H/W         |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.009/  | Crypto      | N           | Optional    |             |
| infra.hw.   | A           |             |             |             |
| nac.cfg.001 | cceleration |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.015/  | SmartNIC    | N           | Optional    |             |
| infra.hw.   |             |             |             |             |
| nac.cfg.002 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| infra.hw.   | Compression | Optional    | Optional    |             |
| nac.cfg.003 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| e.cap.013/  | SR-IOV over | N           | Yes         |             |
| infra.hw.   | PCI-PT      |             |             |             |
| nac.cfg.004 |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Table 2-4b: Reference Model Requirements - Cloud Infrastructure Hardware
Profile Extensions Requirements

Cloud Infrastructure Management Requirements (source `RM 4.1.5 <../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+-----------------+-----------------+-----------------+
| Reference       | Description     | Requirement     | Specification   |
|                 |                 | (common to all  | Reference       |
|                 |                 | Profiles)       |                 |
+=================+=================+=================+=================+
| e.man.001       | Capability to   | Must support    |                 |
|                 | allocate        |                 |                 |
|                 | virtual compute |                 |                 |
|                 | resources to a  |                 |                 |
|                 | workload        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| e.man.002       | Capability to   | Must support    |                 |
|                 | allocate        |                 |                 |
|                 | virtual storage |                 |                 |
|                 | resources to a  |                 |                 |
|                 | workload        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| e.man.003       | Capability to   | Must support    |                 |
|                 | allocate        |                 |                 |
|                 | virtual         |                 |                 |
|                 | networking      |                 |                 |
|                 | resources to a  |                 |                 |
|                 | workload        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| e.man.004       | Capability to   | Must support    |                 |
|                 | isolate         |                 |                 |
|                 | resources       |                 |                 |
|                 | between tenants |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| e.man.005       | Capability to   | Must support    |                 |
|                 | manage workload |                 |                 |
|                 | software images |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| e.man.006       | Capability to   | Must support    |                 |
|                 | provide         |                 |                 |
|                 | information     |                 |                 |
|                 | related to      |                 |                 |
|                 | allocated       |                 |                 |
|                 | virtualised     |                 |                 |
|                 | resources per   |                 |                 |
|                 | tenant          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| e.man.007       | Capability to   | Must support    |                 |
|                 | notify state    |                 |                 |
|                 | changes of      |                 |                 |
|                 | allocated       |                 |                 |
|                 | resources       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| e.man.008       | Capability to   | Must support    |                 |
|                 | collect and     |                 |                 |
|                 | expose          |                 |                 |
|                 | performance     |                 |                 |
|                 | information on  |                 |                 |
|                 | virtualised     |                 |                 |
|                 | resources       |                 |                 |
|                 | allocated       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| e.man.009       | Capability to   | Must support    |                 |
|                 | collect and     |                 |                 |
|                 | notify fault    |                 |                 |
|                 | information on  |                 |                 |
|                 | virtualised     |                 |                 |
|                 | resources       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

Table 2-5: Reference Model Requirements: Cloud Infrastructure Management
Requirements

Cloud Infrastructure Security Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Hardening (source `RM 7.9.1 <../../../ref_model/chapters/chapter07.md#791-system-hardening>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+---------------+---------------+------------------+
| Reference        | sub-category  | Description   | Specification    |
|                  |               |               | Reference        |
+==================+===============+===============+==================+
| sec.gen.001      | Hardening     | The Platform  | `RA-1 6.3.6      |
|                  |               | **must**      | “Security        |
|                  |               | maintain the  | LCM” <./ch       |
|                  |               | specified     | apter06.md#636-s |
|                  |               | c             | ecurity-lcm>`__, |
|                  |               | onfiguration. | `RA-1 7.2 “Cloud |
|                  |               |               | Infrastructure   |
|                  |               |               | and VIM          |
|                  |               |               | configuration    |
|                  |               |               | manageme         |
|                  |               |               | nt” <./chapter07 |
|                  |               |               | .md#72-cloud-inf |
|                  |               |               | rastructure-and- |
|                  |               |               | vim-configuratio |
|                  |               |               | n-management>`__ |
+------------------+---------------+---------------+------------------+
| sec.gen.002      | Hardening     | All systems   | `RA-1 6.3.1.3    |
|                  |               | part of Cloud | “Password        |
|                  |               | I             | policy” <./chapt |
|                  |               | nfrastructure | er06.md#6313-pas |
|                  |               | **must**      | sword-policy>`__ |
|                  |               | support       |                  |
|                  |               | password      |                  |
|                  |               | hardening as  |                  |
|                  |               | defined in    |                  |
|                  |               | `CIS Password |                  |
|                  |               | Policy        |                  |
|                  |               | Guide <https: |                  |
|                  |               | //www.cisecur |                  |
|                  |               | ity.org/white |                  |
|                  |               | -papers/cis-p |                  |
|                  |               | assword-polic |                  |
|                  |               | y-guide/>`__. |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.003      | Hardening     | All servers   | `RA-1 6.3.1.1    |
|                  |               | part of Cloud | “Server boot     |
|                  |               | I             | hardening        |
|                  |               | nfrastructure | ” <./chapter06.m |
|                  |               | **must**      | d#6311-server-bo |
|                  |               | support a     | ot-hardening>`__ |
|                  |               | root of trust |                  |
|                  |               | and secure    |                  |
|                  |               | boot.         |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.004      | Hardening     | The Operating | `RA-1 6.3.1.4    |
|                  |               | Systems of    | “Function and    |
|                  |               | all the       | Software         |
|                  |               | servers part  | ” <./chapter06.m |
|                  |               | of Cloud      | d#6314-function- |
|                  |               | I             | and-software>`__ |
|                  |               | nfrastructure |                  |
|                  |               | **must** be   |                  |
|                  |               | hardened by   |                  |
|                  |               | removing or   |                  |
|                  |               | disabling     |                  |
|                  |               | unnecessary   |                  |
|                  |               | services,     |                  |
|                  |               | applications  |                  |
|                  |               | and network   |                  |
|                  |               | protocols,    |                  |
|                  |               | configuring   |                  |
|                  |               | operating     |                  |
|                  |               | system user   |                  |
|                  |               | au            |                  |
|                  |               | thentication, |                  |
|                  |               | configuring   |                  |
|                  |               | resource      |                  |
|                  |               | controls,     |                  |
|                  |               | installing    |                  |
|                  |               | and           |                  |
|                  |               | configuring   |                  |
|                  |               | additional    |                  |
|                  |               | security      |                  |
|                  |               | controls      |                  |
|                  |               | where needed, |                  |
|                  |               | and testing   |                  |
|                  |               | the security  |                  |
|                  |               | of the        |                  |
|                  |               | Operating     |                  |
|                  |               | System (NIST  |                  |
|                  |               | SP 800-123).  |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.005      | Hardening     | The Platform  | `RA-1 6.3.1.2    |
|                  |               | **must**      | “System          |
|                  |               | support       | Access” <./cha   |
|                  |               | Operating     | pter06.md#6312-s |
|                  |               | System level  | ystem-access>`__ |
|                  |               | access        |                  |
|                  |               | control.      |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.006      | Hardening     | The Platform  | `RA-1 6.3.1.2    |
|                  |               | **must**      | “System          |
|                  |               | support       | Access” <./cha   |
|                  |               | Secure        | pter06.md#6312-s |
|                  |               | logging.      | ystem-access>`__ |
|                  |               | Logging with  |                  |
|                  |               | root account  |                  |
|                  |               | must be       |                  |
|                  |               | prohibited    |                  |
|                  |               | when root     |                  |
|                  |               | privileges    |                  |
|                  |               | are not       |                  |
|                  |               | required.     |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.007      | Hardening     | All servers   | `RA-1 6.3.7.6    |
|                  |               | part of Cloud | “Security Logs   |
|                  |               | I             | Time             |
|                  |               | nfrastructure | Synchronisat     |
|                  |               | **must** be   | ion” <./chapter0 |
|                  |               | Time          | 6.md#6376-securi |
|                  |               | synchronised  | ty-logs-time-syn |
|                  |               | with          | chronisation>`__ |
|                  |               | authenticated |                  |
|                  |               | Time service. |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.008      | Hardening     | All servers   | `RA-1 6.3.1.5    |
|                  |               | part of Cloud | “Patches” <      |
|                  |               | I             | ./chapter06.md#6 |
|                  |               | nfrastructure | 315-patches>`__, |
|                  |               | **must** be   | `RA-1 6.3.6      |
|                  |               | regularly     | “Security        |
|                  |               | updated to    | LCM” <./c        |
|                  |               | address       | hapter06.md#636- |
|                  |               | security      | security-lcm>`__ |
|                  |               | vul           |                  |
|                  |               | nerabilities. |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.009      | Hardening     | The Platform  | `RA-1 6.3.3.2    |
|                  |               | **must**      | “Integrity of    |
|                  |               | support       | OpenStack        |
|                  |               | software      | components       |
|                  |               | integrity     | configur         |
|                  |               | protection    | ation” <./chapte |
|                  |               | and           | r06.md#6332-inte |
|                  |               | verification. | grity-of-opensta |
|                  |               |               | ck-components-co |
|                  |               |               | nfiguration>`__, |
|                  |               |               | `RA-1 6.3.5      |
|                  |               |               | “Image           |
|                  |               |               | Security” <./cha |
|                  |               |               | pter06.md#635-im |
|                  |               |               | age-security>`__ |
+------------------+---------------+---------------+------------------+
| sec.gen.010      | Hardening     | The Cloud     | `RA-1 6.3.3.3    |
|                  |               | I             | “Confidentiality |
|                  |               | nfrastructure | and Integrity of |
|                  |               | **must**      | tenant           |
|                  |               | support       | dat              |
|                  |               | encrypted     | a” <./chapter06. |
|                  |               | storage, for  | md#6333-confiden |
|                  |               | example,      | tiality-and-inte |
|                  |               | block, object | grity-of-tenant- |
|                  |               | and file      | data-secmon012-a |
|                  |               | storage, with | nd-secmon013>`__ |
|                  |               | access to     |                  |
|                  |               | encryption    |                  |
|                  |               | keys          |                  |
|                  |               | restricted    |                  |
|                  |               | based on a    |                  |
|                  |               | need to know  |                  |
|                  |               | (`Controlled  |                  |
|                  |               | Access Based  |                  |
|                  |               | on the Need   |                  |
|                  |               | to            |                  |
|                  |               | K             |                  |
|                  |               | now <https:// |                  |
|                  |               | www.cisecurit |                  |
|                  |               | y.org/control |                  |
|                  |               | s/controlled- |                  |
|                  |               | access-based- |                  |
|                  |               | on-the-need-t |                  |
|                  |               | o-know/>`__). |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.012      | Hardening     | The Operator  | This             |
|                  |               | **must**      | requirement’s    |
|                  |               | ensure that   | verification     |
|                  |               | only          | goes beyond      |
|                  |               | authorised    | Anuket testing   |
|                  |               | actors have   | scope            |
|                  |               | physical      |                  |
|                  |               | access to the |                  |
|                  |               | underlying    |                  |
|                  |               | in            |                  |
|                  |               | frastructure. |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.013      | Hardening     | The Platform  | `RA-1 6.3.1.2    |
|                  |               | **must**      | “System          |
|                  |               | ensure that   | Access” <./cha   |
|                  |               | only          | pter06.md#6312-s |
|                  |               | authorised    | ystem-access>`__ |
|                  |               | actors have   |                  |
|                  |               | logical       |                  |
|                  |               | access to the |                  |
|                  |               | underlying    |                  |
|                  |               | in            |                  |
|                  |               | frastructure. |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.015      | Hardening     | Any change to | `RA-1 6.3.6      |
|                  |               | the Platform  | “Security        |
|                  |               | **must** be   | LCM” <./c        |
|                  |               | logged as a   | hapter06.md#636- |
|                  |               | security      | security-lcm>`__ |
|                  |               | event, and    |                  |
|                  |               | the logged    |                  |
|                  |               | event must    |                  |
|                  |               | include the   |                  |
|                  |               | identity of   |                  |
|                  |               | the entity    |                  |
|                  |               | making the    |                  |
|                  |               | change, the   |                  |
|                  |               | change, the   |                  |
|                  |               | date and the  |                  |
|                  |               | time of the   |                  |
|                  |               | change.       |                  |
+------------------+---------------+---------------+------------------+

Table 2-6: Reference Model Requirements - System Hardening Requirements

Platform and Access (source `RM 7.9.2 <../../../ref_model/chapters/chapter07.md#792-platform-and-access>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+---------------+---------------+--------------------+
| Reference     | sub-category  | Description   | Specification      |
|               |               |               | Reference          |
+===============+===============+===============+====================+
| sec.sys.001   | Access        | The Platform  | `RA-1 6.3.2.4      |
|               |               | **must**      | “RBAC” <./chapter0 |
|               |               | support       | 6.md#6324-rbac>`__ |
|               |               | authenticated |                    |
|               |               | and secure    |                    |
|               |               | access to     |                    |
|               |               | API, GUI and  |                    |
|               |               | command line  |                    |
|               |               | interfaces    |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.002   | Access        | The Platform  | `RA-1 6.3.4        |
|               |               | **must**      | “Workload          |
|               |               | support       | Security” <./ch    |
|               |               | Traffic       | apter06.md#634-wor |
|               |               | Filtering for | kload-security>`__ |
|               |               | workloads     |                    |
|               |               | (for example, |                    |
|               |               | Firewall).    |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.003   | Access        | The Platform  | `RA-1 6.3.3.1      |
|               |               | **must**      | “Confidentiality   |
|               |               | support       | and Integrity of   |
|               |               | Secure and    | communications”    |
|               |               | encrypted     | <./chapter06.md#63 |
|               |               | co            | 31-confidentiality |
|               |               | mmunications, | -and-integrity-of- |
|               |               | and           | communications>`__ |
|               |               | co            |                    |
|               |               | nfidentiality |                    |
|               |               | and integrity |                    |
|               |               | of network    |                    |
|               |               | traffic.      |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.004   | Access        | The Cloud     | `RA-1 6.3.3.1      |
|               |               | I             | “Confidentiality   |
|               |               | nfrastructure | and Integrity of   |
|               |               | **must**      | communications”    |
|               |               | support       | <./chapter06.md#63 |
|               |               | au            | 31-confidentiality |
|               |               | thentication, | -and-integrity-of- |
|               |               | integrity and | communications>`__ |
|               |               | co            |                    |
|               |               | nfidentiality |                    |
|               |               | on all        |                    |
|               |               | network       |                    |
|               |               | channels.     |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.005   | Access        | The Cloud     | `RA-1 6.3.3.1      |
|               |               | I             | “Confidentiality   |
|               |               | nfrastructure | and Integrity of   |
|               |               | **must**      | communications”    |
|               |               | segregate the | <./chapter06.md#63 |
|               |               | underlay and  | 31-confidentiality |
|               |               | overlay       | -and-integrity-of- |
|               |               | networks.     | communications>`__ |
+---------------+---------------+---------------+--------------------+
| sec.sys.006   | Access        | The Cloud     | `RA-1 6.3.2.1      |
|               |               | I             | “Identity          |
|               |               | nfrastructure | Security” <./cha   |
|               |               | **must** be   | pter06.md#6321-ide |
|               |               | able to       | ntity-security>`__ |
|               |               | utilise the   |                    |
|               |               | Cloud         |                    |
|               |               | I             |                    |
|               |               | nfrastructure |                    |
|               |               | Manager       |                    |
|               |               | identity      |                    |
|               |               | lifecycle     |                    |
|               |               | management    |                    |
|               |               | capabilities. |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.007   | Access        | The Platform  | `RA-1 6.3.2.4      |
|               |               | **must**      | “RBAC” <./chapter0 |
|               |               | implement     | 6.md#6324-rbac>`__ |
|               |               | controls      |                    |
|               |               | enforcing     |                    |
|               |               | separation of |                    |
|               |               | duties and    |                    |
|               |               | privileges,   |                    |
|               |               | least         |                    |
|               |               | privilege use |                    |
|               |               | and least     |                    |
|               |               | common        |                    |
|               |               | mechanism     |                    |
|               |               | (Role-Based   |                    |
|               |               | Access        |                    |
|               |               | Control).     |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.008   | Access        | The Platform  | `RA-1 6.3.4        |
|               |               | **must** be   | “Workload          |
|               |               | able to       | Security” <./ch    |
|               |               | assign the    | apter06.md#634-wor |
|               |               | Entities that | kload-security>`__ |
|               |               | comprise the  |                    |
|               |               | tenant        |                    |
|               |               | networks to   |                    |
|               |               | different     |                    |
|               |               | trust         |                    |
|               |               | domains.      |                    |
|               |               | (             |                    |
|               |               | Communication |                    |
|               |               | between       |                    |
|               |               | different     |                    |
|               |               | trust domains |                    |
|               |               | is not        |                    |
|               |               | allowed, by   |                    |
|               |               | default.)     |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.009   | Access        | The Platform  |                    |
|               |               | **must**      |                    |
|               |               | support       |                    |
|               |               | creation of   |                    |
|               |               | Trust         |                    |
|               |               | Relationships |                    |
|               |               | between trust |                    |
|               |               | domains.      |                    |
|               |               | These maybe   |                    |
|               |               | un            |                    |
|               |               | i-directional |                    |
|               |               | relationships |                    |
|               |               | where the     |                    |
|               |               | trusting      |                    |
|               |               | domain trusts |                    |
|               |               | another       |                    |
|               |               | domain (the   |                    |
|               |               | “trusted      |                    |
|               |               | domain”) to   |                    |
|               |               | authenticate  |                    |
|               |               | users for     |                    |
|               |               | them or to    |                    |
|               |               | allow access  |                    |
|               |               | to its        |                    |
|               |               | resources     |                    |
|               |               | from the      |                    |
|               |               | trusted       |                    |
|               |               | domain. In a  |                    |
|               |               | bidirectional |                    |
|               |               | relationship  |                    |
|               |               | both domain   |                    |
|               |               | are           |                    |
|               |               | “trusting”    |                    |
|               |               | and           |                    |
|               |               | “trusted”.    |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.010   | Access        | For two or    |                    |
|               |               | more domains  |                    |
|               |               | without       |                    |
|               |               | existing      |                    |
|               |               | trust         |                    |
|               |               | r             |                    |
|               |               | elationships, |                    |
|               |               | the Platform  |                    |
|               |               | **must not**  |                    |
|               |               | allow the     |                    |
|               |               | effect of an  |                    |
|               |               | attack on one |                    |
|               |               | domain to     |                    |
|               |               | impact the    |                    |
|               |               | other domains |                    |
|               |               | either        |                    |
|               |               | directly or   |                    |
|               |               | indirectly.   |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.011   | Access        | The Platform  | `RA-1 6.3.1.2      |
|               |               | **must not**  | “System            |
|               |               | reuse the     | Access” <.         |
|               |               | same          | /chapter06.md#6312 |
|               |               | a             | -system-access>`__ |
|               |               | uthentication |                    |
|               |               | credentials   |                    |
|               |               | (e.g., key    |                    |
|               |               | pairs) on     |                    |
|               |               | different     |                    |
|               |               | Platform      |                    |
|               |               | components    |                    |
|               |               | (e.g.,        |                    |
|               |               | different     |                    |
|               |               | hosts, or     |                    |
|               |               | different     |                    |
|               |               | services).    |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.012   | Access        | The Platform  |                    |
|               |               | **must**      |                    |
|               |               | protect all   |                    |
|               |               | secrets by    |                    |
|               |               | using strong  |                    |
|               |               | encryption    |                    |
|               |               | techniques    |                    |
|               |               | and storing   |                    |
|               |               | the protected |                    |
|               |               | secrets       |                    |
|               |               | externally    |                    |
|               |               | from the      |                    |
|               |               | component     |                    |
|               |               | (e.g., in     |                    |
|               |               | OpenStack     |                    |
|               |               | Barbican)     |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.013   | Access        | The Platform  |                    |
|               |               | **must**      |                    |
|               |               | generate      |                    |
|               |               | secrets       |                    |
|               |               | dynamically   |                    |
|               |               | as and when   |                    |
|               |               | needed.       |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.015   | Access        | The Platform  |                    |
|               |               | **must not**  |                    |
|               |               | contain back  |                    |
|               |               | door entries  |                    |
|               |               | (unpublished  |                    |
|               |               | access        |                    |
|               |               | points, APIs, |                    |
|               |               | etc.).        |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.016   | Access        | Login access  | `RA-1 6.3.6        |
|               |               | to the        | “Security          |
|               |               | Platform’s    | LCM”               |
|               |               | components    | <./chapter06.md#63 |
|               |               | **must** be   | 6-security-lcm>`__ |
|               |               | through       |                    |
|               |               | encrypted     |                    |
|               |               | protocols     |                    |
|               |               | such as SSH   |                    |
|               |               | v2 or TLS     |                    |
|               |               | v1.2 or       |                    |
|               |               | higher. Note: |                    |
|               |               | Hardened jump |                    |
|               |               | servers       |                    |
|               |               | isolated from |                    |
|               |               | external      |                    |
|               |               | networks are  |                    |
|               |               | recommended   |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.017   | Access        | The Platform  | `RA-1 6.3.3.1      |
|               |               | **must**      | “Confidentiality   |
|               |               | provide the   | and Integrity of   |
|               |               | capability of | communications”    |
|               |               | using digital | <./chapter06.md#63 |
|               |               | certificates  | 31-confidentiality |
|               |               | that comply   | -and-integrity-of- |
|               |               | with X.509    | communications>`__ |
|               |               | standards     |                    |
|               |               | issued by a   |                    |
|               |               | trusted       |                    |
|               |               | Certification |                    |
|               |               | Authority.    |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.018   | Access        | The Platform  |                    |
|               |               | **must**      |                    |
|               |               | provide the   |                    |
|               |               | capability of |                    |
|               |               | allowing      |                    |
|               |               | certificate   |                    |
|               |               | renewal and   |                    |
|               |               | revocation.   |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.019   | Access        | The Platform  |                    |
|               |               | **must**      |                    |
|               |               | provide the   |                    |
|               |               | capability of |                    |
|               |               | testing the   |                    |
|               |               | validity of a |                    |
|               |               | digital       |                    |
|               |               | certificate   |                    |
|               |               | (CA           |                    |
|               |               | signature,    |                    |
|               |               | validity      |                    |
|               |               | period, non   |                    |
|               |               | revocation,   |                    |
|               |               | identity).    |                    |
+---------------+---------------+---------------+--------------------+

Table 2-7: Reference Model Requirements - Platform and Access
Requirements

Confidentiality and Integrity (source `RM 7.9.3 <../../../ref_model/chapters/chapter07.md#793-confidentiality-and-integrity>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Specification     |
|              |                   |              | Reference         |
+==============+===================+==============+===================+
| sec.ci.001   | Confiden          | The Platform | `RA-1 6.3.3       |
|              | tiality/Integrity | **must**     | “Confidentiality  |
|              |                   | support      | and               |
|              |                   | Con          | Integrity” <.     |
|              |                   | fidentiality | /chapter06.md#633 |
|              |                   | and          | -confidentiality- |
|              |                   | Integrity of | and-integrity>`__ |
|              |                   | data at rest |                   |
|              |                   | and in       |                   |
|              |                   | transit.     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.ci.003   | Confiden          | The Platform |                   |
|              | tiality/Integrity | **must**     |                   |
|              |                   | support      |                   |
|              |                   | Con          |                   |
|              |                   | fidentiality |                   |
|              |                   | and          |                   |
|              |                   | Integrity of |                   |
|              |                   | data related |                   |
|              |                   | metadata.    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.ci.004   | Confidentiality   | The Platform |                   |
|              |                   | **must**     |                   |
|              |                   | support      |                   |
|              |                   | Con          |                   |
|              |                   | fidentiality |                   |
|              |                   | of processes |                   |
|              |                   | and restrict |                   |
|              |                   | information  |                   |
|              |                   | sharing with |                   |
|              |                   | only the     |                   |
|              |                   | process      |                   |
|              |                   | owner (e.g., |                   |
|              |                   | tenant).     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.ci.005   | Confiden          | The Platform |                   |
|              | tiality/Integrity | **must**     |                   |
|              |                   | support      |                   |
|              |                   | Con          |                   |
|              |                   | fidentiality |                   |
|              |                   | and          |                   |
|              |                   | Integrity of |                   |
|              |                   | pro          |                   |
|              |                   | cess-related |                   |
|              |                   | metadata and |                   |
|              |                   | restrict     |                   |
|              |                   | information  |                   |
|              |                   | sharing with |                   |
|              |                   | only the     |                   |
|              |                   | process      |                   |
|              |                   | owner (e.g., |                   |
|              |                   | tenant).     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.ci.006   | Confiden          | The Platform |                   |
|              | tiality/Integrity | **must**     |                   |
|              |                   | support      |                   |
|              |                   | Con          |                   |
|              |                   | fidentiality |                   |
|              |                   | and          |                   |
|              |                   | Integrity of |                   |
|              |                   | workload     |                   |
|              |                   | resource     |                   |
|              |                   | utilisation  |                   |
|              |                   | (RAM, CPU,   |                   |
|              |                   | Storage,     |                   |
|              |                   | Network I/O, |                   |
|              |                   | cache,       |                   |
|              |                   | hardware     |                   |
|              |                   | offload) and |                   |
|              |                   | restrict     |                   |
|              |                   | information  |                   |
|              |                   | sharing with |                   |
|              |                   | only the     |                   |
|              |                   | workload     |                   |
|              |                   | owner (e.g., |                   |
|              |                   | tenant).     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.ci.007   | Confiden          | The Platform |                   |
|              | tiality/Integrity | **must not** |                   |
|              |                   | allow Memory |                   |
|              |                   | Inspection   |                   |
|              |                   | by any actor |                   |
|              |                   | other than   |                   |
|              |                   | the          |                   |
|              |                   | authorised   |                   |
|              |                   | actors for   |                   |
|              |                   | the Entity   |                   |
|              |                   | to which     |                   |
|              |                   | Memory is    |                   |
|              |                   | assigned     |                   |
|              |                   | (e.g.,       |                   |
|              |                   | tenants      |                   |
|              |                   | owning the   |                   |
|              |                   | workload),   |                   |
|              |                   | for Lawful   |                   |
|              |                   | Inspection,  |                   |
|              |                   | and for      |                   |
|              |                   | secure       |                   |
|              |                   | monitoring   |                   |
|              |                   | services.    |                   |
|              |                   | Ad           |                   |
|              |                   | ministrative |                   |
|              |                   | access must  |                   |
|              |                   | be managed   |                   |
|              |                   | using        |                   |
|              |                   | Platform     |                   |
|              |                   | Identity     |                   |
|              |                   | Lifecycle    |                   |
|              |                   | Management.  |                   |
+--------------+-------------------+--------------+-------------------+
| sec.ci.008   | Confidentiality   | The Cloud    | `RA-1 6.3.4       |
|              |                   | In           | “Workload         |
|              |                   | frastructure | Security” <./chap |
|              |                   | **must**     | ter06.md#634-work |
|              |                   | support      | load-security>`__ |
|              |                   | tenant       |                   |
|              |                   | networks     |                   |
|              |                   | segregation. |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-8: Reference Model Requirements: Confidentiality and Integrity
Requirements

Workload Security (source `RM 7.9.4 <../../../ref_model/chapters/chapter07.md#794-workload-security>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Specification     |
|              |                   |              | Reference         |
+==============+===================+==============+===================+
| sec.wl.001   | Workload          | The Platform | `RA-1 6.3.4       |
|              |                   | **must**     | “Workload         |
|              |                   | support      | Security” <./chap |
|              |                   | Workload     | ter06.md#634-work |
|              |                   | placement    | load-security>`__ |
|              |                   | policy.      |                   |
+--------------+-------------------+--------------+-------------------+
| sec.wl.002   | Workload          | The Cloud    |                   |
|              |                   | In           |                   |
|              |                   | frastructure |                   |
|              |                   | **must**     |                   |
|              |                   | provide      |                   |
|              |                   | methods to   |                   |
|              |                   | ensure the   |                   |
|              |                   | platform’s   |                   |
|              |                   | trust status |                   |
|              |                   | and          |                   |
|              |                   | integrity    |                   |
|              |                   | (e.g.,       |                   |
|              |                   | remote       |                   |
|              |                   | attestation, |                   |
|              |                   | Trusted      |                   |
|              |                   | Platform     |                   |
|              |                   | Module).     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.wl.003   | Workload          | The Platform | `RA-1 6.3.4       |
|              |                   | **must**     | “Workload         |
|              |                   | support      | Security” <./chap |
|              |                   | secure       | ter06.md#634-work |
|              |                   | provisioning | load-security>`__ |
|              |                   | of           |                   |
|              |                   | Workloads.   |                   |
+--------------+-------------------+--------------+-------------------+
| sec.wl.004   | Workload          | The Platform | `RA-1 6.3.4       |
|              |                   | **must**     | “Workload         |
|              |                   | support      | Security” <./chap |
|              |                   | Location     | ter06.md#634-work |
|              |                   | assertion    | load-security>`__ |
|              |                   | (for         |                   |
|              |                   | mandated     |                   |
|              |                   | in-country   |                   |
|              |                   | or location  |                   |
|              |                   | re           |                   |
|              |                   | quirements). |                   |
+--------------+-------------------+--------------+-------------------+
| sec.wl.005   | Workload          | The Platform | This              |
|              |                   | **must**     | requirement’s     |
|              |                   | support the  | verification goes |
|              |                   | separation   | beyond Anuket     |
|              |                   | of           | testing scope     |
|              |                   | production   |                   |
|              |                   | and          |                   |
|              |                   | no           |                   |
|              |                   | n-production |                   |
|              |                   | Workloads.   |                   |
+--------------+-------------------+--------------+-------------------+
| sec.wl.006   | Workload          | The Platform | `RA-1 6.3.4       |
|              |                   | **must**     | “Workload         |
|              |                   | support the  | Security” <./chap |
|              |                   | separation   | ter06.md#634-work |
|              |                   | of Workloads | load-security>`__ |
|              |                   | based on     |                   |
|              |                   | their        |                   |
|              |                   | ca           |                   |
|              |                   | tegorisation |                   |
|              |                   | (for         |                   |
|              |                   | example,     |                   |
|              |                   | payment card |                   |
|              |                   | information, |                   |
|              |                   | healthcare,  |                   |
|              |                   | etc.)        |                   |
+--------------+-------------------+--------------+-------------------+
| sec.wl.007   | Workload          | The Operator |                   |
|              |                   | **must**     |                   |
|              |                   | implement    |                   |
|              |                   | processes    |                   |
|              |                   | and tools to |                   |
|              |                   | verify NF    |                   |
|              |                   | authenticity |                   |
|              |                   | and          |                   |
|              |                   | integrity.   |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-9: Reference Model Requirements - Workload Security Requirements

Image Security (source `RM 7.9.5 <../../../ref_model/chapters/chapter07.md#795-image-security>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Specification     |
|              |                   |              | Reference         |
+==============+===================+==============+===================+
| sec.img.001  | Image             | Images from  | `RA-1 6.3.5       |
|              |                   | untrusted    | “Image            |
|              |                   | sources      | Security” <./c    |
|              |                   | **must not** | hapter06.md#635-i |
|              |                   | be used.     | mage-security>`__ |
+--------------+-------------------+--------------+-------------------+
| sec.img.002  | Image             | Images       | `RA-1 6.3.5       |
|              |                   | **must** be  | “Image            |
|              |                   | scanned to   | Security” <./c    |
|              |                   | be           | hapter06.md#635-i |
|              |                   | maintained   | mage-security>`__ |
|              |                   | free from    |                   |
|              |                   | known        |                   |
|              |                   | vuln         |                   |
|              |                   | erabilities. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.img.003  | Image             | Images       |                   |
|              |                   | **must not** |                   |
|              |                   | be           |                   |
|              |                   | configured   |                   |
|              |                   | to run with  |                   |
|              |                   | privileges   |                   |
|              |                   | higher than  |                   |
|              |                   | the          |                   |
|              |                   | privileges   |                   |
|              |                   | of the actor |                   |
|              |                   | authorised   |                   |
|              |                   | to run them. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.img.004  | Image             | Images       | `RA-1 6.3.3.2     |
|              |                   | **must**     | “Confidentiality  |
|              |                   | only be      | and Integrity of  |
|              |                   | accessible   | com               |
|              |                   | to           | munications” <./c |
|              |                   | authorised   | hapter06.md#6332- |
|              |                   | actors.      | integrity-of-open |
|              |                   |              | stack-components- |
|              |                   |              | configuration>`__ |
+--------------+-------------------+--------------+-------------------+
| sec.img.005  | Image             | Image        | `RA-1 6.3.3.2     |
|              |                   | Registries   | “Confidentiality  |
|              |                   | **must**     | and Integrity of  |
|              |                   | only be      | com               |
|              |                   | accessible   | munications” <./c |
|              |                   | to           | hapter06.md#6332- |
|              |                   | authorised   | integrity-of-open |
|              |                   | actors.      | stack-components- |
|              |                   |              | configuration>`__ |
+--------------+-------------------+--------------+-------------------+
| sec.img.006  | Image             | Image        | `RA-1 6.3.3.2     |
|              |                   | Registries   | “Confidentiality  |
|              |                   | **must**     | and Integrity of  |
|              |                   | only be      | com               |
|              |                   | accessible   | munications” <./c |
|              |                   | over         | hapter06.md#6332- |
|              |                   | networks     | integrity-of-open |
|              |                   | that enforce | stack-components- |
|              |                   | aut          | configuration>`__ |
|              |                   | hentication, |                   |
|              |                   | integrity    |                   |
|              |                   | and          |                   |
|              |                   | conf         |                   |
|              |                   | identiality. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.img.007  | Image             | Image        | `RA-1 6.3.3.2     |
|              |                   | registries   | “Confidentiality  |
|              |                   | **must** be  | and Integrity of  |
|              |                   | clear of     | comm              |
|              |                   | vulnerable   | unications” <./ch |
|              |                   | and out of   | apter06.md#6332-i |
|              |                   | date         | ntegrity-of-opens |
|              |                   | versions.    | tack-components-c |
|              |                   |              | onfiguration>`__, |
|              |                   |              | `RA-1 6.3.5       |
|              |                   |              | “Image            |
|              |                   |              | Security” <./c    |
|              |                   |              | hapter06.md#635-i |
|              |                   |              | mage-security>`__ |
+--------------+-------------------+--------------+-------------------+
| sec.img.008  | Image             | Images       |                   |
|              |                   | **must not** |                   |
|              |                   | include any  |                   |
|              |                   | secrets.     |                   |
|              |                   | Secrets      |                   |
|              |                   | include      |                   |
|              |                   | passwords,   |                   |
|              |                   | cloud        |                   |
|              |                   | provider     |                   |
|              |                   | credentials, |                   |
|              |                   | SSH keys,    |                   |
|              |                   | TLS          |                   |
|              |                   | certificate  |                   |
|              |                   | keys, etc.   |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-10: Reference Model Requirements - Image Security Requirements

Security LCM (source `RM 7.9.6 <../../../ref_model/chapters/chapter07.md#796-security-lcm>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Specification     |
|              |                   |              | Reference         |
+==============+===================+==============+===================+
| sec.lcm.001  | LCM               | The Platform | `RA-1 6.3.7       |
|              |                   | **must**     | “Monitoring and   |
|              |                   | support      | Security          |
|              |                   | Secure       | Audit” <.         |
|              |                   | P            | /chapter06.md#637 |
|              |                   | rovisioning, | -monitoring-and-s |
|              |                   | A            | ecurity-audit>`__ |
|              |                   | vailability, |                   |
|              |                   | and          |                   |
|              |                   | De           |                   |
|              |                   | provisioning |                   |
|              |                   | (Secure      |                   |
|              |                   | Clean-Up) of |                   |
|              |                   | workload     |                   |
|              |                   | resources    |                   |
|              |                   | where Secure |                   |
|              |                   | Clean-Up     |                   |
|              |                   | includes     |                   |
|              |                   | tear-down,   |                   |
|              |                   | defense      |                   |
|              |                   | against      |                   |
|              |                   | virus or     |                   |
|              |                   | other        |                   |
|              |                   | attacks.     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.002  | LCM               | The Cloud    | `RA-1 6.3.6       |
|              |                   | Operator     | “Security         |
|              |                   | **must** use | LCM” <.           |
|              |                   | management   | /chapter06.md#636 |
|              |                   | protocols    | -security-lcm>`__ |
|              |                   | limiting     |                   |
|              |                   | security     |                   |
|              |                   | risk such as |                   |
|              |                   | SNMPv3, SSH  |                   |
|              |                   | v2, ICMP,    |                   |
|              |                   | NTP, syslog  |                   |
|              |                   | and TLS v1.2 |                   |
|              |                   | or higher.   |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.003  | LCM               | The Cloud    | `RA-1 6.3.7       |
|              |                   | Operator     | “Monitoring and   |
|              |                   | **must**     | Security          |
|              |                   | implement    | Audit” <.         |
|              |                   | and strictly | /chapter06.md#637 |
|              |                   | follow       | -monitoring-and-s |
|              |                   | change       | ecurity-audit>`__ |
|              |                   | management   |                   |
|              |                   | processes    |                   |
|              |                   | for Cloud    |                   |
|              |                   | Inf          |                   |
|              |                   | rastructure, |                   |
|              |                   | Cloud        |                   |
|              |                   | In           |                   |
|              |                   | frastructure |                   |
|              |                   | Manager and  |                   |
|              |                   | other        |                   |
|              |                   | components   |                   |
|              |                   | of the       |                   |
|              |                   | cloud, and   |                   |
|              |                   | Platform     |                   |
|              |                   | change       |                   |
|              |                   | control on   |                   |
|              |                   | hardware.    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.005  | LCM               | Platform     | `RA-1 6.3.7       |
|              |                   | **must**     | “Monitoring and   |
|              |                   | provide logs | Security          |
|              |                   | and these    | Audit” <.         |
|              |                   | logs must be | /chapter06.md#637 |
|              |                   | monitored    | -monitoring-and-s |
|              |                   | for          | ecurity-audit>`__ |
|              |                   | anomalous    |                   |
|              |                   | behaviour.   |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.006  | LCM               | The Platform | `RA-1 6.3.3.3     |
|              |                   | **must**     | “Confidentiality  |
|              |                   | verify the   | and Integrity of  |
|              |                   | integrity of | tenant            |
|              |                   | all Resource | data” <./chapt    |
|              |                   | management   | er06.md#6333-conf |
|              |                   | requests.    | identiality-and-i |
|              |                   |              | ntegrity-of-tenan |
|              |                   |              | t-data-secmon012- |
|              |                   |              | and-secmon013>`__ |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.007  | LCM               | The Platform |                   |
|              |                   | **must** be  |                   |
|              |                   | able to      |                   |
|              |                   | update newly |                   |
|              |                   | i            |                   |
|              |                   | nstantiated, |                   |
|              |                   | suspended,   |                   |
|              |                   | hibernated,  |                   |
|              |                   | migrated and |                   |
|              |                   | restarted    |                   |
|              |                   | images with  |                   |
|              |                   | current time |                   |
|              |                   | information. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.008  | LCM               | The Platform |                   |
|              |                   | **must** be  |                   |
|              |                   | able to      |                   |
|              |                   | update newly |                   |
|              |                   | i            |                   |
|              |                   | nstantiated, |                   |
|              |                   | suspended,   |                   |
|              |                   | hibernated,  |                   |
|              |                   | migrated and |                   |
|              |                   | restarted    |                   |
|              |                   | images with  |                   |
|              |                   | relevant DNS |                   |
|              |                   | information. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.009  | LCM               | The Platform |                   |
|              |                   | **must** be  |                   |
|              |                   | able to      |                   |
|              |                   | update the   |                   |
|              |                   | tag of newly |                   |
|              |                   | i            |                   |
|              |                   | nstantiated, |                   |
|              |                   | suspended,   |                   |
|              |                   | hibernated,  |                   |
|              |                   | migrated and |                   |
|              |                   | restarted    |                   |
|              |                   | images with  |                   |
|              |                   | relevant     |                   |
|              |                   | geolocation  |                   |
|              |                   | (g           |                   |
|              |                   | eographical) |                   |
|              |                   | information. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.010  | LCM               | The Platform |                   |
|              |                   | **must** log |                   |
|              |                   | all changes  |                   |
|              |                   | to           |                   |
|              |                   | geolocation  |                   |
|              |                   | along with   |                   |
|              |                   | the          |                   |
|              |                   | mechanisms   |                   |
|              |                   | and sources  |                   |
|              |                   | of location  |                   |
|              |                   | information  |                   |
|              |                   | (i.e. GPS,   |                   |
|              |                   | IP block,    |                   |
|              |                   | and timing). |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.011  | LCM               | The Platform | `RA-1 6.3.1.5     |
|              |                   | **must**     | “Patches          |
|              |                   | implement    | ” <./chapter06.md |
|              |                   | Security     | #6315-patches>`__ |
|              |                   | life cycle   |                   |
|              |                   | management   |                   |
|              |                   | processes    |                   |
|              |                   | including    |                   |
|              |                   | the          |                   |
|              |                   | proactive    |                   |
|              |                   | update and   |                   |
|              |                   | patching of  |                   |
|              |                   | all deployed |                   |
|              |                   | Cloud        |                   |
|              |                   | In           |                   |
|              |                   | frastructure |                   |
|              |                   | software.    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.lcm.012  | LCM               | The Platform | `RA-1 6.3.7.2     |
|              |                   | **must** log | “What to          |
|              |                   | any access   | Log” <.           |
|              |                   | privilege    | /chapter06.md#637 |
|              |                   | escalation.  | 2-what-to-log--wh |
|              |                   |              | at-not-to-log>`__ |
+--------------+-------------------+--------------+-------------------+

Table 2-11: Reference Model Requirements - Security LCM Requirements

Monitoring and Security Audit (source `RM 7.9.7 <../../../ref_model/chapters/chapter07.md#797-monitoring-and-security-audit>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Platform is assumed to provide configurable alerting and
notification capability and the operator is assumed to have automated
systems, policies and procedures to act on alerts and notifications in a
timely fashion. In the following the monitoring and logging capabilities
can trigger alerts and notifications for appropriate action.

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Specification     |
|              |                   |              | Reference         |
+==============+===================+==============+===================+
| sec.mon.001  | Monitoring/Audit  | Platform     | `RA-1 6.3.7.1     |
|              |                   | **must**     | “Creating         |
|              |                   | provide logs | logs” <./ch       |
|              |                   | and these    | apter06.md#6371-c |
|              |                   | logs must be | reating-logs>`__, |
|              |                   | regularly    | `RA-1 6.3.7.4     |
|              |                   | monitored    | “Required         |
|              |                   | for events   | Fields” <./cha    |
|              |                   | of interest. | pter06.md#6374-re |
|              |                   | The logs     | quired-fields>`__ |
|              |                   | **must**     |                   |
|              |                   | contain the  |                   |
|              |                   | following    |                   |
|              |                   | fields:      |                   |
|              |                   | event type,  |                   |
|              |                   | date/time,   |                   |
|              |                   | protocol,    |                   |
|              |                   | service or   |                   |
|              |                   | program used |                   |
|              |                   | for access,  |                   |
|              |                   | succ         |                   |
|              |                   | ess/failure, |                   |
|              |                   | login ID or  |                   |
|              |                   | process ID,  |                   |
|              |                   | IP address   |                   |
|              |                   | and ports    |                   |
|              |                   | (source and  |                   |
|              |                   | destination) |                   |
|              |                   | involved.    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.002  | Monitoring        | Security     | `RA-1 6.3.7.6     |
|              |                   | logs         | “Security Logs    |
|              |                   | **must** be  | Time              |
|              |                   | time         | Synchron          |
|              |                   | s            | isation” <./chapt |
|              |                   | ynchronised. | er06.md#6376-secu |
|              |                   |              | rity-logs-time-sy |
|              |                   |              | nchronisation>`__ |
+--------------+-------------------+--------------+-------------------+
| sec.mon.003  | Monitoring        | The Platform | `RA-1 6.3.7.6     |
|              |                   | **must** log | “Security Logs    |
|              |                   | all changes  | Time              |
|              |                   | to time      | Synchron          |
|              |                   | server       | isation” <./chapt |
|              |                   | source,      | er06.md#6376-secu |
|              |                   | time, date   | rity-logs-time-sy |
|              |                   | and time     | nchronisation>`__ |
|              |                   | zones.       |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.004  | Audit             | The Platform | `RA-1 6.3.6       |
|              |                   | **must**     | “Security         |
|              |                   | secure and   | LCM” <.           |
|              |                   | protect      | /chapter06.md#636 |
|              |                   | Audit logs   | -security-lcm>`__ |
|              |                   | (containing  |                   |
|              |                   | sensitive    |                   |
|              |                   | information) |                   |
|              |                   | both         |                   |
|              |                   | in-transit   |                   |
|              |                   | and at rest. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.005  | Monitoring/Audit  | The Platform | `RA-1 6.3.3.2     |
|              |                   | **must**     | “Confidentiality  |
|              |                   | Monitor and  | and Integrity of  |
|              |                   | Audit        | comm              |
|              |                   | various      | unications” <./ch |
|              |                   | behaviours   | apter06.md#6332-i |
|              |                   | of           | ntegrity-of-opens |
|              |                   | connection   | tack-components-c |
|              |                   | and login    | onfiguration>`__, |
|              |                   | attempts to  | `RA-1 6.3.7.2     |
|              |                   | detect       | “What to log,     |
|              |                   | access       | what not to       |
|              |                   | attacks and  | log” <.           |
|              |                   | potential    | /chapter06.md#637 |
|              |                   | access       | 2-what-to-log--wh |
|              |                   | attempts and | at-not-to-log>`__ |
|              |                   | take         |                   |
|              |                   | corrective   |                   |
|              |                   | actions      |                   |
|              |                   | accordingly  |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.006  | Monitoring/Audit  | The Platform | `RA-1 6.3.3.2     |
|              |                   | **must**     | “Integrity of     |
|              |                   | Monitor and  | OpenStack         |
|              |                   | Audit        | components        |
|              |                   | operations   | con               |
|              |                   | by           | figuration” <./ch |
|              |                   | authorised   | apter06.md#6332-i |
|              |                   | account      | ntegrity-of-opens |
|              |                   | access after | tack-components-c |
|              |                   | login to     | onfiguration>`__, |
|              |                   | detect       | `RA-1 6.3.7       |
|              |                   | malicious    | “Monitoring and   |
|              |                   | operational  | Security          |
|              |                   | activity and | Audit” <.         |
|              |                   | take         | /chapter06.md#637 |
|              |                   | corrective   | -monitoring-and-s |
|              |                   | actions.     | ecurity-audit>`__ |
+--------------+-------------------+--------------+-------------------+
| sec.mon.007  | Monitoring/Audit  | The Platform | `RA-1 6.3.3.2     |
|              |                   | **must**     | “Integrity of     |
|              |                   | Monitor and  | OpenStack         |
|              |                   | Audit        | components        |
|              |                   | security     | co                |
|              |                   | parameter    | nfiguration” <./c |
|              |                   | co           | hapter06.md#6332- |
|              |                   | nfigurations | integrity-of-open |
|              |                   | for          | stack-components- |
|              |                   | compliance   | configuration>`__ |
|              |                   | with defined |                   |
|              |                   | security     |                   |
|              |                   | policies.    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.008  | Monitoring/Audit  | The Platform | `RA-1 6.3.3.1     |
|              |                   | **must**     | “Confidentiality  |
|              |                   | Monitor and  | and Integrity of  |
|              |                   | Audit        | com               |
|              |                   | externally   | munications” <./c |
|              |                   | exposed      | hapter06.md#6331- |
|              |                   | interfaces   | confidentiality-a |
|              |                   | for illegal  | nd-integrity-of-c |
|              |                   | access       | ommunications>`__ |
|              |                   | (attacks)    |                   |
|              |                   | and take     |                   |
|              |                   | corrective   |                   |
|              |                   | security     |                   |
|              |                   | hardening    |                   |
|              |                   | measures.    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.009  | Monitoring/Audit  | The Platform | `RA-1 6.3.3.2     |
|              |                   | **must**     | “Confidentiality  |
|              |                   | Monitor and  | and Integrity of  |
|              |                   | Audit        | comm              |
|              |                   | service for  | unications” <./ch |
|              |                   | various      | apter06.md#6332-i |
|              |                   | attacks      | ntegrity-of-opens |
|              |                   | (malformed   | tack-components-c |
|              |                   | messages,    | onfiguration>`__, |
|              |                   | signalling   | `RA-1 6.3.7       |
|              |                   | flooding and | “Monitoring and   |
|              |                   | replaying,   | Security          |
|              |                   | etc.) and    | Audit” <.         |
|              |                   | take         | /chapter06.md#637 |
|              |                   | corrective   | -monitoring-and-s |
|              |                   | actions      | ecurity-audit>`__ |
|              |                   | accordingly. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.010  | Monitoring/Audit  | The Platform | `RA-1 6.3.7       |
|              |                   | **must**     | “Monitoring and   |
|              |                   | Monitor and  | Security          |
|              |                   | Audit        | Audit” <.         |
|              |                   | running      | /chapter06.md#637 |
|              |                   | processes to | -monitoring-and-s |
|              |                   | detect       | ecurity-audit>`__ |
|              |                   | unexpected   |                   |
|              |                   | or           |                   |
|              |                   | unauthorised |                   |
|              |                   | processes    |                   |
|              |                   | and take     |                   |
|              |                   | corrective   |                   |
|              |                   | actions      |                   |
|              |                   | accordingly. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.011  | Monitoring/Audit  | The Platform | `RA-1 6.3.7.1     |
|              |                   | **must**     | “Creating         |
|              |                   | Monitor and  | logs” <./c        |
|              |                   | Audit logs   | hapter06.md#6371- |
|              |                   | from         | creating-logs>`__ |
|              |                   | in           |                   |
|              |                   | frastructure |                   |
|              |                   | elements and |                   |
|              |                   | workloads to |                   |
|              |                   | detected     |                   |
|              |                   | anomalies in |                   |
|              |                   | the system   |                   |
|              |                   | components   |                   |
|              |                   | and take     |                   |
|              |                   | corrective   |                   |
|              |                   | actions      |                   |
|              |                   | accordingly. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.012  | Monitoring/Audit  | The Platform | `RA-1 6.3.3.3     |
|              |                   | **must**     | “Confidentiality  |
|              |                   | Monitor and  | and Integrity of  |
|              |                   | Audit        | tenant            |
|              |                   | Traffic      | data” <./chapt    |
|              |                   | patterns and | er06.md#6333-conf |
|              |                   | volumes to   | identiality-and-i |
|              |                   | prevent      | ntegrity-of-tenan |
|              |                   | malware      | t-data-secmon012- |
|              |                   | download     | and-secmon013>`__ |
|              |                   | attempts.    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.013  | Monitoring        | The          |                   |
|              |                   | monitoring   |                   |
|              |                   | system       |                   |
|              |                   | **must not** |                   |
|              |                   | affect the   |                   |
|              |                   | security     |                   |
|              |                   | (integrity   |                   |
|              |                   | and          |                   |
|              |                   | conf         |                   |
|              |                   | identiality) |                   |
|              |                   | of the       |                   |
|              |                   | inf          |                   |
|              |                   | rastructure, |                   |
|              |                   | workloads,   |                   |
|              |                   | or the user  |                   |
|              |                   | data         |                   |
|              |                   | (through     |                   |
|              |                   | back door    |                   |
|              |                   | entries).    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.015  | Monitoring        | The Platform | `RA-1 6.3.7       |
|              |                   | **must**     | “Monitoring and   |
|              |                   | ensure that  | Security          |
|              |                   | the          | Audit” <.         |
|              |                   | Monitoring   | /chapter06.md#637 |
|              |                   | systems are  | -monitoring-and-s |
|              |                   | never        | ecurity-audit>`__ |
|              |                   | starved of   |                   |
|              |                   | resources    |                   |
|              |                   | and **must** |                   |
|              |                   | activate     |                   |
|              |                   | alarms when  |                   |
|              |                   | resource     |                   |
|              |                   | utilisation  |                   |
|              |                   | exceeds a    |                   |
|              |                   | configurable |                   |
|              |                   | threshold.   |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.017  | Audit             | The Platform | `RA-1 6.3.1.5     |
|              |                   | **must**     | “Patches          |
|              |                   | audit        | ” <./chapter06.md |
|              |                   | systems for  | #6315-patches>`__ |
|              |                   | any missing  |                   |
|              |                   | security     |                   |
|              |                   | patches and  |                   |
|              |                   | take         |                   |
|              |                   | appropriate  |                   |
|              |                   | actions.     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.018  | Monitoring        | The          | `RA-1 6.3.7.3     |
|              |                   | Platform,    | “Where to         |
|              |                   | starting     | Log” <./          |
|              |                   | from         | chapter06.md#6373 |
|              |                   | ini          | -where-to-log>`__ |
|              |                   | tialisation, |                   |
|              |                   | **must**     |                   |
|              |                   | collect and  |                   |
|              |                   | analyse logs |                   |
|              |                   | to identify  |                   |
|              |                   | security     |                   |
|              |                   | events, and  |                   |
|              |                   | store these  |                   |
|              |                   | events in an |                   |
|              |                   | external     |                   |
|              |                   | system.      |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.019  | Monitoring        | The          | `RA-1 6.3.7.2     |
|              |                   | Platform’s   | “What to          |
|              |                   | components   | Log” <.           |
|              |                   | **must not** | /chapter06.md#637 |
|              |                   | include an   | 2-what-to-log--wh |
|              |                   | au           | at-not-to-log>`__ |
|              |                   | thentication |                   |
|              |                   | credential,  |                   |
|              |                   | e.g.,        |                   |
|              |                   | password, in |                   |
|              |                   | any logs,    |                   |
|              |                   | even if      |                   |
|              |                   | encrypted.   |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.020  | Monitoring/Audit  | The          | `RA-1 6.3.7.5     |
|              |                   | Platform’s   | “Data             |
|              |                   | logging      | Retention <./ch   |
|              |                   | system       | apter06.md#6375-d |
|              |                   | **must**     | ata-retention>`__ |
|              |                   | support the  |                   |
|              |                   | storage of   |                   |
|              |                   | security     |                   |
|              |                   | audit logs   |                   |
|              |                   | for a        |                   |
|              |                   | configurable |                   |
|              |                   | period of    |                   |
|              |                   | time.        |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.021  | Monitoring        | The Platform | `RA-1 6.3.7.3     |
|              |                   | **must**     | “Where to         |
|              |                   | store        | Log” <./          |
|              |                   | security     | chapter06.md#6373 |
|              |                   | events       | -where-to-log>`__ |
|              |                   | locally if   |                   |
|              |                   | the external |                   |
|              |                   | logging      |                   |
|              |                   | system is    |                   |
|              |                   | unavailable  |                   |
|              |                   | and shall    |                   |
|              |                   | periodically |                   |
|              |                   | attempt to   |                   |
|              |                   | send these   |                   |
|              |                   | to the       |                   |
|              |                   | external     |                   |
|              |                   | logging      |                   |
|              |                   | system until |                   |
|              |                   | successful.  |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-12: Reference Model Requirements - Monitoring and Security Audit
Requirements

Open-Source Software (source `RM 7.9.8 <../../../ref_model/chapters/chapter07.md#798-open-source-sotfware>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+-------------------+---------------------+---------------+
| Reference | sub-category      | Description         | Specification |
|           |                   |                     | Reference     |
+===========+===================+=====================+===============+
| se        | Software          | Open-source code    |               |
| c.oss.001 |                   | **must** be         |               |
|           |                   | inspected by tools  |               |
|           |                   | with various        |               |
|           |                   | capabilities for    |               |
|           |                   | static and dynamic  |               |
|           |                   | code analysis.      |               |
+-----------+-------------------+---------------------+---------------+
| se        | Software          | The `CVE (Common    |               |
| c.oss.002 |                   | Vulnerabilities and |               |
|           |                   | Exposures) <https:/ |               |
|           |                   | /cve.mitre.org/>`__ |               |
|           |                   | **must** be used to |               |
|           |                   | identify            |               |
|           |                   | vulnerabilities and |               |
|           |                   | their severity      |               |
|           |                   | rating for          |               |
|           |                   | open-source code    |               |
|           |                   | part of Cloud       |               |
|           |                   | Infrastructure and  |               |
|           |                   | workloads software. |               |
+-----------+-------------------+---------------------+---------------+
| se        | Software          | Critical and high   |               |
| c.oss.003 |                   | severity rated      |               |
|           |                   | vulnerabilities     |               |
|           |                   | **must** be fixed   |               |
|           |                   | in a timely manner. |               |
|           |                   | Refer to the `CVSS  |               |
|           |                   | (Common             |               |
|           |                   | Vulnerability       |               |
|           |                   | Scoring             |               |
|           |                   | Sy                  |               |
|           |                   | stem) <https://www. |               |
|           |                   | first.org/cvss/>`__ |               |
|           |                   | to know a           |               |
|           |                   | vulnerability score |               |
|           |                   | and its associated  |               |
|           |                   | rate (low, medium,  |               |
|           |                   | high, or critical). |               |
+-----------+-------------------+---------------------+---------------+
| se        | Software          | A dedicated         |               |
| c.oss.004 |                   | internal isolated   |               |
|           |                   | repository          |               |
|           |                   | separated from the  |               |
|           |                   | production          |               |
|           |                   | environment         |               |
|           |                   | **must** be used to |               |
|           |                   | store vetted        |               |
|           |                   | open-source         |               |
|           |                   | content.            |               |
+-----------+-------------------+---------------------+---------------+

Table 2-13: Reference Model Requirements - Open-Source Software Security
Requirements

IaaC security (source `RM 7.9.9 <../../../ref_model/chapters/chapter07.md#799-iaac---secure-design-and-architecture-stage-requirements>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Secure Code Stage Requirements**

+-----------+-------------------+---------------------+---------------+
| Reference | sub-category      | Description         | Specification |
|           |                   |                     | Reference     |
+===========+===================+=====================+===============+
| sec       | IaaC              | SAST -Static        |               |
| .code.001 |                   | Application         |               |
|           |                   | Security Testing    |               |
|           |                   | **must** be applied |               |
|           |                   | during Secure       |               |
|           |                   | Coding stage        |               |
|           |                   | triggered by Pull,  |               |
|           |                   | Clone or Comment    |               |
|           |                   | trigger. Security   |               |
|           |                   | testing that        |               |
|           |                   | analyses            |               |
|           |                   | application source  |               |
|           |                   | code for software   |               |
|           |                   | vulnerabilities and |               |
|           |                   | gaps against best   |               |
|           |                   | practices. Example: |               |
|           |                   | open source OWASP   |               |
|           |                   | range of tools.     |               |
+-----------+-------------------+---------------------+---------------+

Table 2-14: Reference Model Requirements: IaaC Security Requirements,
Secure Code Stage

**Continuous Build, Integration and Testing Stage Requirements**

+-----------+-------------------+---------------------+---------------+
| Reference | sub-category      | Description         | Specification |
|           |                   |                     | Reference     |
+===========+===================+=====================+===============+
| se        | IaaC              | Image Scan **must** |               |
| c.bld.003 |                   | be applied during   |               |
|           |                   | the Continuous      |               |
|           |                   | Build, Integration  |               |
|           |                   | and Testing stage   |               |
|           |                   | triggered by        |               |
|           |                   | Package trigger,    |               |
|           |                   | example: A push of  |               |
|           |                   | a container image   |               |
|           |                   | to a container      |               |
|           |                   | registry may        |               |
|           |                   | trigger a           |               |
|           |                   | vulnerability scan  |               |
|           |                   | before the image    |               |
|           |                   | becomes available   |               |
|           |                   | in the registry.    |               |
+-----------+-------------------+---------------------+---------------+

Table 2-15: Reference Model Requirements - IaaC Security Requirements,
Continuous Build, Integration and Testing Stage

**Continuous Delivery and Deployment Stage Requirements**

+-----------+-------------------+---------------------+---------------+
| Reference | sub-category      | Description         | Specification |
|           |                   |                     | Reference     |
+===========+===================+=====================+===============+
| se        | IaaC              | Image Scan **must** |               |
| c.del.001 |                   | be applied during   |               |
|           |                   | the Continuous      |               |
|           |                   | Delivery and        |               |
|           |                   | Deployment stage    |               |
|           |                   | triggered by        |               |
|           |                   | Publish to Artifact |               |
|           |                   | and Image           |               |
|           |                   | Repository trigger. |               |
|           |                   | Example: GitLab     |               |
|           |                   | uses the open       |               |
|           |                   | source Clair engine |               |
|           |                   | for container image |               |
|           |                   | scanning.           |               |
+-----------+-------------------+---------------------+---------------+
| se        | IaaC              | Code Signing        |               |
| c.del.002 |                   | **must** be applied |               |
|           |                   | during the          |               |
|           |                   | Continuous Delivery |               |
|           |                   | and Deployment      |               |
|           |                   | stage triggered by  |               |
|           |                   | Publish to Artifact |               |
|           |                   | and Image           |               |
|           |                   | Repository trigger. |               |
|           |                   | Code Signing        |               |
|           |                   | provides            |               |
|           |                   | authentication to   |               |
|           |                   | assure that         |               |
|           |                   | downloaded files    |               |
|           |                   | are form the        |               |
|           |                   | publisher named on  |               |
|           |                   | the certificate.    |               |
+-----------+-------------------+---------------------+---------------+
| se        | IaaC              | Component           |               |
| c.del.004 |                   | Vulnerability Scan  |               |
|           |                   | **must** be applied |               |
|           |                   | during the          |               |
|           |                   | Continuous Delivery |               |
|           |                   | and Deployment      |               |
|           |                   | stage triggered by  |               |
|           |                   | Instantiate         |               |
|           |                   | Infrastructure      |               |
|           |                   | trigger. The        |               |
|           |                   | vulnerability       |               |
|           |                   | scanning system is  |               |
|           |                   | deployed on the     |               |
|           |                   | cloud platform to   |               |
|           |                   | detect security     |               |
|           |                   | vulnerabilities of  |               |
|           |                   | specified           |               |
|           |                   | components through  |               |
|           |                   | scanning and to     |               |
|           |                   | provide timely      |               |
|           |                   | security            |               |
|           |                   | protection.         |               |
|           |                   | Example: OWASP Zed  |               |
|           |                   | Attack Proxy (ZAP). |               |
+-----------+-------------------+---------------------+---------------+

Table 2-16: Reference Model Requirements - IaaC Security Requirements,
Continuous Delivery and Deployment Stage

**Runtime Defence and Monitoring Requirements**

+-----------+-------------------+---------------------+---------------+
| Reference | sub-category      | Description         | Specification |
|           |                   |                     | Reference     |
+===========+===================+=====================+===============+
| se        | IaaC              | Component           |               |
| c.run.001 |                   | Vulnerability       |               |
|           |                   | Monitoring **must** |               |
|           |                   | be continuously     |               |
|           |                   | applied during the  |               |
|           |                   | Runtime Defence and |               |
|           |                   | Monitoring stage.   |               |
|           |                   | Security technology |               |
|           |                   | that monitors       |               |
|           |                   | components like     |               |
|           |                   | virtual servers and |               |
|           |                   | assesses data,      |               |
|           |                   | applications, and   |               |
|           |                   | infrastructure for  |               |
|           |                   | security risks.     |               |
+-----------+-------------------+---------------------+---------------+

Table 2-17: Reference Model Requirements - IaaC Security Requirements,
Runtime Defence and Monitoring Stage

Compliance with Standards (source `RM 7.9.10 <../../../ref_model/chapters/chapter07.md#7910-compliance-with-standards>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+-------------------+---------------------+---------------+
| Reference | sub-category      | Description         | Specification |
|           |                   |                     | Reference     |
+===========+===================+=====================+===============+
| se        | Standards         | The Public Cloud    |               |
| c.std.012 |                   | Operator **must**,  |               |
|           |                   | and the Private     |               |
|           |                   | Cloud Operator      |               |
|           |                   | **may** be          |               |
|           |                   | certified to be     |               |
|           |                   | compliant with the  |               |
|           |                   | International       |               |
|           |                   | Standard on         |               |
|           |                   | Awareness           |               |
|           |                   | Engagements (ISAE)  |               |
|           |                   | 3402 (in the US:    |               |
|           |                   | SSAE 16);           |               |
|           |                   | International       |               |
|           |                   | Standard on         |               |
|           |                   | Awareness           |               |
|           |                   | Engagements (ISAE)  |               |
|           |                   | 3402. US            |               |
|           |                   | Equivalent: SSAE16. |               |
+-----------+-------------------+---------------------+---------------+

Table 2-18: Reference Model Requirements: Cloud Infrastructure Security
Requirements

Architecture and OpenStack Requirements
---------------------------------------

“Architecture” in this chapter refers to Cloud Infrastructure (referred
to as NFVI by ETSI) + VIM (as specified in Reference Model Chapter 3).

General Requirements
~~~~~~~~~~~~~~~~~~~~

+----+------------------+--------------------------+------------------+
| R  | sub-category     | Description              | Specification    |
| ef |                  |                          | Reference        |
| er |                  |                          |                  |
| en |                  |                          |                  |
| ce |                  |                          |                  |
+====+==================+==========================+==================+
| ge | Open source      | The Architecture         | `RA-1            |
| n. |                  | **must** use OpenStack   | 5.3 <./chap      |
| os |                  | APIs.                    | ter05.md#5.3>`__ |
| t. |                  |                          |                  |
| 01 |                  |                          |                  |
+----+------------------+--------------------------+------------------+
| ge | Open source      | The Architecture         | `RA-1            |
| n. |                  | **must** support dynamic | 5.3              |
| os |                  | request and              |  <./chapter05.md |
| t. |                  | configuration of virtual | #53-consolidated |
| 02 |                  | resources (compute,      | -set-of-apis>`__ |
|    |                  | network, storage)        |                  |
|    |                  | through OpenStack APIs.  |                  |
+----+------------------+--------------------------+------------------+
| ge | Resiliency       | The Architecture         |                  |
| n. |                  | **must** support         |                  |
| rs |                  | resilient OpenStack      |                  |
| l. |                  | components that are      |                  |
| 01 |                  | required for the         |                  |
|    |                  | continued availability   |                  |
|    |                  | of running workloads.    |                  |
+----+------------------+--------------------------+------------------+
| ge | Availability     | The Architecture         | `RA-1 4.2        |
| n. |                  | **must** provide High    | “Underlying      |
| av |                  | Availability for         | Resour           |
| l. |                  | OpenStack components.    | ces” <./chapter0 |
| 01 |                  |                          | 4.md#42-underlyi |
|    |                  |                          | ng-resources>`__ |
+----+------------------+--------------------------+------------------+

Table 2-19: General Requirements

Infrastructure Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-------------------+-----------------------------+--------------+
| R  | sub-category      | Description                 | S            |
| ef |                   |                             | pecification |
| er |                   |                             | Reference    |
| en |                   |                             |              |
| ce |                   |                             |              |
+====+===================+=============================+==============+
| in | Compute           | The Architecture **must**   | `RA-1        |
| f. |                   | provide compute resources   | 3.3.1.4      |
| co |                   | for instances.              | “Cloud       |
| m. |                   |                             | Workload     |
| 01 |                   |                             | Services”    |
|    |                   |                             | <./chapter03 |
|    |                   |                             | .md#3314-clo |
|    |                   |                             | ud-workload- |
|    |                   |                             | services>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Compute           | The Architecture **must**   | `RA-1 4.4.1. |
| f. |                   | be able to support multiple | “Support for |
| co |                   | CPU type options to support | Cloud        |
| m. |                   | various infrastructure      | In           |
| 04 |                   | profiles (Basic and High    | frastructure |
|    |                   | Performance).               | Profiles and |
|    |                   |                             | flavors” <   |
|    |                   |                             | ./chapter04. |
|    |                   |                             | md#4.4.1>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Compute           | The Architecture **must**   | `RA-1 4.4.1. |
| f. |                   | support Hardware Platforms  | “Support for |
| co |                   | with NUMA capabilities.     | Cloud        |
| m. |                   |                             | In           |
| 05 |                   |                             | frastructure |
|    |                   |                             | Profiles and |
|    |                   |                             | flavors” <   |
|    |                   |                             | ./chapter04. |
|    |                   |                             | md#4.4.1>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Compute           | The Architecture **must**   | `RA-1 4.4.1. |
| f. |                   | support CPU Pinning of the  | “Support for |
| co |                   | vCPUs of an instance.       | Cloud        |
| m. |                   |                             | In           |
| 06 |                   |                             | frastructure |
|    |                   |                             | Profiles and |
|    |                   |                             | flavors” <   |
|    |                   |                             | ./chapter04. |
|    |                   |                             | md#4.4.1>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Compute           | The Architecture **must**   | `RA-1 3.3.3. |
| f. |                   | support different hardware  | “Host        |
| co |                   | configurations to support   | aggregates   |
| m. |                   | various infrastructure      | providing    |
| 07 |                   | profiles (Basic and High    | resource     |
|    |                   | Performance).               | poo          |
|    |                   |                             | ling” <./cha |
|    |                   |                             | pter03.md#33 |
|    |                   |                             | 3-host-aggre |
|    |                   |                             | gates-provid |
|    |                   |                             | ing-resource |
|    |                   |                             | -pooling>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Compute           | The Architecture **must**   | `RA-1        |
| f. |                   | support allocating certain  | 4.2.2.7      |
| co |                   | number of host cores for    | “Reservation |
| m. |                   | all non-tenant workloads    | of Compute   |
| 08 |                   | such as for OpenStack       | Node         |
|    |                   | services. SMT threads can   | cores        |
|    |                   | be allocated to individual  | ” <./chapter |
|    |                   | OpenStack services or their | 04.md#4227-r |
|    |                   | components. `Dedicating     | eservation-o |
|    |                   | host cores to certain       | f-compute-no |
|    |                   | workloads (e.g., OpenStack  | de-cores>`__ |
|    |                   | services) <https://docs.o   |              |
|    |                   | penstack.org/nova/latest/co |              |
|    |                   | nfiguration/config.html#com |              |
|    |                   | pute.cpu_dedicated_set>`__. |              |
|    |                   | Please see example,         |              |
|    |                   | `“Configuring libvirt       |              |
|    |                   | compute nodes for CPU       |              |
|    |                   | pinning” <https://docs.o    |              |
|    |                   | penstack.org/nova/latest/ad |              |
|    |                   | min/cpu-topologies.html>`__ |              |
+----+-------------------+-----------------------------+--------------+
| in | Compute           | The Architecture **must**   | `RA-1        |
| f. |                   | ensure that the host cores  | 4.2.2.7      |
| co |                   | assigned to non-tenant and  | “Reservation |
| m. |                   | tenant workloads are SMT    | of Compute   |
| 09 |                   | aware: that is, a host core | Node         |
|    |                   | and its associated SMT      | cores        |
|    |                   | threads are either all      | ” <./chapter |
|    |                   | assigned to non-tenant      | 04.md#4227-r |
|    |                   | workloads or all assigned   | eservation-o |
|    |                   | to tenant workloads.        | f-compute-no |
|    |                   |                             | de-cores>`__ |
|    |                   |                             | and `RA-1    |
|    |                   |                             | 4.2.2.8      |
|    |                   |                             | “Pinned and  |
|    |                   |                             | Unpinned     |
|    |                   |                             | CPUs” <      |
|    |                   |                             | ./chapter04. |
|    |                   |                             | md#4228-pinn |
|    |                   |                             | ed-and-unpin |
|    |                   |                             | ned-cpus>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Storage           | The Architecture **must**   | `RA-1        |
| f. |                   | provide remote (not         | 3.4.2.3.     |
| st |                   | directly attached to the    | “Stora       |
| g. |                   | host) Block storage for     | ge” <./chapt |
| 01 |                   | Instances.                  | er03.md#3423 |
|    |                   |                             | -storage>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Storage           | The Architecture **must**   | `RA-1        |
| f. |                   | provide Object storage for  | 4.3.1.4      |
| st |                   | Instances. Operators        | “S           |
| g. |                   | **may** choose not to       | wift” <./cha |
| 02 |                   | implement Object Storage    | pter04.md#43 |
|    |                   | but must be cognizant of    | 14-swift>`__ |
|    |                   | the risk of “Compliant      |              |
|    |                   | VNFs” failing in their      |              |
|    |                   | environment.                |              |
+----+-------------------+-----------------------------+--------------+
| in | Network           | The Architecture **must**   | `RA-1 5.2.5. |
| f. |                   | provide virtual network     | “Neut        |
| nt |                   | interfaces to instances.    | ron” <./chap |
| w. |                   |                             | ter05.md#525 |
| 01 |                   |                             | -neutron>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Network           | The Architecture **must**   | `RA-1 3.2.5. |
| f. |                   | include capabilities for    | “Virtual     |
| nt |                   | integrating SDN controllers | Networking – |
| w. |                   | to support provisioning of  | 3rd party    |
| 02 |                   | network services, from the  | SDN          |
|    |                   | OpenStack Neutron service,  | solu         |
|    |                   | such as networking of VTEPs | tion” <./cha |
|    |                   | to the Border Edge based    | pter03.md#32 |
|    |                   | VRFs.                       | 5-virtual-ne |
|    |                   |                             | tworking--3r |
|    |                   |                             | d-party-sdn- |
|    |                   |                             | solution>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Network           | The Architecture **must**   | `RA-1 4.2.3. |
| f. |                   | support low latency and     | “Network     |
| nt |                   | high throughput traffic     | Fabric” <.   |
| w. |                   | needs.                      | /chapter04.m |
| 03 |                   |                             | d#423-networ |
|    |                   |                             | k-fabric>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Network           | The Architecture **must**   | `RA-1 4.2.3. |
| f. |                   | allow for East/West tenant  | “Network     |
| nt |                   | traffic within the cloud    | Fabric” <.   |
| w. |                   | (via tunnelled              | /chapter04.m |
| 05 |                   | encapsulation overlay such  | d#423-networ |
|    |                   | as VXLAN or Geneve).        | k-fabric>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Network           | The Architecture **must**   | `RA-1        |
| f. |                   | support network             | 3.4.2.2.     |
| nt |                   | `resiliency                 | “Netwo       |
| w. |                   |  <../../../common/glossary. | rk” <./chapt |
| 07 |                   | md#cloud-platform-abstracti | er03.md#3422 |
|    |                   | on-related-terminology>`__. | -network>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Network           | The Cloud Infrastructure    | `RA-1        |
| f. |                   | Network Fabric **must** be  | 3.4.2.2.     |
| nt |                   | capable of enabling highly  | “Netwo       |
| w. |                   | available (Five 9’s or      | rk” <./chapt |
| 10 |                   | better) Cloud               | er03.md#3422 |
|    |                   | Infrastructure.             | -network>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Network           | The Architecture **must**   | `RA-1        |
| f. |                   | support multiple networking | 4.2.3.4.     |
| nt |                   | options for Cloud           | “Neutron     |
| w. |                   | Infrastructure to support   | ML2-plugin   |
| 15 |                   | various infrastructure      | I            |
|    |                   | profiles (Basic and High    | ntegration”  |
|    |                   | Performance).               | <./chapter04 |
|    |                   |                             | .md#4234-neu |
|    |                   |                             | tron-ml2-int |
|    |                   |                             | egration>`__ |
|    |                   |                             | and          |
|    |                   |                             | `“OpenStack  |
|    |                   |                             | Neutron      |
|    |                   |                             | P            |
|    |                   |                             | lugins” <htt |
|    |                   |                             | ps://wiki.op |
|    |                   |                             | enstack.org/ |
|    |                   |                             | wiki/Neutron |
|    |                   |                             | _Plugins_and |
|    |                   |                             | _Drivers>`__ |
+----+-------------------+-----------------------------+--------------+
| in | Network           | The Architecture **must**   |              |
| f. |                   | support dual stack IPv4 and |              |
| nt |                   | IPv6 for tenant networks    |              |
| w. |                   | and workloads.              |              |
| 16 |                   |                             |              |
+----+-------------------+-----------------------------+--------------+

Table 2-20: Infrastructure Requirements

VIM Requirements
~~~~~~~~~~~~~~~~

+----+--------------------+----------------------------+-------------+
| R  | sub-category       | Description                | Sp          |
| ef |                    |                            | ecification |
| er |                    |                            | Reference   |
| en |                    |                            |             |
| ce |                    |                            |             |
+====+====================+============================+=============+
| vi | General            | The Architecture **must**  | `RA-1 3.2.  |
| m. |                    | allow infrastructure       | “Consumable |
| 01 |                    | resource sharing.          | Inf         |
|    |                    |                            | rastructure |
|    |                    |                            | Resources   |
|    |                    |                            | and         |
|    |                    |                            | Serv        |
|    |                    |                            | ices” <./ch |
|    |                    |                            | apter03.md# |
|    |                    |                            | 32-consumab |
|    |                    |                            | le-infrastr |
|    |                    |                            | ucture-reso |
|    |                    |                            | urces-and-s |
|    |                    |                            | ervices>`__ |
+----+--------------------+----------------------------+-------------+
| vi | General            | The Architecture **must**  | `RA-1       |
| m. |                    | allow VIM to discover and  | 5.2.7.      |
| 03 |                    | manage Cloud               | “           |
|    |                    | Infrastructure resources.  | Placement”  |
|    |                    |                            | <./chapter0 |
|    |                    |                            | 5.md#527-pl |
|    |                    |                            | acement>`__ |
+----+--------------------+----------------------------+-------------+
| vi | General            | The Architecture **must**  | `RA-1       |
| m. |                    | include image repository   | 4.3.1.2.    |
| 05 |                    | management.                | “Glance     |
|    |                    |                            | ” <./chapte |
|    |                    |                            | r04.md#4312 |
|    |                    |                            | -glance>`__ |
+----+--------------------+----------------------------+-------------+
| vi | General            | The Architecture **must**  | `RA-1       |
| m. |                    | support multi-tenancy.     | 3.2.1.      |
| 07 |                    |                            | “Multi-Te   |
|    |                    |                            | nancy” <./c |
|    |                    |                            | hapter03.md |
|    |                    |                            | #321-multi- |
|    |                    |                            | tenancy-exe |
|    |                    |                            | cution-envi |
|    |                    |                            | ronment>`__ |
+----+--------------------+----------------------------+-------------+
| vi | General            | The Architecture **must**  | `“OpenStack |
| m. |                    | support resource tagging.  | Resource    |
| 08 |                    |                            | Tags” <htt  |
|    |                    |                            | ps://specs. |
|    |                    |                            | openstack.o |
|    |                    |                            | rg/openstac |
|    |                    |                            | k/api-wg/gu |
|    |                    |                            | idelines/ta |
|    |                    |                            | gs.html>`__ |
+----+--------------------+----------------------------+-------------+

Table 2-21: VIM Requirements

Interfaces & APIs Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+--------------+------------------------------+-----------------+
| Ref | sub-category | Description                  | Specification   |
| ere |              |                              | Reference       |
| nce |              |                              |                 |
+=====+==============+==============================+=================+
| i   | API          | The Architecture **must**    | `RA-1 5.2.1     |
| nt. |              | provide APIs to access the   | “Keystone” <.   |
| api |              | authentication service and   | /chapter05.md#5 |
| .01 |              | the associated mandatory     | 21-keystone>`__ |
|     |              | features detailed in chapter |                 |
|     |              | 5.                           |                 |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture **must**    | `RA-1 5.2.2     |
| nt. |              | provide APIs to access the   | “Glance”        |
| api |              | image management service and | <./chapter05.md |
| .02 |              | the associated mandatory     | #522-glance>`__ |
|     |              | features detailed in chapter |                 |
|     |              | 5.                           |                 |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture **must**    | `RA-1 5.2.3     |
| nt. |              | provide APIs to access the   | “Cinder”        |
| api |              | block storage management     | <./chapter05.md |
| .03 |              | service and the associated   | #523-cinder>`__ |
|     |              | mandatory features detailed  |                 |
|     |              | in chapter 5.                |                 |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture **must**    | `RA-1 5.2.4     |
| nt. |              | provide APIs to access the   | “Swift”         |
| api |              | object storage management    |  <./chapter05.m |
| .04 |              | service and the associated   | d#524-swift>`__ |
|     |              | mandatory features detailed  |                 |
|     |              | in chapter 5.                |                 |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture **must**    | `RA-1 5.2.5     |
| nt. |              | provide APIs to access the   | “Neutron” <     |
| api |              | network management service   | ./chapter05.md# |
| .05 |              | and the associated mandatory | 525-neutron>`__ |
|     |              | features detailed in chapter |                 |
|     |              | 5.                           |                 |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture **must**    | `RA-1 5.2.6     |
| nt. |              | provide APIs to access the   | “Nova           |
| api |              | compute resources management | ” <./chapter05. |
| .06 |              | service and the associated   | md#526-nova>`__ |
|     |              | mandatory features detailed  |                 |
|     |              | in chapter 5.                |                 |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture **must**    | `RA-1 4.3.1.9   |
| nt. |              | provide GUI access to tenant | “Horizon” <.    |
| api |              | facing cloud platform core   | /chapter04.md#4 |
| .07 |              | services except at Edge/Far  | 319-horizon>`__ |
|     |              | Edge clouds.                 |                 |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture **must**    | `RA-1 5.2.7.    |
| nt. |              | provide APIs needed to       | “Placement” <./ |
| api |              | discover and manage Cloud    | chapter05.md#52 |
| .08 |              | Infrastructure resources.    | 7-placement>`__ |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture **must**    | `RA-1 5.2.8     |
| nt. |              | provide APIs to access the   | “Heat           |
| api |              | orchestration service.       | ” <./chapter05. |
| .09 |              |                              | md#528-heat>`__ |
+-----+--------------+------------------------------+-----------------+
| i   | API          | The Architecture must expose | `RA-1 5.2 Core  |
| nt. |              | the latest version and       | OpenStack       |
| api |              | microversion of the APIs for | Services        |
| .10 |              | the given Anuket OpenStack   | APIs <./cha     |
|     |              | release for each of the      | pter05.md#52-co |
|     |              | OpenStack core services.     | re-openstack-se |
|     |              |                              | rvices-apis>`__ |
+-----+--------------+------------------------------+-----------------+

Table 2-22: Interfaces and APIs Requirements

Tenant Requirements
~~~~~~~~~~~~~~~~~~~

+----+-------------------+--------------------+-----------------------+
| R  | sub-category      | Description        | Specification         |
| ef |                   |                    | Reference             |
| er |                   |                    |                       |
| en |                   |                    |                       |
| ce |                   |                    |                       |
+====+===================+====================+=======================+
| tn | General           | The Architecture   | `RA-1 4.3.1.9         |
| t. |                   | **must** support   | “Horizon” <./chapter0 |
| ge |                   | self-service       | 4.md#4319-horizon>`__ |
| n. |                   | dashboard (GUI)    | and `3.3.1.4 Cloud    |
| 01 |                   | and APIs for users | Workload              |
|    |                   | to deploy,         | Services <./cha       |
|    |                   | configure and      | pter03.md#3314-cloud- |
|    |                   | manage their       | workload-services>`__ |
|    |                   | workloads.         |                       |
+----+-------------------+--------------------+-----------------------+

Table 2-23: Tenant Requirements

Operations and LCM
~~~~~~~~~~~~~~~~~~

+------+-----------------+----------------------+----------------------+
| R    | sub-category    | Description          | Specification        |
| efer |                 |                      | Reference            |
| ence |                 |                      |                      |
+======+=================+======================+======================+
| lc   | General         | The Architecture     |                      |
| m.ge |                 | **must** support     |                      |
| n.01 |                 | zero downtime of     |                      |
|      |                 | running workloads    |                      |
|      |                 | when the number of   |                      |
|      |                 | compute hosts and/or |                      |
|      |                 | the storage capacity |                      |
|      |                 | is being expanded or |                      |
|      |                 | unused capacity is   |                      |
|      |                 | being removed.       |                      |
+------+-----------------+----------------------+----------------------+
| lc   | Automated       | The Architecture     |                      |
| m.ad | deployment      | **must** support     |                      |
| p.02 |                 | upgrades of          |                      |
|      |                 | software, provided   |                      |
|      |                 | by the cloud         |                      |
|      |                 | provider, so that    |                      |
|      |                 | the running          |                      |
|      |                 | workloads are not    |                      |
|      |                 | impacted (viz.,      |                      |
|      |                 | hitless upgrades).   |                      |
|      |                 | Please note that     |                      |
|      |                 | this means that the  |                      |
|      |                 | existing data plane  |                      |
|      |                 | services should not  |                      |
|      |                 | fail (go down).      |                      |
+------+-----------------+----------------------+----------------------+

Table 2-24: LCM Requirements

Assurance Requirements
~~~~~~~~~~~~~~~~~~~~~~

+------+-------------+--------------------------------+----------------+
| R    | s           | Description                    | Specification  |
| efer | ub-category |                                | Reference      |
| ence |             |                                |                |
+======+=============+================================+================+
| as   | Integration | The Architecture **must**      |                |
| r.mo |             | include integration with       |                |
| n.01 |             | various infrastructure         |                |
|      |             | components to support          |                |
|      |             | collection of telemetry for    |                |
|      |             | assurance monitoring and       |                |
|      |             | network intelligence.          |                |
+------+-------------+--------------------------------+----------------+
| as   | Monitoring  | The Architecture **must**      |                |
| r.mo |             | allow for the collection and   |                |
| n.03 |             | dissemination of performance   |                |
|      |             | and fault information.         |                |
+------+-------------+--------------------------------+----------------+
| as   | Network     | The Cloud Infrastructure       |                |
| r.mo |             | Network Fabric and Network     |                |
| n.04 |             | Operating System **must**      |                |
|      |             | provide network operational    |                |
|      |             | visibility through alarming    |                |
|      |             | and streaming telemetry        |                |
|      |             | services for operational       |                |
|      |             | management, engineering        |                |
|      |             | planning, troubleshooting, and |                |
|      |             | network performance            |                |
|      |             | optimisation.                  |                |
+------+-------------+--------------------------------+----------------+

Table 2-25: Assurance Requirements

Architecture and OpenStack Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requirements listed in this section are optional, and are not
required in order to be deemed a conformant implementation.

General Recommendations
~~~~~~~~~~~~~~~~~~~~~~~

+-----+----------+--------------------------------+-------------------+
| Ref | sub-     | Description                    | Notes             |
| ere | category |                                |                   |
| nce |          |                                |                   |
+=====+==========+================================+===================+
| g   | Cloud    | The Architecture **should**    | OpenStack         |
| en. | na       | consist of stateless service   | consists of both  |
| cnt | tiveness | components. However, where     | stateless and     |
| .01 |          | state is required it must be   | stateful services |
|     |          | kept external to the           | where the         |
|     |          | component.                     | stateful services |
|     |          |                                | utilise a         |
|     |          |                                | database. For     |
|     |          |                                | latter see        |
|     |          |                                | “`Configuring the |
|     |          |                                | stateful          |
|     |          |                                | services <        |
|     |          |                                | https://docs.open |
|     |          |                                | stack.org/ha-guid |
|     |          |                                | e/control-plane-s |
|     |          |                                | tateful.html>`__” |
+-----+----------+--------------------------------+-------------------+
| g   | Cloud    | The Architecture **should**    |                   |
| en. | na       | consist of service components  |                   |
| cnt | tiveness | implemented as microservices   |                   |
| .02 |          | that are individually          |                   |
|     |          | dynamically scalable.          |                   |
+-----+----------+--------------------------------+-------------------+
| g   | Sca      | The Architecture **should**    | This requirement  |
| en. | lability | support policy driven          | is currently not  |
| scl |          | auto-scaling.                  | addressed but     |
| .01 |          |                                | will likely be    |
|     |          |                                | supported through |
|     |          |                                | `Senl             |
|     |          |                                | in <https://docs. |
|     |          |                                | openstack.org/sen |
|     |          |                                | lin/wallaby/>`__, |
|     |          |                                | cluster           |
|     |          |                                | management        |
|     |          |                                | service.          |
+-----+----------+--------------------------------+-------------------+
| g   | Re       | The Architecture **should**    |                   |
| en. | siliency | support resilient OpenStack    |                   |
| rsl |          | service components that are    |                   |
| .02 |          | not subject to gen.rsl.01.     |                   |
+-----+----------+--------------------------------+-------------------+

Table 2-26: General Recommendations

Infrastructure Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+----------+--------------------------------+-------------------+
| Ref | sub-     | Description                    | Notes             |
| ere | category |                                |                   |
| nce |          |                                |                   |
+=====+==========+================================+===================+
| i   | Compute  | The Architecture **should**    |                   |
| nf. |          | include industry standard      |                   |
| com |          | hardware management systems at |                   |
| .02 |          | both HW device level           |                   |
|     |          | (embedded) and HW platform     |                   |
|     |          | level (external to device).    |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Compute  | The Architecture **should**    |                   |
| nf. |          | support Symmetric              |                   |
| com |          | Multiprocessing with shared    |                   |
| .03 |          | memory access as well as       |                   |
|     |          | Simultaneous Multithreading.   |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Storage  | The Architecture **should**    |                   |
| nf. |          | allow use of externally        |                   |
| stg |          | provided large archival        |                   |
| .08 |          | storage for its Backup /       |                   |
|     |          | Restore / Archival needs.      |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Storage  | The Architecture **should**    |                   |
| nf. |          | make available all non-host OS |                   |
| stg |          | / Hypervisor / Host systems    |                   |
| .09 |          | storage as network-based       |                   |
|     |          | Block, File or Object Storage  |                   |
|     |          | for tenant/management          |                   |
|     |          | consumption.                   |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Storage  | The Architecture **should**    | `RA-1 “Virtual    |
| nf. |          | provide local Block storage    | Storage” <./ch    |
| stg |          | for Instances.                 | apter03.md#323-vi |
| .10 |          |                                | rtual-storage>`__ |
+-----+----------+--------------------------------+-------------------+
| i   | Network  | The Architecture **should**    |                   |
| nf. |          | support service function       |                   |
| ntw |          | chaining.                      |                   |
| .04 |          |                                |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Network  | The Architecture **should**    |                   |
| nf. |          | support Distributed Virtual    |                   |
| ntw |          | Routing (DVR) to allow compute |                   |
| .06 |          | nodes to route traffic         |                   |
|     |          | efficiently.                   |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Network  | The Cloud Infrastructure       |                   |
| nf. |          | Network Fabric **should**      |                   |
| ntw |          | embrace the concepts of open   |                   |
| .08 |          | networking and disaggregation  |                   |
|     |          | using commodity networking     |                   |
|     |          | hardware and disaggregated     |                   |
|     |          | Network Operating Systems.     |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Network  | The Cloud Infrastructure       |                   |
| nf. |          | Network Fabric **should**      |                   |
| ntw |          | embrace open-based standards   |                   |
| .09 |          | and technologies.              |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Network  | The Cloud Infrastructure       |                   |
| nf. |          | Network Fabric **should** be   |                   |
| ntw |          | architected to provide a       |                   |
| .11 |          | standardised, scalable, and    |                   |
|     |          | repeatable deployment model    |                   |
|     |          | across all applicable Cloud    |                   |
|     |          | Infrastructure sites.          |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Network  | The Architecture **should**    |                   |
| nf. |          | use dual stack IPv4 and IPv6   |                   |
| ntw |          | for Cloud Infrastructure       |                   |
| .17 |          | internal networks.             |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Acce     | The Architecture **should**    | `RA-1 3.2.6.      |
| nf. | leration | support Application Specific   | “Acceleration” <. |
| acc |          | Acceleration (exposed to       | /chapter03.md#326 |
| .01 |          | VNFs).                         | -acceleration>`__ |
+-----+----------+--------------------------------+-------------------+
| i   | Acce     | The Architecture **should**    | `“OpenStack       |
| nf. | leration | support Cloud Infrastructure   | Future - Specs    |
| acc |          | Acceleration (such as          | defined” <http    |
| .02 |          | SmartNICs).                    | s://specs.opensta |
|     |          |                                | ck.org/openstack/ |
|     |          |                                | neutron-specs/spe |
|     |          |                                | cs/stein/neutron- |
|     |          |                                | ovs-agent-support |
|     |          |                                | -baremetal-with-s |
|     |          |                                | mart-nic.html>`__ |
+-----+----------+--------------------------------+-------------------+
| i   | Acce     | The Architecture **may** rely  |                   |
| nf. | leration | on SR-IOV PCI-Pass through to  |                   |
| acc |          | provide acceleration to VNFs.  |                   |
| .03 |          |                                |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Image    | The Architecture **should**    | `RA-1 4.3.1.2.    |
| nf. |          | make the immutable images      | “Glanc            |
| img |          | available via location         | e” <./chapter04.m |
| .01 |          | independent means.             | d#4312-glance>`__ |
+-----+----------+--------------------------------+-------------------+

Table 2-27: Infrastructure Recommendations

Recommendations
~~~~~~~~~~~~~~~

+----+--------------------+----------------------------+-------------+
| R  | sub-category       | Description                | Notes       |
| ef |                    |                            |             |
| er |                    |                            |             |
| en |                    |                            |             |
| ce |                    |                            |             |
+====+====================+============================+=============+
| vi | General            | The Architecture           | `RA-1       |
| m. |                    | **should** support         | 4.3.2.      |
| 02 |                    | deployment of OpenStack    | “Co         |
|    |                    | components in containers.  | ntainerised |
|    |                    |                            | OpenStack   |
|    |                    |                            | Services” < |
|    |                    |                            | ./chapter04 |
|    |                    |                            | .md#432-con |
|    |                    |                            | tainerised- |
|    |                    |                            | openstack-s |
|    |                    |                            | ervices>`__ |
+----+--------------------+----------------------------+-------------+
| vi | General            | The Architecture           |             |
| m. |                    | **should** support         |             |
| 04 |                    | Enhanced Platform          |             |
|    |                    | Awareness (EPA) only for   |             |
|    |                    | discovery of               |             |
|    |                    | infrastructure resource    |             |
|    |                    | capabilities.              |             |
+----+--------------------+----------------------------+-------------+
| vi | General            | The Architecture           |             |
| m. |                    | **should** allow           |             |
| 06 |                    | orchestration solutions to |             |
|    |                    | be integrated with VIM.    |             |
+----+--------------------+----------------------------+-------------+
| vi | General            | The Architecture           |             |
| m. |                    | **should** support         |             |
| 09 |                    | horizontal scaling of      |             |
|    |                    | OpenStack core services.   |             |
+----+--------------------+----------------------------+-------------+

Table 2-28: VIM Recommendations

Interfaces and APIs Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+----------+--------------------------------+-------------------+
| Ref | sub-     | Description                    | Notes             |
| ere | category |                                |                   |
| nce |          |                                |                   |
+=====+==========+================================+===================+
| i   | Acce     | The Architecture **should**    |                   |
| nt. | leration | provide an open and standard   |                   |
| acc |          | acceleration interface to      |                   |
| .01 |          | VNFs.                          |                   |
+-----+----------+--------------------------------+-------------------+
| i   | Acce     | The Architecture **should      | duplicate of      |
| nt. | leration | not** rely on SR-IOV PCI-Pass  | inf.acc.03 under  |
| acc |          | through for acceleration       | “Infrastructure   |
| .02 |          | interface exposed to VNFs.     | Recommendations”  |
+-----+----------+--------------------------------+-------------------+

Table 2-29: Interfaces and APIs Recommendations

Tenant Recommendations
~~~~~~~~~~~~~~~~~~~~~~

This section is left blank for future use.

========= ============ =========== =====
Reference sub-category Description Notes
========= ============ =========== =====
========= ============ =========== =====

Table 2-30: Tenant Recommendations

Operations and LCM Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------+-----------------+----------------------+----------------------+
| R    | sub-category    | Description          | Notes                |
| efer |                 |                      |                      |
| ence |                 |                      |                      |
+======+=================+======================+======================+
| lc   | Automated       | The Architecture     |                      |
| m.ad | deployment      | **should** allow for |                      |
| p.01 |                 | “cookie cutter”      |                      |
|      |                 | automated            |                      |
|      |                 | deployment,          |                      |
|      |                 | configuration,       |                      |
|      |                 | provisioning and     |                      |
|      |                 | management of        |                      |
|      |                 | multiple Cloud       |                      |
|      |                 | Infrastructure       |                      |
|      |                 | sites.               |                      |
+------+-----------------+----------------------+----------------------+
| lc   | Automated       | The Architecture     |                      |
| m.ad | deployment      | **should** support   |                      |
| p.03 |                 | hitless upgrade of   |                      |
|      |                 | all software         |                      |
|      |                 | provided by the      |                      |
|      |                 | cloud provider that  |                      |
|      |                 | are not covered by   |                      |
|      |                 | lcm.adp.02. Whenever |                      |
|      |                 | hitless upgrades are |                      |
|      |                 | not feasible,        |                      |
|      |                 | attempt should be    |                      |
|      |                 | made to minimise the |                      |
|      |                 | duration and nature  |                      |
|      |                 | of impact.           |                      |
+------+-----------------+----------------------+----------------------+
| lc   | Automated       | The Architecture     |                      |
| m.ad | deployment      | **should** support   |                      |
| p.04 |                 | declarative          |                      |
|      |                 | specifications of    |                      |
|      |                 | hardware and         |                      |
|      |                 | software assets for  |                      |
|      |                 | automated            |                      |
|      |                 | deployment,          |                      |
|      |                 | configuration,       |                      |
|      |                 | maintenance and      |                      |
|      |                 | management.          |                      |
+------+-----------------+----------------------+----------------------+
| lc   | Automated       | The Architecture     |                      |
| m.ad | deployment      | **should** support   |                      |
| p.05 |                 | automated process    |                      |
|      |                 | for Deployment and   |                      |
|      |                 | life-cycle           |                      |
|      |                 | management of VIM    |                      |
|      |                 | Instances.           |                      |
+------+-----------------+----------------------+----------------------+
| lc   | CI/CD           | The Architecture     |                      |
| m.ci |                 | **should** support   |                      |
| d.02 |                 | integrating with     |                      |
|      |                 | CI/CD Toolchain for  |                      |
|      |                 | Cloud Infrastructure |                      |
|      |                 | and VIM components   |                      |
|      |                 | Automation.          |                      |
+------+-----------------+----------------------+----------------------+

Table 2-31: LCM Recommendations

Assurance Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~

+------+-------------+--------------------------------+----------------+
| R    | s           | Description                    | Notes          |
| efer | ub-category |                                |                |
| ence |             |                                |                |
+======+=============+================================+================+
| as   | Monitoring  | The Architecture **should**    |                |
| r.mo |             | support Network Intelligence   |                |
| n.02 |             | capabilities that allow richer |                |
|      |             | diagnostic capabilities which  |                |
|      |             | take as input broader set of   |                |
|      |             | data across the network and    |                |
|      |             | from VNF workloads.            |                |
+------+-------------+--------------------------------+----------------+

Table 2-32: Assurance Recommendations

Security Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~

.. _system-hardening-source-rm-7.9.1-1:

System Hardening (source `RM 7.9.1 <../../../ref_model/chapters/chapter07.md#791-system-hardening>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+---------------+---------------+------------------+
| Reference        | sub-category  | Description   | Notes            |
+==================+===============+===============+==================+
| sec.gen.011      | Hardening     | The Cloud     |                  |
|                  |               | I             |                  |
|                  |               | nfrastructure |                  |
|                  |               | **should**    |                  |
|                  |               | support Read  |                  |
|                  |               | and Write     |                  |
|                  |               | only storage  |                  |
|                  |               | partitions    |                  |
|                  |               | (write only   |                  |
|                  |               | permission to |                  |
|                  |               | one or more   |                  |
|                  |               | authorised    |                  |
|                  |               | actors).      |                  |
+------------------+---------------+---------------+------------------+
| sec.gen.014      | Hardening     | All servers   |                  |
|                  |               | part of Cloud |                  |
|                  |               | I             |                  |
|                  |               | nfrastructure |                  |
|                  |               | **should**    |                  |
|                  |               | support       |                  |
|                  |               | measured boot |                  |
|                  |               | and an        |                  |
|                  |               | attestation   |                  |
|                  |               | server that   |                  |
|                  |               | monitors the  |                  |
|                  |               | measurements  |                  |
|                  |               | of the        |                  |
|                  |               | servers.      |                  |
+------------------+---------------+---------------+------------------+

Table 2-33: System Hardening Recommendations

.. _platform-and-access-source-rm-7.9.2-1:

Platform and Access (source `RM 7.9.2 <../../../ref_model/chapters/chapter07.md#792-platform-and-access>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+---------------+---------------+--------------------+
| Reference     | sub-category  | Description   | Notes              |
+===============+===============+===============+====================+
| sec.sys.014   | Access        | The Platform  |                    |
|               |               | **should**    |                    |
|               |               | use Linux     |                    |
|               |               | Security      |                    |
|               |               | Modules such  |                    |
|               |               | as SELinux to |                    |
|               |               | control       |                    |
|               |               | access to     |                    |
|               |               | resources.    |                    |
+---------------+---------------+---------------+--------------------+
| sec.sys.020   | Access        | The Cloud     | Zero Trust         |
|               |               | I             | Architecture (ZTA) |
|               |               | nfrastructure | described in NIST  |
|               |               | architecture  | SP 800-207         |
|               |               | **should**    |                    |
|               |               | rely on Zero  |                    |
|               |               | Trust         |                    |
|               |               | principles to |                    |
|               |               | build a       |                    |
|               |               | secure by     |                    |
|               |               | design        |                    |
|               |               | environment.  |                    |
+---------------+---------------+---------------+--------------------+

Table 2-34: Platform and Access Recommendations

.. _confidentiality-and-integrity-source-rm-7.9.3-1:

Confidentiality and Integrity (source `RM 7.9.3 <../../../ref_model/chapters/chapter07.md#793-confidentiality-and-integrity>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.ci.002   | Confiden          | The Platform |                   |
|              | tiality/Integrity | **should**   |                   |
|              |                   | support      |                   |
|              |                   | sel          |                   |
|              |                   | f-encrypting |                   |
|              |                   | storage      |                   |
|              |                   | devices      |                   |
+--------------+-------------------+--------------+-------------------+
| sec.ci.009   | Confiden          | For          |                   |
|              | tiality/Integrity | sensitive    |                   |
|              |                   | data         |                   |
|              |                   | encryption,  |                   |
|              |                   | the key      |                   |
|              |                   | management   |                   |
|              |                   | service      |                   |
|              |                   | **should**   |                   |
|              |                   | leverage a   |                   |
|              |                   | Hardware     |                   |
|              |                   | Security     |                   |
|              |                   | Module to    |                   |
|              |                   | manage and   |                   |
|              |                   | protect      |                   |
|              |                   | c            |                   |
|              |                   | ryptographic |                   |
|              |                   | keys.        |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-35: Confidentiality and Integrity Recommendations

.. _workload-security-source-rm-7.9.4-1:

Workload Security (source `RM 7.9.4 <../../../ref_model/chapters/chapter07.md#794-workload-security>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.wl.007   | Workload          | The Operator |                   |
|              |                   | **should**   |                   |
|              |                   | implement    |                   |
|              |                   | processes    |                   |
|              |                   | and tools to |                   |
|              |                   | verify VNF   |                   |
|              |                   | authenticity |                   |
|              |                   | and          |                   |
|              |                   | integrity.   |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-36: Workload Security Recommendations

.. _image-security-source-rm-7.9.5-1:

Image Security (source `RM 7.9.5 <../../../ref_model/chapters/chapter07.md#795-image-security>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section is left blank for future use.

+-------------+--------------+------------------------------+-------+
| Reference   | sub-category | Description                  | Notes |
+=============+==============+==============================+=======+
| sec.img.009 | Image        | CIS Hardened Images          |       |
|             |              | **should** be used whenever  |       |
|             |              | possible.                    |       |
+-------------+--------------+------------------------------+-------+
| sec.img.010 | Image        | Minimalist base images       |       |
|             |              | **should** be used whenever  |       |
|             |              | possible.                    |       |
+-------------+--------------+------------------------------+-------+

Table 2-37: Image Security Recommendations

.. _security-lcm-source-rm-7.9.6-1:

Security LCM (source `RM 7.9.6 <../../../ref_model/chapters/chapter07.md#796-security-lcm>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.lcm.004  | LCM               | The Cloud    |                   |
|              |                   | Operator     |                   |
|              |                   | **should**   |                   |
|              |                   | support      |                   |
|              |                   | automated    |                   |
|              |                   | templated    |                   |
|              |                   | approved     |                   |
|              |                   | changes;     |                   |
|              |                   | Templated    |                   |
|              |                   | approved     |                   |
|              |                   | changes for  |                   |
|              |                   | automation   |                   |
|              |                   | where        |                   |
|              |                   | available    |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-38: LCM Security Recommendations

.. _monitoring-and-security-audit-source-rm-7.9.7-1:

Monitoring and Security Audit (source `RM 7.9.7 <../../../ref_model/chapters/chapter07.md#797-monitoring-and-security-audit>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Platform is assumed to provide configurable alerting and
notification capability and the operator is assumed to have automated
systems, policies and procedures to act on alerts and notifications in a
timely fashion. In the following the monitoring and logging capabilities
can trigger alerts and notifications for appropriate action.

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.mon.014  | Monitoring        | The          |                   |
|              |                   | Monitoring   |                   |
|              |                   | systems      |                   |
|              |                   | **should**   |                   |
|              |                   | not impact   |                   |
|              |                   | IaaS, PaaS,  |                   |
|              |                   | and SaaS     |                   |
|              |                   | SLAs         |                   |
|              |                   | including    |                   |
|              |                   | availability |                   |
|              |                   | SLAs         |                   |
+--------------+-------------------+--------------+-------------------+
| sec.mon.016  | Monitoring        | The Platform |                   |
|              |                   | Monitoring   |                   |
|              |                   | components   |                   |
|              |                   | **should**   |                   |
|              |                   | follow       |                   |
|              |                   | security     |                   |
|              |                   | best         |                   |
|              |                   | practices    |                   |
|              |                   | for          |                   |
|              |                   | auditing,    |                   |
|              |                   | including    |                   |
|              |                   | secure       |                   |
|              |                   | logging and  |                   |
|              |                   | tracing      |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-39: Monitoring and Security Audit Recommendations

Open-Source Software Security (source `RM 7.9.8 <../../../ref_model/chapters/chapter07.md#798-open-source-sotfware>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.oss.005  | Software          | A Software   | https://w         |
|              |                   | Bill of      | ww.ntia.gov/SBOM. |
|              |                   | Materials    |                   |
|              |                   | (SBOM)       |                   |
|              |                   | **should**   |                   |
|              |                   | be provided  |                   |
|              |                   | or build,    |                   |
|              |                   | and          |                   |
|              |                   | maintained   |                   |
|              |                   | to identify  |                   |
|              |                   | the software |                   |
|              |                   | components   |                   |
|              |                   | and their    |                   |
|              |                   | origins.     |                   |
|              |                   | Inventory of |                   |
|              |                   | software     |                   |
|              |                   | components   |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-40: Open-Source Software Security Recommendations

.. _iaac-security-source-rm-7.9.9-1:

IaaC security (source `RM 7.9.9 <../../../ref_model/chapters/chapter07.md#799-iaac---secure-design-and-architecture-stage-requirements>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Secure Design and Architecture Stage**

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.arch.001 | IaaC              | Threat       | It may be done    |
|              |                   | Modelling    | manually or using |
|              |                   | m            | tools like open   |
|              |                   | ethodologies | source OWASP      |
|              |                   | and tools    | Threat Dragon     |
|              |                   | **should**   |                   |
|              |                   | be used      |                   |
|              |                   | during the   |                   |
|              |                   | Secure       |                   |
|              |                   | Design and   |                   |
|              |                   | Architecture |                   |
|              |                   | stage        |                   |
|              |                   | triggered by |                   |
|              |                   | Software     |                   |
|              |                   | Feature      |                   |
|              |                   | Design       |                   |
|              |                   | trigger.     |                   |
|              |                   | Methodology  |                   |
|              |                   | to identify  |                   |
|              |                   | and          |                   |
|              |                   | understand   |                   |
|              |                   | threats      |                   |
|              |                   | impacting a  |                   |
|              |                   | resource or  |                   |
|              |                   | set of       |                   |
|              |                   | resources.   |                   |
+--------------+-------------------+--------------+-------------------+
| sec.arch.002 | IaaC              | Security     | Typically done    |
|              |                   | Control      | manually by       |
|              |                   | Baseline     | internal or       |
|              |                   | Assessment   | independent       |
|              |                   | **should**   | assessors.        |
|              |                   | be performed |                   |
|              |                   | during the   |                   |
|              |                   | Secure       |                   |
|              |                   | Design and   |                   |
|              |                   | Architecture |                   |
|              |                   | stage        |                   |
|              |                   | triggered by |                   |
|              |                   | Software     |                   |
|              |                   | Feature      |                   |
|              |                   | Design       |                   |
|              |                   | trigger.     |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-41: Reference Model Requirements: IaaC Security, Design and
Architecture Stage

**Secure Code Stage Requirements**

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.code.002 | IaaC              | SCA –        | Example: open     |
|              |                   | Software     | source OWASP      |
|              |                   | Composition  | range of tools.   |
|              |                   | Analysis     |                   |
|              |                   | **should**   |                   |
|              |                   | be applied   |                   |
|              |                   | during       |                   |
|              |                   | Secure       |                   |
|              |                   | Coding stage |                   |
|              |                   | triggered by |                   |
|              |                   | Pull, Clone  |                   |
|              |                   | or Comment   |                   |
|              |                   | trigger.     |                   |
|              |                   | Security     |                   |
|              |                   | testing that |                   |
|              |                   | analyses     |                   |
|              |                   | application  |                   |
|              |                   | source code  |                   |
|              |                   | or compiled  |                   |
|              |                   | code for     |                   |
|              |                   | software     |                   |
|              |                   | components   |                   |
|              |                   | with known   |                   |
|              |                   | vuln         |                   |
|              |                   | erabilities. |                   |
+--------------+-------------------+--------------+-------------------+
| sec.code.003 | IaaC              | Source Code  | Typically done    |
|              |                   | Review       | manually.         |
|              |                   | **should**   |                   |
|              |                   | be performed |                   |
|              |                   | continuously |                   |
|              |                   | during       |                   |
|              |                   | Secure       |                   |
|              |                   | Coding       |                   |
|              |                   | stage.       |                   |
+--------------+-------------------+--------------+-------------------+
| sec.code.004 | IaaC              | Integrated   |                   |
|              |                   | SAST via IDE |                   |
|              |                   | Plugins      |                   |
|              |                   | **should**   |                   |
|              |                   | be used      |                   |
|              |                   | during       |                   |
|              |                   | Secure       |                   |
|              |                   | Coding stage |                   |
|              |                   | triggered by |                   |
|              |                   | Developer    |                   |
|              |                   | Code         |                   |
|              |                   | trigger. On  |                   |
|              |                   | the local    |                   |
|              |                   | machine:     |                   |
|              |                   | through the  |                   |
|              |                   | IDE or       |                   |
|              |                   | integrated   |                   |
|              |                   | test suites; |                   |
|              |                   | triggered on |                   |
|              |                   | completion   |                   |
|              |                   | of coding by |                   |
|              |                   | developer.   |                   |
+--------------+-------------------+--------------+-------------------+
| sec.code.005 | IaaC              | SAST of      |                   |
|              |                   | Source Code  |                   |
|              |                   | Repo         |                   |
|              |                   | **should**   |                   |
|              |                   | be performed |                   |
|              |                   | during       |                   |
|              |                   | Secure       |                   |
|              |                   | Coding stage |                   |
|              |                   | triggered by |                   |
|              |                   | Developer    |                   |
|              |                   | Code         |                   |
|              |                   | trigger.     |                   |
|              |                   | Continuous   |                   |
|              |                   | delivery     |                   |
|              |                   | pre          |                   |
|              |                   | -deployment: |                   |
|              |                   | scanning     |                   |
|              |                   | prior to     |                   |
|              |                   | deployment.  |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-42: Reference Model Requirements: IaaC Security, Secure Code
Stage

**Continuous Build, Integration and Testing Stage Requirements**

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.bld.001  | IaaC              | SAST -Static | Example: open     |
|              |                   | Application  | source OWASP      |
|              |                   | Security     | range of tools.   |
|              |                   | Testing      |                   |
|              |                   | **should**   |                   |
|              |                   | be applied   |                   |
|              |                   | during the   |                   |
|              |                   | Continuous   |                   |
|              |                   | Build,       |                   |
|              |                   | Integration  |                   |
|              |                   | and Testing  |                   |
|              |                   | stage        |                   |
|              |                   | triggered by |                   |
|              |                   | Build and    |                   |
|              |                   | Integrate    |                   |
|              |                   | trigger.     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.bld.002  | IaaC              | SCA –        | Example: open     |
|              |                   | Software     | source OWASP      |
|              |                   | Composition  | range of tools.   |
|              |                   | Analysis     |                   |
|              |                   | **should**   |                   |
|              |                   | be applied   |                   |
|              |                   | during the   |                   |
|              |                   | Continuous   |                   |
|              |                   | Build,       |                   |
|              |                   | Integration  |                   |
|              |                   | and Testing  |                   |
|              |                   | stage        |                   |
|              |                   | triggered by |                   |
|              |                   | Build and    |                   |
|              |                   | Integrate    |                   |
|              |                   | trigger.     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.bld.004  | IaaC              | DAST –       | Example: OWASP    |
|              |                   | Dynamic      | ZAP.              |
|              |                   | Application  |                   |
|              |                   | Security     |                   |
|              |                   | Testing      |                   |
|              |                   | **should**   |                   |
|              |                   | be applied   |                   |
|              |                   | during the   |                   |
|              |                   | Continuous   |                   |
|              |                   | Build,       |                   |
|              |                   | Integration  |                   |
|              |                   | and Testing  |                   |
|              |                   | stage        |                   |
|              |                   | triggered by |                   |
|              |                   | Stage & Test |                   |
|              |                   | trigger.     |                   |
|              |                   | Security     |                   |
|              |                   | testing that |                   |
|              |                   | analyses a   |                   |
|              |                   | running      |                   |
|              |                   | application  |                   |
|              |                   | by           |                   |
|              |                   | exercising   |                   |
|              |                   | application  |                   |
|              |                   | f            |                   |
|              |                   | unctionality |                   |
|              |                   | and          |                   |
|              |                   | detecting    |                   |
|              |                   | vul          |                   |
|              |                   | nerabilities |                   |
|              |                   | based on     |                   |
|              |                   | application  |                   |
|              |                   | behaviour    |                   |
|              |                   | and          |                   |
|              |                   | response.    |                   |
+--------------+-------------------+--------------+-------------------+
| sec.bld.005  | IaaC              | Fuzzing      | Example: GitLab   |
|              |                   | **should**   | Open Sources      |
|              |                   | be applied   | Protocol Fuzzer   |
|              |                   | during the   | Community         |
|              |                   | Continuous   | Edition.          |
|              |                   | Build,       |                   |
|              |                   | Integration  |                   |
|              |                   | and testing  |                   |
|              |                   | stage        |                   |
|              |                   | triggered by |                   |
|              |                   | Stage & Test |                   |
|              |                   | trigger.     |                   |
|              |                   | Fuzzing or   |                   |
|              |                   | fuzz testing |                   |
|              |                   | is an        |                   |
|              |                   | automated    |                   |
|              |                   | software     |                   |
|              |                   | testing      |                   |
|              |                   | technique    |                   |
|              |                   | that         |                   |
|              |                   | involves     |                   |
|              |                   | providing    |                   |
|              |                   | invalid,     |                   |
|              |                   | unexpected,  |                   |
|              |                   | or random    |                   |
|              |                   | data as      |                   |
|              |                   | inputs to a  |                   |
|              |                   | computer     |                   |
|              |                   | program.     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.bld.006  | IaaC              | IAST –       | Example: Contrast |
|              |                   | Interactive  | Community         |
|              |                   | Application  | Edition.          |
|              |                   | Security     |                   |
|              |                   | Testing      |                   |
|              |                   | **should**   |                   |
|              |                   | be applied   |                   |
|              |                   | during the   |                   |
|              |                   | Continuous   |                   |
|              |                   | Build,       |                   |
|              |                   | Integration  |                   |
|              |                   | and Testing  |                   |
|              |                   | stage        |                   |
|              |                   | triggered by |                   |
|              |                   | Stage & Test |                   |
|              |                   | trigger.     |                   |
|              |                   | Software     |                   |
|              |                   | component    |                   |
|              |                   | deployed     |                   |
|              |                   | with an      |                   |
|              |                   | application  |                   |
|              |                   | that         |                   |
|              |                   | assesses     |                   |
|              |                   | application  |                   |
|              |                   | behaviour    |                   |
|              |                   | and detects  |                   |
|              |                   | presence of  |                   |
|              |                   | vul          |                   |
|              |                   | nerabilities |                   |
|              |                   | on an        |                   |
|              |                   | application  |                   |
|              |                   | being        |                   |
|              |                   | exercised in |                   |
|              |                   | realistic    |                   |
|              |                   | testing      |                   |
|              |                   | scenarios.   |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-43: Reference Model Requirements: IaaC Security, Continuous
Build, Integration and Testing Stage

**Continuous Delivery and Deployment Stage Requirements**

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.del.003  | IaaC              | Artifact and | Example: GitLab   |
|              |                   | Image        | uses the open     |
|              |                   | Repository   | source Clair      |
|              |                   | Scan         | engine for        |
|              |                   | **should**   | container         |
|              |                   | be           | scanning.         |
|              |                   | continuously |                   |
|              |                   | applied      |                   |
|              |                   | during the   |                   |
|              |                   | Continuous   |                   |
|              |                   | Delivery and |                   |
|              |                   | Deployment   |                   |
|              |                   | stage.       |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-44: Reference Model Requirements: IaaC Security, Continuous
Delivery and Deployment Stage

**Runtime Defence and Monitoring Requirements**

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.run.002  | IaaC              | RASP –       |                   |
|              |                   | Runtime      |                   |
|              |                   | Application  |                   |
|              |                   | Sel          |                   |
|              |                   | f-Protection |                   |
|              |                   | **should**   |                   |
|              |                   | be           |                   |
|              |                   | continuously |                   |
|              |                   | applied      |                   |
|              |                   | during the   |                   |
|              |                   | Runtime      |                   |
|              |                   | Defence and  |                   |
|              |                   | Monitoring   |                   |
|              |                   | stage.       |                   |
|              |                   | Security     |                   |
|              |                   | technology   |                   |
|              |                   | deployed     |                   |
|              |                   | within the   |                   |
|              |                   | target       |                   |
|              |                   | application  |                   |
|              |                   | in           |                   |
|              |                   | production   |                   |
|              |                   | for          |                   |
|              |                   | detecting,   |                   |
|              |                   | alerting,    |                   |
|              |                   | and blocking |                   |
|              |                   | attacks.     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.run.003  | IaaC              | Application  | Example: GitLab   |
|              |                   | testing and  | Open Sources      |
|              |                   | Fuzzing      | Protocol Fuzzer   |
|              |                   | **should**   | Community         |
|              |                   | be           | Edition.          |
|              |                   | continuously |                   |
|              |                   | applied      |                   |
|              |                   | during the   |                   |
|              |                   | Runtime      |                   |
|              |                   | Defence and  |                   |
|              |                   | Monitoring   |                   |
|              |                   | stage.       |                   |
|              |                   | Fuzzing or   |                   |
|              |                   | fuzz testing |                   |
|              |                   | is an        |                   |
|              |                   | automated    |                   |
|              |                   | software     |                   |
|              |                   | testing      |                   |
|              |                   | technique    |                   |
|              |                   | that         |                   |
|              |                   | involves     |                   |
|              |                   | providing    |                   |
|              |                   | invalid,     |                   |
|              |                   | unexpected,  |                   |
|              |                   | or random    |                   |
|              |                   | data as      |                   |
|              |                   | inputs to a  |                   |
|              |                   | computer     |                   |
|              |                   | program.     |                   |
+--------------+-------------------+--------------+-------------------+
| sec.run.004  | IaaC              | Penetration  | Typically done    |
|              |                   | Testing      | manually.         |
|              |                   | **should**   |                   |
|              |                   | be           |                   |
|              |                   | continuously |                   |
|              |                   | applied      |                   |
|              |                   | during the   |                   |
|              |                   | Runtime      |                   |
|              |                   | Defence and  |                   |
|              |                   | Monitoring   |                   |
|              |                   | stage.       |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-45: Reference Model Requirements: Iaac Security, Runtime Defence
and Monitoring Stage

.. _compliance-with-standards-source-rm-7.9.10-1:

Compliance with Standards (source `RM 7.9.10 <../../../ref_model/chapters/chapter07.md#7910-compliance-with-standards>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+-------------------+---------------------+---------------+
| Reference | sub-category      | Description         | Notes         |
+===========+===================+=====================+===============+
| se        | Standards         | The Cloud Operator  |               |
| c.std.001 |                   | **should** comply   |               |
|           |                   | with `Center for    |               |
|           |                   | Internet Security   |               |
|           |                   | CIS                 |               |
|           |                   | Con                 |               |
|           |                   | trols <https://www. |               |
|           |                   | cisecurity.org/>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator, |               |
| c.std.002 |                   | Platform and        |               |
|           |                   | Workloads           |               |
|           |                   | **should** follow   |               |
|           |                   | the guidance in the |               |
|           |                   | CSA Security        |               |
|           |                   | Guidance for        |               |
|           |                   | Critical Areas of   |               |
|           |                   | Focus in Cloud      |               |
|           |                   | Computing (latest   |               |
|           |                   | version)- CSA,      |               |
|           |                   | `Cloud Security     |               |
|           |                   | Alliance <          |               |
|           |                   | https://cloudsecuri |               |
|           |                   | tyalliance.org/>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Platform and    |               |
| c.std.003 |                   | Workloads           |               |
|           |                   | **should** follow   |               |
|           |                   | the guidance in the |               |
|           |                   | `OWASP Cheat Sheet  |               |
|           |                   | Series              |               |
|           |                   | (OCSS) <https://    |               |
|           |                   | github.com/OWASP/Ch |               |
|           |                   | eatSheetSeries>`__- |               |
|           |                   | OWASP, `Open Web    |               |
|           |                   | Application         |               |
|           |                   | Security            |               |
|           |                   | Project <https:     |               |
|           |                   | //www.owasp.org>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator, |               |
| c.std.004 |                   | Platform and        |               |
|           |                   | Workloads           |               |
|           |                   | **should** ensure   |               |
|           |                   | that their code is  |               |
|           |                   | not vulnerable to   |               |
|           |                   | the `OWASP Top Ten  |               |
|           |                   | Security            |               |
|           |                   | Risks <http         |               |
|           |                   | s://owasp.org/www-p |               |
|           |                   | roject-top-ten/>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator, |               |
| c.std.005 |                   | Platform and        |               |
|           |                   | Workloads           |               |
|           |                   | **should** strive   |               |
|           |                   | to improve their    |               |
|           |                   | maturity on the     |               |
|           |                   | `OWASP Software     |               |
|           |                   | Maturity Model      |               |
|           |                   | (                   |               |
|           |                   | SAMM) <https://owas |               |
|           |                   | psamm.org/blog/2019 |               |
|           |                   | /12/20/version2-com |               |
|           |                   | munity-release/>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator, |               |
| c.std.006 |                   | Platform and        |               |
|           |                   | Workloads           |               |
|           |                   | **should** utilise  |               |
|           |                   | the `OWASP Web      |               |
|           |                   | Security Testing    |               |
|           |                   | Guid                |               |
|           |                   | e <https://github.c |               |
|           |                   | om/OWASP/wstg/tree/ |               |
|           |                   | master/document>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator, |               |
| c.std.007 |                   | and Platform        |               |
|           |                   | **should** satisfy  |               |
|           |                   | the requirements    |               |
|           |                   | for Information     |               |
|           |                   | Management Systems  |               |
|           |                   | specified in        |               |
|           |                   | `ISO/IEC            |               |
|           |                   | 27001 <https://     |               |
|           |                   | www.iso.org/obp/ui/ |               |
|           |                   | #iso:std:iso-iec:27 |               |
|           |                   | 001:ed-2:v1:en>`__; |               |
|           |                   | ISO/IEC 27001 is    |               |
|           |                   | the international   |               |
|           |                   | Standard for        |               |
|           |                   | best-practice       |               |
|           |                   | information         |               |
|           |                   | security management |               |
|           |                   | systems (ISMSs)     |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator, |               |
| c.std.008 |                   | and Platform        |               |
|           |                   | **should**          |               |
|           |                   | implement the Code  |               |
|           |                   | of practice for     |               |
|           |                   | Security Controls   |               |
|           |                   | specified `ISO/IEC  |               |
|           |                   | 27002:2013 (or      |               |
|           |                   | latest) <https:/    |               |
|           |                   | /www.iso.org/obp/ui |               |
|           |                   | /#iso:std:iso-iec:2 |               |
|           |                   | 7002:ed-2:v1:en>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator, |               |
| c.std.009 |                   | and Platform        |               |
|           |                   | **should**          |               |
|           |                   | implement the       |               |
|           |                   | `ISO/IEC 27032:2012 |               |
|           |                   | (or latest)         |               |
|           |                   | Guidelines for      |               |
|           |                   | Cybersecurity       |               |
|           |                   | t                   |               |
|           |                   | echniques <https:// |               |
|           |                   | www.iso.org/obp/ui/ |               |
|           |                   | #iso:std:iso-iec:27 |               |
|           |                   | 032:ed-1:v1:en>`__; |               |
|           |                   | ISO/IEC 27032 is    |               |
|           |                   | the international   |               |
|           |                   | Standard focusing   |               |
|           |                   | explicitly on       |               |
|           |                   | cybersecurity       |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator  |               |
| c.std.010 |                   | **should** conform  |               |
|           |                   | to the ISO/IEC      |               |
|           |                   | 27035 standard for  |               |
|           |                   | incidence           |               |
|           |                   | management; ISO/IEC |               |
|           |                   | 27035 is the        |               |
|           |                   | international       |               |
|           |                   | Standard for        |               |
|           |                   | incident management |               |
+-----------+-------------------+---------------------+---------------+
| se        | Standards         | The Cloud Operator  |               |
| c.std.011 |                   | **should** conform  |               |
|           |                   | to the ISO/IEC      |               |
|           |                   | 27031 standard for  |               |
|           |                   | business            |               |
|           |                   | continuity; ISO/IEC |               |
|           |                   | 27031 - ISO/IEC     |               |
|           |                   | 27031 is the        |               |
|           |                   | international       |               |
|           |                   | Standard for ICT    |               |
|           |                   | readiness for       |               |
|           |                   | business continuity |               |
+-----------+-------------------+---------------------+---------------+

Table 2-46: Security Recommendations
