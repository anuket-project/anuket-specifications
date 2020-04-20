[<< Back](../../openstack)

# 6. Security
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

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

This guide is intended to provide basic security requirements to CNTT architects who are looking to implementing NFVI using [OpenStack](https://www.openstack.org/) technology.  This is minimal set of high-level general security practice, not intended to cover all implementation scenarios.  Please ensure to also reference your enterprise security and compliance requirements in addition to this guide.

<a name="6.2"></a>
## 6.2 Security Requirements

Based on chapter 2 requirements

<a name="6.3"></a>
## 6.3 NFVI and VIM Security

OpenStack security guide:
https://docs.openstack.org/security-guide/introduction/introduction-to-openstack.html

<a name="6.3.1"></a>
### 6.3.1 Platform Access

#### 6.3.1.1 Identity
The OpenStack Identity service (Keystone) provides identity, token, catalog, and policy services for use specifically by services in the OpenStack family. Identity service is organized as a group of internal services exposed on one or many endpoints. Many of these services are used in a combined fashion by the front end.

OpenStack Keystone could work with an Identity service that your enterprise may already have, such as LDAP with Active Directory.  In those cases, the recommendation is to integrate Keystone with the cloud provider's Identity Services.  

#### 6.3.1.2 Authentication
Authentication is the first line of defense for any real-world implementation of OpenStack.  At its core, authentication is the process of confirming the user logging in is who they claim to be.  OpenStack Keystone supports multiple methods of authentication, such as username/password, LDAP, and others.  For more details, please refer to [OpenStack Authentication Methods](https://docs.openstack.org/security-guide/identity/authentication-methods.html)

##### Keystone Tokens
Once a user is authenticated, a token is generated for authorization and access to an OpenStack environment and resources.  By default, the token is set to expire in one hour.  This setting could be change based on the business and operational needs, but it's highly recommended to set the expiration to the shortest possible value without dramatically impacting your operations.

<b>Special Note on Logging Tokens:</b> since the token would allow access to the OpenStack services, it <i>MUST</i> be masked before outputting to any logs.

#### 6.3.1.3 Authorization
Authorization serves as the next level of defense.  At its core, it checks if the authenticated users have the permission to execute an action. Most Identity Service supports the notion of groups and roles. A user belongs to groups and each group has a list of roles that permits certain action on certain resource. OpenStack services reference the roles of the user attempting to access the service. OpenStack policy enforcer middleware takes into consideration the policy rules associated with each resource then the user’s group/roles and association to determine if access can the requested resource.  For more details on policies, please refer to the [OpenStack Policies](https://docs.openstack.org/security-guide/identity/policies.html#policy-section).

#### 6.3.1.4 RBAC
In order to properly manage user access to OpenStack services, service provider should utilize the Role Based Access Control (RBAC) system.  Based on the OpenStack Identify Service (Keystone v3) Group and Domain component, the RBAC system implements a set of access roles that accommodate most use cases. Operations staff can create users and assign them to roles using standard OpenStack commands for users, groups, and roles.

###### Rules
The following rules govern create, read, update, and delete (CRUD) level access.

<ul>
 <li><i>_member_</i> can create, read, update, and delete the resources defined at the tenant level.</li>
 <li><i>support_member</i> can create and read the resources defined at the tenant level.</li>
 <li><i>viewer</i> can read the resources defined at the tenant level.</li>
 <li><i>admin</i> can create, read, update, and delete all resources.</li>
</ul>

###### Recommended Default Roles to Start
</ul>
 <li><b>site_admin</b> (HIGHLY RESTRICTED) </li>
 <ul>
  <li>Site Level Super Admin - usually assign to Operation Staffs who already have root level access to hosts</li>
  <li>Permission to create/read/update/delete all tenants and resources at the site, including creating snapshot and upload public images</li>
  <li>Limited ability to create/read/update/delete tenant projects</li>
 </ul>
  
 <li><b>site_admin_support</b></li>
 <ul>
  <li>Site Level Admin - usually assign to Operation Staffs who need to manage resource except delete </li>
  <li>Permission to create/read/update all tenants and resources at the site</li>
  <li>Cannot create snapshots</li>
 </ul>

 <li><b>site_admin_viewer</b></li>
 <ul>
  <li>Site Level Admin Read Only - usually assign to groups who need to view all resources, such as Capacity Planners</li>
  <li>Permission to read all tenants and resources at the site</li>
  <li>Cannot create/update/delete </li>
 </ul>

 <li><b>site_image_manager</b></li>
 <ul>
  <li>Site wide admin level privileges to Glance API (via CLI)</li>
  <li>Restricted to Image team</li>
 </ul>
  
 <li><b>tenant_member</b></li>
 <ul>
  <li>Tenant Level Admin - typically assign to majority of tenant users to manage their resources</li>
  <li>Permission to create/read/update/delete to all resources at the tenant project level</li>
  <li>Cannot upload image or create snapshot</li>
  <li>Cannot touch any other tenant except the one the role is located</li>
 </ul>

 <li><b>tenant_snapshot_member</b></li>
 <ul>
  <li>Tenant Level Admin with Snapshot - typically assign to tenant users who needs to create snapshot via special request to Operations Staff</li>
  <li>Permission is same as tenant_member except the user can also create snapshots</li>
 </ul>

 <li><b>tenant_support_member</b></li>
 <ul>
  <li>Tenant Level Support - typically assign to tenant users who needs to create resource in the project space</li>
  <li>Permission to create/read all resources at the tenant project level</li>
  <li>Cannot update/delete or create snapshots</li>
 </ul>
 
 <li><b>tenant_viewer</b></li>
 <ul>
  <li>Tenant Level Read Only - typically assign to tenant users who needs to read all resource in the project space</li>
  <li>Permission to read all resources at the tenant level</li>
  <li>Cannot create/update/delete</li>
 </ul>
</ul>

<a name="6.3.2"></a>
### 6.3.2 System Hardening

<a name="6.3.3"></a>
### 6.3.3 Confidentiality and Integrity

<a name="6.3.4"></a>
### 6.3.4 Workload Security

OpenStack segregates its infrastructure (for example, hosts) by Regions, Host aggregates and Availability Zones (AZ). Workloads can also be segregated by server groups (affinity and non-affinity groups). These options support the workloads placement requirement _sec.wl.001_.

Separation of non-production and production workloads, or by workload category (for example, payment card information, healthcare, etc.) requires separation through server groups (Regions, AZs) but also requires network and storage segregation as in Regions but also AZs if engineered to do so. Thus, the separation of these workloads is handled through placement of workloads in separate AZs and/or Regions (_sec.wl.005_ and _sec.wl.006_).

Regions also support the _sec.wl.004_ requirement for separation by Location (for example, country).

Operational security (_sec.wl.002_) is handled through a combination of mechanisms including the above and security groups. Security groups limit the types of traffic that have access to instances. One or more security groups can be automatically assigned to an instance at launch. The rules associated with a security group control the incoming traffic.  Any incoming traffic not matched by a rule is denied access. The security group rules govern access through the setting of different parameters: traffic source, protocols and destination port on a VM.  Errors in provisioning/managing OpenStack Security Groups can lead to non-functioning applications and can take a long time to identify faults and correct them.  Thus, use of tools for auto provisioning and continued inspection of security groups and network policies is required.

Given the rate of change in the workload development and deployment, and the cloud environment itself, _sec.wl.003_ requires that the workloads should be assessed during the CI/CD process as the images are created and then whenever they are deployed. In addition, the infrastructure must be configured for security as discussed elsewhere in this chapter including secure boot. 

<a name="6.3.4.1"></a>
### 6.3.4.1 SR-IOV and DPDK Considerations

SR-IOV agent only works with NoopFirewallDriver when Security Groups are enabled, but can still use other firewall_driver for other Agents by updating their conf with the requested firewall driver." Please see [SR-IOV Passthrough for Networking](https://wiki.openstack.org/wiki/SR-IOV-Passthrough-For-Networking).

Operators typically do not implement Security Groups when ussing SR-IOV or DPDK networking technologies.

<a name="6.3.5"></a>
### 6.3.5 Image Security

<a name="6.3.6"></a>
### 6.3.6 Security LCM

<a name="6.3.7"></a>
### 6.3.7 Security Audit Logging
This intent of this section is to provide key baseline and minimal requirement to implement logging that would meet the basic security auditing needs.  This  should provide sufficient preliminary guidance, but is not intended to provide a comprehensive solution.  Regular review of security logs that record user access, as well as session and network activity, is critical in preventing and detecting intrusions that could disrupt business operations. This monitoring process also allows administrators to retrace an intruder's activity and may help correct any damage caused by the intrusion. 

#### 6.3.7.1 Creating Logs
* All resources to which access is controlled, including but not limited to applications and operating systems must have the capability of generating security audit logs.
* Logs must be generated for any component (ex. Nova in Openstack) that form the NFVI.
* All security logging mechanisms must be active from system initialization. 
    *  These mechanisms include any automatic routines necessary to maintain the activity records and cleanup programs to ensure the integrity of the security audit/logging systems.

#### 6.3.7.2 What to Log / What NOT to Log
##### What to log
Where technically feasible the following system events must be recorded:
* Successful and unsuccessful login attempts
* Logoffs
* Successful and unsuccessful changes to a privilege level
* Starting and stopping of security logging
* Creating, removing, or changing the inherent privilege level of users
* Connections to a network listener of the resource
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
