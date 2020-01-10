[<< Back](../../kubernetes)

# 6. Security
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 Principles](#6.2)
* [6.3 Node Hardening](#6.3)
* [6.4 Authentication & Authorisation](#6.4)
* [6.5 Use Namespaces to Establish Security Boundaries](#6.5)
* [6.6 Seperate Sensitive Workload](#6.6)
* [6.7 Create and Define Network Policies](#6.7)
* [6.8 Run latest Version](#6.8)
* [6.9 Secure Platform Metadata](#6.9)
* [6.10 Enable Logging and Monitoring](#6.10)
* [6.11 Run-time Security](#6.11)
* [6.12 Secrets Management](#6.12)
* [6.13 Trusted Registry](#6.13)
* [6.14 Orchestration & Container Manager](#6.14)
* [6.15 Security Parameters](#6.15)
* [6.16 Isolation](#6.16)

<a name="6.1"></a>
## 6.1 Introduction
Securing Kubernetes requires several layers of security features to provide end to end security for cloud native applications. It is also important to adopt a layered packaging model which support separation of concerns during image build. A fully integrated security testing should be baked into the CI/CD pipeline. Automated security policies should also be used to flag builds with issue.  Image registries must be monitored to automatically block or replace images with known vulnerabilites, while also ensuring policies are used to gate what can be deployed and who can deploy from the registry.

The following functionalities are recommended for securing kubernetes platform;
- Image Signing
- Role-base Access Control
- Secret Managment
- Kubernetes Cluster Multi-tenancy security
  - Tenant can be distinct teams or workload types (Develpoment or Production) within an organisation, each with a namespace
  - Tenant can also be per dedicated kubernetes cluster
- Integration with other security ecosystem like monitoring and alerting tools

<a name="6.2"></a>
##  6.2 Principles
The following are core principles to consider when securing cloud native applications;

- Deploy only secure applications and trusted codes
- Only deploy applications from validated and verified images
- Only deploy applications from trusted registries
- Containers orchestration (Kubernetes) must be secure with administrative boundaries between tenants
  - Use Namespaces to establish security boundaries between tenants
  - Create and define cluster network policies
  - Run a cluster-wide pod security policy
  - Turn on Audit Logging
  - Separate sensitive workloads using namespaces
  - Secure tenant metadata Access
- Network segmentation using security zoning and network standards must be followed when deploying containers 
- The Host OS running the containers must be hardened
- Use container-aware runtime defense tools
- Enable Role-Based Access Control (RBAC)

<a name="6.3"></a>
##  6.3 Node Hardening
Ensure kubernetes nodes are secure, hardened and configured correctly following well known security framework e.g. CIS benchmark, etc. Administrative access to kubernetes nodes should be restricted while operational activities including debugging, troubleshoting, and other tasks should be handled without direct access to the nodes.

##  6.4 Authentication & Authorisation
All connections to a Kubernetes cluster must be via a secure channel. The following security authentication mechanism must be adopted;

 - User roles and access levels must be configured to provide segregation of duties (RBAC)
 - Multi-factor authentication is mandated for all administrative access
 - Service and session authentication mechanisms must be token-based or certificate-based
 - Access control should be integrated with existing identity management platforms e.g SAML, AD, etc.

##  6.5 Use Namespaces to Establish Security Boundaries
Namespaces in Kubernetes is the first level of isolation between components. It is easier to apply security controls (Network Policies, Pod policies, etc) to diffferent types of workloads when deployed in seperate namespaaces. 

##  6.6 Seperate Sensitive Workload
To limit the potential impact of a compromise, it is best to run sensitive workloads on a dedicated set of machines. This approach reduces the risk of a sensitive application being accessed through a less-secure application that shares a container runtime or host.

- The seperation can achieved by using node pools and Kubernetes namespaces.

##  6.7 Create and Define Network Policies
Network Policies allow kubernetes managers to control network access into and out of the containerized applications. It is recommended to have a well defined ingress and egress policy for containerised applications. It is also important to modify the default network policies, such as blocking or allowing traffic from other namespaces or clusters while ensuring the namespaces/clusters are running with policy support enabled.

##  6.8 Run latest Version
As new security features and patches are added in every quarterly update, it is important to take advantage of these fixes and patches. 
- It is recommended to run the latest release with its most recent patches.

##  6.9 Secure Platform Metadata
Kubernetes metadata contain sensitive information including kubelet admin credentials. It is recommended to secure them using encryption to avoid this being stolen and use to for escalated privileges in the the cluster.

- Limit discovery by restricting services and users that can access cluster managment metadata on configuration, container application, and nodes
- Ensure all metadata  information are encryption and network access must run over TLS connections
##  6.10  Enable Logging and Monitoring
Logging, monitoring, alerting and log aggregation are essential for Kubernetes. Audit logs must be enabled and monitored for anomalous or unwanted API calls, especially any authorisation failure. 

##  6.11  Run-Time Security
The following are recommnended best practices for container run-time;
- Integrate run-time processes to Security Information and Event Monitoring (SIEM)
- Use container-aware run-time defense tools
- Ensure all running container applications are from secure and verified images
- Containerised application should not run with root priviledges
- Ensure sensitive workloads are proper segmented by namespaces or cluster to mitigate the scope of compromise.

##  6.12  Secrets Management
The principle of least privilege must be applied to secret management in Kubernetes;

- Ensure the containerised code can read only the secrets that it needs
- Have different set of secrets for different environments( like production, development, and testing)

Secret values protect sensitive data, it is recommended to protect them from unauthorised access. Ideally, they must be protected at rest and in transit. Encryption in transit is achieved by encrypting the traffic between the Kubernetes control-plane components and worker nodes using TLS.

Secrets must not be stored in scripts or code but provided dynamically at runtime as needed. Keep any sensitive data, including SSH keys, API access keys, and database credentials, in a secure data repository such as a key manager or vault. Only pull credentials on demand and over secure channels to ensure sensitive data is not written to disk unprotected. The key manager or vault encryption keys should be backed by a FIPS 140-2 Hardware Security Module. It is also important to implement the following;

- Check there are no hard-coded passwords, keys, and other sensitive items in the container application.
- Where possible use security tools to automate scanning for hard-coded passwords, keys, and other sensitive items in the container application

##  6.13  Trusted Registry
Ensure that the container registry only accepts container images from trusted sources that have tested and validated the images. Where images are provided by third parties, define and follow a formal process to validate compliance with security requirements. Also ensure that access control is applied to registries requiring unique credentials, to limit who can control the build or add images.

 - Network access to the registry must run over TLS or VPN connections

Ensure container applications are validated to assess their use and applicability as well as scanned for viruses and vulnerabilities. Only deploy container application from images that are signed with a trusted key

- Ensure the latest certified container application is always selected by versioning images
- Trusted repository and registry services should reject containers that are not properly signed
- Images loaded into production must come from the approved registry
- Where possible, use third-party products to validate container content both before and after deployment

Ensure stale images are removed from the registry. Remove unsafe, vulnerable images (e.g. containers should no longer be used based on time triggers and labels associated with images).

##  6.14  Orchestration & Container Manager
The kubernetes orchestration manager also know as the control plane consist of various components including a Kube-API server, an etcd storage, a kube-controller-manager, a cloud-controller-manager, a kube-scheduler, and a DNS server for Kubernetes services. 
The communication over these APIs needs to be secured via different mechanisms like TLS encryption, API authentication via LDAP etc. A master node in an unsecured boundary can lead to a potential threat to the running workloads. A master must be hardened in terms of security by disabling unused ports, prohibiting root access etc. 

They following are security recommendations for orchestration manager;

- Cluster management Network isolation can help protect the master node and control where administrative commands can run. Use network isolation techniques, configure RBAC on the cluster manager and configure node service accounts following the principle of least privilege.
- Ensure that access control is applied to registries requiring unique credentials, to limit who can control the build or add images.
- Network access must run over TLS connections.
- User roles and access levels must be configured to provide segregation of duties.
  - Do not mix container and non-containers services on the same node
  - Do not run containers as root
- Multi-factor authentication is mandatory for all administrative access.
- Harden the configuration by using CIS (Center for Internet Security) benchmarks, which are available for container runtime and Kubernetes
- Deploy security products that provide whitelisting,  behaviour monitoring and anomaly detection for preventing malicious activity
- Avoid privileged container application through policy management to reduce the effects of potential attacks.
- Avoid privileged container application through policy management to reduce the effects of potential attacks
- Enable integration with other security ecosystem (SIEM)
- Isolate environments (Dev /test /Production) from other environments within the cluster.
- Create administrative boundaries between resources using namespace and avoid using default namespaces.
- Enable Seccomp to ensure that the workloads have restricted actions available within the container application.
- Limit discovery by restricting services and users that can access cluster managment metadata on configuration, containers and nodes 
 
##  6.15  Security Perimeters
When applications or workloads run on Kubernetes, there are several layers which come into picture that govern the security. Each of these layers needs to be secured within their perimeters. The various layers that come into picture are:

- Container Registry: A container registry is a repository to manage container images. The access to container registry needs to be secured in order to prevent unauthorised access or image tampering.
- Container Images: Stored instance of a container that holds a set of software needed to run an application. Before loading them to container registry, they need to be secured by performing various checks like vulnerability analysis, scans etc. These images should also be signed from trusted sources
- Containers: A lightweight and portable executable image that contains software and all of its dependencies. The containers need to be prevented from accessing the underlying OS like loading of kernel modules, mounting of directories of underlying OS etc and it must also be ensured that they don't run in priveleged mode..
- Pods: A Pod represents a set of running containers on your cluster. Kuberenetes inherently offers pod security policies that define a set of conditions that a pod must run with in order to be accepted into the system. These policies help in ensuring the necessary checks for running the pods.
- Kubernetes Node: A Kubernetes node in an unsecured boundary can lead to a potential threat to the running workloads. Such a node should be hardened by disabling unused ports, prohibiting root access etc.
- Kubernetes Master: A master node in an unsecured boundary can lead to a potential threat to the running workloads. A master may be hardened in terms of security by disabling unused ports, prohibiting root access etc.
- Kubernetes Control Plane: The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers. The communication over these APIs needs to be secured via different mechanisms like TLS encryption, API authentication via LDAP etc.

<a name="6.15"></a>
##  6.16  Isolation
### VM vs. Container Isolation
Sometimes container isolation is compared directly with VM based isolation, with the conclusion '*there are issues with container isolation, it is not as good as VM isolation*'. Such 1:1 comparison is not reasonable because VM and container based isolation are fundamentally different:
- VMs: hard isolation, in the layers underlying the application SW
- Containers: isolation by SW based mechanisms available in OS, Docker and Kubernetes. A container workload is just a set of Linux processes. It is _possible_ to configure SW based _additional isolation_ for container workloads, for example by kernel namespaces.


Thus the primary isolation mechanism in Kubernetes environment should be VM or physical machine based isolation. This means: multiple container applications should not be deployed together in the same Kubernetes cluster - unless those have been planned and verified to co-exist.

### Container Isolation in Kubernetes Cluster
#### Namespaces  
Kubernetes namespaces should be used to provide resource isolation within a Kubernetes cluster. Kubernetes should be used to isolate different types of workloads like Development, Production or Test. The default is to allocate one namespace per Containerised Network Function (CNF).
