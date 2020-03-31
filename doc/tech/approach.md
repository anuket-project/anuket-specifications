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

### 5.1.2 Networking Principles & Strategy

•	**Abstraction**: A standardized layer between Virtualization Layer domains and the Networking Hardware layer resource pool hiding the implementation details of the Networking Hardware.
Note: This Principle may be deployed in many different ways depending on target use case requirements, workload characteristics (different algorithms implementing pipeline steps) and available platforms. This includes network functions running on server nodes with our without programmable HW acceleration, or functions running on a programmable standalone network switch in the network.

•	**Agnosticity** : Build Network Fabric that can carry any type of workload in terms of :

      o	Workload type : Can be Control, User and Management plan

      o	Workload supported acceleration Technologies : SRIOV or DPDK based workload
 
•	**Automation**: Full Automation, starting from Fabric provisioning to automation of VNF/CNF onboarding

•	**Openness**: All CNTT networking is based on open API ( NBI and SBI )  and Open source SDN controllers integration 

•	**Programmability**: should be based on state of art programmable fabric.

•	**Scalability**: should be scalable to handle all traffic traverse North-South and East-West.

•	**Multi-Cloud**: should be capable to handle any VNF , CNF and BareMetal workload

•	**Telco grade**: should be a Telco grade Fabric and SDN to fulfil Telco requirements such as Service chaining , Network Slicing,...etc
•	**Edge**: Can be extended to covers the edge use cases

•	**Future prove**: should be support a new acceleration technologies like smart NIC 




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
