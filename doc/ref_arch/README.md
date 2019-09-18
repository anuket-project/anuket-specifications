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
