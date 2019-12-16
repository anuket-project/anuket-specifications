[<< Back](../../ref_model)
# Appendix A - Guidelines For VNF Vendors
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [A.1 Goals](#A.1)
* [A.2 Intro and Terminology](#A.2)
* [A.3 VNF Evolution Phases](#A.3)
* [A.4 Links](#A.3)
* [A.5 Hardware-Dependent Coding Policies](#A.4)
* [A.6 Miscellaneous](#A.5)

<a name="A.1"></a>
## A.1 Goals
This Appendix has two goals:
1. Provide guidance to VNF or more generally Application vendors on how to consume CNTT Reference Model and Architectures
2. Provide usable definitions of maturity levels for VNF software architecture between Physical-to-Virtual migration and “Cloud Native”.

The goal is not to be prescriptive on how to re-architect existing or architect new applications but rather staying within scope of focusing on interface and interaction between applications and platform. So, it will primarily look at Operational impact (in steps like Install, Configure, Validate, Operate) towards full lifecycle automation supporting CI/CD.

<a name="A.2"></a>
## A.2 Intro and Terminology
(Summary status and trends of ETSI NFV and Cloud.)

Terminology used or introduced:

-	Decoupling, Loose Coupling = Loosely coupled system is one in which each of its components has, or makes use of, little or no knowledge of the definitions of other separate components. Loose coupling is the opposite of tight coupling. [1]

-	Encapsulation = Restricting of direct access to some of an object's components. [2]

-	Appliance deployment model = Application has tight coupling with underlying Platform even if the application is virtualized or containerized.

-	Tenant/Cloud deployment model = Tenant brings applications that are decoupled from the platform provided by Cloud operator. Tenant and Cloud operator are normally different legal entities.

-	Application Control = Any way of controlling tenant’s application. Depending on RA and technologies used, it can be tenant’s VNFM or Orchestration SW, or Platform capability.

-	Decomposition = Decomposition (also known as factoring) is breaking a complex system into parts that are easier to program and maintain. [3]

-	Resilience = Resilience is the ability to provide and maintain an acceptable level of service in the face of various faults and challenges to normal operation. [4]

-	Observability = Observability is a measure of how well internal states of a system can be inferred from knowledge of its external outputs. [5]


<a name="A.3"></a>
## A.3 VNF Maturity Levels
(And how they map to CNTT RAs)

Taking advantage of CNTT pre-defined environments with common capabilities, applications can be developed and deployed more rapidly, providing more service agility and easier operations. The extent to which this can be achieved will depend on levels of decoupling between application and infrastructure or platform underneath the application:

**1. Infrastructure**:
- a. Application functionality or application control require infrastructure components beyond RM profiles or requires infrastructure configuration changes beyond RA exposed APIs. Generally, such application is tightly coupled with infrastructure which results in Appliance deployment model. 
- b. Application control using RA APIs finds node with required infrastructure component(s), and in that node using RA APIs configures infrastructure components that make application work. Example is application that requires certain acceleration adapter available in RM profile and is exposed through RA APIs.
- c. Application control using RA APIs finds node with optional infrastructure component(s), and in that node using RA APIs configures infrastructure component(s) that make application work better (like more performant) than without that infrastructure component. Example is app that would work better with certain acceleration adapter but can also work without it.
- d. Application control using RA APIs finds general profile node without any specific infrastructure component.

**2. Platform as a Service** (as per RA2 WIP: common services starting from Load Balancer and Store State, also typically includes Logging and Telemetry):
- a. Application functionality or application control can work only with its own components implementing platform services already provided by CNTT-defined PaaS.
- b. With custom integration effort, application can be made to use CNTT-defined PaaS.
- c. Application is designed and can be configured for running with CNTT-defined PaaS.

**3. Application Resiliency** (Note: “resilient” is the 1st word describing “enabled loosely coupled systems” in CNCF Cloud Native Definition [6])
- a. Application was designed and tested to run only on Carrier Grade platform with predictable infrastructure availability and performance
- b. Application was designed and tested for HW and SW component full failures but not for infrastructure impairment which still needs predictable infrastructure performance (like CPU cycles and network latencies)
- c. Application was designed to run on shared Cloud platforms and tested for resilience to infrastructure impairments

Relevant for sizing infrastructure and application operations (which often is another telco organizational unit or external 3rd party running on telco cloud) is also how much is application decomposed from:

**4. Other application functionality** (decomposition, manageability):
- a. Application consists of huge monolithic components including algorithms that have different scaling (for example depending on type of traffic) and/or availability requirements
- b. Application is decomposed into smaller components that are tightly coupled by same versioning (upgrading all components or none)
- c. Decomposed application has components that can be upgraded separately
- d. Availability like N+K or 1:1 is defined during application design and not configurable at deployment time.
- e. Patching/upgrading existing running application components or always rolling out new ones.

(WIP: After agreeing above criteria, next is defining number and naming of Maturity Levels and mapping the criteria to different levels.)

<a name="A.4"></a>
## A.4 Links

Wikipedia 1. https://en.wikipedia.org/wiki/Loose_coupling , 2. https://en.wikipedia.org/wiki/Encapsulation_(computer_programming) , 3. https://en.wikipedia.org/wiki/Decomposition_(computer_science) , 4. https://en.wikipedia.org/wiki/Resilience_(network) , 5. https://en.wikipedia.org/wiki/Observability .

CNCF Cloud Native Definition v1.0 from June 2018, 6. https://github.com/cncf/toc/blob/master/DEFINITION.md .

<a name="A.5"></a>
## A.5 Hardware-Dependent Coding Policies

As described in the Principles sections of RM Chapter 1, features that require hardware-dependent code in the workload are prohibited in CNTT compliant implementations. This principle is henceforth referred to as the "Abstraction Principle". Note, this is not the case for the Compute node host software (e.g., host OS). Within the Infra, hosts are expected to have software that is customized for the specific hardware equipped. However, the intent is that these software drivers and higher layers will abstract the Capabilities they enable, thereby exposing them with an open API. An example of exposing capabilities in this manner is implemented in the Virtio family of APIs. This requirement is in support of VNF abstraction and portability of VNFs across the Infra landscape.

CNTT realizes there are implications to this and limitations to the ability to live by the Abstraction Principle. A textbook example of a Capability that transgresses this principle, is SR-IOV. Other, less notable, yet very important examples include vGPUs and other acceleration hardware, such as FPGA. A less obvious, yet critically important example is the VNF program(s) itself. As workloads execute native microarchitecture opcodes, those instruction sets effectively constitute an ABI (Application Binary Interface). Additionally, these programs may or may not, attempt to execute vendor-specific extensions to standard instruction sets, such as x86 or ARM.

Solving the problems associated with implementing the Abstraction Principle is a work in progress. CNTT has not solved all of the associated problems, nor has the industry. As technology evolves and more designs incorporate cloud native concepts, these problems will be addressed. This appendix is specifically intended to provide CNTT policies to manage these situations as they exist today,   and their exceptions and transitions, as the technology around and supporting the Abstraction Principle matures.

Several specific technology areas have been identified by CNTT as using an ABI impacted by the Abstraction Principle, as follows:
- SR-IOV
- GPU/NPU
- FPGA/Other Acceleration
- CPU Instruction Sets and Extensions

The preceding list is not exhaustive; technologies will be added as required.

Current CNTT Policies:

**SR-IOV:**

Note on CNTT VNF Transition Guidelines plan for SR-IOV with vendor-specific drivers in VNFs: Currently (end of 2019) SR-IOV is often used as most performant way of getting packets into VNFs with tradeoffs in agility (VNF onboarding), operational issues (vendor drivers in VNFs) and changes in networking and security management. The tradeoff of allowing SR-IOV Virtual Function PCI Pass Through for VNF network connectivity is acceptable only until a solution is available without vendor-specific driver and acceptable resource consumption (CPU). As other connectivity technologies with open standard interfaces improve both technically and commercially, future CNTT releases will phase out SR-IOV with vendor-specific drivers in VNFs and any other connectivity technology tightly coupling applications and infrastructure.

CNTT recognizes that today, SR-IOV provides a critical Capability for increased throughput over network interfaces at an economical cost. As such, the CNTT approach to SR-IOV is to (detailed policy language under development; to be tied in with VNF Evolution).

Without arguing for or against SR-IOV, CNTT provides the following anecdotes which have been raised in discussions over SR-IOV:
- SR-IOV mitigates the need for duplicated servicing of interrupts from unbuffered (i.e. small buffer) NICs, however it does not reduce the number of frame reception driven interrupts which much be serviced.
- SR-IOV increases the Fabric management complexity, as encapsulation must be applied by the ToR/Leaf interface and the encapsulation must be managed as VNFs and/or networks are added/deleted from the Tenant. Therefore, performance isn't the only factor; fabric touch points and Service Chaining must also be considered.
- Indications are that technologies such as DPDK, VPP, FD.io and others offer comparable throughput, today.<sup>(Citations Needed)</sup>


**GPU/NPU:**
<content needed>

**FPGA/Other Acceleration:**
<content needed>

**CPU Instruction Sets and Extensions:**
<content needed>

End of policies.

<a name="A.6"></a>
## A.6 Miscellaneous
### A.6.1 VNF Network Monitoring Capabilities - UseCase.
Network Monitoring capabilities exposed by NFVI Platform are used for the passive observation of VNF-specific traffic traversing the NFVI when:
* Performance issues and/or packet drops reported in VNF
* Determining performance bottle necks at VNF level
* Doing anomaly detection and network forensics

**Note:** It is responsibility of NFVI Platform to expose capability to create virtual interface having mirrored traffic from monitored VNF. This port can be attached to Monitoring VNF so that all traffic from Monitored VNF would be available for troubleshooting/debugging purpose.
