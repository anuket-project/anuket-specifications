Architecture Requirements
=========================

Introduction
------------

This chapter will use the requirements defined in the overall Reference Model and only make additional entries in
section `2.3 <#2.3>`__ if there are additional requirements needed for this Reference Architecture.

Definitions
-----------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in `RFC2119 <https://www.ietf.org/rfc/rfc2119.txt>`__.

Reference Model Requirements
----------------------------

The tables below contain the requirements from the Reference Model to cover the Basic and High-Performance profiles.
The table also includes a reference to the specification from
:ref:`ref_arch/kubernetes/chapters/chapter04:component level architecture` and from
:ref:`ref_arch/kubernetes/chapters/chapter05:security guidance` to ensure traceability. If the related Specification
does not exist, the reference will read "N/A" (and in bold "**N/A**" for mandatory requirements).

To ensure alignment with the infrastructure profile catalogue, the following requirements are referenced through:

-  Those relating to Cloud Infrastructure Software Profiles
-  Those relating to Cloud Infrastructure Hardware Profiles
-  Those relating to Cloud Infrastructure Management
-  Those relating to Cloud Infrastructure Security

Cloud Infrastructure Software Profile Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
| Reference Model Section  | Reference| Description            | Requirement for | Requirement for | Specification    |
|                          |          |                        | Basic Profile   | High-Performance| Reference        |
|                          |          |                        |                 | Profile         |                  |
+==========================+==========+========================+=================+=================+==================+
|`4.1.2`                   |e.cap.001 | Max number of vCPU that| At least 16     | At least 16     |`ra2.ch.011`      |
|                          |          | can be assigned to a   |                 |                 |                  |
|                          |          | single Pod by the Cloud|                 |                 |                  |
|                          |          | Infrastructure         |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.002 | Max memory in MB that  | at least 32 GB  | at least 32 GB  |`ra2.ch.012`      |
|                          |          | can be assigned to a   |                 |                 |                  |
|                          |          | single Pod by the Cloud|                 |                 |                  |
|                          |          | Infrastructure         |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.003 | Max storage in GB that | at least 320 GB | at least 320 GB |`ra2.ch.010`      |
|                          |          | can be assigned to a   |                 |                 |                  |
|                          |          | single Pod by the Cloud|                 |                 |                  |
|                          |          | Infrastructure         |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.004 | Max number of          | 6               | 6               |`ra2.ntw.003`     |
|                          |          | connection points that |                 |                 |                  |
|                          |          | can be assigned to a   |                 |                 |                  |
|                          |          | single Pod by the Cloud|                 |                 |                  |
|                          |          | Infrastructure         |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.005 | Max storage in GB that | Up to 16TB (1)  | Up to 16TB (1)  | N/A              |
|                          |          | can be attached /      |                 |                 |                  |
|                          |          | mounted to Pod by the  |                 |                 |                  |
|                          |          | Cloud Infrastructure   |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.2`                   |e.cap.006 | CPU pinning support    | Not required    | Must support    |`ra2.k8s.009`     |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.2`                   |e.cap.007 | NUMA support           | Not required    | Must support    |`ra2.k8s.006`     |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.008 | IPSec Acceleration     | Not required    | Optional        | N/A              |
|                          |          | using the virtio-ipsec |                 |                 |                  |
|                          |          | interface              |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.009 | Crypto Acceleration    | Not required    | Optional        | N/A              |
|                          |          | using the virtio-crypto|                 |                 |                  |
|                          |          | interface              |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.010 | Transcoding            | Not required    | Not required    | N/A              |
|                          |          | Acceleration           |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.011 | Programmable           | Not required    | Not required    | N/A              |
|                          |          | Acceleration           |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.012 | Enhanced Cache         | E               | E               | N/A              |
|                          |          | Management: L=Lean;    |                 |                 |                  |
|                          |          | E=Equal; X=eXpanded    |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.2`                   |e.cap.013 | SR-IOV over PCI-PT     | Not required    | Must support    |`ra2.ch.002`      |
|                          |          |                        |                 |                 |`ra2.ch.003`      |
|                          |          |                        |                 |                 |`ra2.k8s.007`     |
|                          |          |                        |                 |                 |`ra2.ntw.004`     |
|                          |          |                        |                 |                 |`ra2.ntw.008`     |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.014 | Hardware coprocessor   | Not required    | Not required    | N/A              |
|                          |          | support (GPU/NPU)      |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.015 | SmartNICs              | Not required    | Optional        | N/A              |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.016 | FPGA/other Acceleration| Not required    | Optional        |`ra2.k8s.007`     |
|                          |          | H/W                    |                 |                 |`ra2.ntw.012`     |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2`                   |e.cap.017 | *Ability to monitor    | *n/a (2)*       | \*n/a (2) \*    | N/A              |
|                          |          | L2-L7 data from        |                 |                 |                  |
|                          |          | workload*              |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.cap.014 | Specifies the          | 2               | 2               |`ra2.k8s.008`     |
|                          |          | proportion of CPU cores|                 |                 |                  |
|                          |          | consumed by the Cloud  |                 |                 |                  |
|                          |          | Infrastructure system  |                 |                 |                  |
|                          |          | on the worker nodes. If|                 |                 |                  |
|                          |          | SMT is used, it        |                 |                 |                  |
|                          |          | indicates the number of|                 |                 |                  |
|                          |          | consumed SMT threads.  |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.cap.015 | Indicates the memory   | 16 GB           | 16 GB           |                  |
|                          |          | consumed by Cloud      |                 |                 |                  |
|                          |          | Infrastructure on the  |                 |                 |                  |
|                          |          | worker nodes           |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.cap.016 | Number of virtual cores| 1:1             | 1:1             |`ra2.ch.004`      |
|                          |          | per physical core; also|                 |                 |`ra2.ch.005`      |
|                          |          | known as CPU           |                 |                 |                  |
|                          |          | overbooking ratio that |                 |                 |                  |
|                          |          | is required            |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.cap.017 | QoS enablement of the  | Not required    | Must support    | **N/A**          |
|                          |          | connection point (vNIC |                 |                 |                  |
|                          |          | or interface)          |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.cap.018 | Support for huge pages | Not required    | Must support    |`ra2.ch.001`      |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.pm.001  | Monitor worker node    | Must support    | Must support    | **N/A**          |
|                          |          | CPU usage, per         |                 |                 |                  |
|                          |          | nanosecond             |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.pm.002  | Monitor pod CPU usage, | Must support    | Must support    | **N/A**          |
|                          |          | per nanosecond         |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.pm.003  | Monitor worker node    | Must support    | Must support    | **N/A**          |
|                          |          | CPU utilisation (%)    |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.pm.004  | Monitor pod CPU        | Must support    | Must support    | **N/A**          |
|                          |          | utilisation            |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.pm.005  | Measure external       | Must support    | Must support    | **N/A**          |
|                          |          | storage IOPs           |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.pm.006  | Measure external       | Must support    | Must support    | **N/A**          |
|                          |          | storage throughput     |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4`                   |i.pm.007  | Measure external       | Must support    | Must support    | **N/A**          |
|                          |          | storage capacity       |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.2`                   |i.os.001  | Host operating system  | Must support    | Must support    |`ra2.ch.004`      |
|                          |          | must provide drivers   |                 |                 |                  |
|                          |          | etc. to support listed |                 |                 |                  |
|                          |          | capabilities.          |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+


**Table 2-1:** Reference Model Requirements: Internal Performance Measurement Capabilities
:ref:`ref_model/chapters/chapter04:capabilities and performance measurements`

**(1)** Defined in the ``.bronze`` configuration in RM section :ref:`ref_model/chapters/chapter04:storage extensions`

**(2)** In Kubernetes based infrastructures packet monitoring is out of the scope for the infrastructure.

Virtual Network Interface Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The required number of connection points to a Pod is described in ``e.cap.004`` above. This section describes the
required bandwidth of those connection points.

+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
| Reference Model Section  | Reference| Description            | Requirement for | Requirement for | Specification    |
|                          |          |                        | Basic Profile   | High-Performance| Reference        |
|                          |          |                        |                 | Profile         |                  |
+==========================+==========+========================+=================+=================+==================+
|`4.2.5`                   | n1, n2,  | 1, 2, 3, 4, 5, 6 Gbps  | Must support    | Must support    | **N/A**          |
|                          | n3, n4,  |                        |                 |                 |                  |
|                          | n5, n6   |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.5`                   | nn10,    | 10, 20, 30, 40, 50,    | Must support    | Must support    | **N/A**          |
|                          | n20,     | 60 Gbps                |                 |                 |                  |
|                          | n30,     |                        |                 |                 |                  |
|                          | n40,     |                        |                 |                 |                  |
|                          | n50, n60 |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.5`                   |n25, n50, | 25, 50, 75, 100, 125,  | Must support    | Must support    | **N/A**          |
|                          |n75, n100,| 150 Gbps               |                 |                 |                  |
|                          |n125, n150|                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.5`                   |nn50, n100| 50, 100, 150, 200,     | Must support    | Must support    | **N/A**          |
|                          |, n150,   | 250, 300 Gbps          |                 |                 |                  |
|                          |n200, n250|                        |                 |                 |                  |
|                          |, n300    |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.5`                   |n100,     | 100, 200, 300, 400,    | Must support    | Must support    | **N/A**          |
|                          |n200,     | 500, 600 Gbps          |                 |                 |                  |
|                          |n300,     |                        |                 |                 |                  |
|                          |n400,     |                        |                 |                 |                  |
|                          |n500, n600|                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+

**Table 2-2:** Reference Model Requirements: Network Interface Specifications
:ref:`ref_model/chapters/chapter04:virtual network interface specifications`

Cloud Infrastructure Software Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
| Reference Model Section  | Reference| Description            | Requirement for | Requirement for | Specification    |
|                          |          |                        | Basic Profile   | High-Performance| Reference        |
|                          |          |                        |                 | Profile         |                  |
+==========================+==========+========================+=================+=================+==================+
|`5.1.1`                   |infra.com.| CPU allocation ratio   | 1:1             | 1:1             |`ra2.ch.005`      |
|                          |cfg.001   |                        |                 |                 |`ra2.ch.006`      |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.1`                   |infra.com.| NUMA awareness         | Not required    | Must support    |`ra2.k8s.006`     |
|                          |cfg.002   |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.1`                   |infra.com.| CPU pinning capability | Not required    | Must support    |`ra2.k8s.009`     |
|                          |cfg.003   |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.1`                   |infra.com.| Huge pages             | Not required    | Must support    |`ra2.ch.001`      |
|                          |cfg.004   |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2`                   |infra.stg.| Storage Block          | Must support    | Must support    |`ra2.stg.004`     |
|                          |cfg.002   |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2`                   |infra.stg.| Storage with           | Not required    | Must support    | **N/A**          |
|                          |cfg.003   | replication            |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2`                   |infra.stg.| Storage with           | Must support    | Must support    | **N/A**          |
|                          |cfg.004   | encryption             |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2`                   |infra.stg.| Storage IOPS oriented  | Not required    | Must support    | **N/A**          |
|                          |acc.cfg.00| encryption             |                 |                 |                  |
|                          |1         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2`                   |infra.stg.| Storage capacity       | Not required    | Not required    | N/A              |
|                          |acc.cfg.00| oriented encryption    |                 |                 |                  |
|                          |2         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| IO virtualisation      | Must support    | Must support    | **N/A**          |
|                          |cfg.001   | using virtio1.1        | (1)             | (1)             |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| The overlay network    | Must support    | *No requirement | **N/A**          |
|                          |cfg.002   | encapsulation protocol | VXLAN,          | specified*      |                  |
|                          |          | needs to enable ECMP   | MPLSoUDP,       |                 |                  |
|                          |          | in the underlay to     | GENEVE, other   |                 |                  |
|                          |          | take advantage of the  |                 |                 |                  |
|                          |          | scale-out features of  |                 |                 |                  |
|                          |          | the network fabric.(2) |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| Network Address        | Must support    | Must support    | **N/A**          |
|                          |cfg.003   | Translation            |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| Security Groups        | Must support    | Must support    |`ra2.k8s.014`     |
|                          |cfg.004   |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| SFC support            | Not required    | Must support    | **N/A**          |
|                          |cfg.005   |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| Traffic patterns       | Must support    | Must support    | **N/A**          |
|                          |cfg.006   | symmetry               |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| vSwitch optimisation   | Not required    | Must support    |`ra2.ntw.010`     |
|                          |acc.cfg.00|                        |                 | DPDK (3)        |                  |
|                          |1         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| Support of HW offload  | Not required    | Optional,       | N/A              |
|                          |acc.cfg.00|                        |                 | SmartNic        |                  |
|                          |2         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| Crypto acceleration    | Not required    | Optional        | N/A              |
|                          |acc.cfg.00|                        |                 |                 |                  |
|                          |3         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3`                   |infra.net.| Crypto Acceleration    | Not required    | Optional        | N/A              |
|                          |acc.cfg.00| Interface              |                 |                 |                  |
|                          |4         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+

**Table 2-3:** Reference Model Requirements: Cloud Infrastructure Software Profile Requirements
:ref:`ref_model/chapters/chapter05:virtual networking`

**(1)** Might have other interfaces (such as SR-IOV VFs to be directly passed to a VM or a Pod) or NIC-specific drivers
on guest machines transiently allowed until more mature solutions are available with an acceptable level of efficiency
to support telecom workloads (for example regarding CPU and energy consumption).

**(2)** In Kubernetes based infrastructures network separation is possible without an overlay (e.g.: with IPVLAN)

**(3)** This feature is not applicable for Kubernetes based infrastructures due to lack of vSwitch however workloads
need access to user space networking solutions.

Cloud Infrastructure Hardware Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
| Reference Model Section  | Reference| Description            | Requirement for | Requirement for | Specification    |
|                          |          |                        | Basic Profile   | High-Performance| Reference        |
|                          |          |                        |                 | Profile         |                  |
+==========================+==========+========================+=================+=================+==================+
|`5.4.1`                   |infra.hw. | Minimum number of CPU  | 2               | 2               |`ra2.ch.008`      |
|                          |cpu.cfg.  | sockets                |                 |                 |                  |
|                          |001       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.1`                   |infra.hw. | Minimum number of      | 20              | 20              |`ra2.ch.008`      |
|                          |cpu.cfg.  | Cores per CPU          |                 |                 |                  |
|                          |002       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.1`                   |infra.hw. | NUMA Alignment         | N               | Y               |`ra2.ch.008`      |
|                          |cpu.cfg.  |                        |                 |                 |                  |
|                          |003       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.1`                   |infra.hw. | Simultaneous           | Must support    | Optional        |`ra2.ch.004`      |
|                          |cpu.cfg.  | Multithreading/        |                 |                 |                  |
|                          |004       | Symmetric              |                 |                 |                  |
|                          |          | Multiprocessing        |                 |                 |                  |
|                          |          | (SMT/SMP)              |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.1`                   |infra.hw. | GPU                    | Not required    | Optional        | N/A              |
|                          |cac.cfg.  |                        |                 |                 |                  |
|                          |001       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.2`                   |infra.hw. | Local Storage HDD      | *No requirement | *No requirement | N/A              |
|                          |stg.hdd.  |                        | specified*      | specified*      |                  |
|                          |cfg.001   |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.2`                   |infra.hw. | Local Storage SSD      | Should support  | Should support  |`ra2.ch.009`      |
|                          |stg.ssd.  |                        |                 |                 |                  |
|                          |cfg.002   |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3`                   |infra.hw. | Total Number of NIC    | 4               | 4               |`ra2.ch.013`      |
|                          |nic.cfg.  | Ports available in the |                 |                 |                  |
|                          |001       | host                   |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3`                   |infra.hw. | Port speed specified   | 10              | 25              |`ra2.ch.014`      |
|                          |nic.cfg.  | in Gbps (minimum       |                 |                 |`ra2.ch.015`      |
|                          |002       | values)                |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3`                   |infra.hw. | Number of PCIe slots   | 8               | 8               |`ra2.ch.016`      |
|                          |pci.cfg.  | available in the host  |                 |                 |                  |
|                          |001       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3`                   |infra.hw. | PCIe speed             | Gen 3           | Gen 3           |`ra2.ch.016`      |
|                          |pci.cfg.  |                        |                 |                 |                  |
|                          |002       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3`                   |infra.hw. | PCIe Lanes             | 8               | 8               |`ra2.ch.016`      |
|                          |pci.cfg.  |                        |                 |                 |                  |
|                          |003       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3`                   |infra.hw. | Cryptographic          | Not required    | Optional        | N/A              |
|                          |nac.cfg.  | Acceleration           |                 |                 |                  |
|                          |001       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3`                   |infra.hw. | A SmartNIC that is     | Not required    | Optional (1)    | N/A              |
|                          |nac.cfg.  | used to offload        |                 |                 |                  |
|                          |002       | vSwitch functionality  |                 |                 |                  |
|                          |          | to hardware            |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3`                   |infra.hw. | Compression            | Optional        | Optional        | N/A              |
|                          |nac.cfg.  |                        |                 |                 |                  |
|                          |003       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+

**Table 2-4:** Reference Model Requirements: Cloud Infrastructure Hardware Profile Requirements
:ref:`ref_model/chapters/chapter05:network acceleration configurations`

**(1)** There is no vSwitch in case of containers, but a SmartNIC can be used to offload any other network processing.

Edge Cloud Infrastructure Hardware Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the case of Telco Edge Cloud Deployments, hardware requirements can differ from the above to account for
environmental and other constraints.
The Reference Model :ref:`ref_model/chapters/chapter08:hybrid multi-cloud architecture`
includes considerations specific to deployments at the edge of the network. The infrastructure profiles "Basic" and
"High Performance" as per :ref:`ref_model/chapters/chapter04:profiles and workload flavours` still apply, but a number
of requirements of the above table are relaxed as follows:

+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
| Reference Model Section  | Reference| Description            | Requirement for | Requirement for | Specification    |
|                          |          |                        | Basic Profile   | High-Performance| Reference        |
|                          |          |                        |                 | Profile         |                  |
+==========================+==========+========================+=================+=================+==================+
|`8.x.x`                   |cpu.cfg.  | sockets                |                 |                 |                  |
|                          |001       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`8.x.x`                   |infra.hw. | Minimum number of      | 1               | 1               |`ra2.ch.008`      |
|                          |cpu.cfg.  | Cores per CPU          |                 |                 |                  |
|                          |002       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`8.x.x`                   |infra.hw. | NUMA Alignment         |  N              | Y (1)           |`ra2.ch.008`      |
|                          |cpu.cfg.  |                        |                 |                 |                  |
|                          |003       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+

**Table 2-5:** Reference Model Requirements: Edge Cloud Infrastructure Hardware Profile Requirements.
:ref:`ref_model/chapters/chapter08:telco edge cloud: infrastructure profiles`.

**(1)** immaterial if the number of CPU sockets (infra.hw.cpu.cfg.001) is 1.

Cloud Infrastructure Management Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
| Reference Model Section          | Reference | Description                    | Requirement     | Specification     |
|                                  |           |                                | (common to all  | Reference         |
|                                  |           |                                | Profiles)       |                   |
+==================================+===========+================================+=================+===================+
|`4.1.5`                           | e.man.001 | Capability to allocate virtual | Must support    | **N/A**           |
|                                  |           | compute resources to a         |                 |                   |
|                                  |           | workload                       |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5`                           | e.man.002 | Capability to allocate virtual | Must support    | **N/A**           |
|                                  |           | storage resources to a         |                 |                   |
|                                  |           | workload                       |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5`                           | e.man.003 | Capability to allocate virtual | Must support    | **N/A**           |
|                                  |           | networking resources to a      |                 |                   |
|                                  |           | workload                       |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5`                           | e.man.004 | Capability to isolate          | Must support    | **N/A**           |
|                                  |           | resources between tenants      |                 |                   |
|                                  |           |                                |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5`                           | e.man.005 | Capability to manage workload  | Must support    | **N/A**           |
|                                  |           | software images                |                 |                   |
|                                  |           |                                |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5`                           | e.man.006 | Capability to provide          | Must support    | **N/A**           |
|                                  |           | information related to         |                 |                   |
|                                  |           | allocated virtualised          |                 |                   |
|                                  |           | resources per tenant           |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5`                           | e.man.007 | Capability to notify state     | Must support    | **N/A**           |
|                                  |           | changes of allocated resources |                 |                   |
|                                  |           |                                |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5`                           | e.man.008 | Capability to collect and      | Must support    | **N/A**           |
|                                  |           | expose performance information |                 |                   |
|                                  |           | on virtualised resources       |                 |                   |
|                                  |           | allocated                      |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5`                           | e.man.009 | Capability to collect and      | Must support    | **N/A**           |
|                                  |           | notify fault information on    |                 |                   |
|                                  |           | virtualised resources          |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+

**Table 2-6:** Reference Model Requirements: Cloud Infrastructure Management Requirements
:ref:`ref_model/chapters/chapter04:cloud infrastructure management capabilities`.


Cloud Infrastructure Security Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+-----------+--------------------------------------+-------------------------+
| Reference Model Section                | Reference | Description                          | Specification           |
|                                        |           |                                      | Reference               |
|                                        |           |                                      |                         |
+========================================+===========+======================================+=========================+
|`7.9.1`                                 |sec.gen.001| The Platform **must** maintain the   |                         |
|                                        |           | specified configuration.             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.002| All systems part of Cloud            | `5.3.1 Node Hardening:  |
|                                        |           | Infrastructure **must** support      | Securing Kubernetes     |
|                                        |           | password hardening as defined in     | Hosts`                  |
|                                        |           | `CIS Password Policy Guide <https:// |                         |
|                                        |           | www.cisecurity.org/white-papers/cis- |                         |
|                                        |           | -policy-guide/>`__. Hardening: CIS   |                         |
|                                        |           | Password Policy Guide                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.003| All servers part of Cloud            |                         |
|                                        |           | Infrastructure **must** support a    |                         |
|                                        |           | root of trust and secure boot.       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.004| The Operating Systems of all the     | `5.2 Principles` and    |
|                                        |           | servers part of Cloud Infrastructure | `5.3 Node Hardening`    |
|                                        |           | **must** be hardened by removing or  |                         |
|                                        |           | disabling unnecessary services,      |                         |
|                                        |           | applications and network protocols,  |                         |
|                                        |           | configuring operating system user    |                         |
|                                        |           | authentication, configuring resource |                         |
|                                        |           | controls, installing and configuring |                         |
|                                        |           | additional security controls where   |                         |
|                                        |           | needed, and testing the security of  |                         |
|                                        |           | the Operating System.                |                         |
|                                        |           | (NIST SP 800-123)                    |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.005| The Platform **must** support        | `5.3 Node Hardening`    |
|                                        |           | Operating System level access        |                         |
|                                        |           | control                              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.006| The Platform **must** support Secure | `5.3.2 Restrict direct  |
|                                        |           | logging. Logging with root account   | access to nodes`        |
|                                        |           | must be prohibited when root         |                         |
|                                        |           | privileges are not required.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.007| All servers part of Cloud            |                         |
|                                        |           | Infrastructure **must** be Time      |                         |
|                                        |           | synchronized with authenticated Time |                         |
|                                        |           | service.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.008| All servers part of Cloud            | `5.3.3 Vulnerability    |
|                                        |           | Infrastructure **must** be regularly | assessment`             |
|                                        |           | updated to address security          |                         |
|                                        |           | vulnerabilities.                     |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.009| The Platform **must** support        | `5.4 Securing           |
|                                        |           | Software integrity protection and    | Kubernetes orchestrator`|
|                                        |           | verification and **must** scan       |                         |
|                                        |           | source code and manifests.           |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.010| The Cloud Infrastructure **must**    |                         |
|                                        |           | support encrypted storage, for       |                         |
|                                        |           | example, block, object and file      |                         |
|                                        |           | storage, with access to encryption   |                         |
|                                        |           | keys restricted based on a need to   |                         |
|                                        |           | know. `Controlled Access Based on    |                         |
|                                        |           | the Need to Know <https://www.cisecu |                         |
|                                        |           | rity.org/controls/controlled-access- |                         |
|                                        |           | based-on-the-need-to-know/>`__       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.011| The Cloud Infrastructure **should**  |                         |
|                                        |           | support Read and Write only storage  |                         |
|                                        |           | partitions (write only permission to |                         |
|                                        |           | one or more authorized actors).      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.012| The Operator **must** ensure that    |                         |
|                                        |           | only authorized actors have physical |                         |
|                                        |           | access to the underlying             |                         |
|                                        |           | infrastructure.                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.013| The Platform **must** ensure that    | `5.4 Securing           |
|                                        |           | only authorized actors have logical  | Kubernetes orchestrator`|
|                                        |           | access to the underlying             |                         |
|                                        |           | infrastructure.                      |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.014| All servers part of Cloud            |                         |
|                                        |           | Infrastructure **should** support    |                         |
|                                        |           | measured boot and an attestation     |                         |
|                                        |           | server that monitors the             |                         |
|                                        |           | measurements of the servers.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1`                                 |sec.gen.015| Any change to the Platform must be   |                         |
|                                        |           | logged as a security event, and the  |                         |
|                                        |           | logged event must include the        |                         |
|                                        |           | identity of the entity making the    |                         |
|                                        |           | change, the change, the date and the |                         |
|                                        |           | time of the change.                  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.001| The Platform **must** support        | `5.4 Securing           |
|                                        |           | authenticated and secure access to   | Kubernetes orchestrator`|
|                                        |           | API, GUI and command line            |                         |
|                                        |           | interfaces.                          |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.002| The Platform **must** support        |                         |
|                                        |           | Traffic Filtering for workloads (for |                         |
|                                        |           | example, Firewall).                  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.003| The Platform **must** support Secure | `5.4.3 Use Transport    |
|                                        |           | and encrypted communications, and    | Layer Security and      |
|                                        |           | confidentiality and integrity of     | Service Mesh`           |
|                                        |           | network traffic.                     |                         |
|                                        |           |                                      |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.004| The Cloud Infrastructure **must**    | `5.4.3 Use Transport    |
|                                        |           | support authentication, integrity    | Layer Security and      |
|                                        |           | and confidentiality on all network   | Service Mesh`           |
|                                        |           | channels.                            |                         |
|                                        |           |                                      |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.005| The Cloud Infrastructure **must**    |                         |
|                                        |           | segregate the underlay and overlay   |                         |
|                                        |           | networks.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.006| The Cloud Infrastructure must be     | `5.2 Principles`        |
|                                        |           | able to utilise the Cloud            |                         |
|                                        |           | Infrastructure Manager identity      |                         |
|                                        |           | lifecycle management capabilities.   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.007| The Platform **must** implement      | `5.2 Principles`        |
|                                        |           | controls enforcing separation of     |                         |
|                                        |           | duties and privileges, least         |                         |
|                                        |           | privilege use and least common       | `5.4 Securing           |
|                                        |           | mechanism (Role-Based Access         | Kubernetes orchestrator`|
|                                        |           | Control).                            |                         |
|                                        |           |                                      |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.008| The Platform **must** be able to     |                         |
|                                        |           | assign the Entities that comprise    |                         |
|                                        |           | the tenant networks to different     |                         |
|                                        |           | trust domains. Communication between |                         |
|                                        |           | different trust domains is not       |                         |
|                                        |           | allowed, by default.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.009| The Platform **must** support        |                         |
|                                        |           | creation of Trust Relationships      |                         |
|                                        |           | between trust domains.               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.010| For two or more domains without      |                         |
|                                        |           | existing trust relationships, the    |                         |
|                                        |           | Platform **must not** allow the      |                         |
|                                        |           | effect of an attack on one domain to |                         |
|                                        |           | impact the other domains either      |                         |
|                                        |           | directly or indirectly.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.011| The Platform **must not** reuse the  |                         |
|                                        |           | same authentication credential       |                         |
|                                        |           | (e.g., key-pair) on different        |                         |
|                                        |           | Platform components (e.g., on        |                         |
|                                        |           | different hosts, or different        |                         |
|                                        |           | services).                           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.012| The Platform **must** protect all    |                         |
|                                        |           | secrets by using strong encryption   |                         |
|                                        |           | techniques, and storing the          |                         |
|                                        |           | protected secrets externally from    |                         |
|                                        |           | the component                        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.013| The Platform **must** provide        |                         |
|                                        |           | secrets dynamically as and when      |                         |
|                                        |           | needed.                              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.014| The Platform **should** use Linux    |                         |
|                                        |           | Security Modules such as SELinux to  |                         |
|                                        |           | control access to resources.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.015| The Platform **must not** contain    |                         |
|                                        |           | back door entries (unpublished       |                         |
|                                        |           | access points, APIs, etc.).          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.016| Login access to the platform's       | `5.4 Securing           |
|                                        |           | components **must** be through       | Kubernetes orchestrator`|
|                                        |           | encrypted protocols such as SSH v2   |                         |
|                                        |           | or TLS v1.2 or higher. Note:         |                         |
|                                        |           | Hardened jump servers isolated from  |                         |
|                                        |           | external networks are recommended    |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.017| The Platform **must** provide the    |                         |
|                                        |           | capability of using digital          |                         |
|                                        |           | certificates that comply with X.509  |                         |
|                                        |           | standards issued by a trusted        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.018| The Platform **must** provide the    |                         |
|                                        |           | capability of allowing certificate   |                         |
|                                        |           | renewal and revocation.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.019| The Platform **must** provide the    |                         |
|                                        |           | capability of testing the validity   |                         |
|                                        |           | of a digital certificate (CA         |                         |
|                                        |           | signature, validity period, non      |                         |
|                                        |           | revocation, identity).               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2`                                 |sec.sys.020| The Cloud Infrastructure             |                         |
|                                        |           | architecture **should** rely on Zero |                         |
|                                        |           | Trust principles to build a secure   |                         |
|                                        |           | by design environment.               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.001 | The Platform **must** support        | `5.4 Securing           |
|                                        |           | Confidentiality and Integrity of     | Kubernetes orchestrator`|
|                                        |           | data at rest and in-transit.         |                         |
|                                        |           | by design environment.               |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.002 | The Platform **should** support      |                         |
|                                        |           | self-encrypting storage devices.     |                         |
|                                        |           | data at rest and in-transit.         |                         |
|                                        |           | by design environment.               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.003 | The Platform **must** support        |                         |
|                                        |           | Confidentiality and Integrity of     |                         |
|                                        |           | data related metadata.               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.004 | The Platform **must** support        |                         |
|                                        |           | Confidentiality of processes and     |                         |
|                                        |           | restrict information sharing with    |                         |
|                                        |           | only the process owner (e.g.,        |                         |
|                                        |           | tenant).                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.005 | The Platform **must** support        |                         |
|                                        |           | Confidentiality and Integrity of     |                         |
|                                        |           | process-related metadata and         |                         |
|                                        |           | restrict information sharing with    |                         |
|                                        |           | only the process owner (e.g.,        |                         |
|                                        |           | tenant).                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.006 | The Platform **must** support        |                         |
|                                        |           | Confidentiality and Integrity of     |                         |
|                                        |           | workload resource utilization (RAM,  |                         |
|                                        |           | CPU, Storage, Network I/O, cache,    |                         |
|                                        |           | hardware offload) and restrict       |                         |
|                                        |           | information sharing with only the    |                         |
|                                        |           | workload owner (e.g., tenant).       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.007 | The Platform **must not** allow      |                         |
|                                        |           | Memory Inspection by any actor other |                         |
|                                        |           | than the authorized actors for the   |                         |
|                                        |           | Entity to which Memory is assigned   |                         |
|                                        |           | (e.g., tenants owning the workload), |                         |
|                                        |           | for Lawful Inspection, and by secure |                         |
|                                        |           | monitoring services.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.008 | The Cloud Infrastructure **must**    | `5.7 Create and define  |
|                                        |           | support tenant networks segregation. | Network Policies`       |
|                                        |           |                                      |                         |
|                                        |           |                                      |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.3`                                 |sec.ci.009 | For sensitive data encryption, the   |                         |
|                                        |           | key management service **should**    |                         |
|                                        |           | leverage a Hardware Security Module  |                         |
|                                        |           | to manage and protect cryptographic  |                         |
|                                        |           | keys.                                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4`                                 |sec.wl.001 | The Platform **must** support        |                         |
|                                        |           | Workload placement policy.           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4`                                 |sec.wl.002 | The Cloud Infrastructure **must**    |                         |
|                                        |           | provide methods to ensure the        |                         |
|                                        |           | platform’s trust status and          |                         |
|                                        |           | integrity (e.g. remote attestation,  |                         |
|                                        |           | Trusted Platform Module).            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4`                                 |sec.wl.003 | The Platform **must** support secure | `5.4 Securing           |
|                                        |           | provisioning of workloads.           | Kubernetes orchestrator`|
|                                        |           |                                      |                         |
|                                        |           |                                      |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4`                                 |sec.wl.004 | The Platform **must** support        |                         |
|                                        |           | Location assertion (for mandated     |                         |
|                                        |           | in-country or location               |                         |
|                                        |           | requirements).                       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4`                                 |sec.wl.005 | The Platform **must** support the    | `5.4 Securing           |
|                                        |           | separation of production and         | Kubernetes orchestrator`|
|                                        |           | non-production Workloads.            |                         |
|                                        |           |                                      |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4`                                 |sec.wl.006 | The Platform **must** support the    | `5.4 Securing           |
|                                        |           | separation of Workloads based on     | Kubernetes orchestrator`|
|                                        |           | their categorisation (for example,   |                         |
|                                        |           | payment card information,            |                         |
|                                        |           | healthcare, etc.).                   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4`                                 |sec.wl.007 | The Operator **must** implement      | `5.13 Trusted Registry` |
|                                        |           | processes and tools to verify VNF    |                         |
|                                        |           | authenticity and integrity.          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.001| Images from untrusted sources **must | `5.13 Trusted Registry` |
|                                        |           | not** be used.                       |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.002| Images **must** be scanned to be     | `5.13 Trusted Registry` |
|                                        |           | maintained free from known           |                         |
|                                        |           | vulnerabilities.                     |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.003| Images **must not** be configured to | `5.11 Run-Time Security`|
|                                        |           | run with privileges higher than the  |                         |
|                                        |           | privileges of the actor authorized   |                         |
|                                        |           | to run them.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.004| Images **must** only be accessible   |                         |
|                                        |           | to authorized actors.                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.005| Image Registries **must** only be    |                         |
|                                        |           | accessible to authorized actors.     |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.006| Image Registries **must** only be    | `5.13 Trusted Registry` |
|                                        |           | accessible over secure networks that |                         |
|                                        |           | enforce authentication, integrity    |                         |
|                                        |           | and confidentiality.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.007| Image registries **must** be clear   | `5.13 Trusted Registry` |
|                                        |           | of vulnerable and out of date        |                         |
|                                        |           | versions.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.008| Images **must not** include any      | `5.12 Secrets Mgmt.`    |
|                                        |           | secrets. Secrets include passwords,  |                         |
|                                        |           | cloud provider credentials, SSH      |                         |
|                                        |           | keys, TLS certificate keys, etc.     |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.009| CIS Hardened Images **should** be    |                         |
|                                        |           | used whenever possible.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5`                                 |sec.img.010| Minimalist base images **should** be |                         |
|                                        |           | used whenever possible.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.001| The Platform **must** support Secure |                         |
|                                        |           | Provisioning, Availability, and      |                         |
|                                        |           | Deprovisioning (Secure Clean-Up) of  |                         |
|                                        |           | workload resources where Secure      |                         |
|                                        |           | Clean-Up includes tear-down, defense |                         |
|                                        |           | against virus or other attacks.      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.002| Cloud operations staff and systems   | `5.4 Securing           |
|                                        |           | **must** use management protocols    | Kubernetes              |
|                                        |           | limiting security risk such as       | orchestrator`           |
|                                        |           | SNMPv3, SSH v2, ICMP, NTP, syslog    |                         |
|                                        |           | and TLS v1.2 or higher.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.003| The Cloud Operator **must**          |                         |
|                                        |           | implement and strictly follow change |                         |
|                                        |           | management processes for Cloud       |                         |
|                                        |           | Infrastructure, Cloud Infrastructure |                         |
|                                        |           | Manager and other components of the  |                         |
|                                        |           | cloud, and Platform change control   |                         |
|                                        |           | on hardware.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.004| The Cloud Operator **should**        |                         |
|                                        |           | support automated templated approved |                         |
|                                        |           | changes.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.005| Platform **must** provide logs and   | `5.10 Enable Logging    |
|                                        |           | these logs must be regularly         | and Monitoring`         |
|                                        |           | monitored for anomalous behavior.    |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.006| The Platform **must** verify the     |                         |
|                                        |           | integrity of all Resource management |                         |
|                                        |           | requests.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.007| The Platform **must** be able to     | `5.4 Securing           |
|                                        |           | update newly instantiated,           | Kubernetes              |
|                                        |           | suspended, hibernated, migrated and  | orchestrator`           |
|                                        |           | restarted images with current time   |                         |
|                                        |           | information.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.008| The Platform **must** be able to     |                         |
|                                        |           | update newly instantiated,           |                         |
|                                        |           | suspended, hibernated, migrated and  |                         |
|                                        |           | restarted images with relevant DNS   |                         |
|                                        |           | information.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.009| The Platform **must** be able to     |                         |
|                                        |           | update the tag of newly              |                         |
|                                        |           | instantiated, suspended,             |                         |
|                                        |           | hibernated, migrated and restarted   |                         |
|                                        |           | images with relevant geolocation     |                         |
|                                        |           | (geographical) information.          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.010| The Platform **must** log all        |                         |
|                                        |           | changes to geolocation along with    |                         |
|                                        |           | the mechanisms and sources of        |                         |
|                                        |           | location information (i.e. GPS, IP   |                         |
|                                        |           | block, and timing).                  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.011| The Platform **must** implement      |                         |
|                                        |           | Security life cycle management       |                         |
|                                        |           | processes including the proactive    |                         |
|                                        |           | update and patching of all deployed  |                         |
|                                        |           | Cloud Infrastructure software.       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6`                                 |sec.lcm.012| The Platform **must** log any access |                         |
|                                        |           | privilege escalation.                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.001| Platform **must** provide logs and   |                         |
|                                        |           | these logs must be regularly         |                         |
|                                        |           | monitored for events of interest.    |                         |
|                                        |           | The logs **must** contain the        |                         |
|                                        |           | following fields: event type,        |                         |
|                                        |           | date/time, protocol, service or      |                         |
|                                        |           | program used for access,             |                         |
|                                        |           | success/failure, login ID or process |                         |
|                                        |           | ID, IP address and ports (source     |                         |
|                                        |           | and destination) involved.           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.002| Security logs **must** be time       |                         |
|                                        |           | synchronised.                        |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.003| The Platform **must** log all        |                         |
|                                        |           | changes to time server source, time, |                         |
|                                        |           | date and time zones.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.004| The Platform **must** secure and     |                         |
|                                        |           | protect Audit logs (containing       |                         |
|                                        |           | sensitive information) both          |                         |
|                                        |           | in-transit and at rest.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.005| The Platform **must** Monitor and    |                         |
|                                        |           | Audit various behaviours of          |                         |
|                                        |           | connection and login attempts to     |                         |
|                                        |           | detect access attacks and potential  |                         |
|                                        |           | access attempts and take corrective  |                         |
|                                        |           | actions accordingly.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.006| The Platform **must** Monitor and    |                         |
|                                        |           | Audit operations by authorized       |                         |
|                                        |           | account access after login to detect |                         |
|                                        |           | malicious operational activity and   |                         |
|                                        |           | take corrective actions accordingly. |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.007| The Platform **must** Monitor and    |                         |
|                                        |           | Audit security parameter             |                         |
|                                        |           | configurations for compliance with   |                         |
|                                        |           | defined security policies.           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.008| The Platform **must** Monitor and    |                         |
|                                        |           | Audit externally exposed interfaces  |                         |
|                                        |           | for illegal access (attacks) and     |                         |
|                                        |           | take corrective security hardening   |                         |
|                                        |           | measures.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.009| The Platform **must** Monitor and    |                         |
|                                        |           | Audit service handling for various   |                         |
|                                        |           | attacks (malformed messages,         |                         |
|                                        |           | signalling flooding and replaying,   |                         |
|                                        |           | etc.) and take corrective actions    |                         |
|                                        |           | accordingly.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.010| The Platform **must** Monitor and    |                         |
|                                        |           | Audit running processes to detect    |                         |
|                                        |           | unexpected or unauthorized processes |                         |
|                                        |           | and take corrective actions          |                         |
|                                        |           | accordingly.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.011| The Platform **must** Monitor and    |                         |
|                                        |           | Audit logs from infrastructure       |                         |
|                                        |           | elements and workloads to detected   |                         |
|                                        |           | anomalies in the system components   |                         |
|                                        |           | and take corrective actions          |                         |
|                                        |           | accordingly.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.012| The Platform **must** Monitor and    |                         |
|                                        |           | Audit Traffic patterns and volumes   |                         |
|                                        |           | to prevent malware download          |                         |
|                                        |           | attempts.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.013| The monitoring system **must not**   |                         |
|                                        |           | affect the security (integrity and   |                         |
|                                        |           | confidentiality) of the              |                         |
|                                        |           | infrastructure, workloads, or the    |                         |
|                                        |           | user data (through back door         |                         |
|                                        |           | entries).                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.014| The Monitoring systems **should      |                         |
|                                        |           | not** impact IAAS, PAAS, and SAAS    |                         |
|                                        |           | SLAs including availability SLAs.    |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.015| The Platform **must** ensure that    |                         |
|                                        |           | the Monitoring systems are never     |                         |
|                                        |           | starved of resources and **must**    |                         |
|                                        |           | activate alarms when resource        |                         |
|                                        |           | utilisation exceeds a configurable   |                         |
|                                        |           | threshold.                           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.016| The Platform Monitoring components   |                         |
|                                        |           | **should** follow security best      |                         |
|                                        |           | practices for auditing, including    |                         |
|                                        |           | secure logging and tracing.          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.017| The Platform **must** audit systems  | `5.3.3 Vulnerability    |
|                                        |           | for any missing security patches and | assessment`             |
|                                        |           | take appropriate actions.            |                         |
|                                        |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.018| The Platform, starting from          | `5.3.4 Patch management`|
|                                        |           | initialization, **must** collect and |                         |
|                                        |           | analyze logs to identify security    |                         |
|                                        |           | events, and store these events in an |                         |
|                                        |           | external system.                     |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.019| The Platform’s components **must     |                         |
|                                        |           | not** include an authentication      |                         |
|                                        |           | credential, e.g., password, in any   |                         |
|                                        |           | logs, even if encrypted.             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.020| The Platform’s logging system        |                         |
|                                        |           | **must** support the storage of      |                         |
|                                        |           | security audit logs for a            |                         |
|                                        |           | configurable period of time.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.7`                                 |sec.mon.021| The Platform **must** store security |                         |
|                                        |           | events locally if the external       |                         |
|                                        |           | logging system is unavailable and    |                         |
|                                        |           | shall periodically attempt to send   |                         |
|                                        |           | these to the external logging system |                         |
|                                        |           | until successful.                    |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8`                                 |sec.oss.001| Open source code **must** be         | `5.3.3 Vulnerability    |
|                                        |           | inspected by tools with various      | assessment`             |
|                                        |           | capabilities for static and dynamic  |                         |
|                                        |           | code analysis.                       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8`                                 |sec.oss.002| The `CVE (Common Vulnerabilities     |                         |
|                                        |           | and Exposures) <https://cve.mitre.or |                         |
|                                        |           | g/>`__ **must** be used to identify  |                         |
|                                        |           | vulnerabilities and their severity   |                         |
|                                        |           | rating for open source code part of  |                         |
|                                        |           | Cloud Infrastructure and workloads   |                         |
|                                        |           | software.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8`                                 |sec.oss.003| Critical and high severity rated     |                         |
|                                        |           | vulnerabilities **must** be fixed in |                         |
|                                        |           | a timely manner. Refer to the `CVSS  |                         |
|                                        |           | (Common Vulnerability Scoring System)|                         |
|                                        |           | <https://www.first.org/cvss/>`__ to  |                         |
|                                        |           | know a vulnerability score and its   |                         |
|                                        |           | associated rate (low, medium, high,  |                         |
|                                        |           | or critical).                        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8`                                 |sec.oss.004| A dedicated internal isolated        | `5.13 Trusted Registry` |
|                                        |           | repository separated from the        |                         |
|                                        |           | production environment **must** be   |                         |
|                                        |           | used to store vetted open source     |                         |
|                                        |           | content.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8`                                 |sec.oss.005| A Software Bill of Materials (`SBOM  |                         |
|                                        |           | <https://www.ntia.gov/SBOM>`__)      |                         |
|                                        |           | **should** be provided or build, and |                         |
|                                        |           | maintained to identify the software  |                         |
|                                        |           | components and their origins.        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.9`                                 |sec.arch.00| Threat Modelling methodologies and   |                         |
|                                        |1          | tools **should** be used during the  |                         |
|                                        |           | Secure Design and Architecture stage |                         |
|                                        |           | triggered by Software Feature Design |                         |
|                                        |           | trigger. It may be done manually or  |                         |
|                                        |           | using tools like open source OWASP   |                         |
|                                        |           | Threat Dragon                        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.9`                                 |sec.arch.00| Security Control Baseline Assessment |                         |
|                                        |2          | **should** be performed during the   |                         |
|                                        |           | Secure Design and Architecture stage |                         |
|                                        |           | triggered by Software Feature Design |                         |
|                                        |           | trigger. Typically done manually by  |                         |
|                                        |           | internal or independent assessors.   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10`                                |sec.code.00| SAST -Static Application Security    |                         |
|                                        |1          | Testing **must** be applied during   |                         |
|                                        |           | Secure Coding stage triggered by     |                         |
|                                        |           | Pull, Clone or Comment trigger.      |                         |
|                                        |           | Security testing that analyses       |                         |
|                                        |           | application source code for software |                         |
|                                        |           | vulnerabilities and gaps against     |                         |
|                                        |           | best practices. Example: open source |                         |
|                                        |           | OWASP range of tools.                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10`                                |sec.code.00| SCA – Software Composition Analysis  |                         |
|                                        |2          | **should** be applied during Secure  |                         |
|                                        |           | Coding stage triggered by Pull,      |                         |
|                                        |           | Clone or Comment trigger. Security   |                         |
|                                        |           | testing that analyses application    |                         |
|                                        |           | source code or compiled code for     |                         |
|                                        |           | software components with known       |                         |
|                                        |           | vulnerabilities. Example: open       |                         |
|                                        |           | source OWASP range of tools.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10`                                |sec.code.00| Source Code Review **should** be     |                         |
|                                        |3          | performed continuously during Secure |                         |
|                                        |           | Coding stage. Typically done         |                         |
|                                        |           | manually.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10`                                |sec.code.00| Integrated SAST via IDE Plugins      |                         |
|                                        |4          | **should** be used during Secure     |                         |
|                                        |           | Coding stage triggered by Developer  |                         |
|                                        |           | Code trigger. On the local machine:  |                         |
|                                        |           | through the IDE or integrated test   |                         |
|                                        |           | suites; triggered on completion of   |                         |
|                                        |           | coding be developer.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10`                                |sec.code.00| SAST of Source Code Repo **should**  |                         |
|                                        |5          | be performed during Secure Coding    |                         |
|                                        |           | stage triggered by Developer Code    |                         |
|                                        |           | trigger. Continuous delivery         |                         |
|                                        |           | pre-deployment: scanning prior to    |                         |
|                                        |           | deployment.                          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11`                                |sec.bld.001| SAST -Static Application Security    |                         |
|                                        |           | Testing **should** be applied during |                         |
|                                        |           | the Continuous Build, Integration    |                         |
|                                        |           | and Testing stage triggered by Build |                         |
|                                        |           | and Integrate trigger. Example: open |                         |
|                                        |           | source OWASP range of tools.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11`                                |sec.bld.002| SCA – Software Composition Analysis  |                         |
|                                        |           | **should** be applied during the     |                         |
|                                        |           | Continuous Build, Integration and    |                         |
|                                        |           | Testing stage triggered by Build and |                         |
|                                        |           | Integrate trigger. Example: open     |                         |
|                                        |           | source OWASP range of tools.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11`                                |sec.bld.003| Image Scan **must** be applied       |                         |
|                                        |           | during the Continuous Build,         |                         |
|                                        |           | Integration and Testing stage        |                         |
|                                        |           | triggered by Package trigger.        |                         |
|                                        |           | Example: A push of a container image |                         |
|                                        |           | to a container registry may trigger  |                         |
|                                        |           | a vulnerability scan before the      |                         |
|                                        |           | image becomes available in the       |                         |
|                                        |           | registry.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11`                                |sec.bld.004| DAST – Dynamic Application Security  |                         |
|                                        |           | Testing **should** be applied during |                         |
|                                        |           | the Continuous Build, Integration    |                         |
|                                        |           | and Testing stage triggered by Stage |                         |
|                                        |           | & Test trigger. Security testing     |                         |
|                                        |           | that analyses a running application  |                         |
|                                        |           | by exercising application            |                         |
|                                        |           | functionality and detecting          |                         |
|                                        |           | vulnerabilities based on             |                         |
|                                        |           | application behaviour and response.  |                         |
|                                        |           | Example: OWASP ZAP.                  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11`                                |sec.bld.005| Fuzzing **should** be applied during |                         |
|                                        |           | the Continuous Build, Integration    |                         |
|                                        |           | and testing stage triggered by Stage |                         |
|                                        |           | & Test trigger. Fuzzing or fuzz      |                         |
|                                        |           | testing is an automated software     |                         |
|                                        |           | testing technique that involves      |                         |
|                                        |           | providing invalid, unexpected, or    |                         |
|                                        |           | random data as inputs to a computer  |                         |
|                                        |           | program. Example: GitLab Open        |                         |
|                                        |           | Sources Protocol Fuzzer Community    |                         |
|                                        |           | Edition.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11`                                |sec.bld.006| IAST – Interactive Application       |                         |
|                                        |           | Security Testing **should** be       |                         |
|                                        |           | applied during the Continuous Build, |                         |
|                                        |           | Integration and Testing stage        |                         |
|                                        |           | triggered by Stage & Test trigger.   |                         |
|                                        |           | Software component deployed with an  |                         |
|                                        |           | application that assesses            |                         |
|                                        |           | application behaviour and detects    |                         |
|                                        |           | presence of vulnerabilities on an    |                         |
|                                        |           | application being exercised in       |                         |
|                                        |           | realistic testing scenarios.         |                         |
|                                        |           | Example: Contrast Community Edition. |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.12`                                |sec.del.001| Image Scan **must** be applied       |                         |
|                                        |           | during the Continuous Delivery and   |                         |
|                                        |           | Deployment stage triggered by        |                         |
|                                        |           | Publish to Artifact and Image        |                         |
|                                        |           | Repository trigger. Example: GitLab  |                         |
|                                        |           | uses the open-source Clair engine    |                         |
|                                        |           | for container image scanning.        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.12`                                |sec.del.002| Code Signing **must** be applied     |                         |
|                                        |           | during the Continuous Delivery and   |                         |
|                                        |           | Deployment stage triggered by        |                         |
|                                        |           | Publish to Artifact and Image        |                         |
|                                        |           | Repository trigger. Code Signing     |                         |
|                                        |           | provides authentication to assure    |                         |
|                                        |           | that downloaded files are form the   |                         |
|                                        |           | publisher named on the certificate.  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.12`                                |sec.del.003| Artifact and Image Repository Scan   |                         |
|                                        |           | **should** be continuously applied   |                         |
|                                        |           | during the Continuous Delivery and   |                         |
|                                        |           | Deployment stage. Example: GitLab    |                         |
|                                        |           | uses the open source Clair engine    |                         |
|                                        |           | for container scanning.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.12`                                |sec.del.004| Component Vulnerability Scan         |                         |
|                                        |           | **must** be applied during the       |                         |
|                                        |           | Continuous Delivery and Deployment   |                         |
|                                        |           | stage triggered by Instantiate       |                         |
|                                        |           | Infrastructure trigger. The          |                         |
|                                        |           | vulnerability scanning system is     |                         |
|                                        |           | deployed on the cloud platform to    |                         |
|                                        |           | detect security vulnerabilities of   |                         |
|                                        |           | specified components through         |                         |
|                                        |           | scanning and to provide timely       |                         |
|                                        |           | security protection. Example: OWASP  |                         |
|                                        |           | Zed Attack Proxy (ZAP).              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.13`                                |sec.run.001| Component Vulnerability Monitoring   |                         |
|                                        |           | **must** be continuously applied     |                         |
|                                        |           | during the Runtime Defence and       |                         |
|                                        |           | Monitoring stage and remediation     |                         |
|                                        |           | actions **must** be applied for high |                         |
|                                        |           | severity rated vulnerabilities.      |                         |
|                                        |           | Security technology that monitors    |                         |
|                                        |           | components like virtual servers and  |                         |
|                                        |           | assesses data, applications, and     |                         |
|                                        |           | infrastructure for security risks.   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.13`                                |sec.run.002| RASP – Runtime Application Self-     |                         |
|                                        |           | Protection **should** be             |                         |
|                                        |           | continuously applied during the      |                         |
|                                        |           | Runtime Defence and Monitoring       |                         |
|                                        |           | stage. Security technology deployed  |                         |
|                                        |           | within the target application in     |                         |
|                                        |           | production for detecting, alerting,  |                         |
|                                        |           | and blocking attacks.                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.13`                                |sec.run.003| Application testing and Fuzzing      |                         |
|                                        |           | **should** be continuously applied   |                         |
|                                        |           | during the Runtime Defence and       |                         |
|                                        |           | Monitoring stage. Fuzzing or fuzz    |                         |
|                                        |           | testing is an automated software     |                         |
|                                        |           | testing technique that involves      |                         |
|                                        |           | providing invalid, unexpected, or    |                         |
|                                        |           | random data as inputs to a computer  |                         |
|                                        |           | program. Example: GitLab Open        |                         |
|                                        |           | Sources Protocol Fuzzer Community    |                         |
|                                        |           | Edition.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.13`                                |sec.run.004| Penetration Testing **should** be    |                         |
|                                        |           | continuously applied during the      |                         |
|                                        |           | Runtime Defence and Monitoring       |                         |
|                                        |           | stage. Typically done manually.      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.001| The Cloud Operator **should** comply |                         |
|                                        |           | with Center for Internet Security    |                         |
|                                        |           | CIS Controls (`https://www.cisecur   |                         |
|                                        |           | ity.org/ <https://www.cisecurity.org |                         |
|                                        |           | />`__)                               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.002| The Cloud Operator, Platform and     |                         |
|                                        |           | Workloads **should** follow the      |                         |
|                                        |           | guidance in the CSA Security         |                         |
|                                        |           | Guidance for Critical Areas of Focus |                         |
|                                        |           | in Cloud Computing (latest version)  |                         |
|                                        |           | `https://cloudsecurityalliance.      |                         |
|                                        |           | org/ <https://cloudsecurityalliance. |                         |
|                                        |           | org/>`__                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.003| The Platform and Workloads           |                         |
|                                        |           | **should** follow the guidance in    |                         |
|                                        |           | the `OWASP Cheat Sheet Series (OCSS) |                         |
|                                        |           | <https://github.com/OWASP/CheatSheet |                         |
|                                        |           | Series>`__                           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.004| The Cloud Operator, Platform and     |                         |
|                                        |           | Workloads **should** ensure that     |                         |
|                                        |           | their code is not vulnerable to the  |                         |
|                                        |           | OWASP Top Ten Security Risks         |                         |
|                                        |           | `https://owasp.org/www-project-top-t |                         |
|                                        |           | en/ <https://owasp.org/www-project-t |                         |
|                                        |           | op-ten/>`__                          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.005| The Cloud Operator, Platform and     |                         |
|                                        |           | Workloads **should** strive to       |                         |
|                                        |           | improve their maturity on the `OWASP |                         |
|                                        |           | Software Maturity Model (SAMM) <http |                         |
|                                        |           | s://owaspsamm.org/blog/2019/12/20/ve |                         |
|                                        |           | rsion2-community-release/>`__        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.006| The Cloud Operator, Platform and     |                         |
|                                        |           | Workloads **should** utilize the `OW |                         |
|                                        |           | ASP Web Security Testing Guide <http |                         |
|                                        |           | s://github.com/OWASP/wstg/tree/maste |                         |
|                                        |           | r/document>`__                       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.007| The Cloud Operator, and Platform     |                         |
|                                        |           | **should** satisfy the requirements  |                         |
|                                        |           | for Information Management Systems   |                         |
|                                        |           | specified in `ISO/IEC 27001 <https:/ |                         |
|                                        |           | /www.iso.org/obp/ui/#iso:std:iso-iec |                         |
|                                        |           | :27001:ed-2:v1:en>`__. ISO/IEC       |                         |
|                                        |           | 27002:2013 - ISO/IEC 27001 is the    |                         |
|                                        |           | international Standard for           |                         |
|                                        |           | best-practice information security   |                         |
|                                        |           | management systems (ISMSs).          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.008| The Cloud Operator, and Platform     |                         |
|                                        |           | **should** implement the Code of     |                         |
|                                        |           | practice for Security Controls       |                         |
|                                        |           | specified `ISO/IEC 27002:2013 (or la |                         |
|                                        |           | test) <https://www.iso.org/obp/ui/#i |                         |
|                                        |           | so:std:iso-iec:27002:ed-2:v1:en>`__  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.009| The Cloud Operator, and Platform     |                         |
|                                        |           | **should** implement the `ISO/IEC 27 |                         |
|                                        |           | 032:2012 (or latest) <https://www.is |                         |
|                                        |           | o.org/obp/ui/#iso:std:iso-iec:27032: |                         |
|                                        |           | ed-1:v1:en>`__ Guidelines for        |                         |
|                                        |           | Cybersecurity techniques. ISO/IEC    |                         |
|                                        |           | 27032 - ISO/IEC 27032 is the         |                         |
|                                        |           | international Standard focusing      |                         |
|                                        |           | explicitly on cybersecurity.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.010| The Cloud Operator **should**        |                         |
|                                        |           | conform to the ISO/IEC 27035         |                         |
|                                        |           | standard for incidence management.   |                         |
|                                        |           | ISO/IEC 27035 - ISO/IEC 27035 is the |                         |
|                                        |           | international Standard for incident  |                         |
|                                        |           | management.                          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.011| The Cloud Operator **should**        |                         |
|                                        |           | conform to the ISO/IEC 27031         |                         |
|                                        |           | standard for business continuity.    |                         |
|                                        |           | ISO/IEC 27031 - ISO/IEC 27031 is the |                         |
|                                        |           | international Standard for ICT       |                         |
|                                        |           | readiness for business continuity.   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14`                                |sec.std.012| The Public Cloud Operator **must**,  |                         |
|                                        |           | and the Private Cloud Operator       |                         |
|                                        |           | **may** be certified to be compliant |                         |
|                                        |           | with the International Standard on   |                         |
|                                        |           | Awareness Engagements (ISAE) 3402    |                         |
|                                        |           | (in the US: SSAE 16). International  |                         |
|                                        |           | Standard on Awareness Engagements    |                         |
|                                        |           | (ISAE) 3402. US Equivalent: SSAE16.  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+

**Table 2-7:** Reference Model Requirements: Cloud Infrastructure Security Requirements
:ref:`ref_model/chapters/chapter07:consolidated security requirements`

Kubernetes Architecture Requirements
------------------------------------

The requirements in this section are to be delivered in addition to those in section 2.2, and have been
created to support the Principles defined in the :ref:`ref_arch/kubernetes/chapters/chapter01:Overview` of this
Reference Architecture.

The Reference Model (RM) defines the Cloud Infrastructure, which consists of the physical resources, virtualised
resources and a software management system.

In virtualisation platforms, the Cloud Infrastructure consists of the Guest Operating System, Hypervisor and, if
needed, other software such as libvirt. The Cloud Infrastructure Management component is responsible for, among others,
tenant management, resources management, inventory, scheduling, and access management.

With regards to containerisation platforms, the scope of the following Architecture requirements include the Cloud
Infrastructure Hardware (e.g. physical resources), Cloud Infrastructure Software (e.g. Hypervisor (optional), Container
Runtime, virtual or container Orchestrator(s), Operating System), and infrastructure resources consumed by virtual
machines or containers.

+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|Reference | Category     | Sub-category | Description                          | Specification Reference             |
+==========+==============+==============+======================================+=====================================+
|gen.cnt.02| General      | Cloud        | The Architecture **must** support    | `ra2.ch.017`                        |
|          |              | nativeness   | immutable infrastructure.            |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.cnt.03| General      | Cloud        | The Architecture **must** run        | `ra2.k8s.001`                       |
|          |              | nativeness   | conformant Kubernetes as defined by  |                                     |
|          |              |              | the `CNCF <https://github.com/cncf/k |                                     |
|          |              |              | 8s-conformance>`__.                  |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.cnt.04| General      | Cloud        | The Architecture **must** support    |                                     |
|          |              | nativeness   | clearly defined abstraction layers.  |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.cnt.05| General      | Cloud        | The Architecture **should** support  |                                     |
|          |              | nativeness   | configuration of all components in   |                                     |
|          |              |              | an automated manner using openly     |                                     |
|          |              |              | published API definitions.           |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.scl.01| General      | Scalability  | The Architecture **should** support  |                                     |
|          |              |              | policy driven horizontal             |                                     |
|          |              |              | auto-scaling of workloads.           |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.rsl.01| General      | Resiliency   | The Architecture **must** support    | `ra2.k8s.004`                       |
|          |              |              | resilient Kubernetes components that |                                     |
|          |              |              | are required for the continued       |                                     |
|          |              |              | availability of running workloads.   |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.rsl.02| General      | Resiliency   | The Architecture **should** support  | `ra2.k8s.002`, `ra2.k8s.003`        |
|          |              |              | resilient Kubernetes service         |                                     |
|          |              |              | components that are not subject to   |                                     |
|          |              |              | gen.rsl.01.                          |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.avl.01| General      | Availability | The Architecture **must** provide    | `ra2.k8s.002`, `ra2.k8s.003`,       |
|          |              |              | High Availability for Kubernetes     | `ra2.k8s.004`                       |
|          |              |              | components.                          |                                     |
|          |              |              |                                      |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.ost.01| Openness     | Availability | The Architecture **should** embrace  | `ra2.crt.001`, `ra2.crt.002`,       |
|          |              |              | open-based standards and             | `ra2.ntw.002`, `ra2.ntw.006`,       |
|          |              |              | technologies.                        | `ra2.ntw.007`                       |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.com.01|Infrastructure| Compute      | The Architecture **must** provide    | `ra2.k8s.004`                       |
|          |              |              | compute resources for Pods.          |                                     |
|          |              |              | technologies.                        |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.stg.01|Infrastructure| Storage      | The Architecture **must** support    | `ra2.stg.004`                       |
|          |              |              | the ability for an operator to       |                                     |
|          |              |              | choose whether or not to deploy      |                                     |
|          |              |              | persistent storage for Pods.         |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.01|Infrastructure| Network      | The Architecture **must** support    |                                     |
|          |              |              | network resiliency on the Kubernetes |                                     |
|          |              |              | nodes.                               |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.02|Infrastructure| Network      | The Architecture **must** support    |                                     |
|          |              |              | fully redundant network connectivity |                                     |
|          |              |              | to the Kubernetes nodes, leveraging  |                                     |
|          |              |              | multiple network connections.        |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.03|Infrastructure| Network      | The networking solution **should**   | `ra2.ntw.001, `ra2.ntw.004`         |
|          |              |              | be able to be centrally              |                                     |
|          |              |              | administrated and configured.        |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.04|Infrastructure| Network      | The Architecture **must** support    | `ra2.ch.007`, `ra2.k8s.010`         |
|          |              |              | dual stack IPv4 and IPv6 for         |                                     |
|          |              |              | Kubernetes workloads.                |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.05|Infrastructure| Network      | The Architecture **must** support    |                                     |
|          |              |              | capabilities for integrating SDN     |                                     |
|          |              |              | controllers.                         |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.06|Infrastructure| Network      | The Architecture **must** support    | `ra2.ntw.005`, `ra2.ntw.007`        |
|          |              |              | more than one networking solution.   |                                     |
|          |              |              |                                      |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.07|Infrastructure| Network      | The Architecture **must** support    | `ra2.ntw.005`                       |
|          |              |              | the ability for an operator to       |                                     |
|          |              |              | choose whether or not to deploy more |                                     |
|          |              |              | than one networking solution.        |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.08|Infrastructure| Network      | The Architecture **must** provide a  | `ra2.ntw.002`                       |
|          |              |              | default network which implements the |                                     |
|          |              |              | Kubernetes network model.            |                                     |
|          |              |              |                                      |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.09|Infrastructure| Network      | The networking solution **must not** |                                     |
|          |              |              | interfere with or cause interference |                                     |
|          |              |              | to any interface or network it does  |                                     |
|          |              |              | not own.                             |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.10|Infrastructure| Network      | The Architecture **must** support    |                                     |
|          |              |              | Cluster wide coordination of IP      |                                     |
|          |              |              | address assignment.                  |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.13|Infrastructure| Network      | The platform **must** allow          |                                     |
|          |              |              | specifying multiple separate IP      |                                     |
|          |              |              | pools. Tenants are required to       |                                     |
|          |              |              | select at least one IP pool that is  |                                     |
|          |              |              | different from the control           |                                     |
|          |              |              | infrastructure IP pool or other      |                                     |
|          |              |              | tenant IP pools.                     |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.14|Infrastructure| Network      | The platform **must** allow NATless  | `ra2.ntw.011`                       |
|          |              |              | traffic (i.e. exposing the pod IP    |                                     |
|          |              |              | address directly to the outside),    |                                     |
|          |              |              | allowing source and destination IP   |                                     |
|          |              |              | addresses to be preserved in the     |                                     |
|          |              |              | traffic headers from workloads to    |                                     |
|          |              |              | external networks. This is needed    |                                     |
|          |              |              | e.g. for signaling applications,     |                                     |
|          |              |              | using SIP and Diameter protocols.    |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.15|Infrastructure| Network      | The platform **must** support        |                                     |
|          |              |              | LoadBalancer `Publishing Service     |                                     |
|          |              |              | (ServiceType) <https://kubernetes.io |                                     |
|          |              |              | /docs/concepts/services-networking/s |                                     |
|          |              |              | ervice/#publishing-services-service- |                                     |
|          |              |              | types>`__                            |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.16|Infrastructure| Network      | The platform **must** support        |                                     |
|          |              |              | `Ingress <https://kubernetes.io/docs |                                     |
|          |              |              | /concepts/services-networking/ingres |                                     |
|          |              |              | s/>`__.                              |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.17|Infrastructure| Network      | The platform **should** support      |                                     |
|          |              |              | NodePort `Publishing Service         |                                     |
|          |              |              | (ServiceTypes) <https://kubernetes.i |                                     |
|          |              |              | o/docs/concepts/services-networking/ |                                     |
|          |              |              | service/#publishing-services-service |                                     |
|          |              |              | -types>`__.                          |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.18|Infrastructure| Network      | The platform **should** support      |                                     |
|          |              |              | ExternalName `Publishing Service     |                                     |
|          |              |              | (ServiceTypes) <https://kubernetes.i |                                     |
|          |              |              | o/docs/concepts/services-networking/ |                                     |
|          |              |              | service/#publishing-services-service |                                     |
|          |              |              | -types>`__.                          |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.vir.01|Infrastructure| Virtual Infr | The Architecture **must** support    | `ra2.ch.005`                        |
|          |              | astructure   | the capability for Containers to     | `ra2.ch.011`                        |
|          |              |              | consume infrastructure resources     |                                     |
|          |              |              | abstracted by Host Operating Systems |                                     |
|          |              |              | that are running within a virtual    |                                     |
|          |              |              | machine.                             |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.phy.01|Infrastructure| Physical     | The Architecture **must** support    | `ra2.ch.008`                        |
|          |              | Infrastructu | the capability for Containers to     |                                     |
|          |              | re           | consume infrastructure resources     |                                     |
|          |              |              | abstracted by Host Operating Systems |                                     |
|          |              |              | that are running within a physical   |                                     |
|          |              |              | server.                              |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|kcm.gen.01| Kubernetes   | General      | The Architecture **must** support    | **N/A**                             |
|          | Cluster      |              | policy driven horizontal auto-       |                                     |
|          |              |              | scaling of Kubernetes Cluster.       |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|kcm.gen.02| Kubernetes   | General      | The Architecture **must** enable     | `ra2.k8s.004`                       |
|          | Cluster      |              | workload resiliency.                 |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|int.api.01| API          | General      | The Architecture **must** leverage   | For Networking: `ra2.ntw.001`,      |
|          |              |              | the Kubernetes APIs to discover and  | `ra2.ntw.008`, `ra2.app.006`        |
|          |              |              | declaratively manage compute         |                                     |
|          |              |              | (virtual and bare metal resources),  |                                     |
|          |              |              | network, and storage.                |                                     |
|          |              |              |                                      | Compute/storage not yet met.        |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|int.api.02| API          | General      | The Architecture **must** support    | `ra2.pkg.001`                       |
|          |              |              | the usage of a Kubernetes            |                                     |
|          |              |              | Application package manager using    |                                     |
|          |              |              | the Kubernetes API, like Helm v3.    |                                     |
|          |              |              | network, and storage.                |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|int.api.03| API          | General      | The Architecture **must** support    |                                     |
|          |              |              | stable features in its APIs.         |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|int.api.04| API          | General      | The Architecture **must** support    |                                     |
|          |              |              | limited backward compatibility in    |                                     |
|          |              |              | its APIs. Support for the whole API  |                                     |
|          |              |              | must not be dropped, but the schema  |                                     |
|          |              |              | or other details can change.         |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+

**Table 2-8:** Kubernetes Architecture Requirements
