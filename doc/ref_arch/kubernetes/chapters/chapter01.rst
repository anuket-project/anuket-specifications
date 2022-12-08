Overview
========

Introduction
------------

The objective of this Reference Architecture (RA) is to develop a usable Kubernetes-based platform for the Telco
industry. The RA will be based on the standard Kubernetes platform wherever possible. This Reference Architecture
for Kubernetes will describe the high level system components and their interactions, taking the goals and requirements
from the :doc:`Reference Model <ref_model:index>` (RM) and mapping them to Kubernetes (and related) components. This document
needs to be sufficiently detailed and robust such that it can be used to guide the production deployment of Kubernetes
within an operator, whilst being flexible enough to evolve with and remain aligned with the wider Kubernetes ecosystem
outside of Telco.

To set this in context, it makes sense to start with the high level definition and understanding of Kubernetes.
`Kubernetes <https://kubernetes.io/>`__ is a "portable, extensible, open-source platform for managing containerised
workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing
ecosystem. Kubernetes services, support, and tools are widely available"
[`kubernetes.io <https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/>`__]. Kubernetes is developed as an
open source project in the `kubernetes/kubernetes <https://github.com/kubernetes/kubernetes>`__ repository of GitHub.

To assist with the goal of creating a reference architecture that will support Telco workloads, but at the same time
leverage the work that already has been completed in the Kubernetes community, RA2 will take an
"RA2 `Razor <https://en.wikipedia.org/wiki/Philosophical_razor>`__" approach to build the foundation. This can be
explained along the lines of "if something is useful for non-Telco workloads, we will not include it only for Telco
workloads". For example, start the Reference Architecture from a vanilla Kubernetes (say, v1.16) feature set, then
provide clear evidence that a functional requirement cannot be met by that system (say, multi-NIC support), only then
the RA would add the least invasive, Kubernetes-community aligned extension (say, Multus) to fill the gap. If there are
still gaps that cannot be filled by standard Kubernetes community technologies or extensions then the RA will concisely
document the requirement in the :doc:`"Gaps, Innovation, and Development"<chapters/chapter07>` chapter of this document
and approach the relevant project maintainers with a request to add this functionality into the feature set.

The Kubernetes Reference Architecture will be used to determine a Kubernetes Reference Implementation. The Kubernetes
Reference Implementation would then also be used to test and validate the supportability and compatibility with
Kubernetes-based Network Function workloads, and lifecycle management of Kubernetes clusters, of interest to the Anuket
community. The intention is to expand as much of the existing test frameworks to be used for the verification and
conformance testing of Kubernetes-based workloads, and Kubernetes cluster lifecycle management.

Terminology
~~~~~~~~~~~

For terminology used in this document refer to the :ref:`cntt:common/glossary:glossary`.

.. replace with glossary table

Architectural Principles
------------------------

This Reference Architecture conforms with the Anuket principles:

1. **Open-source preference:** for building Cloud Infrastructure
   solutions, components and tools, using open-source technology.
2. **Open APIs:** to enable interoperability, component
   substitution, and minimise integration efforts.
3. **Separation of concerns:** to promote lifecycle independence of
   different architectural layers and modules (e.g., disaggregation of
   software from hardware).
4. **Automated lifecycle management:** to minimise the
   end-to-end lifecycle costs, maintenance downtime (target zero
   downtime), and errors resulting from manual processes.
5. **Automated scalability:** of workloads to minimise costs and
   operational impacts.
6. **Automated closed loop assurance:** for fault resolution,
   simplification, and cost reduction of cloud operations.
7. **Cloud nativeness:** to optimise the utilisation of resources
   and enable operational efficiencies.
8. **Security compliance:** to ensure the architecture follows
   the industry best security practices and is at all levels compliant
   to relevant security regulations.
9. **Resilience and Availability:** to withstand
   Single Point of Failure.

Cloud Native Principles
~~~~~~~~~~~~~~~~~~~~~~~

For the purposes of this document, the CNCF TOC's (Technical Oversight Committee) definition of Cloud Native applies:

   CNCF Cloud Native Definition v1.0
   Approved by TOC: 2018-06-11

   “Cloud native technologies empower organizations to build and run **scalable** applications in modern,
   **dynamic environments** such as public, private, and hybrid clouds. Containers, **service meshes**,
   **microservices**, **immutable infrastructure**, and **declarative APIs** exemplify this approach.

   These techniques enable **loosely coupled** systems that are **resilient**, **manageable**, and **observable**.
   Combined with **robust automation**, they allow engineers to make **high-impact changes frequently and predictably**
   with minimal toil.

   The Cloud Native Computing Foundation seeks to drive adoption of this paradigm by fostering and sustaining an
   ecosystem of open source, vendor-neutral projects. We democratize state-of-the-art patterns to make these innovations
   accessible for everyone.”

The CNCF TUG (Telecom User Group), formed in June 2019, published a set of Cloud Native Principles suited to the
requirements of the Telecom community:
`Expanded Cloud Native Principles <https://networking.cloud-native-principles.org/cloud-native-principles>`__. 
There are many similarities with the CNCF principles, briefly that infrastructure needs to be:

-  **scalable**
-  **dynamic environments**
-  **service meshes**
-  **microservices**
-  **immutable infrastructure**
-  **declarative APIs**
-  **loosely coupled**
-  **resilient**
-  **manageable**
-  **observable**
-  **robust automation**
-  **high-impact changes frequently and predictably**

Exceptions
~~~~~~~~~~

Anuket specifications define certain policies and :ref:`cntt:common/chapter00:anuket general principles` and strive to
coalesce the industry towards conformant Cloud Infrastructure technologies and configurations. With the currently
available technology options, incompatibilities, performance and operator constraints (including costs), these
policies and principles may not always be achievable and, thus, require an exception process. These policies
describe how to handle :ref:`cntt:common/policies:anuket project policies for managing non-conforming technologies`.
In general, non-conformance with policies is handled through a set of exceptions (please also see
:ref:`cntt:gov/chapters/chapter09:exception types`).

The following sub-sections list the exceptions to the principles of Anuket specifications and shall be updated whenever
technology choices, versions and requirements change. The Exceptions have an associated period of validity and this
period shall include time for transitioning.

Technology Exceptions
^^^^^^^^^^^^^^^^^^^^^

The list of Technology Exceptions will be updated or removed when alternative technologies, aligned with the principles
of Anuket specifications, develop and mature.

.. list-table:: Technology Exceptions
   :widths: 10 10 20 5 50 5
   :header-rows: 1

   * - Ref
     - Name
     - Description
     - Valid Until
     - Rationale
     - Implication
   * - ra2.exc.tec.001
     - SR-IOV
     - This exception allows workloads to use SR-IOV over PCI-PassThrough technology.
     - TBD
     - Emulation of virtual devices for each virtual machine creates an I/O
       bottleneck resulting in poor performance and limits the number of virtual
       machines a physical server can support. SR-IOV implements virtual devices
       in hardware, and by avoiding the use of a switch, near maximal performance
       can be achieved. For containerisation the downsides of creating dependencies
       on hardware is reduced as Kubernetes nodes are either physical, or if virtual
       have no need to "live migrate" as a VNF VM might.
     -

.. Requirements Exceptions
.. ^^^^^^^^^^^^^^^^^^^^^^^

.. The Requirements Exceptions lists the Reference Model (RM) requirements and/or Reference Architecture (RA) requirements
.. that will be either waived or be only partially implemented in this version of the RA. The exception list will be
.. updated to allow for a period of transitioning as and when requirements change.

.. .. list-table:: Requirements Exceptions
..    :widths: 10 10 20 5 50 5
..    :header-rows: 1

..    * - Ref
..      - Name
..      - Description
..      - Valid Until
..      - Rationale
..      - Implication
..    * - ra1.exc.req.001
..      - Req.
..      - xxxx
..      - xxxxxxx
..      -
..      -

Scope
-----

The scope of this particular Reference Architecture can be described as follows (the capabilities themselves will be
listed and described in subsequent chapters), also shown in :numref:`Kubernetes Reference Architecture scope`

-  Kubernetes platform capabilities required to conform to the Reference Model requirements
-  Support for CNFs that consist wholly of containers
-  Support for CNFs that consist partly of containers and partly of VMs, both of which will be orchestrated by
   Kubernetes
-  **Kubernetes Cluster lifecycle management**: including Cluster creation/upgrade/scaling/deletion, and node
   customisation due to workload requirements.

The following items are considered **out of scope**:

-  **Kubernetes-based Application / VNF Management**: this is an application layer capability that is
   out of scope of Anuket.

.. figure:: ../figures/ch01_scope_k8s.png
   :alt: Kubernetes Reference Architecture scope
   :name: Kubernetes Reference Architecture scope

   Kubernetes Reference Architecture scope

Approach
--------

The approach taken in this Reference Architecture is to start with a basic Kubernetes architecture, based on the
community distribution, and then add detail and additional features/extensions as is required to meet the requirements
of the Reference Model and the functional and non-functional requirements of common cloud native network functions.

This document starts with a description of interfaces and capabilities requirements (the "what") before providing
guidance on "how" those elements are deployed, through specifications. The details of how the elements will be used
together are documented in full detail in the Reference Implementation.
