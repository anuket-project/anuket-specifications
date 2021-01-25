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
  * [10.3.6 Closed-loop automation](#10.3.6)


<a name="10.1"></a>
## 10.1 Introduction 

This chapter is dedicated to identifying the challenges and gaps found in the course of the development of the reference model to ensure that it continues to be of strategic and tactical value intended over time. Should a challenge or gap not be identified that is not already addressed in the model itself, the community may assume it will remain an unknown and, therefore, the community is encouraged to engage with and raise an issue with the appropriate working group(s) to close the gap. In this manner, the Reference Model can continuously improve.

<a name="10.2"></a>
## 10.2 Challenges 

The continuous challenge is finalizing a stable version from which all stakeholders in the application value-chain can derive the intended value of a Common Cloud Infrastructure. This maturity level is reached when the released Reference Model version is adopted by stakeholders into their application development and deployment cycles.

<a name="10.3"></a>
## 10.3 Gaps 

This section addresses major open issues identified in the development of the Reference Model, Reference Architecture and Reference Implementation of the Common Cloud Infrastructure Lifecycle Framework. 

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
The ability to dynamically scale a network function by load balancing across multiple instances/replicas of the same VNF or CNF is essential. New architectures and application patterns such as micro services is making this even more crucial. It must not only be possible to load balance and scale each service layer independently, support to chain the different layers together through "Service Function Chaining" is also needed. 


The load balancing and scaling needed for typical enterprise applications is well supported in OpenStack by the Octavia v2 API, the Octavia v2 API is a backwards comnpatible superset of the old neutron LBaaS v2 API that it is replacing.

The built in mechanism in Kubernetes for scaling enterprise type of services and PODs is also sufficient for applications that only use one interface.

What is not supported in either OpenStack or Kubernetes is to scale and load balance a typical VNF and CNF. There is no support in OpenStack to scale stateful L3 applications such as SCTP, QUIC. mTCP, and gRPC. In Kubernetes it is even worse. The built in Kubernetes network support is tied to the first POD/container interface. Support for secondary interfaces is managed through the Container Network Interface, CNI, and by CNI plugins, such as Multus, that support the "Kubernetes Network Customs Resource Definition" specified by the Kubernetes Network Plumbing Group. This specification supports attachment of network endpoints to PODs, IP address management and the ability of define interface specific static routes. There is no support for network orchestration and functions such as load balancing, routing, ACL and firewalls.

<a name="10.3.3"></a>
### 10.3.3 Service Function Chain
Over the past few years there has been a significant move towards decomposing network functions into smaller sub-functions that can be independently scaled and potentially reused across multiple network functions. A service function chain allows composition of network functions by passing selected packets through an ordered list of services. In order to support this capability in a sustainable manner, there is a need to have the capability to model service chains as a high level abstraction. This is essential to ensure that the underlying connection setup, and (re-)direction of traffic flows can be performed in an automated manner. There is also a need to provide specialized tools aid troubleshooting of individual services and the communication between them in order to investigate issues in the performance of composed network functions.

<a name="10.3.4"></a>
### 10.3.4 Packet Acceleration Request (e.g. Hardware Acceleration)
While generic server hardware capabilities can be exclusively used for handling networking related workloads, this strategy is neither performant nor energy efficient. There are several forms of accelerators such as smart NICs, programmable networking fabrics/switches, and GPUs that can offload some of these workloads in order to provide higher throughput, energy efficiency and lower latency. The acceleration hardware is typically optimized for specific kinds of workloads and some form of disaggregation might be required to separate control and user plane responsibilities between generic server hardware and accelerators. Additionally, there might also be a need for disaggregation between user plane functions that may require different types of accelerators. There is also a need for workload orchestration to be able to understand the packet acceleration needs of specific workloads and schedule such workloads on infrastructure with the requisite capabilities. This will require that there be some form of discovery mechanism that would allow the workload orchestration to discover the presence of acceleration hardware.

<a name="10.3.5"></a>
### 10.3.5 Multi-cloud architecture directions for network workloads
There is a growing interest in using a multi-cloud environment for the deployment of network functions. The industry investigates and starts to experiment with deploying and operating network functions across several private and/or public clouds to reuse services and capabilities available in these cloud environments instead of investing in a duplications of such capabilities.  5G and Edge deployments seem to be some of the catalysts of the growing interest.  The Reference Model will need to provide in its future releases relevant guidelines for such multi-cloud architectures.

<a name="10.3.6"></a>
### 10.3.6 Closed-loop automation 
The state of a system is defined by a set of variables that fully describe the system and determines the response of the system to any given set of inputs. A closed loop automation system automatically maintains the specified desired state of the controlled system. 

Closed-loop automation is evolving as a major advancement in the telecommunication network automation. In the context of telecommunication systems, it means a system that in a continuous loop programmatically validates the state of the cloud infrastructure against the declared desired state, and in case of deviation from the desires state, it automatically takes remediation actions necessary for bringing the actual state to the desired state. The Reference Model specification will in its next releases address this important area.
