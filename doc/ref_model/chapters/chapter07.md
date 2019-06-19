[<< Back](../../ref_model)
# 7	APIs & Interfaces
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [7.1 Infra related APIs.](#)
  * [2.1 VNFs collateral (Sample).](#)
* [7.2 NFVI APIs.](#)
* [7.3 Supporting Enabler Service APIs (not-MVP).](#)
  * [7.3.1 NTP, DNS, etc.](#)
  * [7.3.2 Licensing and imaging connectivity.](#)
* [7.4 Acceleration Interfaces and APIs (not-MVP).](#)
* [7.5 Tool functionalities needed (not-MVP).](#)
  * [7.5.1 Categorized (not specifically named).](#)
  * [7.5.2 Policies and Security related primarily.](#)
  * [7.5.3 If embedded in VM.](#)
* [7.6 Cloud agnostic (not-MVP).](#)	
* [7.7 IPL (Reference Model component only) (not-MVP).](#)	 
 
In this document’s earlier chapters, the various resources and capabilities of the NFVI have been catalogued and the workloads (VNFs) have been profiled with respect to those capabilities. The intent behind this chapter and an “API Layer” is to similarly provide a single place to catalogue and thereby codify, a common set of open APIs to access (i.e. request, consume, control, etc.) the aforementioned resources, be them directly exposed to the VNFs, or purely internal to the NFVI.

It is a further intent of this chapter and this document to ensure the APIs adopted for CNTT NFVI implementations are open and not proprietary, in support of compatibility, component substitution and ability to realize maximum value from existing and future test heads and harnesses.

While it is the intent of this chapter, when included in a Reference Architecture, to catalogue the APIs, it is not the intent of this chapter to reprint the APIs, as this would make maintenance of the chapter impractical and the length of the chapter disproportionate within the Reference Model document. Instead, the APIs selected for CNTT NFVI implementations and specified in this chapter, will be incorporated by reference and URLs for the latest, authoritative versions of the APIs, provided in the References section of this document.

Although the document does not attempt to reprint the APIs themselves, where appropriate and generally where the mapping of resources and capabilities within the NFVI to objects in APIs would be otherwise ambiguous, this chapter shall provide explicit identification and mapping.

In addition to the raw or base-level NFVI functionality to API and object mapping, it is further the intent to specify an explicit, normalized set of APIs and mappings to control the logical interconnections and relationships between these objects, notably, but not limited to, support of SFC (Service Function Chaining) and other networking and network management functionality.
It is initially proposed to divide the APIs into three primary categories, each reflecting a specific domain relative to the NFVI, as follows, and described in detail in the first three sections of this chapter:

1.	Intra-Infrastructure (NFVI) APIs
2.	NFVI APIs
3.	Enabler Services APIs

**Infra Related**: These APIs are provided and consumed directly by the infra. These APIs are purely internal to the NFVI, and not exposed to VNF workloads.

**NFVI APIs**: These APIs are provided to the VNF workloads (i.e. exposed), by the infra.

**Enabler Services**: These APIs are provided by functions which may be instantiated at higher layers (i.e. in user or workload space), and provide facilities that are required for a majority of VNFs. For example, DHCP, DNS, NTP, DBaaS, etc. Note, in some cases Enabler Services may mirror services provided within the Infra, such as DNS or DHCP. However, the purpose in this section is explicitly to describe instances of those services which are both hosted and consumed above the Infra water mark.
