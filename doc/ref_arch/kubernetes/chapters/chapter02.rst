Architecture Requirements
=========================

Introduction
------------

This chapter will use the requirements defined in the overall Reference Model and only make additional entries in
section `Kubernetes Architecture Requirements <#kubernetes-architecture-requirements>`__ if there are additional
requirements needed for this Reference Architecture.

Definitions
-----------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in `RFC2119 <https://www.ietf.org/rfc/rfc2119.txt>`__.

Reference Model Requirements
----------------------------

The tables below contain the requirements from the Reference Model to cover the Basic and High-Performance profiles.
The table also includes a reference to the specification from
:ref:`chapters/chapter04:component level architecture` and from
:ref:`chapters/chapter05:security guidance` to ensure traceability. If the related Specification
does not exist, the reference will read "N/A" (and in bold "**N/A**" for mandatory requirements).

To ensure alignment with the infrastructure profile catalogue, the following requirements are referenced through:

-  Those relating to Cloud Infrastructure Software Profiles
-  Those relating to Cloud Infrastructure Hardware Profiles
-  Those relating to Cloud Infrastructure Management
-  Those relating to Cloud Infrastructure Security

Cloud Infrastructure Software Profile Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Reference Model Requirements: Cloud Infrastructure Software Profile Capabilities
   :widths: 10 10 50 10 10 10
   :header-rows: 1

   * - Reference Model Section
     - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.001
     - Max number of vCPU that can be assigned to a single Pod by the Cloud Infrastructure
     - At least 16
     - At least 16
     - ra2.ch.011
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.002
     - Max memory in MB that can be assigned to a single Pod by the Cloud Infrastructure
     - at least 32 GB
     - at least 32 GB
     - ra2.ch.012
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.003
     - Max storage in GB that can be assigned to a single Pod by the Cloud Infrastructure
     - at least 320 GB
     - at least 320 GB
     - ra2.ch.010
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.004
     - Max number of connection points that can be assigned to a single Pod by the Cloud Infrastructure
     - 6
     - 6
     - ra2.ntw.003
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.005
     - Max storage in GB that can be attached / mounted to Pod by the Cloud Infrastructure
     - Up to 16TB (1)
     - Up to 16TB (1)
     - N/A
   * - :ref:`ref_model:chapters/chapter04:profiles specifications & capability mapping`
     - e.cap.006
     - CPU pinning support
     - Not required
     - Must support
     - ra2.k8s.009
   * - :ref:`ref_model:chapters/chapter04:profiles specifications & capability mapping`
     - e.cap.007
     - NUMA support
     - Not required
     - Must support
     - ra2.k8s.006
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.008
     - IPSec Acceleration using the virtio-ipsec interface
     - Not required
     - Optional
     - N/A
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.009
     - Crypto Acceleration using the virtio-crypto interface
     - Not required
     - Optional
     - N/A
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.010
     - Transcoding Acceleration
     - Not required
     - Not required
     - N/A
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.011
     - Programmable Acceleration
     - Not required
     - Not required
     - N/A
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.012
     - Enhanced Cache Management: L=Lean; E=Equal; X=eXpanded
     - E
     - E
     - N/A
   * - :ref:`ref_model:chapters/chapter04:profiles specifications & capability mapping`
     - e.cap.013
     - SR-IOV over PCI-PT
     - Not required
     - Must support
     - ra2.ch.002 ra2.ch.003 ra2.k8s.007 ra2.ntw.004 ra2.ntw.008
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.014
     - Hardware coprocessor support (GPU/NPU)
     - Not required
     - Not required
     - N/A
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.015
     - SmartNICs
     - Not required
     - Optional
     - N/A
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.016
     - FPGA/other Acceleration H/W
     - Not required
     - Optional
     - ra2.k8s.007 ra2.ntw.012
   * - :ref:`ref_model:chapters/chapter04:exposed infrastructure capabilities`
     - e.cap.017
     - Ability to monitor L2-L7 data from workload
     - n/a (2)
     - *n/a (2)*
     - N/A
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.cap.014
     - Specifies the proportion of CPU cores consumed by the Cloud Infrastructure system on the
       worker nodes. If SMT is used, it indicates the number of consumed SMT threads.
     - 2
     - 2
     - ra2.k8s.008
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.cap.015
     - Indicates the memory consumed by Cloud Infrastructure on the worker nodes
     - 16 GB
     - 16 GB
     -
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.cap.016
     - Number of virtual cores per physical core; also known as CPU overbooking ratio that is required
     - 01:01
     - 01:01
     - ra2.ch.004 :ref:`ra2.ch.005 <chapters/chapter04:Kubernetes Node>`
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.cap.017
     - QoS enablement of the connection point (vNIC or interface)
     - Not required
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.cap.018
     - Support for huge pages
     - Not required
     - Must support
     - ra2.ch.001
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.pm.001
     - Monitor worker node CPU usage, per nanosecond
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.pm.002
     - Monitor pod CPU usage, per nanosecond
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.pm.003
     - Monitor worker node CPU utilisation (%)
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.pm.004
     - Monitor pod CPU utilisation
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.pm.005
     - Measure external storage IOPs
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.pm.006
     - Measure external storage throughput
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:internal infrastructure capabilities`
     - i.pm.007
     - Measure external storage capacity
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:profiles specifications & capability mapping`
     - i.os.001
     - Host operating system must provide drivers etc. to support listed capabilities.
     - Must support
     - Must support
     - ra2.ch.004

:ref:`ref_model:chapters/chapter04:capabilities and performance measurements`


**(1)** Defined in the ``.bronze`` configuration in RM section :ref:`ref_model:chapters/chapter04:storage extensions`

**(2)** In Kubernetes based infrastructures packet monitoring is out of the scope for the infrastructure.

Virtual Network Interface Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The required number of connection points to a Pod is described in ``e.cap.004`` above. This section describes the
required bandwidth of those connection points.

.. list-table:: Reference Model Requirements: Network Interface Specifications
   :widths: 10 30 30 10 10 10
   :header-rows: 1

   * - Reference Model Section
     - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - :ref:`ref_model:chapters/chapter04:virtual network interface specifications`
     - n1, n2, n3, n4, n5, n6
     - 1, 2, 3, 4, 5, 6 Gbps
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:virtual network interface specifications`
     - n10, n20, n30, n40, n50, n60
     - 10, 20, 30, 40, 50, 60 Gbps
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:virtual network interface specifications`
     - n25, n50, n75, n100, n125, n150
     - 25, 50, 75, 100, 125, 150 Gbps
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:virtual network interface specifications`
     - n50, n100 , n150, n200, n250 , n300
     - 50, 100, 150, 200, 250, 300 Gbps
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:virtual network interface specifications`
     - n100, n200, n300, n400, n500, n600
     - 100, 200, 300, 400, 500, 600 Gbps
     - Must support
     - Must support
     - N/A

:ref:`ref_model:chapters/chapter04:virtual network interface specifications`


Cloud Infrastructure Software Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Reference Model Requirements: Cloud Infrastructure Software Profile Requirements
   :widths: 10 10 50 10 10 10
   :header-rows: 1

   * - Reference Model Section
     - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - :ref:`ref_model:chapters/chapter05:virtual compute`
     - infra.com. cfg.001
     - CPU allocation ratio
     - 1:1
     - 1:1
     - :ref:`ra2.ch.005 <chapters/chapter04:Kubernetes Node>` ra2.ch.006
   * - :ref:`ref_model:chapters/chapter05:virtual compute`
     - infra.com. cfg.002
     - NUMA awareness
     - Not required
     - Must support
     - ra2.k8s.006
   * - :ref:`ref_model:chapters/chapter05:virtual compute`
     - infra.com. cfg.003
     - CPU pinning capability
     - Not required
     - Must support
     - ra2.k8s.009
   * - :ref:`ref_model:chapters/chapter05:virtual compute`
     - infra.com. cfg.004
     - Huge pages
     - Not required
     - Must support
     - ra2.ch.001
   * - :ref:`ref_model:chapters/chapter05:virtual storage`
     - infra.stg. cfg.002
     - Storage Block
     - Must support
     - Must support
     - :ref:`ra2.stg.004 <chapters/chapter04:Storage components>`
   * - :ref:`ref_model:chapters/chapter05:virtual storage`
     - infra.stg. cfg.003
     - Storage with replication
     - Not required
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual storage`
     - infra.stg. cfg.004
     - Storage with encryption
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual storage`
     - infra.stg. acc.cfg.00 1
     - Storage IOPS oriented encryption
     - Not required
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual storage`
     - infra.stg. acc.cfg.00 2
     - Storage capacity oriented encryption
     - Not required
     - Not required
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.cfg.001
     - IO virtualisation using virtio1.1
     - Must support (1)
     - Must support (1)
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.cfg.002
     - The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the
       scale-out features of the network fabric.(2)
     - Must support VXLAN, MPLSoUDP, GENEVE, other
     - No requirement specified
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.cfg.003
     - Network Address Translation
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.cfg.004
     - Security Groups
     - Must support
     - Must support
     - ra2.k8s.014
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.cfg.005
     - SFC support
     - Not required
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.cfg.006
     - Traffic patterns symmetry
     - Must support
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.acc.cfg.001
     - vSwitch optimisation
     - Not required
     - Must support DPDK (3)
     - ra2.ntw.010
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.acc.cfg.002
     - Support of HW offload
     - Not required
     - Optional, SmartNic
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.acc.cfg.003
     - Crypto acceleration
     - Not required
     - Optional
     - N/A
   * - :ref:`ref_model:chapters/chapter05:virtual networking`
     - infra.net.acc.cfg.004
     - Crypto Acceleration Interface
     - Not required
     - Optional
     - N/A

:ref:`ref_model:chapters/chapter05:virtual networking`

**(1)** Might have other interfaces (such as SR-IOV VFs to be directly passed to a VM or a Pod) or NIC-specific drivers
on guest machines transiently allowed until more mature solutions are available with an acceptable level of efficiency
to support telecom workloads (for example regarding CPU and energy consumption).

**(2)** In Kubernetes based infrastructures network separation is possible without an overlay (e.g.: with IPVLAN)

**(3)** This feature is not applicable for Kubernetes based infrastructures due to lack of vSwitch however workloads
need access to user space networking solutions.

Cloud Infrastructure Hardware Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Reference Model Requirements: Cloud Infrastructure Hardware Profile Requirements
   :widths: 10 10 50 10 10 10
   :header-rows: 1

   * - Reference Model Section
     - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - :ref:`ref_model:chapters/chapter05:compute resources`
     - infra.hw.cpu.cfg.001
     - Minimum number of CPU sockets
     - 2
     - 2
     - :ref:`ra2.ch.008 <chapters/chapter04:Kubernetes Node>`
   * - :ref:`ref_model:chapters/chapter05:compute resources`
     - infra.hw.cpu.cfg.002
     - Minimum number of Cores per CPU
     - 20
     - 20
     - :ref:`ra2.ch.008 <chapters/chapter04:Kubernetes Node>`
   * - :ref:`ref_model:chapters/chapter05:compute resources`
     - infra.hw.cpu.cfg.003
     - NUMA Alignment
     - N
     - Y
     - :ref:`ra2.ch.008 <chapters/chapter04:Kubernetes Node>`
   * - :ref:`ref_model:chapters/chapter05:compute resources`
     - infra.hw.cpu.cfg.004
     - Simultaneous Multithreading/ Symmetric Multiprocessing (SMT/SMP)
     - Must support
     - Optional
     - ra2.ch.004
   * - :ref:`ref_model:chapters/chapter05:compute resources`
     - infra.hw.cac.cfg.001
     - GPU
     - Not required
     - Optional
     - N/A
   * - :ref:`ref_model:chapters/chapter05:storage configurations`
     - infra.hw.stg.hdd.cfg.001
     - Local Storage HDD
     - No requirement specified
     - No requirement specified
     - N/A
   * - :ref:`ref_model:chapters/chapter05:storage configurations`
     - infra.hw.stg.ssd.cfg.002
     - Local Storage SSD
     - Should support
     - Should support
     - ra2.ch.009
   * - :ref:`ref_model:chapters/chapter05:network resources`
     - infra.hw.nic.cfg.001
     - Total Number of NIC Ports available in the host
     - 4
     - 4
     - ra2.ch.013
   * - :ref:`ref_model:chapters/chapter05:network resources`
     - infra.hw.nic.cfg.002
     - Port speed specified in Gbps (minimum values)
     - 10
     - 25
     - ra2.ch.014, ra2.ch.015
   * - :ref:`ref_model:chapters/chapter05:network resources`
     - infra.hw.pci.cfg. 001
     - Number of PCIe slots available in the host
     - 8
     - 8
     - ra2.ch.016
   * - :ref:`ref_model:chapters/chapter05:network resources`
     - infra.hw.pci.cfg.002
     - PCIe speed
     - Gen 3
     - Gen 3
     - ra2.ch.016
   * - :ref:`ref_model:chapters/chapter05:network resources`
     - infra.hw.pci.cfg.003
     - PCIe Lanes
     - 8
     - 8
     - ra2.ch.016
   * - :ref:`ref_model:chapters/chapter05:network resources`
     - infra.hw.nac.cfg.001
     - Cryptographic Acceleration
     - Not required
     - Optional
     - N/A
   * - :ref:`ref_model:chapters/chapter05:network resources`
     - infra.hw.nac.cfg.002
     - A SmartNIC that is used to offload vSwitch functionality to hardware
     - Not required
     - Optional (1)
     - N/A
   * - :ref:`ref_model:chapters/chapter05:network resources`
     - infra.hw.nac.cfg.003
     - Compression
     - Optional
     - Optional
     - N/A

:ref:`ref_model:chapters/chapter05:network acceleration configurations`

**(1)** There is no vSwitch in case of containers, but a SmartNIC can be used to offload any other network processing.

Edge Cloud Infrastructure Hardware Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the case of Telco Edge Cloud Deployments, hardware requirements can differ from the above to account for
environmental and other constraints.
The Reference Model :ref:`ref_model:chapters/chapter08:hybrid multi-cloud architecture`
includes considerations specific to deployments at the edge of the network. The infrastructure profiles "Basic" and
"High Performance" as per :ref:`ref_model:chapters/chapter04:profiles and workload flavours` still apply, but a number
of requirements of the above table are relaxed as follows:

.. list-table:: Reference Model Requirements: Edge Cloud Infrastructure Hardware Profile Requirements
   :widths: 10 10 50 10 10 10
   :header-rows: 1

   * - Reference Model Section
     - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - :ref:`ref_model:chapters/chapter08:telco edge cloud: infrastructure profiles`
     - infra.hw.cpu.cfg.001
     - sockets
     -
     -
     -
   * - :ref:`ref_model:chapters/chapter08:telco edge cloud: infrastructure profiles`
     - infra.hw.cpu.cfg.002
     - Minimum number of Cores per CPU
     - 1
     - 1
     - :ref:`ra2.ch.008 <chapters/chapter04:Kubernetes Node>`
   * - :ref:`ref_model:chapters/chapter08:telco edge cloud: infrastructure profiles`
     - infra.hw.cpu.cfg.003
     - NUMA Alignment
     - N
     - Y (1)
     - :ref:`ra2.ch.008 <chapters/chapter04:Kubernetes Node>`

:ref:`ref_model:chapters/chapter08:telco edge cloud: infrastructure profiles`.


**(1)** immaterial if the number of CPU sockets (infra.hw.cpu.cfg.001) is 1.

Cloud Infrastructure Management Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Reference Model Requirements: Cloud Infrastructure Management Requirements
   :widths: 10 10 50 10 10
   :header-rows: 1

   * - Reference Model Section
     - Reference
     - Description
     - Requirement (common to all Profiles)
     - Specification Reference
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.001
     - Capability to allocate virtual compute resources to a workload
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.002
     - Capability to allocate virtual storage resources to a workload
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.003
     - Capability to allocate virtual networking resources to a workload
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.004
     - Capability to isolate resources between tenants
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.005
     - Capability to manage workload software images
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.006
     - Capability to provide information related to allocated virtualised resources per tenant
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.007
     - Capability to notify state changes of allocated resources
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.008
     - Capability to collect and expose performance information on virtualised resources allocated
     - Must support
     - N/A
   * - :ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`
     - e.man.009
     - Capability to collect and notify fault information on virtualised resources
     - Must support
     - N/A

:ref:`ref_model:chapters/chapter04:cloud infrastructure management capabilities`.



Cloud Infrastructure Security Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Reference Model Requirements: Cloud Infrastructure Security Requirements
   :widths: 10 10 70 10
   :header-rows: 1

   * - Reference Model Section
     - Reference
     - Description
     - Specification Reference
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.001
     - The Platform **must** maintain the specified configuration.
     -
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.002
     - All systems part of Cloud Infrastructure **must** support password hardening as defined in
       `CIS Password Policy Guide <https://www.cisecurity.org/white-papers/cis-policy-guide/>`__.
       Hardening: CIS Password Policy Guide
     - `5.3.1 Node Hardening: Securing Kubernetes Hosts`
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.003
     - All servers part of Cloud Infrastructure **must** support a root of trust and secure boot.
     -
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.004
     - The Operating Systems of all the servers part of Cloud Infrastructure **must** be hardened by removing or
       disabling unnecessary services, applications and network protocols, configuring operating system user
       authentication, configuring resource controls, installing and configuring additional security controls where
       needed, and testing the security of the Operating System. (NIST SP 800-123)
     - :ref:`chapters/chapter05:principles` and :ref:`chapters/chapter05:node hardening`
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.005
     - The Platform **must** support Operating System level access control
     - :ref:`chapters/chapter05:node hardening`
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.006
     - The Platform **must** support Secure logging. Logging with root account must be prohibited when root
       privileges are not required.
     - :ref:`chapters/chapter05:restrict direct access to nodes`
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.007
     - All servers part of Cloud Infrastructure **must** be Time synchronized with authenticated Time service.
     -
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.008
     - All servers part of Cloud Infrastructure **must** be regularly updated to address security vulnerabilities.
     - :ref:`chapters/chapter05:vulnerability assessment`
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.009
     - The Platform **must** support Software integrity protection and verification and **must** scan source code
       and manifests.
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.010
     - The Cloud Infrastructure **must** support encrypted storage, for example, block, object and file storage,
       with access to encryption keys restricted based on a need to know. `Controlled Access Based on the Need
       to Know <https://www.cisecurity.org/controls/controlled-access-based-on-the-need-to-know/>`__
     -
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.011
     - The Cloud Infrastructure **should** support Read and Write only storage partitions (write only permission
       to one or more authorized actors).
     -
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.012
     - The Operator **must** ensure that only authorized actors have physical access to the underlying infrastructure.
     -
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.013
     - The Platform **must** ensure that only authorized actors have logical access to the underlying infrastructure.
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.014
     - All servers part of Cloud Infrastructure **should** support measured boot and an attestation server that monitors
       the measurements of the servers.
     -
   * - :ref:`ref_model:chapters/chapter07:system hardening`
     - sec.gen.015
     - Any change to the Platform must be logged as a security event, and the logged event must include
       the identity of the entity making the change, the change, the date and the time of the change.
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.001
     - The Platform **must** support authenticated and secure access to API, GUI and command line interfaces.
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.002
     - The Platform **must** support Traffic Filtering for workloads (for example, Firewall).
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.003
     - The Platform **must** support Secure and encrypted communications, and confidentiality and integrity of
       network traffic.
     - `:ref:`ref_model:chapters/chapter05:network resources` Use Transport Layer Security and Service Mesh`
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.004
     - The Cloud Infrastructure **must** support authentication, integrity and confidentiality on all network channels.
     - `:ref:`ref_model:chapters/chapter05:network resources` Use Transport Layer Security and Service Mesh`
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.005
     - The Cloud Infrastructure **must** segregate the underlay and overlay networks.
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.006
     - The Cloud Infrastructure must be able to utilise the Cloud Infrastructure Manager identity lifecycle
       management capabilities.
     - :ref:`chapters/chapter05:principles`
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.007
     - The Platform **must** implement controls enforcing separation of duties and privileges, least privilege
       use and least common mechanism (Role-Based Access Control).
     - :ref:`chapters/chapter05:principles` :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.008
     - The Platform **must** be able to assign the Entities that comprise the tenant networks to different
       trust domains. Communication between different trust domains is not allowed, by default.
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.009
     - The Platform **must** support creation of Trust Relationships between trust domains.
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.010
     - For two or more domains without existing trust relationships, the Platform **must not** allow the effect
       of an attack on one domain to impact the other domains either directly or indirectly.
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.011
     - The Platform **must not** reuse the same authentication credential (e.g., key-pair) on different Platform
       components (e.g., on different hosts, or different services).
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.012
     - The Platform **must** protect all secrets by using strong encryption techniques, and storing the protected
       secrets externally from the component
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.013
     - The Platform **must** provide secrets dynamically as and when needed.
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.014
     - The Platform **should** use Linux Security Modules such as SELinux to control access to resources.
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.015
     - The Platform **must not** contain back door entries (unpublished access points, APIs, etc.).
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.016
     - Login access to the platform's components **must** be through encrypted protocols such as SSH v2
       or TLS v1.2 or higher. Note: Hardened jump servers isolated from external networks are recommended
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.017
     - The Platform **must** provide the capability of using digital certificates that comply with X.509 standards
       issued by a trusted
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.018
     - The Platform **must** provide the capability of allowing certificate renewal and revocation.
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.019
     - The Platform **must** provide the capability of testing the validity of a digital certificate (CA signature,
       validity period, non revocation, identity).
     -
   * - :ref:`ref_model:chapters/chapter07:platform and access`
     - sec.sys.020
     - The Cloud Infrastructure architecture **should** rely on Zero Trust principles to build a secure by design environment.
     -
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.001
     - The Platform **must** support Confidentiality and Integrity of data at rest and in-transit. by design environment.
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.002
     - The Platform **should** support self-encrypting storage devices. data at rest and in-transit. by design environment.
     -
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.003
     - The Platform **must** support Confidentiality and Integrity of data related metadata.
     -
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.004
     - The Platform **must** support Confidentiality of processes and restrict information sharing with only the process
       owner (e.g., tenant).
     -
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.005
     - The Platform **must** support Confidentiality and Integrity of process-related metadata and restrict information
       sharing with only the process owner (e.g., tenant).
     -
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.006
     - The Platform **must** support Confidentiality and Integrity of workload resource utilization (RAM, CPU,
        Storage, Network I/O, cache, hardware offload) and restrict information sharing with only the workload
        owner (e.g., tenant).
     -
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.007
     - The Platform **must not** allow Memory Inspection by any actor other than the authorized actors for the
       Entity to which Memory is assigned (e.g., tenants owning the workload), for Lawful Inspection, and by
       secure monitoring services.
     -
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.008
     - The Cloud Infrastructure **must** support tenant networks segregation.
     - `5.7 Create and define Network Policies`
   * - :ref:`ref_model:chapters/chapter07:confidentiality and integrity`
     - sec.ci.009
     - For sensitive data encryption, the key management service **should** leverage a Hardware Security Module
       to manage and protect cryptographic keys.
     -
   * - :ref:`ref_model:chapters/chapter07:workload security`
     - sec.wl.001
     - The Platform **must** support Workload placement policy.
     -
   * - :ref:`ref_model:chapters/chapter07:workload security`
     - sec.wl.002
     - The Cloud Infrastructure **must** provide methods to ensure the platform's trust status and integrity
       (e.g., remote attestation, Trusted Platform Module).
     -
   * - :ref:`ref_model:chapters/chapter07:workload security`
     - sec.wl.003
     - The Platform **must** support secure provisioning of workloads.
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:workload security`
     - sec.wl.004
     - The Platform **must** support Location assertion (for mandated in-country or location requirements).
     -
   * - :ref:`ref_model:chapters/chapter07:workload security`
     - sec.wl.005
     - The Platform **must** support the separation of production and non-production Workloads.
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:workload security`
     - sec.wl.006
     - The Platform **must** support the separation of Workloads based on their categorisation (for example,
       payment card information, healthcare, etc.).
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:workload security`
     - sec.wl.007
     - The Operator **must** implement processes and tools to verify VNF authenticity and integrity.
     - :ref:`chapters/chapter05:trusted registry`
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.001
     - Images from untrusted sources **must not** be used.
     - :ref:`chapters/chapter05:trusted registry`
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.002
     - Images **must** be scanned to be maintained free from known vulnerabilities.
     - :ref:`chapters/chapter05:trusted registry`
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.003
     - Images **must not** be configured to run with privileges higher than the privileges of the actor
       authorized to run them.
     - :ref:`chapters/chapter05:run-time security`
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.004
     - Images **must** only be accessible to authorized actors.
     -
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.005
     - Image Registries **must** only be accessible to authorized actors.
     -
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.006
     - Image Registries **must** only be accessible over secure networks that enforce authentication,
       integrity and confidentiality.
     - :ref:`chapters/chapter05:trusted registry`
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.007
     - Image registries **must** be clear of vulnerable and out of date versions.
     - :ref:`chapters/chapter05:trusted registry`
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.008
     - Images **must not** include any secrets. Secrets include passwords, cloud provider credentials,
       SSH keys, TLS certificate keys, etc.
     - :ref:`chapters/chapter05:secrets management`
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.009
     - CIS Hardened Images **should** be used whenever possible.
     -
   * - :ref:`ref_model:chapters/chapter07:image security`
     - sec.img.010
     - Minimalist base images **should** be used whenever possible.
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.001
     - The Platform **must** support Secure Provisioning, Availability, and Deprovisioning (Secure Clean-Up)
       of workload resources where Secure Clean-Up includes tear-down, defense against virus or other attacks.
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.002
     - Cloud operations staff and systems **must** use management protocols limiting security risk such as
       SNMPv3, SSH v2, ICMP, NTP, syslog and TLS v1.2 or higher.
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.003
     - The Cloud Operator **must** implement and strictly follow change management processes for Cloud
       Infrastructure, Cloud Infrastructure Manager and other components of the cloud, and Platform change
       control on hardware.
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.004
     - The Cloud Operator **should** support automated templated approved changes.
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.005
     - Platform **must** provide logs and these logs must be regularly monitored for anomalous behavior.
     - :ref:`chapters/chapter05:enable logging and monitoring`
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.006
     - The Platform **must** verify the integrity of all Resource management requests.
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.007
     - The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and
       restarted images with current time information.
     - :ref:`chapters/chapter05:securing kubernetes orchestrator`
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.008
     - The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and
       restarted images with relevant DNS information.
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.009
     - The Platform **must** be able to update the tag of newly instantiated, suspended, hibernated,
       migrated and restarted images with relevant geolocation (geographical) information.
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.010
     - The Platform **must** log all changes to geolocation along with the mechanisms and sources of
       location information (i.e. GPS, IP block, and timing).
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.011
     - The Platform **must** implement Security life cycle management processes including the proactive
       update and patching of all deployed Cloud Infrastructure software.
     -
   * - :ref:`ref_model:chapters/chapter07:security lcm`
     - sec.lcm.012
     - The Platform **must** log any access privilege escalation.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.001
     - Platform **must** provide logs and these logs must be regularly monitored for events of interest.
       The logs **must** contain the following fields: event type, date/time, protocol, service or program
       used for access, success/failure, login ID or process ID, IP address and ports (source and destination)
       involved.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.002
     - Security logs **must** be time synchronised.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.003
     - The Platform **must** log all changes to time server source, time, date and time zones.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.004
     - The Platform **must** secure and protect Audit logs (containing sensitive information) both in-transit
       and at rest.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.005
     - The Platform **must** Monitor and Audit various behaviours of connection and login attempts to
       detect access attacks and potential access attempts and take corrective actions accordingly.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.006
     - The Platform **must** Monitor and Audit operations by authorized account access after login to
       detect malicious operational activity and take corrective actions accordingly.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.007
     - The Platform **must** Monitor and Audit security parameter configurations for compliance with
       defined security policies.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.008
     - The Platform **must** Monitor and Audit externally exposed interfaces for illegal access (attacks)
       and take corrective security hardening measures.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.009
     - The Platform **must** Monitor and Audit service handling for various attacks (malformed messages,
       signalling flooding and replaying, etc.) and take corrective actions accordingly.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.010
     - The Platform **must** Monitor and Audit running processes to detect unexpected or unauthorized
       processes and take corrective actions accordingly.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.011
     - The Platform **must** Monitor and Audit logs from infrastructure elements and workloads to
       detected anomalies in the system components and take corrective actions accordingly.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.012
     - The Platform **must** Monitor and Audit Traffic patterns and volumes to prevent malware
       download attempts.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.013
     - The monitoring system **must not** affect the security (integrity and confidentiality) of
       the infrastructure, workloads, or the user data (through back door entries).
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.014
     - The Monitoring systems **should not** impact IAAS, PAAS, and SAAS SLAs including availability SLAs.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.015
     - The Platform **must** ensure that the Monitoring systems are never starved of resources and **must**
       activate alarms when resource utilisation exceeds a configurable threshold.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.016
     - The Platform Monitoring components **should** follow security best practices for auditing,
       including secure logging and tracing.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.017
     - The Platform **must** audit systems for any missing security patches and take appropriate actions.
     - :ref:`chapters/chapter05:vulnerability assessment`
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.018
     - The Platform, starting from initialization, **must** collect and analyze logs to identify security
       events, and store these events in an external system.
     - :ref:`chapters/chapter05:patch management`
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.019
     - The Platform's components **must not** include an authentication credential, e.g., password, in any
       logs, even if encrypted.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.020
     - The Platform's logging system **must** support the storage of security audit logs for a configurable
       period of time.
     -
   * - :ref:`ref_model:chapters/chapter07:monitoring and security audit`
     - sec.mon.021
     - The Platform **must** store security events locally if the external logging system is unavailable and
       shall periodically attempt to send these to the external logging system until successful.
     -
   * - :ref:`ref_model:chapters/chapter07:open source software`
     - sec.oss.001
     - Open source code **must** be inspected by tools with various capabilities for static and dynamic code analysis.
     - :ref:`chapters/chapter05:vulnerability assessment`
   * - :ref:`ref_model:chapters/chapter07:open source software`
     - sec.oss.002
     - The `CVE (Common Vulnerabilities and Exposures) <https://cve.mitre.org/>`__ **must** be used to identify
       vulnerabilities and their severity rating for open source code part of Cloud Infrastructure and workloads
       software.
     -
   * - :ref:`ref_model:chapters/chapter07:open source software`
     - sec.oss.003
     - Critical and high severity rated vulnerabilities **must** be fixed in a timely manner. Refer to the
       `CVSS (Common Vulnerability Scoring System <https://www.first.org/cvss/>`__ to know a vulnerability
       score and its associated rate (low, medium, high, or critical).
     -
   * - :ref:`ref_model:chapters/chapter07:open source software`
     - sec.oss.004
     - A dedicated internal isolated repository separated from the production environment **must** be used to
       store vetted open source content.
     - :ref:`chapters/chapter05:trusted registry`
   * - :ref:`ref_model:chapters/chapter07:open source software`
     - sec.oss.005
     - A Software Bill of Materials (`SBOM <https://www.ntia.gov/SBOM>`__) **should** be provided or build,
       and maintained to identify the software components and their origins.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - secure design and architecture stage requirements`
     - sec.arch.001
     - Threat Modelling methodologies and tools **should** be used during the Secure Design and Architecture
       stage triggered by Software Feature Design trigger. It may be done manually or using tools like open source
       OWASP Threat Dragon
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - secure design and architecture stage requirements`
     - sec.arch.002
     - Security Control Baseline Assessment **should** be performed during the Secure Design and Architecture
       stage triggered by Software Feature Design trigger. Typically done manually by internal or independent
       assessors.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - secure code stage requirements`
     - sec.code.001
     - SAST -Static Application Security Testing **must** be applied during Secure Coding stage triggered by Pull,
       Clone or Comment trigger. Security testing that analyses application source code for software vulnerabilities
       and gaps against best practices. Example: open source OWASP range of tools.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - secure code stage requirements`
     - sec.code.002
     - SCA - Software Composition Analysis **should** be applied during Secure Coding stage triggered by Pull,
       Clone or Comment trigger. Security testing that analyses application source code or compiled code for
       software components with known vulnerabilities. Example: open source OWASP range of tools.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - secure code stage requirements`
     - sec.code.003
     - Source Code Review **should** be performed continuously during Secure Coding stage. Typically done manually.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - secure code stage requirements`
     - sec.code.004
     - Integrated SAST via IDE Plugins **should** be used during Secure Coding stage triggered by Developer Code
       trigger. On the local machine: through the IDE or integrated test suites; triggered on completion of coding be
       developer.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - secure code stage requirements`
     - sec.code.005
     - SAST of Source Code Repo **should** be performed during Secure Coding stage triggered by Developer Code trigger.
       Continuous delivery pre-deployment: scanning prior to deployment.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous build, integration and testing stage requirements`
     - sec.bld.001
     - SAST -Static Application Security Testing **should** be applied during the Continuous Build, Integration and
       Testing stage triggered by Build and Integrate trigger. Example: open source OWASP range of tools.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous build, integration and testing stage requirements`
     - sec.bld.002
     - SCA - Software Composition Analysis **should** be applied during the Continuous Build, Integration and
       Testing stage triggered by Build and Integrate trigger. Example: open source OWASP range of tools.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous build, integration and testing stage requirements`
     - sec.bld.003
     - Image Scan **must** be applied during the Continuous Build, Integration and Testing stage triggered by
       Package trigger. Example: A push of a container image to a container registry may trigger a vulnerability
       scan before the image becomes available in the registry.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous build, integration and testing stage requirements`
     - sec.bld.004
     - DAST - Dynamic Application Security Testing **should** be applied during the Continuous Build, Integration
       and Testing stage triggered by Stage & Test trigger. Security testing that analyses a running application by
       exercising application functionality and detecting vulnerabilities based on application behaviour and response.
       Example: OWASP ZAP.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous build, integration and testing stage requirements`
     - sec.bld.005
     - Fuzzing **should** be applied during the Continuous Build, Integration and testing stage triggered by
       Stage & Test trigger. Fuzzing or fuzz testing is an automated software testing technique that involves
       providing invalid, unexpected, or random data as inputs to a computer program. Example: GitLab Open
       Sources Protocol Fuzzer Community Edition.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous build, integration and testing stage requirements`
     - sec.bld.006
     - IAST - Interactive Application Security Testing **should** be applied during the Continuous Build, Integration
       and Testing stage triggered by Stage & Test trigger. Software component deployed with an application that
       assesses application behaviour and detects presence of vulnerabilities on an application being exercised in
       realistic testing scenarios. Example: Contrast Community Edition.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous delivery and deployment stage requirements`
     - sec.del.001
     - Image Scan **must** be applied during the Continuous Delivery and Deployment stage triggered by
       Publish to Artifact and Image Repository trigger. Example: GitLab uses the open-source Clair engine for
       container image scanning.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous delivery and deployment stage requirements`
     - sec.del.002
     - Code Signing **must** be applied during the Continuous Delivery and Deployment stage triggered by
       Publish to Artifact and Image Repository trigger. Code Signing provides authentication to assure that
       downloaded files are from the publisher named on the certificate.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous delivery and deployment stage requirements`
     - sec.del.003
     - Artifact and Image Repository Scan **should** be continuously applied during the Continuous Delivery
       and Deployment stage. Example: GitLab uses the open source Clair engine for container scanning.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - continuous delivery and deployment stage requirements`
     - sec.del.004
     - Component Vulnerability Scan **must** be applied during the Continuous Delivery and Deployment stage
       triggered by Instantiate Infrastructure trigger. The vulnerability scanning system is deployed on the cloud
       platform to detect security vulnerabilities of specified components through scanning and to provide timely
       security protection. Example: OWASP Zed Attack Proxy (ZAP).
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - runtime defence and monitoring requirements`
     - sec.run.001
     - Component Vulnerability Monitoring **must** be continuously applied during the Runtime Defence and
       Monitoring stage and remediation actions **must** be applied for high severity rated vulnerabilities.
       Security technology that monitors components like virtual servers and assesses data, applications, and
       infrastructure for security risks.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - runtime defence and monitoring requirements`
     - sec.run.002
     - RASP - Runtime Application Self- Protection **should** be continuously applied during the Runtime Defence
       and Monitoring stage. Security technology deployed within the target application in production for detecting,
       alerting, and blocking attacks.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - runtime defence and monitoring requirements`
     - sec.run.003
     - Application testing and Fuzzing **should** be continuously applied during the Runtime Defence
       and Monitoring stage. Fuzzing or fuzz testing is an automated software testing technique that
       involves providing invalid, unexpected, or random data as inputs to a computer program.
       Example: GitLab Open Sources Protocol Fuzzer Community Edition.
     -
   * - :ref:`ref_model:chapters/chapter07:iaac - runtime defence and monitoring requirements`
     - sec.run.004
     - Penetration Testing **should** be continuously applied during the Runtime Defence and Monitoring stage.
       Typically done manually.
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.001
     - The Cloud Operator **should** comply with Center for Internet Security CIS Controls
       (`https://www.cisecurity.org <https://www.cisecurity.org/>`__)
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.002
     - The Cloud Operator, Platform and Workloads **should** follow the guidance in the CSA Security
       Guidance for Critical Areas of Focus in Cloud Computing (latest version)
       `https://cloudsecurityalliance. org/ <https://cloudsecurityalliance.org/>`__
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.003
     - The Platform and Workloads **should** follow the guidance in the
       `OWASP Cheat Sheet Series (OCSS) <https://github.com/OWASP/CheatSheetSeries>`__
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.004
     - The Cloud Operator, Platform and Workloads **should** ensure that their code is not vulnerable to the
       OWASP Top Ten Security Risks `https://owasp.org/www-project-top-t en/
       <https://owasp.org/www-project-top-ten/>`__
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.005
     - The Cloud Operator, Platform and Workloads **should** strive to improve their maturity on the
       `OWASP Software Maturity Model (SAMM) <https://owaspsamm.org/blog/2019/12/20/version2-community-release/>`__
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.006
     - The Cloud Operator, Platform and Workloads **should** utilize the
       `OWASP Web Security Testing Guide <https://github.com/OWASP/wstg/tree/master/document>`__
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.007
     - The Cloud Operator, and Platform **should** satisfy the requirements for Information Management Systems
       specified in `ISO/IEC 27001 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>`__. ISO/IEC
       27002:2013 - ISO/IEC 27001 is the international Standard for best-practice information security management
       systems (ISMSs).
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.008
     - The Cloud Operator, and Platform **should** implement the Code of practice for Security Controls specified
       `ISO/IEC 27002:2013 (or la test) <https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en>`__
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.009
     - The Cloud Operator, and Platform **should** implement the `ISO/IEC 27 032:2012 (or latest)
       <https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en>`__ Guidelines for Cybersecurity techniques.
       ISO/IEC 27032 - ISO/IEC 27032 is the international Standard focusing explicitly on cybersecurity.
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.010
     - The Cloud Operator **should** conform to the ISO/IEC 27035 standard for incidence management.
       ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management.
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.011
     - The Cloud Operator **should** conform to the ISO/IEC 27031 standard for business continuity. ISO/IEC 27031 -
       ISO/IEC 27031 is the international Standard for ICT readiness for business continuity.
     -
   * - :ref:`ref_model:chapters/chapter07:compliance with standards`
     - sec.std.012
     - The Public Cloud Operator **must**, and the Private Cloud Operator **may** be certified to be compliant
       with the International Standard on Awareness Engagements (ISAE) 3402 (in the US: SSAE 16). International
       Standard on Awareness Engagements (ISAE) 3402. US Equivalent: SSAE16.
     -

:ref:`ref_model:chapters/chapter07:consolidated security requirements`

Kubernetes Architecture Requirements
------------------------------------

The requirements in this section are to be delivered in addition to those in section `Reference Model
Requirements <#reference-model-requirements>`_, and have been
created to support the Principles defined in the :ref:`chapters/chapter01:Overview` of this
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

.. list-table:: Kubernetes Architecture Requirements
   :widths: 10 10 10 50 20
   :header-rows: 1

   * - Reference
     - Category
     - Sub-category
     - Description
     - Specification Reference
   * - gen.cnt.02
     - General
     - Cloud nativeness
     - The Architecture must support immutable infrastructure.
     - :ref:`ra2.ch.017 <chapters/chapter04:Kubernetes Node>`
   * - gen.cnt.03
     - General
     - Cloud nativeness
     - The Architecture must run conformant Kubernetes as defined by the
       `CNCF <https://github.com/cncf/k8s-conformance>`__.
     - :ref:`ra2.k8s.001 <chapters/chapter04:Kubernetes>`
   * - gen.cnt.04
     - General
     - Cloud nativeness
     - The Architecture must support clearly defined abstraction layers.
     -
   * - gen.cnt.05
     - General
     - Cloud nativeness
     - The Architecture should support configuration of all components in an automated manner
       using openly published API definitions.
     -
   * - gen.scl.01
     - General
     - Scalability
     - The Architecture should support policy driven horizontal auto-scaling of workloads.
     -
   * - gen.rsl.01
     - General
     - Resiliency
     - The Architecture must support resilient Kubernetes components that are required for the
       continued availability of running workloads.
     - :ref:`ra2.k8s.004 <chapters/chapter04:Kubernetes>`
   * - gen.rsl.02
     - General
     - Resiliency
     - The Architecture should support resilient Kubernetes service components that are not
       subject to gen.rsl.01.
     - :ref:`ra2.k8s.002 <chapters/chapter04:Kubernetes>`, :ref:`ra2.k8s.003 <chapters/chapter04:Kubernetes>`
   * - gen.avl.01
     - General
     - Availability
     - The Architecture must provide High Availability for Kubernetes components.
     - :ref:`ra2.k8s.002 <chapters/chapter04:Kubernetes>`, :ref:`ra2.k8s.003 <chapters/chapter04:Kubernetes>`,
       :ref:`ra2.k8s.004 <chapters/chapter04:Kubernetes>`
   * - gen.ost.01
     - Openness
     - Availability
     - The Architecture should embrace open-based standards and technologies.
     - :ref:`ra2.crt.001 <chapters/chapter04:Container runtimes>`,
       :ref:`ra2.crt.002 <chapters/chapter04:Container runtimes>`,
       :ref:`ra2.ntw.002 <chapters/chapter04:Networking solutions>`,
       :ref:`ra2.ntw.006 <chapters/chapter04:Networking solutions>`,
       :ref:`ra2.ntw.007 <chapters/chapter04:Networking solutions>`
   * - inf.com.01
     - Infrastructure
     - Compute
     - The Architecture must provide compute resources for Pods. technologies.
     - :ref:`ra2.k8s.004 <chapters/chapter04:Kubernetes>`
   * - inf.stg.01
     - Infrastructure
     - Storage
     - The Architecture must support the ability for an operator to choose whether or
       not to deploy persistent storage for Pods.
     - :ref:`ra2.stg.004 <chapters/chapter04:Storage components>`
   * - inf.ntw.01
     - Infrastructure
     - Network
     - The Architecture must support network resiliency on the Kubernetes nodes.
     -
   * - inf.ntw.02
     - Infrastructure
     - Network
     - The Architecture must support fully redundant network connectivity to the Kubernetes
       nodes, leveraging at least two physical network connections per node. If the node is
       virtualised, the redundant network interfaces must be implemented on the Hypervisor
       host.
     -
   * - inf.ntw.03
     - Infrastructure
     - Network
     - The networking solution should be able to be centrally administrated and configured.
     - :ref:`ra2.ntw.001 <chapters/chapter04:Networking solutions>`,
       :ref:`ra2.ntw.004 <chapters/chapter04:Networking solutions>`
   * - inf.ntw.04
     - Infrastructure
     - Network
     - The Architecture must support dual stack IPv4 and IPv6 for Kubernetes workloads.
     - :ref:`ra2.ch.007 <chapters/chapter04:Kubernetes Node>`,
       :ref:`ra2.k8s.010 <chapters/chapter04:Kubernetes>`
   * - inf.ntw.05
     - Infrastructure
     - Network
     - The Architecture must support capabilities for integrating SDN controllers.
     -
   * - inf.ntw.06
     - Infrastructure
     - Network
     - The Architecture must support more than one networking solution.
     - :ref:`ra2.ntw.005 <chapters/chapter04:Networking solutions>`,
       :ref:`ra2.ntw.007 <chapters/chapter04:Networking solutions>`
   * - inf.ntw.07
     - Infrastructure
     - Network
     - The Architecture must support the ability for an operator to choose whether or not
       to deploy more than one networking solution.
     - :ref:`ra2.ntw.005 <chapters/chapter04:Networking solutions>`
   * - inf.ntw.08
     - Infrastructure
     - Network
     - The Architecture must provide a default network which implements the Kubernetes network model.
     - :ref:`ra2.ntw.002 <chapters/chapter04:Networking solutions>`
   * - inf.ntw.09
     - Infrastructure
     - Network
     - The networking solution must not interfere with or cause interference to any interface or
       network it does not own.
     -
   * - inf.ntw.10
     - Infrastructure
     - Network
     - The Architecture must support Cluster wide coordination of IP address assignment.
     -
   * - inf.ntw.13
     - Infrastructure
     - Network
     - The platform must allow specifying multiple separate IP pools. Tenants are required to
       select at least one IP pool that is different from the control infrastructure IP pool or
       other tenant IP pools.
     -
   * - inf.ntw.14
     - Infrastructure
     - Network
     - The platform must allow NATless traffic (i.e. exposing the pod IP address directly to the
       outside), allowing source and destination IP addresses to be preserved in the traffic headers
       from workloads to external networks. This is needed e.g. for signaling applications, using SIP
       and Diameter protocols.
     - :ref:`ra2.ntw.011 <chapters/chapter04:Networking solutions>`
   * - inf.ntw.15
     - Infrastructure
     - Network
     - The platform must support LoadBalancer Publishing Service (ServiceType)
     -
   * - inf.ntw.16
     - Infrastructure
     - Network
     - The platform must support Ingress.
     -
   * - inf.ntw.17
     - Infrastructure
     - Network
     - The platform should support NodePort Publishing Service (ServiceTypes).
     -
   * - inf.ntw.18
     - Infrastructure
     - Network
     - The platform should support ExternalName Publishing Service (ServiceTypes).
     -
   * - inf.vir.01
     - Infrastructure
     - Virtual Infr astructure
     - The Architecture must support the capability for Containers to consume infrastructure resources
       abstracted by Host Operating Systems that are running within a virtual machine.
     - :ref:`ra2.ch.005 <chapters/chapter04:Kubernetes Node>`,
       :ref:`ra2.ch.011 <chapters/chapter04:Kubernetes Node>`
   * - inf.phy.01
     - Infrastructure
     - Physical Infrastructu re
     - The Architecture must support the capability for Containers to consume infrastructure resources
       abstracted by Host Operating Systems that are running within a physical server.
     - :ref:`ra2.ch.008 <chapters/chapter04:Kubernetes Node>`
   * - kcm.gen.01
     - Kubernetes Cluster
     - General
     - The Architecture must support policy driven horizontal auto- scaling of Kubernetes Cluster.
     - N/A
   * - kcm.gen.02
     - Kubernetes Cluster
     - General
     - The Architecture must enable workload resiliency.
     - :ref:`ra2.k8s.004 <chapters/chapter04:Kubernetes>`
   * - int.api.01
     - API
     - General
     - The Architecture must leverage the Kubernetes APIs to discover and declaratively manage compute
       (virtual and bare metal resources), network, and storage.
     - For Networking: :ref:`ra2.ntw.001 <chapters/chapter04:Networking solutions>`,
       :ref:`ra2.ntw.008 <chapters/chapter04:Networking solutions>`,
       :ref:`ra2.app.006 <chapters/chapter04:Kubernetes workloads>`. Compute/storage not yet met.
   * - int.api.02
     - API
     - General
     - The Architecture must support the usage of a Kubernetes Application package manager using the
       Kubernetes API, like Helm v3. network, and storage.
     - :ref:`ra2.pkg.001 <chapters/chapter04:Kubernetes Application package manager>`
   * - int.api.03
     - API
     - General
     - The Architecture must support stable features in its APIs.
     -
   * - int.api.04
     - API
     - General
     - The Architecture must support limited backward compatibility in its APIs. Support for the whole
       API must not be dropped, but the schema or other details can change.
     -
