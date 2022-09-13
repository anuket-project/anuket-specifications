Security
========


This guide is intended to provide basic security requirements to
architects who are implementing Cloud Infrastructure using
OpenStack :cite:p:`openstack` technology. This is a minimal
set of high-level general security practices, not intended to cover all
implementation scenarios. Please ensure to also reference your
enterprise security and compliance requirements in addition to this
guide.

Security Requirements
---------------------

The sections :ref:`chapters/chapter02:cloud infrastructure security requirements`
and :ref:`chapters/chapter02:security recommendations` gather
all the requirements and recommendations regarding security topics developed
in this chapter.

Cloud Infrastructure and VIM Security
-------------------------------------

In the "Security boundaries and threats" section :cite:p:`openstacksecb`
of the OpenStack security guide :cite:p:`openstacksecg`,
there is extensive description on security domains, threat
classifications, and attack vectors. The following only touches on some
of the topics and at a high level.

System Hardening
~~~~~~~~~~~~~~~~

All infrastructure components should undergo system hardening, establish
processes to govern the hardening, and documents to cover at a minimal
for the following areas.

Server boot hardening
^^^^^^^^^^^^^^^^^^^^^

Server boot process must be trusted. For this purpose, the integrity and
authenticity of all BIOS firmware components must be verified at boot.
Per sec.gen.003 requirement, Secure Boot based on UEFI must be used. By
verifying the signatures of all BIOS components, Secure Boot will ensure
that servers start with the firmware expected and without malware
insertion into the system. Secure Boot checks the digital signatures
locally. To implement a chain of trust, Secure Boot must be complemented
by the use of a hardware based Root of Trust provided by a TPM (Trusted
Platform Module).

System Access
^^^^^^^^^^^^^

Access to all the platform's components must be restricted (sec.gen.013)
applying the following rules:

-  Remove, or at a minimum disable all unnecessary user accounts
-  Change all default user accounts where technically feasible
-  Change all default credentials
-  Prohibit logging with root account when root privileges are not
   required (sec.gen.006)
-  Restrict access according to only those protocols/service/address
   adhering to the Principle of Least Privilege
-  The same authentication credentials must not be reused on different
   components (sec.sys.011)
-  Restrict access to Operating System (sec.gen.005)

Password policy
^^^^^^^^^^^^^^^

For all infrastructure components, passwords must be hardened, and a
strict password policy must be applied (sec.gen.002).

Passwords must be strengthened:

-  All vendors' default passwords must be changed
-  Passwords must contain at least 8 characters as a minimal value, 14
   characters length passwords are recommended
-  Passwords must contain at least one upper case letter, one lower case
   letter and one non-alphabetic character
-  For administration privileges accounts, passwords must contain at
   least one upper case letter, one lower case letter, one numeral and
   one special (non-alphanumeric) character

For passwords updates, the identity of users must be verified before
permitting a password change.

Passwords must be encrypted at rest and in-transit. Password files must
be stored separately from application system data.

Password's composition, complexity and policy should follow the
recommendations consolidated within the CIS Password Policy
guide :cite:p:`cispwd` such as:

-  Check the password for known bad passwords (repetitive or sequential
   characters, dictionary words, context-specific words, previously used
   passwords, etc.)
-  Limit number of failed login attempts
-  Implement Multi-factor Authentication
-  Periodic (for example, Yearly, Quarterly, etc.) password change or on
   key events such as indication of compromise, change of user roles, a
   defined period of inactivity, when a user leaves the organisation,
   etc.

Function and Software
^^^^^^^^^^^^^^^^^^^^^

Infrastructure must be implemented to perform the minimal functions
needed to operate the Cloud Infrastructure.

Regarding software (sec.gen.004):

-  Install only software which is required to support the functions
-  Remove any unnecessary software or packages
-  Where software cannot be removed, disable all services to it

Patches
^^^^^^^

All deployed Cloud Infrastructure software must be audited and must be
implemented to allow installation of the latest patches to address
security vulnerabilities in the following timescale from discovery
(sec.gen.008, sec.lcm.011):

.. table:: Time to Remediate
   :widths: auto

   +----------+-------------------------+
   | Severity | Time to Remediate       |
   +==========+=========================+
   | Zero-Day | Immediately or as soon  |
   |          | as practically possible |
   +----------+-------------------------+
   | Critical | 30 days                 |
   +----------+-------------------------+
   | High     | 60 days                 |
   +----------+-------------------------+
   | Medium   | 90 days                 |
   +----------+-------------------------+
   | Low      | 180 days                |
   +----------+-------------------------+

**See** Common Vulnerability Scoring System :cite:p:`cve`
and NIST Vulnerability Metrics :cite:p:`nistvm`.

Network Protocols
^^^^^^^^^^^^^^^^^

-  Only allow protocols that are required by the system functions
   (sec.sys.002)
-  Tighten all required TCP/IP (Transmission Control Protocol/Internet
   Protocol) services

Anti-Virus and Firewall
^^^^^^^^^^^^^^^^^^^^^^^

-  Install and run your Enterprise approved anti-virus software/
   intrusion protection/ malware/ spyware endpoint security software
   with up-to-date profiles; minimal daily refresh
-  Install and run firewall software where applicable

Vulnerability Detection and Prevention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Implement DoS (Denial of Service) protection where applicable
-  Ensure logging and alerting is actively running
-  Run host-based scanning and fix all findings per vulnerability
   severity
-  Run network-based scanning and fix all findings per vulnerability
   severity

Platform Access
~~~~~~~~~~~~~~~

Identity Security
^^^^^^^^^^^^^^^^^

The OpenStack Identity service (Keystone) :cite:p:`openstackseci`
provides identity, token, catalog, and policy services for use
specifically by services in the OpenStack family. Identity service is
organised as a group of internal services exposed on one or many
endpoints. Many of these services are used in a combined fashion by the
front end (sec.sys.006).

OpenStack Keystone can work with an Identity service that your
enterprise may already have, such as LDAP with Active Directory. In
those cases, the recommendation is to integrate Keystone with the cloud
provider's Identity Services.

Authentication
^^^^^^^^^^^^^^

Authentication is the first line of defence for any real-world
implementation of OpenStack. At its core, authentication is the process
of confirming the user logging in is who they claim to be. OpenStack
Keystone supports multiple methods of authentication, such as
username/password, LDAP, and others. For more details, please refer to
OpenStack Authentication Methods :cite:p:`openstackaut`.

Limiting the number of repeated failed login attempts (configurable)
reduces the risk of unauthorised access via password guessing (Bruce
force attack) - sec.mon.006. The restriction on the number of
consecutive failed login attempts ("lockout_failure_attempts") and any
actions post such access attempts (such as locking the account where the
"lockout_duration" is left unspecified) should abide by the operator's
policies. For example, an operator may restrict the number of
consecutive failed login attempts to 3 ("lockout_failure_attempts = 3")
and lock the account preventing any further access and where the account
is unlocked by getting necessary approvals.

Keystone Tokens
'''''''''''''''

Once a user is authenticated, a token is generated for authorisation and
access to an OpenStack environment and resources. By default, the token
is set to expire in one hour. This setting can be changed based on the
business and operational needs, but it's highly recommended to set the
expiration to the shortest possible value without dramatically impacting
your operations.

**Special Note on Logging Tokens:** since the token would allow access
to the OpenStack services, it *MUST* be masked before outputting to any
logs.

Authorisation
^^^^^^^^^^^^^

Authorisation serves as the next level of defence. At its core, it
checks if the authenticated users have permission to execute an
action. Most Identity Services support the notion of groups and roles. A
user belongs to groups and each group has a list of roles that permits
certain actions on certain resources. OpenStack services reference the
roles of the user attempting to access the service. OpenStack policy
enforcer middleware takes into consideration the policy rules associated
with each resource and the user's group/roles and association to
determine if access will be permitted for the requested resource. For
more details on policies, please refer to the OpenStack
Policies :cite:p:`openstackpol`.

RBAC
^^^^

In order to properly manage user access to OpenStack services, service
providers must utilise the Role Based Access Control (RBAC) system
(sec.sys.001, sec.sys.007). Based on the OpenStack Identify Service
(Keystone v3) Group and Domain component, the RBAC system implements a
set of access roles that accommodate most use cases. Operations staff
can create users and assign them to roles using standard OpenStack
commands for users, groups, and roles.

Keystone provides three default roles :cite:p:`openstackdr`
admin, member, and reader. As of Train release, Keystone applies the
following personas consistently across its API.

-  The reader role provides read-only access to resources within the
   system, a domain, or a project.
-  The member role, same as reader in Keystone,
   introduces granularity between admin and reader to other OpenStack
   services.
-  The admin role is reserved for the most privileged operations within
   a given scope for managing resources.

For specific use-case, policies can be overridden, and new roles can be
created for each OpenStack service by editing the policy.json file.

Rules
'''''

The following rules govern create, read, update, and delete (CRUD) level
access.

-  *member* can create, read, update, and delete the resources defined
   at the tenant level.
-  *support_member* can create and read the resources defined at the
   tenant level.
-  *viewer* can read the resources defined at the tenant level.
-  *admin* can create, read, update, and delete all resources.

Recommended Default Roles to Start
''''''''''''''''''''''''''''''''''

**site_admin** (HIGHLY RESTRICTED)

-  *Site Level Super Admin* - usually assign to Operation Staffs who
   already have root level access to hosts
-  Permission to create/read/update/delete all tenants and resources at
   the site, including creating snapshot and upload public images
-  Limited ability to create/read/update/delete tenant projects

**site_admin_support**

-  *Site Level Admin* - usually assign to Operation Staffs who need to
   manage resource except delete
-  Permission to create/read/update all tenants and resources at the
   site
-  Cannot create snapshots

**site_admin_viewer**

-  *Site Level Admin Read Only* - usually assigned to groups who need to
   view all resources, such as Capacity Planners
-  Permission to read all tenants and resources at the site
-  Cannot create/update/delete

**site_image_manager**

-  Site wide admin level privileges to Glance API (via CLI)
-  Restricted to Image team

**tenant_member**

-  *Tenant Level Admin* - typically assigned to majority of tenant users
   to manage their resources
-  Permission to create/read/update/delete to all resources at the
   tenant project level
-  Cannot upload image or create snapshot
-  Cannot touch any other tenant except the one the role is located

**tenant_snapshot_member**

-  *Tenant Level Admin with Snapshot* - typically assigned to tenant users
   who need to create snapshot via special request to Operations Staff
-  Permission is same as tenant_member except the user can also create
   snapshots

**tenant_support_member**

-  *Tenant Level Support* - typically assigned to tenant users who need to
   create resource in the project space
-  Permission to create/read all resources at the tenant project level
-  Cannot update/delete or create snapshots

**tenant_viewer**

-  *Tenant Level Read Only* - typically assigned to tenant users who need
   to read all resources in the project space
-  Permission to read all resources at the tenant level
-  Cannot create/update/delete

Confidentiality and Integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confidentiality implies that data and resources must be protected
against unauthorised introspection/exfiltration. Integrity implies that
the data must be protected from unauthorised modifications or deletions.

Regarding confidentiality and integrity in Cloud Infrastructure, 2 main
concerns are raised:

-  confidentiality and integrity of the Cloud Infrastructure components
   (networks, hypervisor, OpenStack services)
-  confidentiality and integrity of the tenant's data

The Cloud Infrastructure must also provide the mechanism to identify
corrupted data.

Confidentiality and Integrity of communications (sec.ci.001)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is essential to secure the infrastructure from external attacks. To
counter this threat, API endpoints exposed to external networks must be
protected by either a rate-limiting proxy or web application firewall
(WAF), and must be placed behind a reverse HTTPS proxy (sec.mon.008).
Attacks can also be generated by corrupted internal components, and for
this reason, it is security best practice to ensure integrity and
confidentiality of all network communications (internal and external) by
using Transport Layer Security (TLS) protocol (sec.sys.003,
sec.sys.004). When using TLS, according to the OpenStack security
guide :cite:p:`openstackseccom`
recommendation, the minimum version to be used is TLS 1.2.

3 categories of traffic will be protected using TLS:

-  traffic from and to external domains
-  communications between OpenStack components (OpenStack services, Bus
   message, Data Base)
-  management traffic

Certificates used for TLS encryption must be compliant with X.509
standards and be signed by a trusted authority (sec.sys.017). To issue
certificates for internal OpenStack users or services, the cloud
provider can use a Public Key Infrastructure (PKI) with its own internal
Certification Authority (CA), certificate policies, and management.

Integrity of OpenStack components configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The cloud deployment components/tools store all the information required
to install the infrastructure including sensitive information such as
credentials. It is recommended to turn off deployment components after
deployment to minimise the attack surface area, limit the risk of
compromise, and to deploy and provision the infrastructure through a
dedicated network (VLAN).

Configuration files contain sensitive information. These files must be
protected from malicious or accidental modifications or deletions by
configuring strict access permissions for such files. All access failed
attempts to change and all changes (pre-change, post-change and by who)
must be securely logged, and all failed access and failed changes must
be alerted on (sec.mon.005).

The Cloud Infrastructure must provide the mechanisms to identify
corrupted data (sec.gen.009):

-  the integrity of configuration files and binaries must be checked by
   using cryptographic hash
-  it is recommended to run scripts (such as checksec.sh) to verify the
   properties of the QEMU/KVM
-  it is recommended to use tools such as CIS-CAT (Center for Internet
   security- Configuration Assessment Tool :cite:p:`ciscat`)
   to check the compliance of systems configuration against respective
   CIS benchmarks :cite:p:`cisben`.

It is strongly recommended to protect all repositories, such as Linux
repositories and Docker registries, against the corruption of their data
and unauthorised access, by adopting protection measures such as hosting
a local repository/registry with restricted and controlled access, and
using TLS (sec.img.004, sec.img.005, sec.img.006). This
repository/registry must contain only signed images or packages.

Confidentiality and Integrity of tenant data (sec.ci.001)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tenant data are forwarded unencrypted over the network. Since the VNF is
responsible for its security, it is up to the VMs to establish secure
data plane, e.g., using IPsec over its tenant network.

A Cloud actor must not be able to retrieve secrets used by VNF managers.
All communications between the VNFM or orchestrator, and the
infrastructure must be protected in integrity and confidentiality (e.g.,
by using TLS) and controlled via appropriate IP filtering rules
(sec.lcm.006).

The Cloud Infrastructure must onboard only trusted and verified VM
images, implying that VNF vendors provide signed images (sec.img.001);
images from non-trusted sources may contain security breaches or
unsolicited malicious code (spoofing, information disclosure). It is
recommended to scan all VM images with a vulnerability
scanner(sec.img.002). The scan is mandatory for images from unknown or
untrusted sources.

To mitigate tampering attacks, it is recommended to use the Glance
image signing feature :cite:p:`openstackisv`
to validate an image when uploading. In this case, Barbican service must
be installed.

In order to protect data, VNFs must encrypt the volumes they use. In
this case, the encryption key must not be stored on the infrastructure.
When a key management service is provided by the infrastructure,
OpenStack can encrypt data on behalf of tenants (sec.gen.010). It is
recommended to rely on Barbican, as the key manager service of
OpenStack.

Workload Security
~~~~~~~~~~~~~~~~~

OpenStack segregates its infrastructure (sec.ci.008) (for example,
hosts) by Regions, Host Aggregates and Availability Zones (AZ).
Workloads can also be segregated by server groups (affinity and
non-affinity groups) (sec.sys.008). These options support the workloads
placement requirement (sec.wl.001, sec.wl.004).

Separation of non-production and production workloads, or by workload
category (for example, payment card information, healthcare, etc.)
requires separation through server groups (for example, Regions, AZs),
but also requires network and storage segregation as in Regions. Thus,
the separation of these workloads is handled through placement of
workloads in separate AZs and/or Regions (sec.wl.005 and sec.wl.006).

Regions also support the sec.wl.004 requirement for separation by
Location (for example, country).

Operational security is handled through a combination of mechanisms
including the above and security groups (sec.sys.002). Security groups
limit the types of traffic that have access to instances. One or more
security groups can be automatically assigned to an instance at launch.
The rules associated with a security group control the incoming traffic.
Any incoming traffic not matched by a rule is denied access. The
security group rules govern access through the setting of different
parameters: traffic source, protocols and destination port on a VM.
Errors in provisioning/managing OpenStack Security Groups can lead to
non-functioning applications, and it can take a long time to identify
faults and correct them. Thus, the use of tools for auto provisioning
and continued inspection of security groups and network policies is
required.

Given the rate of change in the workload development and deployment, and
the cloud environment itself, sec.wl.003 requires that the workloads
must be assessed during the CI/CD process as the images are created and
then whenever they are deployed. In addition, the infrastructure must be
configured for security as discussed elsewhere in this chapter including
secure boot.

SR-IOV and DPDK Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SR-IOV agent only works with NoopFirewallDriver when Security Groups
are enabled, but can still use other firewall_driver for other Agents by
updating their conf with the requested firewall driver. Please see
SR-IOV Passthrough for Networking :cite:p:`openstacksr`.

Operators typically do not implement Security Groups when using SR-IOV
or DPDK networking technologies.

Image Security
~~~~~~~~~~~~~~

Images from untrusted sources must not be used (sec.img.001). Valuable
guidance on trusted image creation process and image signature
verification is provided in the "Trusted Images" section of the
OpenStack Security Guide :cite:p:`openstackti`.
The OpenStack Security Guide includes reference to the "OpenStack
Virtual Machine Image Guide :cite:p:`openstackim`" that describes how
to obtain, create, and modify OpenStack compatible virtual machine
images.

Images to be ingested, including signed images from trusted sources,
need to be verified prior to ingestion into the Image Service (Glance)
(sec.gen.009). The operator will need toolsets for scanning images,
including for virus and malware detection (sec.img.002). Adding Signed
Images to the Image Service (Glance) is specified in OpenStack
Operations Guide :cite:p:`openstackasi`.
Image signing and verification protects image integrity and authenticity
by enabling deployers to sign images and save the signatures and public
key certificates as image properties. The creation of signature per
individual artifact in the VNF package is required by ETSI NFV
SOL004 :cite:p:`etsisol4`.

The chain of trust requires that all images are verified again in the
Compute service (Nova) prior to use. Integrity verification at the time
of instantiation is required by ETSI NFV
SEC021 :cite:p:`etsisec21`.

Images must be also updated to benefit from the latest security patches
(sec.gen.008, sec.img.007).

Security LCM
~~~~~~~~~~~~

Cloud Infrastructure LCM encompasses provisioning, deployment,
configuration and management (resources scaling, services upgrades,
etc.) as described in
:ref:`chapters/chapter07:operations and life cycle management`.
These operations must be securely performed in order to keep the
infrastructure safe and operational (sec.lcm.003).

**Provisioning/Deployment**

Regarding the provisioning of servers, switches, routers and networking,
tools must be used to automate the provisioning eliminating human error.
For Infrastructure hardware resources, a set of recommendations is
detailed in :ref:`chapters/chapter07:underlying resources provisioning`
to automate and secure their provisioning (sec.lcm.001).

For OpenStack services and software components, deployment tools or
components must be used to automate the deployment and avoid errors. The
deployment tool is a sensitive component storing critical information
(deployment scripts, credentials, etc.). The following rules must be
applied:

-  The boot of the server or the VM hosting the deployment tool must be
   protected
-  Integrity of the deployment images must be checked, before starting
   deployment
-  Deployment must be done through a dedicated network (e.g. VLAN)
-  When the deployment is finished, the deployment tool must be
   turned-off, if the tool is only dedicated to deployment. Otherwise,
   any access to the deployment tool must be restricted.
-  Strict access permissions must be set on OpenStack configuration
   files.

**Configuration and management**

Configuration operations must be tracked (sec.gen.015, sec.mon.006,
sec.mon.007). Events such as system access attempts, actions with high
privileges, modification of configuration, must be logged and exported
on the fly to a non-local storage. The communication channel used for
log collection must be protected for integrity and confidentiality, and
the logs protected against unauthorised modification (sec.mon.004).

Per sec.sys.0016 and sec.lcm.002 requirements, management protocols
limiting security risks must be used such as SNMPv3, SSH v2, ICMP, NTP,
syslog and TLS. How to secure logging is described in the following
section.

**Platform backup**

The storage for backup must be independent of storage offered to
tenants.

**Security upgrades**

To defend against virus or other attacks, security patches must be
installed for firmware, OS, Hypervisor and OpenStack services according
to their criticality.

Monitoring and Security Audit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The intent of this section is to provide a key baseline and minimum
requirements to implement logging that can meet the basic monitoring and
security auditing needs. This should provide sufficient preliminary
guidance, but is not intended to provide a comprehensive solution.
Regular review of security logs that record user access, as well as
session (sec.mon.010) and network activity (sec.mon.012), is critical in
preventing and detecting intrusions that could disrupt business
operations. This monitoring process also allows administrators to
retrace an intruder's activity and may help correct any damage caused by
the intrusion (sec.mon.011).

The logs have to be continuously monitored and analysed with alerts
created for anomalies (sec.lcm.005). The resources for logging,
monitoring and alerting also need to be logged and monitored, and
corrective actions taken so that they are never short of the needed
resources (sec.mon.015).

Creating Logs
^^^^^^^^^^^^^

-  All resources to which access is controlled, including but not
   limited to applications and operating systems, must have the
   capability of generating security audit logs (sec.mon.001).
-  Logs must be generated for all components (e.g., Nova in OpenStack)
   that form the Cloud Infrastructure (sec.mon.001).
-  All security logging mechanisms must be active from system
   initialisation (sec.mon.018):

   -  These mechanisms include any automatic routines necessary to
      maintain the activity records and clean-up programs to ensure the
      integrity of the security audit/logging systems.

-  Logs must be time synchronised (sec.mon.002).

What to Log / What NOT to Log
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What to log
'''''''''''

Where technically feasible the following system events must be recorded
(sec.mon.005):

-  Successful and unsuccessful login attempts including:

   -  Command line authentication (i.e., when initially getting token
      from keystone)
   -  Horizon authentication
   -  SSH authentication and sudo on the computes, controllers, network
      and storage nodes

-  Logoffs

-  Successful and unsuccessful changes to a privilege level
   (sec.lcm.012)

-  Successful and unsuccessful configuration changes

-  Successful and unsuccessful security policy changes

-  Starting and stopping of security logging

-  Creating, removing, or changing the inherent privilege level of users
   (sec.lcm.012)

-  Connections to a network listener of the resource

-  Starting and stopping of processes including attempts to start
   unauthorised processes

-  All command line activity performed by the following innate OS
   programs known to otherwise leave no evidence upon command completion
   including PowerShell on Windows systems (e.g., Servers, Desktops, and
   Laptops)

-  Where technically feasible, any other security events should be
   recorded

What NOT to log
'''''''''''''''

Security audit logs must NOT contain:

-  Authentication credentials, even if encrypted (e.g., password)
   (sec.mon.019);
-  Keystone Token;
-  Proprietary or Sensitive Personal Information.

Where to Log
^^^^^^^^^^^^

-  The logs must be stored in an external system (sec.mon.018), in a
   manner where the event can be linked to the resource on which it
   occurred.
-  Where technically feasible, events must be recorded on the device
   (e.g. VM, physical node, etc.) where the event occurs, if the
   external logging system is not available (sec.mon.021).
-  Security audit logs must be protected in transit and at rest
   (sec.mon.004).

Required Fields
^^^^^^^^^^^^^^^

The security audit log must contain at minimum the following fields
(sec.mon.001) where applicable and technically feasible:

-  Event type
-  Date/time
-  Protocol
-  Service or program used for access
-  Success/failure
-  Login ID — Where the Login ID is defined on the
   system/application/authentication server; otherwise, the field should
   contain ‘unknown', in order to protect authentication credentials
   accidentally entered at the Login ID prompt from appearing in the
   security audit log.
-  Source and destination IP Addresses and ports

Data Retention
^^^^^^^^^^^^^^

-  Log files must be retained for 180 days, or the relevant regulator
   mandate, or your customer mandate, whichever is higher (sec.mon.020).
-  Implementation and monitoring: after 180 days or your mandated
   retention period, security audit logs must be destroyed.

Security Logs Time Synchronisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The host and various system clocks must be synchronised with an
authenticated time service/NTP server (sec.gen.007).

For time synchronisation, we need to specify the synchronisation
interval and the tolerance where the latter specifies the permissible
difference the local time can be out of synchronisation. Whenever the
time synchronisation forces the local time to change or the use of
another NTP server, the change details must be logged including time
server source, time, date and time zones (sec.mon.003).
