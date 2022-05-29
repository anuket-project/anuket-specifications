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

.. list-table:: Reference Model Requirements: Cloud Infrastructure Software Profile Capabilities
   :widths: 20 20 10 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - e.cap.001
     - Max number of vCPU that can be assigned to a single instance by the Cloud Infrastructure
     - At least 16
     - At least 16
     -
   * - e.cap.002
     - Max memory that can be assigned to a single instance by the Cloud Infrastructure
     - at least 32 GB
     - at least 32 GB
     -
   * - e.cap.003
     - Max storage that can be assigned to a single instance by the Cloud Infrastructure
     - at least 320 GB
     - at least 320 GB
     -
   * - e.cap.004
     - Max number of connection points that can be assigned to a single instance by the Cloud Infrastructure
     - 6
     - 6
     -
   * - e.cap.005
     - Max storage that can be attached / mounted to an instance by the Cloud Infrastructure
     - Up to 16TB:sup:`1`
     - Up to 16TB:sup:`1`
     -
   * - e.cap.006/infra.com.cfg.003
     - CPU pinning support
     - Not required
     - Must support
     -
   * - e.cap.007/infra.com.cfg.002
     - NUMA support
     - Not required
     - Must support
     -
   * - e.cap.018/infra.com.cfg.005
     - Simultaneous Multithreading (SMT) enabled
     - Must
     - Optional support
     -
   * - i.cap.018/infra.com.cfg.004
     - Huge pages configured
     - Not required
     - Must support
     -

**:sup:`1`** Defined in the ``.bronze`` configuration in
:ref:`ref_model/chapters/chapter04:storage extensions`

Cloud Infrastructure Software Profile Extensions Requirements for Compute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Cloud Infrastructure Software Profile Extensions Requirements for Compute
   :widths: 20 20 10 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Profile Extensions
     - Profile Extra-Specs
     - Specification Reference
   * - e.cap.008/infra.com.acc.cfg.001
     - IPSec Acceleration using the virtio-ipsec interface
     - Compute Intensive GPU
     -
     -
   * - e.cap.010/infra.com.acc.cfg.002
     - Transcoding Acceleration
     - Compute Intensive GPU
     - Video Transcoding
     -
   * - e.cap.011/infra.com.acc.cfg.003
     - Programmable Acceleration
     - Firmware-programmable adapter
     - Accelerator
     -
   * - e.cap.012
     - Enhanced Cache Management: L=Lean; E=Equal; X=eXpanded
     - E
     - E
     -
   * - e.cap.014/infra.com.acc.cfg.004
     - Hardware coprocessor support (GPU/NPU)
     - Compute Intensive GPU
     -
     -
   * - e.cap.016/infra.com.acc.cfg.005
     - FPGA/other Acceleration H/W
     - Firmware-programmable adapter
     -
     -

Cloud Infrastructure Software Profile Requirements for Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter05:virtual networking`)

The features and configuration requirements related to virtual
networking for the two (2) types of Cloud Infrastructure Profiles are
specified below followed by networking bandwidth requirements.

.. list-table:: Reference Model Requirements - Virtual Networking
   :widths: 20 30 10 10 10
   :header-rows: 1

   * - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - infra.net.cfg.001
     - IO virtualisation using virtio1.1
     - Must support
     - Must support
     -
   * - infra.net.cfg.002
     - The overlay network encapsulation protocol needs to enable ECMP in the
       underlay to take advantage of the scale-out features of the network fabric
     - Must support VXLAN, MPLSoUDP, GENEVE, other
     - No requirement specified
     -
   * - infra.net.cfg.003
     - Network Address Translation
     - Must support
     - Must support
     -
   * - infra.net.cfg.004
     - Security Groups
     - Must support
     - Must support
     -
   * - infra.net.cfg.005
     - SFC support
     - Not required
     - Must support
     -
   * - infra.net.cfg.006
     - Traffic patterns symmetry
     - Must support
     - Must support
     -

The required number of connection points to an instance is described in
``e.cap.004`` `above <#2.2.1>`__. The table below specifies the required
bandwidth of those connection points.

.. list-table:: Reference Model Requirements - Network Interface Specifications
   :widths: 20 20 10 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High Performance Profile
     - Specification Reference
   * - n1, n2, n3, n4, n5, n6
     - 1, 2, 3, 4, 5, 6 Gbps
     - Must support
     - Must support
     -
   * - n10, n20, n30, n40, n50, n60
     - 10, 20, 30, 40, 50, 60 Gbps
     - Must support
     - Must support
     -
   * - n25, n50, n75, n100, n125, n150
     - 25, 50, 75, 100, 125, 150 Gbps
     - Optional
     - Must support
     -
   * - n50, n100, n150, n200, n250, n300
     - 50, 100, 150, 200, 250, 300 Gbps
     - Optional
     - Must support
     -
   * - n100, n200, n300, n400, n500, n600
     - 100, 200, 300, 400, 500, 600 Gbps
     - Optional
     - Must support
     -

Cloud Infrastructure Software Profile Extensions Requirements for Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Cloud Infrastructure Software Profile Extensions Requirements
   for Networking
   :widths: 20 20 10 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - e.cap.013/infra.hw.nac.cfg.004
     - SR-IOV over PCI-PT
     - N
     - Y
     -
   * - e.cap.019/infra.net.acc.cfg.001
     - vSwitch optimisation (DPDK)
     - N
     - Y
     -
   * - e.cap.015/infra.net.acc.cfg.002
     - SmartNIC (for HW Offload)
     - N
     - Optional
     -
   * - e.cap.009/infra.net.acc.cfg.003
     - Crypto acceleration
     - N
     - Optional
     -
   * - infra.net.acc.cfg.004
     - Crypto Acceleration Interface
     - N
     - Optional
     -

Cloud Infrastructure Software Profile Requirements for Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter05:cloud infrastructure software profiles features and requirements`)

.. list-table:: Reference Model Requirements - Cloud Infrastructure Software
   Profile Requirements for Storage
   for Networking
   :widths: 20 20 10 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - infra.stg.cfg.002
     - Storage Block
     - Must support
     - Must support
     -
   * - infra.stg.cfg.003
     - Storage with replication
     - Not required
     - Must support
     -
   * - infra.stg.cfg.004
     - Storage with encryption
     - Must support
     - Must support
     -
   * - infra.stg.acc.cfg.001
     - Storage IOPS oriented
     - Not required
     - Must support
     -
   * - infra.stg.acc.cfg.002
     - Storage capacity oriented
     - Not required
     - Not required
     -

Cloud Infrastructure Software Profile Extensions Requirements for Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Reference Model Requirements - Cloud Infrastructure Software
   Profile Extensions Requirements for Storage
   for Networking
   :widths: 15 15 20 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Profile Extensions
     - Profile Extra-Specs
     - Specification Reference
   * - infra.stg.acc.cfg.001
     - Storage IOPS oriented
     - Storage Intensive High-performance storage
     -
     -
   * - infra.stg.acc.cfg.002
     - Storage capacity oriented
     - High Capacity
     -
     -

Cloud Infrastructure Hardware Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter05:cloud infrastructure hardware profiles features and requirements.`)

.. list-table:: Reference Model Requirements - Cloud Infrastructure Hardware
   Profile Requirements
   :widths: 20 20 10 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - infra.hw.001
     - CPU Architecture (Values such as x64, ARM, etc.)
     -
     -
     -
   * - infra.hw.cpu.cfg.001
     - Minimum number of CPU (Sockets)
     - 2
     - 2
     -
   * - infra.hw.cpu.cfg.002
     - Minimum number of Cores per CPU
     - 20
     - 20
     -
   * - infra.hw.cpu.cfg.003
     - NUMA
     - Not required
     - Must support
     -
   * - infra.hw.cpu.cfg.004
     - Simultaneous Multithreading/Symmetric Multiprocessing (SMT/SMP)
     - Must support
     - Optional
     -
   * - infra.hw.stg.hdd.cfg.001
     - Local Storage HDD
     - No requirement specified
     - No requirement specified
     -
   * - infra.hw.stg.ssd.cfg.002
     - Local Storage SSD
     - Should support
     - Should support
     -
   * - infra.hw.nic.cfg.001
     - Total Number of NIC Ports available in the host
     - 4
     - 4
     -
   * - infra.hw.nic.cfg.002
     - Port speed specified in Gbps (minimum values)
     - 10
     - 25
     -
   * - infra.hw.pci.cfg.001
     - Number of PCIe slots available in the host
     - 8
     - 8
     -
   * - infra.hw.pci.cfg.002
     - PCIe speed
     - Gen 3
     - Gen 3
     -
   * - infra.hw.pci.cfg.003
     - PCIe Lanes
     - 8
     - 8
     -
   * - infra.hw.nac.cfg.003
     - Compression
     - No requirement specified
     - No requirement specified
     -

Cloud Infrastructure Hardware Profile-Extensions Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter05:cloud infrastructure hardware profiles features and requirements.`)

.. list-table:: Reference Model Requirements - Cloud Infrastructure Hardware
   Profile Extensions Requirements
   :widths: 20 20 10 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Requirement for Basic Profile
     - Requirement for High-Performance Profile
     - Specification Reference
   * - e.cap.014/infra.hw.cac.cfg.001
     - GPU
     - N
     - Optional
     -
   * - e.cap.016/infra.hw.cac.cfg.002
     - FPGA/other Acceleration H/W
     - N
     - Optional
     -
   * - e.cap.009/infra.hw.nac.cfg.001
     - Crypto Acceleration
     - N
     - Optional
     -
   * - e.cap.015/infra.hw.nac.cfg.002
     - SmartNIC
     - N
     - Optional
     -
   * - infra.hw.nac.cfg.003
     - Compression
     - Optional
     - Optional
     -
   * - e.cap.013/infra.hw.nac.cfg.004
     - SR-IOV over PCI-PT
     - N
     - Yes
     -

Cloud Infrastructure Management Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(source :ref:`ref_model/chapters/chapter04:cloud infrastructure management capabilities`)

.. list-table:: Reference Model Requirements - Cloud Infrastructure
   Management Requirements
   :widths: 20 30 10 20
   :header-rows: 1

   * - Reference
     - Description
     - Requirement (common to all Profiles)
     - Specification Reference
   * - e.man.001
     - Capability to allocate virtual compute resources to a workload
     - Must support
     -
   * - e.man.002
     - Capability to allocate virtual storage resources to a workload
     - Must support
     -
   * - e.man.003
     - Capability to allocate virtual networking resources to a workload
     - Must support
     -
   * - e.man.004
     - Capability to isolate resources between tenants
     - Must support
     -
   * - e.man.005
     - Capability to manage workload software images
     - Must support
     -
   * - e.man.006
     - Capability to provide information related to allocated virtualised resources per tenant
     - Must support
     -
   * - e.man.007
     - Capability to notify state changes of allocated resources
     - Must support
     -
   * - e.man.008
     - Capability to collect and expose performance information on virtualised resources allocated
     - Must support
     -
   * - e.man.009
     - Capability to collect and notify fault information on virtualised resources
     - Must support
     -

Cloud Infrastructure Security Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Hardening Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:system hardening`)

.. list-table:: Reference Model Requirements - System Hardening Requirements
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.gen.001
     - Hardening
     - The Platform **must** maintain the specified configuration.
     - :ref:`ref_arch/openstack/chapters/chapter06:security lcm`

       :ref:`ref_arch/openstack/chapters/chapter07:\
       cloud infrastructure provisioning and configuration management`
   * - sec.gen.002
     - Hardening
     - All systems part of Cloud Infrastructure **must** support hardening as
       defined in `CIS Password Policy Guide
       <https://www.cisecurity.org/white-papers/cis-password-policy-guide/>`__
       .
     - :ref:`ref_arch/openstack/chapters/chapter06:password policy`
   * - sec.gen.003
     - Hardening
     - All servers part of Cloud Infrastructure **must** support a root of
       trust and secure boot.
     - :ref:`ref_arch/openstack/chapters/chapter06:server boot hardening`
   * - sec.gen.004
     - Hardening
     - The Operating Systems of all the servers part of Cloud Infrastructure
       **must** be hardened by removing or disabling unnecessary services,
       applications and network protocols, configuring operating system user
       authentication, configuring resource controls, installing and
       configuring additional security controls where needed, and testing the
       security of the Operating System (NIST SP 800-123).
     - :ref:`ref_arch/openstack/chapters/chapter06:function and software`
   * - sec.gen.005
     - Hardening
     - The Platform **must** support Operating System level access control.
     - :ref:`ref_arch/openstack/chapters/chapter06:system access`
   * - sec.gen.006
     - Hardening
     - The Platform **must** support Secure logging. Logging with root account
       must be prohibited when root privileges are not required.
     - :ref:`ref_arch/openstack/chapters/chapter06:system access`
   * - sec.gen.007
     - Hardening
     - All servers part of Cloud Infrastructure **must** be Time synchronised
       with authenticated Time service.
     - :ref:`ref_arch/openstack/chapters/chapter06:\
       security logs time synchronisation`
   * - sec.gen.008
     - Hardening
     - All servers part of Cloud Infrastructure **must** be regularly updated
       to address security vulnerabilities.
     - :ref:`ref_arch/openstack/chapters/chapter06:security lcm`
   * - sec.gen.009
     - Hardening
     - The Platform **must** support software integrity protection and
       verification.
     - :ref:`ref_arch/openstack/chapters/chapter06:\
       integrity of openstack components configuration`
   * - sec.gen.010
     - Hardening
     - The Cloud Infrastructure **must** support encrypted storage, for
       example, block, object and file storage, with access to encryption
       keys restricted based on a need to know
       (`Controlled Access Based on the Need to Know
       <https://www.cisecurity.org/controls/controlled-access-based-on-the-need-to-know/>`__).
     - :ref:`ref_arch/openstack/chapters/chapter06:\
       confidentiality and integrity`
   * - sec.gen.012
     - Hardening
     - The Operator **must** ensure that only authorised actors have physical
       access to the underlying infrastructure.
     - This requirement's verification goes beyond Anuket testing scope
   * - sec.gen.013
     - Hardening
     - The Platform **must** ensure that only authorised actors have logical
       access to the underlying infrastructure.
     - :ref:`ref_arch/openstack/chapters/chapter06:system access`
   * - sec.gen.015
     - Hardening
     - Any change to the Platform **must** be logged as a security event, and
       the logged event must include the identity of the entity making the
       change, the change, the date and the time of the change.
     - :ref:`ref_arch/openstack/chapters/chapter06:security lcm`

Platform and Access Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:platform and access`)

.. list-table:: Reference Model Requirements - Platform and Access
   Requirements
   :widths: 20 10 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.sys.001
     - Access
     - The Platform must support authenticated and secure access to API, GUI
       and command line interfaces
     - :ref:`ref_arch/openstack/chapters/chapter06:rbac`
   * - sec.sys.002
     - Access
     - The Platform must support Traffic Filtering for workloads (for example,
       Firewall).
     - :ref:`ref_arch/openstack/chapters/chapter06:workload security`
   * - sec.sys.003
     - Access
     - The Platform must support Secure and encrypted communications, and
       confidentiality and integrity of network
     - :ref:`ref_arch/openstack/chapters/chapter06:confidentiality and integrity`
   * - sec.sys.004
     - Access
     - The Cloud Infrastructure must support authentication, integrity and
       confidentiality on all network channels.
     - :ref:`ref_arch/openstack/chapters/chapter06:confidentiality and integrity` `
   * - sec.sys.005
     - Access
     - The Cloud Infrastructure must segregate the underlay and overlay networks.
     - :ref:`ref_arch/openstack/chapters/chapter06:confidentiality and integrity`
   * - sec.sys.006
     - Access
     - The Cloud Infrastructure must be able to utilise the Cloud Infrastructure Manager
       identity lifecycle management capabilities.
     - :ref:`ref_arch/openstack/chapters/chapter06:identity security`
   * - sec.sys.007
     - Access
     - The Platform must implement controls enforcing separation of duties and privileges,
       least privilege use and least common mechanism (Role-Based Access Control).
     - :ref:`ref_arch/openstack/chapters/chapter06:rbac`
   * - sec.sys.008
     - Access
     - The Platform must be able to assign the Entities that comprise the tenant networks to
       different trust domains. (Communication between different trust domains is not allowed,
       by default.)
     - :ref:`ref_arch/openstack/chapters/chapter06:workload security`
   * - sec.sys.009
     - Access
     - The Platform must support creation of Trust Relationships between trust domains. These
       maybe uni-directional relationships where the trusting domain trusts another domain (the
       "trusted domain") to authenticate users for them them or to allow access to its resources
       from the trusted domain. In a bidirectional relationship both domain are "trusting" and
       "trusted".
     -
   * - sec.sys.010
     - Access
     - For two or more domains without existing trust relationships, the Platform must not allow
       the effect of an attack on one domain to impact the other domains either directly or
       indirectly.
     -
   * - sec.sys.011
     - Access
     - The Platform must not reuse the same authentication credentials (e.g., key pairs) on
       different Platform components (e.g., different hosts, or different services).
     - :ref:`ref_arch/openstack/chapters/chapter06:system access`
   * - sec.sys.012
     - Access
     - The Platform must protect all secrets by using strong encryption techniques and storing
       the protected secrets externally from the component (e.g., in OpenStack Barbican)
     -
   * - sec.sys.013
     - Access
     - The Platform must generate secrets dynamically as and when needed.
     -
   * - sec.sys.015
     - Access
     - The Platform must not contain back door entries (unpublished access points, APIs, etc.).
     -
   * - sec.sys.016
     - Access
     - Login access to the Platform’s components must be through encrypted protocols such as SSH
       v2 or TLS v1.2 or higher. Note: Hardened jump servers isolated from external networks are
       recommended
     - :ref:`ref_arch/openstack/chapters/chapter06:security lcm`
   * - sec.sys.017
     - Access
     - The Platform must provide the capability of using digital certificates that comply with X.509
       standards issued by a trusted Certification Authority.
     - :ref:`ref_arch/openstack/chapters/chapter06:confidentiality and integrity`
   * - sec.sys.018
     - Access
     - The Platform must provide the capability of allowing certificate renewal and revocation.
     -
   * - sec.sys.019
     - Access
     - The Platform must provide the capability of testing the validity of a digital certificate (CA
       signature, validity period, non revocation identity).
     -

Confidentiality and Integrity Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:confidentiality and integrity`)

.. list-table:: Reference Model Requirements - Confidentiality and Integrity
   Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.ci.001
     - Confidentiality/Integrity
     - The Platform must support Confidentiality and Integrity of data
       at rest and in transit.
     - :ref:`ref_arch/openstack/chapters/chapter06:confidentiality and
       integrity`
   * - sec.ci.003
     - Confidentiality/Integrity
     - The Platform must support Confidentiality and Integrity of data
       related metadata.
     -
   * - sec.ci.004
     - Confidentiality
     - The Platform must support Confidentiality of processes and restrict
       information sharing with only the process owner (e.g., tenant).
     -
   * - sec.ci.005
     - Confidentiality/Integrity
     - The Platform must support Confidentiality and Integrity of process-
       related metadata and restrict information sharing with only the
       process owner (e.g., tenant).
     -
   * - sec.ci.006
     - Confidentiality/Integrity
     - The Platform must support Confidentiality and Integrity of workload
       resource utilisation (RAM, CPU, Storage, Network I/O, cache,
       hardware offload) and restrict information sharing with only the
       workload owner (e.g., tenant).
     -
   * - sec.ci.007
     - Confidentiality/Integrity
     - The Platform must not allow Memory Inspection by any actor other
       than the authorised actors for the Entity to which Memory is
       assigned (e.g., tenants owning the workload), for Lawful
       Inspection, and for secure monitoring services. Administrative
       access must be managed using Platform Identity Lifecycle
       Management.
     -
   * - sec.ci.008
     - Confidentiality
     - The Cloud Infrastructure must support tenant networks segregation.
     - :ref:`ref_arch/openstack/chapters/chapter06:workload security`


Workload Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:workload security requirements`)

.. list-table:: Reference Model Requirements - Workload Security
   Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.wl.001
     - Workload
     - The Platform must support Workload placement policy.
     - :ref:`ref_arch/openstack/chapters/chapter06:workload security`
   * - sec.wl.002
     - Workload
     - The Cloud Infrastructure provide methods to ensure the platform's
       trust status and integrity (e.g., remote attestation, Trusted
       Platform Module).
     -
   * - sec.wl.003
     - Workload
     - The Platform must support secure provisioning of Workloads.
     - :ref:`ref_arch/openstack/chapters/chapter06:workload security`
   * - sec.wl.004
     - Workload
     - The Platform must support Location assertion (for mandated in-
       country or location requirements).
     - :ref:`ref_arch/openstack/chapters/chapter06:workload security`
   * - sec.wl.005
     - Workload
     - The Platform must support the separation of production and non-
       production Workloads.
     - This requirement's verification goes beyond Anuket testing scope
   * - sec.wl.006
     - Workload
     - The Platform must support the separation of Workloads based on
       their categorisation (for example, payment card information,
       healthcare, etc.)
     - :ref:`ref_arch/openstack/chapters/chapter06:workload security`
   * - sec.wl.007
     - Workload
     - The Operator must implement processes and tools to verify verify
       NF authenticity and integrity.
     -

Image Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:image security`)

.. list-table:: Reference Model Requirements - Image Security
   Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.img.001
     - Image
     - Images from untrusted sources must not be used.
     - :ref:`ref_arch/openstack/chapters/chapter06:image security`
   * - sec.img.002
     - Image
     - Images must be scanned to be maintained free from known vulnerabilities.
     - :ref:`ref_arch/openstack/chapters/chapter06:image security`
   * - sec.img.003
     - Image
     - Images must not be configured to run with privileges higher than the
       privileges of the actor authorised to run them.
     -
   * - sec.img.004
     - Image
     - Images must only be accessible to authorised actors.
     - :ref:`ref_arch/openstack/chapters/chapter06:integrity of openstack
       components configuration`
   * - sec.img.005
     - Image
     - Image Registries must only be accessible to authorised actors.
     - :ref:`ref_arch/openstack/chapters/chapter06:integrity of openstack
       components configuration`
   * - sec.img.006
     - Image
     - Image Registries must only be accessible over networks that enforce
       authentication, integrity and confidentiality.
     - :ref:`ref_arch/openstack/chapters/chapter06:integrity of openstack
       components configuration`
   * - sec.img.007
     - Image
     - Image registries must be clear of vulnerable and out of date versions.
     - :ref:`ref_arch/openstack/chapters/chapter06:image security`
   * - sec.img.008
     - Image
     - Images must not include any secrets. Secrets include passwords, cloud
       provider credentials, SSH keys, TLS certificate keys, etc.
     -

Security LCM Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:security lcm`)

.. list-table:: Reference Model Requirements - Security LCM
   Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.lcm.001
     - LCM
     - The Platform must support Secure Provisioning, Availability, and
       Deprovisioning (Secure Clean-Up) of workload resources where Secure
       Clean-Up includes tear-down, defense against virus or other attacks.
     - :ref:`ref_arch/openstack/chapters/chapter06:monitoring and security
       audit`
   * - sec.lcm.002
     - LCM
     - The Cloud Operator must use management protocols limiting security risk
       such as SNMPv3, SSH v2, ICMP, NTP, syslog and TLS v1.2 or higher.
     - :ref:`ref_arch/openstack/chapters/chapter06:security lcm`
   * - sec.lcm.003
     - LCM
     - The Cloud Operator must implement and strictly follow change management
       processes for Cloud Infrastructure, Infrastructure Manager and other
       components of the cloud, and Platform change control on hardware.
     - :ref:`ref_arch/openstack/chapters/chapter06:monitoring and security
       audit`
   * - sec.lcm.005
     - LCM
     - Platform must provide logs and these logs must be monitored for
       anomalous behaviour.
     - :ref:`ref_arch/openstack/chapters/chapter06:monitoring and security
       audit`
   * - sec.lcm.006
     - LCM
     - The Platform must verify the integrity of all Resource management
       requests.
     - :ref:`ref_arch/openstack/chapters/chapter06:confidentiality and
       integrity of tenant data (sec.ci.001)`
   * - sec.lcm.007
     - LCM
     - The Platform must be able to update newly instantiated, suspended,
       hibernated, migrated and restarted images with current time information.
     -
   * - sec.lcm.008
     - LCM
     - The Platform must be able to update newly instantiated, suspended,
       hibernated, migrated and restarted images with relevant DNS information.
     -
   * - sec.lcm.009
     - LCM
     - The Platform must be able to update the tag of newly instantiated,
       suspended, hibernated, migrated and restarted images with relevant
       geolocation (geographical) information.
     -
   * - sec.lcm.010
     - LCM
     - The Platform must log all changes to geolocation along with the
       mechanisms and sources of location information (i.e. GPS, IP block,
       and timing).
     -
   * - sec.lcm.011
     - LCM
     - The Platform must implement Security life cycle management processes
       including the proactive update and patching of all deployed Cloud
       Infrastructure software.
     - :ref:`ref_arch/openstack/chapters/chapter06:patches`
   * - sec.lcm.012
     - LCM
     - The Platform must log any access privilege escalation.
     - :ref:`ref_arch/openstack/chapters/chapter06:what to log / what not
       to log`

Monitoring and Security Audit Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source
:ref:`ref_model/chapters/chapter07:monitoring and security audit`)

The Platform is assumed to provide configurable alerting and
notification capability and the operator is assumed to have automated
systems, policies and procedures to act on alerts and notifications in a
timely fashion. In the following the monitoring and logging capabilities
can trigger alerts and notifications for appropriate action.

.. list-table:: Reference Model Requirements - Monitoring and Security Audit
   Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.mon.001
     - Monitoring/Audit
     - Platform must provide logs and these logs must be regularly monitored
       for events of interest. The logs must contain the following fields:
       event type, date/time, protocol, service or program used for access,
       success/failure, login ID or process ID, IP address and ports (source
       and destination) involved.
     - :ref:`ref_arch/openstack/chapters/chapter06:required fields`
   * - sec.mon.002
     - Monitoring
     - Security logs must be time synchronised.
     - :ref:`ref_arch/openstack/chapters/chapter06:security logs time
       synchronisation`
   * - sec.mon.003
     - Monitoring
     - The Platform must log all changes to time server source, time, date
       and time zones.
     - :ref:`ref_arch/openstack/chapters/chapter06:security logs time
       synchronisation`
   * - sec.mon.004
     - Audit
     - The Platform must secure and protect Audit logs (containing sensitive
       information) both in-transit and at rest.
     - :ref:`ref_arch/openstack/chapters/chapter06:security lcm`
   * - sec.mon.005
     - Monitoring/Audit
     - The Platform must Monitor and Audit various behaviours of connection
       and login attempts to detect access attacks and potential access
       attempts and take corrective accordingly actions.
     - :ref:`ref_arch/openstack/chapters/chapter06:what to log / what not
       to log`
   * - sec.mon.006
     - Monitoring/Audit
     - The Platform must Monitor and Audit operations by authorised account
       access after login to detect malicious operational activity and take
       corrective actions.
     - :ref:`ref_arch/openstack/chapters/chapter06:monitoring and security
       audit`
   * - sec.mon.007
     - Monitoring/Audit
     - The Platform must Monitor and Audit security parameter configurations
       for compliance with defined security policies.
     - :ref:`ref_arch/openstack/chapters/chapter06:integrity of openstack
       components configuration`
   * - sec.mon.008
     - Monitoring/Audit
     - The Platform must Monitor and Audit externally exposed interfaces for
       illegal access (attacks) and take corrective security hardening
       measures.
     - :ref:`ref_arch/openstack/chapters/chapter06:confidentiality and
       integrity of communications (sec.ci.001)`
   * - sec.mon.009
     - Monitoring/Audit
     - The Platform must Monitor and Audit service for various attacks
       (malformed messages, signalling flooding and replaying, etc.) and take
       corrective actions accordingly.
     - :ref:`ref_arch/openstack/chapters/chapter06:monitoring and security
       audit`
   * - sec.mon.010
     - Monitoring/Audit
     - The Platform must Monitor and Audit running processes to detect
       unexpected or unauthorised processes and take corrective actions
       accordingly.
     - :ref:`ref_arch/openstack/chapters/chapter06:monitoring and security
       audit`
   * - sec.mon.011
     - Monitoring/Audit
     - The Platform must Monitor and Audit logs from infrastructure elements
       and workloads to detected anomalies in the system components and take
       corrective actions accordingly.
     - :ref:`ref_arch/openstack/chapters/chapter06:creating logs`
   * - sec.mon.012
     - Monitoring/Audit
     - The Platform must Monitor and Audit Traffic patterns and volumes to
       prevent malware download attempts.
     - :ref:`ref_arch/openstack/chapters/chapter06:confidentiality and
       integrity of tenant data (sec.ci.001)`
   * - sec.mon.013
     - Monitoring
     - The monitoring system must not affect the security (integrity and
       confidentiality) of the infrastructure, workloads, or the user data
       (through back door entries)
     -
   * - sec.mon.015
     - Monitoring
     - The Platform must ensure that the Monitoring systems are never starved
       of resources and must activate alarms when resource utilisation exceeds
       a configurable threshold.
     - :ref:`ref_arch/openstack/chapters/chapter06:monitoring and security
       audit`
   * - sec.mon.017
     - Audit
     - The Platform must audit systems for any missing security patches and
       take appropriate actions.
     - :ref:`ref_arch/openstack/chapters/chapter06:patches`
   * - sec.mon.018
     - Monitoring
     - The Platform, starting from initialisation, must collect and analyse
       logs to identify security events, and store these events in an external
       system.
     - :ref:`ref_arch/openstack/chapters/chapter06:where to log`
   * - sec.mon.019
     - Monitoring
     - The Platform's components must not include an authentication
       credential, e.g., password, in any logs, even if encrypted.
     - :ref:`ref_arch/openstack/chapters/chapter06:what to log / what not
       to log`
   * - sec.mon.020
     - Monitoring/Audit
     - The Platform's logging system must support the storage of security
       audit logs for a configurable period of time.
     - :ref:`ref_arch/openstack/chapters/chapter06:data retention`
   * - sec.mon.021
     - Monitoring
     - The Platform must store security events locally if the external logging
       system is unavailable and shall periodically attempt to send these to
       the external logging system until successful.
     - :ref:`ref_arch/openstack/chapters/chapter06:where to log`

Open-Source Software Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:open-source software security`)

.. list-table:: Reference Model Requirements - Open-Source Software Security
   Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.oss.001
     - Software
     - Open-source code must be inspected by tools with various capabilities
       for static and dynamic code analysis.
     -
   * - sec.oss.002
     - Software
     - The CVE (Common Vulnerabilities and Exposures) must be used to identify
       vulnerabilities and their severity rating for open-source code part of
       Cloud Infrastructure and workloads software.
     -
   * - sec.oss.003
     - Software
     - Critical and high severity rated vulnerabilities must be fixed in a
       timely manner. Refer to the CVSS (Common Vulnerability Scoring System)
       to know a vulnerability score and its associated rate (low, medium,
       high, or critical)
     -
   * - sec.oss.004
     - Software
     - A dedicated internal isolated repository separated from the production
       environment must be used to store vetted open-source content.
     -

IaaC security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^

(source
:ref:`ref_model/chapters/chapter07:iaac - secure design and architecture stage requirements`)

**Secure Code Stage Requirements**

.. list-table:: Reference Model Requirements: IaaC Security Requirements,
   Secure Code Stage
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.code.001
     - IaaC
     - SAST -Static Application Security Testing must be applied during Secure
       Coding stage triggered by Pull, Clone or Comment trigger. Security
       testing that analyses application source code for software
       vulnerabilities and gaps against bestpractices. Example: open source
       OWASP range of tools.
     -

**Continuous Build, Integration and Testing Stage Requirements**

.. list-table:: Reference Model Requirements - IaaC Security Requirements,
   Continuous Build, Integration and Testing Stage
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.bld.003
     - IaaC
     - Image Scan must be applied during the Continuous Build, Integration and
       Testing stage triggered by Package trigger, example: A push of a container
       image to a containerregistry may trigger a vulnerability scan before the
       image becomes available in the registry.
     -

**Continuous Delivery and Deployment Stage Requirements**

.. list-table:: Reference Model Requirements - IaaC Security Requirements,
   Continuous Delivery and Deployment Stage
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.del.001
     - IaaC
     - Image Scan must be applied during the Continuous Delivery and
       Deployment stage triggered by Publish to Artifact and Image
       Repository trigger. Example: GitLab uses the open source Clair
       engine for container image scanning.
     -
   * - sec.del.002
     - IaaC
     - Code Signing must be applied during the Continuous Deliveryand
       Deployment stage and Image Repository trigger. Code Signing provides
       authentication to assure that downloaded files are form the publisher
       named on the certificate.
     -
   * - sec.del.004
     - IaaC
     - Component Vulnerability Scan must be applied during the Continuous
       Delivery and Deployment stage triggered by Instantiate Infrastructure
       trigger. The vulnerability scanning system is deployed on the cloud
       platform to detect security vulnerabilities of specified components
       through scanning and to provide timely security protection. Example:
       OWASP Zed Attack Proxy (ZAP).
     -

**Runtime Defence and Monitoring Requirements**

.. list-table:: Reference Model Requirements - IaaC Security Requirements,
   Runtime Defence and Monitoring Stage
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.run.001
     - IaaC
     - Component Vulnerability Monitoring must be continuously applied
       during the Runtime Defence and monitoring stage. Security technology that
       monitors components like virtual servers and assesses data, applications,
       and infrastructure forsecurity risks.
     -

Compliance with Standards Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:compliance with standards`)

.. list-table:: Reference Model Requirements: Compliance with Standards
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - sec.std.012
     - Standards
     - The Public Cloud Operator must, and the Private Cloud Operator may be
       certified to be compliant with the International Standard on Awareness
       Engagements (ISAE) 3402 (in the US:SSAE 16); International Standard on
       Awareness Engagements (ISAE) 3402. US Equivalent: SSAE16.
     -

Architecture and OpenStack Requirements
---------------------------------------

“Architecture” in this chapter refers to Cloud Infrastructure (referred
to as NFVI by ETSI) + VIM (as specified in Reference Model Chapter 3).

General Requirements
~~~~~~~~~~~~~~~~~~~~

.. list-table:: General Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - gen.ost.01
     - Open source
     - The Architecture must use OpenStack APIs.
     - :ref:`ref_arch/openstack/chapters/chapter05:\ consolidated set of apis`
   * - gen.ost.02
     - Open source
     - The Architecture must support dynamic request and configuration of
        virtual resources (compute, network, storage) through OpenStack APIs.
     - :ref:`ref_arch/openstack/chapters/chapter05:\ consolidated set of apis`
   * - gen.rsl.01
     - Resiliency
     - The Architecture must support resilient OpenStack components that are
       required for the continued availability of running workloads.
     -
   * - gen.avl.01
     - Availability
     - The Architecture must provide High Availability for OpenStack
       components.
     - :ref:`ref_arch/openstack/chapters/chapter04:\ underlying resources`

Infrastructure Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Infrastructure Requirements
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - inf.com.01
     - Compute
     - The Architecture **must** provide compute resources for instances.
     - :ref:`ref_arch/openstack/chapters/chapter03:cloud workload services`
   * - inf.com.04
     - Compute
     - The Architecture **must** be able to support multiple CPU type options
       to support various infrastructure profiles (Basic and High
       Performance).
     - :ref:`ref_arch/openstack/chapters/chapter04:\
       support for cloud infrastructure profiles and flavors`
   * - inf.com.05
     - Compute
     - The Architecture **must** support Hardware Platforms with NUMA
       capabilities.
     - :ref:`ref_arch/openstack/chapters/chapter04:\
       support for cloud infrastructure profiles and flavors`
   * - inf.com.06
     - Compute
     - The Architecture **must** support CPU Pinning of the vCPUs of an
       instance.
     - :ref:`ref_arch/openstack/chapters/chapter04:\
       support for cloud infrastructure profiles and flavors`
   * - inf.com.07
     - Compute
     - The Architecture **must** support different hardware configurations
       to support various infrastructure profiles (Basic and High
       Performance).
     - :ref:`ref_arch/openstack/chapters/chapter03:\
       cloud partitioning: host aggregates, availability zones`
   * - inf.com.08
     - Compute
     - The Architecture **must** support allocating certain number of host
       cores for all non-tenant workloads such as for OpenStack services.
       SMT threads can be allocated to individual OpenStack services or their
       components. `Dedicating host cores to certain workloads
       (e.g., OpenStack services)
       <https://docs.openstack.org/nova/latest/configuration/config.html#compute.cpu_dedicated_set>`__.
       Please see example, `Configuring libvirt compute nodes for CPU pinning
       <https://docs.openstack.org/nova/latest/admin/cpu-topologies.html>`__
     - :ref:`ref_arch/openstack/chapters/chapter03:\
       cloud partitioning: host aggregates, availability zones`
   * - inf.com.09
     - Compute
     - The Architecture **must** ensure that the host cores assigned to
       non-tenant and tenant workloads are SMT aware: that is, a host core and
       its associated SMT threads are either all assigned to non-tenant
       workloads or all assigned to tenant workloads.
     - :ref:`ref_arch/openstack/chapters/chapter04:\
       pinned and unpinned cpus`
   * - inf.stg.01
     - Storage
     - The Architecture **must** provide remote (not directly attached to the
       host) Block storage for Instances.
     - :ref:`ref_arch/openstack/chapters/chapter03:storage`
   * - inf.stg.02
     - Storage
     - The Architecture **must** provide Object storage for Instances.
       Operators **may** choose not to implement Object Storage but must be
       cognizant of the the risk of "Compliant VNFs" failing in their
       environment.
     - :ref:`ref_arch/openstack/chapters/chapter04:swift`
   * - inf.nw.01
     - Network
     - The Architecture **must** provide virtual network interfaces to
       instances.
     - :ref:`ref_arch/openstack/chapters/chapter05:neutron`
   * - inf.nw.02
     - Network
     - The Architecture **must** include capabilities for integrating SDN
       controllers to support provisioning of network services, from the SDN
       OpenStack Neutron service, such as networking of VTEPs to the Border
       Edge based VRFs.
     - :ref:`ref_arch/openstack/chapters/chapter03:\
       virtual networking – 3rd party sdn solution`
   * - inf.nw.03
     - Network
     - The Architecture **must** support low latency and high throughput
       traffic needs.
     - :ref:`ref_arch/openstack/chapters/chapter04:network fabric`
   * - inf.nw.05
     - Network
     - The Architecture **must** allow for East/West tenant traffic within the
       cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve).
     - :ref:`ref_arch/openstack/chapters/chapter04:network fabric`
   * - inf.nw.07
     - Network
     - The Architecture must support network :ref:`resiliency
       <common/glossary:cloud platform abstraction related terminology:>`
     - :ref:`ref_arch/openstack/chapters/chapter03:network`
   * - inf.nw.10
     - Network
     - The Cloud Infrastructure Network Fabric **must** be capable of enabling
       highly available (Five 9’s or better) Cloud Infrastructure.
     - :ref:`ref_arch/openstack/chapters/chapter03:network`
   * - inf.nw.15
     - Network
     - The Architecture **must** support multiple networking options for Cloud
       Infrastructure to support various infrastructure profiles (Basic and
       High Performance).
     - :ref:`ref_arch/openstack/chapters/chapter04:\
       neutron extensions` and `OpenStack Neutron Plugins
       <https://wiki.openstack.org/wiki/Neutron_Plugins_and_Drivers>`__
   * - inf.nw.16
     - Network
     - The Architecture **must** support dual stack IPv4 and IPv6 for tenant
       networks and workloads.
     -

VIM Requirements
~~~~~~~~~~~~~~~~

.. list-table:: VIM Requirements
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - vim.01
     - General
     - The Architecture **must** allow infrastructure resource sharing.
     - :ref:`ref_arch/openstack/chapters/chapter03:consumable
       infrastructure resources and services`
   * - vim.03
     - General
     - The Architecture **must** allow VIM to discover and manage Cloud
       Infrastructure resources.
     - :ref:`ref_arch/openstack/chapters/chapter05:placement`
   * - vim.05
     - General
     - The Architecture **must** include image repository management.
     - :ref:`ref_arch/openstack/chapters/chapter05:glance`
   * - vim.07
     - General
     - The Architecture **must** support multi-tenancy.
     - :ref:`ref_arch/openstack/chapters/chapter03:multi-tenancy
       (execution environment)`
   * - vim.08
     - General
     - The Architecture **must** support resource tagging.
     - `OpenStack Resource Tags
       <https://specs.openstack.org/openstack/api-wg/guidelines/tags.html>`__

Interfaces & APIs Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Interfaces and APIs Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference

   * - int.api.01
     - API
     - The Architecture must provide APIs to access the authentication service
       and the associated mandatory features detailed in chapter 5
     - :ref:`ref_arch/openstack/chapters/chapter05:keystone`
   * - int.api.02
     - API
     - The Architecture must provide APIs to access the image management
       service and the associated mandatory features detailed in chapter 5
     - :ref:`ref_arch/openstack/chapters/chapter05:glance`
   * - int.api.03
     - API
     - The Architecture must provide APIs to access the block storage
       management service and the associated mandatory features detailed in chapter 5.
     - :ref:`ref_arch/openstack/chapters/chapter05:cinder`
   * - int.api.04
     - API
     - The Architecture must provide APIs to access the object storage
       management service and the associated mandatory features detailed in chapter 5.
     - :ref:`ref_arch/openstack/chapters/chapter05:swift`
   * - int.api.05
     - API
     - The Architecture must provide APIs to access the network management
       service and the associated mandatory features detailed in chapter 5.
     - :ref:`ref_arch/openstack/chapters/chapter05:neutron`
   * - int.api.06
     - API
     - The Architecture must provide APIs to access the compute resources
       management service and the associated mandatory features detailed in chapter 5.
     - :ref:`ref_arch/openstack/chapters/chapter05:nova`
   * - int.api.07
     - API
     - The Architecture must provide GUI access to tenant facing cloud
       platform core services except at Edge/Far Edge clouds.
     - :ref:`ref_arch/openstack/chapters/chapter04:horizon`
   * - int.api.08
     - API
     - The Architecture must provide APIs needed to discover and manage
       Cloud Infrastructure resources.
     - :ref:`ref_arch/openstack/chapters/chapter05:placement`
   * - int.api.09
     - API
     - The Architecture must provide APIs to access the orchestration service.
     - :ref:`ref_arch/openstack/chapters/chapter05:heat`
   * - int.api.10
     - API
     - The Architecture must expose the latest version and microversion of the
       APIs for the given Anuket OpenStack release for each of the OpenStack core
       services.
     - :ref:`ref_arch/openstack/chapters/chapter05:core openstack services apis`


Tenant Requirements
~~~~~~~~~~~~~~~~~~~

.. list-table:: Tenant Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference

   * - tnt.gen.01
     - General
     - The Architecture must support self-service dashboard (GUI) and
       APIs for users to deploy, configure and manage their workloads.
     - :ref:`ref_arch/openstack/chapters/chapter04:horizon`

       :ref:`ref_arch/openstack/chapters/chapter03:cloud workload services`

Operations and LCM
~~~~~~~~~~~~~~~~~~

.. list-table:: LCM Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - lcm.gen.01
     - General
     - The Architecture must support zero downtime of running workloads when
       the number of compute hosts and/or the storage capacity is being
       expanded or unused capacity is being removed.
     -
   * - lcm.adp.02
     - Automated deployment
     - The Architecture must support upgrades of software, provided by the
       cloud provider, so that the running workloads are not impacted
       (viz., hitless upgrades). Please note that this means that the existing
       data plane services should not fail (go down).
     -

Assurance Requirements
~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Assurance Requirements
   :widths: 15 15 30 20
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Specification Reference
   * - asr.mon.01
     - Integration
     - The Architecture must include integration with various infrastructure
       components to support collection of telemetry for assurance monitoring
       and network intelligence.
     -
   * - asr.mon.03
     - Monitoring
     - The Architecture must allow for the collection and dissemination of
       performance and fault information.
     -
   * - asr.mon.04
     - Network
     - The Cloud Infrastructure Network Fabric and Network Operating System
       must provide network operational visibility through alarming and streaming
       telemetry services for operational management, engineering planning,
       troubleshooting, and network performance optimisation.
     -


Architecture and OpenStack Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requirements listed in this section are optional, and are not
required in order to be deemed a conformant implementation.

General Recommendations
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: General Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - gen.cnt.01
     - Cloud nativeness
     - The Architecture **should** consist of stateless service components.
       However, where state is required it must be kept external to the
       component.
     - OpenStack consists of both stateless and stateful services where the
       stateful services utilise a database. For latter see `Configuring the
       stateful services
       <https://docs.openstack.org/ha-guide/control-plane-stateful.html>`__
   * - gen.cnt.02
     - Cloud nativeness
     - The Architecture **should** consist of service components implemented
       as microservices that are individually dynamically scalable.
     -
   * - gen.scl.01
     - Scalability
     - The Architecture **should** support policy driven auto-scaling.
     - This requirement is currently not addressed but will likely be
       supported through
       `Senlin <https://docs.openstack.org/senlin/wallaby/>`__, cluster
       management service.
   * - gen.rsl.02
     - Resiliency
     - The Architecture **should** support resilient OpenStack service
       components that are not subject to gen.rsl.01.
     -

Infrastructure Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Infrastructure Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - inf.com.02
     - Compute
     - The Architecture **should** include industry standard hardware
       management systems at both HW device level (embedded) and HW platform
       level (external to device).
     -
   * - inf.com.03
     - Compute
     - The Architecture **should** support Symmetric Multiprocessing with
       shared memory access as well as Simultaneous Multithreading.
     -
   * - inf.stg.08
     - Storage
     - The Architecture **should** allow use of externally provided large
       archival storage for its Backup / Restore / Archival needs.
     -
   * - inf.stg.09
     - Storage
     - The Architecture **should** make available all non-host OS / Hypervisor
       / Host systems storage as network-based Block, File or Object Storage
       for tenant/management consumption.
     -
   * - inf.stg.10
     - Storage
     - The Architecture **should** provide local Block storage for Instances.
     - :ref:`ref_arch/openstack/chapters/chapter03:virtual storage`
   * - inf.nw.04
     - Network
     - The Architecture **should** support service function chaining.
     -
   * - inf.nw.06
     - Network
     - The Architecture **should** support Distributed Virtual Routing (DVR)
       to allow compute nodes to route traffic efficiently.
     -
   * - inf.nw.08
     - Network
     - The Cloud Infrastructure Network Fabric **should** embrace the concepts
       of open networking and disaggregation using commodity networking
       hardware and disaggregated Network Operating Systems.
     -
   * - inf.nw.09
     - Network
     - The Cloud Infrastructure Network Fabric **should** embrace open-based
       standards and technologies.
     -
   * - inf.nw.11
     - Network
     - The Cloud Infrastructure Network Fabric **should** be architected to
       provide a standardised, scalable, and repeatable deployment model
       across all applicable Cloud Infrastructure sites.
     -
   * - inf.nw.17
     - Network
     - The Architecture **should** use dual stack IPv4 and IPv6 for Cloud
       Infrastructure internal networks.
     -
   * - inf.acc.01
     - Acceleration
     - The Architecture **should** support Application Specific Acceleration
       (exposed to VNFs).
     - :ref:`ref_arch/openstack/chapters/chapter03:acceleration`
   * - inf.acc.02
     - Acceleration
     - The Architecture **should** support Cloud Infrastructure Acceleration
       (such as SmartNICs).
     - `OpenStack Future - Specs defined
       <https://specs.openstack.org/openstack/neutron-specs/specs/stein/neutron-ovs-agent-support-baremetal-with-smart-nic.html>`__
   * - inf.acc.03
     - Acceleration
     - The Architecture **may** rely on on SR-IOV PCI-Pass through to provide
       acceleration to VNFs.
     -
   * - inf.img.01
     - Image
     - The Architecture **should** make the immutable images available via
       location independent means.
     - :ref:`ref_arch/openstack/chapters/chapter04:glance`

VIM Recommendations
~~~~~~~~~~~~~~~~~~~

.. list-table:: VIM Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - vim.02
     - General
     - The Architecture **should** support deployment of OpenStack components
       in containers.
     - :ref:`ref_arch/openstack/chapters/chapter04:\
       containerised openstack services`
   * - vim.04
     - General
     - The Architecture **should** support Enhanced Platform Awareness (EPA)
       only for discovery of infrastructure resource capabilities.
     -
   * - vim.06
     - General
     - The Architecture **should** allow orchestration solutions to be integrated
       with VIM.
     -
   * - vim.09
     - General
     - The Architecture **should** support horizontal scaling of OpenStack core
       services.
     -

Interfaces and APIs Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Interfaces and APIs Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - int.acc.01
     - Acceleration
     - The Architecture **should** provide an open and standard acceleration
       interface to VNFs.
     -
   * - int.acc.02
     - Acceleration
     - The Architecture **should not** rely on SR-IOV PCI-Pass through for
       acceleration interface exposed to VNFs.”
     - duplicate of inf.acc.03 under "Infrastructure Recommendation"

Tenant Recommendations
~~~~~~~~~~~~~~~~~~~~~~

This section is left blank for future use.

.. list-table:: Tenant Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * -
     -
     -
     -

Operations and LCM Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: LCM Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - lcm.adp.01
     - Automated deployment
     - The Architecture **should** allow for cookie cutter automated
       deployment, configuration, provisioning and management of multiple
       Cloud Infrastructure sites.
     -
   * - lcm.adp.03
     - Automated deployment
     - The Architecture **should** support hitless upgrade of all software
       provided by the cloud provider that are not covered by lcm.adp.02.
       Whenever hitless upgrades are not feasible, attempt should be made
       to minimise the duration and nature of impact.
     -
   * - lcm.adp.04
     - Automated deployment
     - The Architecture **should** support declarative specifications of
       hardware and software assets for automated deployment, configuration,
       maintenance and management.
     -
   * - lcm.adp.05
     - Automated deployment
     - The Architecture **should** support automated process for Deployment
       and life-cycle management of VIM Instances.
     -
   * - lcm.cid.02
     - CI/CD
     - The Architecture **should** support integrating with CI/CD Toolchain
       for Cloud Infrastructure and VIM components Automation.
     -

Assurance Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Assurance Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - asr.mon.02
     - Monitoring
     - The Architecture **should** support Network Intelligence capabilities
       that allow richer diagnostic capabilities which take as input broader
       set of data across the network and from VNF workloads.
     -

Security Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~

System Hardening Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:system hardening`)

.. list-table:: System Hardening Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.gen.011
     - Hardening
     - The Cloud Infrastructure **should** support Read and Write only storage
       partitions (write only permission to one or more authorised actors).
     -
   * - sec.gen.014
     - Hardening
     - All servers part of Cloud Infrastructure **should** support measured
       boot and an attestation server that monitors the measurements of the
       servers.
     -

Platform and Access Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:platform and access`)

.. list-table:: Platform and Access Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.sys.014
     - Access
     - The Platform **should** use Linux Security Modules such as SELinux to
       control access to resources.
     -
   * - sec.sys.020
     - Access
     - The Cloud Infrastructure architecture **should** rely on Zero Trust
       principles to build a secure by design environment.
     - Zero Trust Architecture (ZTA) described in NIST SP 800-207

Confidentiality and Integrity Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:confidentiality and integrity`)

.. list-table:: Confidentiality and Integrity Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.ci.002
     - Confidentiality/Integrity
     - The Platform **should** support self-encrypting storage devices.
     -
   * - sec.ci.009
     - Confidentiality/Integrity
     - For sensitive data encryption, the key management service **should**
       leverage a Hardware Security Module to manage and protect cryptographic
       keys.
     -

Workload Security Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:workload security`)

.. list-table:: Workload Security Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.wl.007
     - Workload
     - The Operator **should** implement processes and tools to verify VNF
       authenticity and integrity.
     -

Image Security Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:image security`)

This section is left blank for future use.

.. list-table:: Image Security Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.img.009
     - Image
     - CIS Hardened Images **should** be used whenever possible.
     -
   * - sec.img.010
     - Image
     - Minimalist base images **should** be used whenever possible.
     -

Security LCM Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:security lcm`)

.. list-table:: LCM Security Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.lcm.004
     - LCM
     - The Cloud Operator **should** support automated templated approved
       changes; Templated approved changes for automation where available
     -

Monitoring and Security Audit Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source
:ref:`ref_model/chapters/chapter07:monitoring and security audit`)

The Platform is assumed to provide configurable alerting and
notification capability and the operator is assumed to have automated
systems, policies and procedures to act on alerts and notifications in a
timely fashion. In the following the monitoring and logging capabilities
can trigger alerts and notifications for appropriate action.

.. list-table:: Monitoring and Security Audit Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.mon.014
     - Monitoring
     - The Monitoring systems **should** not impact IaaS, PaaS, and SaaS SLAs
       including availability SLAs
     -
   * - sec.mon.016
     - Monitoring
     - The Platform Monitoring components **should** follow security best
       practices for auditing, including secure logging and tracing
     -

Open-Source Software Security Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:open source software`)

.. list-table:: Open-Source Software Security Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.oss.005
     - Software
     - A Software Bill of Materials (SBOM) **should** be provided or build,
       and maintained to identify the software components and their origins.
       Inventory of software components
     - `NTIA SBOM <https://www.ntia.gov/SBOM>`__

IaaC security Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source
:ref:`ref_model/chapters/chapter07:iaac - secure design and architecture stage requirements`)

**Secure Design and Architecture Stage**

.. list-table:: Reference Model Requirements: IaaC Security,
                Design and Architecture Stage
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.arch.001
     - IaaC
     - Threat Modelling methodologies and tools **should** be used during the
       Secure Design and Architecture stage triggered by Software Feature
       Design trigger. Methodology to identify and understand threats
       impacting a resource or set of resources.
     - It may be done manually or using tools like open source OWASP Threat
       Dragon
   * - sec.arch.002
     - IaaC
     - Security Control Baseline Assessment **should** be performed during the
       Secure Design and Architecture stage triggered by Software Feature
       Design trigger.
     - Typically done manually by internal or independent assessors.

**Secure Code Stage Recommendations**

.. list-table:: Reference Model Requirements: IaaC Security, Secure Code Stage
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.code.002
     - IaaC
     - SCA – Software Composition Analysis **should** be applied during
       Secure Coding stage triggered by Pull, Clone or Comment trigger.
       Security testing that analyses application source code or compiled code
       for software components with known vulnerabilities.
     - Example: open source OWASP range of tools.
   * - sec.code.003
     - IaaC
     - Source Code Review **should** be performed continuously during Secure
       Coding stage.
     - Typically done manually.
   * - sec.code.004
     - IaaC
     - Integrated SAST via IDE Plugins should be used during Secure Coding
       stage triggered by Developer Code trigger. On the local machine:
       through the IDE or integrated test suites; triggered on completion of
       coding by developer.
     -
   * - sec.code.005
     - IaaC
     - SAST of Source Code Repo **should** be performed during Secure Coding
       stage triggered by Developer Code trigger. Continuous delivery
       pre -deployment: scanning prior to deployment.
     -

**Continuous Build, Integration and Testing Stage Recommendations**

.. list-table:: Reference Model Requirements: IaaC Security, Continuous Build,
                Integration and Testing Stage
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.bld.001
     - IaaC
     - SAST -Static Application Security Testing **should** be applied during
       the Continuous Build, Integration and Testing stage triggered by Build
       and Integrate trigger.
     - Example: open source OWASP range of tools.
   * - sec.bld.002
     - IaaC
     - SCA – Software Composition Analysis **should** be applied during the
       Continuous Build, Integration and Testing stage triggered by Build and
       Integrate trigger.
     - Example: open source OWASP range of tools.
   * - sec.bld.004
     - IaaC
     - SDAST – Dynamic Application Security Testing **should** be applied
       during the Continuous Build, Integration and Testing stage triggered
       by Stage & Test trigger. Security testing that analyses a running
       application by exercising application functionality and detecting
       vulnerabilities based on application behaviour and response.
     - Example: OWASP ZAP.
   * - sec.bld.005
     - IaaC
     - Fuzzing **should** be applied during the Continuous Build, Integration
       and testing stage triggered by Stage & Test trigger. Fuzzing or fuzz
       testing is an automated software testing technique that involves
       providing invalid, unexpected, or random data as inputs to a computer
       program.
     - Example: GitLab Open Sources Protocol Fuzzer Community Edition.
   * - sec.bld.006
     - IaaC
     - IAST – Interactive Application Security Testing **should** be applied
       during the Continuous Build, Integration and Testing stage triggered by
       Stage & Test trigger. Software component deployed with an application
       that assesses application behaviour and detects presence of
       vulnerabilities on an application being exercised in realistic testing
       scenarios.
     - Example: Contrast Community Edition.

**Continuous Delivery and Deployment Stage Recommendations**

.. list-table:: Reference Model Requirements: IaaC Security, Continuous
                Delivery and Deployment Stage
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.del.003
     - IaaC
     - Artifact and Image Repository Scan **should** be continuously applied
       during the Continuous Delivery and Deployment stage.
     - Example: GitLab uses the open source Clair engine for container
       scanning.

**Runtime Defence and Monitoring Recommendations**

.. list-table:: Reference Model Requirements: Iaac Security, Runtime Defence
                and Monitoring Stage
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.run.002
     - IaaC
     - RASP – Runtime Application Self-Protection **should** be continuously
       applied during the Runtime Defence and Monitoring stage. Security
       technology deployed within the target application in production for
       detecting, alerting, and blocking attacks.
     -
   * - sec.run.003
     - IaaC
     - Application testing and Fuzzing **should** be continuously applied
       during the Runtime Defence and Monitoring stage. Fuzzing or fuzz
       testing is an automated software testing technique that involves
       providing invalid, unexpected, or random data as inputs to a computer
       program.
     - Example: GitLab Open Sources Protocol Fuzzer Community Edition.
   * - sec.run.004
     - IaaC
     - Penetration Testing **should** be continuously applied during the
       Runtime Defence and Monitoring stage.
     - Typically done manually.

Compliance with Standards Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(source :ref:`ref_model/chapters/chapter07:compliance with standards`)

.. list-table:: Compliance with Security Recommendations
   :widths: 15 15 40 30
   :header-rows: 1

   * - Reference
     - sub-category
     - Description
     - Notes
   * - sec.std.001
     - Standards
     - The Cloud Operator **should** comply with `Center for Internet Security
       CIS Controls <https://www.cisecurity.org/>`__
     -
   * - sec.std.002
     - Standards
     - The Cloud Operator, Platform and Workloads **should** follow the
       guidance in the CSA Security Guidance for Critical Areas of Focus in
       Cloud Computing (latest version)- CSA, `Cloud Security Alliance
       <https://cloudsecurityalliance.org/>`__
     -
   * - sec.std.003
     - Standards
     - The Platform and Workloads **should** follow the guidance in the
       `OWASP Cheat Sheet Series (OCSS)
       <https://github.com/OWASP/CheatSheetSeries>`__ - OWASP, `Open Web
       Application Security Project <https://www.owasp.org>`__
     -
   * - sec.std.004
     - Standards
     - The Cloud Operator, Platform and Workloads **should** ensure that their
       code is not vulnerable to the `OWASP Top Ten Security Risks
       <https://owasp.org/www-project-top-ten/>`__
     -
   * - sec.std.005
     - Standards
     - The Cloud Operator, Platform and Workloads **should** strive to improve
       their maturity on the `OWASP Software Maturity Model (SAMM)
       <https://owaspsamm.org/blog/2019/12/20/version2-community-release/>`__
     -
   * - sec.std.006
     - Standards
     - The Cloud Operator, Platform and Workloads should utilise the
       `OWASP Web Security Testing Guide
       <https://github.com/OWASP/wstg/tree/master/document>`__
     -
   * - sec.std.007
     - Standards
     - The Cloud Operator, and Platform **should** satisfy the requirements
       for Information Management Systems specified in `ISO/IEC 27001
       <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>`__;
       ISO/IEC 27001 is the international Standard for best-practice
       information security management systems (ISMSs)
     -
   * - sec.std.008
     - Standards
     - The Cloud Operator, and Platform **should** implement the Code of
       practice for Security Controls specified
       `ISO/IEC 27002:2013 (or latest)
       <https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en>`__
     -
   * - sec.std.009
     - Standards
     - The Cloud Operator, and Platform **should** implement the
       `ISO/IEC 27032:2012 (or latest) Guidelines for Cybersecurity techniques
       <https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en>`__;
       ISO/IEC 27032 is the international Standard focusing explicitly on
       cybersecurity
     -
   * - sec.std.010
     - Standards
     - The Cloud Operator **should** conform to the ISO/IEC 27035 standard for
       incidence management; ISO/IEC 27035 is the international Standard for
       incident management
     -
   * - sec.std.011
     - Standards
     - The Cloud Operator **should** conform to the ISO/IEC 27031 standard for
       business continuity; ISO/IEC 27031 - ISO/IEC 27031 is the international
       Standard for ICT readiness for business continuity
     -
