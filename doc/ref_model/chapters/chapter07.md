[<< Back](../../ref_model)
# 7 Security

## Table of Contents
* [7.1 Introduction](#7.1)
* [7.2 Potential attack vectors](#7.2)
* [7.3 Security Scope](#7.3)
  * [7.3.1 In-scope and Out-of-Scope definition](#7.3.1)
  * [7.3.2 High level security requirements](#7.3.2)
* [7.4 Cloud Infrastructure Security](#7.4)
  * [7.4.1 General Platform Security](#7.4.1)
  * [7.4.2 Platform ‘back-end’ access security](#7.4.2)
  * [7.4.3 Platform ‘front-end’ access security](#7.4.3)
* [7.5 Workload Security - Vendor Responsibility](#7.5)
  * [7.5.1 Software Hardening](#7.5.1)
  * [7.5.2 Port Protection](#7.5.2)
  * [7.5.3 Software Code Quality and Security](#7.5.3)
  * [7.5.4 Alerting and Monitoring](#7.5.4)
  * [7.5.5 Logging](#7.5.5)
  * [7.5.6 VNF images](#7.5.6)
  * [7.5.7 Vulnerability Management](#7.5.7)
* [7.6 Workload Security- Cloud Infrastructure Operator Responsibility](#7.6)
  * [7.6.1 Remote Attestation/openCIT](#7.6.1)
  * [7.6.2 Workload Image Scanning / Signing](#7.6.2)
  * [7.6.3 Networking Security Zoning](#7.6.3)
  * [7.6.4 Encryption](#7.6.4)
  * [7.6.5 Root of Trust for Measurements (RTM)](#7.6.5)
* [7.7 Common security standards](#7.7)
* [7.8 Testing & Certification](#7.8)
* [7.9 Consolidated Security requirements](#7.9)
  * [7.9.1 System Hardening](#7.9.1)
  * [7.9.2 Platform Access](#7.9.2)
  * [7.9.3 Confidentiality and Integrity](#7.9.3)
  * [7.9.4 Workload Security](#7.9.4)
  * [7.9.5 Image Security](#7.9.5)
  * [7.9.6 Security LCM](#7.9.6)
  * [7.9.7 Monitoring and Security Audit](#7.9.7)
  * [7.9.8 Compliance with Standards](#7.9.8)
 * [7.10 Security References](#7.10)


<a name="7.1"></a>
## 7.1 Introduction

Security vulnerabilities and attack vectors are everywhere.  The Telecom industry and its cloud infrastructures are even more vulnerable to potential attacks due to the ubiquitous nature of the infrastructures and services combined with the vital role Telecommunications play in the modern world. The attack vectors are many and varied, ranging from the potential for exposure of sensitive data, both personal and corporate, to weaponized disruption to the global telecommunications networks.  The threats can take the form of a physical attack on the locations the infrastructure hardware is housed, to network attacks such as denial of service and targeted corruption of the network service applications themselves.  Whatever the source, any Cloud Infrastructure built needs to be able to withstand attacks in whatever form they take.

This chapter examines multiple aspects of security as it relates to Cloud Infrastructure and security aspects for workloads. After discussing security attack vectors, this chapter delves into security requirements. Regarding security requirements and best practices, specifications and documents are published by standards organizations. A selection of standards of interest for Cloud Infrastructure security is listed in a dedicated section. The chapter culminates with a consolidated set of “must” requirements and desired (should) recommendations; it is suggested that operators carefully evaluate the recommendations for possible implementation.

<a name="7.2"></a>
## 7.2 Potential attack vectors
Previously attacks designed to place and migrate workload outside the legal boundaries were not possible using traditional infrastructure, due to the closed nature of these systems. However, using Cloud Infrastructure, violation of regulatory policies and laws becomes possible by actors diverting or moving an application from an authenticated and legal location to another potentially illegal location. The consequences of violating regulatory policies may take the form of a complete banning of service and/or an exertion of a financial penalty by a governmental agency or through SLA enforcement.  Such vectors of attack may well be the original intention of the attacker in an effort to harm the service provider. One possible attack scenario can be when an attacker exploits the insecure VNF API to dump the records of personal data from the database in an attempt to violate user privacy. Cloud Infrastructure operators should ensure that the applications APIs are secure, accessible over a secure network (TLS) under very strict set of security best practices, and RBAC policies to limit exposure of this vulnerability.

<a name="7.3"></a>
## 7.3 Security Scope

<a name="7.3.1"></a>
### 7.3.1 In-scope and Out-of-Scope definition

The scope of the security controls requirements maps to the scope of the Reference Model architecture.

Cloud Infrastructure requirements must cover the virtual infrastructure layer and the hardware infrastructure layer, including virtual resources, hardware resources, virtual infrastructure manager and hardware infrastructure manager, as described in Chapter 3.
 
<a name="7.3.2"></a>
### 7.3.2 High level security Requirements

The following diagram shows the different security domains that impact the Reference Model:

<p align="center"><img src="../figures/ch7_security_posture.png" alt="Overview" title="Security Domains" width="100%"/></p>
<p align="center"><b>Figure 7-1:</b> Reference Model Security Domains</p>

Note: "Platform" refers to the Cloud Infrastructure with all its hardware and software components.

<a name="7.3.2.1"></a>
#### 7.3.2.1 Platform security requirements

At a high level, the following areas/requirements cover platform security for a particular deployment:
* Platform certification
* Secure access controls for administrators
* Secure API interface for tenants
* Encryption for all external and control communications
* Strong separation between tenants - ensuring network, data, memory and runtime process (CPU running core) isolation between tenants
* Authenticated/secure APIs provided to overlay network administrators
* Platform change control on hardware
* Templated approved changes for automation where available
* Typically well-defined security framework documentation including approved deployment use cases
* Infrastructure software update process

<a name="7.3.2.2"></a>
#### 7.3.2.2 Workload security requirements

At a high level, the following areas/requirements cover workload security for a particular deployment:
* Up to platform-level certification
* Each workload network will need to undertake it own security self-assessment and accreditation, and not inherit a security accreditation from the platform
* Potentially automated service activation
* Workload owner owns workload security certification process
* Workload owner owns workload design change process
* Workload owner owns workload software update process
  

<a name="7.4"></a>
## 7.4 Cloud Infrastructure Security

<a name="7.4.1"></a>
### 7.4.1 General Platform Security

The security certification of the platform will typically need to be the same, or higher, than the workload or VNF requirements.

The platform supports the workload, and in effect controls access to the workload from and to external endpoints such as carriage networks used by workloads, or by Data Centre Operations staff supporting the workload, or by tenants accessing workloads. From an access security perspective, the following diagram shows where different access controls will operate within the platform to provide access controls throughout the platform:

<p align="center"><img src="../figures/ch7-data-access-model.png" alt="Overview" title="Access Controls" width="100%"/></p>
<p align="center"><b>Figure 7-2:</b> Reference Model Access Controls</p>

<a name="7.4.1.1"></a>
#### 7.4.1.1 The high-level functions of these different access controls

* **MGNT ACCESS CONTROLS** - Platform access to workloads for service management. Typically all management and control-plane traffic is encrypted.
* **DATA ACCESS CONTROLS** - Control of east-west traffic between workloads, and control of north-south traffic between the VNF and other platform services such as front-end carriage networks and platform services. Inherently strong separation between tenants is mandatory.
* **SERVICES ACCESS CONTROLS** - Protects platform services from any platform access
* **BACK-END ACCESS CONTROLS** - Data Centre Operations access to the platform, and subsequently, workloads. Typically stronger authentication requirements such as (Two-Factor Authentication) 2FA, and using technologies such as Role-Based Access Control (RBAC) and encryption. Application Programming Interface (API) gateways may be required for automated/script-driven processes.
* **FRONT-END ACCESS CONTROLS** - Protects the platform from malicious carriage network access, and provides connectivity for specific workloads to specific carriage networks. Carriage networks being those that are provided as public networks and operated by carriers, and in this case with interfaces that are usually sub, or virtual networks.
* **TENANT ACCESS CONTROLS** - Provides appropriate tenant access controls to specific platform services, and tenant workloads - including Role-Based Access Control (RBAC), authentication controls as appropriate for the access arrangement, and Application Programming Interface (API) gateways for automated/script-driven processes.

<a name="7.4.1.2"></a>
#### 7.4.1.2 The following general security requirements apply to the Cloud Infrastructure

**System Hardening**
* Adhering to the principle of least privilege, no login to root on any platform systems (platform systems are those that are associated with the platform and include systems that directly or indirectly affect the viability of the platform) when root privileges are not required.
* Ensure that all the platform's components (including hypervisors, VMs, etc.) are kept up to date with the latest patch.
* In order to tightly control access to resources and protect them from malicious access and introspection, Linux Security Modules such as SELinux should be used to enforce access rules.

**Platform access**
* Restrict traffic to only traffic that is necessary, and deny all other traffic, including traffic from and to 'Back-end'.
* Provide protections between the Internet and any workloads including web and volumetrics attack preventions.
* All host to host communications within the cloud provider network are to be cryptographically protected in transit.
* Use cryptographically-protected protocols for administrative access to the platform.
* Data Centre Operations staff and systems must use management protocols that limit security risk such as SNMPv3, SSH v2, ICMP, NTP, syslog, and TLS v1.2 or higher.
* Processes for managing platform access control filters must be documented, followed, and monitored.
* Role-Based Access Control (RBAC) must apply for all platform systems access.
* All APIs access must use TLS protocol, including back-end APIs.

**Workload security**
* Restrict traffic to (and from) the workload to only traffic that is necessary, and deny all other traffic.
* Support zoning within a tenant workload - using application-level filtering.
* Not expose tenant internal IP address details to another tenant.
* All production workloads must be separated from all non-production workloads including separation between non-hosted non-production external networks.

**Confidentiality and Integrity**
* All data persisted to primary, replica, or backup storage is to be encrypted.

**Monitoring and security audit**
* All platform security logs are to be time synchronised.
* Logs are to be regularly scanned for events of interest.
* The cloud services must be regularly vulnerability and penetration tested.

**Platform provisioning and LCM**
* A platform change management process that is documented, well communicated to staff and tenants, and rigorously followed.
* A process to check change management adherence that is implemented, and rigorously followed.
* An approved system or process for last resort access must exist for the platform.
* Where there are multiple hosting facilities used in the provisioning of a service, network communications between the facilities for the purpose of backup, management, and workload communications are cryptographically protected in transit between data centre facilities.
* Continuous Cloud security compliance is mandatory.
* An incident response plan must exist for the platform.

<a name="7.4.2"></a>
### 7.4.2 Platform ‘back-end’ access security

* Validate and verify the integrity of resources management requests coming from a higher orchestration layer to the Cloud Infrastructure manager.

<a name="7.4.3"></a>
### 7.4.3 Platform ‘front-end’ access security

* Front-end network security at the application level will be the responsibility of the workload, however the platform must ensure the isolation and integrity of tenant connectivity to front-end networks.
* The front-end network may provide (Distributed Denial Of Service) DDOS support.


<a name="7.5"></a>
## 7.5 Workload Security - Vendor Responsibility

<a name="7.5.1"></a>
### 7.5.1 Software Hardening

* No hard-coded credentials or clear text passwords. Software should support configurable, or industry standard, password complexity rules.
* Software should be independent of the infrastructure platform (no OS point release dependencies to patch).
* Software is code signed and all individual sub-components are assessed and verified for EULA violations.
* Software should have a process for discovery, classification, communication, and timely resolution of security vulnerabilities (i.e.; bug bounty, Penetration testing/scan findings, etc.).
* Software should support recognized encryption standards and encryption should be decoupled from software.
* Software should have support for configurable banners to display authorized use criteria/policy.


<a name="7.5.2"></a>
### 7.5.2 Port Protection

* Unused software and unused network ports should be disabled by default.

<a name="7.5.3"></a>
### 7.5.3 Software Code Quality and Security

* Vendors should use industry recognized software testing suites
  * Static and dynamic scanning.
  * Automated static code review with remediation of Medium/High/Critical security issues. The tool used for static code analysis and analysis of code being released must be shared.
  * Dynamic security tests with remediation of Medium/High/Critical security issues. The tool used for Dynamic security analysis of code being released must be shared.
  * Penetration tests (pen tests) with remediation of Medium/High/Critical security issues.
  * Methodology for ensuring security is included in the Agile/DevOps delivery lifecycle for ongoing feature enhancement/maintenance.

<a name="7.5.4"></a>
### 7.5.4 Alerting and monitoring

* Security event logging: all security events must be logged, including informational.
* Privilege escalation must be detected.

  <a name="7.5.5"></a>
### 7.5.5 Logging

* Logging output should support customizable Log retention and Log rotation.

  <a name="7.5.6"></a>
### 7.5.6 VNF images

* Image integrity – fingerprinting/validation.
* Container Images
  * Container Management.
  * Immutability.

<a name="7.5.7"></a>
### 7.5.7 Vulnerability Management

* Security defect must be reported.
* Cadence should aligned with Cloud Infrastructure vendors (OSSA for OpenStack).
* Components should be analysed: mechanisms to validate components of the platform stack by checking libraries and supporting code against the Common Vulnerabilities and Exposures (CVE) databases to determine whether the code contains any known vulnerabilities must be embedded into the NFVI architecture itself.  Some of the components required include tools for checking common libraries against CVE databases integrated into the deployment and orchestration pipelines.

<a name="7.6"></a>
## 7.6 Workload Security - Cloud Infrastructure Operator Responsibility

The Operator’s responsibility is to not only make sure that security is included in all the vendor supplied infrastructure and NFV components, but it is also responsible for the maintenance of the security functions from an operational and management perspective. This includes but is not limited to securing the following elements:

* Maintaining standard security operational management methods and processes.
* Monitoring and reporting functions.
* Processes to address regulatory compliance failure.
* Support for appropriate incident response and reporting.
* Methods to support appropriate remote attestation certification of the validity of the security components, architectures, and methodologies used.

<a name="7.6.1"></a>
### 7.6.1 Remote Attestation/openCIT

Cloud Infrastructure operators must ensure that remote attestation methods are used to remotely verify the trust status of a given Cloud Infrastructure platform.  The basic concept is based on boot integrity measurements leveraging the Trusted Platform Module (TPM) built into the underlying hardware. Remote attestation can be provided as a service, and may be used by either the platform owner or a consumer/customer to verify that the platform has booted in a trusted manner. Practical implementations of the remote attestation service include the Open Cloud Integrity Tool (Open CIT).   Open CIT provides ‘Trust’ visibility of the Cloud Infrastructure and enables compliance in Cloud Datacenters by establishing the root of trust and builds the chain of trust across hardware, operating system, hypervisor, VM, and container.  It includes asset tagging for location and boundary control. The platform trust and asset tag attestation information is used by Orchestrators and/or Policy Compliance management to ensure workloads are launched on trusted and location/boundary compliant platforms. They provide the needed visibility and auditability of infrastructure in both public and private cloud environments.

<a name="7.6.2"></a>
### 7.6.2 Workload Image Scanning / Signing

It is easy to tamper with workload images. It requires only a few seconds to insert some malware into a workload image file while it is being uploaded to an image database or being transferred from an image database to a compute node. To guard against this possibility, workload images can be cryptographically signed and verified during launch time. This can be achieved by setting up a signing authority and modifying the hypervisor configuration to verify an image’s signature before they are launched. To implement image security, the VNF operator must test the image and supplementary components verifying that everything conforms to security policies and best practices.

Use of Image scanners such as OpenSCAP to determine security vulnerabilities is strongly recommended.

<a name="7.6.3"></a>
### 7.6.3 Networking Security Zoning

Network segmentation is important to ensure that applications can only communicate with the applications they are supposed to. To prevent a workload from impacting other workloads or hosts, it is a good practice to separate workload traffic and management traffic. This will prevent attacks by VMs or containers breaking into the management infrastructure. It is also best to separate the VLAN traffic into appropriate groups and disable all other VLANs that are not in use. Likewise, workloads of similar functionalities can be grouped into specific zones and their traffic isolated. Each zone can be protected using access control policies and a dedicated firewall based on the needed security level.

Recommended practice to set network security policies following the principle of least privileged, only allowing approved protocol flows. For example, set 'default deny' inbound and add approved policies required for the functionality of the application running on the NFV Infrastructure.

<a name="7.6.4"></a>
### 7.6.4 Volume Encryption

Virtual volume disks associated with workloads may contain sensitive data. Therefore, they need to be protected. Best practice is to secure the workload volumes by encrypting them and storing the cryptographic keys at safe locations. Be aware that the decision to encrypt the volumes might cause reduced performance, so the decision to encrypt needs to be dependent on the requirements of the given infrastructure.  The TPM module can also be used to securely store these keys. In addition, the hypervisor should be configured to securely erase the virtual volume disks in the event of application crashes or is intentionally destroyed to prevent it from unauthorized access.


<a name="7.6.5"></a>
### 7.6.5 Root of Trust for Measurements (RTM)

The sections that follow define mechanisms to ensure the integrity of the infrastructure pre-boot and post-boot (running). The following defines a set of terms used in those sections.

-  The hardware root of trust helps with the pre-boot and post-boot security issues. 

-  Unified Extensible Firmware Interface (UEFI) adheres to standards defined by an industry consortium. Vendors (hardware, software) and solution providers collaborate to define common interfaces, protocols and  structures for computing  platforms.

-  Platform Configuration Register (PCR) is a memory location in the TPM used to store TPM Measurements (hash values generated by the SHA-1 standard hashing algorithm). PCRs are cleared only on TPM reset. UEFI defines 24 PCRs of which the first 16, PCR 0 - PCR 15, are used to store measures created during the UEFI boot process.

-  Root of Trust for Measurement (RTM) is a computing engine capable of making integrity measurements.

-  Core Root of Trust for Measurements (CRTM) is a set of instructions executed when performing RTM.

-  Platform Attestation provides proof of validity of the platform’s integrity measurements. Please see Section [7.6.1 Remote Attestation/openCIT](#7.6.1).

Values stored in a PCR cannot be reset (or forged) as they can only be extended. Whenever a measurement is sent to a TPM, the hash of the concatenation of the current value of the PCR and the new measurement is stored in the PCR. The PCR values are used to encrypt data.  If the proper environment is not loaded which will result in different PCR values, the TPM will be unable to decrypt the data.  
 
<a name="7.6.5.1"></a>
#### 7.6.5.1 Static Root of Trust for Measurement (SRTM)

Static RTM (SRTM) begins with measuring and verifying the integrity of the BIOS firmware. It then measures additional firmware modules, verifies their integrity, and adds each component’s measure to an SRTM value. The final value represents the expected state of boot path loads. SRTM stores results as one or more values stored in PCR storage. In SRTM, the CRTM resets PCRs 0 to 15 only at boot.

Using a Trusted Platform Module (TPM), as a hardware root of trust, measurements of platform components, such as firmware, bootloader, OS kernel, can be securely stored and verified.
Cloud Infrastructure operators should ensure that the TPM support is enabled in the platform firmware, so that platform measurements are correctly recorded during boot time.

A simple process would work as follows;
1. The BIOS CRTM (Bios Boot Block) is executed by the CPU and used to measure the BIOS firmware.
1. The SHA1 hash of the result of the measurement is sent to the TPM.
1. The TPM stores this new result hash by extending the currently stored value.
1. The hash comparisons can validate settings as well as the integrity of the modules.

Cloud Infrastructure operators should ensure that OS kernel measurements can be recorded by using a TPM-aware bootloader (e.g. tboot, see https://sourceforge.net/projects/tboot/ or shim, see https://github.com/rhboot/shim), which can extend the root of trust up to the kernel level.

The validation of the platform measurements can be performed by TPM’s launch control policy (LCP) or through the remote attestation server.

<a name="7.6.5.2"></a>
#### 7.6.5.2 Dynamic Root of Trust for Measurement (DRTM)
In Dynamic Root of Trust for Measurement (DRTM), the RTM for the running environment are stored in PCRs starting with PCR 17. 

If a remote attestation server is used to monitor platform integrity, the operators should ensure that attestation is performed periodically or in a timely manner.
Additionally, platform monitoring can be extended to monitor the integrity of the static file system at run-time by using a TPM aware kernel module, such as Linux IMA (Integrity Measurement Architecture), see https://sourceforge.net/p/linux-ima/wiki/Home, or by using the trust policies (see https://github.com/opencit/opencit/wiki/Open-CIT-3.2-Product-Guide#88-trust-policies) functionality of OpenCIT.

The static file system includes a set of important files and folders which do not change between reboots during the lifecycle of the platform.
This allows the attestation server to detect any tampering with the static file system during the runtime of the platform.

<a name="7.7"></a>
## 7.7 Common security standards

The Cloud Infrastructure Reference Model and the supporting architectures are not only required to optimally support networking functions, but they must be designed with common security principles and standards from inception.  These best practices must be applied at all layers of the infrastructure stack and across all points of interconnections with outside networks, APIs and contact points with the NFV network functions overlaying or interacting with that infrastructure.
Standards organizations with recommendations and best practices, and certifications that need to be taken into consideration include the following examples. However this is by no means an exhaustive list, just some of the more important standards in current use.

* Center for Internet Security - https://www.cisecurity.org/
* Cloud Security Alliance - https://cloudsecurityalliance.org/
* Open Web Application Security Project https://www.owasp.org
* The National Institute of Standards and Technology (NIST) (US Only)
* FedRAMP Certification https://www.fedramp.gov/ (US Only)
* ETSI Cyber Security Technical Committee (TC CYBER) - https://www.etsi.org/committee/cyber
* ETSI Industry Specification Group Network Functions Virtualisation (ISG NFV) - https://www.etsi.org/technologies/nfv
  * ETSI NFV ISG [SEC WG specifications](https://www.etsi.org/standards-search#page=1&search=NFV-SEC&title=0&etsiNumber=1&content=0&version=1&onApproval=0&published=1&historical=0&startDate=1988-01-15&endDate=2020-02-27&harmonized=0&keyword=&TB=&stdType=&frequency=&mandate=&collection=&sort=1)
* ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) - www.iso.org.  The following ISO standards are of particular interest for NFVI
  * ISO/IEC 27002:2013 - ISO/IEC 27001 are the international Standard for best-practice information security management systems (ISMSs)
  * ISO/IEC 27032 - ISO/IEC 27032 is the international Standard focusing explicitly on cybersecurity
  * ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management
  * ISO/IEC 27031 - ISO/IEC 27031 is the international Standard for ICT readiness for business continuity

A good place to start to understand the requirements is to use the widely accepted definitions developed by the OWASP – Open Web Application Security Project.  These include the following core principles:

* Confidentiality – Only allow access to data for which the user is permitted.
* Integrity – Ensure data is not tampered with or altered by unauthorized users.
* Availability – ensure systems and data are available to authorized users when they need it.

Additional Cloud Infrastructure security principles that need to be incorporated:
* Authenticity – The ability to confirm the users are in fact valid users with the correct rights to access the systems or data.

<a name="7.8"></a>
## 7.8 Testing & certification

<a name="7.8.1"></a>
### 7.8.1 Testing demarcation points

It is not enough to just secure all potential points of entry and hope for the best, any Cloud Infrastructure architecture must be able to be tested and validated that it is in fact protected from attack as much as possible. The ability to test the infrastructure for vulnerabilities on a continuous basis is critical for maintaining the highest level of security possible.  Testing needs to be done both from the inside and outside of the systems and networks.  Below is a small sample of some of the testing methodologies and frameworks available.

• OWASP testing guide

• Penetration Testing Execution Standard, PTES

• Technical Guide to Information Security Testing and Assessment, NIST 800-115

• VULCAN, Vulnerability Assessment Framework for Cloud Computing, IEEE 2013

• Penetration Testing Framework, VulnerabilityAssessment.co.uk

• Information Systems Security Assessment Framework (ISSAF)

• Open Source Security Testing Methodology Manual (OSSTMM)

• FedRAMP Penetration Test Guidance (US Only)

• CREST Penetration Testing Guide

Insuring that the security standards and best practices are incorporated into the Cloud Infrastructure and architectures must be a shared responsibility, among the Telecommunications operators interested in building and maintaining the infrastructures in support of their services, the application vendors developing the network services that will be consumed by the operators, and the Cloud Infrastructure vendors creating the infrastructures for their Telecommunications customers.  All of the parties need to incorporate security and testing components, and maintain operational processes and procedures to address any security threats or incidents in an appropriate manner.  Each of the stakeholders need to contribute their part to create effective security for the Cloud Infrastructure.


<a name="7.8.2"></a>
### 7.8.2 Certification requirements

Security certification should encompass the following elements:

* Security test cases executed and test case results.
* Industry standard compliance achieved (NIST, ISO, PCI, FedRAMP Moderate etc.).
* Output and analysis from automated static code review, dynamic tests, and penetration tests with remediation of Medium/High/Critical security issues. Tools used for security testing of software being released must be shared.
* Details on un-remediated low severity security issues must be shared.
* Threat models performed during design phase. Including remediation summary to mitigate threats identified.
* Details on un-remediated low severity security issues.
* Any additional Security and Privacy requirements implemented in the software deliverable beyond the default rules used security analysis tools.
* Resiliency tests run (such as hardware failures or power failure tests)

<a name="7.9"></a>
## 7.9 Consolidated Security Requirements

<a name="7.9.1"></a>
### 7.9.1. System Hardening

|  Ref | Requirement  | Definition/Note  |
|-------|------|-------|
| req.sec.gen.001 | The Platform **must** maintain the specified configuration. |  |
| req.sec.gen.002 | All systems part of Cloud Infrastructure **must** support password hardening as defined in CIS Password Policy Guide https://www.cisecurity.org/white-papers/cis-password-policy-guide. | Hardening: CIS Password Policy Guide |
| req.sec.gen.003 | All servers part of Cloud Infrastructure **must** support a root of trust and secure boot. |  |
| req.sec.gen.004 | The Operating Systems of all the servers part of Cloud Infrastructure **must** be hardened by removing or disabling unnecessary services, applications and network protocols, configuring operating system user authentication, configuring resource controls, installing and configuring additional security controls where needed, and testing the security of the Operating System. | NIST SP 800-123 |
| req.sec.gen.005 | The Platform **must** support Operating System level access control. |   |
| req.sec.gen.006 | The Platform **must** support Secure logging. Logging with root account must be prohibited when root privileges are not required. |   |
| req.sec.gen.007 | All servers part of Cloud Infrastructure **must** be Time synchronized with authenticated Time service. | |
| req.sec.gen.008 | All servers part of Cloud Infrastructure **must** be regularly updated to address security vulnerabilities. |  |
| req.sec.gen.009 | The Platform **must** support Software integrity protection and verification. | |
| req.sec.gen.010 | The Cloud Infrastructure **must** support encrypted storage, for example, block, object and file storage, with access to encryption keys restricted based on a need to know. Controlled Access Based on the Need to Know https://www.cisecurity.org/controls/controlled-access-based-on-the-need-to-know. |   |
| req.sec.gen.011 | The Cloud Infrastructure **should** support Read and Write only storage partitions (write only permission to one or more authorized actors). | |
| req.sec.gen.012 | The Operator **must** ensure that only authorized actors have physical access to the underlying infrastructure. | It is mandatory for a Cloud Infrastructure Operator, but this requirement’s verification goes beyond CNTT testing scope |
| req.sec.gen.013 | The Platform **must** ensure that only authorized actors have logical access to the underlying infrastructure. |  |
| req.sec.gen.014 | All servers part of Cloud Infrastructure **should** support measured boot and an attestation server that monitors the measurements of the servers. |  |
| req.sec.gen.015 | Any change to the Platform must be logged as a security event, and the logged event must include the identity of the entity making the change, the change, the date and the time of the change. |  |

<p align="center"><b>Table 7-1:</b> System hardening requirements</p>

<a name="7.9.2"></a>
###  7.9.2. Platform and Access

|  Ref | Requirement  | Definition/Note  |
|-------|------|-------|
| req.sec.sys.001 | The Platform **must** support authenticated and secure access to API, GUI and command line interfaces. | |
| req.sec.sys.002 | The Platform **must** support Traffic Filtering for workloads (for example, Fire Wall). | |
| req.sec.sys.003 | The Platform **must** support Secure and encrypted communications, and confidentiality and integrity of network traffic.| |
| req.sec.sys.004 | The Cloud Infrastructure **must** support authentication, integrity and confidentiality on all network channels. | A secure channel enables transferring of data that is resistant to overhearing and tampering. |
| req.sec.sys.005 | The Cloud Infrastructure **must** segregate the underlay and overlay networks. | |
| req.sec.sys.006 | The Cloud Infrastructure must be able to utilize the Cloud Infrastructure Manager identity lifecycle management capabilities. | |
| req.sec.sys.007 | The Platform **must** implement controls enforcing separation of duties and privileges, least privilege use and least common mechanism (Role-Based Access Control). | |
| req.sec.sys.008 | The Platform **must** be able to assign the Entities that comprise the tenant networks to different trust domains. | Communication between different trust domains is not allowed, by default.  |
| req.sec.sys.009 | The Platform **must** support creation of Trust Relationships between trust domains. | These maybe uni-directional relationships where the trusting domain trusts anther domain (the “trusted domain”) to authenticate users for them or to allow access to its resources from the trusted domain.  In a bidirectional relationship both domain are “trusting” and “trusted”. |
| req.sec.sys.010 | For two or more domains without existing trust relationships, the Platform **must not** allow the effect of an attack on one domain to impact the other domains either directly or indirectly. | |
| req.sec.sys.011 | The Platform **must not** reuse the same authentication credential (e.g., key-pair) on different Platform components (e.g., on different hosts, or different services). | |
| req.sec.sys.012 | The Platform **must** protect all secrets by using strong encryption techniques, and storing the protected secrets externally from the component. | (e.g., in OpenStack Barbican). |
| req.sec.sys.013 | The Platform **must** provide secrets dynamically as and when needed. | |
| req.sec.sys.014 | The Platform **should** use Linux Security Modules such as SELinux to control access to resources. | |

<p align="center"><b>Table 7-2:</b> Platform and access requirements</p>

<a name="7.9.3"></a>
### 7.9.3. Confidentiality and Integrity

| Ref | Requirement | Definition/Note |
|---|----|----|
| req.sec.ci.001 | The Platform **must** support Confidentiality and Integrity of data at rest and in transit. | |
| req.sec.ci.002 | The Platform **should** support self-encrypting storage devices. | |
| req.sec.ci.003 | The Platform **must** support Confidentiality and Integrity of data related metadata. | |
| req.sec.ci.004 | The Platform **must** support Confidentiality of processes and restrict information sharing with only the process owner (e.g., tenant). | |
| req.sec.ci.005 | The Platform **must** support Confidentiality and Integrity of process-related metadata and restrict information sharing with only the process owner (e.g., tenant). | |
| req.sec.ci.006 | The Platform **must** support Confidentiality and Integrity of workload resource utilization (RAM, CPU, Storage, Network I/O, cache, hardware offload) and restrict information sharing with only the workload owner (e.g., tenant). | |
| req.sec.ci.007 | The Platform **must not** allow Memory Inspection by any actor other than the authorized actors for the Entity to which Memory is assigned (e.g., tenants owning the workload), for Lawful Inspection, and by secure monitoring services. | Admin access must be carefully regulated. |
| req.sec.ci.008 | The Cloud Infrastructure **must** support tenant networks segregation. | |

<p align="center"><b>Table 7-3:</b> Confidentiality and integrity requirements</p>

<a name="7.9.4"></a>
### 7.9.4. Workload Security

| Ref | Requirement | Definition/Note |
|---|----|----|
| req.sec.wl.001 | The Platform **must** support Workload placement policy. | |
| req.sec.wl.002 | The Cloud Infrastructure **must** provide methods to ensure the platform’s trust status and integrity (e.g. remote attestation, Trusted Platform Module). | |
| req.sec.wl.003 | The Platform **must** support secure provisioning of workloads.  | |
| req.sec.wl.004 | The Platform **must** support Location assertion (for mandated in-country or location requirements). | |
| req.sec.wl.005 | The Platform **must** support the separation of production and non-production Workloads. | This requirement’s verification goes beyond CNTT testing scope. |
| req.sec.wl.006 | The Platform **must** support the separation of Workloads based on their categorisation (for example, payment card information, healthcare, etc.). | |
| req.sec.wl.007 | The Operator **should** implement processes and tools to verify VNF authenticity and integrity. |  |

<p align="center"><b>Table 7-4:</b> Workload security requirements</p>

<a name="7.9.5"></a>
### 7.9.5. Image Security

| Ref | Requirement | Definition/Note |
|---|----|----|
| req.sec.img.001 | Images from untrusted sources **must not** be used. | |
| req.sec.img.002 | Images **must** be maintained to be free from known vulnerabilities. |  |
| req.sec.img.003 | Images **must not** be configured to run with privileges higher than the privileges of the actor authorized to run them. |  |
| req.sec.img.004 | Images **must** only be accessible to authorized actors. |  |
| req.sec.img.005 | Image Registries **must** only be accessible to authorized actors. |  |
| req.sec.img.006 | Image Registries **must** only be accessible over secure networks that enforce authentication, integrity and confidentiality. |  |
| req.sec.img.007 | Image registries **must** be clear of vulnerable and out of date versions. |  |

<p align="center"><b>Table 7-5:</b> Image security requirements</p>

<a name="7.9.6"></a>
### 7.9.6. Security LCM

| Ref | Requirement | Definition/Note |
|---|----|----|
| req.sec.lcm.001 | The Platform **must** support Secure Provisioning, Availability, and Deprovisioning (Secure Clean-Up) of workload resources where Secure Clean-Up includes tear-down, defence against virus or other attacks. | Secure clean-up: tear-down, defending against virus or other attacks, or observing of cryptographic or user service data. |
| req.sec.lcm.002 | Operational **must** use management protocols limiting security risk such as SNMPv3, SSH v2, ICMP, NTP, syslog and TLS v1.2 or higher. | |
| req.sec.lcm.003 | The Cloud Operator **must** implement and strictly follow change management processes for Cloud Infrastructure, Cloud Infrastructure Manager and other components of the cloud, and Platform change control on hardware. | |
| req.sec.lcm.004 | The Cloud Operator **should** support automated templated approved changes. | Templated approved changes for automation where available. |
| req.sec.lcm.005 | Platform **must** provide logs and these logs must be regularly monitored for anomalous behaviour. |  |
| req.sec.lcm.006 | The Platform **must** verify the integrity of all Resource management requests. | |
| req.sec.lcm.007 | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with current time information. |  |
| req.sec.lcm.008 | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with relevant DNS information. |  |
| req.sec.lcm.009 |  The Platform **must** be able to update the tag of newly instantiated, suspended, hibernated, migrated and restarted images with relevant geolocation (geographical) information. | |
| req.sec.lcm.010 | The Platform **must** log all changes to geolocation along with the mechanisms and sources of location information (i.e. GPS, IP block, and timing). |  |
| req.sec.lcm.011 | The Platform **must** implement Security life cycle management processes including the proactive update and patching of all deployed Cloud Infrastructure software. | |

<p align="center"><b>Table 7-6:</b> Security LCM requirements</p>

<a name="7.9.7"></a>
### 7.9.7. Monitoring and Security Audit

The Platform is assumed to provide configurable alerting and notification capability and the operator is assumed to have automated systems, policies and procedures to act on alerts and notifications in a timely fashion. In the following the monitoring and logging capabilities can trigger alerts and notifications for appropriate action.

| Ref | Requirement | Definition/Note |
|---|----|---|
| req.sec.mon.001 | Platform **must** provide logs and these logs must be regularly monitored for events of interest. | |
| req.sec.mon.002 | Security logs **must** be time synchronised. |  |
| req.sec.mon.003 | The Platform **must** log all changes to time server source, time, date and time zones. |  |
| req.sec.mon.004 | The Platform **must** secure and protect Audit logs (containing sensitive information) both in-transit and at rest. |  |
| req.sec.mon.005 | The Platform **must** Monitor and Audit various behaviours of connection and login attempts to detect access attacks and potential access attempts and take corrective actions accordingly. | |
| req.sec.mon.006 | The Platform **must** Monitor and Audit operations by authorized account access after login to detect malicious operational activity and take corrective actions. |  |
| req.sec.mon.007 | The Platform **must** Monitor and Audit security parameter configurations for compliance with defined security policies. | |
| req.sec.mon.008 | The Platform **must** Monitor and Audit externally exposed interfaces for illegal access (attacks) and take corrective security hardening measures. | |
| req.sec.mon.009 | The Platform **must** Monitor and Audit service for various attacks (malformed messages, signalling flooding and replaying, etc.) and take corrective actions accordingly. | |
| req.sec.mon.010 | The Platform **must** Monitor and Audit running processes to detect unexpected or unauthorized processes and take corrective actions accordingly. |  |
| req.sec.mon.011 | The Platform **must** Monitor and Audit logs from infrastructure elements and workloads to detected anomalies in the system components and take corrective actions accordingly. | |
| req.sec.mon.012 | The Platform **must** Monitor and Audit Traffic patterns and volumes to prevent malware download attempts. | |
| req.sec.mon.013 | The monitoring system **must not** affect the security (integrity and confidentiality) of the infrastructure, workloads, or the user data (through back door entries). |  |
| req.sec.mon.014 | The Monitoring systems **should not** impact IAAS, PAAS, and SAAS SLAs including availability SLAs. |  |
| req.sec.mon.015 | The Platform **must** ensure that the Monitoring systems are never starved of resources. |  |
| req.sec.mon.016 | The Platform Monitoring components **should** follow security best practices for auditing, including secure logging and tracing. | |
| req.sec.lcm.017 | The Platform **must** audit systems for any missing security patches and take appropriate actions. |  |

<p align="center"><b>Table 7-7:</b> Monitoring and security audit requirements</p>

<a name="7.9.8"></a>
### 7.9.8. Compliance with Standards

| Ref | Requirement | Definition/Note |
|---|----|---|
| req.sec.std.001 | The Cloud Operator **should** comply with Center for Internet Security CIS Controls. | Center for Internet Security - [https://www.cisecurity.org/](https://www.cisecurity.org/) |
| req.sec.std.002 | The Cloud Operator, Platform and Workloads **should** follow the guidance in the CSA Security Guidance for Critical Areas of Focus in Cloud Computing (latest version). | Cloud Security Alliance - [https://cloudsecurityalliance.org/](https://cloudsecurityalliance.org/) |
| req.sec.std.003 | The Platform and Workloads **should** follow the guidance in the OWASP Cheat Sheet Series (OCSS) https://github.com/OWASP/CheatSheetSeries. | Open Web Application Security Project [https://www.owasp.org](https://www.owasp.org) |
| req.sec.std.004 | The Cloud Operator, Platform and Workloads **should** ensure that their code is not vulnerable to the OWASP Top Ten Security Risks [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/). |  |
| req.sec.std.005 | The Cloud Operator, Platform and Workloads **should** strive to improve their maturity on the OWASP Software Maturity Model (SAMM) https://owaspsamm.org/blog/2019/12/20/version2-community-release/. |  |
| req.sec.std.006 | The Cloud Operator, Platform and Workloads **should** utilize the OWASP Web Security Testing Guide https://github.com/OWASP/wstg/tree/master/document. |  |
| req.sec.std.007 | The Cloud Operator, and Platform **should** satisfy the requirements for Information Management Systems specified in ISO/IEC 27001  https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en .| ISO/IEC 27002:2013 - ISO/IEC 27001 is the international Standard for best-practice information security management systems (ISMSs). |
| req.sec.std.008 | The Cloud Operator, and Platform **should** implement the Code of practice for Security Controls specified ISO/IEC 27002:2013 (or latest)  https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en .| |
| req.sec.std.009 | The Cloud Operator, and Platform **should** implement the ISO/IEC 27032:2012 (or latest) Guidelines for Cybersecurity techniques  https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en .| ISO/IEC 27032 - ISO/IEC 27032is the international Standard focusing explicitly on cybersecurity. |
| req.sec.std.010 | The Cloud Operator **should** conform to the ISO/IEC 27035 standard for incidence management. | ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management. |
| req.sec.std.011 | The Cloud Operator **should** conform to the ISO/IEC 27031 standard for business continuity  ISO/IEC 27031 - ISO/IEC 27031 is the international Standard for ICT readiness for business continuity. |  |
| req.sec.std.012 | The Public Cloud Operator **must**, and the Private Cloud Operator **may** be certified to be compliant with the International Standard on Awareness Engagements (ISAE) 3402 (in the US: SSAE 16). | International Standard on Awareness Engagements (ISAE) 3402. US Equivalent: SSAE16. |

<p align="center"><b>Table 7-8:</b> Compliance with standards requirements</p>

<a name="7.10"></a>
## 7.10. Security References

Network Functions Virtualisation (NFV);NFV Security; Problem Statement, ETSI GS NFV-SEC 001 V1.1.1 (2014-10)

Network Functions Virtualisation (NFV);NFV Security; Security and Trust Guidance, ETSI GS NFV-SEC 003 V1.1.1 (2014-12)

Network Functions Virtualisation (NFV) Release 3; Security; Security Management and Monitoring specification, ETSI GS NFV-SEC 013 V3.1.1 (2017-02)

Network Functions Virtualisation (NFV) Release 3; NFV Security; Security Specification for MANO Components and Reference points, ETSI GS NFV-SEC 014 V3.1.1 (2018-04)

Network Functions Virtualisation (NFV) Release 2; Security; VNF Package Security Specification, ETSI GS NFV-SEC 021 V2.6.1 (2019-06)

ETSI Industry Specification Group Network Functions Virtualisation (ISG NFV) - [https://www.etsi.org/committee/1427-nfv](https://www.etsi.org/committee/1427-nfv)

ETSI Cyber Security Technical Committee (TC CYBER) - [https://www.etsi.org/committee/cyber](https://www.etsi.org/committee/cyber)

**NIST Documents**

NIST SP 800-53 Security and Privacy Controls for Federal Information Systems and Organizations https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf

NIST SP 800-53A Assessing Security and Privacy Controls in Federal Information Systems and Organizations: Building Effective Assessment Plans https://www.serdp-estcp.org/content/download/47513/453118/file/NIST%20SP%20800-53A%20Rev%204%202013.pdf

NIST SP 800-63B Digital Identity Guidelines https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf

NIST SP 800-115 Technical Guide to Information Security Testing and Assessment https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf

NIST SP 800-123 Guide to General Server Security https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-123.pdf

NIST SP 800-125 Guide to Security for Full Virtualization Technologies https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-125.pdf

NIST SP 800-125a Security Recommendations for Server-based Hypervisor Platforms https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-125Ar1.pdf

NIST SP 800-125b Secure Virtual Network Configuration for Virtual Machine (VM) Protection https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-125B.pdf

NIST SP 800-137 Information Security Continuous Monitoring for Federal Information Systems and Organizations https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-137.pdf

NIST SP 800-145 The NIST Definition of Cloud Computing https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf

NIST SP 800-190 Application Container Security Guide [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)
