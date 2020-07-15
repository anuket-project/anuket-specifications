[<< Back](../../ref_model)
# Appendix A - Guidelines For Application Vendors
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [A.1 Goals](#A.1)
* [A.2 Intro and Terminology](#A.2)
* [A.3 Exception List](#A.3)
* [A.4 Links](#A.4)
* [A.5 Hardware-Dependent Coding Policies](#A.5)
* [A.6 VNF Design and Implementation Guidelines](#A.6)
* [A.7 Miscellaneous](#A.7)

<a name="A.1"></a>
## A.1 Goals
This Appendix has two goals:
1. Provide guidance to VNF or more generally Application vendors on how to consume CNTT Reference Model and Architectures
2. Provide usable definitions of maturity levels for VNF software architecture between Physical-to-Virtual migration and “Cloud Native”.

The goal is not to be prescriptive on how to re-architect existing or architect new applications but rather staying within scope of focusing on interface and interaction between applications and platform.

<a name="A.2"></a>
## A.2 Intro and Terminology

Taking advantage of RM and RA environments with common capabilities, applications can be developed and deployed more rapidly, providing more service agility and easier operations. The extent to which this can be achieved will depend on levels of decoupling between application and infrastructure or platform underneath the application:

**1. Infrastructure**:
- a. Application functionality or application control requires infrastructure components beyond RM profiles or infrastructure configuration changes beyond RA exposed APIs. Generally, such an application is tightly coupled with the infrastructure which results in an Appliance deployment model.
- b. Application control using RA APIs finds node (already configured in support of the profiles) with required infrastructure component(s), and in that node using RA APIs configures infrastructure components that make application work. Example is application that to achieve latency requirements needs certain acceleration adapter available in RM profile and is exposed through RA APIs.
- c. Application control using RA APIs finds node (already configured in support of the profiles) with optional infrastructure component(s), and in that node using RA APIs configures infrastructure component(s) that make application work better (like more performant) than without that infrastructure component. Example is application that would have better TCO with certain acceleration adapter but can also work without it.
- d. Application control using RA APIs finds general profile node without any specific infrastructure component.

**2. Platform Services**
- a. Application functionality or application control can work only with its own components instead of using RA-defined Platform Services.
- b. With custom integration effort, application can be made to use RA-defined Platform Services.
- c. Application is designed and can be configured for running with RA-defined Platform Services.

**3. Application Resiliency**
- a. Application was designed and tested to run only on Carrier Grade platform with predictable infrastructure availability and performance.
- b. Application was designed and tested for full failures of infrastructure HW and SW components, but not for infrastructure impairment as the Application still needs predictable infrastructure performance (like CPU cycles and network latencies).
- c. Application was designed to run on shared Cloud platforms and tested for resilience to infrastructure impairments.

Relevant for sizing infrastructure and application operations (which often is another telco organizational unit or external 3rd party) is also how much is application decomposed from:

**4. Other application functionality** (decomposition and manageability for scaling, availability and upgrades):
- a. Application consists of huge monolithic components including algorithms that have different scaling (for example depending on type of traffic) and/or availability requirements.
- b. Application consists of smaller tightly coupled components.
- c. Decomposed application with loosely- or decoupled components.
- d. Availability like N+K or 1+1 is defined during application design and not configurable at deployment time.
- e. Mutable or immutable instances of application components.


<a name="A.3"></a>
## A.3 Exception List

As Part of the [Transition Plan](../../gov/chapters/chapter09.md#9.2) described in the adoption strategy, following table explains the exceptions allowed in this RM release. The list of Exceptions described here are considered to be against CNTT principles and will be removed in future releases as soon as an alternative technology that is aligned with CNTT principles develops and matures.

| Ref        | Type       | Name       | Description                                                           |
|------------|------------|------------|-----------------------------------------------------------------------|
| rm.exc.001 | Technology | SRIOV      | This exception allows workloads (VNF/CNF) to rely on SR-IOV over PCI-PassThrough technology. |


<p align="center"><b>Table A-1:</b> Exceptions allowed in this RM release</p>

<a name="A.4"></a>
## A.4 Links

<a name="A.5"></a>
## A.5 Hardware-Dependent Coding Policies

As described in the Principles sections of RM Chapter 1, features that require hardware-dependent code in the workload are prohibited in CNTT compliant implementations. This principle is henceforth referred to as the "Abstraction Principle". Note, this prohibition does not apply to the Compute node host software (e.g., host OS). Within the Infra, hosts are expected to have software that is customized for the specific hardware equipped. However, the intent is that these software drivers and higher layers will abstract the Capabilities they enable, thereby exposing them with an open API. An example of exposing capabilities in this manner is implemented in the Virtio family of APIs. This requirement is in support of VNF abstraction and portability of VNFs across the Infra landscape.

CNTT realizes there are implications and limitations to the ability to live by the Abstraction Principle. A textbook example of a Capability that transgresses this principle, is SR-IOV over PCI-PT <sup>1)</sup>. Other, less notable, yet very important examples include GPU and other acceleration hardware, such as FPGA. A less obvious, yet critically important example is the VNF program(s) itself. As workloads are coded in native microarchitecture opcodes, microarchitectures' instruction sets effectively constitute ABIs (Application Binary Interface). Additionally, the VNF programs may or may not, attempt to execute vendor-specific extensions to base instruction sets, such as de facto x86 or ARM.

Solving the problems associated with implementing the Abstraction Principle is a work in progress. CNTT has not solved all of the associated problems, nor has the industry. As technology evolves and more designs incorporate cloud native concepts, these problems will be addressed. This appendix is specifically intended to provide CNTT policies to manage these situations as they exist today, and their exceptions and transitions, as the technology around and supporting the Abstraction Principle matures.

<sup>1)</sup> For a detailed description of the mechanisms underlying PCI-PT (PCI-PassThrough), refer to [Section 8.1](../../common/technologies.md#8.1) of Relevant Technologies.

Several specific technology areas have been identified by CNTT as using an ABI impacted by the Abstraction Principle, as follows:
- SR-IOV over PCI-PT
- GPU/NPU
- FPGA/Other Acceleration
- CPU Instruction Sets and Extensions

The preceding list is not exhaustive; technologies will be added as required.

Current CNTT Policies:

**SR-IOV over PCI-PT:**

CNTT recognizes that today, SR-IOV over PCI-PT provides a critical Capability for increased throughput over network interfaces at an economical cost. As such, the CNTT approach to SR-IOV over PCI-PT is to (detailed policy language under development; to be tied in with VNF Evolution).

Without arguing for or against SR-IOV over PCI-PT, CNTT provides the following anecdotes which have been raised in discussions over SR-IOV:
- SR-IOV over PCI-PT mitigates the need for duplicated servicing of interrupts from unbuffered (i.e. small buffer) NICs, however it does not reduce the number of frame reception driven interrupts which much be serviced.
- SR-IOV over PCI-PT increases the Fabric management complexity, as encapsulation must be applied by the ToR/Leaf interface and the encapsulation must be managed as VNFs and/or networks are added/deleted from the Tenant. Therefore, performance isn't the only factor; fabric touch points and Service Chaining must also be considered.
- Indications are that technologies such as DPDK, VPP, FD.io and others offer comparable throughput, today.<sup>(Citations Needed)</sup>


**GPU/NPU:**
<content needed>

**FPGA/Other Acceleration:**
<content needed>

**CPU Instruction Sets and Extensions:**
<content needed>

End of policies.

<a name="A.6"></a>
## A.6 VNF Design Guidelines
A number of software design guidelines (industry best practices) have been developed over the years including micro-services, cohesion and coupling. In addition to the industry best-practices, there are additonal guidelines and requirements specified by  ONAP in "[VNF or PNF Requirements Documentation](https://onap.readthedocs.io/en/latest/submodules/vnfrqts/requirements.git/docs/index.html)." This section does not supplant these well-known guidelines and practices. The content here only draws attention to some other design consideration that VNF Developers need to incorporate in their practices. Please note that some of these guidelines may be incorporated by operators in their contracts with VNF Vendors.


These guidelines are written in an informal style and any resemblance to requirements is incidental. The VNF Developer **should** ensure that their software and the resultant VNF image:
1. does not contain malicious code (e.g., malware, logic bombs, etc.).
1. does not contain code such as daemons that exposes them to risk.
1. does not contain clear text secrets.
1. are only created with content and files from trusted sources.
1. are only packaged with files that have been found free of malware and vulnerabilities.

Additionally, in the design and implementation of their software, the VNF Developer **should** follow the guidance in the:
1. [CSA Security Guidance for Critical Areas of Focus in Cloud Computing (latest version)](https://cloudsecurityalliance.org).
1. [OWASP Cheat Sheet Series (OCSS)](https://github.com/OWASP/CheatSheetSeries) from the [Open Web Application Security Project](https://www.owasp.org).

The VNF Developer **should** ensure that their code is not vulnerable to the [OWASP Top Ten Security Risks](https://owasp.org/www-project-top-ten/) created by the [Open Web Application Security Project](https://www.owasp.org).


<a name="A.7"></a>
## A.7 Miscellaneous
### A.7.1 VNF Network Monitoring Capabilities - UseCase.
Network Monitoring capabilities exposed by NFVI Platform are used for the passive observation of VNF-specific traffic traversing the NFVI when:
* Performance issues and/or packet drops reported in VNF
* Determining performance bottle necks at VNF level
* Doing anomaly detection and network forensics

**Note:** It is responsibility of NFVI Platform to expose capability to create virtual interface having mirrored traffic from monitored VNF. This port can be attached to Monitoring VNF so that all traffic from Monitored VNF would be available for troubleshooting/debugging purpose.
