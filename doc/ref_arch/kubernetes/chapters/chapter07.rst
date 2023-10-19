Gaps, Innovation, and Development
=================================

Introduction to Gaps, Innovation, and Development
-------------------------------------------------

There are functional gaps between the current state of technology available in open source and the requirements of this
Reference Architecture or the Reference Model. This chapter highlights these gaps in detail and provides proposed
solutions. As a result, various “upstream” community projects may be identified and will be targeted for development
efforts.

Gap template
~~~~~~~~~~~~

   **Related requirements:** List the requirement references ``abc.xyz.00`` from RA2 or RM which this gap tries to
   address.

..

   **Baseline project:** Describe against which upstream project the gap exists, for example, *Kubernetes*. If the gap is not
   against any specific upstream project, state "none".

   **Gap description:** Describe which functionality described in the related requirements is currently missing in the
   implementations that you are aware of. Include references to work ongoing in the target project, which may address the gap.

.. Container run-time Interfaces towards NFVI resources
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..
..   (unclear) This is the southbound interface from the container to the infrastructure resources provided by the IaaS provider.
..
..
..
   e.g., network interface type that is presented to a running container.

Multitenancy and workload isolation with Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:** ``e.man.004``, ``sec.ci.008``, ``sec.wl.005``, ``sec.wl.006``

**Baseline project:** *Kubernetes*

**Gap description:** Today, Kubernetes lacks hard multitenancy capabilities that allow untrusted tenants to share
infrastructure resources. This presents a security problem when operators seek to separate workloads by categorization
or simply production versus non-production. Furthermore, tenant networks need to be segregated, yet still centrally
administered and maintained. Beyond just security, this also presents an operational problem. Trying to deploy too
many CNFs in the same cluster could result in version conflicts, configuration conflicts, and problems with software
lifecycle management. Finally, without proper isolation, there is an increased risk of cascading failures.

**Proposals & Resolution:** Kubernetes is not a single-cluster solution. This has been demonstrated across the
industry from case studies at prominent companies such as :cite:t:`alibaba-blog-twitter_ra2`, :cite:t:`youtube-zalando_ra2`, and
:cite:t:`cncf-blog-alibaba_ra2` to the biannual CNCF survey that finds that the number of clusters being deployed within
an organization is growing. While there are many reasons behind the multicluster paradigm, examining the gap above we
find that a multicluster solution can address many of these problems such as security and software lifecycle management.

Without multitenancy within a cluster, separate clusters must be used to provide adequate separation for CNFs that
require strong isolation. CNFs may need to be separated for various reasons, including different types of workloads based
on their vendors, environments such as production versus non-production, per-categorization, or supporting independent
lifecycles. Having multiple clusters in which to deploy CNFs allows operators to choose similar CNFs together while
segregating those with different lifecycles from each other. CNFs deployed in the same cluster can be upgraded
together to reduce the operational load, while CNFs that require different versions, configurations, and dependencies
can run in separate clusters and be upgraded independently, if necessary.

If running multiple clusters is the only solution to meeting these workload and infrastructure requirements, the
operational burden of this model must also be considered. Running a multitude of clusters at scale could be a massive
operational challenge, if done manually. Any operator considering running Kubernetes at scale should carefully evaluate
their multicluster management strategy, including the management of the applications within those clusters.

Kubernetes as a VM-based VNF orchestrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** None.

   **Baseline project:** *Kubernetes*, *Kubevirt*

   **Gap description:** Kubernetes and at least one CRI-compliant runtime should support the running of VNFs without
   requiring changes to the VNF's architecture and deployment artifacts.

Native multiple network interfaces on Pods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** Virtual Network Interface Specifications section in Chapter 4 of :cite:t:`refmodel_ra2`

   **Baseline project:** *Kubernetes*

   **Gap description:** Kubernetes does not have native support for multiple Pod interfaces. Therefore, a CNI
   multiplexer, such as :cite:t:`github-multus_ra2`, is needed to provision multiple interfaces. Implementation of different
   network services for the interfaces, such as Network Policies, Ingress, Egress, or Load Balancers, depends on the feature
   set of the CNI multiplexer and the CNI plugins it uses. It is therefore inconsistent.

   **Status:** There is a :cite:t:`googledocs-kep-multi-network-pod-object_ra2` created to support multiple Pod interfaces
   natively.

Dynamic network management
~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** inf.ntw.03 in :ref:`ref_arch/kubernetes/chapters/chapter02:kubernetes architecture requirements`

   **Baseline project:** *Kubernetes*

   **Gap description:** Kubernetes does not have an API for network service management (for example, VPNs). Therefore,
   a CNI plugin, such as :cite:t:`github-multus_ra2`, needs to be used to expose APIs for Network services. Alternatively,
   this is done nowadays with Netconf and so on, and integration with SDN controllers, for example, connecting
   individual VPNs, such as L3VPN, to the CNF, on demand.

Control plane efficiency
~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** None

   **Baseline project:** *Kubernetes*

   **Gap description:** In situations where multiple sites/availability zones exist, an operator may
   choose to run multiple Kubernetes clusters, not only for security/multitenancy reasons but also for fault, resilience,
   latency purposes, and so on. This produces an overhead of Kubernetes Control plane nodes. There should be a way to
   operate multiple clusters more efficiently while still being able to meet the non-functional requirements of the operator,
   such as fault, resilience, latency, and so on.

Interoperability with VRF-based networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** None

   **Baseline project:** *Kubernetes*

   **Gap description:** In existing networks, L3 VRFs/VPNs are commonly used for traffic separation (for example, for
   separating L3 VPN for signalling, charging, LI, O&M, and so on). CNFs have to interwork with existing network elements.
   Therefore, a Kubernetes POD will somehow need to be connected to a L3 VPN. Currently, this is only possible via Multus.
   However, typically there is a network orchestration responsibility to connect the network interface to a gateway
   router, where the L3 VPN is terminated. This network orchestration is not taken care of by K8s, nor is there a
   production-grade solution in the open-source space to take care of this.

   .. note::
      With an underlying IaaS, this is possible. However, it introduces a dependency between workload orchestration in K8s
      and infrastructure orchestration in IaaS, which is not desirable.

Hardware topology-aware huge pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:** ``infra.com.cfg.004`` and ``infra.com.cfg.002`` in the Virtual Compute Profiles section in
Chapter 5 of :cite:t:`refmodel_ra2`.

**Baseline project:** *Kubernetes*

**Gap description:** The Memory Manager was added in v1.21 as alpha feature. For details, see
:ref:`ref_arch/kubernetes/chapters/chapter03:management of memory and huge pages resources`.

User namespaces in Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:** ``e.man.004`` in the Cloud Infrastructure Management Capabilities section in Chapter 4 of
:cite:t:`refmodel_ra2`, :ref:`inf.ntw.03 <ref_arch/kubernetes/chapters/chapter02:Kubernetes Architecture Requirements>`

**Baseline project:** *Kubernetes*

**Gap description:** Kubernetes does not support namespace scoped user IDs (UIDs). Therefore, when a CNF requires system
privileges, the container either needs to run in privileged mode, or the infrastructure needs to provide random system
UIDs. Randomised UIDs result in errors when the application needs to set kernel capabilities (for example, in the case of
VLAN trunking), or when a Pod shares data with other Pods via persistent storage. The "privileged mode" solution is not secure
while "random UID" solution is error-prone. These techniques should therefore not be used. Support for proper user
namespaces in Kubernetes has been introduced as an alpha feature in Kubernetes 1.25 :cite:t:`kubernetes-user-namespaces_ra2`
(relevant KEP :cite:t:`kubernetes-kep-user-namespaces_ra2`).
