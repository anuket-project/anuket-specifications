Gaps, Innovation, and Development
=================================

Introduction
------------

While this Reference Architecture is being developed, Gaps will be identified that require addressing. This chapter
will highlight these gaps in detail and may provide proposed solutions. As a result, various “upstream” community
projects will be identified and will be targeted for development efforts.

Gap analysis
------------

-  Container Run-Time Interfaces towards NFVI resources.
-  Multi-Tenancy
-  K8s as VM based VNF Orchestrator

Gap template
~~~~~~~~~~~~

   **Related requirements:** List the requirement references ``abc.xyz.00`` from RA2 or RM which this gap tries to
   address.

..

   **Baseline project:** Describe against which upstream project the gap exists e.g. *Kubernetes*. If the gap is not
   against any specific upstream project, state "none".

   **Gap description:** Describe which functionality described in the related requirements is currently missing in the
   implementations you're aware of. Include references to work ongoing in the target project, which may adress the gap.

Container run-time Interfaces towards NFVI resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   This is the southbound infrastructure resources from the container platform as presented by the IaaS provider.

..

   e.g., network interface type that is presented to a running container.

Multi-tenancy and workload isolation with Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:** ``e.man.004``, ``sec.ci.008``, :literal:`sec.wl.005`, `sec.wl.006`

**Baseline project:** *Kubernetes*

**Gap description:** Today, Kubernetes lacks hard multi-tenancy capabilities that give the ability to allow untrusted
tenants to share infrastructure resources. This presents a security problem when operators seek to separate workloads
by categorization or even just production vs non-production. Further, tenant networks need to be both segregated, but
still centrally administered and maintained. Beyond just security, this also presents an operational problem. Trying to
deploy too many CNFs into the same cluster could result in version conflicts, configuration conflicts, and problems with
software life cycle management. Finally, without proper isolation there is an increased risk of cascading failures.

**Proposals & Resolution:** Kubernetes is not a single cluster solution. This has been demonstrated across the
industry from case studies at prominent companies like
`Twitter <https://www.alibabacloud.com/blog/what-can-we-learn-from-twitters-move-to-kubernetes_595156>`__,
`USA Today <https://medium.com/usa-today-network/there-and-back-again-scaling-multi-tenant-kubernetes-cluster-s-
67afb437716c>`__,
`Zalando <https://www.youtube.com/watch?v=LpFApeaGv7A>`__, and
`Alibaba <https://www.cncf.io/blog/2019/12/12/demystifying-kubernetes-as-a-service-how-does-alibaba-cloud-manage-10000s
-of-kubernetes-clusters/>`__ to the bi-annual CNCF survey that finds that the number of clusters being deployed within
an organization is growing. While there are many reasons behind the multi cluster paradigm, examining the gap above we
find that a multi cluster solution can address many of these problems like security and software life cycle management.

Without multi tenancy within a cluster, separate clusters must be used to provide adequate separation for CNFs that
require strong isolation. CNFs may need to be separated for various reasons including different types of
workloads based on their vendors, rnvironments like production vs. non production, per categorization, or supporting
independent lifecycles. Having multiple clusters to deploy CNFs into allows operators to chose similar CNFs together
while segregating those with different lifecycles from each other. CNFs deployed into the same cluster can be upgraded
together to reduce the operational load while CNFs that require different versions, configurations, and dependencies
can run in separate clusters and be upgraded independently if needed.

If running multiple clusters is the only solution to meeting these workload and infrastructure requirements, the
operational burden of this model must also be considered. Running a multitude of clusters at scale could be a massive
operational challenge if done manually. Any operator considering running Kubernetes at scale should carefully evaluate
their multi cluster management strategy including the management of the applications within those clusters.

Kubernetes as a VM-based VNF Orchestrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** None.

..

   **Baseline project:** *Kubernetes*, *Kubevirt*

   **Gap description:** Kubernetes and at least one CRI compliant runtime should support the running of VNFs without
   requiring changes to the VNF's architecture and deployment artifacts.

Multiple network interfaces on Pods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** :ref:`ref_model:chapters/chapter04:virtual network interface specifications`

..

   **Baseline project:** *Kubernetes*

   **Gap description:** Kubernetes does not have native support for multiple Pod interfaces, therefore a CNI
   multiplexer, like `Multus <https://github.com/intel/multus-cni>`__ is needed to provision multiple interfaces.
   Implementation of different network services for the interfaces, like Network Policies, Ingress, Egress or Load
   Balancers depends on the feature set of the CNI multiplexer and the CNI plugins it uses, therefore it is
   inconsistent.

   **Status:** There is a `draft Kubernetes Enhancement Proposal (KEP)
   <https://docs.google.com/document/d/1ztx9TOQ9Hiyj9PG9aPv6jyDLhe_FB7haV_yjJIcb-0Y/>`__
   created to support multiple Pod interfaces natively.

Dynamic network management
~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** :ref:`inf.ntw.03 <chapters/chapter02:kubernetes architecture requirements>`

..

   **Baseline project:** *Kubernetes*

   **Gap description:** Kubernetes does not have an API for network management, therefore a different CNI plugin, like
   `DANM <https://github.com/nokia/danm>`__ needs to be used to expose Kubernetes network services on an API.
   Alternatively this is done today with Netconf etc., integration with SDN controllers, for example connecting
   individual VPNs - e.g., L3VPN - onto the CNF, on demand.

Control Plane Efficiency
~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** None

..

   **Baseline project:** *Kubernetes*

   **Gap description:** For example, in situations where multiple sites / availability zones exist, an operator may
   choose to run multiple Kubernetes clusters, not only for security/multitenancy reasons but also fault, resilience,
   latency, etc.
   This produces an overhead of Kubernetes Masters - is there a way of making this more efficient whilst still able to
   meet the non-functional requirements of the operator (fault, resilience, latency, etc.)

Interoperability with VNF-based networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** None

..

   **Baseline project:** *Kubernetes*

   **Gap description:** For example, today in existing networks L3 VPNs are commonly used for traffic separation (e.g.,
   separate L3 VPN for signalling, charging, LI, O&M etc.). CNFs will have to interwork with existing network elements
   and therefore a K8s POD will somehow need to be connected to a L3 VPN. Today this is only possible via Multus
   (or DANM), however typically there is a network orchestration responsibility to connect the network interface to a
   gateway router (where the L3 VPN is terminated). This network orchestration is not taken care of by K8s, nor there
   is a production grade solution in the open source space to take care of this.

Note: with an underlying IaaS this is possible, but then it introduces (undesirable) dependency between workload
orchestration in K8s and infrastructure orchestration in IaaS.

HW topology aware huge pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:** ``infra.com.cfg.004`` and ``infra.com.cfg.002``

**Baseline project:** *Kubernetes*

**Gap description:** Memory Manager was added in v1.21 as alpha feature. More in
:ref:`chapters/chapter03:memory and huge pages resources management`.

User namespaces in Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:**

.. list-table:: API Machinery Special Interest Group
   :widths: 20 60
   :header-rows: 1

   * - Reference
     - Requirement
   * - e.man.004
     - Capability to isolate resources between tenants
   * - sec.sys.007
     - The Platform must implement controls enforcing separation of duties and privileges, least privilege
       use and least common mechanism (Role-Based Access Control).

**Baseline project:** *Kubernetes*

**Gap description:** Kubernetes does not support namespace scoped user IDs (UIDs). Therefore, when a container-based
application requires system privileges the container either needs to run in privileged mode or the infrastructure needs
to provide random system UIDs. Randomised UIDs result in errors when the application needs to set kernel capabilities
(e.g., in case of VLAN trunking) or when a Pod shares data with other Pods via persistent storage. The
"privileged mode" solution is not secure while "random UID" solution is error prone, and therefore these techniques
should not be used. Support for proper user namespaces in Kubernetes is
`under discussion <https://github.com/kubernetes/enhancements/pull/2101>`__.
