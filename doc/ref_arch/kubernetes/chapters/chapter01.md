[<< Back](../../kubernetes)

# 1. Overview
<p align="right"><img src="../figures/bogo_dfp.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Introduction.](#1.1)
* [1.2 Terminology](#1.2)
* [1.3 Principles](#1.3)
  * [1.3.1 Cloud Native.](#1.3.1)
* [1.4 Scope](#1.4)
* [1.5 Approach](#1.5)


<a name="1.1"></a>
## 1.1 Introduction

The intention of this Reference Architecture is to develop a usable Kubernetes based platform for the Telecom operator community. The RA will be based on the standard Kubernetes platform where ever possible. This Reference Architecture for Kubernetes will describe the high level system components and their interactions, taking the goals and requirements of the [Reference Model](../../../ref_model/chapters/chapter01.md) and mapping them to real-world Kubernetes (and related) components. This document needs to be sufficiently detailed and robust such that it can be used to guide the production deployment of Kubernetes within an operator, whilst being flexible enough to evolve with and remain aligned with the wider Kubernetes ecosystem outside of Telco.

To set this in context, it makes sense to start with the high level definition and understanding of Kubernetes itself as it stands. [Kubernetes](https://kubernetes.io/) is a "portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available" [[kubernetes.io](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)]. Kubernetes is developed as an open source project in the [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) repository of GitHub.

To assist with the goal of creating a reference architecture that will support Telco workloads, but at the same time leverage the work that already has been completed in the Kubernetes community, RA2 will take an "RA2 [Razor](https://en.wikipedia.org/wiki/Philosophical_razor)" approach to build the foundation. This can be explained along the lines of "if something is useful for non-Telco workloads, we will not include it only for Telco workloads". For example, start the Reference Architecture from a vanilla Kubernetes (say, v1.16) feature set, then provide clear evidence that a functional requirement cannot be met by that system (say, multi-NIC support), only then the RA would add the least invasive, Kubernetes-community aligned extension (say, Multus) to fill the gap. If there are still gaps that cannot be filled by standard Kubernetes community technologies or extensions then the RA will concisely document the requirement and approach the relevant project maintainers with a request to add this functionality into the feature set.

The Kubernetes Reference Architecture will be used to determine a Kubernetes Reference Implementation. The Kubernetes Reference Implementation would then also be used to test and validate the supportability and compatibility with Kubernetes-based Network Function workloads of interest to the CNTT community. It is expected the Kubernetes Reference Architecture, Reference Implementation, and Reference Conformance will be developed in parallel to OVP Phase 2, which is building on the work already in place for OpenStack implementations. The intention is to expand as much of the existing test frameworks to be used for the verification and conformance testing of Kubernetes-based workloads.

<a name="1.2"></a>
### 1.2 Terminology

For terminology used in this document refer to the [glossary](../../../common/glossary.md)

<a name="1.3"></a>
## 1.3 Principles

This Reference Architecture conforms with the principles defined in [here](../../../common/chapter00.md#2.0).

<a name="1.3.1"></a>
### 1.3.1 Cloud Native Principles

The definition for Cloud Native is somewhat controversial.  For the purposes of this document, the CNCF TOC's (Technical Oversight Committee) definition of Cloud Native will be used:
>CNCF Cloud Native Definition v1.0
>Approved by TOC: 2018-06-11

>“Cloud native technologies empower organizations to build and run **scalable** applications in modern, **dynamic environments** such as public, private, and hybrid clouds. Containers, **service meshes**, **microservices**, **immutable infrastructure**, and **declarative APIs** exemplify this approach.

>These techniques enable **loosely coupled** systems that are **resilient**, **manageable**, and **observable**. Combined with **robust automation**, they allow engineers to make **high-impact changes frequently and predictably** with minimal toil.

>The Cloud Native Computing Foundation seeks to drive adoption of this paradigm by fostering and sustaining an ecosystem of open source, vendor-neutral projects. We democratize state-of-the-art patterns to make these innovations accessible for everyone”

Individual contributors who are also active in the CNCF TUG (Telecom User Group), formed in June 2019, are also working on a set of Cloud Native Principles that are more suited to the requirements of the Telecom cummunity and with more detail than the existing CNCF definition: [Expanded Cloud Native Principles](https://networking.cloud-native-principles.org/cloud-native-principles). There are many similarities, but the key principles from both, which are applicable to this document, are:

- **scalable**
- **dynamic environments**
- **service meshes**
- **microservices**
- **immutable infrastructure**
- **declarative APIs**
- **loosely coupled**
- **resilient**
- **manageable**
- **observable**
- **robust automation**
- **high-impact changes frequently and predictably**

<a name="1.4"></a>
## 1.4 Scope

The scope of this particular Reference Architecture can be described as follows (the capabilities themselves will be listed and described in subsequent chapters), also shown in Figure 1-1:
- Kubernetes capabilities required to conform to the Reference Model requirements
- Support for CNFs that consist wholly of containers
- Support for CNFs that consist partly of containers and partly of VMs, both of which will be orchestrated by Kubernetes

The following items are considered **out of scope**:
- **Kubernetes cluster lifecycle management**: Since it is not considered to be "visible" to a CNF, it should not be included.
- **Kubernetes-based Application / VNF Management**: similar to VNFM, this is an application layer capability that is out of scope of CNTT. This includes Kubernetes-based Application Package Management, such as Helm, as this is a client application and set of libraries that would be part of a modern/cloud native VNFM, not part of the infrastructure itself.

<p align="center"><img src="../figures/ch01_scope_k8s.png" alt="Kubernetes Reference Architecture scope" title="Kubernetes Reference Architecture scope" width="100%"/></p>
<p align="center"><b>Figure 1-1:</b> Kubernetes Reference Architecture scope</p>

<a name="1.5"></a>
## 1.5 Approach

The approach taken in this Reference Architecture is to start as simply as possible (i.e. with a basic Kubernetes architecture), and then add detail and additional features/extensions as is required to meet the requirements of the Reference Model and the functional and non-functional requirements of common cloud native network functions.

For example, while the management of VMs through Kubernetes is included, the intention is to start with the "native" control of containers and add support for VMs at a later date.  The final decision will be determined and documented in the Roadmap section.

This document will start with a description of interfaces and capabilities (the "what") before at a later date providing guidance on "how" those elements are deployed.  The details of how the elements will be used together will be documented in full detail in the Reference Implementation. In addition, an [Appendix](./appendix-a.md) is included with the purpose of describing the transition from VNF to CNF and the potential pitfalls and complexities that may need consideration. This appendix may in turn lead to the identification of gaps that need attention in one or more Reference Architectures.
