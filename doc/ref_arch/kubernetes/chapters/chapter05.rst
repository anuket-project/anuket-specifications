Security Guidance
=================

Introduction to Security Guidance
---------------------------------

Securing Kubernetes requires several layers of security features to provide end
to end security for cloud native applications. It is recommended that:

-  Security testing is fully integrated into the CI/CD pipelines of all parties
   (e.g., vendors and operators).
-  Automated security policies are used to flag builds with issues.
-  Image registries are monitored to automatically block or replace images with
   known vulnerabilities, while also ensuring policies are used to gate what can
   be deployed and who can deploy from the registry.
-  Adopt a layered packaging model which supports separation of concerns during
   image build.

The following functionalities are recommended for securing Kubernetes platforms:

-  Image Certification (Scan for vulnerabilities) and Signing
-  Role-base Access Control (RBAC)
-  Secret Management
-  How to overcome the lack of hard Kubernetes Cluster Multi-tenancy

   -  Tenants without hard multi-tenancy requirements (multiple development teams
      in the same organisation) separated from each other by Namespaces
   -  For strict multi tenancy, a dedicated Kubernetes Cluster per tenant should
      be used

-  Integration with other security ecosystem like monitoring and alerting tools

Security Perimeters
~~~~~~~~~~~~~~~~~~~

When applications or workloads run on Kubernetes, there are several layers which
come into picture that govern the security. Each of these layers needs to be
secured within their perimeters. The various layers that come into picture are:

-  **Container Registry**: A container registry is a repository to manage
   container images. The access to container registry needs to be secured in
   order to prevent unauthorised access or image tampering.
-  **Container Images**: Stored instance of a container that holds a set of
   software needed to run an application. Before loading them to a container
   registry, they need to be secured by performing various checks like
   vulnerability analysis, scans etc. These images should also be signed from
   trusted sources.
-  **Containers**: A lightweight and portable executable image that contains
   software and all of the dependencies. The containers need to be prevented from
   accessing the underlying OS capabilities like loading of kernel modules, mounting of
   directories of the underlying OS, etc., and running in
   privileged mode.
-  **Pods**: A Pod represents a set of running containers on a Kubernetes Cluster.
   Kubernetes inherently offers a PodSecurity admission controller that define a set of
   conditions that a pod needs to run with in order to be accepted into the
   system. These policies help in ensuring the necessary checks for running the
   pods.
-  **Kubernetes Node**: A Kuberentes (worker) Node is a physical or virtual server running the workloads in a Kubernetes
   Cluster. A Kubernetes node in an unsecured boundary can lead to a potential threat to the running workloads. Such a
   node should be hardened by disabling unused ports, prohibiting root access etc.
-  **Kubernetes Control Plane Node**: A control plane node in an unsecured boundary can lead to a
   potential threat to the running workloads. A control plane may be hardened in terms
   of security by disabling unused ports, prohibiting root access etc.
-  **Kubernetes Control Plane**: The container orchestration layer that exposes
   the API and interfaces to define, deploy, and manage the lifecycle of
   containers. The communication over these APIs needs to be secured via
   different mechanisms like TLS encryption, API authentication via LDAP etc.

Security Principles
-------------------

The following are core principles to consider when securing cloud native
applications:

-  Deploy only secure and trusted applications and codes
-  Only deploy applications from validated and verified images
-  Only deploy applications from trusted registries
-  Kubernetes containers orchestration must be secured with administrative boundaries
   between tenants

   -  Use Namespaces to establish security boundaries between tenants
   -  Create and define Cluster network policies
   -  Run a Cluster-wide Pod Security admission controller
   -  Turn on Audit Logging
   -  Separate sensitive workloads using Namespaces
   -  Secure tenant metadata Access

-  Segregate container networks using security zoning and network standards
-  Harden the Host OS running the containers
-  Use container-aware runtime defence tools
-  Enable Role-Based Access Control (RBAC)

Node Hardening
--------------

Node hardening: Securing Kubernetes hosts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an operating system or application is installed, it comes with default
settings. Usually, all ports are open, and all application services are turned
on. In other words, freshly installed assets are highly insecure.

Ensure Kubernetes nodes are secure, hardened and configured correctly following
well known security frameworks. Security benchmarks, for example, CIS benchmarks
are a set of configuration standards and best practices designed to help ‘harden’
the security of their digital assets.

Restrict direct access to nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Restrict root/administrative access to Kubernetes nodes while avoiding direct
access to nodes for operational activities including debugging, troubleshooting,
and other tasks.

Vulnerability assessment
~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability assessments are a crucial part of IT risk management lifecycles.
The mitigation of the vulnerabilities helps in protecting systems and data from unauthorised access and breaches.
Implement necessary vulnerability scanner tools (e.g., OpenVAS or any other
open source or commercial tools) to identify threats and flaws within the
infrastructure that represents potential risks.

Patch management
~~~~~~~~~~~~~~~~

Patch management is another key aspect of IT risk management lifecycle for
security, compliance, uptime, feature enhancements, etc. Implement
necessary patch management to ensure your environment is not susceptible to
exploitation.

Securing Kubernetes orchestrator
--------------------------------

The communication over the Kubernetes control plane APIs needs to be
secured via different mechanisms like TLS encryption, API authentication via
LDAP etc. A control plane node in an unsecured boundary can lead to a potential
threat to the running workloads. It is recommended that a control plane node is
hardened in terms of security by disabling unused ports, prohibiting root access
etc.

They following are security recommendations for orchestration manager:

-  Cluster management Network isolation can help protect the control plane node and
   control where administrative commands can run. Use network isolation
   techniques, configure RBAC on the Cluster manager and configure node service
   accounts following the principle of least privilege.
-  Ensure that access control is applied to registries requiring unique
   credentials, to limit who can control the build or add images.
-  Network access runs over TLS connections.
-  User roles and access levels are configured to provide segregation of duties.

   -  Do not mix container and non-containers services on the same node
   -  Do not run containers as root

-  Multi-factor authentication is used for all administrative access.
-  Harden the configuration by using CIS (Center for Internet Security)
   benchmarks, which are available for container runtime and Kubernetes
-  Deploy security products that provide whitelisting, behaviour monitoring and
   anomaly detection for preventing malicious activity
-  Avoid privileged container application through policy management to reduce the
   effects of potential attacks.
-  Enable integration with other security ecosystem (SIEM)
-  Isolate environments (Dev /test /Production) from other environments within
   the Cluster.
-  Create administrative boundaries between resources using Namespace and avoid
   using default Namespaces.
-  Enable Seccomp to ensure that the workloads have restricted actions available
   within the container application.
-  Limit discovery by restricting services and users that can access Cluster
   management metadata on configuration, containers and nodes

Control network access to sensitive ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kubernetes clusters usually listen on a range of well-defined and distinctive
ports which makes it easy to identify the clusters and attack them. Hence, it is
highly recommended to configure authentication and authorisation on the cluster
and cluster nodes.

The Kubernetes documentation :cite:p:`k8s-documentation-ports-and-protocols` specifies the default ports used in
Kubernetes. Make sure that your network blocks access to unnecessary ports and consider limiting access to the
Kubernetes API server except from trusted networks.

**Control plane node(s):**

======== ========== =======================
Protocol Port Range Purpose
======== ========== =======================
TCP      6443       Kubernetes API Server
TCP      2379-2380  etcd server client API
TCP      10250      Kubelet API
TCP      10259      kube-scheduler
TCP      10257      kube-controller-manager
======== ========== =======================

**Worker nodes:**

======== =========== =================
Protocol Port Range  Purpose
======== =========== =================
TCP      10250       Kubelet API
TCP      30000-32767 NodePort Services
======== =========== =================

Controlling access to the Kubernetes API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Kubernetes platform is controlled using APIs, which are the first items to be secured in order to defend against
attackers.
Controlling who has access and what actions they are allowed to perform is the primary concern.

Use Transport Layer Security and Service Mesh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Communication in the cluster between services should be handled using TLS,
encrypting all traffic by default. Kubernetes expects that all API communication
in the cluster is encrypted by default with TLS, and the majority of installation methods
will allow the necessary certificates to be created and distributed to the cluster components.
Note that some components and installation methods may enable local ports over
HTTP and administrators should familiarize themselves with the settings of each
component to identify potentially unsecured traffic.

Advances in network technology, such as the service mesh, have led to the
creation of products like LinkerD and Istio which can enable TLS by default
while providing extra telemetry information on transactions between services.
The service mesh is a mesh of layer 7 proxies handling service-to-service communications.
The service mesh architecture consists of data plane components made up of network proxies paired with each
micro-service,
and control plane components providing proxies configuration, managing TLS certificates and policies.
The two documents, NIST SP 800-204A :cite:t:`nist-800-204a` and NIST SP 800-204B :cite:t:`nist-800-204b` provide
guidance to deploy service mesh.

API Authentication, API Authorisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Secure all connections to a Kubernetes Cluster. Adopt the following security
authentication mechanisms:

-  Configure user roles and access levels to provide segregation of duties (RBAC)
-  Use multi-factor authentication for all administrative access
-  Use token-based or certificate-based service and session authentication
   mechanisms
-  Integrated with existing identity management platforms e.g., SAML, AD, etc. for
   access control

Restrict access to etcd and encrypt contents within etcd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

etcd is a critical Kubernetes component which stores information on state and
secrets, and it should be protected differently from the rest of your cluster.
Write access to the API server's etcd is equivalent to gaining root on the
entire cluster, and even read access can be used to escalate privileges fairly
easily.

The Kubernetes scheduler will search etcd for pod definitions that do not have a
node. It then sends the pods it finds to an available kubelet for scheduling.
Validation for submitted pods is performed by the API server before it writes
them to etcd, so malicious users writing directly to etcd can bypass many
security mechanisms e.g., PodSecurityPolicies.

Administrators should always use strong credentials from the API servers to
their etcd server, such as mutual auth via TLS client certificates, and it is
often recommended to isolate the etcd servers behind a firewall that only the
API servers may access.

Controlling access to the Kubelet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kubelets expose HTTPS endpoints which grant powerful control over the node and
containers. By default Kubelets allow unauthenticated access to this API.
Production clusters should enable Kubelet authentication and authorization

Securing Kubernetes Dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Kubernetes dashboard is a webapp for managing your cluster. It is not a
part of the Kubernetes cluster itself, it has to be installed by the owners of
the cluster; a number of tutorials show how to do this.
Unfortunately, most of them create a service account with very high privileges.
This caused Tesla and some others to be hacked via such a poorly configured Kubernetes
dashboard (Reference: Tesla cloud resources are hacked to run
cryptocurrency-mining malware :cite:p:`arstechnica-tesla`).

To prevent attacks via the dashboard, you should follow some best practices:

-  Do not expose the dashboard without additional authentication to the public.
   There is no need to access such a powerful tool from outside your LAN
-  Turn on RBAC, so you can limit the service account the dashboard uses
-  Review the privileges granted to the service account of the dashboard privileges,
   and remove disable any additional privileges assigned.
-  Grant permissions per user, so each user can only access what they are supposed to
   access
-  If using network policies, block requests to the dashboard
   even from internal pods (this will not affect the proxy tunnel via kubectl
   proxy)
-  Before version 1.8, the dashboard had a service account with full privileges,
   so check that there is no role binding for cluster-admin left.
-  Deploy the dashboard with an authenticating reverse proxy, with multi-factor
   authentication enabled. This can be done with either embeded OpenID Connect (OIDC) id_tokens or
   using Kubernetes Impersonation. This allows the use of the dashboard with the
   user's credentials instead of using a privileged ServiceAccount. This method
   can be used on both on-prem and managed cloud clusters.

Use Namespaces to Establish Security Boundaries
-----------------------------------------------

Namespaces in Kubernetes is the first level of isolation between components. It
is easier to apply security controls (Network Policies, Pod policies, etc.) to
different types of workloads when deployed in separate Namespaces.

Separate Sensitive Workload
---------------------------

To limit the potential impact of a compromise, it is recommended to run
sensitive workloads on a dedicated set of nodes. This approach reduces the
risk of a sensitive application being accessed through a less-secure application
that shares a container runtime or host.

-  The separation can be achieved by using node pools and Kubernetes Namespaces.

Create and Define Network Policies
----------------------------------

Network Policies allow Kubernetes managers to control network access into and
out of the cloud native applications. It is recommended to have a well defined
ingress and egress policy for cloud native applications. It is also important to
modify the default network policies, such as blocking or allowing traffic from
other Namespaces or Clusters while ensuring the Namespaces/Clusters are running
with policy support enabled.

Run latest Version
------------------

As new security features and patches are added in every quarterly update, it is
important to take advantage of these fixes and patches.

-  It is recommended to run the latest release with its most recent patches.

Secure Platform Metadata
------------------------

Kubernetes metadata contain sensitive information including kubelet admin
credentials. It is recommended to secure them using encryption to avoid this
being stolen and use to for escalated privileges in the the Cluster.

-  Limit discovery by restricting services and users that can access Cluster
   management metadata on configuration, container application, and nodes
-  Ensure all metadata is encrypted and network access runs over TLS connections

Enable Logging and Monitoring
-----------------------------

Logging, monitoring, alerting and log aggregation are essential for Kubernetes.
Enable and monitor audit logs for anomalous or unwanted API calls, especially
any authorisation failure.

Run-Time Security
-----------------

The following are recommended best practices for container run-time:

-  Integrate run-time processes to Security Information and Event Monitoring
   (SIEM)
-  Use container-aware run-time defence tools
-  Ensure all running cloud native applications are from secure and verified
   images
-  Cloud native applications are not run with root privileges
-  Ensure sensitive workloads are properly segmented by Namespaces or Cluster to
   mitigate the scope of compromise.

Secrets Management
------------------

It is recommended that the principle of least privilege is applied to secret
management in Kubernetes:

-  Ensure that the cloud native applications can only read the secrets that these
   applications need
-  Have different set of secrets for different environments (like production,
   development, and testing)

Secret values protect sensitive data, it is recommended to protect them from
unauthorised access. Ideally, by being protected at rest and in transit.
Encryption in transit is achieved by encrypting the traffic between the
Kubernetes control-plane components and worker nodes using TLS.

It is recommended that Secrets are not be stored in scripts or code but provided
dynamically at runtime as needed. Keep any sensitive data, including SSH keys,
API access keys, and database credentials, in a secure data repository such as a
key manager or vault. Only pull credentials on demand and over secure channels
to ensure sensitive data is not written to disk unprotected. The key manager or
vault encryption keys should be backed by a FIPS 140-2 Hardware Security Module.
It is also important to implement the following:

-  Check there are no hard-coded passwords, keys, and other sensitive items in
   the container application.
-  Where possible use security tools to automate scanning for hard-coded
   passwords, keys, and other sensitive items in the container application

Trusted Registry
----------------

Ensure that the container registry only accepts container images from trusted
sources that have tested and validated the images. Where images are provided by
third parties, define and follow a formal process to validate compliance with
security requirements. Also ensure that access control is applied to registries
requiring unique credentials, to limit who can control the build or add images.

-  It is strongly recommended that network access to the registry is secured
   using TLS, SSL or VPN connections to ensure trust.
-  Ensure container applications are validated to assess their use and
   applicability as well as scanned for viruses and vulnerabilities. Only deploy
   container application from images that are signed with a trusted key
-  Ensure the latest certified container application is always selected by
   versioning images
-  Trusted repository and registry services should reject containers that are not
   properly signed
-  Use approved registries for images loaded into production
-  Where possible, use third-party products to validate container content both
   before and after deployment

Ensure stale images are removed from the registry. Remove unsafe, vulnerable
images (e.g. containers should no longer be used based on time triggers and
labels associated with images).

Isolation
---------

.. _vm-vs-container-isolation:

VM vs. Container Isolation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes container isolation is compared directly with VM based isolation, with
the conclusion "*there are issues with container isolation, it is not as good as
VM isolation*". Such 1:1 comparison is not reasonable because VM and container
based isolation are fundamentally different:

-  VMs: hard isolation, in the layers underlying the application SW
-  Containers: isolation by SW based mechanisms available in OS, the container runtime and
   Kubernetes. A container workload is just a set of Linux processes. It is
   *possible* to configure SW based *additional isolation* for container
   workloads, for example by kernel namespaces.

The primary isolation mechanism in Kubernetes environment should be VM or
physical machine based. This implies that multiple cloud native applications
should not be deployed together in the same Kubernetes Cluster - unless these
applications have been planned and verified to co-exist. Thus, the default is to
allocate one Namespace per Cloud Native Network Function (CNF).

Container Isolation in Kubernetes Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Namespaces
^^^^^^^^^^

Kubernetes Namespaces should be used to provide resource isolation within a
Kubernetes Cluster. They should not be used to isolate different steps in the
deployment process like Development, Production, or Testing. The most reliable
separation is achieved by deploying sensitive workloads into dedicated Clusters.
