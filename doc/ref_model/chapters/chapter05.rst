Feature set and Requirements from Infrastructure
================================================

A profile :ref:`chapters/chapter02:profiles, profile extensions & flavours` specifies the configuration of a
Cloud Infrastructure node (host or server); :ref:`chapters/chapter02:profile extensions (specialisations)`
may specify additional configuration. Workloads utilise profiles to describe the configuration of nodes on which they
can be hosted to execute on. Workload Flavours provide a mechanism to specify the VM or Pod sizing information to host
the workload. Depending on the requirements of the workloads, a VM or a Pod will be deployed as per the specified
Flavour information on a node configured as per the specified Profile. Not only do the nodes (the hardware) have to be
configured but some of the capabilities also need to be configured in the software layers (such as Operating System and
Virtualisation Software). Thus, a Profile can be defined in terms of configuration needed in the software layers, the
Cloud Infrastructure Software Profile, and the hardware, the Cloud Infrastructure Hardware Profile.

Cloud Infrastructure Software profile description
-------------------------------------------------

Cloud Infrastructure Software layer is composed of 2 layers, :numref:`Cloud Infrastructure software layers`:

-  The virtualisation Infrastructure layer, which is based on hypervisor virtualisation technology or container-based
   virtualisation technology. Container virtualisation can be nested in hypervisor-based virtualisation
-  The host OS layer

.. figure:: ../figures/ch05-cloud-infrastructure-sw-profile-layers.png
   :name: Cloud Infrastructure software layers
   :alt: Cloud Infrastructure software layers

   Cloud Infrastructure software layers

+--------------+----------------+---------+-------------------------------------------------------------+--------------+
| Ref          | Cloud          | Type    | Definition/Notes                                            | Capabilities |
|              | Infrastructure |         |                                                             | Reference    |
|              | Software       |         |                                                             | (1)          |
+==============+================+=========+=============================================================+==============+
| infra.sw.001 | Host Operating | <value> | Values such as Ubuntu20.04, Windows 10 Release #, etc.      | e.cap.021    |
|              | System         |         |                                                             |              |
+--------------+----------------+---------+-------------------------------------------------------------+--------------+
| infra.sw.002 | Virtualisation | <value> | Values such as KVM, Hyper-V, Kubernetes, etc.               | e.cap.022    |
|              | Infrastructure |         |                                                             |              |
|              | Layer          |         |                                                             |              |
+--------------+----------------+---------+-------------------------------------------------------------+--------------+

..

   (1) Reference to the capabilities defined in
   :ref:`chapters/chapter04:infrastructure capabilities, measurements and catalogue`.

For a host (compute node or physical server), the virtualisation layer is an abstraction layer between hardware
components (compute, storage, and network resources) and virtual resources allocated to a VM or a Pod.
:numref:`Cloud Infrastructure Virtual resources` represents the virtual resources (virtual compute, virtual network, and
virtual storage) allocated to a VM or a Pod and managed by the Cloud Infrastructure Manager.

.. figure:: ../figures/ch05_b_ref_profile.png
   :name: Cloud Infrastructure Virtual resources
   :alt: Cloud Infrastructure Virtual resources

   Cloud Infrastructure Virtual resources

A Cloud Infrastructure Software Profile is a set of features, capabilities, and metrics offered by a Cloud
Infrastructure software layer and configured in the software layers (the Operating System (OS) and the virtualisation
software (such as hypervisor)). :numref:`Cloud Infrastructure Software Profiles` depicts a high level view of the Basic
and High Performance Cloud Infrastructure Profiles.

.. figure:: ../figures/RM-ch05-sw-profile.png
   :name: Cloud Infrastructure Software Profiles
   :alt: Cloud Infrastructure Software Profiles

   Cloud Infrastructure Software Profiles

The following sections detail the Cloud Infrastructure Software Profile capabilities per type of virtual resource.

Virtual Compute Profiles
~~~~~~~~~~~~~~~~~~~~~~~~

**Table 5-1** and **Table 5-2** depict the features related to virtual compute.

+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| Reference         | Feature              | Type            | Description                              | Capabilities |
|                   |                      |                 |                                          | Reference    |
+===================+======================+=================+==========================================+==============+
| infra.com.cfg.001 | CPU allocation ratio | <value>         | Number of virtual cores per physical     | i.cap.016    |
|                   |                      |                 | core.                                    |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.cfg.002 | NUMA alignment       | Yes/No          | Support of NUMA at the Host OS and       | e.cap.007    |
|                   |                      |                 | virtualisation layers, in addition to    |              |
|                   |                      |                 | hardware.                                |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.cfg.003 | CPU pinning          | Yes/No          | Binds a vCPU to a physical core or SMT   | e.cap.006    |
|                   |                      |                 | thread. Configured in OS and             |              |
|                   |                      |                 | virtualisation layers.                   |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.cfg.004 | Huge pages           | Yes/No          | Ability to manage huge pages of memory.  | i.cap.018    |
|                   |                      |                 | Configured in OS and virtualisation      |              |
|                   |                      |                 | layers.                                  |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.cfg.005 | Simultaneous         | Yes/No/Optional | Allows multiple execution threads to be  | e.cap.018    |
|                   | Multithreading (SMT) |                 | executed on a single physical CPU core.  |              |
|                   |                      |                 | Configured in OS, in addition to the     |              |
|                   |                      |                 | hardware.                                |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+

**Table 5-1:** Virtual Compute features.

+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| Reference         | Feature              | Type            | Description                              | Capabilities |
|                   |                      |                 |                                          | Reference    |
+===================+======================+=================+==========================================+==============+
| infra.com.acc.cfg | IPSec Acceleration   | Yes/No/Optional | IPSec Acceleration                       | e.cap.008    |
| .001              |                      |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.acc.cfg | Transcoding          | Yes/No/Optional | Transcoding Acceleration                 | e.cap.010    |
| .002              | Acceleration         |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.acc.cfg | Programmable         | Yes/No/Optional | Programmable Acceleration                | e.cap.011    |
| .003              | Acceleration         |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.acc.cfg | GPU                  | Yes/No/Optional | Hardware coprocessor                     | e.cap.014    |
| .004              |                      |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.acc.cfg | FPGA/other           | Yes/No/Optional | Non-specific hardware. These             | e.cap.016    |
| .005              | Acceleration H/W     |                 | Capabilities generally require           |              |
|                   |                      |                 | hardware-dependent drivers be injected   |              |
|                   |                      |                 | into workloads.                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+

**Table 5-2:** Virtual Compute Acceleration features.

Virtual Storage Profiles
~~~~~~~~~~~~~~~~~~~~~~~~

**Table 5-3** and **Table 5-4** depict the features related to virtual storage.

================= ======================== ====== ===================================================
Reference         Feature                  Type   Description
================= ======================== ====== ===================================================
infra.stg.cfg.001 Catalogue Storage Types  Yes/No Support of Storage types described in the catalogue
infra.stg.cfg.002 Storage Block            Yes/No
infra.stg.cfg.003 Storage with replication Yes/No
infra.stg.cfg.004 Storage with encryption  Yes/No
================= ======================== ====== ===================================================

**Table 5-3:** Virtual Storage features.

===================== ========================= ====== ===========
Reference             Feature                   Type   Description
===================== ========================= ====== ===========
infra.stg.acc.cfg.001 Storage IOPS oriented     Yes/No
infra.stg.acc.cfg.002 Storage capacity oriented Yes/No
===================== ========================= ====== ===========

**Table 5-4:** Virtual Storage Acceleration features.

Virtual Networking Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Table 5-5** and **Table 5-6** depict the features related to virtual networking.

+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| Reference         | Feature              | Type            | Description                              | Capabilities |
|                   |                      |                 |                                          | Reference    |
+===================+======================+=================+==========================================+==============+
| infra.net.cfg.001 | Connection Point     |IO virtualisation|  eg. virtio1.1                           |              |
|                   | interface IO         |                 |                                          |              |
|                   | virtualisation       |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.002 | Overlay protocol     | Protocols       | The overlay network encapsulation        |              |
|                   |                      |                 | protocol needs to enable ECMP in the     |              |
|                   |                      |                 | underlay to take advantage of the        |              |
|                   |                      |                 | scale-out features of the network        |              |
|                   |                      |                 | fabric.                                  |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.003 | NAT                  | Yes/No          | Support of Network Address Translation   |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.004 | Security Groups      | Yes/No          | Set of rules managing incoming and       |              |
|                   |                      |                 | outgoing network traffic                 |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.005 | Service Function     | Yes/No          | Support of Service Function Chaining     |              |
|                   | Chaining             |                 | (SFC)                                    |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.006 | Traffic patterns     | Yes/No          | Traffic patterns should be optimal, in   |              |
|                   | symmetry             |                 | terms of packet flow. North-south        |              |
|                   |                      |                 | traffic shall not be concentrated in     |              |
|                   |                      |                 | specific elements in the architecture,   |              |
|                   |                      |                 | making those critical choke-points,      |              |
|                   |                      |                 | unless strictly necessary (i.e. when NAT |              |
|                   |                      |                 | 1:many is required).                     |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+

**Table 5-5:** Virtual Networking features.

===================== ============================= ========================== =========== ======================
Reference             Feature                       Type                       Description Capabilities Reference
===================== ============================= ========================== =========== ======================
infra.net.acc.cfg.001 vSwitch optimisation          Yes/No and SW Optimisation e.g. DPDK.  ``e.cap.019``
infra.net.acc.cfg.002 SmartNIC (for HW Offload)     Yes/No                     HW Offload  ``e.cap.015``
infra.net.acc.cfg.003 Crypto acceleration           Yes/No                                 ``e.cap.009``
infra.net.acc.cfg.004 Crypto Acceleration Interface Yes/No
===================== ============================= ========================== =========== ======================

**Table 5-6:** Virtual Networking Acceleration features.

Security
~~~~~~~~

See Chapter 7 Security.

Platform Services
~~~~~~~~~~~~~~~~~

This section details the services that may be made available to workloads by the Cloud Infrastructure.

================= ============== ====== ==========================================
Reference         Feature        Type   Description
================= ============== ====== ==========================================
infra.svc.stg.001 Object Storage Yes/No Object Storage Service (e.g S3-compatible)
================= ============== ====== ==========================================

**Table 5-7:** Cloud Infrastructure Platform services.

+--------------------------------------+-------------------------------------------------------------------------------+
| Platform Service Category            | Platform Service Examples                                                     |
+======================================+===============================================================================+
| Data Stores/Databases                | Ceph, etcd, MongoDB, Redis                                                    |
+--------------------------------------+-------------------------------------------------------------------------------+
| Streaming and Messaging              | Apache Kafka, Rabbit MQ                                                       |
+--------------------------------------+-------------------------------------------------------------------------------+
| Load Balancer and Service Proxy      | Envoy, Istio, NGINX                                                           |
+--------------------------------------+-------------------------------------------------------------------------------+
| Service Mesh                         | Envoy, Istio                                                                  |
+--------------------------------------+-------------------------------------------------------------------------------+
| Security & Compliance                | Calico, cert-manager                                                          |
+--------------------------------------+-------------------------------------------------------------------------------+
| Monitoring                           | Prometheus, Grafana (for Visualisation), Kiali (for Service Mesh)             |
+--------------------------------------+-------------------------------------------------------------------------------+
| Logging                              | Fluentd, ElasticSearch (Elastic.io, Open Distro), ELK Stack (Elasticsearch,   |
|                                      | Logstash, and Kibana)                                                         |
+--------------------------------------+-------------------------------------------------------------------------------+
| Application Definition and Image     | Helm                                                                          |
| Build                                |                                                                               |
+--------------------------------------+-------------------------------------------------------------------------------+
| CI/CD                                | Argo, GitLab, Jenkins                                                         |
+--------------------------------------+-------------------------------------------------------------------------------+
| Ingress/Egress Controllers           | Envoy, Istio, NGINX                                                           |
+--------------------------------------+-------------------------------------------------------------------------------+
| Network Service                      | CoreDNS, Istio                                                                |
+--------------------------------------+-------------------------------------------------------------------------------+
| Coordination and Service Discovery   | CoreDNS, etcd, Zookeeper                                                      |
+--------------------------------------+-------------------------------------------------------------------------------+
| Automation and Configuration         | Ansible                                                                       |
+--------------------------------------+-------------------------------------------------------------------------------+
| Key Management                       | Vault                                                                         |
+--------------------------------------+-------------------------------------------------------------------------------+
| Tracing                              | Jaeger                                                                        |
+--------------------------------------+-------------------------------------------------------------------------------+

**Table 5-7a:** Service examples.


Platform Services - Load Balancer Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below specifies a set of requirements for the Load Balancer platform service.

+------------+--------------------------------------------------------+---------------------------------------------+
| Reference  | Requirement                                            | Notes                                       |
+============+========================================================+=============================================+
| pas.lb.001 | The Load Balancer must support workload resource       |                                             |
|            | scaling                                                |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.002 | The Load Balancer must support resource resiliency     |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.003 | The Load Balancer must support scaling and resiliency  | Local environment: within a subnet, tenant  |
|            | in the local environment                               | network, Availability Zone of a cloud, ...  |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.004 | The Load Balancer must support OSI Level 3/4           | OSI Level 3 load-balancing decision on the  |
|            | load-balancing                                         | source and destination IP addresses and OSI |
|            |                                                        | Level 4 TCP port numbers.                   |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.005 | The Load Balancer must, at a minimum, support          |                                             |
|            | round-robin load-balancing                             |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.006 | The Load Balancer must create event logs with the      |                                             |
|            | appropriate severity levels (catastrophic,             |                                             |
|            | critical, ...)                                         |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.007 | The Load Balancer must support monitoring of endpoints |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.008 | The Load Balancer must support Direct Server           | Other modes OK as well, but DSR should      |
|            | Return (DSR)                                           | always be supported                         |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.009 | The Load Balancer must stateful TCP load-balancing     |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.010 | The Load Balancer must support UDP load-balancing      |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.011 | The Load Balancer must support load-balancing and      |                                             |
|            | correct handling of fragmented packets                 |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.012 | The Load Balancer may support state-full SCTP          |                                             |
|            | load-balancing                                         |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.013 | The Load Balancer may support state-full M-TCP         |                                             |
|            | load-balancing                                         |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.014 | The Load Balancer may support Level 7                  | OSI Level 7 (application characteristics    |
|            | load balancing                                         | based) should support HTTP and HTTPS        |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.015 | The L7 Load Balancer may support HTTP2                 |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.016 | The L7 Load Balancer may support HTTP3                 |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.017 | The L7 Load Balancer may support QUIC                  |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+

**Table 5-7b:** Platform Services - Load Balancer Requirements.

Platform Services - Log Management Service (LMS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below specifies a set of requirements for the Log Management Service (LMS).

+-------------+-----------------------------------------------------------------------+---------------------------------------+
| Reference   | Requirement                                                           | Notes                                 |
+=============+=======================================================================+=======================================+
| pas.lms.001 | LMS must support log management from multiple, distributed sources    |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.002 | LMS must manage log rotation at configurable time periods             |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.003 | LMS must manage log rotation at configurable log file status (%full)  |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.004 | LMS must manage archival and retention of logs for configurable       |                                       |
|             | time periods by different log types                                   |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.005 | LMS must ensure log file integrity (no changes, particularly changes  | Covered by req.sec.mon.005: "The      |
|             | that may affect the completeness, consistency, and accuracy including | Prod-Platform and NonProd-Platform    |
|             | event times, of the log file content)                                 | must secure  and protect all logs     |
|             |                                                                       | (containing  sensitive information)   |
|             |                                                                       | both in-transit  and at rest."        |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.006 | LMS must monitor log rotation and log archival processes              |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.007 | LMS must monitoring the logging status of all log sources             |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.008 | LMS must ensure that each logging host’s clock is synched to a common |                                       |
|             | time source                                                           |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.009 | LMS must support reconfiguring of logging as needed based on policy   |                                       |
|             | changes, technology changes, and other factors                        |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.010 | LMS must support the documenting and reporting of anomalies in log    |                                       |
|             | settings, configurations, and processes                               |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.011 | LMS must support the correlating of entries from multiple logs that   |                                       |
|             | relate to the same event                                              |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.012 | LMS must support the correlating of multiple log entries from a       |                                       |
|             | single source or multiple sources based on logged values (e.g., event |                                       |
|             | types, timestamps, IP addresses)                                      |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.013 | LMS should support rule-based correlation                             |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+

**Table 5-7c:** Platform Services - Log Management Service (LMS) Requirements.


Platform Services - Monitoring Service Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below specifies a set of requirements for the Monitoring service (aka monitoring system).

+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| Reference   | Requirement                                                           | Notes                                                 |
+=============+=======================================================================+=======================================================+
| pas.mon.001 | The Monitoring service must be able to collect data generated by or   | Capabilities to monitor applications, services,       |  
|             | collected from any resource (physical and virtual infrastructure,     | operating systems, network protocols, system metrics  |
|             | application, network, etc.)                                           | and infrastructure components                         |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.002 | The Monitoring service must be able to aggregate collected data       |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.003 | The Monitoring service must be able to correlate data from different  |                                                       |
|             | systems                                                               |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.004 | The Monitoring service must be able to perform at least one           |                                                       |
|             | of active or passive monitoring                                       |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.005 | The Monitoring service must support configuration of thresholds,      |                                                       |
|             | outside of which the resource cannot function normally, for alert     |                                                       |
|             | generation                                                            |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.006 | The Monitoring service must support configuration of alert            |                                                       |
|             | notification medium (email, SMS, phone, etc.)                         |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.007 | The Monitoring service must support configurable re-alerting after    |                                                       |
|             | a configurable period of time if the metric remains outside of the    |                                                       |
|             | threshold                                                             |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.008 | The Monitoring service must support configurable alert escalations    |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.009 | The Monitoring service must support alert acknowledgments by          |                                                       |
|             | disabling future alerting of the same resource/reason                 |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.010 | The Monitoring service must support selective enabling and            |                                                       |
|             | disabling of alerts by resource, category of resources, time periods. |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.011 | The monitoring service must publish its APIs for programmatic         |                                                       |
|             | invocation of all monitoring service functions                        |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.012 | The monitoring service must itself be monitored through a logging     |                                                       |
|             | service                                                               |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.013 | The Monitoring service should be implemented for high availability    |                                                       |
|             | to ensure non-stop monitoring of critical infrastructure components   |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.014 | The Monitoring service should run as separately from production       |                                                       |
|             | services                                                              |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.015 | Failure of the system being monitored should not cause a failure      |                                                       |
|             | in the monitoring service                                             |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.016 | An inoperative monitoring service should not generate alerts about    |                                                       |
|             | the monitored system                                                  |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.017 | The monitoring service should provide a consolidated view of the      |  View: dashboard or report                            |
|             | entire monitored infrastructure                                       |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+

**Table 5-7d:** Platform Services - Monitoring Service Requirements.



Cloud Infrastructure Software Profiles features and requirements
----------------------------------------------------------------


This section will detail Cloud Infrastructure Software Profiles and associated configurations for the 2 types of Cloud 
Infrastructure Profiles: Basic and High Performance.

.. _virtual-compute-1:

Virtual Compute
~~~~~~~~~~~~~~~


**Table 5-8** depicts the features and configurations related to virtual compute for the two (2) Cloud Infrastructure
Profiles.

================= ================================= =============== ===== ================
Reference         Feature                           Type            Basic High Performance
================= ================================= =============== ===== ================
infra.com.cfg.001 CPU allocation ratio              <value>         N:1   1:1
infra.com.cfg.002 NUMA alignment                    Yes/No          N     Y
infra.com.cfg.003 CPU pinning                       Yes/No          N     Y
infra.com.cfg.004 Huge pages                        Yes/No          N     Y
infra.com.cfg.005 Simultaneous Multithreading (SMT) Yes/No/Optional Y     Optional
================= ================================= =============== ===== ================

**Table 5-8:** Virtual Compute features and configuration for the 2 types of Cloud Infrastructure Profiles.


**Table 5-9** lists the features related to compute acceleration for the High Performance profile. The table also 
lists the applicable :ref:`chapters/chapter04:profile extensions` and Extra Specs that may need to be 
specified.


===================== =========================== ============================= ===================
Reference             Feature                     Profile-Extensions            Profile Extra Specs
===================== =========================== ============================= ===================
infra.com.acc.cfg.001 IPSec Acceleration          Compute Intensive GPU
infra.com.acc.cfg.002 Transcoding Acceleration    Compute Intensive GPU         Video Transcoding
infra.com.acc.cfg.003 Programmable Acceleration   Firmware-programmable adapter Accelerator
infra.com.acc.cfg.004 GPU                         Compute Intensive GPU
infra.com.acc.cfg.005 FPGA/other Acceleration H/W Firmware-programmable adapter
===================== =========================== ============================= ===================

**Table 5-9:** Virtual Compute Acceleration features.

.. _virtual-storage-1:

Virtual Storage
~~~~~~~~~~~~~~~


**Table 5-10** and **Table 5-11** depict the features and configurations related to virtual storage for the two (2)
Cloud Infrastructure Profiles.

================= ======================== ====== ===== ================
Reference         Feature                  Type   Basic High Performance
================= ======================== ====== ===== ================
infra.stg.cfg.001 Catalogue storage Types  Yes/No Y     Y
infra.stg.cfg.002 Storage Block            Yes/No Y     Y
infra.stg.cfg.003 Storage with replication Yes/No N     Y
infra.stg.cfg.004 Storage with encryption  Yes/No Y     Y
================= ======================== ====== ===== ================

**Table 5-10:** Virtual Storage features and configuration for the two (2) profiles.

**Table 5-11** depicts the features related to Virtual storage Acceleration

===================== ========================= ====== ===== ================
Reference             Feature                   Type   Basic High Performance
===================== ========================= ====== ===== ================
infra.stg.acc.cfg.001 Storage IOPS oriented     Yes/No N     Y
infra.stg.acc.cfg.002 Storage capacity oriented Yes/No N     N
===================== ========================= ====== ===== ================

**Table 5-11:** Virtual Storage Acceleration features.

.. _virtual-networking-1:

Virtual Networking
~~~~~~~~~~~~~~~~~~


**Table 5-12** and **Table 5-13** depict the features and configurations related to virtual networking for the 2 types
of Cloud Infrastructure Profiles.

+-------------------+----------------------+------------------------+-------------------------+------------------------+
| Reference         | Feature              | Type                   | Basic                   | High Performance       |
+===================+======================+========================+=========================+========================+
| infra.net.cfg.001 | Connection Point     | IO virtualisation      | virtio1.1               | virtio1.1\*            |
|                   | interface            |                        |                         |                        |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.002 | Overlay protocol     | Protocols              | VXLAN, MPLSoUDP,        | VXLAN, MPLSoUDP,       |
|                   |                      |                        | GENEVE, other           | GENEVE, other          |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.003 | NAT                  | Yes/No                 | Y                       | Y                      |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.004 | Security Group       | Yes/No                 | Y                       | Y                      |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.005 | Service Function     | Yes/No                 | N                       | Y                      |
|                   | Chaining             |                        |                         |                        |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.006 | Traffic patterns     | Yes/No                 | Y                       | Y                      |
|                   | symmetry             |                        |                         |                        |
+-------------------+----------------------+------------------------+-------------------------+------------------------+

**Table 5-12:** Virtual Networking features and configuration for the 2 types of SW profiles.

   **Note:** \* might have other interfaces (such as SR-IOV VFs to be directly passed to a VM or a Pod) or NIC-specific
   drivers on guest machines transiently allowed until mature enough solutions are available with a similar efficiency
   level (for example regarding CPU and energy consumption).

===================== ============================= ========================== ===== ================
Reference             Feature                       Type                       Basic High Performance
===================== ============================= ========================== ===== ================
infra.net.acc.cfg.001 vSwitch optimisation (DPDK)   Yes/No and SW Optimisation N     Y
infra.net.acc.cfg.002 SmartNIC (for HW Offload)     Yes/No/Optional            N     Optional
infra.net.acc.cfg.003 Crypto acceleration           Yes/No/Optional            N     Optional
infra.net.acc.cfg.004 Crypto Acceleration Interface Yes/No/Optional            N     Optional
===================== ============================= ========================== ===== ================

**Table 5-13:** Virtual Networking Acceleration features.

Cloud Infrastructure Hardware Profile description
-------------------------------------------------


The support of a variety of different workload types, each with different (sometimes conflicting) compute, storage, 
and network characteristics, including accelerations and optimizations, drives the need to aggregate these 
characteristics as a hardware (host) profile and capabilities. A host profile is essentially a “personality” assigned 
to a compute host (also known as physical server, compute host, host, node, or pServer). The host profiles and related 
capabilities consist of the intrinsic compute host capabilities (such as number of CPU sockets, number of cores per CPU, 
RAM, local disks and their capacity, etc.), and capabilities enabled in hardware/BIOS, specialised hardware (such as 
accelerators), the underlay networking, and storage.

This chapter defines a simplified host, profile and related capabilities model associated with each of the different 
Cloud Infrastructure Hardware Profile and related capabilities; the two :ref:`chapters/chapter02:profiles, profile 
extensions & flavours` (aka host profiles, node profiles, hardware profiles) and some of their associated capabilities 
are shown in :numref:`Cloud Infrastructure Hardware Profiles and host associated capabilities`.


.. figure:: ../figures/RM-ch05-hw-profile.png
   :name: Cloud Infrastructure Hardware Profiles and host associated capabilities
   :alt: Cloud Infrastructure Hardware Profiles and host associated capabilities

   Cloud Infrastructure Hardware Profiles and host associated capabilities

The profiles can be considered to be the set of EPA-related (Enhanced Performance Awareness) configurations on Cloud
Infrastructure resources.

   **Note:** In this chapter we shall not list all of the EPA-related configuration parameters.


A given host can only be assigned a single host profile; a host profile can be assigned to multiple hosts. In addition
to the host profile, :ref:`chapters/chapter04:profiles and workload flavours` and additional capability
specifications for the configuration of the host can be specified. Different Cloud Service Providers (CSP) may use
different naming standards for their host profiles. For the profiles to be configured, the architecture of the
underlying resource needs to be known.

============ ============================= ======= ============================= ======================
Ref          Cloud Infrastructure Resource Type    Definition/Notes              Capabilities Reference
============ ============================= ======= ============================= ======================
infra.hw.001 CPU Architecture              <value> Values such as x64, ARM, etc. ``e.cap.020``
============ ============================= ======= ============================= ======================


The host profile properties are specified in the following sub-sections. The following diagram
(:numref:`Generic model of a compute host for use in Host Profile configurations`) pictorially represents a high-level
abstraction of a physical server (host).


.. figure:: ../figures/ch06_ref_hw_profile.PNG
   :name: Generic model of a compute host for use in Host Profile configurations
   :alt: Generic model of a compute host for use in Host Profile configurations

   Generic model of a compute host for use in Host Profile configurations

.. _cloud-infrastructure-hardware-profiles-features-and-requirements:

Cloud Infrastructure Hardware Profiles features and requirements.
-----------------------------------------------------------------


The configurations specified in here will be used in specifying the actual hardware profile configurations for each of
the Cloud Infrastructure Hardware Profiles depicted in **Figure 5-4**.


Compute Resources
~~~~~~~~~~~~~~~~~

+----------------------+---------------------------------+---------------------------------+-------------+-------------+
| Reference            | Feature                         | Description                     | Basic       | High        |
|                      |                                 |                                 |             | Performance |
+======================+=================================+=================================+=============+=============+
| infra.hw.cpu.cfg.001 | Minimum number of CPU sockets   | Specifies the minimum number of | 2           | 2           |
|                      |                                 | populated CPU sockets within    |             |             |
|                      |                                 | each host (*)                   |             |             |
+----------------------+---------------------------------+---------------------------------+-------------+-------------+
| infra.hw.cpu.cfg.002 | Minimum number of cores per CPU | Specifies the number of cores   | 20          | 20          |
|                      |                                 | needed per CPU (*)              |             |             |
+----------------------+---------------------------------+---------------------------------+-------------+-------------+
| infra.hw.cpu.cfg.003 | NUMA alignment                  | NUMA alignment enabled and BIOS | N           | Y           |
|                      |                                 | configured to enable NUMA       |             |             |
+----------------------+---------------------------------+---------------------------------+-------------+-------------+
| infra.hw.cpu.cfg.004 | Simultaneous Multithreading     | SMT enabled that allows each    | Y           | Y           |
|                      | (SMT)                           | core to work multiple streams   |             |             |
|                      |                                 | of data simultaneously          |             |             |
+----------------------+---------------------------------+---------------------------------+-------------+-------------+

**Table 5-14:** Minimum sizing and capability configurations for general purpose servers.

..

   (*) Please note that these specifications are for general purpose servers normally located in large data centres.
   Servers for specialised use with the data centres or other locations, such as at edge sites, are likely to have
   different specifications.



Compute Acceleration Hardware Specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================== =========================== =============== ===== ================ ======================
Reference            Feature                     Description     Basic High Performance Capabilities Reference
==================== =========================== =============== ===== ================ ======================
infra.hw.cac.cfg.001 GPU                         GPU             N     Optional         ``e.cap.014``
infra.hw.cac.cfg.002 FPGA/other Acceleration H/W HW Accelerators N     Optional         ``e.cap.016``
==================== =========================== =============== ===== ================ ======================

**Table 5-15:** Compute acceleration configuration specifications.

Storage Configurations
~~~~~~~~~~~~~~~~~~~~~~

========================== ================= ================= =========== ================
Reference                  Feature           Description       Basic       High Performance
========================== ================= ================= =========== ================
infra.hw.stg.hdd.cfg.001\* Local Storage HDD Hard Disk Drive
infra.hw.stg.ssd.cfg.002\* Local Storage SSD Solid State Drive Recommended Recommended
========================== ================= ================= =========== ================

**Table 5-16:** Storage configuration specification.

   **Note:** \*This specified local storage configurations including # and capacity of storage drives.

Network Resources
~~~~~~~~~~~~~~~~~

NIC configurations
^^^^^^^^^^^^^^^^^^

==================== ========== =============================================== ===== ================
Reference            Feature    Description                                     Basic High Performance
==================== ========== =============================================== ===== ================
infra.hw.nic.cfg.001 NIC Ports  Total number of NIC Ports available in the host 4     4
infra.hw.nic.cfg.002 Port Speed Port speed specified in Gbps (minimum values)   10    25
==================== ========== =============================================== ===== ================

**Table 5-17:** Minimum NIC configuration specification.

PCIe Configurations
^^^^^^^^^^^^^^^^^^^

==================== ========== ========================================== ===== ================
Reference            Feature    Description                                Basic High Performance
==================== ========== ========================================== ===== ================
infra.hw.pci.cfg.001 PCIe slots Number of PCIe slots available in the host 8     8
infra.hw.pci.cfg.002 PCIe speed                                            Gen 3 Gen 3
infra.hw.pci.cfg.003 PCIe Lanes                                            8     8
==================== ========== ========================================== ===== ================

**Table 5-18:** PCIe configuration specification.

Network Acceleration Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================== =================== ============================= ======== ================ ======================
Reference            Feature             Description                   Basic    High Performance Capabilities Reference
==================== =================== ============================= ======== ================ ======================
infra.hw.nac.cfg.001 Crypto Acceleration IPSec, Crypto                 N        Optional         ``e.cap.009``
infra.hw.nac.cfg.002 SmartNIC            offload network functionality N        Optional         ``e.cap.015``
infra.hw.nac.cfg.003 Compression                                       Optional Optional
infra.hw.nac.cfg.004 SR-IOV over PCI-PT  SR-IOV                        N        Optional         ``e.cap.013``
==================== =================== ============================= ======== ================ ======================

**Table 5-19:** Network acceleration configuration specification.
