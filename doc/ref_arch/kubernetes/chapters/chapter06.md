[<< Back](../../kubernetes)

# 6. Security
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 Heading](#6.2)
* [6.3 Heading](#6.3)

<a name="6.1"></a>
## 6.1 Introduction
The adoption of cloud-native allows development teams to move fast, deploy software efficiently, and operate at an unprecedented scale. 
Cloud-native applications offer the benefits by providing applications as small microservices (either containers or serverless), and managing them through DevOps processes. To build these applications, organisations need a cloud-native infrastructure which provides flexibility and enough services for developers. Cloud-native infrastructures should provide a platform for the build and release team to effectively perform continuous delivery of its applications, with close to zero human intervention. With Cloud-native, the industy requires a radically different apporach to security in contrast to monolithic architecture. 

<a name="6.2"></a>
##  6.2 Principles
### Cloud Native Security
The following are core principles to consider when securing cloud-native applications and infrastructure;

- Deploy only secure applications and trusted codes
- Only deploy applications from validated and verified images
- Only deploy applications from truested registries
- Containers orchestration (Kubernetes) must be secure with administrative boundaries between tenants
- Network segmentation using security zoning and network standards must be followed when deploying containers. 
- The Host OS running the containers must be hardened
- Use container-aware runtime defense tools.

<a name="6.3"></a>
## 6.3 Security Perimeters
When applications or workloads run on Kubernetes, there are several layers which come into picture that govern the security. Each of these layers need to be secured within their perimeters. The various layers that come into picture are:

- Container Registry: A container registry is a repostory to manage container images. The access to container registry needs to be secured in order to provide a controlled access.
- Container Images: Containers image is a unit of pre-packages application and all its dependencies. Before loading them to container registry, they need to be made secured by performing various checks like vulnerability analysis, scans etc. These should also be signed and from trusted sources.
- Containers: A container is a running instance of a container image. The containers need to be prevented from accessing the underlying OS like loading of kernel modules, checking the privelege level of containers.
- Pods: A pod is a collection of containers.
- Node: A node can either be a master node (where all the core services are running) or a worker node (where the workloads are running). A node in an unsecured boundary can lead to a potential threat to the running workloads. 
- Cluster: A cluster comprises of a collection of nodes which contain the control plane as well as the data plane. It also provides API endpoints for interacting with the cluster. The communication over these APIs needs to be secured via different mechanisms like TLS encryption, API authentication via LDAP etc.

<a name="6.4"></a>
## 6.4 Heading

