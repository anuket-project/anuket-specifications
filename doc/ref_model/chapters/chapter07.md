[<< Back](../../ref_model)
# 7	Security
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [7.1 Introduction.](#7.1)
* [7.2 Principles and Guidelines.](#7.2)
  * [7.2.1 Overarching Objectives and Goals.](#7.2.1)
  * [7.2.2 Verification Methodologies.](#7.2.2)
  * [7.2.3 Governance.](#7.2.3)  
* [7.3 Terms and Resources.](#7.3)
  * [7.3.1 Terms.](#7.3.1)
  * [7.3.2 Resources.](#7.3.2)
* [7.4 Security Scope.](#7.4)
  * [7.4.1 In-scope and Out-of-Scope definition.](#7.4.1)
  * [7.4.2 Define Platform security requirements](#7.4.2)
  * [7.4.3 Define Workload security requirements](#7.4.3)
  * [7.4.4 Define Workload security requirements](#7.4.4)
* [7.5 Platform Security.](#7.5)
  * [7.5.1 Platform Security Assumption.](#7.5.1)
  * [7.5.2 Platform ‘back-end’ access security.](#7.5.2)
  * [7.5.3 Platform ‘front-end’ access security](#7.5.3)
  * [7.5.4 Platform services.](#7.5.4)
* [7.6 Workload Security.](#7.6)
* [7.7 Vendor Responsibilities](#7.7)


<a name="7.1"></a>
## 7.1 Introduction

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<p align="center"><img src="../figures/ch10_ref_model_lfn.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 8-1:</b> CNTT relation to LFN OVP</p>

<a name="7.2"></a>
## 7.2 Principles and Guidelines

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

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
## 7.3 Terms and Resources

<a name="7.3.1"></a>
### 7.3.1 Terms

<table>
  <tr><th>Term</th><th>Description</th></tr>
  <tr><td>AZ</td><td>AZ	Availability Zone</td></tr>
  <tr><td>CPE</td><td>Customer Premises Equipment</td></tr>
  <tr><td>CVC</td><td>Compliance and Verification Committee</td></tr>
  <tr><td>ETSI</td><td>European Telecommunications Standards Institute</td></tr>
  <tr><td>ETSI NFV-TST</td><td>ETSI - Network Functions Virtualisation - Test</td></tr>
  <tr><td>ETSI NFV-IFA</td><td>ETSI - Network Functions Virtualisation - Infrastructure</td></tr>
  <tr><td>GB</td><td>Gigabit</td></tr>
  <tr><td>HW</td><td>Hardware</td></tr>
<tr><td>IMS</td>	<td>IP Multimedia Subsystem</td></tr>
<tr><td>I/O</td>	<td>Input/Output</td></tr>
<tr><td>MB</td>	<td>Megabit</td></tr>
<tr><td>NFV</td>	<td>Network Function Virtualization</td></tr>
<tr><td>NFVI</td>	<td>NFV Infrastructure</td></tr>
<tr><td>NUMA</td>	<td>Non-Unified Memory Access</td></tr>
<tr><td>OPNFV</td>	<td>Open Platform for NFV</td></tr>
<tr><td>RAM</td><td>Random Access Memory</td></tr>
<tr><td>SDN</td>	<td>Software Defined Networking</td></tr>
<tr><td>SD-WAN</td>	<td>Software Defined Wide Area Network</td></tr>
<tr><td>SLA</td>	<td>Service Level Agreement</td></tr>
<tr><td>SUT</td>	<td>System Under Test</td></tr>
<tr><td>SW</td>	<td>Software</td></tr>
<tr><td>vCPU</td>	<td>Virtual CPU (Central Processing Unit)</td></tr>
<tr><td>vNIC</td>	<td>Virtual NIC (Network Interface Card)</td></tr>
<tr><td>vRouter</td>	<td>Virtual Router</td></tr>
<tr><td>vSwitch</td>	<td>Virtual Switch</td></tr>
<tr><td>VIM</td>	<td>Virtual Infrastructure Manager</td></tr>
<tr><td>VNF</td>	<td>Virtualised Network Function</td></tr>
<tr><td>VNF-C</td>	<td>VNF Component (can be hosted on a VM, Container, etc)</td></tr>
<tr><td>VNFM</td>	<td>VNF Manager</td></tr>
</table>

<a name="7.3.2"></a>
### 7.3.2 Resources
1. OPNFV https://www.opnfv.org/ - project and community that facilitates a common NFVI, continuous integration (CI) with upstream projects, stand-alone testing toolsets, and a compliance and verification program for industry-wide testing and integration to accelerate the transformation of enterprise and service provider networks.<br>
2. CVC https://wiki.lfnetworking.org/display/LN/Compliance+and+Verification+Committee - members-driven committee within LF Networking that recommends policies and oversight for compliance and certification program to the Governing Board of LF Networking (“Governing Board”).

<a name="7.4"></a>
## 7.4 Security Scope

<a name="7.1.1"></a>
## 7.4.1 In-scope and Out-of-Scope definition

    *(Declare what should be in scope and what should be out of scope for
    CNTT security)*

-   Define and note separation of security postures of platform and
    workload, but that workload is dependent’ upon platform security.

    *(Provide some background commentary, from a security perspective,
    around the inter-relationship between platform and workload security
    where it is assumed that ‘workload’ leverages ‘platform’ security)*

<a name="7.4.2"></a>
## 7.4.2 Define Platform security requirements

    *(An overview/introduction to platform security requirements and incl
    types of platforms covered)*

<a name="7.4.3"></a>
## 7.4.3 Define Workload security requirements

    *(An overview/introduction to workload security requirements and incl
    types of workloads covered)*

<a name="7.4.4"></a>
## 7.4.4 Define certification/validation requirements

    *(An overview/introduction to workload certification requirements and
    incl types of workloads covered)*

<a name="7.5"></a>
## 7.5 Platform Security

<a name="7.5.1"></a>
## 7.5.1 Platform Security Assumption
    platform security compliance will be the responsibility of the platform owner.

    *(Define the platform security assumption. Note also that the platform
    may have a different security posture/level to the workload, but that
    the workload can leverage security accreditations/compliances/services
    offered by the platform).*

-   Refer industry references (case by case) – i.e. ISO, NIST, and etc.

    *(Can use material from, and update, the existing CNTT section on
    industry security standards)*

<a name="7.5.2"></a>
## 7.5.2 Platform ‘back-end’ access security

    *(Security requirements around how the platform systems must
    interconnect with supporting infrastructure services including
    assurance, fault, asset systems, billing systems, capacity,
    configuration, and etc.)*

<a name="7.5.3"></a>
## 7.5.3 Platform ‘front-end’ access security

    *(Security requirements around how the platform will support network
    connections that can be used by workloads. Generally the platform will
    provide the basic connectivity such as a physical MPLS connection, or
    Internet connection, but the workloads will have a VLAN on that physical
    connection and provide additional security controls).*

<a name="7.5.4"></a>
## 7.5.4 Platform services
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

<a name="7.6"></a>
## 7.6 Workload Security

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

<a name="7.7"></a>
## 7.7 Vendor Responsibilities

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

