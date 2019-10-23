
[<< Back](../../kubernetes)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction.](#2.1)
* [2.2 Reference Model Requirements.](#2.2)
* [2.3 Kubernetes Requirements.](#2.3)

<a name="2.1"></a>
## 2.1 Introduction.

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference architecture and reflected in any implementation targeting this reference architecture. The same applies to _must not_.

**should**: Requirements that are marked as _should_ are expected to be fulfilled by the reference architecture but it is up to each service provider to accept an implementation targeting this reference architecture that is not reflecting on any of those requirements. The same applies to _should not_.
> RFC2119

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

<a name="2.2"></a>
## 2.2 Reference Model Requirements.

Traceability to Reference Model.

<a name="2.3"></a>
## 2.3 Requirements.

<a name="2.3.1"></a>
### 2.3.1 General

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.gen.k8s.01` | Open source | The Architecture **must** use Kubernetes APIs.|
| `req.gen.k8s.02` | Open source | The Architecture **must** support dynamic request and configuration of resources (compute, network, storage) through Kubernetes APIs. |
| `req.gen.cnt.01` | Cloud nativeness | The Architecture **should** consist of stateless service components. However, where state is required it must be kept external to the component. |
| `req.gen.cnt.02` | Cloud nativeness | The Architecture **should** consist of service components implemented as microservices that are individually dynamically scalable. |
| `req.gen.scl.01` | Scalability | The Architecture **should** support policy driven horizontal auto-scaling. |
| `req.gen.rsl.01` | Resiliency | The Architecture **must** support resilient Kubernetes components that are required for the continued availability of running workloads. |
| `req.gen.rsl.02` | Resiliency | The Architecture **should** support resilient Kubernetes service components that are not subject to `req.gen.rsl.01`. |
| `req.gen.avl.01` | Availability | The Architecture **must** provide High Availability for Kubernetes components. |


<p align="center"><b>Table 2-1:</b> Kubernetes General Requirements.</p>
