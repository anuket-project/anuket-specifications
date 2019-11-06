[<< Back](https://cntt-n.github.io/CNTT/)

# CNTT Reference Architectures

<a name="available-ra"></a>
## Available Reference Architectures
* [Openstack Based](openstack)
* [Kubernetes Based](kubernetes)

<a name="principles"></a>
## Principles
**Preamble**

CNTT develops a limited number of NFVI reference architectures. While technology and deployment aspects may differ between them, each of the CNTT reference architectures is based on a common CNTT Reference Model.

There are a number of key architectural principles that apply to all Reference Architectures produced by CNTT. These principles are enumerated below. They are meant to be general and at a high level, and limited in number. Some of the chapters of this document will include more specific principles to provide the implementation guidelines for a particular function or a specific component. Note that the Architectural Principles discussed in this Chapter follow the over-arching principles provided in [CNTT Reference Model:Introduction:Principles](https://cntt-n.github.io/CNTT/doc/ref_model/chapters/chapter01.html#1.3)


We need to distinguish between architectural principles and architectural requirements elaborated later in this document. The principles are here to guide our architectural thinking, while requirements should be understood as a check list used to gauge a level of compliance of a NFVI implementation to the CNTT reference architecture.

1. **Open source preference:** To ensure, by building on technology available in open source projects, that suppliers’ and operators’ investment have a tangible pathway towards a standard and production ready NFVI solution portfolio.

1. **Open APIs:** To enable interoperability and component substitution, and minimize integration efforts by uisng openly published API definitions.

1. **Separation of concerns:** To promote lifecycle independence of different architectural layers and modules (e.g. disagregation of software from hardware).

1. **Automated lifecycle management:** To minimize costs of the end-to-end lifecycle, maintenance downtime (target zero downtime), avoid errors and discrepancies resulting from manual processes.

1. **Automated scalability:** To minimize costs and operational impacts through automated policy-driven scaling of workloads by enabling automated horizontal scalability of workloads.

1. **Automated closed loop assurance:** To minimize operational costs and simplify NFVI platform operations by using automated fault resolution and performance optimization.

1. **Cloud nativeness:** To optimise the utilization of resources and enable operational efficiencies.

1. **Security compliance:** To ensure the architecture follows the industry best security practices and is at all levels compliant to relevant security regulations.

1. **Resilience and Availability:** To allow High Availability and Resilience for hosted VNFs, and to avoid Single Point of Failure.

<a name="ra-relationship-scope"></a>
## Reference Architectures Relationships and Scope

<p align="center"><img src="./figures/ref_arch_relationships.png" alt="Scope and Relationships" title="Scope and Relationships" width="80%"/></p>
<p align="center"><b>Figure 1:</b> Relationships between and scope of the CNTT Reference Architectures</p>


RA1 is focussing on an OpenStack Reference Architecture that will support VM-based VNFs only (i.e. no containerised workloads), whilst delivering the NFVI and VIM requirements as outlined in the Reference Model.

RA2 is adding to this by providing a Kubernetes Reference Architecture that will enable the support for Cloud native Network Functions (CNFs) that comprise of either containers or VMs (both of which would be managed through Kubernetes). Note that RA2 is not looking to support the running of VNFs through Kubernetes (this would likely invoke discussions relating to Kubernetes as a VIM, which is not appropriate at this time).

Key notes:
- The primary difference between VNF and CNF in this context is the maturity of the software to be able to make use of immutable infrastructure, not whether it is a VM or not
- RA2 scope will include mention of Kubernetes cloud providers that may integrate with other clouds (i.e. other than OpenStack as defined in RA1)
- For the purposes of a CNTT Reference Implementation / Reference Certification the only fully conformant implementation of Kubernetes will be a Kubernetes that is conformant with RA2 that is itself deployed on an OpenStack deployment that is conformant with RA1
- Note, any gaps identified between the two (e.g. RA2 includes support for bare metal containerisation but RA1 only deals with VM-based workloads) must be raised as Issues associated with the appropriate workstream
