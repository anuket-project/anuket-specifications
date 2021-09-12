[<< Back](../../ref_model)
# 7 Security

## Table of Contents
* [7.1 Introduction](#7.1)
* [7.2 Potential attack vectors](#7.2)
* [7.3 Security Scope](#7.3)
  * [7.3.1 In-scope and Out-of-Scope definition](#7.3.1)
  * [7.3.2 High level security requirements](#7.3.2)
  * [7.3.3 Common Security Standards](#7.3.3)
* [7.4 Cloud Infrastructure Security](#7.4)
  * [7.4.1 General Platform Security](#7.4.1)
  * [7.4.2 Platform ‘back-end’ access security](#7.4.2)
  * [7.4.3 Platform ‘front-end’ access security](#7.4.3)
  * [7.4.4 Infrastructure as a Code security](#7.4.4)
* [7.5 Workload Security - Vendor Responsibility](#7.5)
  * [7.5.1 Software Hardening](#7.5.1)
  * [7.5.2 Port Protection](#7.5.2)
  * [7.5.3 Software Code Quality and Security](#7.5.3)
  * [7.5.4 Alerting and Monitoring](#7.5.4)
  * [7.5.5 Logging](#7.5.5)
  * [7.5.6 NF images](#7.5.6)
  * [7.5.7 Vulnerability Management](#7.5.7)
* [7.6 Workload Security- Cloud Infrastructure Operator Responsibility](#7.6)
  * [7.6.1 Remote Attestation/openCIT](#7.6.1)
  * [7.6.2 Workload Image Scanning / Signing](#7.6.2)
  * [7.6.3 Networking Security Zoning](#7.6.3)
  * [7.6.4 Volume Encryption](#7.6.4)
  * [7.6.5 Root of Trust for Measurements (RTM)](#7.6.5)
  * [7.6.6 Zero Trust Architecture (ZTA)](#7.6.6)
* [7.7 Open Source Software Security](#7.7)
* [7.8 Testing & Certification](#7.8)
* [7.9 Consolidated Security requirements](#7.9)
  * [7.9.1 System Hardening](#7.9.1)
  * [7.9.2 Platform Access](#7.9.2)
  * [7.9.3 Confidentiality and Integrity](#7.9.3)
  * [7.9.4 Workload Security](#7.9.4)
  * [7.9.5 Image Security](#7.9.5)
  * [7.9.6 Security LCM](#7.9.6)
  * [7.9.7 Monitoring and Security Audit](#7.9.7)
  * [7.9.8 Open Source Software](#7.9.8)
  * [7.9.9 IaaC - Secure Design and Architecture Stage Requirements](#7.9.9)
  * [7.9.10 IaaC - Secure Code Stage Requirements](#7.9.10)
  * [7.9.11 IaaC - Continuous Build, Integration and Testing Stage Requirements](#7.9.11)
  * [7.9.12 IaaC - Continuous Delivery and Deployment Stage Requirements](#7.9.12)
  * [7.9.13 IaaC - Runtime Defence and Monitoring Requirements](#7.9.13)
  * [7.9.14 Compliance with Standards](#7.9.14)
* [7.10 Security References](#7.10)


<a name="7.1"></a>
## 7.1 Introduction

Security vulnerabilities and attack vectors are everywhere.  The Telecom industry and its cloud infrastructures are even more vulnerable to potential attacks due to the ubiquitous nature of the infrastructures and services combined with the vital role Telecommunications play in the modern world. The attack vectors are many and varied, ranging from the potential for exposure of sensitive data, both personal and corporate, to weaponized disruption to the global telecommunications networks.  The threats can take the form of a physical attack on the locations the infrastructure hardware is housed, to network attacks such as denial of service and targeted corruption of the network service applications themselves.  Whatever the source, any Cloud Infrastructure built needs to be able to withstand attacks in whatever form they take.

This chapter examines multiple aspects of security as it relates to Cloud Infrastructure and security aspects for workloads. After discussing security attack vectors, this chapter delves into security requirements. Regarding security requirements and best practices, specifications and documents are published by standards organizations. A selection of standards of interest for Cloud Infrastructure security is listed in a dedicated section. The chapter culminates with a consolidated set of “must” requirements and desired (should) recommendations; it is suggested that operators carefully evaluate the recommendations for possible implementation.

<a name="7.2"></a>
## 7.2 Potential attack vectors
Previously attacks designed to place and migrate workload outside the legal boundaries were not possible using traditional infrastructure, due to the closed nature of these systems. However, using Cloud Infrastructure, violation of regulatory policies and laws becomes possible by actors diverting or moving an application from an authenticated and legal location to another potentially illegal location. The consequences of violating regulatory policies may take the form of a complete banning of service and/or an exertion of a financial penalty by a governmental agency or through SLA enforcement.  Such vectors of attack may well be the original intention of the attacker in an effort to harm the service provider. One possible attack scenario can be when an attacker exploits the insecure NF API to dump the records of personal data from the database in an attempt to violate user privacy. Cloud Infrastructure operators should ensure that the applications APIs are secure, accessible over a secure network (TLS) under very strict set of security best practices, and RBAC policies to limit exposure of this vulnerability.

Typical cloud associated attacker tactics have been identified in the widely accepted [MITRE ATT&CK® Framework](https://www.mitre.org/sites/default/files/publications/mitre-getting-started-with-attack-october-2019.pdf). This framework provides a systematic approach to capture adversarial tactics targeting cloud environments. Examples of such adversarial tactics are listed in the table below.
 
 |  Attacker tactics | Examples  | 
 |-------|------|
 |Initial Access|Compromising user administration accounts that are not protected by multi-factor authentication|
 |Evasion|Modifying cloud compute instances in the production environment by modifying virtual instances for attack staging|
 |Discovery|Using open-source tools to discover what cloud services are operating and then disabling them in a later stage to avoid detection|
 |Data Exfiltration|Moving data from the compromised tenant’s production databases to the hacker’s cloud service account or transferring the data out of the Communication Service Provider (CSP) to the attacker’s private network|
 |Service Impact|Creating denial-of-service availability issues by modifying Web Application Firewall (WAF) rules and compromising APIs and web-based GUIs|

<p align="center"><b>Table 7-0:</b> Cloud attacker tactics - Examples</p>


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
  
 <a name="7.3.3"></a> 
 ### 7.3.3 Common Security Standards

The Cloud Infrastructure Reference Model and the supporting architectures are not only required to optimally support networking functions, but they must be designed with common security principles and standards from inception.  These best practices must be applied at all layers of the infrastructure stack and across all points of interconnections (internal or with outside networks), APIs and contact points with the NFV network functions overlaying or interacting with that infrastructure.
Standards organizations with recommendations and best practices, and certifications that need to be taken into consideration include the following examples. However this is by no means an exhaustive list, just some of the more important standards in current use.

* Center for Internet Security - https://www.cisecurity.org/
* Cloud Security Alliance - https://cloudsecurityalliance.org/
* Open Web Application Security Project https://www.owasp.org
* The National Institute of Standards and Technology (NIST)
* FedRAMP Certification https://www.fedramp.gov/ 
* ETSI Cyber Security Technical Committee (TC CYBER) - https://www.etsi.org/committee/cyber
* ETSI Industry Specification Group Network Functions Virtualisation (ISG NFV) - https://www.etsi.org/technologies/nfv
* ETSI ISG NFV [SEC WG specifications](https://www.etsi.org/standards-search#page=1&search=NFV-SEC&title=0&etsiNumber=1&content=0&version=1&onApproval=0&published=1&historical=0&startDate=1988-01-15&endDate=2020-02-27&harmonized=0&keyword=&TB=&stdType=&frequency=&mandate=&collection=&sort=1)
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

In mobile network field, the GSM Association ([GSMA](https://www.gsma.com/)) and its Fraud and Security working group of experts have developed a set of documents specifying how to secure the global mobile ecosystem. 
* The document “Baseline Security controls”, [FS.31 v2.0](https://www.gsma.com/security/resources/fs-31-gsma-baseline-security-controls/)[20], published in February 2020, is a practical guide intended for operators and stakeholders to check mobile network’s internal security. It lists a set of security controls from business controls (including security roles, organizational policies, business continuity management…) to technological controls (for user equipment, networks, operations…) covering all areas of mobile network, including Cloud Infrastructure. A checklist of questions allows to improve the security of a deployed network. 

The GSMA security activities are currently focussed around 5G services and the new challenges posed by network functions virtualisation and open source software. The 2 following documents are in the scope of Cloud Infrastructure security:
* The white paper [“Open Networking & the Security of Open Source Software deployment”](https://www.gsma.com/futurenetworks/resources/open-networking-the-security-of-open-source-software-deployment/), published in January 2021 [21], deals with open source software security, it highlights the importance of layered security defences and lists recommendations and security concepts able to secure deployments. 
* The “5G Security Guide”, FS.40 version 1.0, Sept. 2020 (GSMA members only) covers 5G security, in a holistic way, from user equipment to networks. The document describes the new security features in 5G. It includes a dedicated section on the impact of Cloud on 5G security with recommendations on virtualization, cloud native applications and containerization security.  

<a name="7.4"></a>
## 7.4 Cloud Infrastructure Security

<a name="7.4.1"></a>
### 7.4.1 General Platform Security

The security certification of the platform will typically need to be the same, or higher, than the workload requirements.

The platform supports the workload, and in effect controls access to the workload from and to external endpoints such as carriage networks used by workloads, or by Data Centre Operations staff supporting the workload, or by tenants accessing workloads. From an access security perspective, the following diagram shows where different access controls will operate within the platform to provide access controls throughout the platform:

<p align="center"><img src="../figures/ch7-data-access-model.png" alt="Overview" title="Access Controls" width="100%"/></p>
<p align="center"><b>Figure 7-2:</b> Reference Model Access Controls</p>

<a name="7.4.1.1"></a>
#### 7.4.1.1 The high-level functions of these different access controls

* **MGNT ACCESS CONTROLS** - Platform access to workloads for service management. Typically all management and control-plane traffic is encrypted.
* **DATA ACCESS CONTROLS** - Control of east-west traffic between workloads, and control of north-south traffic between the NF and other platform services such as front-end carriage networks and platform services. Inherently strong separation between tenants is mandatory.
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
* The front-end network may provide (Distributed Denial Of Service) DDoS support.

<a name="7.4.4"></a>
### 7.4.4 Infrastructure as a Code security
Infrastructure as a Code (IaaC) (or equivalently called Infrastructure as Code IaC) refers to the software used for the declarative management of cloud infrastructure resources. In order to dynamically address user requirements, release features incrementally, and deliver at a faster pace, DevSecOps teams utilize best practices including continuous integration and continuous delivery and integrate information security controls and scanning tools into these processes, with the aim of providing timely and meaningful feedback including identifying vulnerabilities and security policy violations. With  this automated security testing and analysis capabilities it will be of critical value to detecting vulnerabilities early and maintaining a consistent security policy.

Because of the extremely high complexity of modern telco cloud infrastructures, even minor IaaC code changes may lead to disproportionate and sometime disastrous downstream security and privacy impacts. Therefore, integration of security testing into the IaaC software development pipeline requires security activities to be automated using security tools and integrated  with the native DevOps and DevSecOps tools and procedures.

The DevSecOps Automation best practice advocates implementing a framework for security automation and programmatic execution and monitoring of security controls to identify, protect, detect, respond, and recover from cyber threats.  The framework used for the IaaC security is based on, the joint publication of Cloud Security Alliance (CSA) and SAFECode, "[The Six Pillars of DevSecOps: Automation (2020)](https://safecode.org/the-six-pillars-of-devsecops-automation)" [22]. The document utilises the base definitions and constructs from [ISO 27000](https://www.iso.org/standard/73906.html) [23], and CSA's [Information Security Management through Reflexive Security](https://cloudsecurityalliance.org/artifacts/information-security-management-through-reflexive-security/) [24].

The framework identifies the following five distinct stages: 
1.	Secure design and architecture 
2.	Secure coding (Developer IDE and Code Repository) 
3.	Continuous build, integration and test 
4.	Continuous delivery and deployment 
5.	Continuous monitoring and runtime defence

Triggers and checkpoints define transitions within stages. When designing DevSecOps security processes, one needs to keep in mind, that when a trigger condition is met, one or more security activities are activated. The outcomes of those security activities need to determine whether the requirements of the process checkpoint are satisfied. If the outcome of the security activities meets the requirements, the next set of security activities are performed as the process transitions to the next checkpoint, or, alternatively, to the next stage if the checkpoint is the last one in the current stage. If, on the other hand, the outcome of the security activities does not meet the requirements, then the process should not be allowed to advance to the next checkpoint. Tables 7-9 to 7-13 in Section 7.9 define the IaaC security activities presented as security requirements mapped to particular stages and trigger points.

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
### 7.5.6 NF images

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

It is easy to tamper with workload images. It requires only a few seconds to insert some malware into a workload image file while it is being uploaded to an image database or being transferred from an image database to a compute node. To guard against this possibility, workload images can be cryptographically signed and verified during launch time. This can be achieved by setting up a signing authority and modifying the hypervisor configuration to verify an image’s signature before they are launched. To implement image security, the workload operator must test the image and supplementary components verifying that everything conforms to security policies and best practices.

Use of Image scanners such as OpenSCAP to determine security vulnerabilities is strongly recommended.

<a name="7.6.3"></a>
### 7.6.3 Networking Security Zoning

Network segmentation is important to ensure that applications can only communicate with the applications they are supposed to. To prevent a workload from impacting other workloads or hosts, it is a good practice to separate workload traffic and management traffic. This will prevent attacks by VMs or containers breaking into the management infrastructure. It is also best to separate the VLAN traffic into appropriate groups and disable all other VLANs that are not in use. Likewise, workloads of similar functionalities can be grouped into specific zones and their traffic isolated. Each zone can be protected using access control policies and a dedicated firewall based on the needed security level.

Recommended practice to set network security policies following the principle of least privileged, only allowing approved protocol flows. For example, set 'default deny' inbound and add approved policies required for the functionality of the application running on the NFV Infrastructure.

<a name="7.6.4"></a>
### 7.6.4 Volume Encryption

Virtual volume disks associated with workloads may contain sensitive data. Therefore, they need to be protected. Best practice is to secure the workload volumes by encrypting them and storing the cryptographic keys at safe locations. Encryption functions rely on a Cloud Infrastructure internal key management service. Be aware that the decision to encrypt the volumes might cause reduced performance, so the decision to encrypt needs to be dependent on the requirements of the given infrastructure. The TPM module can also be used to securely store these keys. In addition, the hypervisor should be configured to securely erase the virtual volume disks in the event of application crashes or is intentionally destroyed to prevent it from unauthorized access.

For sensitive data encryption, when data sovereignty is required, an external Hardware Security Module (HSM) should be integrated in order to protect the cryptographic keys. A HSM is a physical device which manages and stores secrets. Usage of a HSM strengthens the secrets security. For 5G services, GSMA FASG strongly recommends the implementation of a HSM to secure the storage of UICC (Universal Integrated Circuit Card) credentials.

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

<a name="7.6.6"></a>
### 7.6.6 Zero Trust Architecture (ZTA) 

Remote attestation, section [7.6.1](#7.6.1), and Root of trust for measurements, section [7.6.5](#7.6.5), provide methods to ensure the integrity of the infrastructure. The Zero Trust concept moves a step forward enabling to build secure by design cloud infrastructure, from hardware to applications. The adoption of Zero Trust principles mitigates the threats and attacks within an enterprise, a network or an infrastructure, ensuring a fine grained segmentation between each component of the system.

Zero Trust Architecture (ZTA), described in [NIST SP 800-207 publication](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) [25], assumes there is no implicit trust granted to assets or user accounts whatever their location or ownership.  Zero trust approach focuses on protecting all types of resources: data, services, devices, infrastructure components, virtual and cloud components. Trust is never granted implicitly, and must be evaluated continuously. 

ZTA principles applied to Cloud infrastructure components are the following:

-	Adopt least privilege configurations
-	Authentication and authorization required for each entity, service, or session
-	Fine grained segmentation
-	Separation of control plane and data plane
-	Secure internal and external communications
-	Monitor, test, and analyse security continuously

<a name="7.7"></a>
## 7.7 Open Source Software Security 

Software supply chain safety is crucial and can be a complex task in virtualised and containerized environments. Open source code is present in Cloud Infrastructure software from host Operating System to virtualisation layer components, the most obvious being represented by Linux, KVM, QEMU, OpenStack, and Kubernetes. Workloads components can also be composed of open source code. The proportion of open source code to an application source code can vary. It can be partial or total, visible or not. Open source code can be upstream code coming directly from open source public repositories or code within a commercial application or network function. To ensure the security of the whole system, all software and hardware components must reach the same level of security by following best security practices including secure lifecycle management. The SAFECode paper “Managing Security Risks Inherent in the Use of Third-party Components” provides a detailed risk management approach.

To secure software code, the following methods must be applied:

-	Use best practices coding such as design pattern recommended in the [Twelve-Factor App](https://12factor.net/) or [OWASP “Secure Coding Practices - Quick Reference Guide”](owasp.org)
-	Require suppliers to provide a Software Bill of Materials to identify the open source modules in their product’s software releases
-	Use trusted, authenticated and identified software images that are provided by authenticated software distribution portals  
-	Do threat modelling, as described in the document “Tactical Threat Modeling” published by SAFECode
-	Test the software in a pre-production environment to validate integration 
-	Detect vulnerabilities using security tools scanning and CVE (Common Vulnerabilities and Exposures), https://cve.mitre.org/
-	Actively monitor the open source software repositories to determine if new versions have been released that address identified vulnerabilities discovered in the community
-	Actively monitor the open source software repositories to determine if new versions have been released that address identified vulnerabilities discovered in the community
-	Report and remove vulnerabilities by upgrading components using authenticated software update distribution portals
-	Adopt a DevSecOps approach and rely on testing automation throughout the software build, integration, delivery, deployment, and runtime operation to perform automatic security check, as described in section 7.4.4  ‘”Infrastructure as a Code Security”

The strength of open source code is the availability of code source developed by a community which maintain and improve it. Open source code integration with application source code helps to develop and produce applications faster. But, in return, it can introduce security risks if a risk management DevSecOps approach is not implemented. The GSMA white paper, “Open Networking & the Security of Open Source Software Deployment - Future Networks”, alerts on these risks and addresses the challenges coming with open source code usage. Amongst these risks for security, we can mention a poor quality code containing security flaws, an obsolete code with known vulnerabilities, and the lack of knowledge of open source communities’ branches activity. An active branch will come with bugs fixes, it will not be the case with an inactive branch. The GSMA white paper develops means to mitigate these security issues.

**SBOM**

To begin, it is highly recommended to identify the software components and their origins. The Software Bill of Materials (SBOM), described by [US NTIA](https://www.ntia.gov/SBOM)(National Telecommunications and Information Administration), is an efficient tool to identify software components. The SBOM is an inventory of software components and the relationships between them. NTIA describes how to establish an SBOM and provides SBOM standard data formats. In case of vulnerability detected for a component, the SBOM inventory is an effective means to identify the impacted component and provide remediation.

**Code inspection**

Poor code quality is a factor of risk. Open source code advantage is its transparency, code can be inspected by tools with various capabilities such as open source software discovery and static and dynamic code analysis.

**Vulnerability identification**

Vulnerability management must be continuous: from development to runtime, not only on the development process, but during all the life of the application or workload or service. When a public vulnerability on a component is released, the update of the component must be triggered. When an SBOM recording the code composition is provided, the affected components will be easier to identify. It is essential to remediate the affected components as soon as possible, because code transparency can also be exploited by attackers who can take the benefit of vulnerabilities.

The CVE must be used to identify vulnerabilities and their severity rating. CVE identifies, defines, and catalogues publicly disclosed cybersecurity vulnerabilities.

Various images scanning tools, such as Clair or Trivy, are useful to audit images from security vulnerabilities. The results of vulnerabilities scan audit must be analysed carefully when it is applied to vendor offering packaged solutions; as patches are not detected by scanning tools, some components can be detected as obsolete. 

**Trusted repositories**

A dedicated internal isolated repository separated from the production environment must be used to store vetted open source content, which can include images, but also installer and utilities. These software packages must be signed and the signature verified prior to packages or images installation. Access to the repository must be granted by a dedicated authorization. The code must be inspected and vulnerabilities identified as described previously. After validating the software is risk free, it can be moved to the appropriate production repository.


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
| req.sec.gen.009 | The Platform **must** support Software integrity protection and verification and **must** scan source code and manifests. | |
| req.sec.gen.010 | The Cloud Infrastructure **must** support encrypted storage, for example, block, object and file storage, with access to encryption keys restricted based on a need to know. Controlled Access Based on the Need to Know https://www.cisecurity.org/controls/controlled-access-based-on-the-need-to-know. |   |
| req.sec.gen.011 | The Cloud Infrastructure **should** support Read and Write only storage partitions (write only permission to one or more authorized actors). | |
| req.sec.gen.012 | The Operator **must** ensure that only authorized actors have physical access to the underlying infrastructure. | It is mandatory for a Cloud Infrastructure Operator, but this requirement’s verification is out of scope |
| req.sec.gen.013 | The Platform **must** ensure that only authorized actors have logical access to the underlying infrastructure. |  |
| req.sec.gen.014 | All servers part of Cloud Infrastructure **should** support measured boot and an attestation server that monitors the measurements of the servers. |  |
| req.sec.gen.015 | Any change to the Platform **must** be logged as a security event, and the logged event must include the identity of the entity making the change, the change, the date and the time of the change. |  |

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
| req.sec.sys.015 | The Platform **must not** contain back door entries (unpublished access points, APIs, etc.). |  |
| req.sec.sys.016 | Login access to the platform's components **must** be through encrypted protocols such as SSH v2 or TLS v1.2 or higher. | Note: Hardened jump servers isolated from external networks are recommended |
| req.sec.sys.017 | The Platform **must** provide the capability of using digital certificates that comply with X.509 standards issued by a trusted Certification Authority. |  |
| req.sec.sys.018 | The Platform **must** provide the capability of allowing certificate renewal and revocation. |  |
| req.sec.sys.019 | The Platform **must** provide the capability of testing the validity of a digital certificate (CA signature, validity period, non-revocation, identity). |  |
| req.sec.sys.020 | The Cloud Infrastructure architecture **should** rely on Zero Trust principles to build a secure by design environment. | Zero Trust Architecture (ZTA) described in NIST SP 800-207 |

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
| req.sec.ci.009 | For sensitive data encryption, the key management service **should** leverage a Hardware Security Module to manage and protect cryptographic keys. | |

<p align="center"><b>Table 7-3:</b> Confidentiality and integrity requirements</p>

<a name="7.9.4"></a>
### 7.9.4. Workload Security

| Ref | Requirement | Definition/Note |
|---|----|----|
| req.sec.wl.001 | The Platform **must** support Workload placement policy. | |
| req.sec.wl.002 | The Cloud Infrastructure **must** provide methods to ensure the platform’s trust status and integrity (e.g. remote attestation, Trusted Platform Module). | |
| req.sec.wl.003 | The Platform **must** support secure provisioning of workloads.  | |
| req.sec.wl.004 | The Platform **must** support Location assertion (for mandated in-country or location requirements). | |
| req.sec.wl.005 | The Platform **must** support the separation of production and non-production Workloads. | This requirement’s verification is out of scope. |
| req.sec.wl.006 | The Platform **must** support the separation of Workloads based on their categorisation (for example, payment card information, healthcare, etc.). | |
| req.sec.wl.007 | The Operator **should** implement processes and tools to verify NF authenticity and integrity. |  |

<p align="center"><b>Table 7-4:</b> Workload security requirements</p>

<a name="7.9.5"></a>
### 7.9.5. Image Security

| Ref | Requirement | Definition/Note |
|---|----|----|
| req.sec.img.001 | Images from untrusted sources **must not** be used. | |
| req.sec.img.002 | Images **must** be scanned to be maintained free from known vulnerabilities. |  |
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
| req.sec.lcm.002 | Cloud operations staff and systems **must** use management protocols limiting security risk such as SNMPv3, SSH v2, ICMP, NTP, syslog and TLS v1.2 or higher. | |
| req.sec.lcm.003 | The Cloud Operator **must** implement and strictly follow change management processes for Cloud Infrastructure, Cloud Infrastructure Manager and other components of the cloud, and Platform change control on hardware. | |
| req.sec.lcm.004 | The Cloud Operator **should** support automated templated approved changes. | Templated approved changes for automation where available. |
| req.sec.lcm.005 | Platform **must** provide logs and these logs must be regularly monitored for anomalous behaviour. |  |
| req.sec.lcm.006 | The Platform **must** verify the integrity of all Resource management requests. | |
| req.sec.lcm.007 | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with current time information. |  |
| req.sec.lcm.008 | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with relevant DNS information. |  |
| req.sec.lcm.009 |  The Platform **must** be able to update the tag of newly instantiated, suspended, hibernated, migrated and restarted images with relevant geolocation (geographical) information. | |
| req.sec.lcm.010 | The Platform **must** log all changes to geolocation along with the mechanisms and sources of location information (i.e. GPS, IP block, and timing). |  |
| req.sec.lcm.011 | The Platform **must** implement Security life cycle management processes including the proactive update and patching of all deployed Cloud Infrastructure software. | |
| req.sec.lcm.012 | The Platform **must** log any access privilege escalation. |  |

<p align="center"><b>Table 7-6:</b> Security LCM requirements</p>

<a name="7.9.7"></a>
### 7.9.7. Monitoring and Security Audit

The Platform is assumed to provide configurable alerting and notification capability and the operator is assumed to have automated systems, policies and procedures to act on alerts and notifications in a timely fashion. In the following the monitoring and logging capabilities can trigger alerts and notifications for appropriate action.

| Ref | Requirement | Definition/Note |
|---|----|---|
| req.sec.mon.001 | Platform **must** provide logs and these logs must be regularly monitored for events of interest. The logs **must** contain the following fields: event type, date/time, protocol, service or program used for access, success/failure, login ID or process ID, IP address and ports (source and destination) involved. | |
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
| req.sec.mon.015 | The Platform **must** ensure that the Monitoring systems are never starved of resources and **must** activate alarms when resource utilisation exceeds a configurable threshold. |  |
| req.sec.mon.016 | The Platform Monitoring components **should** follow security best practices for auditing, including secure logging and tracing. | |
| req.sec.mon.017 | The Platform **must** audit systems for any missing security patches and take appropriate actions. |  |
| req.sec.mon.018 | The Platform, starting from initialization, **must** collect and analyse logs to identify security events, and store these events in an external system. | |
| req.sec.mon.019 | The Platform’s components **must not** include an authentication credential, e.g., password, in any logs, even if encrypted. | | 
| req.sec.mon.020 | The Platform’s logging system **must** support the storage of security audit logs for a configurable period of time. | |
| req.sec.mon.021 | The Platform **must** store security events locally if the external logging system is unavailable and shall periodically attempt to send these to the external logging system until successful.. | |

<p align="center"><b>Table 7-7:</b> Monitoring and security audit requirements</p>

<a name="7.9.8"></a>
### 7.9.8. Open Source Software 

| Ref | Requirement | Definition/Note |
|---|----|----|
| req.sec.oss.001 | Open source code **must** be inspected by tools with various capabilities for static and dynamic code analysis. |  |
| req.sec.oss.002 | The CVE(Common Vulnerabilities and Exposures) **must** be used to identify vulnerabilities and their severity rating for open source code part of Cloud Infrastructure and workloads software.  | https://cve.mitre.org/ |
| req.sec.oss.003 | A dedicated internal isolated repository separated from the production environment **must** be used to store vetted open source content. |  |
| req.sec.oss.004 | A Software Bill of Materials (SBOM) **should** be provided or build, and maintained to identify the software components and their origins. | Inventory of software components, https://www.ntia.gov/SBOM. | 

<p align="center"><b>Table 7-8:</b> Open Source Software requirements</p>

<a name="7.9.9"></a>
### 7.9.9. IaaC - Secure Design and Architecture Stage Requirements


| Ref | Requirement | Definition/Note |
|---|----|---|
| req.sec.arch.001 | Threat Modelling methodologies and tools **should** be used during the Secure Design and Architecture stage triggered by Software Feature Design trigger | Methodology to identify and understand threats impacting a resource or set of resources. It may be done manually or using tools like open source OWASP Threat Dragon |
| req.sec.arch.002 | Security Control Baseline Assessment **should** be performed during the Secure Design and Architecture stage triggered by Software Feature Design trigger | Typically done manually by internal or independent assessors.  |

<p align="center"><b>Table 7-9:</b> IaaC - Secure Design and Architecture Stage Requirements</p>

<a name="7.9.10"></a>
### 7.9.10. IaaC - Secure Code Stage Requirements


| Ref | Requirement | Definition/Note |
|---|----|---|
| req.sec.code.001 | SAST -Static Application Security Testing **must** be applied during Secure Coding stage triggered by Pull, Clone or Comment trigger. | Security testing that analyses application source code for software vulnerabilities and gaps against best practices. Example: open source OWASP range of tools.|
| req.sec.code.002 | SCA – Software Composition Analysis **should** be applied during Secure Coding stage triggered by Pull, Clone or Comment trigger. | Security testing that analyses application source code or compiled code for software components with known vulnerabilities. Example: open source OWASP range of tools.  |
| req.sec.code.003 | Source Code Review **should** be performed continuously during Secure Coding stage. | Typically done manually.  |
| req.sec.code.004 | Integrated SAST via IDE Plugins **should** be used during Secure Coding stage triggered by Developer Code trigger. | On the local machine: through the IDE or integrated test suites; triggered on completion of coding be developer. |
| req.sec.code.005 | SAST of Source Code Repo **should** be performed during Secure Coding stage triggered by Developer Code trigger. | Continuous delivery pre-deployment: scanning prior to deployment. |

<p align="center"><b>Table 7-10:</b> IaaC - Secure Code Stage Requirements</p>

<a name="7.9.11"></a>
### 7.9.11. IaaC - Continuous Build, Integration and Testing Stage Requirements


| Ref | Requirement | Definition/Note |
|---|----|---|
| req.sec.bld.001 | SAST -Static Application Security Testing **should** be applied during the Continuous Build, Integration and Testing stage triggered by Build and Integrate trigger. | Example: open source OWASP range of tools.|
| req.sec.bld.002 | SCA – Software Composition Analysis **should** be applied during the Continuous Build, Integration and Testing stage triggered by Build and Integrate trigger. | Example: open source OWASP range of tools.  |
| req.sec.bld.003 | Container and Image Scan **must** be applied during the Continuous Build, Integration and Testing stage triggered by Package trigger. | Example: A push of a container image to a container registry may trigger a vulnerability scan before the image becomes available in the registry.  |
| req.sec.bld.004 | DAST – Dynamic Application Security Testing **should** be applied during the Continuous Build, Integration and Testing stage triggered by Stage & Test trigger. | Security testing that analyses a running application by exercising application functionality and detecting vulnerabilities based on application behaviour and response. Example: OWASP ZAP. |
| req.sec.bld.005 | Fuzzing **should** be applied during the Continuous Build, Integration and testing stage triggered by Stage & Test trigger. | Fuzzing or fuzz testing is an automated software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program. Example: GitLab Open Sources Protocol Fuzzer Community Edition. |
| req.sec.bld.006 | IAST – Interactive Application Security Testing **should** be applied during the Continuous Build, Integration and Testing stage triggered by Stage & Test trigger. | Software component deployed with an application that assesses application behaviour and detects presence of vulnerabilities on an application being exercised in realistic testing scenarios. Example:  Contrast Community Edition. |

<p align="center"><b>Table 7-11:</b> IaaC - Continuous Build, Integration and Testing Stage Requirements</p>

<a name="7.9.12"></a>
### 7.9.12. IaaC - Continuous Delivery and Deployment Stage Requirements


| Ref | Requirement | Definition/Note |
|---|----|---|
| req.sec.del.001 | Image Scan **must** be applied during the Continuous Delivery and Deployment stage triggered by Publish to Artifact and Image Repository trigger. | Example: GitLab uses the open source Clair engine for container scanning.|
| req.sec.del.002 | Code Signing **must** be applied during the Continuous Delivery and Deployment stage triggered by Publish to Artifact and Image Repository trigger. | Code Signing provides authentication to assure that downloaded files are form the publisher named on the certificate.  |
| req.sec.del.003 | Artifact and Image Repository Scan **should** be continuously applied during the Continuous Delivery and Deployment stage. | Example: GitLab uses the open source Clair engine for container scanning.  |
| req.sec.del.004 | Component Vulnerability Scan **must** be applied during the Continuous Delivery and Deployment stage triggered by Instantiate Infrastructure trigger. | The vulnerability scanning system is deployed on the cloud platform to detect security vulnerabilities of specified components through scanning and to provide timely security protection. Example: OWASP Zed Attack Proxy (ZAP). |

<p align="center"><b>Table 7-12:</b> IaaC - Continuous Delivery and Deployment Stage Requirements</p>

<a name="7.9.13"></a>
### 7.9.13. IaaC - Runtime Defence and Monitoring Requirements


| Ref | Requirement | Definition/Note |
|---|----|---|
| req.sec.run.001 | Component Vulnerability Monitoring **must** be continuously applied during the Runtime Defence and Monitoring stage. | Security technology that monitors components like virtual servers and assesses data, applications, and infrastructure for security risks.|
| req.sec.run.002 | RASP – Runtime Application Self-Protection **should** be continuously applied during the Runtime Defence and Monitoring stage. | Security technology deployed within the target application in production for detecting, alerting, and blocking attacks.  |
| req.sec.run.003 | Application testing and Fuzzing **should** be continuously applied during the Runtime Defence and Monitoring stage. | Fuzzing or fuzz testing is an automated software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program. Example: GitLab Open Sources Protocol Fuzzer Community Edition.  |
| req.sec.run.004 | Penetration Testing **should** be continuously applied during the Runtime Defence and Monitoring stage. | Typically done manually. |

<p align="center"><b>Table 7-13:</b> IaaC - Runtime Defence and Monitoring Requirements</p>

<a name="7.9.14"></a>
### 7.9.14. Compliance with Standards

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

<p align="center"><b>Table 7-14:</b> Compliance with standards requirements</p>


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
