[<< Back](../../kubernetes)

# 1. Overview
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Introduction.](#1.1)
* [1.2 Terminology](#1.2)
* [1.3 Principles](#1.3)
  * [1.3.1 Cloud Native.](#1.3.1)
* [1.4 Scope](#1.4)
* [1.5 Vision](#1.5)
* [1.6 Approach](#1.6)
* [1.7 Roadmap](#1.7)


<a name="1.1"></a>
## 1.1 Introduction

> to be written


<a name="1.2"></a>
### 1.2 Terminology

For the terminology refer to the [glossary](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/glossary.md#11.1.4) 


<a name="1.3"></a>
## 1.3 Principles

Kubernetes Reference Architecture must obey to the following set of principles:
- [CNTT Reference Model Principles](../../../ref_model/chapters/chapter01.md#1.3)
- [CNTT Reference Architecture Principles](../../#principles)

>Any Kubernetes specific principles needs to be added here.

<a name="1.3.1"></a>
### 1.3.1 Cloud Native Principles

According to CNCF TOC (Technical Oversight Committee), following is the definition of Cloud Native:
>CNCF Cloud Native Definition v1.0
>Approved by TOC: 2018-06-11

>“Cloud native technologies empower organizations to build and run **scalable** applications in modern, **dynamic environments** such as public, private, and hybrid clouds. Containers, **service meshes**, **microservices**, **immutable infrastructure**, and **declarative APIs** exemplify this approach.

>These techniques enable **loosely coupled** systems that are **resilient**, **manageable**, and **observable**. Combined with **robust automation**, they allow engineers to make high-impact changes frequently and predictably with minimal toil.

>The Cloud Native Computing Foundation seeks to drive adoption of this paradigm by fostering and sustaining an ecosystem of open source, vendor-neutral projects. We democratize state-of-the-art patterns to make these innovations accessible for everyone”

The definition above is very application centric and look at cloud native from the application point of view, in here, we will try and relate those definitions to the platforms of which cloud native applications run on top of.

- **scalable**:
- **dynamic environments**:
- **service meshes**:
- **microservices**:
- **immutable infrastructure**:
- **declarative APIs**:
- **loosely coupled**:
- **resilient**:
- **manageable**:
- **observable**:
- **robust automation**:

<a name="1.4"></a>
## 1.4 Scope

> to be written
<a name="1.5"></a>
## 1.5 Vision

<a name="1.6"></a>
## 1.6 Approach


<a name="1.7"></a>
## 1.7 Roadmap




## General thoughts
***Please note that the notes below will be removed and replaced with content in the chapters of this Reference Architecture***

Kubernetes itself is a “system for automating deployment, scaling, and management of containerized applications” and therefore Kubernetes place within our architecture should be closely linked to the application lifecycle (this is especially important when considering bare-metal containerisation). However, it is very important to point out that a CaaS also consist of other open source projects, or add-ons, such as:
- CNI-compliant network plugins
- CSI-compliant storage plugins
- CRI-compliant container runtimes
- service mesh options
- service discovery options
- monitoring and logging options
- etc.

Figure 1-1 below shows how Kubernetes, CaaS, and the CaaS Manager might fit within the current ETSI architecture.  In terms of this Reference Architecture, we should focus on the requirements of the new interfaces and the capabilities within the CaaS Manager and the Kubernetes clusters.

<p align="center"><img src="../figures/ch01_k8s_arch.png" alt="Kubernetes Architecture for NFV" title="Kubernetes Architecture for NFV" width="100%"/></p>
<p align="center"><b>Figure 1-1:</b> Kubernetes Architecture for NFV</p>

### A note on virtualised and containerised workloads
It is possible that a single VNFM will be managing applications (or components) that are virtualised (i.e. running in VMs) and applications (or components) that are containerised (i.e. running in containers), at the same time.  There are different approaches to achieving this:
1. Application manager (EMS, VNFM) uses both IaaS (VIM) API and Kubernetes API - the former for VM based workloads, the latter for containerised workloads.
2. Application manager (EMS, VNFM) uses just the Kubernetes API for both VM-based and container-based workloads, with the Kubernetes PaaS managing the lifecycle of VMs using on of the following methods:
    a) Kubernetes interacts with IaaS/VIM API (Cluster API model)
    b) Kubernetes is the IaaS/VIM and interacts direct with the hypervisor (Kubevirt model)

### A note on bare metal containerisation
As described above, Kubernetes is an application manager and therefore the lifecycle of Kubernetes clusters should closely match the lifecyle of the application or applications being deployed into Kubernetes. It therefore goes that the engineering teams defining the lifecycle of their applications will also define the lifecycle of the clusters they use for those applications. In an operator this might be a network engineering team, for example.

This has the following considerations when it comes to bare metal:
- With virtualised infrastructure, the underlying hypervisor hosts are or can be shared amongst a large number of tenants (i.e. application teams); much of the financial benefit of NFV was due to this concept
- If the above lifecycle is used then the following things need careful thought:
    - Size of bare metal nodes
    - Infrastructure management API, network overlay, etc.

Regarding the size of the nodes, this is about trying not to reduce the benefits we gained with NFV in the first place. For example, if three hypervisor hosts have 60CPUs and 1.5TB RAM between them, sharing those resources between a large number of applications (lets say 50) is made efficient by the use of virtualisation. For bare metal containerisation, that same number of applications would need a much larger number of bare metal hosts, with each host being a much smaller unit.

Regarding the network overlay, this is about having a service with capabilities that are provided by the VIM for virtualised environments, but for bare metal. So the ability to provision bare metal to a particular tenant, ensure the networking to each node is correctly provisioned (so, for bare metal this may mean calling out to an external SDN controller, as opposed to using an SDN controller provided by the VIM), and so on.
