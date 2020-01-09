[<< Back](../../openstack)

# 5. Interfaces & APIs
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 Introduction](#5.1)
* [5.2 Management APIs](#5.2)
* [5.3 Exposed interfaces](#5.3)
* [5.4 Internal interfaces](#5.4)

<a name="5.1"></a>
## 5.1 Introduction

> Summary of what is included in this chapter and how it will be used to drive RA-compliant Reference Implementations via Reference Certifications.

> Need to be clear [about "exposed" and "internal" interfaces](../../../ref_model/chapters/chapter04.md#4.1.1), in addition to the Kubernetes API and any other APIs used by Application Management capabilities (as opposed to exposed interfaces, which are those used by the workloads themselves).

> In summary, there are:
- APIs and interfaces used by VNF/CNF management capabilities (e.g. Kubernetes API)
- Exposed interfaces and objects used by VNF/CNF workloads
- Internal interfaces and objects used within the Kubernetes platform

<a name="5.2"></a>
## 5.2 Kubernetes API

> Kubernetes API - conformance to CNCF spec using Sonobuoy etc.
>
> https://github.com/cncf/k8s-conformance/blob/master/instructions.md

<a name="5.3"></a>
## 5.3 Exposed interfaces

> Compute, storage, networking, etc. that is used by the VNF/CNF workloads

<a name="5.4"></a>
## 5.4 Internal interfaces

> Compute, storage, networking, etc. that is used by the Kubernetes platform itself (i.e. by worker nodes)
