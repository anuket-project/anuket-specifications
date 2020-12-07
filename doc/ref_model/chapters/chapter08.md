[<< Back](../../ref_model)

# 8. Hybrid Multi-Cloud: Data Center to Edge

## Table of Contents
* [8.1 Introduction](#8.1)
* [8.2 Hybrid Multi-Cloud Architecture](#8.2)
  * [8.2.1. Characteristics of a Federated Cloud](#8.2.1)
  * [8.2.2. Telco Cloud](#8.2.2)
  * [8.2.3. Telco Operator Platform Conceptual Architecture](#8.2.3)

<a name="8.1"></a>
## 8.1 Introduction
The [Reference Model Chapter 3](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter01.md) focuses on cloud infrastructure abstractions. While these are generic abstractions they and the associated capabilities are specified for data center or a colocation center cloud infrastructure. The environmental conditions, facility and other constraints, and the variability of deployments on the edge are significantly different and, thus, requires separate consideration.

It is unrealistic to expect that a private cloud can cost effectively meet the need of all loads, including peak and disaster recovery. It is for that reason that enterprises will implement an hybrid cloud.  In a hybrid cloud deployment, at least two or more distinct cloud infrastructures are inter-connected together.  In a multi-cloud the distinct cloud infrastructures of the hybrid cloud may be implemented using one or more technologies.  The hybrid multi-cloud infrastructure has differences requiring different abstractions. These hybrid multi-clouds can be considered to be federated.

In IaaS clouds, the cloud infrastructure is defined but the tenant workloads include certain needed services (such as LB, messaging); thus, the VNF/CNFs may incorporate different services with the resultant issues related to an explosion of services, their integration and management complexities. To mitigate these issues, the CNTT Reference Model must specify the common services that every Telco cloud must support and thereby require workload developers to utilise these pre-specified services.

A generic Telco cloud is an hybrid multi-cloud or a Federated cloud that has deployments in large data centers, central offices or colocation facilities, and the edge. In this chapter we will discuss the characteristics of Telco Edge and hybrid multi-cloud.

<a name="8.2"></a>
## 8.2 Hybrid Multi-Cloud Architecture
The GSMA whitepaper on "Operator Platform Concept Phase 1: Edge Cloud Computing" (January 2020) states, "Given the wide diversity of use cases that the operators will tasked to address, from healthcare to industrial IoT, it seems logical for operators to create a generic platform that can package the existing assets and capabilities (e.g., voice messaging, IP data services, billing, security, identity management, etc. ...) as well as the new ones that 5G makes available (e.g., Edge cloud, network slicing, etc.) in such a way as to create the necessary flexibility required by this new breed of enterprise customers."

Cloud computing has evolved and matured since 2010 when NIST (http://csrc.nist.gov/publications/nistpubs/800-145/SP800-145.pd) published its definition of cloud computing, with its 5 essential characteristics, 3 service models and 4 deployment models.

The generic model for an enterprise cloud has to be "hybrid" with the special cases of purely private or public clouds as subsets of the generic hybrid cloud deployment model. In a hybrid cloud deployment, at least two or more distinct cloud infrastructures are inter-connected together.

Cloud deployments can be created using a variety of technologies  (e.g., OpenStack, Kubernetes) and commercial technologies (e.g., VMware, AWS, Azure, etc.). A multi-cloud deployment can consist of the use of more than one technology.

A generic Telco cloud is an hybrid multi-cloud. A better designation would be a federation of clouds - a federated cloud:
   - a collection of cooperating, interoperable autonomous component clouds
   -  the component clouds perform their local operations (internal requests) while also participating in the federation and responding to other component clouds (external requests)
        - the component clouds are autonomous in terms of, for example, execution autonomy
        - execution autonomy is the ability of a component cloud to decide the order in which internal and external requests are performed
   - the component clouds are loosely coupled where no no changes are required to participate in a federation
        - also, a federation controller does not impose changes to the component cloud except for running some central component(s) of the federated system (for example, a broker agent – executes as a workload)
   - the component clouds are likely to differ in, for example, infrastructure resources and their cloud platform software
   - workloads may be distributed on single or multiple clouds, where the clouds may be colocated or geographically distributed
   - component clouds only surface NBIs (Please note that VMware deployed in a private and  a public cloud can be treated as a single cloud instance)

<a name="8.2.1"></a>
### 8.2.1 Characteristics of a Federated Cloud
In this section we will further explore the characteristics of the federated cloud, architecture and architecture building blocks that constitute the  federated cloud. For example, a Telco Cloud that consists of 4 sub-clouds: Private on prem, Cloud Vendor provided on prem, Private outsourced (Commercial Cloud Provider such as an Hyperscalar Cloud Provider (HCP), and Public outsourced (see diagram below). Such an implementation of a Telco Cloud allows for mix'n'match of price points, flexibility in market positioning and time to market, capacity with the objective of attaining near "unlimited" capacity, scaling within a sub-cloud or through bursting across sub-clouds, access to "local" capacity near user base, and access to specialised services.

**Add Figure of Cloud A, B, C and D

<a name="8.2.2"></a>
### 8.2.2 Telco Cloud
The Figure below presents a visualisation of a Telco operator cloud (or simply, Telco cloud) with clouds and cloud components distributed across Regional Data Centers, Metro locations (such as Central Office or a Colocation site) and at the Edge, that are interconnected using a partial mesh network. Please note that at the Regional center level the interconnections are likely to be a "fuller" mesh while being a sparser mesh at the Edges.

**Add multi-cloud Figure

The Telco Operator may own and/or have partnerships and network connections to utilize multiple Clouds for network services, IT workloads, external subscribers. The types of the component clouds include:
   - On Prem Private
        - Open source; Operator or Vendor deployed and managed  | OpenStack or Kubernetes based
        - Vendor developed; Operator or Vendor deployed and managed  | Examples: Azure on Prem, VMware, Packet, Nokia, Ericsson, etc.
   - On Prem Public: Commercial Cloud service hosted at Operator location but for both Operator and Public use | Example: AWS Wavelength
   - Outsourced Private: hosting outsourced; hosting can be at a Commercial Cloud Service | Examples: Equinix, AWS, etc.
   - (Outsourced) Public: Commercial Cloud Service | Examples: AWS, Azure, VMware, etc.
   - Multiple different Clouds can be co-located in the same physical location and may share some of the physical infrastructure (for example, racks)

In general, a Telco Cloud consists of multiple interconnected very large data centers that serve trans-continentalareas (Regions). A Telco Cloud Region may connect to multiple regions of another Telco Cloud via large capacity networks. A Telco Cloud also consists of interconnected local/metro sites (multiple possible scenarios). A local site cloud may connect to multiple Regions within that Telco Cloud or another Telco Cloud. A Telco Cloud also consists of a large number of interconnected edge nodes where these edge nodes maybe impermanent. A Telco Cloud's Edge node may connect to multiple local sites within that Telco Cloud or another Telco Cloud; an Edge node may rarely connect to a Telco Cloud Region.

The Table below captures the essential information about the types of deployments, and responsible parties for cloud artifacts.

Type | System Developer | System Maintenance | System Operated & Managed by | Location where Deployed | Primary Resource Consumption Models
---|---|---|---|---|---
Private (Internal Users) | Open Source | Self/Vendor | Self/Vendor | On Prem | Reserved, Dedicated
Private | Vendor  |  HCP* | Self/Vendor | Self/Vendor | On Prem | Reserved, Dedicated
Public | Vendor  |  HCP | Self/Vendor | Self/Vendor | On Prem | Reserved, On Demand
Private | HCP | Vendor | Vendor | Vendor Locations | Reserved, Dedicated
Public (All Users) | HCP | Vendor | Vendor | Vendor Locations | On Demand, Reserved

*HCP - Hyperscaler Cloud Provider

<a name="8.2.3"></a>
### 8.2.3 Telco Operator Platform Conceptual Architecture
The Figure below shows a conceptual Telco Operator Platform Architecture. The Cloud Infrastructure Resources Layer exposes virtualised (including containerised) resources on the physical infrastructure resources and also consists of various virtualisation and management software (see details later in this chapter). The Cloud Platform Components Layer makes available both elementary and composite objects for use by application and service developers, and for use by Services during runtime.  The Cloud Services Layer exposes the Services and Applications that are available to the Users; some of the Services and Applications may be sourced from or execute on other cloud platforms. Please note that while the architecture is shown as a set of layers, this is not an isolation mechanism and, thus, for example, Users may access the Cloud Infrastructure Resources directly without interacting with a Broker.

The Cloud Services and the Cloud Resources Brokers provide value-added services in addition to the fundamental capabilities like service and resource discovery.  These Brokers are critical for a multi-cloud environment to function and utilise cloud specific plugins to perform the necessary activities. These Brokers can, for example, provision and manage environments with resources and services for Machine Learning (ML) services, Augmented/Virtual Reality, or specific industries.
