[<< Back](../../ref_model)
# 7 Security
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [7.1 Introduction](#7.1)
* [7.2 Principles and Guidelines](#7.2)
  * [7.2.1 Overarching Objectives and Goals](#7.2.1)
  * [7.2.2 Verification Methodologies](#7.2.2)
  * [7.2.3 Governance](#7.2.3)
* [7.3 Common standards](#7.3)
  * [7.3.1 Potential attack vectors](#7.3.1)
  * [7.3.2 Testing demarcation points](#7.3.2)
* [7.4 Security Scope](#7.4)
  * [7.4.1 In-scope and Out-of-Scope definition](#7.4.1)
  * [7.4.2 Security requirements](#7.4.2)
  * [7.4.3 Platform security requirements](#7.4.3)
  * [7.4.4 Workload security requirements](#7.4.4)
  * [7.4.5 Certification/validation requirements](#7.4.5)
* [7.5 Platform Security](#7.5)
  * [7.5.1 General Platform Security](#7.5.1)
  * [7.5.2 Platform ‘back-end’ access security](#7.5.2)
  * [7.5.3 Platform ‘front-end’ access security](#7.5.3)
* [7.6 Workload Security](#7.6)
* [7.7 Vendor Responsibilities](#7.7)
  * [7.7.1 Software Hardening](#7.7.1)
  * [7.7.2 Port Protection](#7.7.2)
  * [7.7.3 Software Code Quality](#7.7.3)
  * [7.7.4 Alerting and Monitoring](#7.7.4)
  * [7.7.5 Logging](#7.7.5)
  * [7.7.6 VNF images](#7.7.6)
  * [7.7.7 Identity and Access Management](#7.7.7)
  * [7.7.8 CVEs and Vulnerability Management](#7.7.8)
  * [7.7.9 Encryption suite supports](#7.7.9)
  * [7.7.10 Password complexity support](#7.7.10)
  * [7.7.11 Customized Banner](#7.7.11)
 * [7.8 Operator responsibility](#7.8)
  * [7.8.1 Remote Attestation/openCIT](#7.8.1)
  * [7.8.2 VNF Image Scanning / Signing](#7.8.2)
* [7.9 VNF Vendors responsibility](#7.9)
* [7.10 NFVI Vendors responsibility](#7.10)
  * [7.10.1 Networking Security Zoning](#7.10.1)
  * [7.10.2 Encryption](#7.10.2)
  * [7.10.3 Platform Patching](#7.10.3)
  * [7.10.4 Boot Integrity Measurement (TPM)](#7.10.4)
  * [7.10.5 Runtime Integrity Measurement (TPM)](#7.10.5)
  * [7.10.6 NFVI & VIM](#7.10.6)
* [7.11 Certification requirements](#7.11)

<a name="7.1"></a>
## 7.1 Introduction

This document includes process flow, logistics, and requirements which must be satisfied to ensure Virtualized Network Functions (VNFs) meet the design, feature, and capability expectations of VNF consumers to deliver NFV promoting the use and scalability of SDN capabilities. This chapter captures the core fundamentals and steps needed to certify VNFs on target NFVi frameworks and architectures which drives more work into the community, resulting in pre-certified VNFs on core capabilities ultimately reducing the amount of time and cost it takes each operator to on-board and maintain vendor provided VNFs.

<p align="center"><img src="../figures/ch10_ref_model_lfn.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 8-1:</b> CNTT relation to LFN OVP</p>

<a name="7.2"></a>
## 7.2 Principles and Guidelines

The objectives of the Security verification program are to deliver certified reference architectures which match VNF-developer specifications, levering the OVP ecosystem as the vehicle for deliverying security validated NFV.

These core principles will guide NFV verification deliverables

<a name="7.2.1"></a>
### 7.2.1 Overarching Objectives and Goals

1. Deliver security certified reference architecture which matches VNF-developer specifications<br>
2. All accomplished with augmentation to the current OVP ecosystem.<br>
3. Certified VNFs will on-board and function first shot<br>

<a name="7.2.2"></a>
### 7.2.2 Verification Methodologies
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<a name="7.2.3"></a>
### 7.2.3 Governance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<a name="7.3"></a>
## 7.3 Common standards

Security vulnerabilities and attack vectors are everywhere.  The telecom industry and its cloud infrastructures are even more vulnerable to potential attacks due to the ubiquitous nature of the infrastructures and services combined with the vital role Telecommunications play in the modern world.   The attack vectors are many and varied, ranging from the potential for exposure of sensitive data, both personal and corporate, to weaponized disruption to the global Telecommunications networks.  The threats can take the form of a physical attack on the locations the infrastructure hardware is housed, to network attacks such as denial of service and targeted corruption of the network service applications themselves.  Whatever the source, any NFVI infrastructure built needs to be able to withstand attacks in whatever form they take.

With that in mind, the NFVI reference model and the supporting architectures are not only required to optimally support networking functions, but they must be designed with common security principles and standards from inception.  These best practices must be applied at all layers of the infrastructure stack and across all points of interconnections with outside networks, APIs and contact points with the NFV network functions overlaying or interacting with that infrastructure.
Standards organizations with recommendations and best practices, and certifications that need to be taken into consideration include the following examples. However this is by no means an exhaustive list, just some of the more important standards in current use.

 • Center for Internet Security - https://www.cisecurity.org/

 • Cloud Security Alliance - https://cloudsecurityalliance.org/

 • Open Web Application Security Project https://www.owasp.org

 • The National Institute of Standards and Technology (NIST) (US Only)

 • FedRAMP Certification https://www.fedramp.gov/ (US Only)

 • ETSI Cyber Security Technical Committee (TC CYBER) - https://www.etsi.org/committee/cyber

 • ETSI Industry Specification Group Network Functions Virtualisation (ISG NFV) - https://www.etsi.org/committee/1427-nfv

• ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) - www.iso.org.  The following ISO standards are of particular interest for NFVI

    o ISO/IEC 27002:2013 - ISO/IEC 27001 is the international Standard for best-practice information security management systems (ISMSs).

    o ISO/IEC 27032 - ISO/IEC 27032is the international Standard focusing explicitly on cybersecurity.

    o ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management. Incident management

    o ISO/IEC 27031 - ISO/IEC 27031 is the international Standard for ICT readiness for business continuity.

A good place to start to understand the requirements is to use the widely accepted definitions developed by the OWASP – Open Web Application Security Project.  These include the following core principles:

• Confidentiality – Only allow access to data for which the user is permitted

• Integrity – Ensure data is not tampered with or altered by unauthorized users

• Availability – ensure systems and data are available to authorized users when they need it

Additional NFVI security principles that need to be incorporated:

• Authenticity – The ability to confirm the users are in fact valid users with the correct rights to access the systems or data.

<a name="7.3.1"></a>
## 7.3.1 Potential attack vectors.
Previously attacks designed to place and migrate workload outside the legal boundaries were not possible using traditional infrastructure, due to the closed nature of these systems. However, using NFVI, violation of regulatory policies and laws becomes possible by actors diverting or moving a VNF from an authenticated and legal location to another potentially illegal location. The consequences of violating regulatory policies may take the form of a complete banning of service and/or an exertion of a financial penalty by a governmental agency or through SLA enforcement.  Such vectors of attack may well be the original intention of the attacker in an effort to harm the service provider. One possible attack scenario can be when an attacker exploits the insecure VNF API to dump the records of personal data from the database in an attempt to violate user privacy. NFVI operators should ensure that VNF APIs are secure, accessible over a secure network (TLS) under very strict set of security best practices and RBAC policies to limit exposure of this vulnerability.

<a name="7.3.2"></a>
## 7.3.2 Testing demarcation points.

It is not enough to just secure all potential points of entry and hope for the best, any NFVI architecture must be able to be tested and validated that it is in fact protected from attack as much as possible. The ability to test the infrastructure for vulnerabilities on a continuous basis is critical for maintaining the highest level of security possible.  Testing needs to be done both from the inside and outside of the systems and networks.  Below is a small sample of some of the testing methodologies and frameworks available.

• OWASP testing guide

• PCI Penetration testing guide

• Penetration Testing Execution Standard

• NIST 800-115

    o VULCAN: Vulnerability Assessment Framework for Cloud Computing (NIST)

• Penetration Testing Framework

• Information Systems Security Assessment Framework (ISSAF)

• Open Source Security Testing Methodology Manual (“OSSTMM”)

• FedRAMP Penetration Test Guidance (US Only)

• CREST Penetration Testing Guide

Insuring that the security standards and best practices are incorporated into the NFVI model and architectures must be a shared responsibility, among the Telecommunications operators interested in building and maintaining the infrastructures in support of their services, the VNF vendors developing the network services that will be consumed by the operators, and the NFVI vendors creating the infrastructures for their Telecommunications customers.  All of the parties need to incorporate security and testing components, and maintain operational processes and procedures to address any security threats or incidents in an appropriate manner.  Each of the stakeholders need to contribute their part to create effective security for NFVI.

<a name="7.4"></a>
## 7.4 Security Scope

<a name="7.4.1"></a>
## 7.4.1 In-scope and Out-of-Scope definition

The scope of the security controls requirements maps to the scope of the Reference Model architecture.

The Reference Model scope is shown below (as outlined in chapter 1 of the reference model):

<p align="center"><img src="../figures/ch01_etsi_archi_mapping_v2.PNG" alt="Scope" title="ETSI Scope" width="100%"/></p>
<p align="center"><b>Figure 7-2:</b> ETSI Mapping</p>

This means that the security of the Reference Model requirements must cover the virtual resources (including the virtualisation layer), the hardware resources, and the VIM (Virtualised Infrastructure Manager).

There will be a different set of security requirements for each NFVi reference architecture. In this case, the first reference architecture is OpenStack.

<a name="7.4.2"></a>
## 7.4.2 Security Requirements

The following diagram shows the different security domains that impact the Reference Model:

<p align="center"><img src="../figures/ch7_security_posture.png" alt="Overview" title="Security Domains" width="100%"/></p>
<p align="center"><b>Figure 7-3:</b> Reference Model Security Domains</p>

<a name="7.4.2"></a>
## 7.4.3 Platform security requirements

At a high level, the following areas/requirements cover platform security for a particular deployment:
* Platform certification
* Secure access controls for administrators
* Secure API interface for Tenants
* Encryption for all external and control comms
* Strong separation between tenants - ensuring network, data, and runtime process isolation between tenants
* Authenticated/secure APIs provided to overlay network administrators
* Platform change control on hardware
* Templated approved changes for automation where available
* Typically well defined security framework documentation including approved deployment use cases
* Infrastructure software update process
* Identity Domain = platform

<a name="7.4.3"></a>
## 7.4.4 Workload security requirements

At a high level, the following areas/requirements cover workload security for a particular deployment:
* Up to platform-level certification
* Each workload network will need to undertake it own security self-assessment and accreditation, and not inherit a security accreditation from the platform
* Potentially automated service activation
* Workload owner owns workload security certification process
* Workload owner owns workload design change process
* Workload owner owns workload software update process
* Identity Domain = workload

<a name="7.4.4"></a>
## 7.4.5 Certification/validation requirements

    *(An overview/introduction to workload certification requirements and
    incl types of workloads covered)*

<a name="7.5"></a>
## 7.5 Platform Security

<a name="7.5.1"></a>
### 7.5.1 General Platform Security

The security certification of the platform will typically need to be the same, or higher, than the workload or VNF requirements.

The platform supports the workload, and in effect controls access to the workload from and to external endpoints such as carriage networks used by VNFs, or by Data Centre Operations staff supporting the workload, or by tenants accessing VNFs. From an access security perspective, the following diagram shows where different access controls will operate within the platform to provide access controls throughout the platform:

<p align="center"><img src="../figures/ch7_data_access_model.png" alt="Overview" title="Access Controls" width="100%"/></p>
<p align="center"><b>Figure 7-4:</b> Reference Model Access Controls</p>

<a name="7.5.1.1"></a>
#### 7.5.1.1 The high-level functions of these different access controls
* **MGNT ACCESS CONTROLS** - Platform access to VNFs for service management. Typically all management and control-plane traffic is encrypted.
* **DATA ACCESS CONTROLS** - Control of east-west traffic between VNFs, and control of north-south traffic between the VNF and other platform services such as front-end carriage networks and platform services. Inherently strong separation between tenants is mandatory.
* **SERVICES ACCESS CONTROLS** - Protects platform services from any platform access
* **BACK-END ACCESS CONTROLS** - Data Centre Operations access to the platform, and subsequently, workloads. Typically stronger authentication requirements such as (Two-Factor Authentication) 2FA, and using technologies such as Role-Based Access Control (RBAC) and encryption. Application Programming Interface (API) gateways may be required for automated/script-driven processes.
* **FRONT-END ACCESS CONTROLS** - Protects the platform from malicious carriage network access, and provides connectivity for specific VNFs to specific carriage networks. Carriage networks being those that are provided as public networks and operated by carriers, and in this case with interfaces that are usually sub, or virtual networks.
* **TENANT ACCESS CONTROLS** - Provides apropriate tenant access controls to specific platform services, and tenant workloads - including Role-Based Access Control (RBAC), authentication controls as approriate for the access arrangement, and Application Programming Interface (API) gateways for automated/script-driven processes.

<a name="7.5.1.2"></a>
#### 7.5.1.2 The following general security requirements apply to the platform:
* Restrict traffic to (and from) the workload to only traffic that is necessary, and deny all other traffic.
* Provide protections between the Internet and any workloads including web and volumetrics attack preventions.
* Support zoning within a tenant workload - using application-level filtering.
* All host to host communications within the cloud provider network are to be cryptographically protected in transit.
* Not expose tenant IP address details to another tenant.
* Use cryptographically-protected protocols for administrative access to the platform.
* Data Centre Operations staff and systems must use management protocols that limit security risk such as SNMPv3, SSH v2, ICMP, NTP, syslog, and TLS.
* A platform change management process that is documented, well communicated to staff and tenants, and rigourously followed.
* A process to check change management adherence that is implemented, and rigourously followed.
* Processes for managing platform access control filters that are documented, followed, and monitored.
* No login to root on any platform systems (platform systems are those that are associated with the platform and include systems that directly or indirectly affect the viability of the platform).
* Role-Based Access Control (RBAC) must apply for all platform systems access.
* An approved system or process for last resort access must exist for the platform.
* All API access must use TLS protocol.
* All production workloads must be separated from all non-production workloads including separation between non-hosted non-production external networks.
* Where there are multiple hosting facilities used in provision of the service, network communications between facilities for the purpose of backup, management and application communication are cryptographically protected in transit between data centre facilities.
* Continuous cloud security compliance is mandatory.
* All data persisted to primary, replica or backup storage is to be encrypted.
* All platform security logs are to be time synchronised.
* Logs are to be regularly scanned for events of interest.
* An incident response plan must exist for the platform.
* The cloud services must be regularly vulnerability and penetration tested.

<a name="7.5.2"></a>
### 7.5.2 Platform ‘back-end’ access security
* Restrict traffic to only traffic that is necessary, and deny all other traffic.
* Use cryptographically-protected protocols for administrative access to the platform.
* Data Centre Operations staff and systems must use management protocols that limit security risk such as SNMPv3, SSH v2, ICMP, NTP, syslog, and TLS.
* A platform change management process that is documented, well communicated to staff and tenants, and rigourously followed.
* A process to check change management adherence that is implemented, and rigourously followed.
* Processes for managing platform access control filters that are documented, followed, and monitored.
* No login to root on any platform systems.
* Role-Based Access Control (RBAC) must apply for all systems access.
* An approved system or process for last resort access must exist for the platform.
* All back-end API access must use TLS.

<a name="7.5.3"></a>
### 7.5.3 Platform ‘front-end’ access security
* Front-end network security at the application level will be the responsibility of the workload, however the platform must ensure the isolation and integrity of tenant connectivity to front-end networks
* The front-end network may provide (Distributed Denial Of Service) DDOS support

<a name="7.7"></a>
## 7.7 Vendor Responsibilities

<a name="7.7.1"></a>
### 7.7.1 Software Hardening
        -   No hard-coded credentials/ clear text passwords
        -   Software should be independent of the infrastructure
            platform (no OS point release dependencies to patch)
        -   Software is code signed and all individual sub-components
            are assessed and verified for EULA violations
        -   Software should have a process for discovery,
            classification, communication, and timely resolution of
            security vulnerabilities (i.e.; bug bounty, Penetration
            testing/scan findings, etc)

<a name="7.7.2"></a>
### 7.7.2 Port Protection
        -   Unused software and unused network ports should be disabled,
            by default

<a name="7.7.3"></a>
### 7.7.3 Software Code Quality
        -   Vendors should use industry recognized software testing
            suites
            -   Static and dynamic scanning
                -   Automated static code review with remediation of
                    Medium/High/Critical security issues. The tool used
                    for static code analysis and analysis of code being
                    released must be shared.
                -   Dynamic security tests with remediation of
                    Medium/High/Critical security issues. The tool used
                    for Dynamic security analysis of code being released
                    must be shared
                -   Penetration tests (pen tests) with remediation of
                    Medium/High/Critical security issues.
                -   Methodology for ensuring security is included in the
                    Agile/DevOps delivery lifecycle for ongoing feature
                    enhancement/maintenance.

<a name="7.7.4"></a>
### 7.7.4 Alerting and monitoring
                -   Security event logging (All security events should
                    be logged, including informational)
                -   Privilege escalation detection

  <a name="7.7.5"></a>
### 7.7.5 Logging
                -   (Logging output should support customizable Log
                    retention and Log rotation)

  <a name="7.7.6"></a>
### 7.7.6 VNF images
                -   Image integrity – fingerprinting/validation
            -   Container Images
                -   Container Management
                -   Immutability

<a name="7.7.7"></a>
### 7.7.7 Identity and Access Management

<a name="7.7.8"></a>
### 7.7.8 CVEs and Vulnerability Management
                -   Security defect reporting
                -   Cadence with NFVi vendors (OSSA for OpenStack)

<a name="7.7.9"></a>
### 7.7.9 Encryption suite support
                -   Software should support recognized encryption
                    standards and encryption should be decoupled from
                    software

<a name="7.7.10"></a>
### 7.7.10 Password complexity support
                -   Software should support configurable, or industry
                    standard, password complexity rules

 <a name="7.7.11"></a>
### 7.7.11 Banner
                -   Software should have support for configurable
                    banners to display authorized use criteria/policy


<a name="7.8"></a>
## 7.8 Operator responsibility.

The Operator’s responsibility is to not only make sure that security is included in all the vendor supplied infrastructure and NFV components, but it is also responsible for the maintenance of the security functions from an operational and management perspective.   This includes but is not limited to securing the following elements:

• Maintaining standard security operational management methods and processes

• Monitoring and reporting functions

• Processes to address regulatory compliance failure

• Support for appropriate incident response and reporting

• Methods to support appropriate remote attestation certification of the validity of the security components, architectures and methodologies used

<a name="7.8.1"></a>
### 7.8.1 Remote Attestation/openCIT

NFVI operators must ensure that remote attestation methods are used to remotely verify the trust status of a given NFVI platform.  The basic concept is based on boot integrity measurements leveraging the TPM built into the underlying hardware. Remote attestation can be provided as a service, and may be used by either the platform owner or a consumer/customer to verify that the platform has booted in a trusted manner. Practical implementations of the remote attestation service include the open cloud integrity tool (Open CIT).   Open CIT provides ‘Trust’ visibility of the cloud infrastructure and enables compliance in cloud datacenters by establishing the root of trust and builds the chain of trust across hardware, operating system, hypervisor, VM and container.  It includes asset tagging for location and boundary control. The platform trust and asset tag attestation information is used by Orchestrators and/or Policy Compliance management to ensure workloads are launched on trusted and location/boundary compliant platforms. They provide the needed visibility and auditability of infrastructure in both public and private cloud environments.

Insert diagram here:
https://01.org/sites/default/files/users/u26957/32_architecture.png

<a name="7.8.2"></a>
### 7.8.2 VNF Image Scanning / Signing

It is easy to tamper with VNF images. It requires only a few seconds to insert some malware into a VNF image file while it is being uploaded to an image database or being transferred from an image database to a compute node. To guard against this possibility, VNF images can be cryptographically signed and verified during launch time. This can be achieved by setting up a signing authority and modifying the hypervisor configuration to verify an image’s signature before they are launched. To implement image security, the VNF operator must test the image and supplementary components verifying that everything conforms to security policies and best practices.

<a name="7.9"></a>
## 7.9 VNF Vendors responsibility.

The VNF vendors need to incorporate security elements to support the highest level of security of the networks they support.  This includes but is not limited to securing the following elements:

• Operating system or container

• Application

• Network interfaces

• Management and controller systems used to support the VNFs directly, examples include a SIEM system or a SD WAN policy manager

• Regulatory compliance failure as it relates to the application itself only

Image from https://www.networkworld.com/article/2840273/sdn-security-attack-vectors-and-sdn-hardening.html Will replace with a better image when I create it in the future.

<a name="7.10"></a>
## 7.10 NFVI and VIM Vendors responsibility

The NFVI vendors need to incorporate security elements to support the highest level of security of the infrastructure they support.  This includes but is not limited to securing the following elements:

• Hypervisor

• VM/container management system

• APIs

• Network interfaces

• Networking security zoning

• Platform patching mechanisms

• Regulatory compliance Failure

<a name="7.10.1"></a>
### 7.10.1 Networking Security Zoning

Network segmentation is important to ensure that VMs can only communicate with the VMs they are supposed to. To prevent a VM from impacting other VMs or hosts, it is a good practice to separate VM traffic and management traffic. This will prevent attacks by VMs breaking into the management infrastructure. It is also best to separate the VLAN traffic into appropriate groups and disable all other VLANs that are not in use. Likewise, VMs of similar functionalities can be grouped into specific zones and their traffic isolated. Each zone can be protected using access control policies and a dedicated firewall based on the needed security level.

Recommended practice to set network security policies following the principle of least privileged, only allowing approved protocol flows. For example, set 'default deny' inbound and add approved policies required for the functionality of the application running on the NFVI infrastructure.

<a name="7.10.2"></a>
### 7.10.2 Encryption

Virtual volume disks associated with VNFs may contain sensitive data. Therefore, they need to be protected. Best practice is to secure the VNF volumes by encrypting them and storing the cryptographic keys at safe locations. Be aware that the decision to encrypt the volumes might cause reduced performance, so the decision to encrypt needs to be dependent on the requirements of the given infrastructure.  The TPM module can also be used to securely store these keys. In addition, the hypervisor should be configured to securely erase the virtual volume disks in the event a VNF crashes or is intentionally destroyed to prevent it from unauthorized access.

• Composition analysis: New vulnerabilities are discovered in common open source libraries every week. As such, mechanisms to validate components of the VNF application stack by checking libraries and supporting code against the Common Vulnerabilities and Exposures (CVE) databases to determine whether the code contains any known vulnerabilities must be embedded into the NFVI architecture itself.  Some of the components required include:

• Tools for checking common libraries against CVE databases integrated into the deployment and orchestration pipelines.

• The use of Image scanners such as OpenSCAP to determine security vulnerabilities

<a name="7.10.3"></a>
### 7.10.3 Platform Patching

NFVI operators should ensure that the platform including the components (hypervisors, VMs, etc.) are kept up to date with the latest patch.

<a name="7.10.4"></a>
### 7.10.4 Boot Integrity Measurement (TPM)

Using a trusted platform module (TPM) as a hardware root of trust, the measurement of system sensitive components, such as platform firmware, bootloader, OS kernel, static filesystem and other system components can be securely stored and verified.
NFVI Operators should ensure that the TPM support is enabled in the platform firmware, so that platform measurements are correctly recorded during boot time.

Additionally, NFVI Operators should ensure that OS kernel measurements can be recorded by using a TPM-aware bootloader (e.g. [tboot](https://sourceforge.net/projects/tboot/) or [shim](https://github.com/rhboot/shim)), which can extend the root of trust up to the kernel level.
The validation of the platform measurements can be performed by TPM’s launch control policy (LCP) or through the remote attestation server.

<a name="7.10.5"></a>
### 7.10.5 Runtime Integrity Measurement (TPM)
If a remote attestation server is used to monitor platform integrity, the operators should ensure that attestation is performed periodically or in a timely manner.
Additionally, platform measurements may be extended to monitor the integrity of the static filesystem at run-time by using a TPM aware kernel module, such as [Linux IMA (Integrity Measurement Architecture)](https://sourceforge.net/p/linux-ima/wiki/Home/) for linux platforms, or by using the [trust policies](https://github.com/opencit/opencit/wiki/Open-CIT-3.2-Product-Guide#88-trust-policies) functionality of OpenCIT.
The static filesystem includes a set of important files and folders which do not change between reboots during the lifecycle of the platform.
This allows the attestation server to detect any tampering with the static filesystem during the runtime of the platform.

<a name="7.10.6"></a>
### 7.10.6 NFVI & VIM

Resources management is essential. Requests coming from NFVO or VNFM to the VIM must validated and the integrity of these requets must be verified.
<!-- The following tables have been relocated from Chapter 4, per Issue #245. -MXS 10/9/2019
#### 4.1.4.5 Internal security capabilities
-->
<a name="Table7-1"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|-------------------------------------|--------|------------------------------------------------------------------|
| i.nfvi.sec.cap.001 | VNF-C<->VNF-C  memory isolation | Yes/No | Are VNF-C memories isolated from each other by hardware support |
| i.nfvi.sec.cap.002 | VNF-C -> Host | Yes/No | Can VNF-C access host memory |
| i.nfvi.sec.cap.003 | Host -> VNF-C | Yes/No | Can Host access VNF-C memory |
| i.nfvi.sec.cap.004 | External storage at-rest encryption | Yes/No | Is external storage encrypted at-rest |

<p align="center"><b>Table 7-1:</b> Internal security capabilities of NFVI.</p>

Table 7-2 shows security capabilities

<a name="Table7-2"></a>

| Ref | VIM capability | Unit | Definition/Notes |
|--------------------|------------------|---------|-------------------------------------------|
| e.vim.sec.cap.001 | Resources management requests verification | Yes/No | Capability to validate and verify the integrity of a resources management requests coming from NFVO or VNFM|

<p align="center"><b>Table 7-2:</b> VIM capabilities related to security .</p>

## 7.11 Certification requirements (Just ideas)

-   Security test cases executed and test case results
-   Industry standard compliance achieved (NIST, ISO, PCI, FedRAMP
    Moderate etc.)
-   Output and analysis from automated static code review, dynamic
    tests, and penetration tests with remediation of
    Medium/High/Critical security issues. Tools used for security
    testing of software being released must be shared.
-   Details on un-remediated low severity security issues must be
    shared.
-   Threat models performed during design phase. Including remediation
    summary to mitigate threats identified.
-   Details on un-remediated low severity security issues.
-   Any additional Security and Privacy requirements implemented in the
    software deliverable beyond the default rules used security analysis
    tools
-   Resiliency tests run (such as hardware failures, or power failure
    tests).
