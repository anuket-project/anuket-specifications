Introduction
============

Overview
--------

This Reference Architecture is focussed on OpenStack as the Virtualised
Infrastructure Manager (VIM) chosen based on the criteria laid out in
the Reference Model :doc:`ref_model:chapters/chapter01`.
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
managed through the existing project communities’ processes to add and
validate the required features through well-established mechanisms.

Vision
~~~~~~

The OpenStack-based Reference Architecture will host NFV
workloads, primarily VNFs (Virtual Network Functions),
of interest to the Anuket community. The
Reference Architecture document can be used by operators to deploy
Anuket conformant infrastructure; hereafter, “conformant” denotes that
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
   session’s usage multiplied by the expected number of concurrent
   sessions with overhead.

-  **Network functions**: Network functions is a broad category but
   encompasses workloads that support the exchange of information (data,
   voice, multi-media) over a system’s network. Some of these workloads
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
all of the mandatory (“must”) requirements and the most useful of the
other optional (“should”) requirements. Chapter 3 and 4 cover the Cloud
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

.. glossary::

    Cloud Infrastructure
      A generic term covering **NFVI**, **IaaS** and **CaaS** capabilities -
      essentially the infrastructure on which a **Workload** can be executed.

.. note::

  `The official OpenStack Glossary <https://docs.openstack.org/image-guide/common/glossary.html>`__
  is an extensive list of OpenStack-related concepts. Some additional terms
  used in the Reference Architecture RA-1 or used to relate RA-1 terms with
  terms defined elsewhere.


.. glossary::

    Core (physical)
      An independent computer processing unit that can independently execute
      CPU instructions and is integrated with other cores on a multiprocessor
      (chip, integrated circuit die). Please note that the multiprocessor chip
      is also referred to as a CPU that is placed in a socket of a computer
      motherboard.

    Flavor Capability
      The capability of the Cloud Infrastructure Profile, such as CPU Pinning,
      NUMA or huge pages.

    Flavor Geometry

      Flavor sizing such as number of vCPUs, RAM, disk, etc.

    Huge pages
      Physical memory is partitioned and accessed using the basic page unit (in
      Linux default size of 4 KB). Huge pages, typically 2 MB and 1GB size,
      allows large amounts of memory to be utilised with reduced overhead. In
      an NFV environment, huge pages are critical to support large memory pool
      allocation for data packet buffers. This results in fewer Translation
      Lookaside Buffers (TLB) lookups, which reduces the virtual to physical
      pages address translations. Without huge pages enabled high TLB miss
      rates would occur thereby degrading performance.

    Server

      For the OpenStack Compute API, a server is a virtual machine (VM), a
      physical machine (bare metal) or a container.

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
