Appendix A - Guidance For workload isolation (Multitenancy) with Kubernetes for application vendors
===================================================================================================

Overview of Appendix A
----------------------

Problem statement: A single Kubernetes Cluster does not provide hard multitenancy\* by design. Within a Cluster,
the Kubernetes Namespace is a mechanism to provide Soft isolation multitenancy.
A Kubernetes Namespace does provide isolation by means of role-based access control (RBAC), Resource Isolation, and
Network Policy. However, they are still within the same trust domain and a potential breach of the Cluster Admin Role
could have serious ramifications across the entire Cluster and all its Kubernetes Namespaces.
Therefore, it is necessary to define various use cases or ways to build Multitenancy Deployment Models and define the
Best Practices to secure each Model. The Kubernetes Namespace is a logical representation of namespace (boundary for
resources) within the Kubernetes Cluster. This is different from the :cite:t:`wikipedia-linux-namespaces_ra2`, which are
defined at the operating system kernel level.

.. figure:: ../figures/Model1-ns.png
   :alt: Network service

   Network service

.. figure:: ../figures/Model2-cluster-isolation.png
   :alt: Cluster isolation

   Cluster isolation

Use cases:

1. Two CNFs which are in the same trust domain (for example, they are from the same vendor) are running in a container
   infrastructure.
2. Two CNFs which are in different trust domains (for example, they are from different vendors) are running in
   a container infrastructure.

Solution areas
--------------

The scope is to identify the solution area which is needed to secure the CNF workloads. Securing the platform might
happen as part of it. However, it is not directly the focus or objective here.

1. Isolation of platform and tenant deployment based on the solution model.
2. Separate CICD, manifest, and image repository for platform and tenants.
3. Isolation of networking per tenant.
4. Securing the CNF workload network traffic using a network policy and service mesh.
5. RBAC rules and secrets management for each tenant.
6. Separate isolated view of logging, monitoring, alerting, and tracing per tenant.

Multitenancy Models
-------------------

Solution models :

1. **Soft Multitenancy**: Separate Kubernetes Namespace per tenant within a single Kubernetes cluster. The same
   Kubernetes Cluster and its control plane are shared between multiple tenants.
2. **Hard Multitenancy**: Separate Kubernetes cluster per tenant. The Kubernetes clusters can be created using
   baremetal nodes or virtual machines, either in the private cloud or the public cloud. The workloads do not
   share the same resources, and the clusters are isolated.

Soft multitenancy with Kubernetes Namespaces per tenant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Soft multitenancy with namespaces per tenant can be implemented, resulting in a multitenant cluster, in which multiple
trusted workloads share a cluster and its control plane. This is mainly recommended to reduce management overheads when
the tenants belong to the same trust domain, and have the same cluster configuration requirements (including release,
add-ons, and so on).

The tenants share the cluster control plane and API, including all add-ons, extensions, CNIs, CSIs, and any custom
resources and controllers.

To manage access control, the Kubernetes RBAC must be configured with rules to allow specific tenants to access only
the objects within their own namespace, using a ``Role`` Object to group the resources within a namespace, and a
``RoleBinding`` Object to assign it to a user or a group of users within a namespace.

To prevent or allow network traffic between Pods to belong to different namespaces, ``NetworkPolicy`` must
also be created.

Resource quotas enable the cluster administrator to allocate CPU and memory to each namespace, limiting the amount of
resources the objects belonging to that namespace can consume. This may be configured, in order to ensure that all
tenants use no more than the resources that are assigned to them.

By default, the Kubernetes scheduler runs pods belonging to any namespace on any cluster node. If it is required
that pods from different tenants are run on different hosts, then affinity rules should be created by using the
desired Node Labels on the pod definition. Alternatively, node taints can be used to reserve certain nodes for a
predefined tenant.

Hard multitenancy with dedicated Kubernetes clusters per tenant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When tenants do not belong to the same trust domain, or the requirements on the cluster setup and configuration are
irreconcilable, hard multitenancy must be implemented by creating multiple Kubernetes clusters for each tenant or
group of compatible tenants.

All the default design decisions for Kubernetes clusters apply in this case. No special segregation or capacity
management needs to be set up within the clusters.

From an operational perspective, the increased computational and operational overheads and the Cluster LCM (including
cluster provisioning automation) are the most impactful aspects.

