[<< Back](../../kubernetes)

# 5. Security Guidance
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 Introduction](#51-introduction)
* [5.2 Principles](#52-principles)
* [5.3 Node Hardening](#53-node-hardening)
* [5.4 Authentication & Authorisation](#54-authentication--authorisation)
* [5.5 Use Namespaces to Establish Security Boundaries](#55-use-namespaces-to-establish-security-boundaries)
* [5.6 Separate Sensitive Workload](#56-separate-sensitive-workloads)
* [5.7 Create and Define Network Policies](#57-create-and-define-network-policies)
* [5.8 Run latest Version](#58-run-latest-version)
* [5.9 Secure Platform Metadata](#59-secure-platform-metadata)
* [5.10 Enable Logging and Monitoring](#510-enable-logging-and-monitoring)
* [5.11 Run-time Security](#511-run-time-security)
* [5.12 Secrets Management](#512-secrets-management)
* [5.13 Trusted Registry](#513-trusted-register)
* [5.14 Orchestration & Container Manager](#514-orchestration--container-manager)
* [5.15 Security Parameters](#515-security-parameters)
* [5.16 Isolation](#516-isolation)
    * [5.16.1 VM vs. Container Isolation](5161-vm-vs-container-isolation)
    * [5.16.2 Container Isolation in Kubernetes Cluster](5162-container-isolation-in-kubernetes-cluster)
        * [5.16.2.1 Namespaces](51621-namespaces)

## 5.1 Introduction
Securing Kubernetes requires several layers of security features to provide end
to end security for cloud native applications. It is recommended that:

- Security testing is fully integrated into the CI/CD pipelines of all parties
(e.g. vendors and operators).
- Automated security policies are used to flag builds with issues.
- Image registries are monitored to automatically block or replace images with
known vulnerabilities, while also ensuring policies are used to gate what can be
deployed and who can deploy from the registry.
- Adopt a layered packaging model which supports separation of concerns during
image build.

The following functionalities are recommended for securing Kubernetes platforms:

- Image Certification (Scan for vulnerabilities) and Signing
- Role-base Access Control
- Secret Management
- How to overcome the lack of hard Kubernetes Cluster Multi-tenancy
  - Tenants without hard multi-tenancy requirements (multiple development teams
    in the same organisation) separated from each other by Namespaces
  - For strict multi tenancy, a dedicated Kubernetes Cluster per tenant should be used
- Integration with other security ecosystem like monitoring and alerting tools

## 5.2 Principles
The following are core principles to consider when securing cloud native applications:

- Deploy only secure applications and trusted codes
- Only deploy applications from validated and verified images
- Only deploy applications from trusted registries
- Containers orchestration (Kubernetes) secured with administrative boundaries
between tenants
  - Use Namespaces to establish security boundaries between tenants
  - Create and define Cluster network policies
  - Run a Cluster-wide pod security policy
  - Turn on Audit Logging
  - Separate sensitive workloads using Namespaces
  - Secure tenant metadata Access
- Segregate container networks using security zoning and network standards
- Harden the Host OS running the containers
- Use container-aware runtime defence tools
- Enable Role-Based Access Control (RBAC)

## 5.3 Node Hardening
Ensure Kubernetes nodes are secure, hardened and configured correctly following
well known security framework e.g. CIS benchmark, etc. Restrict administrative
access to Kubernetes nodes while avoiding direct access to nodes for operational
activities including debugging, troubleshooting, and other tasks.

## 5.4 Authentication & Authorisation
Secure all connections to a Kubernetes Cluster. Adopt the following security
authentication mechanisms:
 - Configure user roles and access levels to provide segregation of duties (RBAC)
 - Use multi-factor authentication for all administrative access
 - Use token-based or certificate-based service and session authentication mechanisms
 - Integrated with existing identity management platforms e.g SAML, AD, etc. for
 access control

## 5.5 Use Namespaces to Establish Security Boundaries
Namespaces in Kubernetes is the first level of isolation between components. It
is easier to apply security controls (Network Policies, Pod policies, etc.) to
different types of workloads when deployed in separate Namespaces.

## 5.6 Separate Sensitive Workload
To limit the potential impact of a compromise, it is recommended to run sensitive
workloads on a dedicated set of machines. This approach reduces the risk of a
sensitive application being accessed through a less-secure application that
shares a container runtime or host.
- The separation can be achieved by using node pools and Kubernetes Namespaces.

## 5.7 Create and Define Network Policies
Network Policies allow Kubernetes managers to control network access into and
out of the cloud native applications. It is recommended to have a well defined
ingress and egress policy for cloud native applications. It is also important to
modify the default network policies, such as blocking or allowing traffic from
other Namespaces or Clusters while ensuring the Namespaces/Clusters are running
with policy support enabled.

## 5.8 Run latest Version
As new security features and patches are added in every quarterly update, it is
important to take advantage of these fixes and patches.
- It is recommended to run the latest release with its most recent patches.

## 5.9 Secure Platform Metadata
Kubernetes metadata contain sensitive information including kubelet admin
credentials. It is recommended to secure them using encryption to avoid this
being stolen and use to for escalated privileges in the the Cluster.

- Limit discovery by restricting services and users that can access Cluster
management metadata on configuration, container application, and nodes
- Ensure all metadata is encrypted and network access runs over TLS connections

## 5.10  Enable Logging and Monitoring
Logging, monitoring, alerting and log aggregation are essential for Kubernetes.
Enable and monitor audit logs for anomalous or unwanted API calls, especially
any authorisation failure.

## 5.11  Run-Time Security
The following are recommended best practices for container run-time:
- Integrate run-time processes to Security Information and Event Monitoring (SIEM)
- Use container-aware run-time defence tools
- Ensure all running cloud native applications are from secure and verified images
- Cloud native applications are not run with root privileges
- Ensure sensitive workloads are properly segmented by Namespaces or Cluster to
mitigate the scope of compromise.

## 5.12  Secrets Management
It is recommended that the principle of least privilege is applied to secret
management in Kubernetes:
- Ensure that the cloud native applications can only read the secrets that these
applications need
- Have different set of secrets for different environments(like production,
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
- Check there are no hard-coded passwords, keys, and other sensitive items in
the container application.
- Where possible use security tools to automate scanning for hard-coded passwords,
keys, and other sensitive items in the container application

## 5.13  Trusted Registry
Ensure that the container registry only accepts container images from trusted
sources that have tested and validated the images. Where images are provided by
third parties, define and follow a formal process to validate compliance with
security requirements. Also ensure that access control is applied to registries
requiring unique credentials, to limit who can control the build or add images.

- It is strongly recommended that network access to the registry is secured using
TLS, SSL or VPN connections to ensure trust.
- Ensure container applications are validated to assess their use and
applicability as well as scanned for viruses and vulnerabilities. Only deploy
container application from images that are signed with a trusted key
- Ensure the latest certified container application is always selected by
versioning images
- Trusted repository and registry services should reject containers that are not
properly signed
- Use approved registries for images loaded into production
- Where possible, use third-party products to validate container content both
before and after deployment

Ensure stale images are removed from the registry. Remove unsafe, vulnerable
images (e.g. containers should no longer be used based on time triggers and
labels associated with images).

## 5.14  Orchestration & Container Manager
The Kubernetes orchestration manager also known as the control plane consist of
various components including a Kube-API server, an etcd storage, a
kube-controller-manager, a cloud-controller-manager, a kube-scheduler, and a DNS
server for Kubernetes services. The communication over these APIs needs to be
secured via different mechanisms like TLS encryption, API authentication via
LDAP etc. A control plane node in an unsecured boundary can lead to a potential
threat to the running workloads. It is recommended that a control plane node is
hardened in terms of security by disabling unused ports, prohibiting root access
etc.

They following are security recommendations for orchestration manager:

- Cluster management Network isolation can help protect the master node and
control where administrative commands can run. Use network isolation techniques,
configure RBAC on the Cluster manager and configure node service accounts
following the principle of least privilege.
- Ensure that access control is applied to registries requiring unique credentials,
to limit who can control the build or add images.
- Network access runs over TLS connections.
- User roles and access levels are configured to provide segregation of duties.
  - Do not mix container and non-containers services on the same node
  - Do not run containers as root
- Multi-factor authentication is used for all administrative access.
- Harden the configuration by using CIS (Center for Internet Security) benchmarks,
which are available for container runtime and Kubernetes
- Deploy security products that provide whitelisting, behaviour monitoring and
anomaly detection for preventing malicious activity
- Avoid privileged container application through policy management to reduce the
effects of potential attacks.
- Enable integration with other security ecosystem (SIEM)
- Isolate environments (Dev /test /Production) from other environments within the
Cluster.
- Create administrative boundaries between resources using Namespace and avoid
using default Namespaces.
- Enable Seccomp to ensure that the workloads have restricted actions available
within the container application.
- Limit discovery by restricting services and users that can access Cluster
management metadata on configuration, containers and nodes

## 5.15  Security Perimeters
When applications or workloads run on Kubernetes, there are several layers which
come into picture that govern the security. Each of these layers needs to be
secured within their perimeters. The various layers that come into picture are:

- **Container Registry**: A container registry is a repository to manage container
**images. The access to container registry needs to be secured in order to
**prevent unauthorised access or image tampering.
- **Container Images**: Stored instance of a container that holds a set of
software needed to run an application. Before loading them to container
registry, they need to be secured by performing various checks like
vulnerability analysis, scans etc. These images should also be signed from
trusted sources.
- **Containers**: A lightweight and portable executable image that contains
software and all of its dependencies. The containers need to be prevented from
accessing the underlying OS like loading of kernel modules, mounting of
directories of underlying OS etc and ensuring that they don't
run in privileged mode.
- **Pods**: A Pod represents a set of running containers on your Cluster.
Kubernetes inherently offers pod security policies that define a set of
conditions that a pod needs to run with in order to be accepted into the system.
These policies help in ensuring the necessary checks for running the pods.
- **Kubernetes Node**: A Kubernetes node in an unsecured boundary can lead to a
potential threat to the running workloads. Such a node should be hardened by
disabling unused ports, prohibiting root access etc.
- **Kubernetes Master**: A master node in an unsecured boundary can lead to a
potential threat to the running workloads. A master may be hardened in terms of
security by disabling unused ports, prohibiting root access etc.
- **Kubernetes Control Plane**: The container orchestration layer that exposes
the API and interfaces to define, deploy, and manage the lifecycle of containers.
The communication over these APIs needs to be secured via different mechanisms
like TLS encryption, API authentication via LDAP etc.

## 5.16  Isolation
### 5.16.1 VM vs. Container Isolation
Sometimes container isolation is compared directly with VM based isolation, with
the conclusion "*there are issues with container isolation, it is not as good as
VM isolation*". Such 1:1 comparison is not reasonable because VM and container
based isolation are fundamentally different:
- VMs: hard isolation, in the layers underlying the application SW
- Containers: isolation by SW based mechanisms available in OS, Docker and
Kubernetes. A container workload is just a set of Linux processes. It is
_possible_ to configure SW based _additional isolation_ for container workloads,
for example by kernel namespaces.

The primary isolation mechanism in Kubernetes environment should be VM or
physical machine based. This implies that multiple cloud native applications
should not be deployed together in the same Kubernetes Cluster - unless these
applications have been planned and verified to co-exist. Thus, the default is to
allocate one Namespace per Cloud Native Network Function (CNF).

### 5.16.2 Container Isolation in Kubernetes Cluster
#### 5.16.2.1 Namespaces  
Kubernetes Namespaces should be used to provide resource isolation within a
Kubernetes Cluster. They should not be used to isolate different steps in the
deployment process like Development, Production, or Testing. The most reliable
separation is achieved by deploying sensitive workloads into dedicated Clusters.
