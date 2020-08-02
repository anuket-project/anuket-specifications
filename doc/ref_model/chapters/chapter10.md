[<< Back](../../ref_model)
# 10 Challenges and Gaps

<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [10.1 Introduction](#10.1)
* [10.2 Challenges](#10.2)
* [10.3 Gaps](#10.3)

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


## 10.3 Gaps 

Gaps

This section addresses major open issues identified in the development of the Reference Model, Reference Architecture, Reference Implementation of the Common Cloud Infrastructure Lifecycle Framework. 

## 10.3.1 Discovery
The workloads (VNFs/CNFs) and Cloud Infrastructure should be able to discover each other and exchange their capabilities required or offered. One of the key pain points for most of the operators is the VNF/CNF onboarding - both in terms of time and complexity. It could take weeks or months to onboard a VNF/CNF. There are lots of static and laborious checks performed to ensure the compatibility of the workloads with the corresponding Cloud Infrastructure. 
The onboarding of the workloads (network functions) should be automated as much as possible. The workloads and Cloud Infrastructure should be able to discover and negotiate their capabilities. Following should be supported: 
- Capabilities Discovery and Advertising
    - Cloud Infrastructure should be able to publish the capabilities it offers to workloads (network functions) 
    - workloads should be able to query the Cloud Infrastructure for specific capabilities - such as number of cores, performance parameters
- Capabilities Negotiation/Hand Shake API: 
    - workloads and Cloud Infrastructure should be able to negotiate on certain capabilities. For instance, workload desires HW acceleration for high throughput, but should be able to fall back to high throughput offered by Cloud Infrastructure via DPDK offering, and vice-a-versa.

## 10.3.2 Support Load Balance of VNF/CNFs [Initial language]
Ability to load balance workflows through multiple instances of same VNF or CNF - e.g. using ECMP to distribute workloads through the multiple instances of Firewall. As an example imagine a distributed finance application with multiple instances of Web-tier and DB-tier. The traffic needs to flow through multiple instances of Firewall (for HA as well load balancing). There is no simple way to accomplish this in OpenStack.

## 10.3.3 Service Function Chain [Initial language]
Over the past few years there has been a significant move towards decomposing network functions into smaller sub-functions that can be independently scaled and potentially reused across multiple network functions. A service function chain allows composition of network functions by passing selected packets through an ordered list of services. In order to support this capability in a sustainable manner, there is a need to have the capability to model service chains as a high level abstraction. This is essential to ensure that the underlying connection setup, and (re-)direction of traffic flows can be performed in an automated manner. There is also a need to provide specialized tools aid troubleshooting of individual services and the communication between them in order to investigate issues in the performance of composed network functions.

## 10.3.4 Packet Acceleration Request (e.g Hardware Acceleration) [Initial language]
While generic server hardware capabilities can be exclusively used for handling networking related workloads, this strategy is neither performant nor energy efficient. There are several forms of accelerators such as smart NICs, programmable networking fabrics/switches, and GPUs that can offload some of these workloads in order to provide higher throughput, energy efficiency and lower latency. The acceleration hardware is typically optimized for specific kinds of workloads and some form of disaggregation might be required to separate control and user plane responsibilities between generic server hardware and accelerators. There is also a need for workload orchestration to be able to understand the packet acceleration needs of specific workloads and schedule such workloads on infrastructure with the requisite capabilities.
