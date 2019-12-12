[<< Back](https://cntt-n.github.io/CNTT/)
# Common NFVI Telco Taskforce

## Table of Contents
* [1. Overview](#1.0)
* [2. Scope](#2.0)
* [3. Principles](#3.0)
* [4. Technology Direction](#4.0)
  * [4.1 IO Virtualisation](#4.1)
  * [4.2 SmartNICs](#4.2)
  * [4.3 Acceleration Cards](#4.3)
  * [4.4 FPGA](#4.4)
  * [4.5 GPUs/NPUs](#4.5)
  * [4.6 EPA/NFD](#4.6)
* [5. Available Specifications](#5.0)

<a name="1.0"></a>
## 1. Overview

Initially organized early in 2019, the Common Network Function Virtualisation Infrastructure Telecom Taskforce (CNTT) was initially created in response to rapid changes in how networking applications are being designed, built and managed, plus a growing recognition of a perceived functional gap between the previous standard infrastructure models and the architectures needed to support Network Function Virtualization (NFV) applications.  Organizationally the Common Telco Network Function Virtualisation Infrastructure (NFVI)  project, jointly hosted by GSMA and the Linux Foundation, operates as an open committee responsible for creating and documenting an industry aligned Common NFVI Framework.  The CNTT group was created with the intent that it would create the NFVI framework, and eventually morph into an on-going project under the auspices of the GSMA and the Linux Foundation umbrellas.  The final on-going operational form of the group will be determined as the project evolves. 

<a name="2.0"></a>
## 2. Scope

Within the framework of the Common Telecom NFVI vision, there are three levels of documents needed to document the components and allow the practical application of the systems. They are, as highlighted in **Figure 1**:  **Reference Model**, **Reference Architecture**, and **Reference Implementation**.

<p align="center"><img src="./figures/tech_scope_doc_types.png" alt="scope" title="Document Types" width="100%"/></p>
<p align="center"><b>Figure 1:</b> Scope of CNTT</p>

<a name="2.1"></a>
## 2.1 Specification Types

- **Reference Model**: focuses on the __**NFVI Abstraction**__ and how NFVI services and resources are exposed to VNFs. It written at a high enough level that as new **Reference Architectures** and **Reference Implementations** are added, the model document should require few or no changes. Additionally, the Reference Model is intended to be neutral towards VMs or Containers.
- **Reference Architecture**: High level NFVI system components and their interactions that takes the Reference Model goals and maps them to something that has components in the real world.  It is expected that at least one, but not more than a few, Reference Architecture will conform to the Reference Model.  The intention whenever possible to use existing elements, rather than specify entirely new architectures in support of the high-level goals specified in the **Reference Model**.
- **Reference Implementation**: Builds on the requirements and specifications developed in the other two documents and adds details so that it can be implemented.  Each Reference Architecture is expected to be implemented by at least one Reference Implementation.

Below is a diagram of the different artifacts that will need to be created to support the implementation of the abstract concepts presented in the **Reference Model**, which are then applied to create the **Reference Architecture**, that will be deployed using the requirements spelled out in the **Reference Implementation**.

<p align="center"><img src="./figures/tech_scope_3.png" alt="scope" title="Document Types" width="100%"/></p>
<p align="center"><b>Figure 2:</b> Description of the possible different levels of CNTT artefacts</p>

<a name="3.0"></a>
## 3. Principles

Any specification work created within CNTT **must** obey to set of principles specified by CNTT:

[Reference Model Principles](../ref_model/chapters/chapter01.md#13-principles)
[Reference Architecture Principles](../ref_arch#principles)

<a name="4.0"></a>
## 4. Technology Direction

<a name="4.1"></a>
### 4.1 IO Virtualization

There are different ways of which IO devices (such as NICs) are presented to VMs for consumption by those VMs. Here is a list of current methods of existing IO Virtualisatin:

- Para-Virtualization method (software only).
- Direct assignment with VT-d.
- Device Sharing with SR-IOV & VT-d.
- Para-Virtualisation method (Hardware support).

**Figure 3** below shows some of the relevant IO Virtualization techniques.

<p align="center"><img src="./figures/tech_iov.png" alt="scope" title="Document Types" width="100%"/></p>
<p align="center"><b>Figure 3:</b> Relevant IO Virtualisation Techniques</p>

<a name="4.1.1"></a>
#### 4.1.1 Para-virtualization method (software only)

This is the preferred method of IO virtualisation as it provides flexibility and full abstraction of workloads from the underlying infrastructure. It usually relies on standard IO interfaces that are implemented in software.
For Networking, there are two common networking interfaces used: virtio-net for KVM/QEMU and VMXNET for VMware.

Using a standard interface for IO means that applications don’t need to run any proprietary software drivers for specific hardware vendors and the implementation of that application is completely agnostics of the hardware used.

**Figure 4** below shows the typical components of a para-virtualised interface: 
- frontEnd driver: The frontEnd driver is an off-the-shelf driver that runs on the guest machine
- backEnd driver: runs on the Hypervisor and is responsible of bridging standard communications coming from applications to a hardware specific ones. 

This nature of this disaggregation is what gives the para-virtualised interfaces the flexibility that makes them favourable in a virtualised environment.

The downside of para-virtualisation interfaces is the involvement of the hypervisor which may introduce latency and jitter that can impact the performance.

<p align="center"><img src="./figures/tech_virtio.png" alt="virtio" title="Document Types" width="100%"/></p>
<p align="center"><b>Figure 4:</b> Para-Virtualised interface components (software only).</p>

<a name="4.3"></a>
### 4.2 SmartNICs

<a name="4.4"></a>
### 4.3 Acceleration Cards

<a name="4.5"></a>
### 4.4 FPGAs

<a name="4.6"></a>
### 4.5 GPUs/NPUs

<a name="4.7"></a>
### 4.6 EPA/NFD

<a name="5.0"></a>
## 5. Available Specifications
* [Reference Model](../ref_model)
* [Reference Architecture](../ref_arch)
* [Reference Implementation](../ref_impl)
* [Reference Certification](../ref_cert)
