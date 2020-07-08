[<< Back](https://cntt-n.github.io/CNTT/)
# CNTT Technical Policies and Transition Plan

## Table of Contents
* [CNTT Policies for Managing Non-Conforming Technologies ](#7.1) 
  * [Feature Availability](#7.1.1)
  * [Hardware-Dependent Coding](#7.1.2)
  * [Current CNTT Policies](#7.1.3)
* [CNTT Technical Transition Plan ](#7.2) 

<a name="7.1"></a>
## CNTT Policies for Managing Non-Conforming Technologies

There are multiple situations where a policy, comprised of one or more compromises and/or transitions is required to address technology that does not presently conform to CNTT mandates or strategy, and hence requires explicit direction to prescribe how the situation will be treated in the present, as well as in the future. This informs application designers how RC will react when encountering such technologies during the qualification process, including flagging warnings and potentially errors which could prevent issuance of a certification badge. 

<a name="7.1.1"></a>
### Feature Availability
One such case is where CNTT strategically deems a given capability as mandatory, but the feature is a roadmap item, under development or otherwise unavailable. To address this scenario, a policy can be created to recognize the current state of the technology, and identify a Time Point (TP) in VNF Evolution when the feature will become mandatory for RC purposes.

<a name="7.1.2"></a>
### Hardware-Dependent Coding
Another such case is hardware-dependent coding. As described in the Principles sections of RM Chapter 1, features that require hardware-dependent code in a workload are prohibited in CNTT compliant implementations. This principle is henceforth referred to as the "Abstraction Principle". Note, this prohibition does not apply to the Compute node host software (e.g., host OS). Within the Infra, hosts are expected to contain software customized for the specific hardware equipped. However, the intent is that these software drivers in conjunction with software at higher layers will abstract the capabilities they enable, thereby exposing them through an open, Cloud Native API. An example of exposing capabilities in this manner is implemented in the Virtio family of APIs. This requirement is in support of VNF abstraction and portability of VNFs across the Infra landscape.

CNTT realizes there are implications to these types of prohibitions and practical limitations on the ability to live by the Abstraction Principle. A textbook example of a capability that transgresses this principle is SR-IOV over PCI-PT <sup>1)</sup>. Other, less notable, yet very important examples include vGPUs as well as virtualized manifestations of other acceleration hardware, such as FPGAs. Less obvious, yet critically important examples are the programs comprising the actual VNFs. As workloads are coded in native microarchitecture opcodes, microarchitectures' instruction sets effectively constitute ABIs (Application Binary Interface), which are by definition, dependent on a host's hardware. Additionally, the VNF programs may or may not, attempt to execute vendor-specific extensions to base instruction sets, such as de facto x86 or ARM.

Solving the problems associated with implementing the Abstraction Principle is a work in progress. CNTT has not solved all of the associated problems, nor has the industry. As technology evolves and more designs implement Cloud Native concepts, these problems will be addressed. This document is specifically intended as a one-stop-shop to capture CNTT policies which manage these situations as they exist today and their associated exceptions and transitions, and help drive the technology around and supporting the maturation of the Abstraction Principle.

<sup>1)</sup> For a detailed description of the mechanisms underlying PCI-PT (PCI-PassThrough), refer to [Section 8.1](./technologies.md#8.1) of Relevant Technologies.

Several specific technology areas have been identified by CNTT as using an ABI impacted by the Abstraction Principle, as follows:
- SR-IOV over PCI-PT
- GPU/NPU
- FPGA/Other Acceleration
- CPU Instruction Sets and Extensions

The preceding list is not exhaustive; technologies will be added as required.

<a name="7.1.3"></a>
### Current CNTT Policies

The following sets of compromises and transition plans comprise the policy for each technology subject to this document.

Be aware the compromises and transition plans contained herein, are directly related to factors which are subject to change with the evolution of technology, with changes in industry direction, with changes in standards, etc. Hence, **the policies are subject to change without notice**, and the reader is advised to consult the latest online Github revision of this chapter. All locally stored, printed or other copies should be considered obsolete.

> **Note to Authors:** Status should be set to "Proposed" when initial content is entered. Once alignment is attained following vetting and discussion, status should be set to "Aligned". Immediately prior to merge, status should be set to "In Force". When amending previously approved language, status should be changed from "In Force" to "In Force (Pending Changes)", followed by "Aligned" and ultimately, "In Force".

<a name="7.1.3.1"></a>
#### SR-IOV over PCI-PT

SR-IOV over PCI-PT transgresses the CNTT Abstraction Principle, which prohibits hardware-dependent code be required in a workload. Refer to the Abstraction Principle in RM Chapter 1 for the related rationale and details. However, CNTT recognizes that today, SR-IOV over PCI-PT provides a capability to increase throughput over network interfaces at an economical cost, that some applications as currently implemented, are highly dependent upon. As such, the CNTT approach to SR-IOV shall be:

1. At the present Time Point (TP), TP x, to enable VNFs currently dependent on SR-IOV to transition to Cloud Native technology, VNFs using SR-IOV over PCI-PT will PASS OVP qualification, but generate a WARNING indicating the functionality will be deprecated, and to transition to a Cloud Native implementation
1. At TP x+y, VNFs using SR-IOV over PCI-PT will PASS OVP qualification, but generate a WARNING indicating the functionality is deprecated and they must transition to a Cloud Native implementation
    - **y** will depend on when a technology is developed to replace SR-IOV over PCI-PT and provide an acceptable low latency access to (network interface) devices.
1. At TP x+y+z, VNFs using SR-IOV over PCI-PT will **FAIL** OVP qualification, and generate an **ERROR** indicating the functionality is prohibited

NOTE: A Time Point (TP) metric representing chronologic advancement of the CNTT VNF model is being developed in parallel under the VNF Evolution Framework. Hence, TPs referenced herein are placeholders and intended to be relative, until the absolute TPs are defined, at which point the placeholders are to be replaced with their absolute equivalents.

Without arguing for or against SR-IOV over PCI-PT , CNTT provides the following anecdotes which have been raised in discussions over SR-IOV:
- SR-IOV over PCI-PT mitigates the need for duplicated servicing of interrupts from unbuffered (i.e. small buffer) NICs. However, it does not reduce the number of frame reception driven interrupts which much be serviced.
- SR-IOV over PCI-PT increases the Fabric management complexity, as encapsulation must be applied by the ToR/Leaf interface and the encapsulation must be continually updated as VNF interfaces (i.e. vNICs) and/or networks are added/deleted from Tenant(s) served by that interface. Therefore, performance isn't the only factor; fabric touch points and Service Chaining must also be considered.
- Indications are that technologies such as DPDK, VPP, FD.io and others offer comparable throughput, today.<sup>(Citations Needed)</sup>

<a name="7.2"></a>
## CNTT Technical Transition Plan

Overall Transition Plan is explained in the Governance [Adoption](../gov/chapters/chapter09.md#9.3) strategy.
