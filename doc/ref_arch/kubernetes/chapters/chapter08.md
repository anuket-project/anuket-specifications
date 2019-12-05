[<< Back](../../kubernetes)

# 8. Gaps, Innovation, and Development
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction](#8.1)
* [8.2 Gap analysis](#8.2)
* [8.3 Proposals & Resolution](#8.3)
* [8.4 Development Efforts](#8.3)

<a name="8.1"></a>
## 8.1 Introduction
While this Reference Architecture is being developed, Gaps will be identified that require addressing. This chapter will highlight these gaps in detail and may provide proposed solutions. As a result, various “upstream” community projects will be identified and will be targeted for development efforts.

<a name="8.2"></a>
## 8.2 Gap analysis

- Container Run-Time Interfaces towards NFVI resources.
- Multi-Tenancy
- K8s as VM based VNF Orchestrator

<a name="8.2.1"></a>
### 8.2.1 Container run-time Interfaces towards NFVI resources

> This is the southbound infrastructure resources from the container platform as presented by the IaaS provider.

> e.g. network interface type that is presented to a running container.


<a name="8.2.2"></a>
### 8.2.2 Multi-tenancy within Kubernetes

> Today, Kubernetes lacks hard multi-tenancy capabilities<sup>citations</sup>

> Ability to allow untrusted tenants to share infrastructure resources.


<a name="8.2.3"></a>
### 8.2.3 Kubernetes as a VM-based VNF Orchestrator

> In order to support a transition from VNFs only to VNFs and CNFs in the same environment.


<a name="8.2.4"></a>
### 8.2.4 Multiple network interfaces on Pods

> As well as having multiple network interfaces on Pods (e.g. Multus), being able to have different network interfaces in differnet Pods using different CNI plugins within the same cluster.


<a name="8.2.5"></a>
### 8.2.5 Dynamic network management

> this is done today with Netconf etc. integration with SDN controllers, for example

> connecting individual VPNs - e.g. L3VPN - onto the CNF, on demand

> look to enable this via a standard API


<a name="8.2.6"></a>
### 8.2.6 Control Plane Efficiency

> For example, in situations where multiple sites / availability zones exist, an operator may choose to run multiple Kubernetes clusters, not only for security/multitenancy reasons but also fault, resilience, latency, etc.

> This produces an overhead of Kubernetes Masters - is there a way of making this more efficient whilst still able to meet the non-functional requirements of the operator (fault, resilience, latency, etc.)


<a name="8.3"></a>
## 8.3 Proposals & Resolution

<a name="8.4"></a>
## 8.4 Development Efforts
