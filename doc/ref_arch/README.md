[<< Back](https://cntt-n.github.io/CNTT/)

# CNTT Reference Architectures

<a name="available-ra"></a>
## Available Reference Architectures
* [Openstack Based](openstack)

<a name="principles"></a>
## Principles
**Preamble**

CNTT develops a limited number of NFVI reference architectures. While technology and deployment aspects may differ between them, each of the CNTT reference architectures is based on a common CNTT Reference Model. 

There are a number of key architectural principles that apply to all reference architectures produced by CNTT. These principles are enumerated below. They are meant to be general and at a high level, and limited in number. Some of the chapters of this document will include more specific principles to provide the implementation guidelines for a particular function or a specific component. 

We need to distinguish between architectural principles and architectural requirements elaborated later in this document. The principles are here to guide our architectural thinking, while requirements should be understood as a check list used to gauge a level of compliance of a NFVI implementation to the CNTT reference architecture.

1. **Open source preference:** To ensure that suppliers’ and operators’ investment have a tangible pathway towards a standard and production ready NFVI solution portfolio. 

1. **Open APIs:** To ensure interoperability and minimize integration efforts, and for component substitution.

1. **Disaggregation between clearly defined architecture layers:** To ensure proper separation of concern, example: disagregation of h/w and s/w.

1. **Automated lifecycle management:** To minimize costs of the whole lifecycle, support zero-downtime maintenance, avoid errors and discrepancies resulting from manual processes.

1. **Automated scalability:** To enable scaling out of workloads to minimize costs and operational impacts.

1. **Automated closed loop assurance:** To minimize operational costs and simplify operations.

1. **Cloud nativeness:** To utilise resource and ensure operational efficiencies of cloud native implementations

1. **Security compliance:** To ensure compliance at all level to industry and regional security requirements

1. **Resilience and Availability:** To allow High Availability and Resilience for hosted VNFs, and to avoid Single Point of Failure. 



