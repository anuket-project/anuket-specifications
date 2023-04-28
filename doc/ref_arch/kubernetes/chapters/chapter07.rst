Gaps, Innovation, and Development
=================================

Introduction to Gaps, Innovation, and Development
-------------------------------------------------

During the development of this Reference Architecture, gaps that require addressing may be identified. This chapter
will highlight these gaps in detail and may provide proposed solutions. As a result, various “upstream” community
projects may be identified and will be targeted for development efforts.

Gap template
~~~~~~~~~~~~

   **Related requirements:** List the requirement references ``abc.xyz.00`` from RA2 or RM which this gap tries to
   address.

..

   **Baseline project:** Describe against which upstream project the gap exists e.g. *Kubernetes*. If the gap is not
   against any specific upstream project, state "none".

   **Gap description:** Describe which functionality described in the related requirements is currently missing in the
   implementations you're aware of. Include references to work ongoing in the target project, which may adress the gap.

.. Container run-time Interfaces towards NFVI resources
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..
..   (unclear) This is the southbound interface from the container to the infrastructure resources provided by the IaaS provider.
..
..
..
   e.g., network interface type that is presented to a running container.

Multi-tenancy and workload isolation with Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:** ``e.man.004``, ``sec.ci.008``, ``sec.wl.005``, ``sec.wl.006``

**Baseline project:** *Kubernetes*

**Gap description:** Today, Kubernetes lacks hard multi-tenancy capabilities that give the ability to allow untrusted
tenants to share infrastructure resources. This presents a security problem when operators seek to separate workloads
by categorization or even just production vs non-production. Further, tenant networks need to be both segregated, but
still centrally administered and maintained. Beyond just security, this also presents an operational problem. Trying to
deploy too many CNFs into the same cluster could result in version conflicts, configuration conflicts, and problems with
software life cycle management. Finally, without proper isolation there is an increased risk of cascading failures.

**Proposals & Resolution:** Kubernetes is not a single cluster solution. This has been demonstrated across the
industry from case studies at prominent companies like :cite:t:`alibaba-blog-twitter`, :cite:t:`youtube-zalando`, and
:cite:t:`cncf-blog-alibaba` to the bi-annual CNCF survey that finds that the number of clusters being deployed within
an organization is growing. While there are many reasons behind the multi cluster paradigm, examining the gap above we
find that a multi cluster solution can address many of these problems like security and software life cycle management.

Without multi tenancy within a cluster, separate clusters must be used to provide adequate separation for CNFs that
require strong isolation. CNFs may need to be separated for various reasons including different types of
workloads based on their vendors, environments like production vs. non production, per categorization, or supporting
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

   **Baseline project:** *Kubernetes*, *Kubevirt*

   **Gap description:** Kubernetes and at least one CRI compliant runtime should support the running of VNFs without
   requiring changes to the VNF's architecture and deployment artifacts.

Native Multiple network interfaces on Pods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** Virtual Network Interface Specifications section in Chapter 4 of :cite:t:`refmodel`

   **Baseline project:** *Kubernetes*

   **Gap description:** Kubernetes does not have native support for multiple Pod interfaces, therefore a CNI
   multiplexer, like :cite:t:`github-multus` is needed to provision multiple interfaces.
   Implementation of different network services for the interfaces, like Network Policies, Ingress, Egress or Load
   Balancers depends on the feature set of the CNI multiplexer and the CNI plugins it uses, therefore it is
   inconsistent.

   **Status:** There is a :cite:t:`googledocs-kep-multi-network-pod-object` created to support multiple Pod interfaces
   natively.

Dynamic network management
~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** inf.ntw.03 in :ref:`chapters/chapter02:kubernetes architecture requirements`

   **Baseline project:** *Kubernetes*

   **Gap description:** Kubernetes does not have an API for network service (e.g., VPNs) management, therefore a
   CNI plugin, like :cite:t:`github-multus`, needs to be used to expose APIs for Network
   services.
   Alternatively this is done today with Netconf etc., integration with SDN controllers, for example connecting
   individual VPNs - e.g., L3VPN - onto the CNF, on demand.

Control Plane Efficiency
~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** None

   **Baseline project:** *Kubernetes*

   **Gap description:** For example, in situations where multiple sites / availability zones exist, an operator may
   choose to run multiple Kubernetes clusters, not only for security/multitenancy reasons but also fault, resilience,
   latency, etc.
   This produces an overhead of Kubernetes Control plane nodes - there should be a way to operate multiple clusters
   more efficiently whilst still able to meet the non-functional requirements of the operator (fault, resilience,
   latency, etc.)

Interoperability with VRF-based networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Related requirements:** None

   **Baseline project:** *Kubernetes*

   **Gap description:** For example, in existing networks, L3 VRFs/VPNs are commonly used for traffic separation (e.g.,
   separate L3 VPN for signalling, charging, LI, O&M etc.). CNFs will have to interwork with existing network elements
   and therefore a K8s POD will somehow need to be connected to a L3 VPN. Today this is only possible via Multus
   (or DANM), however typically there is a network orchestration responsibility to connect the network interface to a
   gateway router (where the L3 VPN is terminated). This network orchestration is not taken care of by K8s, nor there
   is a production grade solution in the open source space to take care of this.

Note: with an underlying IaaS this is possible, but then it introduces (undesirable) dependency between workload
orchestration in K8s and infrastructure orchestration in IaaS.

HW topology aware huge pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:** ``infra.com.cfg.004`` and ``infra.com.cfg.002`` in the Virtual Compute Profiles section in
Chapter 5 of :cite:t:`refmodel`.

**Baseline project:** *Kubernetes*

**Gap description:** Memory Manager was added in v1.21 as alpha feature. More in
:ref:`chapters/chapter03:management of memory and huge pages resources`.

User namespaces in Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Related requirements:** ``e.man.004`` in the Cloud Infrastructure Management Capabilities section in Chapter 4 of
:cite:t:`refmodel`, :ref:`inf.ntw.03 <chapters/chapter02:platform and access requirements>`

**Baseline project:** *Kubernetes*

**Gap description:** Kubernetes does not support namespace scoped user IDs (UIDs). Therefore, when a container-based
application requires system privileges the container either needs to run in privileged mode or the infrastructure needs
to provide random system UIDs. Randomised UIDs result in errors when the application needs to set kernel capabilities
(e.g., in case of VLAN trunking) or when a Pod shares data with other Pods via persistent storage. The
"privileged mode" solution is not secure while "random UID" solution is error prone, and therefore these techniques
should not be used. Support for proper user namespaces in Kubernetes has been introduced as alpha feature in
Kubernetes 1.25 :cite:t:`kubernetes-user-namespaces` (relevant KEP :cite:t:`kubernetes-kep-user-namespaces`).
