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

<a name="6.2"></a>
## 6.2 Heading

<a name="6.3"></a>
## 6.3 Heading

