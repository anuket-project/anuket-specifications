[<< Back](../../ref_model)
# 10 Challenges and Gaps



## Table of Contents
* [10.1 Introduction](#10.1)
* [10.2 Challenges](#10.2)
* [10.3 Gaps](#10.3)
  * [10.3.1 Discovery](#10.3.1)
  * [10.3.2 Support Load Balance of VNF/CNFs](#10.3.2)
  * [10.3.3 Service Function Chain](#10.3.3)
  * [10.3.4 Packet Acceleration Request (e.g Hardware Acceleration)](#10.3.4)
  * [10.3.5 Multi-cloud architecture directions for network workloads)](#10.3.5)


<a name="10.1"></a>
## 10.1 Introduction [Draft Language]

The development of this Reference Model is in its initialization stage and it will go through several iteration cycles before it is adding the full value intended. The reference model is also the first component in the establishment of a Common Cloud Infrastructure Lifecycle Framework--see also diagram below:

Key Components of The Common Cloud Infrastructure Lifecycle Framework

- Reference Model
- Reference Architecture
- Reference Implementation
- Verification & Validation
- Lifecycle Feedback Loops

As the first component, the reference model must also be structured and iterated so that it plays its part as the foundation on which the other five components of the ecosystem are built.

Going forward, this chapter shall be dedicated to identifying the challenges and gaps found in the course the development--to ensure the reference model is adding the strategic and tactical value intended over time. Should a challenge or gap not be identified and it is not already addressed in the model itself, the community may assume it will remain an unknown and, therefore, the community is welcomed to engage with and raise an issue with the appropriate working group(s) to close the gap. In this manner, the Reference Model can continuously improve.

For Reference - Common Cloud Infrastructure Lifecycle Framework Diagram (Figure 10-1)
<p align="center"><img src="../figures/ch10-fig-10-1-common-nfvi_lifecycle_framework.png" alt="Framework" title="Framework" width="65%"/></p>

<a name="10.2"></a>
## 10.2 Challenges 

The current challenge is getting to a stable working version from which all stakeholders in the application value-chain can begin to extract the intended value of a Common Cloud Infrastructure. The next maturity level is reached when the Reference Model has stabilized enough for stakeholders to adopt the model into their own application development and deployment cycles.

<a name="10.3"></a>
## 10.3 Gaps 

Gaps

This section addresses major open issues identified in the development of the Reference Model, Reference Architecture, Reference Implementation of the Common Cloud Infrastructure Lifecycle Framework. 

<a name="10.3.1"></a>
### 10.3.1 Discovery
The workloads (VNFs/CNFs) and Cloud Infrastructure should be able to discover each other and exchange their capabilities required or offered. One of the key pain points for most of the operators is the VNF/CNF onboarding - both in terms of time and complexity. It could take weeks or months to onboard a VNF/CNF. There are lots of static and laborious checks performed to ensure the compatibility of the workloads with the corresponding Cloud Infrastructure. 
The onboarding of the workloads (network functions) should be automated as much as possible. The workloads and Cloud Infrastructure should be able to discover and negotiate their capabilities. Following should be supported: 
- Capabilities Discovery and Advertising
    - Cloud Infrastructure should be able to publish the capabilities it offers to workloads (network functions) 
    - workloads should be able to query the Cloud Infrastructure for specific capabilities - such as number of cores, performance parameters
- Capabilities Negotiation/Hand Shake API: 
    - workloads and Cloud Infrastructure should be able to negotiate on certain capabilities. For instance, workload desires HW acceleration for high throughput, but should be able to fall back to high throughput offered by Cloud Infrastructure via DPDK offering, and vice-a-versa.


<a name="10.3.2"></a>
### 10.3.2 Support Load Balance of VNF/CNFs
The ability to dynamically scale a network function by load balancing accross multiple instances/replicas of the same VNF or CNF is essential. New architectures and application patterns such as micro services is making this even more crucial. It must not only be possible to load balance and scale each service layer independently, support to chain the different layers together through "Service Function Chaining" is also needed. 


The load balancing and scaling needed for typical enterprise applications is well supported in OpenStack by the LBaaSv2 API and Octavia. The built in mechanism in Kubernetes for scaling enterprise type of services and PODs is also sufficient for applications that only use one interface.

What is not supported in either OpenStack or Kubernetes is to scale and load balance a typical VNF and CNF. There is no support in OpenStack to scale stateful L3 applications such as SCTP, QUIC. mTCP, and gRPC. In Kubernetes it is even worse. The built in kubernetes network support is tied to the first POD/container interface. Support for secondary interfaces is managed through the Container Network Interface, CNI, and by CNI plugins, such as Multus, that support the "Kubernetes Network Customs Resource Definition" specified by the Kubernetes Network Plumbing Group. This specification supports attachment of network endpoints to PODs, IP address management and the ability of define interface specific static routes. There is no support for network orchestration and functions such as load balancing, routing, ACL and firewalls.

<a name="10.3.3"></a>
### 10.3.3 Service Function Chain
Over the past few years there has been a significant move towards decomposing network functions into smaller sub-functions that can be independently scaled and potentially reused across multiple network functions. A service function chain allows composition of network functions by passing selected packets through an ordered list of services. In order to support this capability in a sustainable manner, there is a need to have the capability to model service chains as a high level abstraction. This is essential to ensure that the underlying connection setup, and (re-)direction of traffic flows can be performed in an automated manner. There is also a need to provide specialized tools aid troubleshooting of individual services and the communication between them in order to investigate issues in the performance of composed network functions.

<a name="10.3.4"></a>
### 10.3.4 Packet Acceleration Request (e.g Hardware Acceleration)
While generic server hardware capabilities can be exclusively used for handling networking related workloads, this strategy is neither performant nor energy efficient. There are several forms of accelerators such as smart NICs, programmable networking fabrics/switches, and GPUs that can offload some of these workloads in order to provide higher throughput, energy efficiency and lower latency. The acceleration hardware is typically optimized for specific kinds of workloads and some form of disaggregation might be required to separate control and user plane responsibilities between generic server hardware and accelerators. Additionally, there might also be a need for disaggregation between user plane functions that may require different types of accelerators. There is also a need for workload orchestration to be able to understand the packet acceleration needs of specific workloads and schedule such workloads on infrastructure with the requisite capabilities. This will require that there be some form of discovery mechanism that would allow the workload orchestration to dicover the presence of acceleration hardware.

### 10.3.5 Multi-cloud architecture directions for network workloads
There is a growing interest in using a multi-cloud environment for the deployment of network functions. The industry investigates and starts to experiment with deploying and operating network functions across several private and/or public clouds to reuse services and capabilities available in these cloud enviroments instead of investing in a duplications of such capabilities.  5G and Edge deployments seem to be some of the catalysts of the growing interest.  The Reference Model will need to provide in its future releases relevant guidelines for such multi-cloud architectures.
