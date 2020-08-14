[<< Back](../../kubernetes)
# Appendix B - Guidance For workload isolation(Multitenancy) with Kubernetes for application Vendors
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [B.1 Overview](#B.1)
* [B.2 Best Practices For workload isolation(Multitenancy](#B.2)
* [B.3 TBC](#B.3)


<a name="B.1"></a>
## B.1 Overview

Problem statement: A single Kubernetes cluster does not provide hard multitenancy by design. Within a Cluster, Namespace is a mechanism to provide Soft isolation multitenancy.
Namespace does provide isolation by means of RBAC, Resource Isolation and Network Policy, however they are still within the same trust domain and a potential breach of Cluster Admin Role could lead to the Blast Radius across the entire Cluster and all its namespaces.
So there is a need to define various use cases or ways to build Multitenancy Deployment Models and define the Best Practices to secure each Model.

<p align="middle"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="100%"/></p>

Use cases:
1 Two CNF-s which are in the same trust domain (e.g.: they are from the same vendor) are running in a container infrastructure
2 Two CNF-s which are in different trust domains (e.g.: they are from different vendors) are running in a container infrastructure


<a name="B.2"></a>
## B.2 Multitenancy Models for CNFs
Solution Models :
1. Seperate Namespace per Vendor within Single Kubernetes Cluster
2. Seperate Kubernetes Cluster per Vendor

<a name="B.3"></a>
## B.3 Solution Areas
The scope is to identify the solution area which is needed to secure the CNF workloads. Securing the platform might happen as part of it but not directly the focus or objective here.
1. Isolation of Platform and Tenant Deployment based on the Solution Model
2. Seperate CICD, Manifest and Image Repository for Platform and Tenants
3. Isolation of Networking for CNF Workloads
4. Securing the CNF Workload Network Traffic using Network Policy and Service Mesh
5. Seperate Storage Backend for each CNF Workloads
6. RBAC and secrets Management for CNF Workload
7. Seperate Isolated view of Logging,Monitoring,Alerting and Tracing for CNF Workloads


