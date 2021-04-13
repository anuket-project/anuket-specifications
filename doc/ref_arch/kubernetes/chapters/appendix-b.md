[<< Back](../../kubernetes)
# Appendix B - Guidance For workload isolation (Multitenancy) with Kubernetes for application vendors
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [B.1 Overview](#B.1)
* [B.2 Multitenancy Models for CNFs](#B.2)
* [B.3 Solution Areas](#B.3)


<a name="B.1"></a>
## B.1 Overview

Problem statement: A single Kubernetes Cluster does not provide hard multitenancy* by design. Within a Cluster, Kubernetes Namespace is a mechanism to provide Soft isolation multitenancy**.
A Kubernetes Namespace does provide isolation by means of role based access control (RBAC), Resource Isolation and Network Policy, however they are still within the same trust domain and a potential breach of Cluster Admin Role could lead to the Blast Radius across the entire Cluster and all its Kubernetes Namespaces.
So there is a need to define various use cases or ways to build Multitenancy Deployment Models and define the Best Practices to secure each Model.
Kubernetes Namespace is a logical representation of namespace (boundary for resources) within the Kubernetes Cluster.
This is different from the Linux namespaces which is defined at the operating system kernel level (Refer: https://en.wikipedia.org/wiki/Linux_namespaces).
<p align="left"><img src="../figures/Model2-cluster-isolation.png" alt="scope" title="Scope" width="50%"/></p>
<p align="left"><img src="../figures/Model1-ns.png" alt="scope" title="Scope" width="50%"/></p>
Use cases:
1 Two CNF-s which are in the same trust domain (e.g.: they are from the same vendor) are running in a container infrastructure
2 Two CNF-s which are in different trust domains (e.g.: they are from different vendors) are running in a container infrastructure


<a name="B.2"></a>
## B.2 Multitenancy Models for CNFs
Solution Models :
1. Seperate Kubernetes Namespace per vendor within Single Kubernetes Cluster
2. Seperate Kubernetes Cluster per vendor.
The Kubernetes Clusters can be created using Baremetal Nodes or Virtual Machines (either on the Baremetal Machines or also the way Public CLoud Provider APIs are used to create the Virtual Machines like in GCP Compute Engine, Azure or AWS Providers.

<a name="B.3"></a>
## B.3 Solution Areas
The scope is to identify the solution area which is needed to secure the CNF workloads. Securing the platform might happen as part of it but not directly the focus or objective here.
1. Isolation of Platform and Tenant Deployment based on the Solution Model
2. Seperate CICD, Manifest and Image Repository for Platform and Tenants
3. Isolation of Networking for CNF Workloads
4. Securing the CNF Workload Network Traffic using Network Policy and Service Mesh
5. Seperate Storage Backend for each CNF Workloads
6. RBAC and secrets Management for CNF Workload
7. Separate Isolated view of Logging, Monitoring, Alerting and Tracing for CNF Workloads

"*" hard multitenancy: can be defined as workload isolation mechanism in which the workloads do not share the same Cluster resources and are isolated at Cluster level. So typically a seperate Cluster for each tenant could be considered as hard isolation.

"**" soft multitenancy is a mechanism in which the same Kubernetes Cluster is being shared between different tenants, like using Namespaces to isolate the tenants.
