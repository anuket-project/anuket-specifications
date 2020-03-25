[<< Back](./README.md)
# CNTT Approach

## Table of Contents
* [5.1 Networking and Fabric Approach](#5.1)
  * [5.1.1 Executive Summary](#5.1.1)
  * [5.1.2 Strategic Objectives](#5.1.2)
  * [5.1.3 Networking Requirements](#5.1.3)
  * [5.1.4 Initial Steps](#5.1.4)

<a name="5.1"></a>
## 5.1 Networking and Fabric Approach

> _**Editor's Note:** The purpose in the subsections is to provide initial high-level content related to networking across CNTT, so as to provide general direction and help coordinate current independent networking development activities, as well as to satisfy the networking MVP deliverables for the Baldy release. The following content addresses the overall CNTT networking solution, and it is anticipated this content will be expanded and be relocated where appropriate._

The basic approach to producing the initial deliverables is to:
A) Summarize the overall CNTT Networking and Fabric Strategy
B) Document the initial list of Objectives and Requirements
C) Document enough initial logistical details for contributors to create coherent content

Readers be aware, in parallel with the CNTT Networking Strategy, the RI team is implementing networking for use today in labs and by RC. As RI has to deliver a working network at the same time the initial networking strategy and specifications are to be delivered, it is not expected nor mandated RI networking be conformant in the immediate future. However, the RI will need to be compatible, meaning, it delivers the network connectivity required by the RA and by RC, even if it does not implement the APIs, topology, encapsulation, etc., that will ultimately be specified herein.

The following subsections, Executive Summary, Strategy Objectives, Networking Requirements and Initial Approach, respectively, are intended to provide an overview of CNTT's vision for networking and intent, objectives, requirements and their supporting rationale, as well as initial development approach.

The networking within a cloud infrastructure, fabric or otherwise, is an area where there is significant variability across implementations. Leaf-Spine topology is well established, however, after topology there are countless decisions an Operator needs to make. Differences arise from many aspects, for example, is the solution layer-2 or layer-3; is the routing static or dynamic; what mechanism is used for encapsulation; what mechanism is used for isolation; does it support SR-IOV; does it support DPDK; does it employ SmartNICs; does it employ distributed control or a centralized control driving a programmable fabric; and the list continues. The multitude of permutations enable cloud infrastructure architects (Operators and Suppliers) to design (or procure) a fabric/networking solution that's optimized for their needs, whether their needs are minimal, very extensive or somewhere in between.

For CNTT, a strategy is needed that affords Operators the performance, flexibility, availability, maintainability and scalability their business requires, yet doesn't require OPNFV to design, manage and test prohibitive numbers of networking solutions.
 
**Some points for CNTT to consider when contemplating recommendations:**
   > * Despite large variances in implementation, the spectrum of networking capabilities ultimately delivered to Workloads is comparatively narrow
   > * Standard CNTT methodology (i.e. normalize interfaces, APIs, capabilities and behaviors at the reference points) applies well to networking, helping mitigate the need to be overly prescriptive about implementation  
   > * CNTT/OPNFV MUST provide a functional networking solution for the RI, and in support of RC  
   > * CNTT/OPNFV potentially does NOT have to provide a production networking solution for RI  
   > * CNTT/OPNFV is NOT planning to provide a production compute solution for RI


<a name="5.1.1"></a>
### 5.1.1 Executive Summary

> _Placeholder for the Executive Summary (targeting Baldy for first draft). **If you are interested in writing this content, please contact the RM lead.**_

<a name="5.1.2"></a>
### 5.1.2 Networking Strategy Objectives

This section catalogs CNTT's high-level objectives for the Network Fabric Strategy. 

> List needs to be prioritized; expect additional objectives to be added, as they arise. This represents the _What_, not the _How_.

1. The implementation of Networking inside the HW Layer should not be visible to the VNF/CNF and should preferably not even be visible to the IaaS/CaaS
1. Provide networks for L3 tenant, GWs, SDS, etc.
1. Cleanly decouple interface/reference points between CNTT constituencies
1. Provide interoperability at layer demarcation/reference points within the cloud infrastructure. Ex.:
   * any RA couples to RM
   * like RI couples to RA
   * like VIs (Vendor's Implementations) couple to RA
   * Operators can design or procure a compatible fabric
1. Concurrently supports containerized and virtualized coexistence for VNF->CNF cutovers, as well as protracted parallel operations
1. Provide a version controlled catalog of APIs, and their respective spans of control, capabilities and purpose, to facilitate predictable integration w/ a wide selection of fabric implementations
1. Provide ability for any number of Operator-specific fabrics to power CNTT cloud infrastructure
1. Enable RC's ability to realize mandated OVP qualification deliverables
1. Unambiguously document the responsibilities of each CNTT constituency
1. In cases where a VNF/CNF require HW layer resources it should be under the control of the Virtualization Layer
1. It is important that the HW Infrastructure Manager, each VIM and each VNF/CNF could be managed by separate organizations
1. Drive the industry towards convergence on ABIs supporting Cloud-Native implementations for SmartNICs

> _**Editor's Note:** Consider moving objectives to a table_

<a name="5.1.3"></a>
### 5.1.3 Networking Requirements

1. cloud infrastructure layer responsibilities will include:
   * HW Infrastructure Manager shall provide an abstracted model of the allocated HW resources into each specific Virtualization domain
     * Additionally, it is responsible for maintaining logical isolation between different instances of virtualization domain
     * Some of the HW resources including networking resources shall be possible to be withheld from Virtualization domains to allow for scaling, spare parts and HW Composition within the HW Infrastructure Layer itself
   * Virtualization layer shall provide the Cloud Tenants with an abstracted networking environment
     * It is therefore responsible for maintaining isolation between Cloud Tenants

An example of the layering described above is depicted in **Figure 1-3**, where the Virtualization layer manages the Overlay Networking (e.g., through VLAN allocation) and the HW Infrastructure manages the Underlay networking (e.g., through VxLAN VNI range allocations).
<p align="center"><img src="./figures/RMCH-01_Network_Layering_v0-3.png" alt="Network Layering" title="Network Layering" width="100%"/></p>
<p align="center"><b>Figure 1-3:</b> Network Layering</p>

<a name="5.1.4"></a>
### 5.1.4 Initial Logistical Steps

> _**Editor's Note:** The purpose in this section is to communicate the responsibilities of the CNTT levels, as they pertain to the networking solution, and how they relate (i.e. what goes in each bucket). The initial content below needs to be expanded with examples of material representative of the scope for each bucket, and refined. It is expected this area be enhanced to help authors in various CNTT levels understand their purview, and ultimately be deleted._

As with most CNTT subsystems, responsibility for Objectives, Requirements, Guidelines, etc. is divided among the CNTT constituencies, as follows:
- **Tech:** High-level strategy and other informative writings
  - e.g. Executive summary, considerations, intent, vision, etc.
- **RM:** Generic modeling and abstraction
  - e.g. Guidelines and other information applicable to all RAs
  - Overall theory of operation
- **RA-x:** architecture, APIs and other service level details
- **RI-x:** networking information for the relevant lab or POD
  - Considerations related to differences between target architecture (RM 5.1) and current RI implementation
  - Factors specific to supporting RC
  - Known non-conformances
- **RC:** Details related to qualification
  - Implications of testbed network environment vs. production environments

<a name="5.1.5"></a>
### 5.1.5 Network Layering and Concepts

Cloud and Telco networking are layered, and it is very important to keep the layering dependences low to enable security, separation and portability in between multiple implementations.

These explanations for Layering and Concepts are likely too rich and verbose for a CNTT document entry, but it is important that we first understand and agree on these concepts before we start entering text that could be misunderstood.

### Underlay and Overlay Networking concepts

The ETSI NFV model divide networking in an Underlay and an Overlay Network layer. The purpose with this layering is to ensure separation of the SW Virtualization tenants Overlay Networks from each other, whilst allowing the traffic to flow on the shared Underlay Network in between all Ethernet connected HW units.

The Overlay Networking separation is often done through encapsulation e.g. through VxLAN on the Underlay Networks e.g. based on L2 (VLAN) or L3 (IP) networks.

In some instances, the SW Virtualization Tenants can bypass the Overlay Networking encapsulation to achieve better performance or network visibility/control. A common method to bypass the Overlay Networking encapsulation is the usage of SR-IOV that effectively hands up the NIC Physical and Virtual Functions on the NIC to the SW Virtualization Layer and Tenants. In these cases, the Underlay Networking must handle the separation e.g. through a Virtual Termination End Point (VTEP) that encapsulate the Overlay Network traffic.

### Software Defined Networking control concepts of the Underlay Networking

VTEP could be manually provisioned in the Underlay Networking or be automated and controlled through a Software Defined Networking interfaces to the Underlay Networking in the HW Infrastructure Layer. Due to the many different facets of Software Defined Networking we will here denote them SDN Underlay (SDNu).

When there are multiple simultaneous SW Virtualization Layers on the same HW Infrastructure, there is a need to ensure Underlay networking separation in the HW Infrastructure Layer. This separation can be done manually through provisioning of a statically configured separation of the Underlay networking in the HW Infrastructure Layer. A better and more agile usage of the HW Infrastructure is to have an authoritative SDN provisioning controller function (here denoted SDNuP) that can be controlled through an automation interface from a HW Infrastructure Orchestrator. The main tasks for the SDNuP are to discover and establish the Underlay resources and then ensure separation of the shared HW Infrastructure Underlay networking resources.

Multiple instances of a Containerized Virtualization Layer (CaaS) running on an Infrastructure as a Service (IaaS) Virtualization Layer could make use of the IaaS layer to handle the required Underlay Networking separation. In these cases, also the IaaS Virtualization Infrastructure Manager (VIM) could include a SDNu control interface enabling automation.

### Hardware and Software Infrastructure Layer concepts

For Cloud implementations of multiple well separated simultaneous SW Virtualization domains on a shared HW Infrastructure there must be a separation of the hardware resources e.g. servers and the Underlay Networking resources that interconnect the hardware resources e.g. through a switching fabric.

To allow multiple separated simultaneous SW Virtualization domains onto a shared switching fabric there is a need to split up the Underlay Networking resources into non overlapping addressing domains
on suitable protocols e.g. VxLAN with their VNI Ranges. This separation must be done through an
administrative domain that could not be compromised by any of the individual SW Virtualization domains either by malicious or unintentional Underlay Network mapping or configuration.

The ETSI NFVI Infrastructure Management thus must be split into two distinct layers that can be referred to as HW Infrastructure Layer and SW Infrastructure Layer which can be managed separately from different administrative domains. When there are multiple separated simultaneous SW Virtualization domains, they have to be possible to be individual administrative domains.

Referenced ETSI NFV model in the Architectural Framework, [ETSI GS NFV 002 V1.2.1.](https://www.etsi.org/deliver/etsi_gs/NFV/001_099/002/01.02.01_60/gs_NFV002v010201p.pdf)

### Switch Fabric and SmartNIC concepts for Underlay Networking separation

The HW Infrastructure Layer can implement the Underlay Networking separation in any type of packet handling component. This may be deployed in many different ways depending on target use case requirements, workload characteristics and available platforms. Two of the most common ways is 1. within the physical Switch Fabric and 2. in a SmartNIC connected to the Server CPU being controlled over a management channel that is not reachable from the Server CPU and its host software. In either way the Underlay Networking separation is controlled by the HW Infrastructure Manager.

In both cases the Underlay Networking can be externally controlled over the SDNu interface, that must be instantiated with appropriate Underlay Networking separation for each of the SW Virtualization administrative domains.

Two exemplifications of different common HW realizations of Underlay separation in the HW Infrastructure Layer can be seen in the figure below.

![RM_NW_Concepts_Layering-HWInfra_Underlay_Examples](https://user-images.githubusercontent.com/38792667/77347741-985c3f80-6d38-11ea-9479-489d13668d27.jpg)

### SDN Overlay and SDN Underlay concepts, layering and relationships

An SDN Overlay controller (here denoted SDNo) is responsible for managing the SW Virtualization Layer virtual switching that manages the Overlay Network switching and encapsulation, and mapping onto the Underlay Networks.

In cases where the V/CNF bypasses the SW Virtualization Layer virtual switching e.g. high performance applications using SR-IOV, there is a need for the HW Infrastructure Layer to perform the encapsulation and mapping onto the Underlay Networking. This is controlled by the SDN Underlay controller (SDNu) that is authoritative and ensures the Overlay Networking separation on the shared Underlay Networking resources.

SDNo controllers can request Underlay encapsulation and mapping to be done by signaling to an SDNu controller. There are however today no standardized way for this signaling and by that there is a missing reference point and API description in this architecture. Examples of useful concepts for this interfaces would be L2GW (OpenStack) and OVSDB.

For deployments with multiple SW Virtualization instances sharing the same Underlay Networking resources, it is the SDNu (or SDNuP) responsibility to ensure separation of the shared Underlay resources and to set up appropriate enforcements in the Underlay Networking forwarding plane since each SW Virtualization
instance or V/CNF that bypasses its local virtual switching instance cannot be trusted. Any fault or misconfiguration in such instances could potentially destroy all networking in the shared Underlay Networking.

Two use case examples with both SDNo and SDNu controllers depicting a normal virtual switch encapsulating SW Virtualization Infrastructure instance and another high performance oriented SW Virtualization Infrastructure instance (e.g. using SR-IOV) are described in the figure below. The examples are showing how the encapsulation and mapping could be done in the virtual switch or in a SmartNIC on top of a statically provisioned underlay switching fabric, but another example could also have been depicted with the SDNu controlling the underlay switching fabric without usage of SmartNICs.

![SDN_Controller_relationships](https://github.com/cntt-n/CNTT/tree/master/doc/tech/figures/RM_NW_Concepts_Layering-SDNo_SDNu_Examples-PA4.jpg)

### Programmable Networking Fabric

The concept of a Programmable Networking Fabric pertains to the ability to have an effective forwarding pipeline (a.k.a. forwarding plane) that can be programmed and/or configured without any risk of disruption to the shared Underlay Networking that is involved with the reprogramming for the specific efficiency increase.

The forwarding plane is distributed by nature and must be possible to implement both in switch elements and on SmartNICs (managed outside the reach of host SW) that both can be managed from a logically centralized control plane residing in the HW Infrastructure Layer.

The logically centralized control plane is the foundation for the authoritative separation in between different SW Virtualization domains or Bare Metal Network Function applications that are regarded as untrusted both from the shared layers and each other.

Although the control plane is logically centralized, scaling and control latency concerns must allow the actual implementation of the control plane to be distributed when required.

All VNF, CNF and SW Virtualization acceleration or specific support functionality that could be programmed in the forwarding plane must be confined to the well separated sections or stages of any shared Underlay Networking. A practical example could be a SW Virtualization instance or VNF/CNF that control a NIC/SmartNIC where the Underlay Networking (Switch Fabric) ensures the separation in the same way as it is done for SR-IOV cases today.

The nature of a shared Underlay Network that shall ensure separation and be robust is that all code in the forwarding plane and in the control plane must be under the scrutiny and life cycle management of the HW Infrastructure Layer.

This also imply that programmable forwarding functions in a Programmable Networking Fabric are shared resources and by that will have to get standardized interfaces over time to be useful for multi-vendor architectures such as ETSI NFV. Example of such future extensions of shared functionality implemented by a Programmable Networking Fabric could be L3 as a Service, Firewall as a Service and Load Balancing as a Service.

Note: Appliance-like applications that fully own its infrastructure layers (share nothing) could manage and utilize a Programmable Networking Fabric in many ways, but that is not a Cloud implementation and falls outside the use cases for these specifications.

### Networking Reference Model

The Networking Reference Model depicted in the figure below is based on the ETSI NFV model and has a strict separation of the HW Infrastructure and SW Infrastructure Layers in NFVI. It enables multiple well separated simultaneous SW Virtualization domains allowing a mix of CaaS on Metal, CaaS on IaaS and IaaS on a shared HW infrastructure.
 
![RM_NW_Concepts_Layering-RMNW_ETSINFV](https://user-images.githubusercontent.com/38792667/77347878-ce012880-6d38-11ea-9bbc-537630ad17ee.jpg)

### Deployment example of a Networking Reference Model

A Networking Reference Model deployment example is depicted in the figure below to demonstrate the mapping to ETSI NFV reference points with additions of packet flows through the infrastructure layers and some other needed reference points. The example illustrates individual responsibilities of a complex organization with multiple separated administrative domains here represented with separate colors.

The example is a rather common example scenario for operators that modernize their network function implementations during a rather long period of migration from VNFs to Cloud Native CNFs. Today the network functions are predominantly VNFs on IaaS environments and the operators are gradually moving a selection of these into CNF on CaaS that either sit on top of the existing IaaS or directly on Bare Metal. It is expected that there will be multiple CaaS instances in most networks since it is not foreseen any generic standard of a CaaS that will be capable to handle all types of CNFs and also have a decoupled Life Cycle Management from all individual CNFs from a multi-vendor community. 

![RM_NW_Concepts_Layering-RMNW_DeploymentExample](https://user-images.githubusercontent.com/38792667/77347922-e2ddbc00-6d38-11ea-86db-a09d406998db.jpg)
