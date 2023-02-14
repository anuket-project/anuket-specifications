Challenges and Gaps
===================

Introduction
------------

This chapter is dedicated to identifying the challenges and gaps found in the course of the development of the reference
model to ensure that it continues to be of strategic and tactical value intended over time. Should a challenge or gap
not be identified that is not already addressed in the model itself, the community may assume it will remain an unknown
and, therefore, the community is encouraged to engage with and raise an issue with the appropriate working group(s) to
close the gap. In this manner, the Reference Model can continuously improve.

Challenges
----------

The continuous challenge is finalizing a stable version from which all stakeholders in the application value-chain can
derive the intended value of a Common Cloud Infrastructure. This maturity level is reached when the released Reference
Model version is adopted by stakeholders into their application development and deployment cycles.

Gaps
----

This section addresses major open issues identified in the development of the Reference Model, Reference Architecture
and Reference Implementation of the Common Cloud Infrastructure Lifecycle Framework.

Discovery
~~~~~~~~~

The workloads (VNFs/CNFs) and Cloud Infrastructure should be able to discover each other and exchange their capabilities
required or offered. One of the key pain points for most of the operators is the VNF/CNF onboarding - both in terms of
time and complexity. It could take weeks or months to onboard a VNF/CNF. There are lots of static and laborious checks
performed to ensure the compatibility of the workloads with the corresponding Cloud Infrastructure.
The onboarding of the workloads (network functions) should be automated as much as possible. The workloads and Cloud
Infrastructure should be able to discover and negotiate their capabilities. Following should be supported:

- Capabilities Discovery and Advertising

  - Cloud Infrastructure should be able to publish the capabilities it offers to workloads (network functions)
  - workloads should be able to query the Cloud Infrastructure for specific capabilities - such as number of cores,
    performance parameters

- Capabilities Negotiation/Hand Shake API:

  - workloads and Cloud Infrastructure should be able to negotiate on certain capabilities. For instance, workload
    desires HW acceleration for high throughput, but should be able to fall back to high throughput offered by Cloud
    Infrastructure via DPDK offering, and vice-a-versa.

Support Load Balance of VNF/CNFs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ability to dynamically scale a network function by load balancing across multiple instances/replicas of the same VNF
or CNF is essential. New architectures and application patterns such as micro services is making this even more crucial.
It must not only be possible to load balance and scale each service layer independently, support to chain the different
layers together through "Service Function Chaining" is also needed.

The load balancing and scaling needed for typical enterprise applications is well supported in OpenStack by the Octavia
v2 API, the Octavia v2 API is a backwards comnpatible superset of the old neutron LBaaS v2 API that it is replacing.

The built in mechanism in Kubernetes for scaling enterprise type of services and PODs is also sufficient for
applications that only use one interface.

What is not supported in either OpenStack or Kubernetes is to scale and load balance a typical VNF and CNF. There is no
support in OpenStack to scale stateful L3 applications such as SCTP, QUIC, mTCP, and gRPC. In Kubernetes it is even
worse. The built in Kubernetes network support is tied to the first POD/container interface. Support for secondary
interfaces is managed through the Container Network Interface, CNI, and by CNI plugins, such as Multus, that support
the "Kubernetes Network Customs Resource Definition" specified by the Kubernetes Network Plumbing Group. This
specification supports attachment of network endpoints to PODs, IP address management and the ability of define
interface specific static routes. There is no support for network orchestration and functions such as load balancing,
routing, ACL and firewalls.

Closed-loop automation
~~~~~~~~~~~~~~~~~~~~~~

The state of a system is defined by a set of variables that fully describe the system and determines the response of the
system to any given set of inputs. A closed loop automation system automatically maintains the specified desired state
of the controlled system.

Closed-loop automation is evolving as a major advancement in the telecommunication network automation. In the context of
telecommunication systems, it means a system that in a continuous loop programmatically validates the state of the cloud
infrastructure against the declared desired state, and in case of deviation from the desires state, it automatically
takes remediation actions necessary for bringing the actual state to the desired state. The Reference Model
specification will in its next releases address this important area.

Hybrid Multi-Cloud: APIs
~~~~~~~~~~~~~~~~~~~~~~~~

Section "8.5 Multi-Cloud Interactions Model" defines several core roles within the Multi-Cloud Model and discusses
stereo-typical interactions between them. However, the Model realises that a federated cloud requires the definition and
agreement on a set of APIs. The current fragmentation in the industry is caused by various factors:

- Proprietary APIs, some of which have been adopted as default industry standards
- A number of Open Source Community projects aiming to provide abstract interfaces to wrap proprietary API
- Vendors offering to act as brokers and
- Standards and Industry APIs to address specific subset of the interactions.

AF_XDP
~~~~~~

Linux-native AF_XDP promises high enough packet processing performance and simplification compared to what SR-IOV and DPDK
require for initial installation and later lifecycle management. Still, it will take time till AF_XDP-based solutions are
financially invested and matured enough in both Virtualization Infrastructure and Network Functions.
