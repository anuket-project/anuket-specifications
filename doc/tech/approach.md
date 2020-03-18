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
### 5.1.1 Networking Scope
According to the ETSI NFV Model, Networking alongside Compute and Storage, is an integral part of the Network Function Virtualisation Infrastructure (NFVI). The general function of Networking in the NFV context is to provide the connectivity between various virtualised and non-virtualised resources required for a delivery of a Network Service. Such a connectivity may manifest itself as a virtualised network between VMs or Containers (e.g. overlay networks managed by SDN Controllers, or programmable fabrics that provide such connectivity natively) or as an integration into the Infrastructure Hardware level for offloading some of the Network Functions into this level. 

The main concern of this specification, is the normalization of the integration reference points between different layers of the NFV architecture stack.  In the Networking context the primary focus is directed on the packet flow and control flow interfaces between Virtualization level (be it IaaS or CaaS type of virtualisation) and Networking Hardware resources, as well as on related integration into MANO level (Hardware/ Network Infrastructure Management/Control, Orchestration).  The Networking Sope includes hence a definition of a normalized Abstraction layer between Virtualization Layer domains and the Networking Hardware layer resource pool in a way that the implementation details of the Networking Hardware are not visible to the VNFs/CNFs, and preferably not even visible to the Virtualization layer.


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
