Architecture Requirements
=========================

Introduction
------------

This chapter will use the requirements defined in the overall Reference Model and only make additional entries in section
`2.3 <#2.3>`__ if there are additional requirements needed for this Reference Architecture.

Definitions
-----------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in `RFC2119 <https://www.ietf.org/rfc/rfc2119.txt>`__.

Reference Model Requirements
----------------------------

The tables below contain the requirements from the Reference Model to cover the Basic and High-Performance profiles.
The table also includes a reference to the specification from
`Chapter 04 - Component Level Architecture <./chapter04.md>`__ and from
`Chapter 05 - Security Guidance </chapter05.md>`__ to ensure traceability. If the related Specification does not
exist, the reference will read "N/A" (and in bold "**N/A**" for mandatory requirements).

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
|`4.1.2 <../../../ref_model|e.cap.001 | Max number of vCPU that| At least 16     | At least 16     |`ra2.ch.011 <chapt|
|/chapters/chapter04.md#exp|          | can be assigned to a   |                 |                 |er04.md#kubernetes|
|osed-infrastructure-capabi|          | single Pod by the Cloud|                 |                 |-node>`__         |
|lities>`__                |          | Infrastructure         |                 |                 |                  |
|                          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.002 | Max memory in MB that  | at least 32 GB  | at least 32 GB  |`ra2.ch.012 <chapt|
|/chapters/chapter04.md#exp|          | can be assigned to a   |                 |                 |er04.md#kubernetes|
|osed-infrastructure-capabi|          | single Pod by the Cloud|                 |                 |-node>`__         |
|lities>`__                |          | Infrastructure         |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.003 | Max storage in GB that | at least 320 GB | at least 320 GB |`ra2.ch.010 <chapt|
|/chapters/chapter04.md#exp|          | can be assigned to a   |                 |                 |er04.md#kubernetes|
|osed-infrastructure-capabi|          | single Pod by the Cloud|                 |                 |-node>`__         |
|lities>`__                |          | Infrastructure         |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.004 | Max number of          | 6               | 6               |`ra2.ntw.003 <chap|
|/chapters/chapter04.md#exp|          | connection points that |                 |                 |ter04.md#networkin|
|osed-infrastructure-capabi|          | can be assigned to a   |                 |                 |g-solutions>`__   |
|lities>`__                |          | single Pod by the Cloud|                 |                 |                  |
|                          |          | Infrastructure         |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.005 | Max storage in GB that | Up to 16TB (1)  | Up to 16TB (1)  | N/A              |
|/chapters/chapter04.md#exp|          | can be attached /      |                 |                 |                  |
|osed-infrastructure-capabi|          | mounted to Pod by the  |                 |                 |                  |
|lities>`__                |          | Cloud Infrastructure   |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.2 <../../../ref_model|e.cap.006 | CPU pinning support    | Not required    | Must support    |`ra2.k8s.009 <chap|
|/chapters/chapter04.md#pro|          |                        |                 |                 |ter04.md#kubernete|
|files-specifications--capa|          |                        |                 |                 |s>`__             |
|bility-mapping>`__        |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.2 <../../../ref_model|e.cap.007 | NUMA support           | Not required    | Must support    |`ra2.k8s.006 <chap|
|/chapters/chapter04.md#pro|          |                        |                 |                 |ter04.md#kubernete|
|files-specifications--capa|          |                        |                 |                 |s>`__             |
|bility-mapping>`__        |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.008 | IPSec Acceleration     | Not required    | Optional        | N/A              |
|/chapters/chapter04.md#exp|          | using the virtio-ipsec |                 |                 |                  |
|osed-infrastructure-capabi|          | interface              |                 |                 |                  |
|lities>`__                |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.009 | Crypto Acceleration    | Not required    | Optional        | N/A              |
|/chapters/chapter04.md#exp|          | using the virtio-crypto|                 |                 |                  |
|osed-infrastructure-capabi|          | interface              |                 |                 |                  |
|lities>`__                |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.010 | Transcoding            | Not required    | Not required    | N/A              |
|/chapters/chapter04.md#exp|          | Acceleration           |                 |                 |                  |
|osed-infrastructure-capabi|          |                        |                 |                 |                  |
|lities>`__                |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.011 | Programmable           | Not required    | Not required    | N/A              |
|/chapters/chapter04.md#exp|          | Acceleration           |                 |                 |                  |
|osed-infrastructure-capabi|          |                        |                 |                 |                  |
|lities>`__                |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.012 | Enhanced Cache         | E               | E               | N/A              |
|/chapters/chapter04.md#exp|          | Management: L=Lean;    |                 |                 |                  |
|osed-infrastructure-capabi|          | E=Equal; X=eXpanded    |                 |                 |                  |
|lities>`__                |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.2 <../../../ref_model|e.cap.013 | SR-IOV over PCI-PT     | Not required    | Must support    |`ra2.ch.002 <chapt|
|/chapters/chapter04.md#pro|          |                        |                 |                 |er04.md#kubernetes|
|files-specifications--capa|          |                        |                 |                 |-node>`__,        |
|bility-mapping>`__        |          |                        |                 |                 |`ra2.ch.003 <chapt|
|                          |          |                        |                 |                 |er04.md#kubernetes|
|                          |          |                        |                 |                 |-node>`__,        |
|                          |          |                        |                 |                 |`ra2.k8s.007 <chap|
|                          |          |                        |                 |                 |ter04.md#kubernete|
|                          |          |                        |                 |                 |s>`__,            |
|                          |          |                        |                 |                 |`ra2.ntw.004 <chap|
|                          |          |                        |                 |                 |ter04.md#networkin|
|                          |          |                        |                 |                 |g-solutions>`__,  |
|                          |          |                        |                 |                 |`ra2.ntw.008 <chap|
|                          |          |                        |                 |                 |ter04.md#networkin|
|                          |          |                        |                 |                 |g-solutions>`__   |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.014 | Hardware coprocessor   | Not required    | Not required    | N/A              |
|/chapters/chapter04.md#exp|          | support (GPU/NPU)      |                 |                 |                  |
|osed-infrastructure-capabi|          |                        |                 |                 |                  |
|lities>`__                |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.015 | SmartNICs              | Not required    | Optional        | N/A              |
|/chapters/chapter04.md#exp|          |                        |                 |                 |                  |
|osed-infrastructure-capabi|          |                        |                 |                 |                  |
|lities>`__                |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|e.cap.016 | FPGA/other Acceleration| Not required    | Optional        |`ra2.k8s.007 <chap|
|/chapters/chapter04.md#exp|          | H/W                    |                 |                 |ter04.md#kubernete|
|osed-infrastructure-capabi|          |                        |                 |                 |s>`__,            |
|lities>`__                |          |                        |                 |                 |`ra2.ntw.012 <chap|
|                          |          |                        |                 |                 |ter04.md#networkin|
|                          |          |                        |                 |                 |g-solutions>`__   |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.2 <../../../ref_model|*e.cap.017| *Ability to monitor    | *n/a (2)*       | \*n/a (2) \*    | N/A              |
|/chapters/chapter04.md#exp|*         | L2-L7 data from        |                 |                 |                  |
|osed-infrastructure-capabi|          | workload*              |                 |                 |                  |
|lities>`__                |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.cap.014 | Specifies the          | 2               | 2               |`ra2.k8s.008 <chap|
|/chapters/chapter04.md#int|          | proportion of CPU cores|                 |                 |ter04.md#kubernete|
|ernal-infrastructure-capab|          | consumed by the Cloud  |                 |                 |s>`__             |
|ilities>`__               |          | Infrastructure system  |                 |                 |                  |
|                          |          | on the worker nodes. If|                 |                 |                  |
|                          |          | SMT is used, it        |                 |                 |                  |
|                          |          | indicates the number of|                 |                 |                  |
|                          |          | consumed SMT threads.  |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.cap.015 | Indicates the memory   | 16 GB           | 16 GB           |                  |
|/chapters/chapter04.md#int|          | consumed by Cloud      |                 |                 |                  |
|ernal-infrastructure-capab|          | Infrastructure on the  |                 |                 |                  |
|ilities>`__               |          | worker nodes           |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.cap.016 | Number of virtual cores| 1:1             | 1:1             |`ra2.ch.004 <chapt|
|/chapters/chapter04.md#int|          | per physical core; also|                 |                 |er04.md#kubernetes|
|ernal-infrastructure-capab|          | known as CPU           |                 |                 |-node>`__,        |
|ilities>`__               |          | overbooking ratio that |                 |                 |`ra2.ch.005 <chapt|
|                          |          | is required            |                 |                 |er04.md#kubernetes|
|                          |          |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.cap.017 | QoS enablement of the  | Not required    | Must support    | **N/A**          |
|/chapters/chapter04.md#int|          | connection point (vNIC |                 |                 |                  |
|ernal-infrastructure-capab|          | or interface)          |                 |                 |                  |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.cap.018 | Support for huge pages | Not required    | Must support    |`ra2.ch.001 <chapt|
|/chapters/chapter04.md#int|          |                        |                 |                 |er04.md#kubernetes|
|ernal-infrastructure-capab|          |                        |                 |                 |-node>`__         |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.pm.001  | Monitor worker node    | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#int|          | CPU usage, per         |                 |                 |                  |
|ernal-infrastructure-capab|          | nanosecond             |                 |                 |                  |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.pm.002  | Monitor pod CPU usage, | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#int|          | per nanosecond         |                 |                 |                  |
|ernal-infrastructure-capab|          |                        |                 |                 |                  |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.pm.003  | Monitor worker node    | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#int|          | CPU utilisation (%)    |                 |                 |                  |
|ernal-infrastructure-capab|          |                        |                 |                 |                  |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.pm.004  | Monitor pod CPU        | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#int|          | utilisation            |                 |                 |                  |
|ernal-infrastructure-capab|          |                        |                 |                 |                  |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.pm.005  | Measure external       | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#int|          | storage IOPs           |                 |                 |                  |
|ernal-infrastructure-capab|          |                        |                 |                 |                  |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.pm.006  | Measure external       | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#int|          | storage throughput     |                 |                 |                  |
|ernal-infrastructure-capab|          |                        |                 |                 |                  |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.1.4 <../../../ref_model|i.pm.007  | Measure external       | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#int|          | storage capacity       |                 |                 |                  |
|ernal-infrastructure-capab|          |                        |                 |                 |                  |
|ilities>`__               |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.2 <../../../ref_model|i.os.001  | Host operating         | Must support    | Must support    |`ra2.ch.004 <chapt|
|/chapters/chapter04.md#pro|          | system support         |                 |                 |er04.md#kubernetes|
|files-specifications--capa|          |                        |                 |                 |-node>`__         |
|bility-mapping>`__        |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+


**Table 2-1:** Reference Model Requirements: Cloud Infrastructure Software Profile Capabilities

**(1)** Defined in the ``.bronze`` configuration in section
`4.2.6 Storage Extensions <../../../ref_model/chapters/chapter04.md#storage-extensions>`__

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
|`4.2.5 <../../../ref_model| n1, n2,  | 1, 2, 3, 4, 5, 6 Gbps  | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#vir| n3, n4,  |                        |                 |                 |                  |
|tual-network-interface-spe| n5, n6   |                        |                 |                 |                  |
|cifications>`__           |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.5 <../../../ref_model| nn10,    | 10, 20, 30, 40, 50,    | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#vir| n20,     | 60 Gbps                |                 |                 |                  |
|tual-network-interface-spe| n30,     |                        |                 |                 |                  |
|cifications>`__           | n40,     |                        |                 |                 |                  |
|                          | n50, n60 |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.5 <../../../ref_model|n25, n50, | 25, 50, 75, 100, 125,  | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#vir|n75, n100,| 150 Gbps               |                 |                 |                  |
|tual-network-interface-spe|n125, n150|                        |                 |                 |                  |
|cifications>`__           |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.5 <../../../ref_model|nn50, n100| 50, 100, 150, 200,     | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#vir|, n150,   | 250, 300 Gbps          |                 |                 |                  |
|tual-network-interface-spe|n200, n250|                        |                 |                 |                  |
|cifications>`__           |, n300    |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`4.2.5 <../../../ref_model|n100,     | 100, 200, 300, 400,    | Must support    | Must support    | **N/A**          |
|/chapters/chapter04.md#vir|n200,     | 500, 600 Gbps          |                 |                 |                  |
|tual-network-interface-spe|n300,     |                        |                 |                 |                  |
|cifications>`__           |n400,     |                        |                 |                 |                  |
|                          |n500, n600|                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+

**Table 2-2:** Reference Model Requirements: Network Interface Specifications

Cloud Infrastructure Software Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
| Reference Model Section  | Reference| Description            | Requirement for | Requirement for | Specification    |
|                          |          |                        | Basic Profile   | High-Performance| Reference        |
|                          |          |                        |                 | Profile         |                  |
+==========================+==========+========================+=================+=================+==================+
|`5.1.1 <../../../ref_model|infra.com.| CPU allocation ratio   | 1:1             | 1:1             |`ra2.ch.005 <chapt|
|/chapters/chapter05.md#vir|cfg.001   |                        |                 |                 |er04.md#kubernetes|
|tual-compute>`__          |          |                        |                 |                 |-node>`__,        |
|                          |          |                        |                 |                 |`ra2.ch.006 <chapt|
|                          |          |                        |                 |                 |er04.md#kubernetes|
|                          |          |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.1 <../../../ref_model|infra.com.| NUMA awareness         | Not required    | Must support    |`ra2.k8s.006 <chap|
|/chapters/chapter05.md#vir|cfg.002   |                        |                 |                 |ter04.md#kubernete|
|tual-compute>`__          |          |                        |                 |                 |s>`__             |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.1 <../../../ref_model|infra.com.| CPU pinning capability | Not required    | Must support    |`ra2.k8s.009 <chap|
|/chapters/chapter05.md#vir|cfg.003   |                        |                 |                 |ter04.md#kubernete|
|tual-compute>`__          |          |                        |                 |                 |s>`__             |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.1 <../../../ref_model|infra.com.| Huge pages             | Not required    | Must support    |`ra2.ch.001 <chapt|
|/chapters/chapter05.md#vir|cfg.004   |                        |                 |                 |ter04.md#kubernete|
|tual-compute>`__          |          |                        |                 |                 |s-node>`__        |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2 <../../../ref_model|infra.stg.| Storage Block          | Must support    | Must support    |`ra2.stg.004 <chap|
|/chapters/chapter05.md#vir|cfg.002   |                        |                 |                 |ter04.md#storage-c|
|tual-storage>`__          |          |                        |                 |                 |omponents>`__     |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2 <../../../ref_model|infra.stg.| Storage with           | Not required    | Must support    | **N/A**          |
|/chapters/chapter05.md#vir|cfg.003   | replication            |                 |                 |                  |
|tual-storage>`__          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2 <../../../ref_model|infra.stg.| Storage with           | Must support    | Must support    | **N/A**          |
|/chapters/chapter05.md#vir|cfg.004   | encryption             |                 |                 |                  |
|tual-storage>`__          |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2 <../../../ref_model|infra.stg.| Storage IOPS oriented  | Not required    | Must support    | **N/A**          |
|/chapters/chapter05.md#vir|acc.cfg.00| encryption             |                 |                 |                  |
|tual-storage>`__          |1         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.2 <../../../ref_model|infra.stg.| Storage capacity       | Not required    | Not required    | N/A              |
|/chapters/chapter05.md#vir|acc.cfg.00| oriented encryption    |                 |                 |                  |
|tual-storage>`__          |2         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| IO virtualisation      | Must support    | Must support    | **N/A**          |
|/chapters/chapter05.md#vir|cfg.001   | using virtio1.1        | (1)             | (1)             |                  |
|tual-networking>`__       |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| The overlay network    | Must support    | *No requirement | **N/A**          |
|/chapters/chapter05.md#vir|cfg.002   | encapsulation protocol | VXLAN,          | specified*      |                  |
|tual-networking>`__       |          | needs to enable ECMP   | MPLSoUDP,       |                 |                  |
|                          |          | in the underlay to     | GENEVE, other   |                 |                  |
|                          |          | take advantage of the  |                 |                 |                  |
|                          |          | scale-out features of  |                 |                 |                  |
|                          |          | the network fabric.(2) |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| Network Address        | Must support    | Must support    | **N/A**          |
|/chapters/chapter05.md#vir|cfg.003   | Translation            |                 |                 |                  |
|tual-networking>`__       |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| Security Groups        | Must support    | Must support    |`ra2.k8s.014 <chap|
|/chapters/chapter05.md#vir|cfg.004   |                        |                 |                 |ter04.md#kubernete|
|tual-networking>`__       |          |                        |                 |                 |s>`__             |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| SFC support            | Not required    | Must support    | **N/A**          |
|/chapters/chapter05.md#vir|cfg.005   |                        |                 |                 |                  |
|tual-networking>`__       |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| Traffic patterns       | Must support    | Must support    | **N/A**          | 
|/chapters/chapter05.md#vir|cfg.006   | symmetry               |                 |                 |                  |
|tual-networking>`__       |          |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| vSwitch optimisation   | Not required    | Must support    |`ra2.ntw.010 <chap|
|/chapters/chapter05.md#vir|acc.cfg.00|                        |                 | DPDK (3)        |ter04.md#networkin|
|tual-networking>`__       |1         |                        |                 |                 |g-solutions>`__   |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| Support of HW offload  | Not required    | Optional,       | N/A              |
|/chapters/chapter05.md#vir|acc.cfg.00|                        |                 | SmartNic        |                  |
|tual-networking>`__       |2         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| Crypto acceleration    | Not required    | Optional        | N/A              |
|/chapters/chapter05.md#vir|acc.cfg.00|                        |                 |                 |                  |
|tual-networking>`__       |3         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.1.3 <../../../ref_model|infra.net.| Crypto Acceleration    | Not required    | Optional        | N/A              |
|/chapters/chapter05.md#vir|acc.cfg.00| Interface              |                 |                 |                  |
|tual-networking>`__       |4         |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+

**Table 2-3:** Reference Model Requirements: Cloud Infrastructure Software Profile Requirements

**(1)** `Workload Transition Guidelines. <../chapters/appendix-a.md>`__ might have other interfaces (such as SR-IOV VFs
to be directly passed to a VM or a Pod) or NIC-specific drivers on guest machines transiently allowed until more mature
solutions are available with an acceptable level of efficiency to support telecom workloads (for example regarding CPU
and energy consumption).

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
|`5.4.1 <../../../ref_model|infra.hw. | Minimum number of CPU  | 2               | 2               |`ra2.ch.008 <chapt|
|/chapters/chapter05.md#com|cpu.cfg.  | sockets                |                 |                 |er04.md#kubernetes|
|pute-resources>`__        |001       |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.1 <../../../ref_model|infra.hw. | Minimum number of      | 20              | 20              |`ra2.ch.008 <chapt|
|/chapters/chapter05.md#com|cpu.cfg.  | Cores per CPU          |                 |                 |er04.md#kubernetes|
|pute-resources>`__        |002       |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.1 <../../../ref_model|infra.hw. | Minimum number of      | 20              | 20              |`ra2.ch.008 <chapt|
|/chapters/chapter05.md#com|cpu.cfg.  | Cores per CPU          |                 |                 |er04.md#kubernetes|
|pute-resources>`__        |003       |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.1 <../../../ref_model|infra.hw. | Simultaneous           | Must support    | Optional        |`ra2.ch.004 <chapt|
|/chapters/chapter05.md#com|cpu.cfg.  | Multithreading/        |                 |                 |er04.md#kubernetes|
|pute-resources>`__        |004       | Symmetric              |                 |                 |-node>`__         |
|                          |          | Multiprocessing        |                 |                 |                  |
|                          |          | (SMT/SMP)              |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.1 <../../../ref_model|infra.hw. | GPU                    | Not required    | Optional        | N/A              |
|/chapters/chapter05.md#com|cac.cfg.  |                        |                 |                 |                  |
|pute-resources>`__        |001       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.2 <../../../ref_model|infra.hw. | Local Storage HDD      | *No requirement | *No requirement | N/A              |
|/chapters/chapter05.md#sto|stg.hdd.  |                        | specified*      | specified*      |                  |
|rage-configurations>`__   |cfg.001   |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.2 <../../../ref_model|infra.hw. | Local Storage SSD      | Should support  | Should support  |`ra2.ch.009 <chapt|
|/chapters/chapter05.md#sto|stg.ssd.  |                        |                 |                 |er04.md#kubernetes|
|rage-configurations>`__   |cfg.002   |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3 <../../../ref_model|infra.hw. | Total Number of NIC    | 4               | 4               |`ra2.ch.013 <chapt|
|/chapters/chapter05.md#net|nic.cfg.  | Ports available in the |                 |                 |er04.md#kubernetes|
|work-resources>`__        |001       | host                   |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3 <../../../ref_model|infra.hw. | Port speed specified   | 10              | 25              |`ra2.ch.014 <chapt|
|/chapters/chapter05.md#net|nic.cfg.  | in Gbps (minimum       |                 |                 |er04.md#kubernetes|
|work-resources>`__        |002       | values)                |                 |                 |-node>`__,        |
|                          |          |                        |                 |                 |`ra2.ch.015 <chapt|
|                          |          |                        |                 |                 |er04.md#kubernetes|
|                          |          |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3 <../../../ref_model|infra.hw. | Number of PCIe slots   | 8               | 8               |`ra2.ch.016 <chapt|
|/chapters/chapter05.md#net|pci.cfg.  | available in the host  |                 |                 |er04.md#kubernetes|
|work-resources>`__        |001       |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3 <../../../ref_model|infra.hw. | PCIe speed             | Gen 3           | Gen 3           |`ra2.ch.016 <chapt|
|/chapters/chapter05.md#net|pci.cfg.  |                        |                 |                 |er04.md#kubernetes|
|work-resources>`__        |002       |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3 <../../../ref_model|infra.hw. | PCIe Lanes             | 8               | 8               |`ra2.ch.016 <chapt|
|/chapters/chapter05.md#net|pci.cfg.  |                        |                 |                 |er04.md#kubernetes|
|work-resources>`__        |003       |                        |                 |                 |-node>`__         |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3 <../../../ref_model|infra.hw. | Cryptographic          | Not required    | Optional        | N/A              |
|/chapters/chapter05.md#net|nac.cfg.  | Acceleration           |                 |                 |                  |
|work-resources>`__        |001       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3 <../../../ref_model|infra.hw. | A SmartNIC that is     | Not required    | Optional (1)    | N/A              |
|/chapters/chapter05.md#net|nac.cfg.  | used to offload        |                 |                 |                  |
|work-resources>`__        |002       | vSwitch functionality  |                 |                 |                  |
|                          |          | to hardware            |                 |                 |                  | 
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+
|`5.4.3 <../../../ref_model|infra.hw. | Compression            | Optional        | Optional        | N/A              |
|/chapters/chapter05.md#net|nac.cfg.  |                        |                 |                 |                  |
|work-resources>`__        |003       |                        |                 |                 |                  |
+--------------------------+----------+------------------------+-----------------+-----------------+------------------+

**Table 2-4:** Reference Model Requirements: Cloud Infrastructure Hardware Profile Requirements

**(1)** There is no vSwitch in case of containers, but a SmartNIC can be used to offload any other network processing.

Cloud Infrastructure Management Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
| Reference Model Section          | Reference | Description                    | Requirement     | Specification     |
|                                  |           |                                | (common to all  | Reference         |
|                                  |           |                                | Profiles)       |                   |
+==================================+===========+================================+=================+===================+
|`4.1.5 <../../../ref_model01/chapt| e.man.001 | Capability to allocate virtual | Must support    | **N/A**           |
|ers/chapter04.md#cloud-infrastruct|           | compute resources to a         |                 |                   |
|ure-management-capabilities>`__   |           | workload                       |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5 <../../../ref_model/chapter| e.man.002 | Capability to allocate virtual | Must support    | **N/A**           |
|s/chapter04.md#cloud-infrastructur|           | storage resources to a         |                 |                   |
|e-management-capabilities>`__     |           | workload                       |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5 <../../../ref_model/chapter| e.man.003 | Capability to allocate virtual | Must support    | **N/A**           |
|s/chapter04.md#cloud-infrastructur|           | networking resources to a      |                 |                   |
|e-management-capabilities>`__     |           | workload                       |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5 <../../../ref_model/chapter| e.man.004 | Capability to isolate          | Must support    | **N/A**           |
|s/chapter04.md#cloud-infrastructur|           | resources between tenants      |                 |                   |
|e-management-capabilities>`__     |           |                                |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5 <../../../ref_model/chapter| e.man.005 | Capability to manage workload  | Must support    | **N/A**           |
|s/chapter04.md#cloud-infrastructur|           | software images                |                 |                   |
|e-management-capabilities>`__     |           |                                |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5 <../../../ref_model/chapter| e.man.006 | Capability to provide          | Must support    | **N/A**           |
|s/chapter04.md#cloud-infrastructur|           | information related to         |                 |                   |
|e-management-capabilities>`__     |           | allocated virtualised          |                 |                   |
|                                  |           | resources per tenant           |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5 <../../../ref_model/chapter| e.man.007 | Capability to notify state     | Must support    | **N/A**           |
|s/chapter04.md#cloud-infrastructur|           | changes of allocated resources |                 |                   |
|e-management-capabilities>`__     |           |                                |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5 <../../../ref_model/chapter| e.man.008 | Capability to collect and      | Must support    | **N/A**           |
|s/chapter04.md#cloud-infrastructur|           | expose performance information |                 |                   |
|e-management-capabilities>`__     |           | on virtualised resources       |                 |                   |
|                                  |           | allocated                      |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+
|`4.1.5 <../../../ref_model/chapter| e.man.009 | Capability to collect and      | Must support    | **N/A**           |
|s/chapter04.md#cloud-infrastructur|           | notify fault information on    |                 |                   |
|e-management-capabilities>`__     |           | virtualised resources          |                 |                   |
+----------------------------------+-----------+--------------------------------+-----------------+-------------------+

**Table 2-5:** Reference Model Requirements: Cloud Infrastructure Management Requirements

Cloud Infrastructure Security Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+-----------+--------------------------------------+-------------------------+
| Reference Model Section                | Reference | Description                          | Specification           |
|                                        |           |                                      | Reference               |
|                                        |           |                                      |                         |
+========================================+===========+======================================+=========================+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.001| The Platform **must** maintain the   |                         |
|ter07.md#system-hardening>`__           |           | specified configuration.             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.002| All systems part of Cloud            | `5.3.1 Node Hardening:  |
|ter07.md#system-hardening>`__           |           | Infrastructure **must** support      | Securing Kubernetes     |
|                                        |           | password hardening as defined in     | Hosts <./chapter05.md#n |
|                                        |           | `CIS Password Policy Guide <https:// | ode-hardening-securing- |
|                                        |           | www.cisecurity.org/white-papers/cis- | kubernetes-hosts>`__    |
|                                        |           | -policy-guide/>`__. Hardening: CIS   |                         |
|                                        |           | Password Policy Guide                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.003| All servers part of Cloud            |                         |
|ter07.md#system-hardening>`__           |           | Infrastructure **must** support a    |                         |
|                                        |           | root of trust and secure boot.       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.004| The Operating Systems of all the     | `5.2 Principles <./chap |
|ter07.md#system-hardening>`__           |           | servers part of Cloud Infrastructure | ter05.md#principles>`__ |
|                                        |           | **must** be hardened by removing or  | and `5.3 Node Hardening |
|                                        |           | disabling unnecessary services,      | <./chapter05.md#node-ha |
|                                        |           | applications and network protocols,  | rdening>`__             |
|                                        |           | configuring operating system user    |                         |
|                                        |           | authentication, configuring resource |                         |
|                                        |           | controls, installing and configuring |                         |
|                                        |           | additional security controls where   |                         |
|                                        |           | needed, and testing the security of  |                         |
|                                        |           | the Operating System.                |                         |
|                                        |           | (NIST SP 800-123)                    |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.005| The Platform **must** support        | `5.3 Node Hardening <./ |
|ter07.md#system-hardening>`__           |           | Operating System level access        | chapter05.md#node-harde |
|                                        |           | control                              | ning>`__                |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.006| The Platform **must** support Secure | `5.3.2 Restrict direct  |
|ter07.md#system-hardening>`__           |           | logging. Logging with root account   | access to nodes <./chap |
|                                        |           | must be prohibited when root         | ter05.md#restrict-direc |
|                                        |           | privileges are not required.         | t-access-to-nodes>`__   |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.007| All servers part of Cloud            |                         |
|ter07.md#system-hardening>`__           |           | Infrastructure **must** be Time      |                         |
|                                        |           | synchronized with authenticated Time |                         |
|                                        |           | service.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.008| All servers part of Cloud            | `5.3.3 Vulnerability as |
|ter07.md#system-hardening>`__           |           | Infrastructure **must** be regularly | sessment <./chapter05.m |
|                                        |           | updated to address security          | d#vulnerability-assessm |
|                                        |           | vulnerabilities.                     | ent>`__                 |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.009| The Platform **must** support        | `5.4 Securing           |
|ter07.md#system-hardening>`__           |           | Software integrity protection and    | Kubernetes orchestrator |
|                                        |           | verification and **must** scan       | <./chapter05.md#securin |
|                                        |           | source code and manifests.           | g-kubernetes-orchestrat |
|                                        |           |                                      | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.010| The Cloud Infrastructure **must**    |                         |
|ter07.md#system-hardening>`__           |           | support encrypted storage, for       |                         |
|                                        |           | example, block, object and file      |                         |
|                                        |           | storage, with access to encryption   |                         |
|                                        |           | keys restricted based on a need to   |                         |
|                                        |           | know. `Controlled Access Based on    |                         |
|                                        |           | the Need to Know <https://www.cisecu |                         |
|                                        |           | rity.org/controls/controlled-access- |                         |
|                                        |           | based-on-the-need-to-know/>`__       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.011| The Cloud Infrastructure **should**  |                         |
|ter07.md#system-hardening>`__           |           | support Read and Write only storage  |                         |
|                                        |           | partitions (write only permission to |                         |
|                                        |           | one or more authorized actors).      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.012| The Operator **must** ensure that    |                         |
|ter07.md#system-hardening>`__           |           | only authorized actors have physical |                         |
|                                        |           | access to the underlying             |                         |
|                                        |           | infrastructure.                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.013| The Platform **must** ensure that    | `5.4 Securing           |
|ter07.md#system-hardening>`__           |           | only authorized actors have logical  | Kubernetes orchestrator |
|                                        |           | access to the underlying             | <./chapter05.md#securin |
|                                        |           | infrastructure.                      | g-kubernetes-orchestrat |
|                                        |           |                                      | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.014| All servers part of Cloud            |                         |
|ter07.md#system-hardening>`__           |           | Infrastructure **should** support    |                         |
|                                        |           | measured boot and an attestation     |                         |
|                                        |           | server that monitors the             |                         |
|                                        |           | measurements of the servers.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.1 <../../../ref_model/chapters/chap|sec.gen.015| Any change to the Platform must be   |                         |
|ter07.md#system-hardening>`__           |           | logged as a security event, and the  |                         |
|                                        |           | logged event must include the        |                         |
|                                        |           | identity of the entity making the    |                         |
|                                        |           | change, the change, the date and the |                         |
|                                        |           | time of the change.                  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.001| The Platform **must** support        | `5.4 Securing           |
|ter07.md#platform-and-access>`__        |           | authenticated and secure access to   | Kubernetes orchestrator |
|                                        |           | API, GUI and command line            | <./chapter05.md#securin |
|                                        |           | interfaces.                          | g-kubernetes-orchestrat |
|                                        |           |                                      | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.002| The Platform **must** support        |                         |
|ter07.md#platform-and-access>`__        |           | Traffic Filtering for workloads (for |                         |
|                                        |           | example, Firewall).                  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.003| The Platform **must** support Secure | `5.4.3 Use Transport    |
|ter07.md#platform-and-access>`__        |           | and encrypted communications, and    | Layer Security and      |
|                                        |           | confidentiality and integrity of     | Service Mesh <./chapter |
|                                        |           | network traffic.                     | 05.md#use-transport-lay |
|                                        |           |                                      | er-security-and-service |
|                                        |           |                                      | -mesh>`__               |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.004| The Cloud Infrastructure **must**    | `5.4.3 Use Transport    |
|ter07.md#platform-and-access>`__        |           | support authentication, integrity    | Layer Security and      |
|                                        |           | and confidentiality on all network   | Service Mesh <./chapter |
|                                        |           | channels.                            | 05.md#use-transport-lay |
|                                        |           |                                      | er-security-and-service |
|                                        |           |                                      | -mesh>`__               |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.005| The Cloud Infrastructure **must**    |                         |
|ter07.md#platform-and-access>`__        |           | segregate the underlay and overlay   |                         |
|                                        |           | networks.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.006| The Cloud Infrastructure must be     | `5.2 Principles <./chap |
|ter07.md#platform-and-access>`__        |           | able to utilise the Cloud            | ter05.md#principles>`__ |
|                                        |           | Infrastructure Manager identity      |                         |
|                                        |           | lifecycle management capabilities.   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.007| The Platform **must** implement      | `5.2 Principles <./chap |
|ter07.md#platform-and-access>`__        |           | controls enforcing separation of     | ter05.md#principles>`__ |
|                                        |           | duties and privileges, least         | and                     |
|                                        |           | privilege use and least common       | `5.4 Securing           |
|                                        |           | mechanism (Role-Based Access         | Kubernetes orchestrator |
|                                        |           | Control).                            | <./chapter05.md#securin |
|                                        |           |                                      | g-kubernetes-orchestrat |
|                                        |           |                                      | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.008| The Platform **must** be able to     |                         |
|ter07.md#platform-and-access>`__        |           | assign the Entities that comprise    |                         |
|                                        |           | the tenant networks to different     |                         |
|                                        |           | trust domains. Communication between |                         |
|                                        |           | different trust domains is not       |                         |
|                                        |           | allowed, by default.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.009| The Platform **must** support        |                         |
|ter07.md#platform-and-access>`__        |           | creation of Trust Relationships      |                         |
|                                        |           | between trust domains.               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.010| For two or more domains without      |                         |
|ter07.md#platform-and-access>`__        |           | existing trust relationships, the    |                         |
|                                        |           | Platform **must not** allow the      |                         |
|                                        |           | effect of an attack on one domain to |                         |
|                                        |           | impact the other domains either      |                         |
|                                        |           | directly or indirectly.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.011| The Platform **must not** reuse the  |                         |
|ter07.md#platform-and-access>`__        |           | same authentication credential       |                         |
|                                        |           | (e.g., key-pair) on different        |                         |
|                                        |           | Platform components (e.g., on        |                         |
|                                        |           | different hosts, or different        |                         |
|                                        |           | services).                           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.012| The Platform **must** protect all    |                         |
|ter07.md#platform-and-access>`__        |           | secrets by using strong encryption   |                         |
|                                        |           | techniques, and storing the          |                         |
|                                        |           | protected secrets externally from    |                         |
|                                        |           | the component                        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.013| The Platform **must** provide        |                         |
|ter07.md#platform-and-access>`__        |           | secrets dynamically as and when      |                         |
|                                        |           | needed.                              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.014| The Platform **should** use Linux    |                         |
|ter07.md#platform-and-access>`__        |           | Security Modules such as SELinux to  |                         |
|                                        |           | control access to resources.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.015| The Platform **must not** contain    |                         |
|ter07.md#platform-and-access>`__        |           | back door entries (unpublished       |                         |
|                                        |           | access points, APIs, etc.).          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.016| Login access to the platform's       | `5.4 Securing           |
|ter07.md#platform-and-access>`__        |           | components **must** be through       | Kubernetes orchestrator |
|                                        |           | encrypted protocols such as SSH v2   | <./chapter05.md#securin |
|                                        |           | or TLS v1.2 or higher. Note:         | g-kubernetes-orchestrat |
|                                        |           | Hardened jump servers isolated from  | or>`__                  |
|                                        |           | external networks are recommended    |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.017| The Platform **must** provide the    |                         |
|ter07.md#platform-and-access>`__        |           | capability of using digital          |                         |
|                                        |           | certificates that comply with X.509  |                         |
|                                        |           | standards issued by a trusted        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.018| The Platform **must** provide the    |                         |
|ter07.md#platform-and-access>`__        |           | capability of allowing certificate   |                         |
|                                        |           | renewal and revocation.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.019| The Platform **must** provide the    |                         |
|ter07.md#platform-and-access>`__        |           | capability of testing the validity   |                         |
|                                        |           | of a digital certificate (CA         |                         |
|                                        |           | signature, validity period, non      |                         |
|                                        |           | revocation, identity).               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.2 <../../../ref_model/chapters/chap|sec.sys.020| The Cloud Infrastructure             |                         |
|ter07.md#platform-and-access>`__        |           | architecture **should** rely on Zero |                         |
|                                        |           | Trust principles to build a secure   |                         |
|                                        |           | by design environment.               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.001 | The Platform **must** support        | `5.4 Securing           |
| apter07.md#confidentiality-and-integri |           | Confidentiality and Integrity of     | Kubernetes orchestrator |
| ty>`__                                 |           | data at rest and in-transit.         | <./chapter05.md#securin |
|                                        |           | by design environment.               | g-kubernetes-orchestrat |
|                                        |           |                                      | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.002 | The Platform **should** support      |                         |
| apter07.md#confidentiality-and-integri |           | self-encrypting storage devices.     |                         |
| ty>`__                                 |           | data at rest and in-transit.         |                         |
|                                        |           | by design environment.               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.003 | The Platform **must** support        |                         |
| apter07.md#confidentiality-and-integri |           | Confidentiality and Integrity of     |                         |
| ty>`__                                 |           | data related metadata.               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.004 | The Platform **must** support        |                         |
| apter07.md#confidentiality-and-integri |           | Confidentiality of processes and     |                         |
| ty>`__                                 |           | restrict information sharing with    |                         |
|                                        |           | only the process owner (e.g.,        |                         |
|                                        |           | tenant).                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.005 | The Platform **must** support        |                         |
| apter07.md#confidentiality-and-integri |           | Confidentiality and Integrity of     |                         |
| ty>`__                                 |           | process-related metadata and         |                         |
|                                        |           | restrict information sharing with    |                         |
|                                        |           | only the process owner (e.g.,        |                         |
|                                        |           | tenant).                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.006 | The Platform **must** support        |                         |
| apter07.md#confidentiality-and-integri |           | Confidentiality and Integrity of     |                         |
| ty>`__                                 |           | workload resource utilization (RAM,  |                         |
|                                        |           | CPU, Storage, Network I/O, cache,    |                         |
|                                        |           | hardware offload) and restrict       |                         |
|                                        |           | information sharing with only the    |                         |
|                                        |           | workload owner (e.g., tenant).       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.007 | The Platform **must not** allow      |                         |
| apter07.md#confidentiality-and-integri |           | Memory Inspection by any actor other |                         |
| ty>`__                                 |           | than the authorized actors for the   |                         |
|                                        |           | Entity to which Memory is assigned   |                         |
|                                        |           | (e.g., tenants owning the workload), |                         |
|                                        |           | for Lawful Inspection, and by secure |                         |
|                                        |           | monitoring services.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.008 | The Cloud Infrastructure **must**    | `5.7 Create and define  |
| apter07.md#confidentiality-and-integri |           | support tenant networks segregation. | Network Policies        |
| ty>`__                                 |           |                                      | <./chapter05.md#create- |
|                                        |           |                                      | and-define-network-poli |
|                                        |           |                                      | cies>`__                |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.3 <../../../ref_model/chapters/ch |sec.ci.009 | For sensitive data encryption, the   |                         |
| apter07.md#confidentiality-and-integri |           | key management service **should**    |                         |
| ty>`__                                 |           | leverage a Hardware Security Module  |                         |
|                                        |           | to manage and protect cryptographic  |                         |
|                                        |           | keys.                                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4 <../../../ref_model/chapters/chap|sec.wl.001 | The Platform **must** support        |                         |
|ter07.md#workload-security>`__          |           | Workload placement policy.           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4 <../../../ref_model/chapters/chap|sec.wl.002 | The Cloud Infrastructure **must**    |                         |
|ter07.md#workload-security>`__          |           | provide methods to ensure the        |                         |
|                                        |           | platform’s trust status and          |                         |
|                                        |           | integrity (e.g. remote attestation,  |                         |
|                                        |           | Trusted Platform Module).            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4 <../../../ref_model/chapters/chap|sec.wl.003 | The Platform **must** support secure | `5.4 Securing           |
|ter07.md#workload-security>`__          |           | provisioning of workloads.           | Kubernetesorchestrator  |
|                                        |           |                                      | <./chapter05.md#securin |
|                                        |           |                                      | g-kubernetes-orchestrat |
|                                        |           |                                      | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4 <../../../ref_model/chapters/chap|sec.wl.004 | The Platform **must** support        |                         |
|ter07.md#workload-security>`__          |           | Location assertion (for mandated     |                         |
|                                        |           | in-country or location               |                         |
|                                        |           | requirements).                       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4 <../../../ref_model/chapters/chap|sec.wl.005 | The Platform **must** support the    | `5.4 Securing           |
|ter07.md#workload-security>`__          |           | separation of production and         | Kubernetes orchestrator |
|                                        |           | non-production Workloads.            | <./chapter05.md#securin |
|                                        |           |                                      | g-kubernetes-orchestrat |
|                                        |           |                                      | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4 <../../../ref_model/chapters/chap|sec.wl.006 | The Platform **must** support the    | `5.4 Securing           |
|ter07.md#workload-security>`__          |           | separation of Workloads based on     | Kubernetes orchestrator |
|                                        |           | their categorisation (for example,   | <./chapter05.md#securin |
|                                        |           | payment card information,            | g-kubernetes-orchestrat |
|                                        |           | healthcare, etc.).                   | or>`__ and `5.6Separate |
|                                        |           |                                      | Sensitive Workload <./c |
|                                        |           |                                      | hapter05.md#separate-se |
|                                        |           |                                      | nsitive-workload>`__    |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.4 <../../../ref_model/chapters/chap|sec.wl.007 | The Operator **must** implement      | `5.13 Trusted Registry  |
|ter07.md#workload-security>`__          |           | processes and tools to verify VNF    | <./chapter05.md#trusted |
|                                        |           | authenticity and integrity.          | -registry>`__           |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.001| Images from untrusted sources **must | `5.13 Trusted Registry  |
|ter07.md#image-security>`__             |           | not** be used.                       | <./chapter05.md#trusted |
|                                        |           |                                      | -registry>`__           |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.002| Images **must** be scanned to be     | `5.13 Trusted Registry  |
|ter07.md#image-security>`__             |           | maintained free from known           | <./chapter05.md#trusted |
|                                        |           | vulnerabilities.                     | -registry>`__           |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.003| Images **must not** be configured to | `5.11 Run-Time Security |
|ter07.md#image-security>`__             |           | run with privileges higher than the  | <./chapter05.md#run-tim |
|                                        |           | privileges of the actor authorized   | e-security>`__          |
|                                        |           | to run them.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.004| Images **must** only be accessible   |                         |
|ter07.md#image-security>`__             |           | to authorized actors.                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.005| Image Registries **must** only be    |                         |
|ter07.md#image-security>`__             |           | accessible to authorized actors.     |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.006| Image Registries **must** only be    | `5.13 Trusted Registry  |
|ter07.md#image-security>`__             |           | accessible over secure networks that | <./chapter05.md#trusted |
|                                        |           | enforce authentication, integrity    | -registry>`__           |
|                                        |           | and confidentiality.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.007| Image registries **must** be clear   | `5.13 Trusted Registry  |
|ter07.md#image-security>`__             |           | of vulnerable and out of date        | <./chapter05.md#trusted |
|                                        |           | versions.                            | -registry>`__           |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.008| Images **must not** include any      | `5.12 Secrets Management|
|ter07.md#image-security>`__             |           | secrets. Secrets include passwords,  | <./chapter05.md#secrets |
|                                        |           | cloud provider credentials, SSH      | -management>`__         |
|                                        |           | keys, TLS certificate keys, etc.     |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.009| CIS Hardened Images **should** be    |                         |
|ter07.md#image-security>`__             |           | used whenever possible.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.5 <../../../ref_model/chapters/chap|sec.img.010| Minimalist base images **should** be |                         |
|ter07.md#image-security>`__             |           | used whenever possible.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.001| The Platform **must** support Secure |                         |
|ter07.md#security-lcm>`__               |           | Provisioning, Availability, and      |                         |
|                                        |           | Deprovisioning (Secure Clean-Up) of  |                         |
|                                        |           | workload resources where Secure      |                         |
|                                        |           | Clean-Up includes tear-down, defense |                         |
|                                        |           | against virus or other attacks.      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.002| Cloud operations staff and systems   | `5.4 Securing           |
|ter07.md#security-lcm>`__               |           | **must** use management protocols    | Kubernetes orchestrator |
|                                        |           | limiting security risk such as       | <./chapter05.md#securin |
|                                        |           | SNMPv3, SSH v2, ICMP, NTP, syslog    | g-kubernetes-orchestrat |
|                                        |           | and TLS v1.2 or higher.              | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.003| The Cloud Operator **must**          |                         |
|ter07.md#security-lcm>`__               |           | implement and strictly follow change |                         |
|                                        |           | management processes for Cloud       |                         |
|                                        |           | Infrastructure, Cloud Infrastructure |                         |
|                                        |           | Manager and other components of the  |                         |
|                                        |           | cloud, and Platform change control   |                         |
|                                        |           | on hardware.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.004| The Cloud Operator **should**        |                         |
|ter07.md#security-lcm>`__               |           | support automated templated approved |                         |
|                                        |           | changes.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.005| Platform **must** provide logs and   | `5.10 Enable Logging    |
|ter07.md#security-lcm>`__               |           | these logs must be regularly         | and Monitoring <./chapt |
|                                        |           | monitored for anomalous behavior.    | er05.md#enable-logging- |
|                                        |           |                                      | and-monitoring>`__      |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.006| The Platform **must** verify the     |                         |
|ter07.md#security-lcm>`__               |           | integrity of all Resource management |                         |
|                                        |           | requests.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.007| The Platform **must** be able to     | `5.4 Securing           |
|ter07.md#security-lcm>`__               |           | update newly instantiated,           | Kubernetes orchestrator |
|                                        |           | suspended, hibernated, migrated and  | <./chapter05.md#securin |
|                                        |           | restarted images with current time   | g-kubernetes-orchestrat |
|                                        |           | information.                         | or>`__                  |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.008| The Platform **must** be able to     |                         |
|ter07.md#security-lcm>`__               |           | update newly instantiated,           |                         |
|                                        |           | suspended, hibernated, migrated and  |                         |
|                                        |           | restarted images with relevant DNS   |                         |
|                                        |           | information.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.009| The Platform **must** be able to     |                         |
|ter07.md#security-lcm>`__               |           | update the tag of newly              |                         |
|                                        |           | instantiated, suspended,             |                         |
|                                        |           | hibernated, migrated and restarted   |                         |
|                                        |           | images with relevant geolocation     |                         |
|                                        |           | (geographical) information.          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.010| The Platform **must** log all        |                         |
|ter07.md#security-lcm>`__               |           | changes to geolocation along with    |                         |
|                                        |           | the mechanisms and sources of        |                         |
|                                        |           | location information (i.e. GPS, IP   |                         |
|                                        |           | block, and timing).                  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.011| The Platform **must** implement      |                         |
|ter07.md#security-lcm>`__               |           | Security life cycle management       |                         |
|                                        |           | processes including the proactive    |                         |
|                                        |           | update and patching of all deployed  |                         |
|                                        |           | Cloud Infrastructure software.       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.6 <../../../ref_model/chapters/chap|sec.lcm.012| The Platform **must** log any access |                         |
|ter07.md#security-lcm>`__               |           | privilege escalation.                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.001| Platform **must** provide logs and   |                         |
| apter07.md#monitoring-and-security-aud |           | these logs must be regularly         |                         |
| it>`__                                 |           | monitored for events of interest.    |                         |
|                                        |           | The logs **must** contain the        |                         |
|                                        |           | following fields: event type,        |                         |
|                                        |           | date/time, protocol, service or      |                         |
|                                        |           | program used for access,             |                         |
|                                        |           | success/failure, login ID or process |                         |
|                                        |           | ID, IP address and ports (source     |                         |
|                                        |           | and destination) involved.           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.002| Security logs **must** be time       |                         |
| apter07.md#monitoring-and-security-aud |           | synchronised.                        |                         |
| it>`__                                 |           |                                      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.003| The Platform **must** log all        |                         |
| apter07.md#monitoring-and-security-aud |           | changes to time server source, time, |                         |
| it>`__                                 |           | date and time zones.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.004| The Platform **must** secure and     |                         |
| apter07.md#monitoring-and-security-aud |           | protect Audit logs (containing       |                         |
| it>`__                                 |           | sensitive information) both          |                         |
|                                        |           | in-transit and at rest.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.005| The Platform **must** Monitor and    |                         |
| apter07.md#monitoring-and-security-aud |           | Audit various behaviours of          |                         |
| it>`__                                 |           | connection and login attempts to     |                         |
|                                        |           | detect access attacks and potential  |                         |
|                                        |           | access attempts and take corrective  |                         |
|                                        |           | actions accordingly.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.006| The Platform **must** Monitor and    |                         |
| apter07.md#monitoring-and-security-aud |           | Audit operations by authorized       |                         |
| it>`__                                 |           | account access after login to detect |                         |
|                                        |           | malicious operational activity and   |                         |
|                                        |           | take corrective actions accordingly. |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.007| The Platform **must** Monitor and    |                         |
| apter07.md#monitoring-and-security-aud |           | Audit security parameter             |                         |
| it>`__                                 |           | configurations for compliance with   |                         |
|                                        |           | defined security policies.           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.008| The Platform **must** Monitor and    |                         |
| apter07.md#monitoring-and-security-aud |           | Audit externally exposed interfaces  |                         |
| it>`__                                 |           | for illegal access (attacks) and     |                         |
|                                        |           | take corrective security hardening   |                         |
|                                        |           | measures.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.009| The Platform **must** Monitor and    |                         |
| apter07.md#monitoring-and-security-aud |           | Audit service handling for various   |                         |
| it>`__                                 |           | attacks (malformed messages,         |                         |
|                                        |           | signalling flooding and replaying,   |                         |
|                                        |           | etc.) and take corrective actions    |                         |
|                                        |           | accordingly.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.010| The Platform **must** Monitor and    |                         |
| apter07.md#monitoring-and-security-aud |           | Audit running processes to detect    |                         |
| it>`__                                 |           | unexpected or unauthorized processes |                         |
|                                        |           | and take corrective actions          |                         |
|                                        |           | accordingly.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.011| The Platform **must** Monitor and    |                         |
| apter07.md#monitoring-and-security-aud |           | Audit logs from infrastructure       |                         |
| it>`__                                 |           | elements and workloads to detected   |                         |
|                                        |           | anomalies in the system components   |                         |
|                                        |           | and take corrective actions          |                         |
|                                        |           | accordingly.                         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.012| The Platform **must** Monitor and    |                         |
| apter07.md#monitoring-and-security-aud |           | Audit Traffic patterns and volumes   |                         |
| it>`__                                 |           | to prevent malware download          |                         |
|                                        |           | attempts.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.013| The monitoring system **must not**   |                         |
| apter07.md#monitoring-and-security-aud |           | affect the security (integrity and   |                         |
| it>`__                                 |           | confidentiality) of the              |                         |
|                                        |           | infrastructure, workloads, or the    |                         |
|                                        |           | user data (through back door         |                         |
|                                        |           | entries).                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.014| The Monitoring systems **should      |                         |
| apter07.md#monitoring-and-security-aud |           | not** impact IAAS, PAAS, and SAAS    |                         |
| it>`__                                 |           | SLAs including availability SLAs.    |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.015| The Platform **must** ensure that    |                         |
| apter07.md#monitoring-and-security-aud |           | the Monitoring systems are never     |                         |
| it>`__                                 |           | starved of resources and **must**    |                         |
|                                        |           | activate alarms when resource        |                         |
|                                        |           | utilisation exceeds a configurable   |                         |
|                                        |           | threshold.                           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.016| The Platform Monitoring components   |                         |
| apter07.md#monitoring-and-security-aud |           | **should** follow security best      |                         |
| it>`__                                 |           | practices for auditing, including    |                         |
|                                        |           | secure logging and tracing.          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.017| The Platform **must** audit systems  | `5.3.3 Vulnerability    |
| apter07.md#monitoring-and-security-aud |           | for any missing security patches and | assessment <./chapter05 |
| it>`__                                 |           | take appropriate actions.            | .md#vulnerability-asses |
|                                        |           |                                      | sment>`__               |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.018| The Platform, starting from          | `5.3.4 Patch management |
| apter07.md#monitoring-and-security-aud |           | initialization, **must** collect and | <./chapter05.md#patch-m |
| it>`__                                 |           | analyze logs to identify security    | anagement>`__           |
|                                        |           | events, and store these events in an |                         |
|                                        |           | external system.                     |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.019| The Platform’s components **must     |                         |
| apter07.md#monitoring-and-security-aud |           | not** include an authentication      |                         |
| it>`__                                 |           | credential, e.g., password, in any   |                         |
|                                        |           | logs, even if encrypted.             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.020| The Platform’s logging system        |                         |
| apter07.md#monitoring-and-security-aud |           | **must** support the storage of      |                         |
| it>`__                                 |           | security audit logs for a            |                         |
|                                        |           | configurable period of time.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
| `7.9.7 <../../../ref_model/chapters/ch |sec.mon.021| The Platform **must** store security |                         |
| apter07.md#monitoring-and-security-aud |           | events locally if the external       |                         |
| it>`__                                 |           | logging system is unavailable and    |                         |
|                                        |           | shall periodically attempt to send   |                         |
|                                        |           | these to the external logging system |                         |
|                                        |           | until successful.                    |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8 <../../../ref_model/chapters/chap|sec.oss.001| Open source code **must** be         | `5.3.3 Vulnerability    |
|ter07.md#open-source-software>`__       |           | inspected by tools with various      | assessment <./chapter05 |
|                                        |           | capabilities for static and dynamic  | .md#vulnerability-asses |
|                                        |           | code analysis.                       | sment>`__               |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8 <../../../ref_model/chapters/chap|sec.oss.002| The `CVE (Common Vulnerabilities     |                         |
|ter07.md#open-source-software>`__       |           | and Exposures) <https://cve.mitre.or |                         |
|                                        |           | g/>`__ **must** be used to identify  |                         |
|                                        |           | vulnerabilities and their severity   |                         |
|                                        |           | rating for open source code part of  |                         |
|                                        |           | Cloud Infrastructure and workloads   |                         |
|                                        |           | software.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8 <../../../ref_model/chapters/chap|sec.oss.003| Critical and high severity rated     |                         |
|ter07.md#open-source-software>`__       |           | vulnerabilities **must** be fixed in |                         |
|                                        |           | a timely manner. Refer to the `CVSS  |                         |
|                                        |           | (Common Vulnerability Scoring System)|                         |
|                                        |           | <https://www.first.org/cvss/>`__ to  |                         |
|                                        |           | know a vulnerability score and its   |                         |
|                                        |           | associated rate (low, medium, high,  |                         |
|                                        |           | or critical).                        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8 <../../../ref_model/chapters/chap|sec.oss.004| A dedicated internal isolated        | `5.13 Trusted Registry  |
|ter07.md#open-source-software>`__       |           | repository separated from the        | <./chapter05.md#trusted |
|                                        |           | production environment **must** be   | -registry>`__           |
|                                        |           | used to store vetted open source     |                         |
|                                        |           | content.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.8 <../../../ref_model/chapters/chap|sec.oss.005| A Software Bill of Materials (`SBOM  |                         |
|ter07.md#open-source-software>`__       |           | <https://www.ntia.gov/SBOM>`__)      |                         |
|                                        |           | **should** be provided or build, and |                         |
|                                        |           | maintained to identify the software  |                         |
|                                        |           | components and their origins.        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.9 <../../../ref_model/chapters/chap|sec.arch.00| Threat Modelling methodologies and   |                         |
|ter07.md#iaac---secure-design-and-archit|1          | tools **should** be used during the  |                         |
|ecture-stage-requirements>`__           |           | Secure Design and Architecture stage |                         |
|                                        |           | triggered by Software Feature Design |                         |
|                                        |           | trigger. It may be done manually or  |                         |
|                                        |           | using tools like open source OWASP   |                         |
|                                        |           | Threat Dragon                        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.9 <../../../ref_model/chapters/chap|sec.arch.00| Security Control Baseline Assessment |                         |
|ter07.md#iaac---secure-design-and-archit|2          | **should** be performed during the   |                         |
|ecture-stage-requirements>`__           |           | Secure Design and Architecture stage |                         |
|                                        |           | triggered by Software Feature Design |                         |
|                                        |           | trigger. Typically done manually by  |                         |
|                                        |           | internal or independent assessors.   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10 <../../../ref_model/chapters/cha|sec.code.00| SAST -Static Application Security    |                         |
|pter07.md#iaac---secure-code-stage-requi|1          | Testing **must** be applied during   |                         |
|rements>`__                             |           | Secure Coding stage triggered by     |                         |
|                                        |           | Pull, Clone or Comment trigger.      |                         |
|                                        |           | Security testing that analyses       |                         |
|                                        |           | application source code for software |                         |
|                                        |           | vulnerabilities and gaps against     |                         |
|                                        |           | best practices. Example: open source |                         |
|                                        |           | OWASP range of tools.                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10 <../../../ref_model/chapters/cha|sec.code.00| SCA – Software Composition Analysis  |                         |
|pter07.md#iaac---secure-code-stage-requi|2          | **should** be applied during Secure  |                         |
|rements>`__                             |           | Coding stage triggered by Pull,      |                         |
|                                        |           | Clone or Comment trigger. Security   |                         |
|                                        |           | testing that analyses application    |                         |
|                                        |           | source code or compiled code for     |                         |
|                                        |           | software components with known       |                         |
|                                        |           | vulnerabilities. Example: open       |                         |
|                                        |           | source OWASP range of tools.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10 <../../../ref_model/chapters/cha|sec.code.00| Source Code Review **should** be     |                         |
|pter07.md#iaac---secure-code-stage-requi|3          | performed continuously during Secure |                         |
|rements>`__                             |           | Coding stage. Typically done         |                         |
|                                        |           | manually.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10 <../../../ref_model/chapters/cha|sec.code.00| Integrated SAST via IDE Plugins      |                         |
|pter07.md#iaac---secure-code-stage-requi|4          | **should** be used during Secure     |                         |
|rements>`__                             |           | Coding stage triggered by Developer  |                         |
|                                        |           | Code trigger. On the local machine:  |                         |
|                                        |           | through the IDE or integrated test   |                         |
|                                        |           | suites; triggered on completion of   |                         |
|                                        |           | coding be developer.                 |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.10 <../../../ref_model/chapters/cha|sec.code.00| SAST of Source Code Repo **should**  |                         |
|pter07.md#iaac---secure-code-stage-requi|5          | be performed during Secure Coding    |                         |
|rements>`__                             |           | stage triggered by Developer Code    |                         |
|                                        |           | trigger. Continuous delivery         |                         |
|                                        |           | pre-deployment: scanning prior to    |                         |
|                                        |           | deployment.                          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11 <../../../ref_model/chapters/cha|sec.bld.001| SAST -Static Application Security    |                         |
|pter07.md#iaac---continuous-build-integr|           | Testing **should** be applied during |                         |
|ation-and-testing-stage-requirements>`__|           | the Continuous Build, Integration    |                         |
|                                        |           | and Testing stage triggered by Build |                         |
|                                        |           | and Integrate trigger. Example: open |                         |
|                                        |           | source OWASP range of tools.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11 <../../../ref_model/chapters/cha|sec.bld.002| SCA – Software Composition Analysis  |                         |
|pter07.md#iaac---continuous-build-integr|           | **should** be applied during the     |                         |
|ation-and-testing-stage-requirements>`__|           | Continuous Build, Integration and    |                         |
|                                        |           | Testing stage triggered by Build and |                         |
|                                        |           | Integrate trigger. Example: open     |                         |
|                                        |           | source OWASP range of tools.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11 <../../../ref_model/chapters/cha|sec.bld.003| Image Scan **must** be applied       |                         |
|pter07.md#iaac---continuous-build-integr|           | during the Continuous Build,         |                         |
|ation-and-testing-stage-requirements>`__|           | Integration and Testing stage        |                         |
|                                        |           | triggered by Package trigger.        |                         |
|                                        |           | Example: A push of a container image |                         |
|                                        |           | to a container registry may trigger  |                         |
|                                        |           | a vulnerability scan before the      |                         |
|                                        |           | image becomes available in the       |                         |
|                                        |           | registry.                            |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11 <../../../ref_model/chapters/cha|sec.bld.004| DAST – Dynamic Application Security  |                         |
|pter07.md#iaac---continuous-build-integr|           | Testing **should** be applied during |                         |
|ation-and-testing-stage-requirements>`__|           | the Continuous Build, Integration    |                         |
|                                        |           | and Testing stage triggered by Stage |                         |
|                                        |           | & Test trigger. Security testing     |                         |
|                                        |           | that analyses a running application  |                         |
|                                        |           | by exercising application            |                         |
|                                        |           | functionality and detecting          |                         |
|                                        |           | vulnerabilities based on             |                         |
|                                        |           | application behaviour and response.  |                         |
|                                        |           | Example: OWASP ZAP.                  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11 <../../../ref_model/chapters/cha|sec.bld.005| Fuzzing **should** be applied during |                         |
|pter07.md#iaac---continuous-build-integr|           | the Continuous Build, Integration    |                         |
|ation-and-testing-stage-requirements>`__|           | and testing stage triggered by Stage |                         |
|                                        |           | & Test trigger. Fuzzing or fuzz      |                         |
|                                        |           | testing is an automated software     |                         |
|                                        |           | testing technique that involves      |                         |
|                                        |           | providing invalid, unexpected, or    |                         |
|                                        |           | random data as inputs to a computer  |                         |
|                                        |           | program. Example: GitLab Open        |                         |
|                                        |           | Sources Protocol Fuzzer Community    |                         |
|                                        |           | Edition.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.11 <../../../ref_model/chapters/cha|sec.bld.006| IAST – Interactive Application       |                         |
|pter07.md#iaac---continuous-build-integr|           | Security Testing **should** be       |                         |
|ation-and-testing-stage-requirements>`__|           | applied during the Continuous Build, |                         |
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
|`7.9.12 <../../../ref_model/chapters/cha|sec.del.001| Image Scan **must** be applied       |                         |
|pter07.md#iaac---continuous-delivery-and|           | during the Continuous Delivery and   |                         |
|-deployment-stage-requirements>`__      |           | Deployment stage triggered by        |                         |
|                                        |           | Publish to Artifact and Image        |                         |
|                                        |           | Repository trigger. Example: GitLab  |                         |
|                                        |           | uses the open-source Clair engine    |                         |
|                                        |           | for container image scanning.        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.12 <../../../ref_model/chapters/cha|sec.del.002| Code Signing **must** be applied     |                         |
|pter07.md#iaac---continuous-delivery-and|           | during the Continuous Delivery and   |                         |
|-deployment-stage-requirements>`__      |           | Deployment stage triggered by        |                         |
|                                        |           | Publish to Artifact and Image        |                         |
|                                        |           | Repository trigger. Code Signing     |                         |
|                                        |           | provides authentication to assure    |                         |
|                                        |           | that downloaded files are form the   |                         |
|                                        |           | publisher named on the certificate.  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.12 <../../../ref_model/chapters/cha|sec.del.003| Artifact and Image Repository Scan   |                         |
|pter07.md#iaac---continuous-delivery-and|           | **should** be continuously applied   |                         |
|-deployment-stage-requirements>`__      |           | during the Continuous Delivery and   |                         |
|                                        |           | Deployment stage. Example: GitLab    |                         |
|                                        |           | uses the open source Clair engine    |                         |
|                                        |           | for container scanning.              |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.12 <../../../ref_model/chapters/cha|sec.del.004| Component Vulnerability Scan         |                         |
|pter07.md#iaac---continuous-delivery-and|           | **must** be applied during the       |                         |
|-deployment-stage-requirements>`__      |           | Continuous Delivery and Deployment   |                         |
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
|`7.9.13 <../../../ref_model/chapters/cha|sec.run.001| Component Vulnerability Monitoring   |                         |
|pter07.md#iaac---runtime-defence-and-mon|           | **must** be continuously applied     |                         |
|itoring-requirements>`__                |           | during the Runtime Defence and       |                         |
|                                        |           | Monitoring stage and remediation     |                         |
|                                        |           | actions **must** be applied for high |                         |
|                                        |           | severity rated vulnerabilities.      |                         |
|                                        |           | Security technology that monitors    |                         |
|                                        |           | components like virtual servers and  |                         |
|                                        |           | assesses data, applications, and     |                         |
|                                        |           | infrastructure for security risks.   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.13 <../../../ref_model/chapters/cha|sec.run.002| RASP – Runtime Application Self-     |                         |
|pter07.md#iaac---runtime-defence-and-mon|           | Protection **should** be             |                         |
|itoring-requirements>`__                |           | continuously applied during the      |                         |
|                                        |           | Runtime Defence and Monitoring       |                         |
|                                        |           | stage. Security technology deployed  |                         |
|                                        |           | within the target application in     |                         |
|                                        |           | production for detecting, alerting,  |                         |
|                                        |           | and blocking attacks.                |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.13 <../../../ref_model/chapters/cha|sec.run.003| Application testing and Fuzzing      |                         |
|pter07.md#iaac---runtime-defence-and-mon|           | **should** be continuously applied   |                         |
|itoring-requirements>`__                |           | during the Runtime Defence and       |                         |
|                                        |           | Monitoring stage. Fuzzing or fuzz    |                         |
|                                        |           | testing is an automated software     |                         |
|                                        |           | testing technique that involves      |                         |
|                                        |           | providing invalid, unexpected, or    |                         |
|                                        |           | random data as inputs to a computer  |                         |
|                                        |           | program. Example: GitLab Open        |                         |
|                                        |           | Sources Protocol Fuzzer Community    |                         |
|                                        |           | Edition.                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.13 <../../../ref_model/chapters/cha|sec.run.004| Penetration Testing **should** be    |                         |
|pter07.md#iaac---runtime-defence-and-mon|           | continuously applied during the      |                         |
|itoring-requirements>`__                |           | Runtime Defence and Monitoring       |                         |
|                                        |           | stage. Typically done manually.      |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.001| The Cloud Operator **should** comply |                         |
|pter07.md#compliance-with-standards>`__ |           | with Center for Internet Security    |                         |
|                                        |           | CIS Controls (`https://www.cisecur   |                         |
|                                        |           | ity.org/ <https://www.cisecurity.org |                         |
|                                        |           | />`__)                               |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.002| The Cloud Operator, Platform and     |                         |
|pter07.md#compliance-with-standards>`__ |           | Workloads **should** follow the      |                         |
|                                        |           | guidance in the CSA Security         |                         |
|                                        |           | Guidance for Critical Areas of Focus |                         |
|                                        |           | in Cloud Computing (latest version)  |                         |
|                                        |           | `https://cloudsecurityalliance.      |                         |
|                                        |           | org/ <https://cloudsecurityalliance. |                         |
|                                        |           | org/>`__                             |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.003| The Platform and Workloads           |                         |
|pter07.md#compliance-with-standards>`__ |           | **should** follow the guidance in    |                         |
|                                        |           | the `OWASP Cheat Sheet Series (OCSS) |                         |
|                                        |           | <https://github.com/OWASP/CheatSheet |                         |
|                                        |           | Series>`__                           |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.004| The Cloud Operator, Platform and     |                         |
|pter07.md#compliance-with-standards>`__ |           | Workloads **should** ensure that     |                         |
|                                        |           | their code is not vulnerable to the  |                         |
|                                        |           | OWASP Top Ten Security Risks         |                         |
|                                        |           | `https://owasp.org/www-project-top-t |                         |
|                                        |           | en/ <https://owasp.org/www-project-t |                         |
|                                        |           | op-ten/>`__                          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.005| The Cloud Operator, Platform and     |                         |
|pter07.md#compliance-with-standards>`__ |           | Workloads **should** strive to       |                         |
|                                        |           | improve their maturity on the `OWASP |                         |
|                                        |           | Software Maturity Model (SAMM) <http |                         |
|                                        |           | s://owaspsamm.org/blog/2019/12/20/ve |                         |
|                                        |           | rsion2-community-release/>`__        |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.006| The Cloud Operator, Platform and     |                         |
|pter07.md#compliance-with-standards>`__ |           | Workloads **should** utilize the `OW |                         |
|                                        |           | ASP Web Security Testing Guide <http |                         |
|                                        |           | s://github.com/OWASP/wstg/tree/maste |                         |
|                                        |           | r/document>`__                       |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.007| The Cloud Operator, and Platform     |                         |
|pter07.md#compliance-with-standards>`__ |           | **should** satisfy the requirements  |                         |
|                                        |           | for Information Management Systems   |                         |
|                                        |           | specified in `ISO/IEC 27001 <https:/ |                         |
|                                        |           | /www.iso.org/obp/ui/#iso:std:iso-iec |                         |
|                                        |           | :27001:ed-2:v1:en>`__. ISO/IEC       |                         |
|                                        |           | 27002:2013 - ISO/IEC 27001 is the    |                         |
|                                        |           | international Standard for           |                         |
|                                        |           | best-practice information security   |                         |
|                                        |           | management systems (ISMSs).          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.008| The Cloud Operator, and Platform     |                         |
|pter07.md#compliance-with-standards>`__ |           | **should** implement the Code of     |                         |
|                                        |           | practice for Security Controls       |                         |
|                                        |           | specified `ISO/IEC 27002:2013 (or la |                         |
|                                        |           | test) <https://www.iso.org/obp/ui/#i |                         |
|                                        |           | so:std:iso-iec:27002:ed-2:v1:en>`__  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.009| The Cloud Operator, and Platform     |                         |
|pter07.md#compliance-with-standards>`__ |           | **should** implement the `ISO/IEC 27 |                         |
|                                        |           | 032:2012 (or latest) <https://www.is |                         |
|                                        |           | o.org/obp/ui/#iso:std:iso-iec:27032: |                         |
|                                        |           | ed-1:v1:en>`__ Guidelines for        |                         |
|                                        |           | Cybersecurity techniques. ISO/IEC    |                         |
|                                        |           | 27032 - ISO/IEC 27032 is the         |                         |
|                                        |           | international Standard focusing      |                         |
|                                        |           | explicitly on cybersecurity.         |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.010| The Cloud Operator **should**        |                         |
|pter07.md#compliance-with-standards>`__ |           | conform to the ISO/IEC 27035         |                         |
|                                        |           | standard for incidence management.   |                         |
|                                        |           | ISO/IEC 27035 - ISO/IEC 27035 is the |                         |
|                                        |           | international Standard for incident  |                         |
|                                        |           | management.                          |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.011| The Cloud Operator **should**        |                         |
|pter07.md#compliance-with-standards>`__ |           | conform to the ISO/IEC 27031         |                         |
|                                        |           | standard for business continuity.    |                         |
|                                        |           | ISO/IEC 27031 - ISO/IEC 27031 is the |                         |
|                                        |           | international Standard for ICT       |                         |
|                                        |           | readiness for business continuity.   |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+
|`7.9.14 <../../../ref_model/chapters/cha|sec.std.012| The Public Cloud Operator **must**,  |                         |
|pter07.md#compliance-with-standards>`__ |           | and the Private Cloud Operator       |                         |
|                                        |           | **may** be certified to be compliant |                         |
|                                        |           | with the International Standard on   |                         |
|                                        |           | Awareness Engagements (ISAE) 3402    |                         |
|                                        |           | (in the US: SSAE 16). International  |                         |
|                                        |           | Standard on Awareness Engagements    |                         |
|                                        |           | (ISAE) 3402. US Equivalent: SSAE16.  |                         |
+----------------------------------------+-----------+--------------------------------------+-------------------------+

**Table 2-6:** Reference Model Requirements: Cloud Infrastructure Security Requirements

Kubernetes Architecture Requirements
------------------------------------

The requirements in this section are to be delivered in addition to those in `section 2.2 <#2.2>`__, and have been
created to support the Principles defined in `Chapter 1 of this Reference Architecture <./chapter01.md>`__.

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
|gen.cnt.02| General      | Cloud        | The Architecture **must** support    | `ra2.ch.017 <chapter04.md#kubernete |
|          |              | nativeness   | immutable infrastructure.            | s-node>`__                          |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.cnt.03| General      | Cloud        | The Architecture **must** run        | `ra2.k8s.001 <chapter04.md#kubernet |
|          |              | nativeness   | conformant Kubernetes as defined by  | es>`__                              |
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
|gen.rsl.01| General      | Resiliency   | The Architecture **must** support    | `ra2.k8s.004 <chapter04.md#kubernet |
|          |              |              | resilient Kubernetes components that | es>`__                              |
|          |              |              | are required for the continued       |                                     |
|          |              |              | availability of running workloads.   |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.rsl.02| General      | Resiliency   | The Architecture **should** support  | `ra2.k8s.002 <chapter04.md#kubernet |
|          |              |              | resilient Kubernetes service         | es>`__, `ra2.k8s.003 <chapter04.md# |
|          |              |              | components that are not subject to   | kubernetes>`__                      |
|          |              |              | gen.rsl.01.                          |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.avl.01| General      | Availability | The Architecture **must** provide    | `ra2.k8s.002 <chapter04.md#kubernet |
|          |              |              | High Availability for Kubernetes     | es>`__, `ra2.k8s.003 <chapter04.md# |
|          |              |              | components.                          | kubernetes>`__, `ra2.k8s.004 <chapt |
|          |              |              |                                      | er04.md#kubernetes>`__              |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|gen.ost.01| Openness     | Availability | The Architecture **should** embrace  | `ra2.crt.001 <chapter04.md#containe |
|          |              |              | open-based standards and             | r-runtimes>`__, `ra2.crt.002 <chapt |
|          |              |              | technologies.                        | er04.md#container-runtimes>`__, `ra |
|          |              |              |                                      | 2.ntw.002 <chapter04.md#networking- |
|          |              |              |                                      | solutions>`__, `ra2.ntw.006 <chapte |
|          |              |              |                                      | r04.md#networking-solutions>`__,    |
|          |              |              |                                      | `ra2.ntw.007 <chapter04.md#networki |
|          |              |              |                                      | ng-solutions>`__                    | 
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.com.01|Infrastructure| Compute      | The Architecture **must** provide    | `ra2.k8s.004 <chapter04.md#kubernet |
|          |              |              | compute resources for Pods.          | es>`__                              |
|          |              |              | technologies.                        |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.stg.01|Infrastructure| Storage      | The Architecture **must** support    | `ra2.stg.004 <chapter04.md#storage- |
|          |              |              | the ability for an operator to       | components>`__                      |
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
|inf.ntw.03|Infrastructure| Network      | The networking solution **should**   | `ra2.ntw.001 <chapter04.md#networki |
|          |              |              | be able to be centrally              | ng-solutions>`__, `ra2.ntw.004 <cha |
|          |              |              | administrated and configured.        | pter04.md#networking-solutions>`__  |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.04|Infrastructure| Network      | The Architecture **must** support    | `ra2.ch.007 <chapter04.md#kubernete |
|          |              |              | dual stack IPv4 and IPv6 for         | s-node>`__, `ra2.k8s.010 <chapter04 |
|          |              |              | Kubernetes workloads.                | .md#kubernetes>`__                  |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.05|Infrastructure| Network      | The Architecture **must** support    |                                     |
|          |              |              | capabilities for integrating SDN     |                                     |
|          |              |              | controllers.                         |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.06|Infrastructure| Network      | The Architecture **must** support    | `ra2.ntw.005 <chapter04.md#networki |
|          |              |              | more than one networking solution.   | ng-solutions>`__, `ra2.ntw.007 <cha |
|          |              |              |                                      | pter04.md#networking-solutions>`__  |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.07|Infrastructure| Network      | The Architecture **must** support    | `ra2.ntw.005 <chapter04.md#networki |
|          |              |              | the ability for an operator to       | ng-solutions>`__                    |
|          |              |              | choose whether or not to deploy more |                                     |
|          |              |              | than one networking solution.        |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.ntw.08|Infrastructure| Network      | The Architecture **must** provide a  | `ra2.ntw.002 <chapter04.md#networki |
|          |              |              | default network which implements the | ng-solutions>`__                    |
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
|inf.ntw.14|Infrastructure| Network      | The platform **must** allow NATless  |                                     |
|          |              |              | traffic (i.e. exposing the pod IP    |                                     |
|          |              |              | address directly to the outside),    |                                     |
|          |              |              | allowing source and destination IP   |                                     |
|          |              |              | addresses to be preserved in the     |                                     |
|          |              |              | traffic headers from workloads to    |                                     |
|          |              |              | external networks. This is needed    |                                     |
|          |              |              | e.g. for signaling applications,     |                                     |
|          |              |              | using SIP and Diameter protocols.    |                                     |
|          |              |              | `ra2.ntw.011 <chapter04.md#networkin |                                     |
|          |              |              | g-solutions>`__                      |                                     |
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
|inf.vir.01|Infrastructure| Virtual Infr | The Architecture **must** support    | `ra2.ch.005 <chapter04.md#kubernete |
|          |              | astructure   | the capability for Containers to     | s-node>`__, `ra2.ch.011 <chapter04. |
|          |              |              | consume infrastructure resources     | md#kubernetes-node>`__              |
|          |              |              | abstracted by Host Operating Systems |                                     |
|          |              |              | that are running within a virtual    |                                     |
|          |              |              | machine.                             |                                     |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|inf.phy.01|Infrastructure| Physical     | The Architecture **must** support    | ra2.ch.008                          |
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
|kcm.gen.02| Kubernetes   | General      | The Architecture **must** enable     | `ra2.k8s.004 <chapter04.md#kubernet |
|          | Cluster      |              | workload resiliency.                 | es>`__                              |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|int.api.01| API          | General      | The Architecture **must** leverage   | For Networking: `ra2.ntw.001 <chapt |
|          |              |              | the Kubernetes APIs to discover and  | er04.md#networking-solutions>`__,   |
|          |              |              | declaratively manage compute         | `ra2.ntw.008 <chapter04.md#networki |
|          |              |              | (virtual and bare metal resources),  | ng-solutions>`__, `ra2.app.006 <cha |
|          |              |              | network, and storage.                | pter04.md#kubernetes-workloads>`__  |
|          |              |              |                                      | Compute/storage not yet met.        |
+----------+--------------+--------------+--------------------------------------+-------------------------------------+
|int.api.02| API          | General      | The Architecture **must** support    | `ra2.pkg.001 <chapter04.md#kubernet |
|          |              |              | the usage of a Kubernetes            | es-application-package-manager>`__  |
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
  
**Table 2-7:** Kubernetes Architecture Requirements
