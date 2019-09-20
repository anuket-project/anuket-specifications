[<< Back](../../kubernetes)

# 1. Overview
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Introduction.](#1.1)
* [1.2 Terminology.](#1.2)
* [1.3 Approach](#1.3)
* [1.4 Principles](#1.4)
* [1.5 scope](#1.4)
* [1.6 Vision](#1.4)
* [1.7 Roadmap](#1.4)

<a name="1.1"></a>
## 1.1 Introduction

Kubernetes itself is a “system for automating deployment, scaling, and management of containerized applications”.  Kubernetes place within our architecture should therefore be closely linked to the application lifecycle.

However, it is very important to point out that Kubernetes Platforms are not just Kubernetes, they also consist of a whole load of other open source projects, or add-ons, such as:
- CNI-compliant network plugins
- CSI-compliant storage plugins
- CRI-compliant container runtimes
- service mesh options
- service discovery options
- monitoring and logging options
- etc.

Therefore, when considering software validation, and in NFV scenarios the compliance, verification and certification complexities, more thought is required around how flexible the "Platform" is, with regards to these add-ons.  i.e. does a single blueprint for a "Kubernetes Platform for NFV" include specific versions of specific projects for each add-on, and if you change from, e.g. Envoy to Fluentd, that is a new blueprint to certify against.

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

Other thoughts:
- Kubernetes / CaaS should be recognised in ETSI NFV / MANO
- I think it is feasible that Kubernetes, using operators and custom resources, could become a generic VNFM (i.e. the Kubernetes parts are the underlying engine, with the operators and custom resources being the equivalent of the specific VNFM).
- Should each operator decide how Kubernetes is shared (if at all)?  Should we/someone suggest some best practice (such as, link Kubernetes cluster lifecycle to application lifecycle - so VNFv1.0 is in one cluster, VNFv2.0 is in another cluster. Are clusters shared between VNF vendors, or VNF types?). 

<a name="1.2"></a>
## 1.2 Terminology

<a name="1.3"></a>
## 1.3 Approach


<a name="1.4"></a>
## 1.4 Principles

Kubernetes Reference Architecture must obey to the following set of principles:
- [CNTT Reference Model Principles](../../../ref_model/chapters/chapter01.md#1.3)
- [CNTT Reference Architecture Principles](../../#principles)

>Any Kubernetes specific principles needs to be added here.


<a name="1.5"></a>
## 1.5 Scope


<a name="1.6"></a>
## 1.6 Vision

<a name="1.7"></a>
## 1.7 Roadmap
