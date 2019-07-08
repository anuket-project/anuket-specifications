[<< Back](../../ref_model)
# 8	Security
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Common standards.](#8.1)
  * [8.1.1 Testing demarcation points.](#8.1.1)
* [8.2 Operator responsibility.](#8.2)
* [8.3 VNF Vendors responsibility.](#8.2)
* [8.4 NFVi Vendors responsibility (qualify what infrastructure means).](#8.3)

<a name="8.1"></a>
## 8.1 Common standards
Security vulnerabilities and attack vectors are everywhere.  The telecom industry and its cloud infrastructures are even more vulnerable to potential attacks due to the ubiquitous nature of the infrastructures and services combined with the vital role Telecommunications plays in the modern world.   The attack vectors are many and varied, ranging from the potential for exposure of sensitive data, both personal and corporate, to as far as weaponized disruption to the global Telecommunications networks.  The threats can take the form of a physical attack on the locations the infrastructure hardware is housed, to network attacks such as denial of service and corruption of the network service applications.  Whatever the source, any NFVi infrastructure built needs to be able to withstand attacks in whatever form they take.

With that in mind, the NFVi reference model and the supporting architectures not only required to optimally support networking functions, but they must be designed with common security principles and standards from inception.  These best practices must be applied at all layers of the infrastructure stack and all across all points of interconnection with outside networks, APIs and contact points with the Network functions overlaying the infrastructure. 

Standards organizations with recommendations and best practices that need to be taken into consideration include the following list of examples. However this is by no means an exhaustive list, just some of the more important standards include. 

•	Center for Internet Security - https://www.cisecurity.org/

•	Cloud Security Alliance - https://cloudsecurityalliance.org/

•	The National Institute of Standards and Technology (NIST) (US Only)

•	ETSI Cyber Security Technical Committee (TC CYBER) - https://www.etsi.org/committee/cyber

•	ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) - www.iso.org. The following ISO standards are of particular interest for NFVi

  o	ISO/IEC 27002:2013 - ISO/IEC 27001 is the international Standard for best-practice information security management systems (ISMSs).
  
  o	ISO/IEC 27032 - ISO/IEC 27032is the international Standard focusing explicitly on cybersecurity.
  
  o	ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management. Incident management
  
  o	ISO/IEC 27031 - ISO/IEC 27031 is the international Standard for ICT readiness for business continuity.

<a name="8.1.1"></a>
## 8.1.1 Testing demarcation points
It is not enough to just secure all potential points of entry and hope for the best, any NFVi architecture must be able to be tested and validated that it is protected from attack. The ability to test the infrastructure for vulnerabilities on a continuous basis is critical for maintaining the highest level of security possible.  Testing needs to be done both from the inside and outside of the systems and networks.  Below is a small sample of some of the testing methodologies and frameworks available.  

•	OWASP testing guide

•	PCI Penetration testing guide

•	Penetration Testing Execution Standard

•	NIST 800-115

•	Penetration Testing Framework

•	Information Systems Security Assessment Framework (ISSAF)

•	Open Source Security Testing Methodology Manual (“OSSTMM”)

•	FedRAMP Penetration Test Guidance (US Only)

•	CREST Penetration Testing Guide

Insuring that the security standards and best practices are incorporated into the NFVi model and architectures must be a shared responsibility, among the Telecommunications organizations interested in building and maintaining the infrastructures in support of their services, the VNF vendors developing the network services themselves, and the NFVi vendors creating the infrastructures for their Telecommunications customers.  All of the parties need to incorporate security and testing components, and maintain operational processes and procedures to address any security threats or incidents in an appropriate manner.

<a name="8.2"></a>
## 8.2 Operator responsibility
The Operator’s responsibility is to make sure that security is included in all the infrastructure and NFV components, but it is also responsible for the maintenance of the security functions from an operational and management perspective.   This includes but is not limited to securing the following elements:

•	Maintaining standard security operational management methods and processes

•	Monitoring and reporting

•	Support for appropriate incident response and reporting

<a name="8.3"></a>
## 8.3 VNF Vendors responsibility
The VNF vendors need to incorporate security elements to support the highest level of security of the networks they support.  This includes but is not limited to securing the following elements:

•	Operating system or container

•	Application

•	Network interfaces

•	Controller systems

Image from https://www.networkworld.com/article/2840273/sdn-security-attack-vectors-and-sdn-hardening.html Will replace with a better image when I create it in the future.

<a name="8.4"></a>
## 8.4 NFVi Vendors responsibility
The NFVi vendors need to incorporate security elements to support the highest level of security of the infrastructure they support.  This includes but is not limited to securing the following elements:

•	Hypervisor

•	VM/container management system

•	APIs

•	Network interfaces

