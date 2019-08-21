[<< Back](../../ref_model)
# 7	Security
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>
**CNTT VNF Security Requirements**

**Security Posture CNTT**

-   In-scope and Out-of-Scope definition

*(Declare what should be in scope and what should be out of scope for
CNTT security)*

-   Define and note separation of security postures of platform and
    workload, but that workload is dependent’ upon platform security.

*(Provide some background commentary, from a security perspective,
around the inter-relationship between platform and workload security
where it is assumed that ‘workload’ leverages ‘platform’ security)*

-   Define Platform security requirements

*(An overview/introduction to platform security requirements and incl
types of platforms covered)*

-   Define Workload security requirements

*(An overview/introduction to workload security requirements and incl
types of workloads covered)*

-   Define certification requirements

*(An overview/introduction to workload certification requirements and
incl types of workloads covered)*

**Platform Security**

-   Platform Security Assumption: that platform security compliance will
    be the responsibility of the platform owner.

*(Define the platform security assumption. Note also that the platform
may have a different security posture/level to the workload, but that
the workload can leverage security accreditations/compliances/services
offered by the platform).*

-   Refer industry references (case by case) – i.e. ISO, NIST, and etc.

*(Can use material from, and update, the existing CNTT section on
industry security standards)*

-   Define platform ‘back-end’ access security

*(Security requirements around how the platform systems must
interconnect with supporting infrastructure services including
assurance, fault, asset systems, billing systems, capacity,
configuration, and etc.)*

-   Define platform ‘front-end’ access security

*(Security requirements around how the platform will support network
connections that can be used by workloads. Generally the platform will
provide the basic connectivity such as a physical MPLS connection, or
Internet connection, but the workloads will have a VLAN on that physical
connection and provide additional security controls).*

-   Platform services – cloud and security

*(Security requirements for any services hosted within the local VIM
environment, or the immediate trusted cloud)*

-   Platform services – external and security

*(Security requirements for any services that are hosted externally, but
leveraged or consumed within the local VIM environment)*

-   Data at rest

*(Security requirements of stored data used by platform services. This
will include provision for workload data)*

-   Data in transit

*(Security requirements for securing the different data types used in
the platform. This will include provision for protection of workload
data)*

-   Network Security considerations incl zoning, tiering, segmentation,
    standalone/hybrid clouds, multi-VIM, etc.

*(This section will have sub-sections – probably based on technology
types. Needs to cover security considerations around network security
for platforms, but also platform-to-platform, VIM-to-VIM where VIMs may
be homogeneous or heterogeneous. This will include confidentiality,
integrity, availability, identity federation and trust (authenticity)).*

-   Operator and support access to platform – requirements

*(It must be shown that operator and programmatic access to a platform
is secure. This will include ensuring that access controls are secure,
but not cumbersome. For programmatic access, there should be guidelines
around API gateway functionality expected and authentication/identity
standards expected).*

-   Assurance and Availability

*(The platform must have an assurance system(s) that meets minimum
requirements for the time to learn state changes, collect performance
and problem data from multiple platform layers, stream, correlate and
prioritise specific data \[to a specific bus type?\], and co-operate
with downstream systems in a closed-loop arrangement).*

-   Vulnerability Management

*(Security requirements around which and how vulnerabilities are
discovered, mitigated, managed in the platform. Any impacts to workloads
must be included).*

-   Logging management & privacy considerations (and incl legal
    intercept considerations?)

*(Requirements for platform security logging. This is likely to include
off-site storage, SIEM integration, logging access control, and log
rotation/archival/retrieval).*

-   Configuration management & CI/CD

*(Security requirements around how configuration changes are made to the
platform. This will include automated update processes and any impacts
to service and availability. Any impacts to workloads must be
included).*

-   Fault Management

*(Security requirements around fault restoration (including zero trust
for more secure deployments?)*

-   Asset Management

*(Security requirements around how assets should be discovered,
collected, stored, accessed and protected).*

-   Closed Loop Security (general) and/or SIEM integration –
    requirements and implementation

*(Security requirements around closed-loop security. Starting to define
a set of standards that we want for vendor standardisation. Implications
on homogeneous/heterogeneous VIMs).*

-   Micro-segmentation (general) – requirements and implementation

*(Security requirements around micro-segmentation – levels of controls
within the platform, how the controls are managed and monitored.
Expectations around application of policy and flow monitoring across
homogeneous/heterogeneous VIMs)*

**Workload Security**

-   Workload Security Assumption: that workload security compliance will
    be a responsibility of the workload owner (if not the platform
    owner) but will leverage any compliances from the platform.

*(Define the workload security assumption. Note also that the workload
may have a different security posture/level to the platform, but that
the workload can leverage security accreditations/compliances/services
offered by the platform).*

-   Strong separation between tenants and tenants
    -   data at rest

*(requirements that tenant data is protected including disk allocation,
namespace separation, and memory isolation)*

-   data in transit

*(ensure that strong access controls and processes exist around
east-west and north-south tenant-to-tenant comms. Define level of access
control and associated access services)*

-   cloud security – refer cloud security industry standards – i.e. TBC

*(meet industry cloud security requirements)*

-   workload services – cloud

*(Security requirements for any services consumed within the local VIM
environment, or the immediate trusted cloud)*

-   workload services – external

*(Security requirements for any services that are consumed from external
sources)*

-   Strong separation between tenants and platform

*(Cover different platform types and separation requirements of each,
including:*

-   *Bare metal*
-   *VM*
-   *Container*

*Incl. separation of workload traffic from platform
management/signalling)*

-   Define workload ‘Front-end’ access security

*(Security requirements around how the workload will connect to network
connections that are external to the tenancy, and are used as part of
the tenancy data service – this could include an MPLS VPN connection, or
an Internet connection. The workload environment will be expected to
support sufficient security to support the workload certification
requirements).*

-   Define workload ‘Back-end’ access security

*(Security requirements around how the workload may be managed - which
may or may not be known by the tenant. This includes management and
signalling and separation/protection/isolation of these network
connections)*

-   Operator and support access to workload including:
    -   Bare Metal
    -   VM
    -   Container
    -   VNF

*(Security requirements around how tenant workloads are supported –
cover a situation where it is tenant, and another where it is a cloud
service. May be different for different service types – i.e. BareMetal,
VM, Container, and VNF).*

-   Workload tenant access to workloads

*(Security requirements around tenant support of a workload. Covers
operator and robotic access. Access controls, policy, and guidelines.
May be different for different service types – i.e. BareMetal, VM,
Container, and VNF).*

-   Assurance – tenant

*(The workload environment must have support for assurance system(s)
that meets minimum requirements for the time to learn state changes,
collect performance and problem data from multiple platform layers,
stream, correlate and prioritise specific data \[to a specific bus
type?\], and co-operate with downstream systems in a closed-loop
arrangement).*

-   Configuration Management – tenant

*(Security requirements around how configuration changes are made to the
workload environment. This will include automated update processes and
any impacts to service and availability. This includes process).*

-   Fault Management – tenant

*(Security requirements around fault restoration in a workload
environment (including zero trust for more secure deployments?)*

-   Telemetry – tenant (reference to a telemetry working group, if any)?

*(Security requirements covering the provision of telemetry to tenants
incl access, authentication, integrity, confidentiality and
availability).*

**Workload Vendor Responsibilities**

-   Host Hardening
    -   Host Protection
        -   No hard-coded credentials/ clear text passwords
        -   Software should be independent of the infrastructure
            platform (no OS point release dependencies to patch)
        -   Software is code signed and all individual sub-components
            are assessed and verified for EULA violations
        -   Software should have a process for discovery,
            classification, communication, and timely resolution of
            security vulnerabilities (i.e.; bug bounty, Penetration
            testing/scan findings, etc)
    -   Port Protection
        -   Unused software and unused network ports should be disabled,
            by default
    -   Software Code Quality
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
            -   Alerting and Monitoring
                -   Security event logging (All security events should
                    be logged, including informational)
                -   Privilege escalation detection
            -   Logging
                -   (Logging output should support customizable Log
                    retention and Log rotation)
            -   VM images
                -   Image integrity – fingerprinting/validation
            -   Container Images
                -   Container Management
                -   Immutability
            -   Identity and Access Management
            -   CVEs and Vulnerability Management
                -   Security defect reporting
                -   Cadence with NFVi vendors (OSSA for OpenStack)
            -   Encryption suite support
                -   Software should support recognized encryption
                    standards and encryption should be decoupled from
                    software
            -   Password complexity support
                -   Software should support configurable, or industry
                    standard, password complexity rules
            -   Banner
                -   Software should have support for configurable
                    banners to display authorized use criteria/policy

**Certification requirements (Just ideas):**

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
## Original Material - for review

## Table of Contents
* [7.1 Common standards.](#7.1)
  * [7.1.1 Potential attack vectors.](#7.1.1)
  * [7.1.1 Testing demarcation points.](#7.1.2)
* [7.2 Operator responsibility.](#7.2)
  * [7.2.1 Remote Attestation/openCIT.](#7.2.1)
  * [7.2.2 VNF Image Scanning / Signing.](#7.2.2)
* [7.3 VNF Vendors responsibility.](#7.3)
* [7.4 NFVI Vendors responsibility](#7.4)
  * [7.4.1 Networking Security Zoning.](#7.4.1)
  * [7.4.2 Encryption.](#7.4.2)
  * [7.4.3 Platform Patching.](#7.4.3)
  * [7.4.4 Boot Integrity Measurement (TPM).](#7.4.4)


<a name="7.1"></a>
## 7.1 Common standards

Security vulnerabilities and attack vectors are everywhere.  The telecom industry and its cloud infrastructures are even more vulnerable to potential attacks due to the ubiquitous nature of the infrastructures and services combined with the vital role Telecommunications play in the modern world.   The attack vectors are many and varied, ranging from the potential for exposure of sensitive data, both personal and corporate, to weaponized disruption to the global Telecommunications networks.  The threats can take the form of a physical attack on the locations the infrastructure hardware is housed, to network attacks such as denial of service and targeted corruption of the network service applications themselves.  Whatever the source, any NFVI infrastructure built needs to be able to withstand attacks in whatever form they take.

With that in mind, the NFVI reference model and the supporting architectures are not only required to optimally support networking functions, but they must be designed with common security principles and standards from inception.  These best practices must be applied at all layers of the infrastructure stack and across all points of interconnections with outside networks, APIs and contact points with the NFV network functions overlaying or interacting with that infrastructure. 
Standards organizations with recommendations and best practices, and certifications that need to be taken into consideration include the following examples. However this is by no means an exhaustive list, just some of the more important standards in current use.  

 •	Center for Internet Security - https://www.cisecurity.org/

 •	Cloud Security Alliance - https://cloudsecurityalliance.org/

 •	Open Web Application Security Project https://www.owasp.org  

 •	The National Institute of Standards and Technology (NIST) (US Only)

 •	FedRAMP Certification https://www.fedramp.gov/ (US Only)

 •	ETSI Cyber Security Technical Committee (TC CYBER) - https://www.etsi.org/committee/cyber

•	ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) - www.iso.org.  The following ISO standards are of particular interest for NFVI

    o	ISO/IEC 27002:2013 - ISO/IEC 27001 is the international Standard for best-practice information security management systems (ISMSs).

    o	ISO/IEC 27032 - ISO/IEC 27032is the international Standard focusing explicitly on cybersecurity.

    o	ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management. Incident management
    
    o	ISO/IEC 27031 - ISO/IEC 27031 is the international Standard for ICT readiness for business continuity.
    
A good place to start to understand the requirements is to use the widely accepted definitions developed by the OWASP – Open Web Application Security Project.  These include the following core principles:

•	Confidentiality – Only allow access to data for which the user is permitted

•	Integrity – Ensure data is not tampered with or altered by unauthorized users

•	Availability – ensure systems and data are available to authorized users when they need it

Additional NFVI security principles that need to be incorporated:

•	Authenticity – The ability to confirm the users are in fact valid users with the correct rights to access the systems or data.

<a name="7.1.1"></a>
## 7.1.1 Potential attack vectors.
Previously attacks designed to place and migrate workload outside the legal boundaries were not possible using traditional infrastructure, due to the closed nature of these systems. However, using NFVI, violation of regulatory policies and laws becomes possible by actors diverting or moving a VNF from an authenticated and legal location to another potentially illegal location. The consequences of violating regulatory policies may take the form of a complete banning of service and/or an exertion of a financial penalty by a governmental agency or through SLA enforcement.  Such vectors of attack may well be the original intention of the attacker in an effort to harm the service provider. One possible attack scenario can be when an attacker exploits the insecure VNF API to dump the records of personal data from the database in an attempt to violate user privacy. NFVI operators should ensure that VNF APIs are secure, accessible over a secure network (TLS) under very strict set of security best practices and RBAC policies to limit exposure of this vulnerability.

<a name="7.1.2"></a>
## 7.1.2 Testing demarcation points.

It is not enough to just secure all potential points of entry and hope for the best, any NFVI architecture must be able to be tested and validated that it is in fact protected from attack as much as possible. The ability to test the infrastructure for vulnerabilities on a continuous basis is critical for maintaining the highest level of security possible.  Testing needs to be done both from the inside and outside of the systems and networks.  Below is a small sample of some of the testing methodologies and frameworks available.  

•	OWASP testing guide

•	PCI Penetration testing guide

•	Penetration Testing Execution Standard

•	NIST 800-115

    o	VULCAN: Vulnerability Assessment Framework for Cloud Computing (NIST)

•	Penetration Testing Framework

•	Information Systems Security Assessment Framework (ISSAF)

•	Open Source Security Testing Methodology Manual (“OSSTMM”)

•	FedRAMP Penetration Test Guidance (US Only)

•	CREST Penetration Testing Guide

Insuring that the security standards and best practices are incorporated into the NFVI model and architectures must be a shared responsibility, among the Telecommunications operators interested in building and maintaining the infrastructures in support of their services, the VNF vendors developing the network services that will be consumed by the operators, and the NFVI vendors creating the infrastructures for their Telecommunications customers.  All of the parties need to incorporate security and testing components, and maintain operational processes and procedures to address any security threats or incidents in an appropriate manner.  Each of the stakeholders need to contribute their part to create effective security for NFVI.

<a name="7.2"></a>
## 7.2 Operator responsibility.

The Operator’s responsibility is to not only make sure that security is included in all the vendor supplied infrastructure and NFV components, but it is also responsible for the maintenance of the security functions from an operational and management perspective.   This includes but is not limited to securing the following elements:

•	Maintaining standard security operational management methods and processes

•	Monitoring and reporting functions

•	Processes to address regulatory compliance failure

•	Support for appropriate incident response and reporting

•	Methods to support appropriate remote attestation certification of the validity of the security components, architectures and methodologies used

<a name="7.2.1"></a>
### 7.2.1 Remote Attestation/openCIT

NFVI operators must ensure that remote attestation methods are used to remotely verify the trust status of a given NFVI platform.  The basic concept is based on boot integrity measurements leveraging the TPM built into the underlying hardware. Remote attestation can be provided as a service, and may be used by either the platform owner or a consumer/customer to verify that the platform has booted in a trusted manner. Practical implementations of the remote attestation service include the open cloud integrity tool (Open CIT).   Open CIT provides ‘Trust’ visibility of the cloud infrastructure and enables compliance in cloud datacenters by establishing the root of trust and builds the chain of trust across hardware, operating system, hypervisor, VM and container.  It includes asset tagging for location and boundary control. The platform trust and asset tag attestation information is used by Orchestrators and/or Policy Compliance management to ensure workloads are launched on trusted and location/boundary compliant platforms. They provide the needed visibility and auditability of infrastructure in both public and private cloud environments.

Insert diagram here:
https://01.org/sites/default/files/users/u26957/32_architecture.png 

<a name="7.2.2"></a>
### 7.2.2 VNF Image Scanning / Signing

It is easy to tamper with VNF images. It requires only a few seconds to insert some malware into a VNF image file while it is being uploaded to an image database or being transferred from an image database to a compute node. To guard against this possibility, VNF images can be cryptographically signed and verified during launch time. This can be achieved by setting up a signing authority and modifying the hypervisor configuration to verify an image’s signature before they are launched. To implement image security, the VNF operator must test the image and supplementary components verifying that everything conforms to security policies and best practices. 

<a name="7.3"></a>
## 7.3 VNF Vendors responsibility.

The VNF vendors need to incorporate security elements to support the highest level of security of the networks they support.  This includes but is not limited to securing the following elements:

•	Operating system or container

•	Application

•	Network interfaces

•	Management and controller systems used to support the VNFs directly, examples include a SIEM system or a SD WAN policy manager

•	Regulatory compliance failure as it relates to the application itself only
 
Image from https://www.networkworld.com/article/2840273/sdn-security-attack-vectors-and-sdn-hardening.html Will replace with a better image when I create it in the future.

<a name="7.4"></a>
## 7.4 NFVI Vendors responsibility

The NFVI vendors need to incorporate security elements to support the highest level of security of the infrastructure they support.  This includes but is not limited to securing the following elements:

•	Hypervisor

•	VM/container management system

•	APIs

•	Network interfaces

•	Networking security zoning

•	Platform patching mechanisms

•	Regulatory compliance Failure

<a name="7.4.1"></a>
### 7.4.1 Networking Security Zoning

Network segmentation is important to ensure that VMs can only communicate with the VMs they are supposed to. To prevent a VM from impacting other VMs or hosts, it is a good practice to separate VM traffic and management traffic. This will prevent attacks by VMs breaking into the management infrastructure. It is also best to separate the VLAN traffic into appropriate groups and disable all other VLANs that are not in use. Likewise, VMs of similar functionalities can be grouped into specific zones and their traffic isolated. Each zone can be protected using access control policies and a dedicated firewall based on the needed security level.

Recommended practice to set network security policies following the principle of least privileged, only allowing approved protocol flows. For example, set 'default deny' inbound and add approved policies required for the functionality of the application running on the NFVI infrastructure.

<a name="7.4.2"></a>
### 7.4.2 Encryption

Virtual volume disks associated with VNFs may contain sensitive data. Therefore, they need to be protected. Best practice is to secure the VNF volumes by encrypting them and storing the cryptographic keys at safe locations. Be aware that the decision to encrypt the volumes might cause reduced performance, so the decision to encrypt needs to be dependent on the requirements of the given infrastructure.  The TPM module can also be used to securely store these keys. In addition, the hypervisor should be configured to securely erase the virtual volume disks in the event a VNF crashes or is intentionally destroyed to prevent it from unauthorized access.  

•	Composition analysis: New vulnerabilities are discovered in common open source libraries every week. As such, mechanisms to validate components of the VNF application stack by checking libraries and supporting code against the Common Vulnerabilities and Exposures (CVE) databases to determine whether the code contains any known vulnerabilities must be embedded into the NFVI architecture itself.  Some of the components required include:

•	Tools for checking common libraries against CVE databases integrated into the deployment and orchestration pipelines.

•	The use of Image scanners such as OpenSCAP to determine security vulnerabilities

<a name="7.4.3"></a>
### 7.4.3 Platform Patching

NFVI operators should ensure that the platform including the components (hypervisors, VMs, etc.) are kept up to date with the latest patch. 

<a name="7.4.4"></a>
### 7.4.4 Boot Integrity Measurement (TPM)

Using trusted platform module (TPM) as a hardware root of trust, the measurement of system sensitive components such as platform firmware, BIOS, bootloader, OS kernel, and other system components can be securely stored and verified. NFVI Operators should ensure that the platform measurement can only be taken when the system is reset or rebooted; there needs to be no ability to write the new platform measurement in TPM during system run-time. The validation of the platform measurements can be performed by TPM’s launch control policy (LCP) or through the remote attestation server
