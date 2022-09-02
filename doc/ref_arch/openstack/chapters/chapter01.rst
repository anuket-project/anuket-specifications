Introduction
============

Overview
--------

This Reference Architecture is focussed on OpenStack as the Virtualised
Infrastructure Manager (VIM) chosen based on the criteria laid out in
the Cloud Infrastructure Reference Model :cite:p:`refmodel`
(referred to as "Reference Model" or "RM" in the document).
OpenStack :cite:p:`openstack` has the advantage of being a
mature and widely accepted open-source technology; a strong ecosystem of
vendors that support it, the OpenInfra Foundation for managing the
community, and, most importantly, it is widely deployed by the global
operator community for both internal infrastructure and external facing
products and services. This means that the operators have existing staff
with the right skill sets to support a Cloud Infrastructure
(or Network Function Virtualisation Infrastructure,
NFVI :cite:p:`etsinfvinf`)
deployment into development, test and production. Another reason to
choose OpenStack is that it has a large active community of vendors and
operators, which means that any code or component changes needed to
support the Common Telco Cloud Infrastructure requirements can be
managed through the existing project communities' processes to add and
validate the required features through well-established mechanisms.

Vision
~~~~~~

The OpenStack-based Reference Architecture will host NFV
workloads, primarily VNFs (Virtual Network Functions),
of interest to the Anuket community. The
Reference Architecture document can be used by operators to deploy
Anuket conformant infrastructure; hereafter, "conformant" denotes that
the resource can satisfy tests conducted to verify conformance with this
reference architecture.

Use Cases
---------

Several NFV use cases are documented in OpenStack. For more examples and
details refer to the OpenStack Use cases :cite:p:`openstackuc`.

Examples include:

-  **Overlay networks**: The overlay functionality design includes
   OpenStack Networking in Open vSwitch :cite:p:`ovs`
   GRE tunnel mode. In this
   case, the layer-3 external routers pair with VRRP, and switches pair
   with an implementation of MLAG to ensure that you do not lose
   connectivity with the upstream routing infrastructure.

-  **Performance tuning**: Network level tuning for this workload is
   minimal. Quality of Service (QoS) applies to these workloads for a
   middle ground Class Selector depending on existing policies. It is
   higher than a best effort queue but lower than an Expedited
   Forwarding or Assured Forwarding queue. Since this type of
   application generates larger packets with longer-lived connections,
   you can optimize bandwidth utilization for long duration TCP. Normal
   bandwidth planning applies here with regards to benchmarking a
   session's usage multiplied by the expected number of concurrent
   sessions with overhead.

-  **Network functions**: Network functions is a broad category but
   encompasses workloads that support the exchange of information (data,
   voice, multi-media) over a system's network. Some of these workloads
   tend to consist of a large number of small-sized packets that are
   short lived, such as DNS queries or SNMP traps. These messages need
   to arrive quickly and, thus, do not handle packet loss. Network
   function workloads have requirements that may affect configurations
   including at the hypervisor level. For an application that generates
   10 TCP sessions per user with an average bandwidth of 512 kilobytes
   per second per flow and expected user count of ten thousand (10,000)
   concurrent users, the expected bandwidth plan is approximately 4.88
   gigabits per second. The supporting network for this type of
   configuration needs to have a low latency and evenly distributed load
   across the topology. These types of workload benefit from having
   services local to the consumers of the service. Thus, use a
   multi-site approach, as well as, deploying many copies of the
   application to handle load as close as possible to consumers. Since
   these applications function independently, they do not warrant
   running overlays to interconnect tenant networks. Overlays also have
   the drawback of performing poorly with rapid flow setup and may incur
   too much overhead with large quantities of small packets and
   therefore we do not recommend them. QoS is desirable for some
   workloads to ensure delivery. DNS has a major impact on the load
   times of other services and needs to be reliable and provide rapid
   responses. Configure rules in upstream devices to apply a
   higher-Class Selector to DNS to ensure faster delivery or a better
   spot in queuing algorithms.

OpenStack Reference Release
---------------------------

This Reference Architecture document conforms to the OpenStack
Wallaby :cite:p:`wallaby` release.
While many features and capabilities are conformant with many OpenStack
releases, this document will refer to features, capabilities and APIs
that are part of the OpenStack Wallaby release. For ease, this
Reference Architecture document version can be referred to as "RA-1 OSTK
Wallaby."

Principles
----------

OpenStack Reference Architecture must obey to the following set of
principles described in:

- :ref:`cntt:common/chapter00:anuket general principles`
- :ref:`cntt:common/chapter00:architectural principles`

OpenStack specific principles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenStack considers the following Four Opens essential for success:

-  Open Source
-  Open Design
-  Open Development
-  Open Community

This OpenStack Reference Architecture is organised around the three
major Cloud Infrastructure resource types as core services of compute,
storage and networking, and a set of shared services of identity
management, image management, graphical user interface, orchestration
engine, etc.

Document Organisation
---------------------

Chapter 2 defines the Reference Architecture requirements and, when
appropriate, provides references to where these requirements are
addressed in this document. The intent of this document is to address
all of the mandatory ("must") requirements and the most useful of the
other optional ("should") requirements. Chapter 3 and 4 cover the Cloud
Infrastructure resources and the core OpenStack services, while the APIs
are covered in Chapter 5. Chapter 6 covers the implementation and
enforcement of security capabilities and controls. Life Cycle Management
of the Cloud Infrastructure and VIM are covered in Chapter 7 with stress
on Logging, Monitoring and Analytics (LMA), configuration management and
some other operational items. Please note that Chapter 7 is not a
replacement for the implementation, configuration and operational
documentation that accompanies the different OpenStack distributions.
Chapter 8 identifies certain Gaps that currently exist and plans on how
to address them (for example, resources autoscaling).

Terminology
-----------

**Abstraction:** Process of removing concrete, fine-grained or
lower-level details or attributes or common properties in the study of
systems to focus attention on topics of greater importance or general
concepts. It can be the result of decoupling.

**Anuket:** A LFN open-source project developing open reference
infrastructure models, architectures, tools, and programs.

**Cloud Infrastructure:** A generic term covering **NFVI**, **IaaS** and
**CaaS** capabilities - essentially the infrastructure on which a
**Workload** can be executed.
**NFVI**, **IaaS** and **CaaS** layers can be built on top of each
other. In case of CaaS some cloud infrastructure features (e.g.: HW
management or multitenancy) are implemented by using an underlying
**IaaS** layer.

**Cloud Infrastructure Hardware Profile:** defines the behaviour,
capabilities, configuration, and metrics provided by a cloud
infrastructure hardware layer resources available for the workloads.

**Host Profile:** is another term for a Cloud Infrastructure Hardware
Profile.

**Cloud Infrastructure Profile:** The combination of the Cloud
Infrastructure Software Profile and the Cloud Infrastructure Hardware
Profile that defines the capabilities and configuration of the Cloud
Infrastructure resources available for the workloads.

**Cloud Infrastructure Software Profile:** defines the behaviour,
capabilities and metrics provided by a Cloud Infrastructure Software
Layer on resources available for the workloads.

**Cloud Native Network Function (CNF):** A cloud native network function
(CNF) is a cloud native application that implements network
functionality. A CNF consists of one or more microservices. All layers
of a CNF are developed using Cloud Native Principles including immutable
infrastructure, declarative APIs, and a “repeatable deployment process”.
This definition is derived from the Cloud Native Thinking for
Telecommunications Whitepaper, which also includes further detail
and examples.

**Compute Node:** An abstract definition of a server.
A compute node can refer to a set of hardware and software that
support the VMs or Containers running on it.

**Container:** A lightweight and portable executable image that contains
software and all of its dependencies.
OCI defines **Container** as "An environment for executing
processes with configurable isolation and resource limitations. For
example, namespaces, resource limits, and mounts are all part of the
container environment." A **Container** provides operating-system-level
virtualisation by abstracting the “user space”. One big difference
between **Containers** and **VMs** is that unlike VMs, where each **VM**
is self-contained with all the operating systems components are within
the **VM** package, containers "share" the host system’s kernel with
other containers.

**Container Image:** Stored instance of a container that holds a set of
software needed to run an application.

**Core (physical):** An independent computer processing unit that can
independently execute CPU instructions and is integrated with other
cores on a multiprocessor (chip, integrated circuit die). Please note
that the multiprocessor chip is also referred to as a CPU that is placed
in a socket of a computer motherboard.

**CPU Type:** A classification of CPUs by features needed for the
execution of computer programs; for example, instruction sets, cache
size, number of cores.

**Decoupling, Loose Coupling:** Loosely coupled system is one in which
each of its components has, or makes use of, little or no knowledge of
the implementation details of other separate components. Loose coupling
is the opposite of tight coupling

**Encapsulation:** Restricting of direct access to some of an object's
components.

**External Network:** External networks provide network connectivity for
a cloud infrastructure tenant to resources outside of the tenant space.

**Fluentd:** An open-source data collector for unified
logging layer, which allows data collection and consumption for better
use and understanding of data. **Fluentd** is a CNCF graduated project.

**Functest:** An open-source project part of Anuket LFN project.
It addresses functional testing with a collection of state-of-the-art
virtual infrastructure test suites, including automatic VNF testing.

**Hardware resources:** Compute/Storage/Network hardware resources on
which the cloud infrastructure platform software, virtual machines and
containers run on.

**Huge pages:** Physical memory is partitioned and accessed using the
basic page unit (in Linux default size of 4 KB). Hugepages, typically 2
MB and 1GB size, allows large amounts of memory to be utilised with
reduced overhead. In an NFV environment, huge pages are critical to
support large memory pool allocation for data packet buffers. This
results in fewer Translation Lookaside Buffers (TLB) lookups, which
reduces the virtual to physical pages’ address translations. Without
huge pages enabled high TLB miss rates would occur thereby degrading
performance.

**Hypervisor:** a software that abstracts and isolates workloads with
their own operating systems from the underlying physical resources. Also
known as a virtual machine monitor (VMM).

**Instance:** is a virtual compute resource, in a known state such as
running or suspended, that can be used like a physical server.
It can be used to specify VM Instance or Container Instance.

**Kibana:** An open-source data visualisation system.

**Kubernetes:** An open-source system for automating deployment, scaling,
and management of containerised applications.

**Monitoring (Capability):** Monitoring capabilities are used for the
passive observation of workload-specific traffic traversing the Cloud
Infrastructure. Note, as with all capabilities, Monitoring may be
unavailable or intentionally disabled for security reasons in a given
cloud infrastructure instance.

**Multi-tenancy:** feature where physical, virtual or service resources
are allocated in such a way that multiple tenants and their computations
and data are isolated from and inaccessible by each other.

**Network Function (NF):** functional block or application that has
well-defined external interfaces and well-defined functional behaviour.
Within **NFV**, a **Network Function** is implemented in a form of
**Virtualised NF** (VNF) or a **Cloud Native NF** (CNF).

**NFV Orchestrator (NFVO):** Manages the VNF lifecycle and **Cloud
Infrastructure** resources (supported by the **VIM**) to ensure an
optimised allocation of the necessary resources and connectivity.

**Network Function Virtualisation (NFV):** The concept of separating
network functions from the hardware they run on by using a virtual
hardware abstraction layer.

**Network Function Virtualisation Infrastructure (NFVI):** The totality
of all hardware and software components used to build the environment in
which a set of virtual applications (VAs) are deployed; also referred to
as cloud infrastructure.
The NFVI can span across many locations, e.g., places where data
centres or edge nodes are operated. The network providing connectivity
between these locations is regarded to be part of the cloud
infrastructure. **NFVI** and **VNF** are the top-level conceptual
entities in the scope of Network Function Virtualisation. All other
components are sub-entities of these two main entities.

**Network Service (NS):** composition of **Network Function**\ (s)
and/or **Network Service**\ (s), defined by its functional and
behavioural specification, including the service lifecycle.

**Open Network Automation Platform (ONAP):** A LFN project developing a
comprehensive platform for orchestration, management, and automation
of network and edge computing services for network operators,
cloud providers, and enterprises.

**ONAP OpenLab:** ONAP community lab.

**Open Platform for NFV (OPNFV):** A collaborative project under
the Linux Foundation. OPNFV is now part of the LFN Anuket project.
It aims to implement, test, and deploy tools for conformance and
performance of NFV infrastructure.

**OPNFV Verification Program (OVP):** An open-source,
community-led compliance and verification program aiming to demonstrate
the readiness and availability of commercial NFV products and services
using OPNFV and ONAP components.

**Platform:** A cloud capabilities type in which the cloud service user
can deploy, manage and run customer-created or customer-acquired
applications using one or more programming languages and one or more
execution environments supported by the cloud service provider. Adapted
from ITU-T Y.3500.
This includes the physical infrastructure, Operating Systems,
virtualisation/containerisation software and other orchestration,
security, monitoring/logging and life-cycle management software.

**Prometheus:** An open-source monitoring and alerting system.

**Quota:** An imposed upper limit on specific types of resources,
usually used to prevent excessive resource consumption by a given
consumer (tenant, VM, container).

**Resource pool:** A logical grouping of cloud infrastructure hardware
and software resources. A resource pool can be based on a certain
resource type (for example, compute, storage and network) or a
combination of resource types. A **Cloud Infrastructure** resource can
be part of none, one or more resource pools.

**Simultaneous Multithreading (SMT):** Simultaneous multithreading (SMT)
is a technique for improving the overall efficiency of superscalar CPUs
with hardware multithreading. SMT permits multiple independent threads
of execution on a single core to better utilise the resources provided
by modern processor architectures.

**Shaker:** A distributed data-plane testing tool built for OpenStack.

**Software Defined Storage (SDS):** An architecture which consists of
the storage software that is independent from the underlying storage
hardware. The storage access software provides data request interfaces
(APIs) and the SDS controller software provides storage access services
and networking.

**Tenant:** cloud service users sharing access to a set of physical and
virtual resources, ITU-T Y.3500.
Tenants represent an independently manageable logical pool of
compute, storage and network resources abstracted from physical
hardware.

**Tenant Instance:** refers to an Instance owned by or dedicated for use by a single **Tenant**.

**Tenant (Internal) Networks:** Virtual networks that are internal to
**Tenant Instances**.

**User**: Natural person, or entity acting on their behalf, associated
with a cloud service customer that uses cloud services.
Examples of such entities include devices and applications.

**Virtual CPU (vCPU):** Represents a portion of the host's computing
resources allocated to a virtualised resource, for example, to a virtual
machine or a container. One or more vCPUs can be assigned to a
virtualised resource.

**Virtualised Infrastructure Manager (VIM):** Responsible for
controlling and managing the Network Function Virtualisation
Infrastructure (NFVI) compute, storage and network resources.

**Virtual Machine (VM):** virtualised computation environment that
behaves like a physical computer/server.
A **VM** consists of all of the components (processor (CPU),
memory, storage, interfaces/ports, etc.) of a physical computer/server.
It is created using sizing information or Compute Flavour.

**Virtualised Network Function (VNF):** A software implementation of a
Network Function, capable of running on the Cloud Infrastructure.
**VNFs** are built from one or more VNF Components (VNFC) and, in most
cases, the VNFC is hosted on a single VM or Container.

**Virtual Compute resource (a.k.a. virtualisation container):**
partition of a compute node that provides an isolated virtualised
computation environment.

**Virtual Storage resource:** virtualised non-volatile storage allocated
to a virtualised computation environment hosting a **VNFC**.

**Virtual Networking resource:** routes information among the network
interfaces of a virtual compute resource and physical network
interfaces, providing the necessary connectivity.

**VMTP:** A data path performance measurement tool built specifically
for OpenStack clouds.

**Workload:** an application (for example **VNF**, or **CNF**) that
performs certain task(s) for the users. In the Cloud Infrastructure,
these applications run on top of compute resources such as **VMs** or
**Containers**.

Abbreviations
-------------

.. list-table::
   :widths: 20 60
   :header-rows: 1

   * - Abbreviation/Acronym
     - Definition
   * - API
     - Application Programming Interface
   * - CPU
     - Central Processing Unit
   * - DNS
     - Domain Name System
   * - DPDK
     - Data Plane Development Kit
   * - ECMP
     - Equal Cost Multi-Path routing
   * - ETSI
     - European Telecommunications Standards Institute
   * - FPGA
     - Field Programmable Gate Array
   * - MB/GB/TB
     - MegaByte/GigaByte/TeraByte
   * - GPU
     - Graphics Processing Unit
   * - GRE
     - Generic Routing Encapsulation
   * - GSM
     - Global System for Mobile Communications (originally Groupe Spécial Mobile)
   * - GSMA
     - GSM Association
   * - GSLB
     - Global Service Load Balancer
   * - GUI
     - Graphical User Interface
   * - HA
     - High Availability
   * - HDD
     - Hard Disk Drive
   * - HTTP
     - HyperText Transfer Protocol
   * - HW
     - Hardware
   * - IaaC (also IaC)
     - Infrastructure as a Code
   * - IaaS
     - Infrastructure as a Service
   * - ICMP
     - Internet Control Message Protocol
   * - IO
     - Input/Output
   * - IOPS
     - Input/Output per Second
   * - IPMI
     - Intelligent Platform Management Interface
   * - KVM
     - Kernel-based Virtual Machine
   * - LCM
     - LifeCycle Management
   * - LDAP
     - Lightweight Directory Access Protocol
   * - LFN
     - Linux Foundation Networking
   * - LMA
     - Logging, Monitoring and Analytics
   * - LVM
     - Logical Volume Management
   * - MANO
     - Management ANd Orchestration
   * - MLAG
     - Multi-chassis Link Aggregation Group
   * - NAT
     - Network Address Translation
   * - NFS
     - Network File System
   * - NFV
     - Network Function Virtualisation
   * - NFVI
     - Network Function Virtualisation Infrastructure
   * - NIC
     - Network Interface Card
   * - NPU
     - Numeric Processing Unit
   * - NTP
     - Network Time Protocol
   * - NUMA
     - Non-Uniform Memory Access
   * - OS
     - Operating System
   * - OSTK
     - OpenStack
   * - OVS
     - Open vSwitch
   * - OWASP
     - Open Web Application Security Project
   * - PCIe
     - Peripheral Component Interconnect Express
   * - PCI-PT
     - PCIe PassThrough
   * - PXE
     - Preboot Execution Environment
   * - QoS
     - Quality of Service
   * - RA
     - Reference Architecture
   * - RA-1
     - Reference Architecture 1 (i.e., Reference Architecture for OpenStack-based Cloud Infrastructure)
   * - RBAC
     - Role-based Access Control
   * - RBD
     - RADOS Block Device
   * - REST
     - Representational state transfer
   * - RI
     - Reference Implementation
   * - RM
     - Reference Model
   * - SAST
     - Static Application Security Testing
   * - SDN
     - Software Defined Networking
   * - SFC
     - Service Function Chaining
   * - SLA
     - Service Level Agreement
   * - SMP
     - Symmetric MultiProcessing
   * - SMT
     - Simultaneous MultiThreading
   * - SNAT
     - Source Network Address Translation
   * - SNMP
     - Simple Network Management Protocol
   * - SR-IOV
     - Single Root Input Output Virtualisation
   * - SSD
     - Solid State Drive
   * - SSL
     - Secure Sockets Layer
   * - TCP
     - Transmission Control Protocol
   * - TLS
     - Transport Layer Security
   * - ToR
     - Top of Rack
   * - TPM
     - Trusted Platform Module
   * - VIM
     - Virtualised Infrastructure Manager
   * - VLAN
     - Virtual LAN
   * - VM
     - Virtual Machine
   * - VNF
     - Virtual Network Function
   * - VRRP
     - Virtual Router Redundancy Protocol
   * - VTEP
     - VXLAN Tunnel End Point
   * - VXLAN
     - Virtual Extensible LAN
   * - WAN
     - Wide Area Network
   * - ZTA
     - Zero Trust Architecture

Conventions
-----------

The key words "must", "must not", "required", "shall", "shall not",
"should", "should not", "recommended", "may", and "optional"
in this document are to be interpreted as described in
RFC 2119 :cite:p:`rfc2119`.

References
----------

.. bibliography::
   :cited:
