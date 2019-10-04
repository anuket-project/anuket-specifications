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

- **Scalable Applicatins**:
- **Declarative APIs**:
- **Platform**:


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

The definition above is very applicatin centric and look at cloud native from the application point of view, in here, we will try and relate those definitions to the platforms of which cloud native applicatiosn run on top of.

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

This document (at this stage, not a RA, we're just using the template as a placeholder), discusses the role of Kubernetes in managing NFV software components (e.g. VNFCs). Application containers such as those managed by Kubernetes can be considered a Foundational PaaS capability<sup>1</sup> and so the following terms can all be thought of as being the topic of this document:
- Kubernetes PaaS (Platform-as-a-Service)
- CaaS (Containers-as-a-Service)
- Kubernetes-based CaaS (Containers-as-a-Service)
- Kubernetes-as-a-Service

Kubernetes itself is a “system for automating deployment, scaling, and management of containerized applications” and therefore Kubernetes place within our architecture should be closely linked to the application lifecycle (this is especially important when considering bare-metal containerisation). However, it is very important to point out that Kubernetes Platforms also consist of other open source projects, or add-ons, such as:
- CNI-compliant network plugins
- CSI-compliant storage plugins
- CRI-compliant container runtimes
- service mesh options
- service discovery options
- monitoring and logging options
- etc.

Therefore, when considering software validation, and in NFV scenarios the compliance, verification and certification complexities, more thought is required around how flexible the "Platform" should be, with regards to these add-ons.  i.e. does a single blueprint for a "Kubernetes Platform for NFV" include specific versions of specific projects for each add-on, meaning that if you change from, e.g. Envoy to Fluentd, a new blueprint is created to certify against.

There are a number of different approaches that could be adopted:
1. Software vendor brings Kubernetes
    - This option places the operator purely as the infrastructure provider, and the software vendor uses the VIM, or IaaS APIs, to manage the lifecycle of the infrastructure required to create, update and delete Kubernetes clusters ***and*** the software being deployed into Kubernetes
2. Operator brings Kubernetes
    - This option places the operator as not only the infrastructure provider, but also a "platform-as-a-service" provider (for Kubernetes Platform). The operator may already be providing platform-as-a-service offerings such as database-as-a-service, or other underlying "enabler services" for the software such as DNS, NTP, mail relay, etc.
    - It is not necessarily the case that the vendor that the operator chooses for Kubernetes is the same vendor that provides the NFVI and/or VIM for that operator. That is a procurement decision for each operator.

The main pros and cons to these approaches can be seen in the table below. This is broadly similar to the discussion had in the early days of virtualisation about whether or not to share NFVI platforms.

| Option | Pros | Cons | Notes |
| --- | --- | --- | --- |
| 1. Software vendor brings Kubernetes | Potentially quicker validation/certification | Potential for silo deployments, operational complexity | ... |
| 2. Operator brings Kubernetes | Maximum efficiency of infrastructure | Good for those operators building capabilities | ... |

Suggested recommendation:
- Option 2, operator brings Kubernetes to meet model for other "as-a-Service" components that are required such as DNS, NTP, etc.

Figure 1-1 below shows this at a high level.

<p align="center"><img src="../figures/ch01_k8s_arch.png" alt="Kubernetes Architecture for NFV" title="Kubernetes Architecture for NFV" width="100%"/></p>
<p align="center"><b>Figure 1-1:</b> Kubernetes Architecture for NFV</p>

### More thoughts
- Kubernetes / CaaS should be recognised in ETSI NFV / MANO
- It is feasible that Kubernetes, using operators and custom resources, could become a generic VNFM (i.e. the Kubernetes parts are the underlying engine, with the operators and custom resources being the equivalent of the specific VNFM).
- Should each operator decide how Kubernetes is shared (if at all)?  Should we/someone suggest some best practice (such as, link Kubernetes cluster lifecycle to application lifecycle - so VNFv1.0 is in one cluster, VNFv2.0 is in another cluster. Are clusters shared between VNF vendors, or VNF types?).

### A note on virtualised and containerised workloads
It is highly likely that a single VNFM will be managing applications (or components) that are virtualised (i.e. running in VMs) and applications (or components) that are containerised (i.e. running in containers), at the same time.  There are different approaches to achieving this:
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


References
---
1: http://www.theenterprisearchitect.eu/blog/categorize-compare-cloud-vendors/
