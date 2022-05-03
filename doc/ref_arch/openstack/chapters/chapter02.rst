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

This chapter includes both "Requirements" that must be satisifed in an
RA-1 conformant implementation and "Recommendations" that are optional
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

Cloud Infrastructure Software Profile Requirements for Compute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter05:cloud infrastructure software profiles features and requirements`)

+-------------------+----------------+-------------+-------------+---------------+
| Reference         | Description    | Requirement | Requirement | Specification |
|                   |                | for Basic   | for High    | Reference     |
|                   |                | Profile     | Performance |               |
|                   |                |             | Profile     |               |
+===================+================+=============+=============+===============+
| e.cap.001         | Max number     | At least 16 | At least 16 |               |
|                   | of vCPU        |             |             |               |
|                   | that can be    |             |             |               |
|                   | assigned to    |             |             |               |
|                   | a single       |             |             |               |
|                   | instance by    |             |             |               |
|                   | the Cloud      |             |             |               |
|                   | Infrastructure |             |             |               |
+-------------------+----------------+-------------+-------------+---------------+
| e.cap.002         | Max memory     | at least 32 | at least 32 |               |
|                   | that can be    | GB          | GB          |               |
|                   | assigned to    |             |             |               |
|                   | a single       |             |             |               |
|                   | instance by    |             |             |               |
|                   | the Cloud      |             |             |               |
|                   | Infrastructure |             |             |               |
+-------------------+----------------+-------------+-------------+---------------+
| e.cap.003         | Max storage    | at least    | at least    |               |
|                   | that can be    | 320 GB      | 320 GB      |               |
|                   | assigned to    |             |             |               |
|                   | a single       |             |             |               |
|                   | instance by    |             |             |               |
|                   | the Cloud      |             |             |               |
|                   | Infrastructure |             |             |               |
+-------------------+----------------+-------------+-------------+---------------+
| e.cap.004         | Max number     | 6           | 6           |               |
|                   | of             |             |             |               |
|                   | connection     |             |             |               |
|                   | points that    |             |             |               |
|                   | can be         |             |             |               |
|                   | assigned to    |             |             |               |
|                   | a single       |             |             |               |
|                   | instance by    |             |             |               |
|                   | the Cloud      |             |             |               |
|                   | Infrastructure |             |             |               |
+-------------------+----------------+-------------+-------------+---------------+
| e.cap.005         | Max storage    | Up to 16TB1 | Up to 16TB1 |               |
|                   | that can be    |             |             |               |
|                   | attached /     |             |             |               |
|                   | mounted to     |             |             |               |
|                   | an instance    |             |             |               |
|                   | by the         |             |             |               |
|                   | Cloud          |             |             |               |
|                   | Infrastructure |             |             |               |
+-------------------+----------------+-------------+-------------+---------------+
| e.cap.006/\       | CPU pinning    | Not         | Must        |               |
| infra.com.cfg.003 | support        | required    | support     |               |
+-------------------+----------------+-------------+-------------+---------------+
| e.cap.007/\       | NUMA           | Not         | Must        |               |
| infra.com.cfg.002 | support        | required    | support     |               |
+-------------------+----------------+-------------+-------------+---------------+
| e.cap.018/\       | Simultaneous   | Must        | Optional    |               |
| infra.com.cfg.005 | Multithreading |             | support     |               |
|                   | (SMT) enabled  |             |             |               |
+-------------------+----------------+-------------+-------------+---------------+
| i.cap.018/\       | Huge pages     | Not         | Must        |               |
| infra.com.cfg.004 | configured     | required    | support     |               |
+-------------------+----------------+-------------+-------------+---------------+

Table 2-1a: Reference Model Requirements: Cloud Infrastructure Software
Profile Capabilities

   **1** Defined in the ``.bronze`` configuration in
   :ref:`ref_model/chapters/chapter04:storage extensions`

Cloud Infrastructure Software Profile Extensions Requirements for Compute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+--------------+---------------+-------------+---------------+
| Reference             | Description  | Profile       | Profile     | Specification |
|                       |              | Extensions    | Extra-Specs | Reference     |
+=======================+==============+===============+=============+===============+
| e.cap.008/\           | IPSec        | Compute       |             |               |
| infra.com.acc.cfg.001 | Acceleration | Intensive     |             |               |
|                       | using the    | GPU           |             |               |
|                       | virtio-ipsec |               |             |               |
|                       | interface    |               |             |               |
+-----------------------+--------------+---------------+-------------+---------------+
| e.cap.010/\           | Transcoding  | Compute       | Video       |               |
| infra.com.acc.cfg.002 | Acceleration | Intensive GPU | Transcoding |               |
+-----------------------+--------------+---------------+-------------+---------------+
| e.cap.011/\           | Programmable | Firmware-\    | Accelerator |               |
| infra.com.acc.cfg.003 | Acceleration | programmable  |             |               |
|                       |              | adapter       |             |               |
+-----------------------+--------------+---------------+-------------+---------------+
| e.cap.012             | Enhanced     | E             | E           |               |
|                       | Cache        |               |             |               |
|                       | Management:  |               |             |               |
|                       | L=Lean;      |               |             |               |
|                       | E=Equal;     |               |             |               |
|                       | X=eXpanded   |               |             |               |
+-----------------------+--------------+---------------+-------------+---------------+
| e.cap.014/\           | Hardware     | Compute       |             |               |
| infra.com.acc.cfg.004 | coprocessor  | Intensive     |             |               |
|                       | support      | GPU           |             |               |
|                       | (GPU/NPU)    |               |             |               |
+-----------------------+--------------+---------------+-------------+---------------+
| e.cap.016/\           | FPGA/other   | Firmware-\    |             |               |
| infra.com.acc.cfg.005 | Acceleration | programmable  |             |               |
|                       | H/W          | adapter       |             |               |
+-----------------------+--------------+---------------+-------------+---------------+

Table 2-1b: Cloud Infrastructure Software Profile Extensions
Requirements for Compute

Cloud Infrastructure Software Profile Requirements for Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter05:virtual networking`)

The features and configuration requirements related to virtual
networking for the two (2) types of Cloud Infrastructure Profiles are
specified below followed by networking bandwidth requirements.

+-------------------+---------------------+-------------+-------------+---------------+
| Reference         | Description         | Requirement | Requirement | Specification |
|                   |                     | for Basic   | for         | Reference     |
|                   |                     | Profile     | High-\      |               |
|                   |                     |             | Performance |               |
|                   |                     |             | Profile     |               |
+===================+=====================+=============+=============+===============+
| infra.net.cfg.001 | IO                  | Must        | Must        |               |
|                   | virtualisation      | support     | support     |               |
|                   | using               |             |             |               |
|                   | virtio1.1           |             |             |               |
+-------------------+---------------------+-------------+-------------+---------------+
| infra.net.cfg.002 | The overlay network | Must        | *No         |               |
|                   | encapsulation       | support     | requirement |               |
|                   | protocol needs to   | VXLAN,      | specified*  |               |
|                   | enable ECMP in the  | MPLSoUDP,   |             |               |
|                   | underlay to take    | GENEVE,     |             |               |
|                   | advantage of the    | other       |             |               |
|                   | scale-out features  |             |             |               |
|                   | of the network      |             |             |               |
|                   | fabric              |             |             |               |
+-------------------+---------------------+-------------+-------------+---------------+
| infra.net.cfg.003 | Network Address     | Must        | Must        |               |
|                   | Translation         | support     | support     |               |
|                   |                     |             |             |               |
+-------------------+---------------------+-------------+-------------+---------------+
| infra.net.cfg.004 | Security            | Must        | Must        |               |
|                   | Groups              | support     | support     |               |
+-------------------+---------------------+-------------+-------------+---------------+
| infra.net.cfg.005 | SFC support         | Not         | Must        |               |
|                   |                     | required    | support     |               |
+-------------------+---------------------+-------------+-------------+---------------+
| infra.net.cfg.006 | Traffic patterns    | Must        | Must        |               |
|                   | symmetry            | support     | support     |               |
+-------------------+---------------------+-------------+-------------+---------------+

Table 2-2a: Reference Model Requirements - Virtual Networking

The required number of connection points to an instance is described in
``e.cap.004`` `above <#2.2.1>`__. The table below specifies the required
bandwidth of those connection points.

+-------------+-------------+-------------+-------------+---------------+
| Reference   | Description | Requirement | Requirement | Specification |
|             |             | for Basic   | for High    | Reference     |
|             |             | Profile     | Performance |               |
|             |             |             | Profile     |               |
+=============+=============+=============+=============+===============+
| n1, n2, n3, | 1, 2, 3, 4, | Must        | Must        |               |
| n4, n5, n6  | 5, 6 Gbps   | support     | support     |               |
+-------------+-------------+-------------+-------------+---------------+
| n10, n20,   | 10, 20, 30, | Must        | Must        |               |
| n30, n40,   | 40, 50, 60  | support     | support     |               |
| n50, n60    | Gbps        |             |             |               |
+-------------+-------------+-------------+-------------+---------------+
| n25, n50,   | 25, 50, 75, | Optional    | Must        |               |
| n75, n100,  | 100, 125,   |             | support     |               |
| n125, n150  | 150 Gbps    |             |             |               |
+-------------+-------------+-------------+-------------+---------------+
| n50, n100,  | 50, 100,    | Optional    | Must        |               |
| n150, n200, | 150, 200,   |             | support     |               |
| n250, n300  | 250, 300    |             |             |               |
|             | Gbps        |             |             |               |
+-------------+-------------+-------------+-------------+---------------+
| n100, n200, | 100, 200,   | Optional    | Must        |               |
| n300, n400, | 300, 400,   |             | support     |               |
| n500, n600  | 500, 600    |             |             |               |
|             | Gbps        |             |             |               |
+-------------+-------------+-------------+-------------+---------------+

Table 2-2b: Reference Model Requirements - Network Interface
Specifications

Cloud Infrastructure Software Profile Extensions Requirements for Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+--------------+-------------+-------------+---------------+
| Reference             | Description  | Requirement | Requirement | Specification |
|                       |              | for Basic   | for High-\  | Reference     |
|                       |              | Profile     | Performance |               |
|                       |              |             | Profile     |               |
+=======================+==============+=============+=============+===============+
| e.cap.013/\           | SR-IOV over  | N           | Y           |               |
| infra.hw.nac.cfg.004  | PCI-PT       |             |             |               |
+-----------------------+--------------+-------------+-------------+---------------+
| e.cap.019/\           | vSwitch      | N           | Y           |               |
| infra.net.acc.cfg.001 | optimisation |             |             |               |
|                       | (DPDK)       |             |             |               |
+-----------------------+--------------+-------------+-------------+---------------+
| e.cap.015/\           | SmartNIC     | N           | Optional    |               |
| infra.net.acc.cfg.002 | (for HW      |             |             |               |
|                       | Offload)     |             |             |               |
+-----------------------+--------------+-------------+-------------+---------------+
| e.cap.009/\           | Crypto       | N           | Optional    |               |
| infra.net.acc.cfg.003 | acceleration |             |             |               |
+-----------------------+--------------+-------------+-------------+---------------+
| infra.net.acc.cfg.004 | Crypto       | N           | Optional    |               |
|                       | Acceleration |             |             |               |
|                       | Interface    |             |             |               |
+-----------------------+--------------+-------------+-------------+---------------+

Table 2-2c: Cloud Infrastructure Software Profile Extensions
Requirements for Networking

Cloud Infrastructure Software Profile Requirements for Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter05:cloud infrastructure software profiles features and requirements`)

+-----------------------+-------------+-------------+-------------+---------------+
| Reference             | Description | Requirement | Requirement | Specification |
|                       |             | for Basic   | for         | Reference     |
|                       |             | Profile     | High-\      |               |
|                       |             |             | Performance |               |
|                       |             |             | Profile     |               |
+=======================+=============+=============+=============+===============+
| infra.stg.cfg.002     | Storage     | Must        | Must        |               |
|                       | Block       | support     | support     |               |
+-----------------------+-------------+-------------+-------------+---------------+
| infra.stg.cfg.003     | Storage     | Not         | Must        |               |
|                       | with        | required    | support     |               |
|                       | replication |             |             |               |
+-----------------------+-------------+-------------+-------------+---------------+
| infra.stg.cfg.004     | Storage     | Must        | Must        |               |
|                       | with        | support     | support     |               |
|                       | encryption  |             |             |               |
+-----------------------+-------------+-------------+-------------+---------------+
| infra.stg.acc.cfg.001 | Storage     | Not         | Must        |               |
|                       | IOPS        | required    | support     |               |
|                       | oriented    |             |             |               |
+-----------------------+-------------+-------------+-------------+---------------+
| infra.stg.acc.cfg.002 | Storage     | Not         | Not         |               |
|                       | capacity    | required    | required    |               |
|                       | oriented    |             |             |               |
+-----------------------+-------------+-------------+-------------+---------------+

Table 2-3a: Reference Model Requirements - Cloud Infrastructure Software
Profile Requirements for Storage

Cloud Infrastructure Software Profile Extensions Requirements for Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-------------+-------------+-------------+---------------+
| Reference             | Description | Profile     | Profile     | Specification |
|                       |             | Extensions  | Extra-Specs |               |
|                       |             |             |             |               |
+=======================+=============+=============+=============+===============+
| infra.stg.acc.cfg.001 | Storage     | Storage     |             |               |
|                       | IOPS        | Intensive   |             |               |
|                       | oriented    | High-\      |             |               |
|                       |             | performance |             |               |
|                       |             | storage     |             |               |
+-----------------------+-------------+-------------+-------------+---------------+
| infra.stg.acc.cfg.002 | Storage     | High        |             |               |
|                       | capacity    | Capacity    |             |               |
|                       | oriented    |             |             |               |
+-----------------------+-------------+-------------+-------------+---------------+

Table 2-3b: Reference Model Requirements - Cloud Infrastructure Software
Profile Extensions Requirements for Storage

Cloud Infrastructure Hardware Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter05:cloud infrastructure hardware profiles features and requirements.`)

+--------------------------+------------------+-------------+-------------+---------------+
| Reference                | Description      | Requirement | Requirement | Specification |
|                          |                  | for Basic   | for         |               |
|                          |                  | Profile     | High-\      | Reference     |
|                          |                  |             | Performance |               |
|                          |                  |             | Profile     |               |
+==========================+==================+=============+=============+===============+
| infra.hw.001             | CPU Architecture |             |             |               |
|                          | (Values such as  |             |             |               |
|                          | x64, ARM, etc.)  |             |             |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.cpu.cfg.001     | Minimum number   | 2           | 2           |               |
|                          | of CPU (Sockets) |             |             |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.cpu.cfg.002     | Minimum number   | 20          | 20          |               |
|                          | of Cores per CPU |             |             |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.cpu.cfg.003     | NUMA             | Not         | Must        |               |
|                          |                  | required    | support     |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.cpu.cfg.004     | Simultaneous     | Must        | Optional    |               |
|                          | Multithreading/\ | support     |             |               |
|                          | Symmetric        |             |             |               |
|                          | Multiprocessing  |             |             |               |
|                          | (SMT/SMP)        |             |             |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.stg.hdd.cfg.001 | Local            | *No         | *No         |               |
|                          | Storage HDD      | requirement | requirement |               |
|                          |                  | specified*  | specified*  |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.stg.ssd.cfg.002 | Local            | Should      | Should      |               |
|                          | Storage SSD      | support     | support     |               |
|                          |                  |             |             |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.nic.cfg.001     | Total Number of  | 4           | 4           |               |
|                          | NIC Ports        |             |             |               |
|                          | available in the |             |             |               |
|                          | host             |             |             |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.nic.cfg.002     | Port speed       | 10          | 25          |               |
|                          | specified in     |             |             |               |
|                          | Gbps (minimum    |             |             |               |
|                          | values)          |             |             |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.pci.cfg.001     | Number of PCIe   | 8           | 8           |               |
|                          | slots            |             |             |               |
|                          | available in     |             |             |               |
|                          | the host         |             |             |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.pci.cfg.002     | PCIe speed       | Gen 3       | Gen 3       |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.pci.cfg.003     | PCIe Lanes       | 8           | 8           |               |
+--------------------------+------------------+-------------+-------------+---------------+
| infra.hw.nac.cfg.003     | Compression      | *No         | *No         |               |
|                          |                  | requirement | requirement |               |
|                          |                  | specified*  | specified*  |               |
+--------------------------+------------------+-------------+-------------+---------------+

Table 2-4a: Reference Model Requirements - Cloud Infrastructure Hardware
Profile Requirements

Cloud Infrastructure Hardware Profile-Extensions Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter05:cloud infrastructure hardware profiles features and requirements.`)

+----------------------+-------------+-------------+-------------+---------------+
| Reference            | Description | Requirement | Requirement | Specification |
|                      |             | for Basic   | for         | Reference     |
|                      |             | Profile     | High-\      |               |
|                      |             |             | Performance |               |
|                      |             |             | Profile     |               |
+======================+==============+============+=============+===============+
| e.cap.014/\          | GPU          | N          | Optional    |               |
| infra.hw.cac.cfg.001 |              |            |             |               |
+----------------------+--------------+------------+-------------+---------------+
| e.cap.016/\          | FPGA/other   | N          | Optional    |               |
| infra.hw.cac.cfg.002 | Acceleration |            |             |               |
|                      | H/W          |            |             |               |
+----------------------+--------------+------------+-------------+---------------+
| e.cap.009/\          | Crypto       | N          | Optional    |               |
| infra.hw.nac.cfg.001 | Acceleration |            |             |               |
+----------------------+--------------+------------+-------------+---------------+
| e.cap.015/\          | SmartNIC     | N          | Optional    |               |
| infra.hw.nac.cfg.002 |              |            |             |               |
+----------------------+--------------+------------+-------------+---------------+
| infra.hw.nac.cfg.003 | Compression  | Optional   | Optional    |               |
+----------------------+--------------+------------+-------------+---------------+
| e.cap.013/\          | SR-IOV over  | N          | Yes         |               |
| infra.hw.nac.cfg.004 | PCI-PT       |            |             |               |
+----------------------+--------------+------------+-------------+---------------+

Table 2-4b: Reference Model Requirements - Cloud Infrastructure Hardware
Profile Extensions Requirements

Cloud Infrastructure Management Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter04:cloud infrastructure management capabilities`)

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

System Hardening Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:system hardening requirements`)

+-------------+-----------+---------------------------------+--------------------------------------------------------+
| Reference   | sub-\     | Description                     | Specification Reference                                |
|             | category  |                                 |                                                        |
+=============+===========+=================================+========================================================+
| sec.gen.001 | Hardening | The Platform **must**           | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | maintain the specified          | security lcm`                                          |
|             |           | configuration.                  |                                                        |
|             |           |                                 | :ref:`ref_arch/openstack/chapters/chapter07:\          |
|             |           |                                 | cloud infrastructure and vim configuration management` |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.002 | Hardening | All systems part of Cloud       | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | Infrastructure **must**         | password policy`                                       |
|             |           | support hardening as defined in |                                                        |
|             |           | `CIS Password Policy Guide      |                                                        |
|             |           | <https://www.cisecurity.org\\   |                                                        |
|             |           | white-papers/cis-password-\     |                                                        |
|             |           | policy-guide/>`__.              |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.003 | Hardening | All servers part of Cloud       | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | Infrastructure **must** support | server boot hardening`                                 |
|             |           | a root of trust and secure      |                                                        |
|             |           | boot.                           |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.004 | Hardening | The Operating Systems of all    | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | the servers part  of Cloud      | function and software`                                 |
|             |           | Infrastructure **must** be      |                                                        |
|             |           | hardened by removing or         |                                                        |
|             |           | disabling unnecessary services, |                                                        |
|             |           | applications and network        |                                                        |
|             |           | protocols, configuring          |                                                        |
|             |           | operating system user           |                                                        |
|             |           | authentication, configuring     |                                                        |
|             |           | resource controls, installing   |                                                        |
|             |           | and configuring additional      |                                                        |
|             |           | security controls where needed, |                                                        |
|             |           | and testing the security of the |                                                        |
|             |           | Operating System                |                                                        |
|             |           | (NIST SP 800-123).              |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.005 | Hardening | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | Operating System level access   | system access`                                         |
|             |           | control.                        |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.006 | Hardening | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | Secure logging. Logging with    | system access`                                         |
|             |           | root account must be prohibited |                                                        |
|             |           | when root privileges are not    |                                                        |
|             |           | required.                       |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.007 | Hardening | All servers part of Cloud       | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | Infrastructure **must** be Time | security logs time synchronisation`                    |
|             |           | synchronised with authenticated |                                                        |
|             |           | Time service.                   |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.008 | Hardening | All servers part of Cloud       | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | Infrastructure  **must** be     | security lcm`                                          |
|             |           | regularly updated to address    |                                                        |
|             |           | security vulnerabilities.       |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.009 | Hardening | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | software integrity protection   | integrity of openstack components configuration`       |
|             |           | and verification.               |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.010 | Hardening | The Cloud Infrastructure        | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | encrypted storage, for example, | confidentiality and integrity`                         |
|             |           | block, object and file storage  |                                                        |
|             |           | access to encryption keys       |                                                        |
|             |           | restricted based on a need to   |                                                        |
|             |           | know (`Controlled Access Based  |                                                        |
|             |           | on the Need to Know             |                                                        |
|             |           | <https://www.cisecurity.org\\   |                                                        |
|             |           | controls/controlled-access-\    |                                                        |
|             |           | based-on-the-need-to-know/>`__\ |                                                        |
|             |           | ).                              |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.012 | Hardening | The Operator **must** ensure    | This requirement\'s verification goes beyond Anuket    |
|             |           | that only authorised actors     | testing scope                                          |
|             |           | have physical access to the     |                                                        |
|             |           | underlying infrastructure.      |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.013 | Hardening | The Platform **must** ensure    | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | that only authorised actors     | system access`                                         |
|             |           | have logical access to the      |                                                        |
|             |           | underlying infrastructure.      |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.gen.015 | Hardening | Any change to the Platform      | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | **must** be logged as a         | security lcm`                                          |
|             |           | security event, and the logged  |                                                        |
|             |           | event must include the          |                                                        |
|             |           | identity of the entity making   |                                                        |
|             |           | the change, the change, the     |                                                        |
|             |           | date and the time of the        |                                                        |
|             |           | change.                         |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+

Table 2-6: Reference Model Requirements - System Hardening Requirements

Platform and Access Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:platform and access requirements`)

+-------------+-----------+---------------------------------+--------------------------------------------------------+
| Reference   | sub-\     | Description                     | Specification Reference                                |
|             | category  |                                 |                                                        |
+=============+===========+=================================+========================================================+
| sec.sys.001 | Access    | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:rbac`      |
|             |           | authenticated and secure access |                                                        |
|             |           | to API, GUI and command line    |                                                        |
|             |           | interfaces                      |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.002 | Access    | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | Traffic Filtering for           | workload security`                                     |
|             |           | workloads (for example,         |                                                        |
|             |           | Firewall).                      |                                                        |
|             |           |                                 |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.003 | Access    | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | Secure and encrypted            | confidentiality and integrity`                         |
|             |           | communications, and             |                                                        |
|             |           | confidentiality and integrity   |                                                        |
|             |           | of network                      |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.004 | Access    | The Cloud Infrastructure        | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | **must** support                | confidentiality and integrity`                    `    |
|             |           | authentication, integrity and   |                                                        |
|             |           | confidentiality on all          |                                                        |
|             |           | network channels.               |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.005 | Access    | The Cloud Infrastructure        | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | **must** segregate the underlay | confidentiality and integrity`                         |
|             |           | and overlay networks.           |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.006 | Access    | The Cloud Infrastructure        | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | **must** be able to utilise     | identity security`                                     |
|             |           | the Cloud Infrastructure        |                                                        |
|             |           | Manager identity lifecycle      |                                                        |
|             |           | management capabilities.        |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.007 | Access    | The Platform **must** implement | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | controls enforcing separation   | rbac`                                                  |
|             |           | of duties and privileges, least |                                                        |
|             |           | privilege use and least common  |                                                        |
|             |           | mechanism (Role-Based Access    |                                                        |
|             |           | Control).                       |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.008 | Access    | The Platform **must** be able   | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | to assign the Entities that     | workload security`                                     |
|             |           | comprise the tenant networks to |                                                        |
|             |           | different trust domains.        |                                                        |
|             |           | (Communication between          |                                                        |
|             |           | different trust domains is not  |                                                        |
|             |           | allowed, by default.)           |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.009 | Access    | The Platform **must** support   |                                                        |
|             |           | creation of Trust Relationships |                                                        |
|             |           | between trust domains. These    |                                                        |
|             |           | maybe uni-directional           |                                                        |
|             |           | relationships where the         |                                                        |
|             |           | trusting domain trusts another  |                                                        |
|             |           | domain (the "trusted domain")   |                                                        |
|             |           | to authenticate users for them  |                                                        |
|             |           | them or to allow access to its  |                                                        |
|             |           | resources from the trusted      |                                                        |
|             |           | domain. In a bidirectional      |                                                        |
|             |           | relationship both domain are    |                                                        |
|             |           | "trusting" and "trusted".       |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.010 | Access    | For two or more domains         |                                                        |
|             |           | without existing trust          |                                                        |
|             |           | relationships, the Platform     |                                                        |
|             |           | **must not** allow the effect   |                                                        |
|             |           | of an attack on one domain to   |                                                        |
|             |           | impact the other domains either |                                                        |
|             |           | directly or indirectly.         |                                                        |
|             |           |                                 |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.011 | Access    | The Platform **must not**       | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | reuse the same authentication   | system access`                                         |
|             |           | credentials (e.g., key  pairs)  |                                                        |
|             |           | on different Platform           |                                                        |
|             |           | components (e.g., different     |                                                        |
|             |           | hosts, or different services).  |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.012 | Access    | The Platform **must** protect   |                                                        |
|             |           | all secrets by using strong     |                                                        |
|             |           | encryption techniques and       |                                                        |
|             |           | storing the protected secrets   |                                                        |
|             |           | externally from the component   |                                                        |
|             |           | (e.g., in OpenStack Barbican)   |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.013 | Access    | The Platform **must** generate  |                                                        |
|             |           | secrets dynamically as and when |                                                        |
|             |           | needed.                         |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.015 | Access    | The Platform **must not**       |                                                        |
|             |           | contain back door entries       |                                                        |
|             |           | (unpublished access points,     |                                                        |
|             |           | APIs,  etc.).                   |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.016 | Access    | Login access to the Platform’s  | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | components **must** be through  | security lcm`                                          |
|             |           | encrypted protocols such as SSH |                                                        |
|             |           | v2 or TLS v1.2 or higher. Note: |                                                        |
|             |           | Hardened jump servers isolated  |                                                        |
|             |           | from external networks are      |                                                        |
|             |           | recommended                     |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.017 | Access    | The Platform **must** provide   | :ref:`ref_arch/openstack/chapters/chapter06:\          |
|             |           | the capability of using digital | confidentiality and integrity`                         |
|             |           | certificates that comply with   |                                                        |
|             |           | X.509 standards issued by a     |                                                        |
|             |           | trusted Certification           |                                                        |
|             |           | Authority.                      |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.018 | Access    | The Platform **must** provide   |                                                        |
|             |           | the capability of allowing      |                                                        |
|             |           | certificate renewal and         |                                                        |
|             |           | revocation.                     |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+
| sec.sys.019 | Access    | The Platform **must** provide   |                                                        |
|             |           | the capability of testing the   |                                                        |
|             |           | validity of a digital           |                                                        |
|             |           | certificate (CA signature,      |                                                        |
|             |           | validity period, non revocation |                                                        |
|             |           | identity).                      |                                                        |
+-------------+-----------+---------------------------------+--------------------------------------------------------+

Table 2-7: Reference Model Requirements - Platform and Access
Requirements

Confidentiality and Integrity Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:confidentiality and integrity requirements`)

+-------------+------------------+-----------------------------------+-----------------------------------------------+
| Reference   | sub-category     | Description                       | Specification Reference                       |
+=============+==================+===================================+===============================================+
| sec.ci.001  | Confidentiality\ | The Platform **must** support     | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|             | /Integrity       | Confidentiality and Integrity of  | confidentiality and integrity`                |
|             |                  | data at rest and in transit.      |                                               |
+-------------+------------------+-----------------------------------+-----------------------------------------------+
| sec.ci.003  | Confidentiality\ | The Platform **must** support     |                                               |
|             | /Integrity       | Confidentiality and Integrity of  |                                               |
|             |                  | data related metadata.            |                                               |
+-------------+------------------+-----------------------------------+-----------------------------------------------+
| sec.ci.004  | Confidentiality  | The Platform **must** support     |                                               |
|             |                  | Confidentiality of processes and  |                                               |
|             |                  | restrict information sharing with |                                               |
|             |                  | only the process owner (e.g.,     |                                               |
|             |                  | tenant).                          |                                               |
+-------------+------------------+-----------------------------------+-----------------------------------------------+
| sec.ci.005  | Confidentiality\ | The Platform **must** support     |                                               |
|             | /Integrity       | Confidentiality and Integrity of  |                                               |
|             |                  | process-related metadata and      |                                               |
|             |                  | restrict information sharing with |                                               |
|             |                  | only the process owner (e.g.,     |                                               |
|             |                  | tenant).                          |                                               |
+-------------+------------------+-----------------------------------+-----------------------------------------------+
| sec.ci.006  | Confidentiality\ | The Platform **must** support     |                                               |
|             | /Integrity       | Confidentiality and Integrity of  |                                               |
|             |                  | workload resource utilisation     |                                               |
|             |                  | (RAM, CPU, Storage, Network I/O,  |                                               |
|             |                  | cache, hardware offload) and      |                                               |
|             |                  | restrict information sharing with |                                               |
|             |                  | only the workload owner (e.g.,    |                                               |
|             |                  | tenant).                          |                                               |
+-------------+------------------+-----------------------------------+-----------------------------------------------+
| sec.ci.007  | Confidentiality\ | The Platform **must not** allow   |                                               |
|             | /Integrity       | Memory Inspection by any actor    |                                               |
|             |                  | other than the authorised actors  |                                               |
|             |                  | for the Entity to which Memory is |                                               |
|             |                  | assigned (e.g., tenants owning    |                                               |
|             |                  | the workload), for Lawful         |                                               |
|             |                  | Inspection, and for secure        |                                               |
|             |                  | monitoring services.              |                                               |
|             |                  | Administrative access must be     |                                               |
|             |                  | managed using Platform Identity   |                                               |
|             |                  | Lifecycle Management.             |                                               |
+-------------+------------------+-----------------------------------+-----------------------------------------------+
| sec.ci.008  | Confidentiality  | The Cloud Infrastructure **must** | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|             |                  | support tenant networks           | workload security`                            |
|             |                  | segregation.                      |                                               |
+-------------+------------------+-----------------------------------+-----------------------------------------------+

Table 2-8: Reference Model Requirements: Confidentiality and Integrity
Requirements

Workload Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:workload security requirements`)

+--------------+-------------------+---------------------------------+-----------------------------------------------+
| Reference    | sub-category      | Description                     | Specification Reference                       |
+==============+===================+=================================+===============================================+
| sec.wl.001   | Workload          | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | Workload placement policy.      | workload security`                            |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.wl.002   | Workload          | The Cloud Infrastructure        |                                               |
|              |                   | provide methods to ensure the   |                                               |
|              |                   | platform's trust status and     |                                               |
|              |                   | integrity (e.g., remote         |                                               |
|              |                   | attestation, Trusted Platform   |                                               |
|              |                   | Module).                        |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.wl.003   | Workload          | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | secure provisioning of          | workload security`                            |
|              |                   | Workloads.                      |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.wl.004   | Workload          | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | Location assertion (for         | workload security`                            |
|              |                   | mandated in-country or location |                                               |
|              |                   | requirements).                  |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.wl.005   | Workload          | The Platform **must** support   | This requirement's verification goes beyond   |
|              |                   | the separation of production    | Anuket testing scope                          |
|              |                   | and non-production Workloads.   |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.wl.006   | Workload          | The Platform **must** support   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | the separation of Workloads     | workload security`                            |
|              |                   | based on their categorisation   |                                               |
|              |                   | (for example, payment card      |                                               |
|              |                   | information, healthcare, etc.)  |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.wl.007   | Workload          | The Operator **must** implement |                                               |
|              |                   | processes and tools to verify   |                                               |
|              |                   | verify NF authenticity and      |                                               |
|              |                   | integrity.                      |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+

Table 2-9: Reference Model Requirements - Workload Security Requirements

Image Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:image security requirements`)

+--------------+-----------------+-------------------------------+--------------------------------------------------+
| Reference    | sub-category    | Description                   | Specification Reference                          |
+==============+=================+===============================+==================================================+
| sec.img.001  | Image           | Images from untrusted sources | :ref:`ref_arch/openstack/chapters/chapter06:\    |
|              |                 | **must not** be used.         | image security`                                  |
+--------------+-----------------+-------------------------------+--------------------------------------------------+
| sec.img.002  | Image           | Images **must** be scanned to | :ref:`ref_arch/openstack/chapters/chapter06:\    |
|              |                 | be maintained free from known | image security`                                  |
|              |                 | vulnerabilities.              |                                                  |
+--------------+-----------------+-------------------------------+--------------------------------------------------+
| sec.img.003  | Image           | Images **must not** be        |                                                  |
|              |                 | configured to run with        |                                                  |
|              |                 | privileges higher than        |                                                  |
|              |                 | the privileges of the actor   |                                                  |
|              |                 | authorised to run them.       |                                                  |
+--------------+-----------------+-------------------------------+--------------------------------------------------+
| sec.img.004  | Image           | Images **must** only be       | :ref:`ref_arch/openstack/chapters/chapter06:\    |
|              |                 | accessible to authorised      | integrity of openstack components configuration` |
|              |                 | actors.                       |                                                  |
+--------------+-----------------+-------------------------------+--------------------------------------------------+
| sec.img.005  | Image           | Image Registries **must**     | :ref:`ref_arch/openstack/chapters/chapter06:\    |
|              |                 | only be accessible to         | integrity of openstack components configuration` |
|              |                 | authorised actors.            |                                                  |
+--------------+-----------------+-------------------------------+--------------------------------------------------+
| sec.img.006  | Image           | Image Registries **must**     | :ref:`ref_arch/openstack/chapters/chapter06:\    |
|              |                 | only be accessible over       | integrity of openstack components configuration` |
|              |                 | networks that enforce         |                                                  |
|              |                 | authentication, integrity and |                                                  |
|              |                 | confidentiality.              |                                                  |
+--------------+-----------------+-------------------------------+--------------------------------------------------+
| sec.img.007  | Image           | Image registries **must**     | :ref:`ref_arch/openstack/chapters/chapter06:\    |
|              |                 | be clear of vulnerable        | image security`                                  |
|              |                 | and out of date versions.     |                                                  |
+--------------+-----------------+-------------------------------+--------------------------------------------------+
| sec.img.008  | Image           | Images **must not** include   |                                                  |
|              |                 | any secrets. Secrets include  |                                                  |
|              |                 | passwords, cloud provider     |                                                  |
|              |                 | credentials, SSH keys, TLS    |                                                  |
|              |                 | certificate keys, etc.        |                                                  |
+--------------+-----------------+-------------------------------+--------------------------------------------------+

Table 2-10: Reference Model Requirements - Image Security Requirements

Security LCM Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:security lcm requirements`)

+--------------+--------------+-------------------------------------+------------------------------------------------+
| Reference    | sub-category | Description                         | Specification Reference                        |
+==============+==============+=====================================+================================================+
| sec.lcm.001  | LCM          | The Platform **must** support       | :ref:`ref_arch/openstack/chapters/chapter06:\  |
|              |              | Secure Provisioning, Availability,  | monitoring and security audit`                 |
|              |              | and Deprovisioning (Secure          |                                                |
|              |              | Clean-Up) of workload resources     |                                                |
|              |              | where Secure Clean-Up includes      |                                                |
|              |              | tear-down, defense against virus or |                                                |
|              |              | other attacks.                      |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.002  | LCM          | The Cloud Operator **must** use     | :ref:`ref_arch/openstack/chapters/chapter06:\  |
|              |              | management protocols limiting       | security lcm`                                  |
|              |              | security risk such as SNMPv3, SSH   |                                                |
|              |              | v2, ICMP, NTP, syslog and TLS v1.2  |                                                |
|              |              | or higher.                          |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.003  | LCM          | The Cloud Operator **must**         | :ref:`ref_arch/openstack/chapters/chapter06:\  |
|              |              | implement and strictly follow       | monitoring and security audit`                 |
|              |              | change management processes for     |                                                |
|              |              | Cloud Infrastructure,               |                                                |
|              |              | Infrastructure Manager and other    |                                                |
|              |              | components of the cloud, and        |                                                |
|              |              | Platform change control on          |                                                |
|              |              | hardware.                           |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.005  | LCM          | Platform **must** provide logs      | :ref:`ref_arch/openstack/chapters/chapter06:\  |
|              |              | and these logs must be monitored    | monitoring and security audit`                 |
|              |              | for anomalous behaviour.            |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.006  | LCM          | The Platform  **must** verify the   | :ref:`ref_arch/openstack/chapters/chapter06:\  |
|              |              | integrity of all Resource           | confidentiality and integrity of tenant data \ |
|              |              | management requests.                | (sec.ci.001)`                                  |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.007  | LCM          | The Platform **must** be able to    |                                                |
|              |              | update newly instantiated,          |                                                |
|              |              | suspended, hibernated, migrated and |                                                |
|              |              | restarted images with current time  |                                                |
|              |              | information.                        |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.008  | LCM          | The Platform **must** be able to    |                                                |
|              |              | update newly instantiated,          |                                                |
|              |              | suspended, hibernated, migrated and |                                                |
|              |              | restarted images with relevant DNS  |                                                |
|              |              | information.                        |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.009  | LCM          | The Platform **must** be able to    |                                                |
|              |              | update the tag of newly             |                                                |
|              |              | instantiated, suspended,            |                                                |
|              |              | hibernated, migrated and restarted  |                                                |
|              |              | images with relevant geolocation    |                                                |
|              |              | (geographical) information.         |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.010  | LCM          | The Platform **must** log all       |                                                |
|              |              | changes to geolocation along with   |                                                |
|              |              | the mechanisms and sources of       |                                                |
|              |              | location information (i.e. GPS, IP  |                                                |
|              |              | block, and timing).                 |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.011  | LCM          | The Platform **must** implement     | :ref:`ref_arch/openstack/chapters/chapter06:\  |
|              |              | Security life cycle management      | patches`                                       |
|              |              | processes including the proactive   |                                                |
|              |              | update and patching of all deployed |                                                |
|              |              | Cloud Infrastructure software.      |                                                |
+--------------+--------------+-------------------------------------+------------------------------------------------+
| sec.lcm.012  | LCM          | The Platform **must** log any       | :ref:`ref_arch/openstack/chapters/chapter06:\  |
|              |              | access privilege escalation.        | what to log / what not to log`                 |
+--------------+--------------+-------------------------------------+------------------------------------------------+

Table 2-11: Reference Model Requirements - Security LCM Requirements

Monitoring and Security Audit Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source
:ref:`ref_model/chapters/chapter07:monitoring and security audit requirements`)

The Platform is assumed to provide configurable alerting and
notification capability and the operator is assumed to have automated
systems, policies and procedures to act on alerts and notifications in a
timely fashion. In the following the monitoring and logging capabilities
can trigger alerts and notifications for appropriate action.

+--------------+-------------------+---------------------------------+-----------------------------------------------+
| Reference    | sub-category      | Description                     | Specification                                 |
|              |                   |                                 | Reference                                     |
+==============+===================+=================================+===============================================+
| sec.mon.001  | Monitoring/Audit  | Platform **must** provide logs  | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and these logs must be          | required fields`                              |
|              |                   | regularly monitored for events  |                                               |
|              |                   | of interest. The logs **must**  |                                               |
|              |                   | contain the following fields:   |                                               |
|              |                   | event type, date/time,          |                                               |
|              |                   | protocol, service or program    |                                               |
|              |                   | used for access,                |                                               |
|              |                   | success/failure, login ID or    |                                               |
|              |                   | process ID, IP address and      |                                               |
|              |                   | ports (source and destination)  |                                               |
|              |                   | involved.                       |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.002  | Monitoring        | Security logs **must** be       | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | time synchronised.              | security logs time synchronisation`           |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.003  | Monitoring        | The Platform **must** log all   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | changes to time server source,  | security logs time synchronisation`           |
|              |                   | time, date and time zones.      |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.004  | Audit             | The Platform **must** secure    | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and protect Audit logs          | security lcm`                                 |
|              |                   | (containing sensitive           |                                               |
|              |                   | information) both in-transit    |                                               |
|              |                   | and at rest.                    |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.005  | Monitoring/Audit  | The Platform **must** Monitor   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and Audit various behaviours    | what to log / what not to log`                |
|              |                   | of connection and login         |                                               |
|              |                   | attempts to detect access       |                                               |
|              |                   | attacks and potential access    |                                               |
|              |                   | attempts and take corrective    |                                               |
|              |                   | accordingly actions.            |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.006  | Monitoring/Audit  | The Platform **must** Monitor   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and Audit operations by         | monitoring and security audit`                |
|              |                   | authorised account access after |                                               |
|              |                   | login to detect malicious       |                                               |
|              |                   | operational activity and        |                                               |
|              |                   | take corrective actions.        |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.007  | Monitoring/Audit  | The Platform **must** Monitor   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and Audit security parameter    | integrity of openstack components \           |
|              |                   | configurations for compliance   | configuration`                                |
|              |                   | with defined security policies. |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.008  | Monitoring/Audit  | The Platform **must** Monitor   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and Audit externally exposed    | confidentiality and integrity of \            |
|              |                   | interfaces for illegal access   | communications (sec.ci.001)`                  |
|              |                   | (attacks) and take              |                                               |
|              |                   | corrective security hardening   |                                               |
|              |                   | measures.                       |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.009  | Monitoring/Audit  | The Platform **must** Monitor   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and Audit service for various   | monitoring and security audit`                |
|              |                   | attacks (malformed messages,    |                                               |
|              |                   | signalling flooding and         |                                               |
|              |                   | replaying, etc.) and take       |                                               |
|              |                   | corrective actions accordingly. |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.010  | Monitoring/Audit  | The Platform **must** Monitor   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and Audit running processes     | monitoring and security audit`                |
|              |                   | to detect unexpected or         |                                               |
|              |                   | unauthorised processes and take |                                               |
|              |                   | corrective actions accordingly. |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.011  | Monitoring/Audit  | The Platform **must** Monitor   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and Audit logs from             | creating logs`                                |
|              |                   | infrastructure elements and     |                                               |
|              |                   | workloads to detected           |                                               |
|              |                   | anomalies in the system         |                                               |
|              |                   | components and take             |                                               |
|              |                   | corrective actions accordingly. |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.012  | Monitoring/Audit  | The Platform **must** Monitor   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | and Audit Traffic patterns      | confidentiality and integrity of tenant \     |
|              |                   | and volumes to prevent          | data (sec.ci.001)`                            |
|              |                   | malware download attempts.      |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.013  | Monitoring        | The monitoring system           |                                               |
|              |                   | **must not** affect the         |                                               |
|              |                   | security (integrity and         |                                               |
|              |                   | confidentiality) of the         |                                               |
|              |                   | infrastructure, workloads,      |                                               |
|              |                   | or the user data (through back  |                                               |
|              |                   | door entries)                   |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.015  | Monitoring        | The Platform **must** ensure    | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | that the Monitoring systems     | monitoring and security audit`                |
|              |                   | are never starved of resources  |                                               |
|              |                   | and **must** activate alarms    |                                               |
|              |                   | when resource utilisation       |                                               |
|              |                   | exceeds a configurable          |                                               |
|              |                   | threshold.                      |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.017  | Audit             | The Platform **must** audit     | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | systems for any missing         | patches`                                      |
|              |                   | security patches and take       |                                               |
|              |                   | appropriate actions.            |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.018  | Monitoring        | The Platform, starting from     | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | initialisation, **must**        | where to log`                                 |
|              |                   | collect and analyse logs to     |                                               |
|              |                   | identify security events, and   |                                               |
|              |                   | store these events in an        |                                               |
|              |                   | external system.                |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.019  | Monitoring        | The Platform's components       | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | **must not** include an         | what to log / what not to log`                |
|              |                   | authentication credential,      |                                               |
|              |                   | e.g., password, in any logs,    |                                               |
|              |                   | even if encrypted.              |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.020  | Monitoring/Audit  | The Platform's logging system   | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | **must** support the storage    | data retention`                               |
|              |                   | of security audit logs for a    |                                               |
|              |                   | configurable period of time.    |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+
| sec.mon.021  | Monitoring        | The Platform **must** store     | :ref:`ref_arch/openstack/chapters/chapter06:\ |
|              |                   | security events locally if      | where to log`                                 |
|              |                   | the external logging system     |                                               |
|              |                   | is unavailable and shall        |                                               |
|              |                   | periodically attempt to send    |                                               |
|              |                   | these to the external logging   |                                               |
|              |                   | system until successful.        |                                               |
+--------------+-------------------+---------------------------------+-----------------------------------------------+

Table 2-12: Reference Model Requirements - Monitoring and Security Audit
Requirements

Open-Source Software Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:open source software security requirements`)

+-------------+-------------------+----------------------------------+---------------+
| Reference   | sub-category      | Description                      | Specification |
|             |                   |                                  | Reference     |
+=============+===================+==================================+===============+
| sec.oss.001 | Software          | Open-source code **must** be     |               |
|             |                   | inspected by tools with various  |               |
|             |                   | capabilities for static and      |               |
|             |                   | dynamic code analysis.           |               |
+-------------+-------------------+----------------------------------+---------------+
| sec.oss.002 | Software          | The `CVE (Common Vulnerabilities |               |
|             |                   | and Exposures)                   |               |
|             |                   | <https://cve.mitre.org/>`__      |               |
|             |                   | **must** be used to identify     |               |
|             |                   | vulnerabilities and their        |               |
|             |                   | severity rating for  open-source |               |
|             |                   | code part of Cloud               |               |
|             |                   | Infrastructure and  workloads    |               |
|             |                   | software.                        |               |
+-------------+-------------------+----------------------------------+---------------+
| sec.oss.003 | Software          | Critical and high severity rated |               |
|             |                   | vulnerabilities **must** be      |               |
|             |                   | fixed in a timely manner. Refer  |               |
|             |                   | to the `CVSS (Common             |               |
|             |                   | Vulnerability Scoring System)    |               |
|             |                   | <https://www.first.org/cvss/>`__ |               |
|             |                   | to know a vulnerability score    |               |
|             |                   | and its associated rate (low,    |               |
|             |                   | medium, high, or critical)       |               |
+-------------+-------------------+----------------------------------+---------------+
| sec.oss.004 | Software          | A dedicated internal isolated    |               |
|             |                   | repository separated from the    |               |
|             |                   | production environment **must**  |               |
|             |                   | be used to store vetted          |               |
|             |                   | open-source content.             |               |
+-------------+-------------------+----------------------------------+---------------+

Table 2-13: Reference Model Requirements - Open-Source Software Security
Requirements

IaaC security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^

(source
:ref:`ref_model/chapters/chapter07:iaac - secure design and architecture stage requirements`)

**Secure Code Stage Requirements**

+--------------+-------------------+---------------------+---------------+
| Reference    | sub-category      | Description         | Specification |
|              |                   |                     | Reference     |
+==============+===================+=====================+===============+
| sec.code.001 | IaaC              | SAST -Static        |               |
|              |                   | Application         |               |
|              |                   | Security Testing    |               |
|              |                   | **must** be applied |               |
|              |                   | during Secure       |               |
|              |                   | Coding stage        |               |
|              |                   | triggered by Pull,  |               |
|              |                   | Clone or Comment    |               |
|              |                   | trigger. Security   |               |
|              |                   | testing that        |               |
|              |                   | analyses            |               |
|              |                   | application source  |               |
|              |                   | code for software   |               |
|              |                   | vulnerabilities and |               |
|              |                   | gaps against best   |               |
|              |                   | practices. Example: |               |
|              |                   | open source OWASP   |               |
|              |                   | range of tools.     |               |
+--------------+-------------------+---------------------+---------------+

Table 2-14: Reference Model Requirements: IaaC Security Requirements,
Secure Code Stage

**Continuous Build, Integration and Testing Stage Requirements**

+-------------+-------------------+---------------------+---------------+
| Reference   | sub-category      | Description         | Specification |
|             |                   |                     | Reference     |
+=============+===================+=====================+===============+
| sec.bld.003 | IaaC              | Image Scan **must** |               |
|             |                   | be applied during   |               |
|             |                   | the Continuous      |               |
|             |                   | Build, Integration  |               |
|             |                   | and Testing stage   |               |
|             |                   | triggered by        |               |
|             |                   | Package trigger,    |               |
|             |                   | example: A push of  |               |
|             |                   | a container image   |               |
|             |                   | to a container      |               |
|             |                   | registry may        |               |
|             |                   | trigger a           |               |
|             |                   | vulnerability scan  |               |
|             |                   | before the image    |               |
|             |                   | becomes available   |               |
|             |                   | in the registry.    |               |
+-------------+-------------------+---------------------+---------------+

Table 2-15: Reference Model Requirements - IaaC Security Requirements,
Continuous Build, Integration and Testing Stage

**Continuous Delivery and Deployment Stage Requirements**

+-------------+-------------------+---------------------+---------------+
| Reference   | sub-category      | Description         | Specification |
|             |                   |                     | Reference     |
+=============+===================+=====================+===============+
| sec.del.001 | IaaC              | Image Scan **must** |               |
|             |                   | be applied during   |               |
|             |                   | the Continuous      |               |
|             |                   | Delivery and        |               |
|             |                   | Deployment stage    |               |
|             |                   | triggered by        |               |
|             |                   | Publish to Artifact |               |
|             |                   | and Image           |               |
|             |                   | Repository trigger. |               |
|             |                   | Example: GitLab     |               |
|             |                   | uses the open       |               |
|             |                   | source Clair engine |               |
|             |                   | for container image |               |
|             |                   | scanning.           |               |
+-------------+-------------------+---------------------+---------------+
| sec.del.002 | IaaC              | Code Signing        |               |
|             |                   | **must** be applied |               |
|             |                   | during the          |               |
|             |                   | Continuous Delivery |               |
|             |                   | and Deployment      |               |
|             |                   | stage triggered by  |               |
|             |                   | Publish to Artifact |               |
|             |                   | and Image           |               |
|             |                   | Repository trigger. |               |
|             |                   | Code Signing        |               |
|             |                   | provides            |               |
|             |                   | authentication to   |               |
|             |                   | assure that         |               |
|             |                   | downloaded files    |               |
|             |                   | are form the        |               |
|             |                   | publisher named on  |               |
|             |                   | the certificate.    |               |
+-------------+-------------------+---------------------+---------------+
| sec.del.004 | IaaC              | Component           |               |
|             |                   | Vulnerability Scan  |               |
|             |                   | **must** be applied |               |
|             |                   | during the          |               |
|             |                   | Continuous Delivery |               |
|             |                   | and Deployment      |               |
|             |                   | stage triggered by  |               |
|             |                   | Instantiate         |               |
|             |                   | Infrastructure      |               |
|             |                   | trigger. The        |               |
|             |                   | vulnerability       |               |
|             |                   | scanning system is  |               |
|             |                   | deployed on the     |               |
|             |                   | cloud platform to   |               |
|             |                   | detect security     |               |
|             |                   | vulnerabilities of  |               |
|             |                   | specified           |               |
|             |                   | components through  |               |
|             |                   | scanning and to     |               |
|             |                   | provide timely      |               |
|             |                   | security            |               |
|             |                   | protection.         |               |
|             |                   | Example: OWASP Zed  |               |
|             |                   | Attack Proxy (ZAP). |               |
+-------------+-------------------+---------------------+---------------+

Table 2-16: Reference Model Requirements - IaaC Security Requirements,
Continuous Delivery and Deployment Stage

**Runtime Defence and Monitoring Requirements**

+-------------+-------------------+---------------------+---------------+
| Reference   | sub-category      | Description         | Specification |
|             |                   |                     | Reference     |
+=============+===================+=====================+===============+
| sec.run.001 | IaaC              | Component           |               |
|             |                   | Vulnerability       |               |
|             |                   | Monitoring **must** |               |
|             |                   | be continuously     |               |
|             |                   | applied during the  |               |
|             |                   | Runtime Defence and |               |
|             |                   | Monitoring stage.   |               |
|             |                   | Security technology |               |
|             |                   | that monitors       |               |
|             |                   | components like     |               |
|             |                   | virtual servers and |               |
|             |                   | assesses data,      |               |
|             |                   | applications, and   |               |
|             |                   | infrastructure for  |               |
|             |                   | security risks.     |               |
+-------------+-------------------+---------------------+---------------+

Table 2-17: Reference Model Requirements - IaaC Security Requirements,
Runtime Defence and Monitoring Stage

Compliance with Standards Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:compliance with standards requirements`)

+-------------+-------------------+---------------------+---------------+
| Reference   | sub-category      | Description         | Specification |
|             |                   |                     | Reference     |
+=============+===================+=====================+===============+
| sec.std.012 | Standards         | The Public Cloud    |               |
|             |                   | Operator **must**,  |               |
|             |                   | and the Private     |               |
|             |                   | Cloud Operator      |               |
|             |                   | **may** be          |               |
|             |                   | certified to be     |               |
|             |                   | compliant with the  |               |
|             |                   | International       |               |
|             |                   | Standard on         |               |
|             |                   | Awareness           |               |
|             |                   | Engagements (ISAE)  |               |
|             |                   | 3402 (in the US:    |               |
|             |                   | SSAE 16);           |               |
|             |                   | International       |               |
|             |                   | Standard on         |               |
|             |                   | Awareness           |               |
|             |                   | Engagements (ISAE)  |               |
|             |                   | 3402. US            |               |
|             |                   | Equivalent: SSAE16. |               |
+-------------+-------------------+---------------------+---------------+

Table 2-18: Reference Model Requirements: Compliance with Standards 
Requirements

Architecture and OpenStack Requirements
---------------------------------------

“Architecture” in this chapter refers to Cloud Infrastructure (referred
to as NFVI by ETSI) + VIM (as specified in Reference Model Chapter 3).

General Requirements
~~~~~~~~~~~~~~~~~~~~

+------------+--------------+--------------------------+-----------------------------------------------+
| Reference  | sub-category | Description              | Specification                                 |
|            |              |                          | Reference                                     |
|            |              |                          |                                               |
|            |              |                          |                                               |
|            |              |                          |                                               |
+============+==============+==========================+===============================================+
| gen.ost.01 | Open source  | The Architecture         | :ref:`ref_arch/openstack/chapters/chapter05:\ |
|            |              | **must** use OpenStack   | consolidated set of apis`                     |
|            |              | APIs.                    |                                               |
+------------+--------------+--------------------------+-----------------------------------------------+
| gen.ost.02 | Open source  | The Architecture         | :ref:`ref_arch/openstack/chapters/chapter05:\ |
|            |              | **must** support dynamic | consolidated set of apis`                     |
|            |              | request and              |                                               |
|            |              | configuration of virtual |                                               |
|            |              | resources (compute,      |                                               |
|            |              | network, storage)        |                                               |
|            |              | through OpenStack APIs.  |                                               |
+------------+--------------+--------------------------+-----------------------------------------------+
| gen.rsl.01 | Resiliency   | The Architecture         |                                               |
|            |              | **must** support         |                                               |
|            |              | resilient OpenStack      |                                               |
|            |              | components that are      |                                               |
|            |              | required for the         |                                               |
|            |              | continued availability   |                                               |
|            |              | of running workloads.    |                                               |
+------------+--------------+--------------------------+-----------------------------------------------+
| gen.avl.01 | Availability | The Architecture         | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | **must** provide High    | underlying resources`                         |
|            |              | Availability for         |                                               |
|            |              | OpenStack components.    |                                               |
+------------+--------------+--------------------------+-----------------------------------------------+

Table 2-19: General Requirements

Infrastructure Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+--------------+----------------------------------------+-----------------------------------------------+
| Reference  | sub-category | Description                            | Specification                                 |
|            |              |                                        | Reference                                     |
+============+==============+========================================+===============================================+
| inf.com.01 | Compute      | The Architecture **must** provide      | :ref:`ref_arch/openstack/chapters/chapter03:\ |
|            |              | compute resources for instances.       | cloud workload services`             `        |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.com.04 | Compute      | The Architecture **must** be able to   | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | support multiple CPU type options      | support for cloud infrastructure profiles \   |
|            |              | to support various infrastructure      | and flavors`                                  |
|            |              | profiles (Basic and High Performance). |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.com.05 | Compute      | The Architecture **must** support      | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | Hardware Platforms with NUMA           | support for cloud infrastructure profiles \   |
|            |              | capabilities.                          | and flavors`                                  |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.com.06 | Compute      | The Architecture **must** support CPU  | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | Pinning of the vCPUs of an instance.   | support for cloud infrastructure profiles \   |
|            |              |                                        | and flavors`                                  |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.com.07 | Compute      | The Architecture **must** support      | :ref:`ref_arch/openstack/chapters/chapter03:\ |
|            |              | different hardware configurations to   | cloud partitioning: host aggregates, \        |
|            |              | support various infrastructure         | availability zones`                           |
|            |              | profiles (Basic and High Performance). |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.com.08 | Compute      | The Architecture **must** support      | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | allocating certain number of host      | reservation of compute node cores`            |
|            |              | cores for  all non-tenant workloads    |                                               |
|            |              | such as for OpenStack services. SMT    |                                               |
|            |              | threads can be allocated to individual |                                               |
|            |              | OpenStack services or their            |                                               |
|            |              | components.                            |                                               |
|            |              | `Dedicating host cores to certain      |                                               |
|            |              | workloads (e.g., OpenStack services)   |                                               |
|            |              | <https://docs.openstack.org/nova\\     |                                               |
|            |              | /latest/configuration/config.html#\    |                                               |
|            |              | compute.cpu_dedicated_set>`__.         |                                               |
|            |              | Please see example,                    |                                               |
|            |              | `Configuring libvirt compute nodes for |                                               |
|            |              | CPU pinning                            |                                               |
|            |              | <https://docs.openstack.org/nova\\     |                                               |
|            |              | /latest/admin/cpu-topologies.html>`__  |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.com.09 | Compute      | The Architecture **must** ensure that  | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | the host cores assigned to non-tenant  | pinned and unpinned cpus`                     |
|            |              | and tenant workloads are SMT aware:    |                                               |
|            |              | that is, a host core and its           |                                               |
|            |              | associated SMT threads are either all  |                                               |
|            |              | assigned to non-tenant workloads or    |                                               |
|            |              | all assigned to tenant workloads.      |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.stg.01 | Storage      | The Architecture **must** provide      | :ref:`ref_arch/openstack/chapters/chapter03:\ |
|            |              | remote (not directly attached to the   | storage`                                      |
|            |              | host) Block storage for Instances.     |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.stg.02 | Storage      | The Architecture **must** provide      | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | Object storage for Instances.          | swift`                                        |
|            |              | Operators **may** choose not to        |                                               |
|            |              | implement Object Storage but must be   |                                               |
|            |              | cognizant of the the risk of           |                                               |
|            |              | "Compliant VNFs" failing in their      |                                               |
+            +              + environment.                           |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.nw.01  | Network      | The Architecture **must** provide      | :ref:`ref_arch/openstack/chapters/chapter05:\ |
|            |              | virtual network interfaces to          | neutron`                                      |
|            |              | instances.                             |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.nw.02  | Network      | The Architecture **must** include      | :ref:`ref_arch/openstack/chapters/chapter03:\ |
|            |              | capabilities for integrating SDN       | virtual networking – 3rd party sdn solution`  |
|            |              | controllers to support provisioning    |                                               |
|            |              | of network services, from the SDN      |                                               |
|            |              | OpenStack Neutron service, such as     |                                               |
|            |              | networking of VTEPs to the Border Edge |                                               |
|            |              | based VRFs.                            |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.nw.03  | Network      | The Architecture **must** support low  | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | latency and high throughput traffic    | network fabric`                               |
|            |              | needs.                                 |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.nw.05  | Network      | The Architecture **must** allow for    | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | East/West tenant traffic within the    | network fabric`                               |
|            |              | cloud (via tunnelled encapsulation     |                                               |
|            |              | overlay such as VXLAN or Geneve).      |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.nw.07  | Network      | The Architecture **must** support      | :ref:`ref_arch/openstack/chapters/chapter03:\ |
|            |              | network :ref:`resiliency \             | network`                                      |
|            |              | <common/glossary:cloud platform \      |                                               |
|            |              | abstraction related terminology:>`     |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.nw.10  | Network      | The Cloud Infrastructure Network       | :ref:`ref_arch/openstack/chapters/chapter03:\ |
|            |              | Fabric **must** be capable of enabling | network`                                      |
|            |              | highly available (Five 9's or better)  |                                               |
|            |              | Cloud Infrastructure.                  |                                               |
+------------+--------------+----------------------------------------+-----------------------------------------------+
| inf.nw.15  | Network      | The Architecture **must** support      | :ref:`ref_arch/openstack/chapters/chapter04:\ |
|            |              | multiple networking options for        | neutron extensions` and                       |
|            |              | Cloud Infrastructure to support        | `OpenStack Neutron Plugins \                  |
|            |              | various infrastructure profiles (Basic | <https://wiki.openstack.org/wiki/\            |
|            |              | and High Performance).                 | Neutron_Plugins_and_Drivers>`__               |
+-----------+---------------+----------------------------------------+-----------------------------------------------+
| inf.nw.16 | Network       | The Architecture **must** support dual |                                               |
|           |               | stack IPv4 and IPv6 for tenant         |                                               |
|           |               | networks and workloads.                |                                               |
+-----------+---------------+----------------------------------------+-----------------------------------------------+

Table 2-20: Infrastructure Requirements

VIM Requirements
~~~~~~~~~~~~~~~~

+--------+----------------+----------------------------+-------------+
| Refer\ | sub-category   | Description                | Sp\         |
| ence   |                |                            | ecification |
|        |                |                            | Reference   |
+========+================+============================+=============+
| vim.01 | General        | The Architecture **must**  | `RA-1       |
|        |                | allow infrastructure       | “Consumable |
|        |                | resource sharing.          | Inf\        |
|        |                |                            | rastructure |
|        |                |                            | Resources   |
|        |                |                            | and         |
|        |                |                            | Services”   |
|        |                |                            | <./ch       |
|        |                |                            | apter03.md# |
|        |                |                            | consumab    |
|        |                |                            | le-infrastr |
|        |                |                            | ucture-reso |
|        |                |                            | urces-and-s |
|        |                |                            | ervices>`__ |
+--------+----------------+----------------------------+-------------+
| vim.03 | General        | The Architecture **must**  | `RA-1       |
|        |                | allow VIM to discover and  | “           |
|        |                | manage Cloud               | Placement”  |
|        |                | Infrastructure resources.  | <./chapter0 |
|        |                |                            | 5.md#pl     |
|        |                |                            | acement>`__ |
+--------+----------------+----------------------------+-------------+
| vim.05 | General        | The Architecture **must**  | `RA-1       |
|        |                | include image repository   | “Glance”    |
|        |                | management.                | <./chapte   |
|        |                |                            | r04.md#     |
|        |                |                            | -glance>`__ |
+--------+----------------+----------------------------+-------------+
| vim.07 | General        | The Architecture **must**  | `RA-1       |
|        |                | support multi-tenancy.     | “Multi-Te\  |
|        |                |                            | nancy” <./c |
|        |                |                            | hapter03.md |
|        |                |                            | #multi-     |
|        |                |                            | tenancy-exe |
|        |                |                            | cution-envi |
|        |                |                            | ronment>`__ |
+--------+----------------+----------------------------+-------------+
| vim.08 | General        | The Architecture **must**  | `“OpenStack |
|        |                | support resource tagging.  | Resource    |
|        |                |                            | Tags” <htt  |
|        |                |                            | ps://specs. |
|        |                |                            | openstack.o |
|        |                |                            | rg/openstac |
|        |                |                            | k/api-wg/gu |
|        |                |                            | idelines/ta |
|        |                |                            | gs.html>`__ |
+--------+----------------+----------------------------+-------------+

Table 2-21: VIM Requirements

Interfaces & APIs Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+--------------+------------------------------+-----------------+
| Ref\| sub-category | Description                  | Specification   |
| ere\|              |                              | Reference       |
| nce\|              |                              |                 |
+=====+==============+==============================+=================+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide APIs to access the   | “Keystone” <.   |
| api\|              | authentication service and   | /chapter05.md#  |
| .01 |              | the associated mandatory     | keystone>`__    |
|     |              | features detailed in chapter |                 |
|     |              | 5.                           |                 |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide APIs to access the   | “Glance”        |
| api\|              | image management service and | <./chapter05.md |
| .02 |              | the associated mandatory     | #glance>`__     |
|     |              | features detailed in chapter |                 |
|     |              | 5.                           |                 |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide APIs to access the   | “Cinder”        |
| api\|              | block storage management     | <./chapter05.md |
| .03 |              | service and the associated   | #cinder>`__     |
|     |              | mandatory features detailed  |                 |
|     |              | in chapter 5.                |                 |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide APIs to access the   | “Swift”         |
| api\|              | object storage management    | <./chapter05.m  |
| .04 |              | service and the associated   | d#swift>`__     |
|     |              | mandatory features detailed  |                 |
|     |              | in chapter 5.                |                 |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide APIs to access the   | “Neutron”       |
| api\|              | network management service   | <./chapter05.md |
| .05 |              | and the associated mandatory | #neutron>`__    |
|     |              | features detailed in chapter |                 |
|     |              | 5.                           |                 |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide APIs to access the   | “Nova”          |
| api\|              | compute resources management | <./chapter05.   |
| .06 |              | service and the associated   | md#nova>`__     |
|     |              | mandatory features detailed  |                 |
|     |              | in chapter 5.                |                 |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide GUI access to tenant | “Horizon” <.    |
| api\|              | facing cloud platform core   | /chapter04.md#  |
| .07 |              | services except at Edge/Far  | horizon>`__     |
|     |              | Edge clouds.                 |                 |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide APIs needed to       | “Placement” <./ |
| api\|              | discover and manage Cloud    | chapter05.md#   |
| .08 |              | Infrastructure resources.    | placement>`__   |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture **must**    | `RA-1           |
| nt.\|              | provide APIs to access the   | “Heat”          |
| api\|              | orchestration service.       | <./chapter05.   |
| .09 |              |                              | md#heat>`__     |
+-----+--------------+------------------------------+-----------------+
| i\  | API          | The Architecture must expose | `RA-1 Core      |
| nt.\|              | the latest version and       | OpenStack       |
| api\|              | microversion of the APIs for | Services        |
| .10 |              | the given Anuket OpenStack   | APIs <./cha     |
|     |              | release for each of the      | pter05.md#co    |
|     |              | OpenStack core services.     | re-openstack-se |
|     |              |                              | rvices-apis>`__ |
+-----+--------------+------------------------------+-----------------+

Table 2-22: Interfaces and APIs Requirements

Tenant Requirements
~~~~~~~~~~~~~~~~~~~

+--------+---------------+--------------------+-----------------------+
| Refer\ | sub-category  | Description        | Specification         |
| ence   |               |                    | Reference             |
+========+===============+====================+=======================+
| tnt.g\ | General       | The Architecture   | `RA-1                 |
| en.01  |               | **must** support   | “Horizon” <./chapter0 |
|        |               | self-service       | 4.md#horizon>`__      |
|        |               | dashboard (GUI)    | and `RA-1 "Cloud      |
|        |               | and APIs for users | Workload              |
|        |               | to deploy,         | Services"             |
|        |               | configure and      | <./chapter03.md#      |
|        |               | manage their       | cloud-workload-       |
|        |               | workloads.         | services>`__          |
+--------+---------------+--------------------+-----------------------+

Table 2-23: Tenant Requirements

Operations and LCM
~~~~~~~~~~~~~~~~~~

+------+-----------------+----------------------+----------------------+
| R\   | sub-category    | Description          | Specification        |
| efer\|                 |                      | Reference            |
| ence |                 |                      |                      |
+======+=================+======================+======================+
| lc\  | General         | The Architecture     |                      |
| m.ge\|                 | **must** support     |                      |
| n.01 |                 | zero downtime of     |                      |
|      |                 | running workloads    |                      |
|      |                 | when the number of   |                      |
|      |                 | compute hosts and/or |                      |
|      |                 | the storage capacity |                      |
|      |                 | is being expanded or |                      |
|      |                 | unused capacity is   |                      |
|      |                 | being removed.       |                      |
+------+-----------------+----------------------+----------------------+
| lc\  | Automated       | The Architecture     |                      |
| m.ad\| deployment      | **must** support     |                      |
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
| R\   | s\          | Description                    | Specification  |
| efer\| ub-category |                                | Reference      |
| ence |             |                                |                |
+======+=============+================================+================+
| as\  | Integration | The Architecture **must**      |                |
| r.mo\|             | include integration with       |                |
| n.01 |             | various infrastructure         |                |
|      |             | components to support          |                |
|      |             | collection of telemetry for    |                |
|      |             | assurance monitoring and       |                |
|      |             | network intelligence.          |                |
+------+-------------+--------------------------------+----------------+
| as\  | Monitoring  | The Architecture **must**      |                |
| r.mo\|             | allow for the collection and   |                |
| n.03 |             | dissemination of performance   |                |
|      |             | and fault information.         |                |
+------+-------------+--------------------------------+----------------+
| as\  | Network     | The Cloud Infrastructure       |                |
| r.mo\|             | Network Fabric and Network     |                |
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
| Ref\| sub-     | Description                    | Notes             |
| ere\| category |                                |                   |
| nce |          |                                |                   |
+=====+==========+================================+===================+
| g\  | Cloud    | The Architecture **should**    | OpenStack         |
| en.\| na\      | consist of stateless service   | consists of both  |
| cnt\| tiveness | components. However, where     | stateless and     |
| .01 |          | state is required it must be   | stateful services |
|     |          | kept external to the           | where the         |
|     |          | component.                     | stateful services |
|     |          |                                | utilise a         |
|     |          |                                | database. For     |
|     |          |                                | latter see        |
|     |          |                                | “`Configuring the |
|     |          |                                | stateful          |
|     |          |                                | services          |
|     |          |                                | <https://docs.ope |
|     |          |                                | nstack.org/ha-gui |
|     |          |                                | de/control-plane- |
|     |          |                                | stateful          |
|     |          |                                | .html>`__”        |
+-----+----------+--------------------------------+-------------------+
| g\  | Cloud    | The Architecture **should**    |                   |
| en.\| na\      | consist of service components  |                   |
| cnt\| tiveness | implemented as microservices   |                   |
| .02 |          | that are individually          |                   |
|     |          | dynamically scalable.          |                   |
+-----+----------+--------------------------------+-------------------+
| g\  | Sca\     | The Architecture **should**    | This requirement  |
| en.\| lability | support policy driven          | is currently not  |
| scl\|          | auto-scaling.                  | addressed but     |
| .01 |          |                                | will likely be    |
|     |          |                                | supported through |
|     |          |                                | `Senlin           |
|     |          |                                | <https://docs.    |
|     |          |                                | openstack.org/sen |
|     |          |                                | lin/wallaby/>`__, |
|     |          |                                | cluster           |
|     |          |                                | management        |
|     |          |                                | service.          |
+-----+----------+--------------------------------+-------------------+
| g\  | Re\      | The Architecture **should**    |                   |
| en.\| siliency | support resilient OpenStack    |                   |
| rsl\|          | service components that are    |                   |
| .02 |          | not subject to gen.rsl.01.     |                   |
+-----+----------+--------------------------------+-------------------+

Table 2-26: General Recommendations

Infrastructure Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+----------+--------------------------------+-------------------+
| Ref\| sub-     | Description                    | Notes             |
| ere\| category |                                |                   |
| nce |          |                                |                   |
+=====+==========+================================+===================+
| i\  | Compute  | The Architecture **should**    |                   |
| nf.\|          | include industry standard      |                   |
| com\|          | hardware management systems at |                   |
| .02 |          | both HW device level           |                   |
|     |          | (embedded) and HW platform     |                   |
|     |          | level (external to device).    |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Compute  | The Architecture **should**    |                   |
| nf.\|          | support Symmetric              |                   |
| com\|          | Multiprocessing with shared    |                   |
| .03 |          | memory access as well as       |                   |
|     |          | Simultaneous Multithreading.   |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Storage  | The Architecture **should**    |                   |
| nf.\|          | allow use of externally        |                   |
| stg\|          | provided large archival        |                   |
| .08 |          | storage for its Backup /       |                   |
|     |          | Restore / Archival needs.      |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Storage  | The Architecture **should**    |                   |
| nf.\|          | make available all non-host OS |                   |
| stg\|          | / Hypervisor / Host systems    |                   |
| .09 |          | storage as network-based       |                   |
|     |          | Block, File or Object Storage  |                   |
|     |          | for tenant/management          |                   |
|     |          | consumption.                   |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Storage  | The Architecture **should**    | `RA-1 “Virtual    |
| nf.\|          | provide local Block storage    | Storage” <./ch    |
| stg\|          | for Instances.                 | apter03.md#vi     |
| .10 |          |                                | rtual-storage>`__ |
+-----+----------+--------------------------------+-------------------+
| i\  | Network  | The Architecture **should**    |                   |
| nf.\|          | support service function       |                   |
| ntw\|          | chaining.                      |                   |
| .04 |          |                                |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Network  | The Architecture **should**    |                   |
| nf.\|          | support Distributed Virtual    |                   |
| ntw\|          | Routing (DVR) to allow compute |                   |
| .06 |          | nodes to route traffic         |                   |
|     |          | efficiently.                   |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Network  | The Cloud Infrastructure       |                   |
| nf.\|          | Network Fabric **should**      |                   |
| ntw\|          | embrace the concepts of open   |                   |
| .08 |          | networking and disaggregation  |                   |
|     |          | using commodity networking     |                   |
|     |          | hardware and disaggregated     |                   |
|     |          | Network Operating Systems.     |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Network  | The Cloud Infrastructure       |                   |
| nf.\|          | Network Fabric **should**      |                   |
| ntw\|          | embrace open-based standards   |                   |
| .09 |          | and technologies.              |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Network  | The Cloud Infrastructure       |                   |
| nf.\|          | Network Fabric **should** be   |                   |
| ntw\|          | architected to provide a       |                   |
| .11 |          | standardised, scalable, and    |                   |
|     |          | repeatable deployment model    |                   |
|     |          | across all applicable Cloud    |                   |
|     |          | Infrastructure sites.          |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Network  | The Architecture **should**    |                   |
| nf.\|          | use dual stack IPv4 and IPv6   |                   |
| ntw\|          | for Cloud Infrastructure       |                   |
| .17 |          | internal networks.             |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Acce     | The Architecture **should**    | `RA-1             |
| nf.\| leration | support Application Specific   | “Acceleration” <. |
| acc\|          | Acceleration (exposed to       | /chapter03.md#    |
| .01 |          | VNFs).                         | acceleration>`__  |
+-----+----------+--------------------------------+-------------------+
| i\  | Acce     | The Architecture **should**    | `“OpenStack       |
| nf.\| leration | support Cloud Infrastructure   | Future - Specs    |
| acc\|          | Acceleration (such as          | defined” <http    |
| .02 |          | SmartNICs).                    | s://specs.opensta |
|     |          |                                | ck.org/openstack/ |
|     |          |                                | neutron-specs/spe |
|     |          |                                | cs/stein/neutron- |
|     |          |                                | ovs-agent-support |
|     |          |                                | -baremetal-with-s |
|     |          |                                | mart-nic.html>`__ |
+-----+----------+--------------------------------+-------------------+
| i\  | Acce     | The Architecture **may** rely  |                   |
| nf.\| leration | on SR-IOV PCI-Pass through to  |                   |
| acc\|          | provide acceleration to VNFs.  |                   |
| .03 |          |                                |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Image    | The Architecture **should**    | `RA-1             |
| nf.\|          | make the immutable images      | “Glance”          |
| img\|          | available via location         | <./chapter04.m    |
| .01 |          | independent means.             | d#glance>`__      |
+-----+----------+--------------------------------+-------------------+

Table 2-27: Infrastructure Recommendations

VIM Recommendations
~~~~~~~~~~~~~~~

+----+--------------------+----------------------------+-------------+
| R\ | sub-category       | Description                | Notes       |
| ef\|                    |                            |             |
| er\|                    |                            |             |
| en\|                    |                            |             |
| ce |                    |                            |             |
+====+====================+============================+=============+
| vi\| General            | The Architecture           | `RA-1       |
| m.\|                    | **should** support         | “Co\        |
| 02 |                    | deployment of OpenStack    | ntainerised |
|    |                    | components in containers.  | OpenStack   |
|    |                    |                            | Services”   |
|    |                    |                            | <./chapter0 |
|    |                    |                            | 4.md#con    |
|    |                    |                            | tainerised- |
|    |                    |                            | openstack-s |
|    |                    |                            | ervices>`__ |
+----+--------------------+----------------------------+-------------+
| vi\| General            | The Architecture           |             |
| m.\|                    | **should** support         |             |
| 04 |                    | Enhanced Platform          |             |
|    |                    | Awareness (EPA) only for   |             |
|    |                    | discovery of               |             |
|    |                    | infrastructure resource    |             |
|    |                    | capabilities.              |             |
+----+--------------------+----------------------------+-------------+
| vi\| General            | The Architecture           |             |
| m.\|                    | **should** allow           |             |
| 06 |                    | orchestration solutions to |             |
|    |                    | be integrated with VIM.    |             |
+----+--------------------+----------------------------+-------------+
| vi\| General            | The Architecture           |             |
| m.\|                    | **should** support         |             |
| 09 |                    | horizontal scaling of      |             |
|    |                    | OpenStack core services.   |             |
+----+--------------------+----------------------------+-------------+

Table 2-28: VIM Recommendations

Interfaces and APIs Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+----------+--------------------------------+-------------------+
| Ref\| sub-     | Description                    | Notes             |
| ere\| category |                                |                   |
| nce |          |                                |                   |
+=====+==========+================================+===================+
| i\  | Acce\    | The Architecture **should**    |                   |
| nt.\| leration | provide an open and standard   |                   |
| acc\|          | acceleration interface to      |                   |
| .01 |          | VNFs.                          |                   |
+-----+----------+--------------------------------+-------------------+
| i\  | Acce\    | The Architecture **should      | duplicate of      |
| nt.\| leration | not** rely on SR-IOV PCI-Pass  | inf.acc.03 under  |
| acc\|          | through for acceleration       | “Infrastructure   |
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
| R\   | sub-category    | Description          | Notes                |
| efer\|                 |                      |                      |
| ence |                 |                      |                      |
+======+=================+======================+======================+
| lc\  | Automated       | The Architecture     |                      |
| m.ad\| deployment      | **should** allow for |                      |
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
| lc\  | Automated       | The Architecture     |                      |
| m.ad\| deployment      | **should** support   |                      |
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
| lc\  | Automated       | The Architecture     |                      |
| m.ad\| deployment      | **should** support   |                      |
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
| lc\  | Automated       | The Architecture     |                      |
| m.ad\| deployment      | **should** support   |                      |
| p.05 |                 | automated process    |                      |
|      |                 | for Deployment and   |                      |
|      |                 | life-cycle           |                      |
|      |                 | management of VIM    |                      |
|      |                 | Instances.           |                      |
+------+-----------------+----------------------+----------------------+
| lc\  | CI/CD           | The Architecture     |                      |
| m.ci\|                 | **should** support   |                      |
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
| R\   | s\          | Description                    | Notes          |
| efer\| ub-category |                                |                |
| ence |             |                                |                |
+======+=============+================================+================+
| as\  | Monitoring  | The Architecture **should**    |                |
| r.mo\|             | support Network Intelligence   |                |
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

System Hardening Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:system hardening recommendations`)

+------------------+---------------+---------------+------------------+
| Reference        | sub-category  | Description   | Notes            |
+==================+===============+===============+==================+
| sec.gen.011      | Hardening     | The Cloud     |                  |
|                  |               | I\            |                  |
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
|                  |               | I\            |                  |
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

Platform and Access Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:platform and access recommendations`)

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
|               |               | I\            | Architecture (ZTA) |
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

Confidentiality and Integrity Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:confidentiality and integrity recommendations`)

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.ci.002   | Confiden\         | The Platform |                   |
|              | tiality/Integrity | **should**   |                   |
|              |                   | support      |                   |
|              |                   | sel\         |                   |
|              |                   | f-encrypting |                   |
|              |                   | storage      |                   |
|              |                   | devices      |                   |
+--------------+-------------------+--------------+-------------------+
| sec.ci.009   | Confiden\         | For          |                   |
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
|              |                   | c\           |                   |
|              |                   | ryptographic |                   |
|              |                   | keys.        |                   |
+--------------+-------------------+--------------+-------------------+

Table 2-35: Confidentiality and Integrity Recommendations

.. _workload-security-source-rm-7.9.4-1:

Workload Security Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:workload security recommendations`)

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

Image Security Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:image security recommendations`)

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

Security LCM Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:security lcm recommendations`)

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

Monitoring and Security Audit Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source
:ref:`ref_model/chapters/chapter07:monitoring and security audit recommendations`)

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

Open-Source Software Security Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:open source software recommendations`)

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.oss.005  | Software          | A Software   | `NTIA SBOM        |
|              |                   | Bill of      | <https://www.     |
|              |                   | Materials    | ntia.gov/SBOM>`__ |
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

IaaC security Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source
:ref:`ref_model/chapters/chapter07:iaac - secure design and architecture stage recommendations`)

**Secure Design and Architecture Stage**

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.arch.001 | IaaC              | Threat       | It may be done    |
|              |                   | Modelling    | manually or using |
|              |                   | m\           | tools like open   |
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

**Secure Code Stage Recommendations**

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
|              |                   | vuln\        |                   |
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

**Continuous Build, Integration and Testing Stage Recommendations**

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
|              |                   | f\           |                   |
|              |                   | unctionality |                   |
|              |                   | and          |                   |
|              |                   | detecting    |                   |
|              |                   | vul\         |                   |
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
|              |                   | vul\         |                   |
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

**Continuous Delivery and Deployment Stage Recommendations**

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

**Runtime Defence and Monitoring Recommendations**

+--------------+-------------------+--------------+-------------------+
| Reference    | sub-category      | Description  | Notes             |
+==============+===================+==============+===================+
| sec.run.002  | IaaC              | RASP –       |                   |
|              |                   | Runtime      |                   |
|              |                   | Application  |                   |
|              |                   | Sel\         |                   |
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

Compliance with Standards Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:compliance with standards recommendations`)

+-----------+-------------------+---------------------+---------------+
| Reference | sub-category      | Description         | Notes         |
+===========+===================+=====================+===============+
| se\       | Standards         | The Cloud Operator  |               |
| c.std.001 |                   | **should** comply   |               |
|           |                   | with `Center for    |               |
|           |                   | Internet Security   |               |
|           |                   | CIS                 |               |
|           |                   | Con\                |               |
|           |                   | trols <https://www. |               |
|           |                   | cisecurity.org/>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se\       | Standards         | The Cloud Operator, |               |
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
|           |                   | Alliance <\         |               |
|           |                   | https://cloudsecuri |               |
|           |                   | tyalliance.org/>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se\       | Standards         | The Platform and    |               |
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
| se\       | Standards         | The Cloud Operator, |               |
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
| se\       | Standards         | The Cloud Operator, |               |
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
| se\       | Standards         | The Cloud Operator, |               |
| c.std.006 |                   | Platform and        |               |
|           |                   | Workloads           |               |
|           |                   | **should** utilise  |               |
|           |                   | the `OWASP Web      |               |
|           |                   | Security Testing    |               |
|           |                   | Guide               |               |
|           |                   | <https://github.c   |               |
|           |                   | om/OWASP/wstg/tree/ |               |
|           |                   | master/document>`__ |               |
+-----------+-------------------+---------------------+---------------+
| se\       | Standards         | The Cloud Operator, |               |
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
| se\       | Standards         | The Cloud Operator, |               |
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
| se\       | Standards         | The Cloud Operator, |               |
| c.std.009 |                   | and Platform        |               |
|           |                   | **should**          |               |
|           |                   | implement the       |               |
|           |                   | `ISO/IEC 27032:2012 |               |
|           |                   | (or latest)         |               |
|           |                   | Guidelines for      |               |
|           |                   | Cybersecurity       |               |
|           |                   | t\                  |               |
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
| se\       | Standards         | The Cloud Operator  |               |
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
| se\       | Standards         | The Cloud Operator  |               |
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

Table 2-46: Compliance with Security Recommendations
