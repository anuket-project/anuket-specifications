[<< Back](../../openstack)

# 6. Security
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 Security Requirements](#6.2)
* [6.3 NFVI and VIM Security](#6.3)
    * [6.3.1 Platform Access](#6.3.1) 
    * [6.3.2 System Hardening](#6.3.2) 
    * [6.3.3 Confidentiality and Integrity](#6.3.3) 
    * [6.3.4 Workload Security](#6.3.4) 
    * [6.3.5 Image Security](#6.3.5) 
    * [6.3.6 Security LCM](#6.3.6) 
    * [6.3.7 Security Audit Logging](#6.3.7)

## 6.1 Introduction

This guide is intended to provide basic security requirements to CNTT architects who are implementing NFVI using [OpenStack](https://www.openstack.org/) technology.  This is a minimal set of high-level general security practices, not intended to cover all implementation scenarios.  Please ensure to also reference your enterprise security and compliance requirements in addition to this guide.

<a name="6.2"></a>
## 6.2 Security Requirements

Chapter 2 gathers all requirements and recommendations regarding security topics developed in this chapter.

<a name="6.3"></a>
## 6.3 NFVI and VIM Security

OpenStack security guide:
https://docs.openstack.org/security-guide/introduction/introduction-to-openstack.html. In the section "[Sceurity boundaries and threats](https://docs.openstack.org/security-guide/introduction/security-boundaries-and-threats.html)" there is extensive description on security domains, threat classifications, and attack vectors. The following only touches on some of the topics and at a high level.

The handling of these security incidents requires various levels of logging of key infrastructure, processes, and use behaviour. These logs have to be continuously monitored and analysed with alerts created for anomalies. The resources for logging, monitoring and alerting also need to logged and monitored and corrective actions taken so that they are never short of the needed resources (sec.mon.015).

<a name="6.3.1"></a>
### 6.3.1 Platform Access

#### 6.3.1.1 [Identity Security](https://docs.openstack.org/security-guide/identity.html)
The OpenStack Identity service (Keystone) provides identity, token, catalog, and policy services for use specifically by services in the OpenStack family. Identity service is organized as a group of internal services exposed on one or many endpoints. Many of these services are used in a combined fashion by the front end.

OpenStack Keystone can work with an Identity service that your enterprise may already have, such as LDAP with Active Directory.  In those cases, the recommendation is to integrate Keystone with the cloud provider's Identity Services.  

#### 6.3.1.2 Authentication
Authentication is the first line of defense for any real-world implementation of OpenStack.  At its core, authentication is the process of confirming the user logging in is who they claim to be.  OpenStack Keystone supports multiple methods of authentication, such as username/password, LDAP, and others.  For more details, please refer to [OpenStack Authentication Methods](https://docs.openstack.org/security-guide/identity/authentication-methods.html).

Limiting the number of repeated failed login attempts (configurable) reduces the risk of unauthorised access via password guessing (Bruce force attack) - sec.mon.006 and sec.mon.009. The restriction on the number of consecutive failed login attempts ("lockout_failure_attempts") and any actions post such access attempts (such as locking the account where the "lockout_duration" is left unspecified) should abide by the operator's policies. For example, an operator may restrict the number of consecutive failed login attempts to 3 ("lockout_failure_attempts = 3") and lock the account preventing any further access and where the account is unlocked by getting necessary approvals.  

##### Keystone Tokens
Once a user is authenticated, a token is generated for authorization and access to an OpenStack environment and resources.  By default, the token is set to expire in one hour. This setting can be changed based on the business and operational needs, but it's highly recommended to set the expiration to the shortest possible value without dramatically impacting your operations.

**Special Note on Logging Tokens:** since the token would allow access to the OpenStack services, it *MUST* be masked before outputting to any logs.

#### 6.3.1.3 Authorization
Authorization serves as the next level of defense.  At its core, it checks if the authenticated users have the permission to execute an action. Most Identity Services support the notion of groups and roles. A user belongs to groups and each group has a list of roles that permits certain action on certain resources. OpenStack services reference the roles of the user attempting to access the service. OpenStack policy enforcer middleware takes into consideration the policy rules associated with each resource and the user’s group/roles and association to determine if access will be permitted for the requested resource. For more details on policies, please refer to the [OpenStack Policies](https://docs.openstack.org/security-guide/identity/policies.html#policy-section).

#### 6.3.1.4 RBAC
In order to properly manage user access to OpenStack services, service providers should utilize the Role Based Access Control (RBAC) system.  Based on the OpenStack Identify Service (Keystone v3) Group and Domain component, the RBAC system implements a set of access roles that accommodate most use cases. Operations staff can create users and assign them to roles using standard OpenStack commands for users, groups, and roles.

###### Rules
The following rules govern create, read, update, and delete (CRUD) level access.
- *_member_* can create, read, update, and delete the resources defined at the tenant level.
- *support_member* can create and read the resources defined at the tenant level.
- *viewer* can read the resources defined at the tenant level.
- *admin* can create, read, update, and delete all resources.


###### Recommended Default Roles to Start
 **site_admin** (HIGHLY RESTRICTED)
 - *Site Level Super Admin* - usually assign to Operation Staffs who already have root level access to hosts
 - Permission to create/read/update/delete all tenants and resources at the site, including creating snapshot and upload public images
 - Limited ability to create/read/update/delete tenant projects
  
 **site_admin_support**
 - *Site Level Admin* - usually assign to Operation Staffs who need to manage resource except delete
 - Permission to create/read/update all tenants and resources at the site
 - Cannot create snapshots
 
 **site_admin_viewer**
  - *Site Level Admin Read Only* - usually assign to groups who need to view all resources, such as Capacity Planners
  - Permission to read all tenants and resources at the site
  - Cannot create/update/delete

 **site_image_manager**
  - Site wide admin level privileges to Glance API (via CLI)
  - Restricted to Image team
    
 **tenant_member**
  - *Tenant Level Admin* - typically assign to majority of tenant users to manage their resources
  - Permission to create/read/update/delete to all resources at the tenant project level
  - Cannot upload image or create snapshot
  - Cannot touch any other tenant except the one the role is located

 **tenant_snapshot_member**
  - *Tenant Level Admin with Snapshot* - typically assign to tenant users who needs to create snapshot via special request to Operations Staff
  - Permission is same as tenant_member except the user can also create snapshots

 **tenant_support_member**
  - *Tenant Level Support* - typically assign to tenant users who needs to create resource in the project space
  - Permission to create/read all resources at the tenant project level
  - Cannot update/delete or create snapshots
 
 **tenant_viewer**
  - *Tenant Level Read Only* - typically assign to tenant users who needs to read all resource in the project space
  - Permission to read all resources at the tenant level
  - Cannot create/update/delete

<a name="6.3.2"></a>
### 6.3.2 System Hardening
All infrastructure should undergo system hardening, establish processes to govern the hardening, and documents to cover at a minimal for the following areas:

#### 6.3.2.1 Password policy
For all infrastructure components, passwords must be hardened and a strict password policy must be applied (req.sec.gen.002).

Passwords must be strengthened:
- All vendors default passwords must be changed
- Passwords must contain at least 8 characters as a minimal value, 14 characters length passwords are recommended
- Passwords must contain at least one upper case letter, one lower case letter and one non-alphabetic character
- For administration privileges accounts, passwords must contain at least one upper case letter, one lower case letter, one numeral and one special (non-alphanumeric) character   

For passwords updates, the identity of users must be verified before permitting a password change.

Passwords must be encrypted at rest and in-transit. Password files must be stored separately from application system data.

Password's composition, complexity and policy should follow the recommendations consolidated within the [CIS Password Policy guide](https://www.cisecurity.org/white-papers/cis-password-policy-guide/) such as:
- Check the password for known bad passwords (repetitive or sequential characters, dictionary words, context-specific words, previously used passwords, etc.)
- Limit number of failed login attempts
- Implement Multi-factor Authentication
- Periodic (for example, Yearly, Quarterly, etc.)  password change or on key events such as indication of compromise, change of user roles, a defined period of inactivity, when a user leaves the organization, etc..


#### 6.3.2.2 Function and Software
Infrastructure should be implemented to perform the minimal function that’s practically needed to support NFVI. 

Regarding software:
- Install only software which is required to support the functions
- Remove any unnecessary software or packages
- Where software cannot be removed, disable all service to it

#### 6.3.2.3 Patches
System should be implemented to allow installation of the latest patches to address security vulnerabilities in the following timescale from discovery:
| Severity | Time to Remediate |
| ----------- | ----------- |
| Zero-Day | Immediately or as soon as practically possible |
| Critical | 30 days |
| High | 60 days |
| Medium | 90 days |
| Low | 180 days |

**See** [Common Vulnerability Scoring System] (https://nvd.nist.gov/vuln-metrics/cvss)
	
#### 6.3.2.4 Network Protocols
- Only allow protocols that are required by the system functions
- Tighten all required TCP/IP (Transmission Control Protocol/Internet Protocol) services

#### 6.3.2.5 System Access
- Remove, or at a minimal, disable all unnecessary user accounts 
- Change all default user accounts where technically feasible
- Change all default credentials
- Restrict access according to only those protocols/service/address adhering to the [Principle of Least Privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)

#### 6.3.2.6 Anti-Virus and Firewall
- Install and run your Enterprise approved anti-virus software / intrusion protection / malware / spyware endpoint security software with up to date profiles, minimal refresh daily
- Install and run firewall software where applicable

#### 6.3.2.7 Vulnerability Detection and Prevention
- Implement DoS (Denial of Service) protection where applicable
- Ensure logging and alerting is actively running
- Run host-based scanning and fix all findings per vulnerability severity 
- Run network-based scanning and fix all findings per vulnerability severity


<a name="6.3.3"></a>
### 6.3.3 Confidentiality and Integrity

Confidentiality implies that data and resources must be protected against unauthorized introspection/exfiltration. Integrity implies that the data must be protected from unauthorized modifications or deletions.

Regarding confidentiality and integrity in Cloud Infrastructure, 2 main concerns are raised: 
- confidentiality and integrity of the Cloud Infrastructure components (networks, hypervisor, OpenStack services)
- confidentiality and integrity of the tenant's data 

The Cloud Infrastructure must also provide the mechanism to identify corrupted data.

#### 6.3.3.1 Confidentiality and Integrity of communications

It is essential to secure the infrastructure from external attacks. To counter this threat, API endpoints exposed to external networks must be protected by either a rate-limiting proxy or web application firewall and must be placed behind a reverse HTTPS proxy (sec.mon.008). Attacks can also be generated by corrupted internal components, and for this reason, it is security best practice to ensure integrity and confidentiality of all network communications (internal and external) by using Transport Layer Security (TLS) protocol.
When using TLS, according to the [OpenStack security guide](https://docs.openstack.org/security-guide/secure-communication/introduction-to-ssl-and-tls.html) recommendation, the minimum version to be used is TLS 1.2.

3 categories of traffic will be protected using TLS:
- traffic from and to external domains
- communications between OpenStack components (OpenStack services, Bus message, Data Base)
- management traffic

Certificates used for TLS encryption must be signed by a trusted authority. To issue certificates for internal OpenStack users or services, the cloud provider can use a Public Key Infrastructure with its own internal Certification Authority (CA), certificate policies, and management.

#### 6.3.3.2 Integrity of OpenStack components configuration

The cloud deployment components/tools store all the information required to install the infrastructure including sensitive information 
such as credentials. It is recommended to turn off deployment components after deployment to minimize attack surface area, limit the risk of compromise, and to deploy and provision the infrastructure through a dedicated network (VLAN).

Configuration files contain sensitive information. 
These files must be protected from malicious or accidental modifications or deletions by configuring strict access permissions for such files. All access, failed attempts to change and all changes (pre-change, post-change and by who) should be securely logged, and all failed access and failed changes should be alerted (sec.mon.006 and sec.mon.007).

The Cloud Infrastructure must provide the mechanisms to identify corrupted data (sec.mon.013):
- the integrity of configuration files and binaries must be checked by using cryptographic hash,
- it is recommended to run scripts (such as checksec.sh) to verify the properties of the QEMU/KVM
- it is recommended to use tool such as [CIS-CAT](https://www.cisecurity.org/cybersecurity-tools/cis-cat-pro/) (Center for Internet security- Configuration Assessment Tool) to check the compliance of systems configuration against respective [CIS benchmarks](https://www.cisecurity.org/cis-benchmarks/).

It is strongly recommend to protect Linux repositories and Docker registries against the corruption of their data, by adopting protection measures such as hosting a local repository/registry with restricted and controlled access, and using TLS. 
This repository/registry must contain only signed images or packages.

#### 6.3.3.3 Confidentiality and Integrity of tenant data (sec.mon.012 and sec.mon.013)

Tenant data are forwarded unencrypted over the network. Since the VNF is responsible for its security, it is up to the VMs to establish secure data plane, e.g. using IPsec over its tenant network.

A Cloud actor must not be able to retrieve secrets used by VNF managers.
All communications between the VNFM or orchestrator, and the infrastructure must be protected in integrity and confidentiality (e.g. by using TLS) and controlled via appropriate IP filtering rules. 

The Cloud Infrastructure should onboard only trusted and verified VM images implying that VNF vendors provide signed images (sec.mon.012).
Images from non-trusted sources may contain security breaches or unsolicited malicious code (spoofing, information disclosure). 
It is recommended to scan all VM images with a vulnerability scanner. The scan is mandatory for images from unknown or untrusted sources.

To mitigate tampering attacks, it is recommended to use [Glance image signing feature](https://docs.openstack.org/glance/pike/user/signature.html) to validate an image when uploading. In this case, Barbican service must be installed.

In order to protect data, VNFs must encrypt the volumes they use. In this case, the encryption key must not be stored on the infrastructure. 
When a key management service is provided by the infrastructure, OpenStack can encrypt data on behalf of tenants.
It is recommended to rely on Barbican, as key manager service of OpenStack.

<a name="6.3.4"></a>
### 6.3.4 Workload Security

OpenStack segregates its infrastructure (for example, hosts) by Regions, Host aggregates and Availability Zones (AZ). Workloads can also be segregated by server groups (affinity and non-affinity groups). These options support the workloads placement requirement _sec.wl.001_.

Separation of non-production and production workloads, or by workload category (for example, payment card information, healthcare, etc.) requires separation through server groups (for example, Regions, AZs) but also requires network and storage segregation as in Regions but also AZs if engineered to do so. Thus, the separation of these workloads is handled through placement of workloads in separate AZs and/or Regions (_sec.wl.005_ and _sec.wl.006_).

Regions also support the _sec.wl.004_ requirement for separation by Location (for example, country).

Operational security (_sec.wl.002_) is handled through a combination of mechanisms including the above and security groups. Security groups limit the types of traffic that have access to instances. One or more security groups can be automatically assigned to an instance at launch. The rules associated with a security group control the incoming traffic.  Any incoming traffic not matched by a rule is denied access. The security group rules govern access through the setting of different parameters: traffic source, protocols and destination port on a VM.  Errors in provisioning/managing OpenStack Security Groups can lead to non-functioning applications and can take a long time to identify faults and correct them.  Thus, use of tools for auto provisioning and continued inspection of security groups and network policies is required.

Given the rate of change in the workload development and deployment, and the cloud environment itself, _sec.wl.003_ requires that the workloads should be assessed during the CI/CD process as the images are created and then whenever they are deployed. In addition, the infrastructure must be configured for security as discussed elsewhere in this chapter including secure boot. 

<a name="6.3.4.1"></a>
### 6.3.4.1 SR-IOV and DPDK Considerations

SR-IOV agent only works with NoopFirewallDriver when Security Groups are enabled, but can still use other firewall_driver for other Agents by updating their conf with the requested firewall driver." Please see [SR-IOV Passthrough for Networking](https://wiki.openstack.org/wiki/SR-IOV-Passthrough-For-Networking).

Operators typically do not implement Security Groups when ussing SR-IOV or DPDK networking technologies.

<a name="6.3.5"></a>
### 6.3.5 Image Security

Valuable guidance on trusted image creation process and image signature verification is provided in the "Trusted Images" section of the [OpenStack Security Guide](https://docs.openstack.org/security-guide/instance-management/security-services-for-instances.html#trusted-images/). The OpenStack Security Guide includes reference to the "[OpenStack Virtual Machine Image Guide](https://docs.openstack.org/image-guide/) that "describes how to obtain, create, and modify" OpenStack compatible virtual machine images. 

Images to be ingested, including signed images from trusted sources, need to be verified prior to ingestion into the Image Service (Glance). The operator will need toolsets for scanning images, including for virus and malware detection. Adding Signed Images to the Image Service (Glance) is specified in [OpenStack Operations Guide](https://docs.openstack.org/operations-guide/ops-user-facing-operations.html#adding-signed-images). The chain of trust requires that all images are verified again in the Compute service (Nova) prior to use.

Integrity Verification at the time of instantiation is required by [ETSI NFV SEC021](https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=53601) and the creation of signature per individual artifact in the VNF package is required by [ETSI NFV SOL004](http://www.etsi.org/deliver/etsi_gs/NFV-SOL/001_099/004/02.03.01_60/gs_nfv-sol004v020301p.pdf).



<a name="6.3.6"></a>
### 6.3.6 Security LCM
Cloud Infrastructure LCM encompasses provisioning, deployment, configuration and management (resources scaling, services upgrades…) as described in [chapter 7](./chapter07.md). These operations must be securely performed in order to keep the infrastructure safe and operational.

**Provisioning/Deployment**

Regarding the provisioning of servers, switches, routers and networking, tools must be used to automate the provisioning eliminating human error. For Infrastructure hardware resources, a set of recommendations is detailed in [7.2.1](./chapter07.md#7.2.1) to automate and secure their provisioning.

For OpenStack services and software components, deployment tools or components must be used to automate the deployment and avoid errors.  The deployment tool is a sensitive component storing critical information (deployment scripts, credentials…). 
The following rules must be applied:

- The boot of the server or the VM hosting the deployment tool must be protected
- Integrity of the deployment images must be checked, before starting deployment
- Deployment must be done through dedicated network (e.g. VLAN)
- When the deployment is finished, the deployment tool must be turned-off
- When the deployment is finished, the deployment tool must be turned-off, if the tool is only dedicated to deployment. Otherwise, any access to the deployment tool must be restricted.

Strict access permissions must be set on OpenStack configuration files.

**Configuration and management**

Configuration operations must be tracked (sec.mon.006, sec.mon.007). Events such as system access attempts, actions with high privileges, modification of configuration must be logged and exported on the fly to a distant storage. The communication channel used for log collection must be protected in integrity and confidentiality and logs protected against unauthorized modification (sec.mon.004).

Per sec.lcm.002 requirement, management protocols limiting security risks must be used such as SNMPv3, SSH v2, ICMP, NTP, syslog and TLS. How to secure logging is described in the following section. 

**Platform backup**

The storage for backup must be independent of storage offered to tenants. 

**Security upgrades**

To defend against virus or other attacks, security patches must be installed for firmware, OS, Hypervisor and OpenStack services according to their criticality.

<a name="6.3.7"></a>
### 6.3.7 Security Audit Logging
This intent of this section is to provide a key baseline and minimum requirements to implement logging that can meet the basic security auditing needs.  This should provide sufficient preliminary guidance, but is not intended to provide a comprehensive solution. Regular review of security logs that record user access, as well as session and network activity, is critical in preventing and detecting intrusions that could disrupt business operations. This monitoring process also allows administrators to retrace an intruder's activity and may help correct any damage caused by the intrusion. 

#### 6.3.7.1 Creating Logs
* All resources to which access is controlled, including but not limited to applications and operating systems must have the capability of generating security audit logs.
* Logs must be generated for all components (ex. Nova in Openstack) that form the NFVI.
* All security logging mechanisms must be active from system initialization. 
    *  These mechanisms include any automatic routines necessary to maintain the activity records and cleanup programs to ensure the integrity of the security audit/logging systems.

#### 6.3.7.2 What to Log / What NOT to Log
##### What to log
Where technically feasible the following system events must be recorded:
* Successful and unsuccessful login attempts
* Logoffs
* Successful and unsuccessful changes to a privilege level
* Successful and unsuccessful configuration changes
* Successful and unsuccessful security policy changes
* Starting and stopping of security logging
* Creating, removing, or changing the inherent privilege level of users
* Connections to a network listener of the resource
* Starting and stopping of processes including attempts to start unauthorised processes
* All command line activity performed by the following innate OS programs known to otherwise leave no evidence upon command completion including PowerShell on Windows systems (e.g. Servers, Desktops, and Laptops)
* Where technically feasible, any other security events should be recorded

##### What NOT to log
Security audit logs must NOT contain:
* Authentication credentials, even if encrypted (ex. password);
* Keystone Token;
* Proprietary or Sensitive Personal Information.

#### 6.3.7.3 Where to Log
* Where technically feasible, events MUST be recorded on the device (e.g. VM, physical node, etc.) where the event occurs. 
* Where it is not technically feasible to record the event on the resource on which it occurs, then the operational use of another resource like a centralized log repository must record the event in a manner where the event can be linked to the resource on which it occurred.

#### 6.3.7.4 Required Fields
The security audit log must contain at minimum the following fields (where applicable and technically feasible): 
* Event type
* Date/time
* Protocol
* Service or program used for access
* Success/failure
* Login ID — Where the Login ID is defined on the system/application/authentication server; otherwise, the field should contain 'unknown', in order to protect authentication credentials accidentally entered at the Login ID prompt from appearing in the security audit log.
* Source IP Address

#### 6.3.7.5 Data Retention 
* Log files must be retained for 180 days, or the relevant regulator mandate, or your customer mandate, whichever is higher.
* Implementation and monitoring: after 180 days or your mandated retention period, security audit logs must be destroyed.

#### 6.3.7.6 Security Logs Time Synchronisation
The host and various system clocks be synchronized with the NTP server (sec.mon.002). In any time synchronisation, we need to specify the synchronization interval and the tolerance where the latter specifies the permissible difference the local time cane out of synch.

Whenever the time synchronisation forces the local time to change or the use of another NTP server, the change details must be logged including time server source, time, date and time zones (sec.mon.003).
