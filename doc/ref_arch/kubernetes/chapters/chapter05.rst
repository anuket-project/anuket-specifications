Security Guidance
=================

Introduction
------------

Securing Kubernetes requires several layers of security features to provide
end-to-end security for cloud-native applications. The following is recommended:

-  Security testing is fully integrated into the CI/CD pipelines of all parties
   (for example, vendors and operators).
-  Automated security policies are used to flag builds with issues.
-  Image registries are monitored to automatically block or replace images with
   known vulnerabilities, while also ensuring policies are used to gate what can
   be deployed and who can deploy from the registry.
-  A layered packaging model is adopted which supports separation of concerns
   during an image build.

The following functionalities are recommended for securing the Kubernetes
platforms:

-  Image Certification (scanning for vulnerabilities) and Signing.
-  Role-Based Access Control (RBAC).
-  Secret Management.
-  How to overcome the lack of hard Kubernetes Cluster Multitenancy.

   -  Tenants without hard multitenancy requirements (multiple development teams
      in the same organisation) separated from each other by Namespaces.
   -  For strict multitenancy, a dedicated Kubernetes Cluster per tenant should
      be used.

-  Integration with other security ecosystem, such as monitoring and alerting tools.

Security perimeters
~~~~~~~~~~~~~~~~~~~

When applications or workloads run on Kubernetes, there are several layers that
govern the security. Each of these layers needs to be secured within its perimeters.
The layers are as follows:

-  **Container registry**: The container registry is a repository for managing
   the container images. The access to container registry needs to be secured, in
   order to prevent unauthorised access or image tampering.
-  **Container images**: A container image is a lightweight and portable executable image
   that contains software and all of the dependencies. Before loading the images to a
   container registry, they need to be secured by performing various checks, such as
   vulnerability analysis, scans, and so on. These images should also be signed from
   trusted sources.
-  **Containers**: A container is a running instance of a container image. The containers
   need to be prevented from accessing the underlying OS capabilities like loading of
   kernel modules, mounting of directories of the underlying OS, and so on, and running in
   privileged mode.
-  **Pods**: A Pod represents a set of running containers on a Kubernetes Cluster.
   Kubernetes inherently offers pod security policies that define a set of
   conditions that a pod needs to run with, in order to be accepted into the
   system. These policies help in ensuring that the necessary checks are made for
   running the pods.
-  **Kubernetes Node**: A Kubernetes (worker) Node is a physical or virtual server that
   runs the workloads in a Kubernetes Cluster. A Kubernetes node in an unsecured boundary
   can lead to a potential threat to the running workloads. Such a node should be
   hardened by disabling unused ports, prohibiting root access, and so on.
-  **Kubernetes Control Plane Node**: A control plane node in an unsecured boundary can
   lead to a potential threat to the running workloads. A control plane may be hardened,
   in terms of security, by disabling unused ports, prohibiting root access, and so on.
-  **Kubernetes Control Plane**: The Kubernetes Control Plane is a container orchestration
   layer that exposes the APIs and other interfaces to define, deploy, and manage the
   lifecycle of the containers. The communication over these APIs needs to be secured via
   different mechanisms, such as TLS encryption, API authentication via LDAP, and so on.

Principles
----------

The core principles to consider when securing cloud-native applications are as follows:

-  Only deploy secure and trusted applications and codes.
-  Only deploy applications from validated and verified images.
-  Only deploy applications from trusted registries.
-  Kubernetes containers orchestration must be secured with administrative boundaries
   between the tenants:

   -  Use Namespaces to establish security boundaries between tenants.
   -  Create and define Cluster network policies.
   -  Run a Cluster-wide pod security policy.
   -  Turn on Audit Logging.
   -  Separate sensitive workloads using Namespaces.
   -  Secure tenant metadata access.

-  Segregate container networks using security zoning and network standards.
-  Harden the Host OS running the containers.
-  Use container-aware runtime defence tools.
-  Enable Role-Based Access Control (RBAC).

Node hardening
--------------

Node hardening: securing the Kubernetes hosts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an operating system or application is installed, it has default settings.
Usually, all the ports are open, and all the application services are turned on.
In other words, freshly installed assets are insecure.

Ensure Kubernetes nodes are secure, hardened, and configured correctly, in
accordance with well-known security frameworks. Security benchmarks, for example,
CIS benchmarks, are a set of configuration standards and best practices designed to
help harden the security of their digital assets.

Restricting direct access to nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Restrict root/administrative access to the Kubernetes nodes while avoiding direct
access to the nodes for operational activities, including debugging, troubleshooting,
and other tasks.

Vulnerability assessment
~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability assessments are a crucial part of IT risk management lifecycles.
The mitigation of vulnerabilities helps in protecting systems and data from
unauthorised access and breaches. Implement necessary vulnerability scanner tools,
such as OpenVAS, or any other open-source or commercial tools, to identify threats
and flaws within the infrastructure that represent potential risks.

Patch management
~~~~~~~~~~~~~~~~

Patch management is another key aspect of the IT risk management lifecycle for
security, compliance, uptime, feature enhancements, and so on. Implement the
necessary patch management to ensure your environment is not susceptible to
exploitation.

Securing the Kubernetes orchestrator
------------------------------------

Communication over the Kubernetes control plane APIs needs to be
secured via different mechanisms, such as TLS encryption, API authentication via
LDAP, and so on. A control plane node in an unsecured boundary can lead to a potential
threat to the running workloads. It is recommended that a control plane node is
hardened in terms of security by disabling unused ports, prohibiting root access, and
so on.

The security recommendations for the orchestration manager are as follows:

-  Cluster management network isolation can help protect the control plane node and
   control where the administrative commands can run. Use network isolation
   techniques, configure RBAC on the Cluster manager, and configure node service
   accounts following the principle of least privilege.
-  Ensure that access control is applied to registries requiring unique
   credentials, to limit who can control the build or add images.
-  Network access runs over the TLS connections.
-  User roles and access levels are configured to provide segregation of duties.

   -  Do not mix container and non-container services on the same node.
   -  Do not run the containers as root.

-  Multifactor authentication is used for all administrative access.
-  Harden the configuration by using Center for Internet Security (CIS)
   benchmarks, which are available for container runtime and Kubernetes.
-  Deploy security products that provide whitelisting, behaviour monitoring, and
   anomaly detection, in order to prevent malicious activity.
-  Avoid privileged container application through policy management to reduce the
   effects of potential attacks.
-  Enable integration with other security ecosystems (SIEM).
-  Isolate environments (Dev/test/Production) from other environments within
   the cluster.
-  Create administrative boundaries between resources using Namespace and avoid
   using default Namespaces.
-  Enable Seccomp to ensure that the workloads have restricted actions available
   within the container application.
-  Limit discovery by restricting services and users that can access cluster
   management metadata on configuration, containers, and nodes.

Control network access to sensitive ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kubernetes clusters usually listen in on a range of well-defined and distinctive
ports. This makes it easy to identify the clusters and attack them. It is therefore
recommended to configure authentication and authorisation on the cluster and the
cluster nodes.

The Kubernetes documentation :cite:p:`k8s-documentation-ports-and-protocols`
specifies the default ports used in Kubernetes. Make sure that your network blocks
access to unnecessary ports. Consider limiting access to the Kubernetes API server,
except from trusted networks.

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

The Kubernetes platform is controlled using APIs. The APIs are the first elements to be secured
when defending against attackers. Controlling who has access to the Kubernetes API, and what
actions they are allowed to perform, is the primary concern.

Using Transport Layer Security and service mesh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Communication in the cluster between services should be handled using Transport Layer Security
(TLS), encrypting all traffic by default. Kubernetes expects that all API communication
in the cluster is encrypted by default with TLS, and the majority of installation methods
allow the necessary certificates to be created and distributed to the cluster components.

.. note::

  Some components and installation methods may enable local ports over HTTP. Administrators
  should familiarize themselves with the settings of each component to identify potentially
  unsecured traffic.

Advances in network technology, such as the service mesh, have led to the creation of products
such as LinkerD and Istio, which can enable TLS by default, while providing extra telemetry
information on transactions between services. The service mesh is a mesh of layer 7 proxies
handling service-to-service communications. The service mesh architecture consists of data
plane components made up of network proxies paired with each microservice, and control plane
components providing proxies configuration, managing TLS certificates and policies.
The documents, NIST SP 800-204A :cite:t:`nist-800-204a` and
NIST SP 800-204B :cite:t:`nist-800-204b` provide guidance on deploying service mesh.

API authentication and authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When securing all connections to a Kubernetes Cluster, adopt the following security
authentication mechanisms:

-  Configure user roles and access levels to provide segregation of duties (RBAC).
-  Use multifactor authentication for all administrative access.
-  Use token-based or certificate-based service and session authentication
   mechanisms.
-  Integrate with existing identity management platforms, such as SAML, AD, and so on,
   for access control.

Restricting access to etcd and encrypt contents within etcd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

etcd is a critical Kubernetes component which stores information on state and
secrets. It should be protected in a different way from the rest of your cluster.
Write access to the API server's etcd is equivalent to gaining root on the
entire cluster. Even read access can be used to escalate privileges fairly
easily.

The Kubernetes scheduler searches etcd for pod definitions that do not have a
node. It then sends the pods it finds to an available kubelet for scheduling.
Validation for submitted pods is performed by the API server before it writes
them to etcd. Therefore, malicious users writing directly to etcd can bypass
many security mechanisms such as PodSecurityPolicies.

Administrators should always use strong credentials from the API servers to
their etcd server, such as mutual authorization via TLS client certificates.
It is recommended to isolate the etcd servers behind a firewall that only the
API servers may access.

Controlling access to the kubelet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kubelets expose HTTPS endpoints which grant control over the node and
containers. By default, kubelets allow unauthenticated access to this API.
Production clusters should enable kubelet authentication and authorization.

Securing the Kubernetes dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Kubernetes dashboard is a web app for managing your cluster. It is not a
part of the Kubernetes cluster itself, it has to be installed by the owners of
the cluster. There are a number of tutorials that show you how to do this.
Unfortunately, most of them create a service account with high privileges.
Consequently, Tesla and some others were hacked via a poorly configured
Kubernetes dashboard (Reference: Tesla cloud resources are hacked to run
cryptocurrency-mining malware :cite:p:`arstechnica-tesla`).

To prevent attacks via the dashboard, follow the best practices detailed here:

-  Do not expose the dashboard to the public without additional authentication.
   There is no need to access such a powerful tool from outside your LAN.
-  Turn on RBAC, so you can limit the service account that the dashboard uses.
-  Review the privileges granted to the service account of the dashboard privileges,
   and remove or disable any additional privileges that have been assigned.
-  Grant permissions per user, so that each user can only access the Information
   they are supposed to access.
-  If you are using network policies, then block requests to the dashboard
   even from internal pods (this will not affect the proxy tunnel via kubectl
   proxy).
-  Prior to version 1.8, the dashboard had a service account with full privileges.
   Therefore, check that there is no longer role binding for cluster-admin.
-  Deploy the dashboard with an authenticating reverse proxy, with multifactor
   authentication enabled. This can be done with either embedded OpenID Connect (OIDC) id_tokens or
   using Kubernetes Impersonation. This allows the use of the dashboard with the
   user's credentials, instead of using a privileged ServiceAccount. This method
   can be used on both on-prem and managed cloud clusters.

Using Namespaces to establish security boundaries
-------------------------------------------------

Namespaces in Kubernetes is the first level of isolation between components. It
is easier to apply security controls (such as Network Policies, Pod policies, and so on)
to different types of workloads when deployed in separate Namespaces.

Separating sensitive workloads
------------------------------

To limit the potential impact of a compromise, it is recommended to run
sensitive workloads on a dedicated set of nodes. This approach reduces the
risk of a sensitive application being accessed through a less secure application
that shares a container runtime or host.

-  The separation can be achieved by using node pools and Kubernetes Namespaces.

Creating and defining Network Policies
--------------------------------------

Network Policies allow Kubernetes managers to control network access into and
out of the cloud-native applications. It is recommended to have a well defined
ingress and egress policy for cloud-native applications. It is also important to
modify the default network policies, such as blocking or allowing traffic from
other Namespaces or Clusters, while ensuring the Namespaces/Clusters are running
with policy support enabled.

Running the latest Version
--------------------------

As new security features and patches are added in every quarterly update, it is
important to take advantage of these fixes and patches.

-  It is recommended to run the latest release with its most recent patches.

Securing Platform Metadata
--------------------------

Kubernetes metadata contains sensitive information, including kubelet admin
credentials. It is recommended to secure them using encryption to prevent it
from being stolen and used for escalated privileges in the Cluster.

-  Limit discovery by restricting services and users that can access Cluster
   management metadata on configurations, container applications, and nodes.
-  Ensure all metadata is encrypted and network access runs over TLS connections.

Enabling logging and monitoring
-------------------------------

Logging, monitoring, alerting, and log aggregation are essential for Kubernetes.
Enable and monitor audit logs for anomalous or unwanted API calls, especially
any authorization failure.

Runtime security
----------------

The following actions are recommended as best practices for container runtime:

-  Integrate runtime processes to Security Information and Event Monitoring
   (SIEM).
-  Use container-aware runtime defense tools.
-  Ensure all running cloud-native applications are from secure and verified
   images.
-  Ensure all cloud-native applications are not run with root privileges.
-  Ensure sensitive workloads are properly segmented by Namespaces or Cluster to
   mitigate the scope of compromise.

Secrets management
------------------

It is recommended that the principle of least privilege is applied to secrets
management in Kubernetes:

-  Ensure that the cloud-native applications can only read the secrets that these
   applications need.
-  Have different sets of secrets for different environments (such as production,
   development, and testing).

Secret values protect sensitive data. It is therefore recommended to protect them from
unauthorized access, ideally by being protected at rest and in transit. Encryption in
transit is achieved by encrypting the traffic between the Kubernetes control plane
components and worker nodes using TLS.


It is recommended that secrets not be stored in scripts or code, but instead provided
dynamically at runtime, as needed. Keep any sensitive data, including SSH keys, API
access keys, and database credentials, in a secure data repository, such as a key
manager or a vault. Only pull credentials on demand and over secure channels, to ensure
that sensitive data is not written to a disk unprotected. The key manager or vault
encryption keys should be backed by a FIPS 140-2 Hardware Security Module. It is also
important to take the following actions:

-  Check that there are no hardcoded passwords, keys, and other sensitive items in
   the container application.
-  Where possible, use security tools to automate scanning for hardcoded passwords,
   keys, and other sensitive items in the container application.

Trusted registry
----------------

Ensure that the container registry only accepts container images from trusted
sources that have tested and validated the images. Where images are provided by
third parties, define and follow a formal process to validate compliance with
security requirements. Also ensure that access control is applied to registries
requiring unique credentials, in order to limit who can control the build or add images.

-  To ensure trust, it is recommended to secure network access to the registry using
   TLS, SSL, or VPN connections.
-  Ensure that the container applications are validated to assess their use and
   applicability as well as scanned for viruses and vulnerabilities. Only deploy
   container application from images that are signed with a trusted key.
-  Ensure that the latest certified container application is always selected by
   versioning images.
-  Trusted repository and registry services should reject containers that are not
   properly signed.
-  Use approved registries for images loaded into production.
-  Where possible, use third-party products to validate container content both
   before and after deployment.

Ensure that stale images are removed from the registry. Remove unsafe and vulnerable
images (for example, containers should no longer be used based on time triggers and
labels associated with images).

Isolation
---------

.. _vm-vs-container-isolation:

VM versus container isolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes container isolation is compared directly to VM-based isolation, with
the conclusion "*There are issues with container isolation, it is not as good as
VM isolation*". Such a 1:1 comparison is not reasonable because VM-based isolation
and container-based isolation are fundamentally different:

-  VMs: Hard isolation, in the layers underlying the application software.
-  Containers: Isolation by software-based mechanisms available in the OS, the
   container runtime, and Kubernetes. A container workload is just a set of Linux
   processes. It is *possible* to configure software-based *additional isolation*
   for container workloads, for example by kernel namespaces.

The primary isolation mechanism in Kubernetes environment should be VM-based or
physical machine-based. This implies that multiple cloud-native applications
should not be deployed together in the same Kubernetes Cluster, unless these
applications have been planned and verified to coexist. Therefore, the default is
to allocate one Namespace per Cloud-Native Network Function (CNF).

Container isolation in the Kubernetes Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Namespaces
^^^^^^^^^^

Kubernetes Namespaces should be used to provide resource isolation within a
Kubernetes Cluster. They should not be used to isolate different steps in the
deployment process, such as development, production, or testing. The most reliable
separation is achieved by deploying sensitive workloads into dedicated Clusters.
