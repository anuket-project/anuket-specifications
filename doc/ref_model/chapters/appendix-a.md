[<< Back](../../ref_model)
# Appendix A - Guidelines For VNF Vendors
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [A.1 Goals](#A.1)
* [A.2 Intro and Terminology](#A.2)
* [A.3 VNF Maturity Levels](#A.3)
* [A.4 Links](#A.3)
* [A.5 Hardware-Dependent Coding Policies](#A.4)

<a name="A.1"></a>
## A.1 Goals
This Appendix has two goals:
1. Provide guidance to VNF or more generally Application vendors on how to consume CNTT Reference Model and Architectures
2. Provide usable definitions of maturity levels for VNF software architecture between Physical-to-Virtual migration and “Cloud Native”.

The goal is not to be prescriptive on how to re-architect existing or architect new applications but rather staying within scope of focusing on interface and interaction between applications and platform.

<a name="A.2"></a>
## A.2 Intro and Terminology
(Summary status and trends of ETSI NFV and Cloud. Decoupling application from platform. Terminology used/introduced.)

<a name="A.3"></a>
## A.3 VNF Maturity Levels
(And how they map to CNTT RAs)

<a name="A.4"></a>
## A.4 Links

<a name="A.5"></a>
## A.5 Hardware-Dependent Coding Policies

As described in the Principles sections of RM Chapter 1, features that require hardware-dependent code in the workload are prohibited in CNTT compliant implementations. This principle is henceforth referred to as the "Abstraction Principle". Note, this is not the case for the Compute node host software (e.g., host OS). Within the Infra, hosts are expected to have software that is customized for the specific hardware equipped. However, the intent is that these software drivers and higher layers will abstract the Capabilities they enable, thereby exposing them with an open API. An example of exposing capabilities in this manner is implemented in the Virtio family of APIs. This requirement is in support of VNF abstraction and portability of VNFs across the Infra landscape.

CNTT realizes there are implications to this and limitations to the ability to live by the Abstraction Principle. A textbook example of a Capability that transgresses this principle, is SR-IOV. Other, less notable, yet very important examples include vGPUs and other acceleration hardware, such as FPGA. A less obvious, yet critically important example is the VNF program(s) itself. As workloads execute native microarchitecture opcodes, those instruction sets effectively constitute an ABI (Application Binary Interface). Additionally, these programs may or may not, attempt to execute vendor-specific extensions to standard instruction sets, such as x86 or ARM.

Solving the problems associated with implementing the Abstraction Principle is a work in progress. CNTT has not solved all of the associated problems, nor has the industry. As technology evolves and more designs incorporate cloud native concepts, these problems will be addressed. This appendix is specifically intended to provide CNTT policies to manage these situations as they exist today,   and their exceptions and transitions, as the technology around and supporting the Abstraction Principle matures.

Several specific technology areas have been identified by CNTT as being impacted by the Abstraction Principle, as follows:
i. SR-IOV
i. GPU/NPU
i. FPGA/Other Acceleration
i. CPU instruction sets and extensions

Current CNTT Policies:

**SR-IOV:**

CNTT recognizes that today, SR-IOV provides a critical Capability for increased throughput over network interfaces at an economical cost. As such, the CNTT approach to SR-IOV is to <language under development>.
  
**GPU/NPU:**
<content needed>

**FPGA/Other Acceleration:**
<content needed>

End of policies.
