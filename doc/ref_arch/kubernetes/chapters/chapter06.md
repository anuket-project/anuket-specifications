[<< Back](../../kubernetes)

# 6. Security
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 Heading](#6.2)
* [6.3 Heading](#6.3)

<a name="6.1"></a>
## 6.1 Introduction
Securing Kubernetes requires several layers of security features to provide end to end security for cloud native applications. It is also important to adopt a layered packaging model which support separation of concerns during image build. A fully integrated security testing should be baked into the CI/CD pipeline. Automated security policies should also be used to flag builds with issue.  Image registries must be monitored to automatically block or replace images with known vulnerabilites, while also ensuring policies are used to gate what can be deployed and who can deploy from the registry.

The following functionalities are recommended for securing kubernetes platform;
- Image Signing
- Role-base Access Control
- Secret Managment
- Platform multitenant security
- Integration with other security ecosystem like monitoring and alerting tools

<a name="6.2"></a>
##  6.2 Principles
The following are core principles to consider when securing cloud-native applications;

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

##  6.3 Kubernetes Security Architecture
Kubernetes Security architecture is made up of of several components that provide end to end security for the infrastructure and application or workload. These components include image registries (private or public), Kubernetes API, RBAC, network services, host and container runtime, keys or secret management. Each of these components work in a collaborative mode to ensure the security of the applications or workload. 

<a name="6.3"></a>
## 6.4 Security Perimeters
When applications or workloads run on Kubernetes, there are several layers which come into picture that govern the security. Each of these layers need to be secured within their perimeters. The various layers that come into picture are:

- Container Registry: A container registry is a repository to manage container images. The access to container registry needs to be secured in order to provide a controlled access.
- Container Images: Stored instance of a container that holds a set of software needed to run an application. Before loading them to container registry, they need to be made secured by performing various checks like vulnerability analysis, scans etc. These should also be signed from trusted sources.
- Containers: A lightweight and portable executable image that contains software and all of its dependencies. The containers need to be prevented from accessing the underlying OS like loading of kernel modules, mounting of directories of underlying OS etc and it must also be ensured that they don't run in priveleged mode..
- Pods: A Pod represents a set of running containers on your cluster. Kuberenetes inherently offers pod security policies that define a set of conditions that a pod must run with in order to be accepted into the system. These policies help in ensuring the necessary checks for running the pods.
- Kubernetes Node: A node is a worker machine in Kubernetes. A worker node may be a VM or physical machine, depending on the cluster. It has local daemons or services necessary to run Pods and is managed by the control plane. A node in an unsecured boundary can lead to a potential threat to the running workloads. A node may be hardened in terms of security by disabling unused ports, prohibiting root access etc.
- Kubernetes Master: The master node(s) manages the worker nodes and the pods in the cluster. Multiple master nodes are used to provide a cluster with failover and high availability. A master in an unsecured boundary can lead to a potential threat to the running workloads. A master may be hardened in terms of security by disabling unused ports, prohibiting root access etc.
- Kubernetes Control Plane: The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers. The communication over these APIs needs to be secured via different mechanisms like TLS encryption, API authentication via LDAP etc.

<a name="6.5"></a>
## 6.5 Isolation
### VM vs. Container Isolation
Sometimes container isolation is compared directly with VM based isolation, with the conclusion '*there are issues with container isolation, it is not as good as VM isolation*'. Such 1:1 comparison is not reasonable because VM and container based isolation are fundamentally different:
- VMs: hard isolation, in the layers underlying the application SW
- Containers: isolation by SW based mechanisms available in OS, Docker and Kubernetes. A container workload is just a set of Linux processes. It is _possible_ to configure SW based _additional isolation_ for container workloads, for example by kernel namespaces.

Thus the primary isolation mechanism in Kubernetes environment should be VM or physical machine based isolation. This means: multiple container applications should not be deployed together in the same Kubernetes cluster - unless those have been planned and verified to co-exist.

### Container Isolation in Kubernetes Cluster
#### Namespaces  
Kernel namespaces should be used to provide process level isolation within a Kubernetes cluster. There are different types of kernel namespaces like PID and network. The default is to allocate one namespace per container application, in case several applications can be deployed in the same cluster.

