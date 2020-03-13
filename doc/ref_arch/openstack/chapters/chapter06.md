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
 * [6.3.7 Monitoring and Security Audit](#6.3.7)

## 6.1 Introduction

This guide is intended to provide basic security requirements to CNTT architects who are looking to implementing NFVi using [OpenStack](https://www.openstack.org/) technology.  This is minimal set of high-level general security practice, not intended to cover all implementation scenarios.  Please ensure to also reference your enterprise security and compliance requirements in addition to this guide.

<a name="6.2"></a>
## 6.2 Security Requirements

Based on chapter 2 requirements

<a name="6.3"></a>
## 6.3 NFVi and VIM Security

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


#### 6.3.1.5 Secrets management (Barbican)


<a name="6.3.2"></a>
