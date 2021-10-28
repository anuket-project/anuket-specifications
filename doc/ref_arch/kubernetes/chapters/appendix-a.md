[<< Back](../../kubernetes)

# Appendix A - Guidance For workload isolation (Multitenancy) with Kubernetes for application vendors

<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents <!-- omit in toc -->

- [Appendix A - Guidance For workload isolation (Multitenancy) with Kubernetes for application vendors](#appendix-a---guidance-for-workload-isolation-multitenancy-with-kubernetes-for-application-vendors)
  - [A.1 Overview](#a1-overview)
  - [A.2 Multitenancy Models for CNFs](#a2-multitenancy-models-for-cnfs)
  - [A.3 Solution Areas](#a3-solution-areas)

## A.1 Overview

Problem statement: A single Kubernetes Cluster does not provide hard multitenancy* by design. Within a Cluster, Kubernetes Namespace is a mechanism to provide Soft isolation multitenancy**.
A Kubernetes Namespace does provide isolation by means of role based access control (RBAC), Resource Isolation and Network Policy, however they are still within the same trust domain and a potential breach of Cluster Admin Role could lead to the Blast Radius across the entire Cluster and all its Kubernetes Namespaces.
So there is a need to define various use cases or ways to build Multitenancy Deployment Models and define the Best Practices to secure each Model.
Kubernetes Namespace is a logical representation of namespace(boundary for resources) within the Kubernetes Cluster.
This is different from the [linux namespaces](https://en.wikipedia.org/wiki/Linux_namespaces) which are defined at the operating system kernel level.

<p align="left"><img src="../figures/Model2-cluster-isolation.png" alt="scope" title="Scope" width="50%"/></p>
<p align="left"><img src="../figures/Model1-ns.png" alt="scope" title="Scope" width="50%"/></p>

Use cases:

1. Two CNFs which are in the same trust domain (e.g.: they are from the same vendor) are running in a container infrastructure
2. Two CNFs which are in different trust domains (e.g.: they are from different vendors) are running in a container infrastructure

## A.2 Multitenancy Models for CNFs

Solution Models :

1. **Soft Multitenancy**: Separate Kubernetes Namespace per CNF within a Single Kubernetes Cluster. The same Kubernetes Cluster and its resources are being shared between multiple tenants.
2. **Hard Multitenancy**: Separate Kubernetes Cluster per CNF.
The Kubernetes Clusters can be created using Baremetal Nodes or Virtual Machines, either on Private or Public Cloud.
The workloads do not share the same resources and Clusters are isolated.

## A.3 Solution Areas

The scope is to identify the solution area which is needed to secure the CNF workloads. Securing the platform might happen as part of it but not directly the focus or objective here.

1. Isolation of Platform and Tenant Deployment based on the Solution Model
2. Separate CICD, Manifest and Image Repository for Platform and Tenants
3. Isolation of Networking for CNF Workloads
4. Securing the CNF Workload Network Traffic using Network Policy and Service Mesh
5. Separate Storage Backend for each CNF Workloads
6. RBAC and secrets Management for CNF Workload
7. Separate Isolated view of Logging, Monitoring, Alerting and Tracing for CNF Workloads
