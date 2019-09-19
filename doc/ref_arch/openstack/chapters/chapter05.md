[<< Back](../../openstack)

# 5. Interfaces and APIs
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 Introduction](#5.1)
* [5.2 Core OpenStack Services APIs.](#5.2)
* [5.3 Consolidated Set of APIs.](#5.3)

<a name="5.1"></a>
## 5.1 Introduction.

This chapter presents a consolidated set of OpenStack Service APIs corresponding to the ETSi Vi-Nf inetrfaces. The Openstack Pike version is used as the baseline for these APIs and CLIs. The Chapter presents the APIs for the core OpenStack services defined in Chapter 3 and later in teh Chapter a consolidated view of these and other APIs that would be of interest.

<a name="5.2"></a>
## 5.2. Core OpenStack Services APIs.

### 5.2.1. Keystone
| **OpenStack Service** | **Link for API and CLI** | **API/client Baseline Version** |
|------------------|----------------------------------------------------|-------------------|
|Identity: Keystone | https://docs.openstack.org/api-ref/identity/v3/index.html | Version 3.10 |
|Identity: Keystone | https://docs.openstack.org/python-keystoneclient/latest/using-api-v3.html | Version 3.10 |

### 5.2.2 Glance
| **OpenStack Service** | **Link for API and CLI** | **API/Client Baseline Version** |
|------------------|----------------------------------------------------|-------------------|
| Imaging: Glance | https://docs.openstack.org/api-ref/image/v2/index.html#images | Version 2.0 |
| Imaging: Glance | https://docs.openstack.org/python-glanceclient/latest/ | Version 2.0 |

### 5.2.3. Cinder 
| **OpenStack Service** | **Link for API and CLI** | **API/CLI Baseline Version** |
|------------------|----------------------------------------------------|-------------------|
|Block Storage: Cinder | https://docs.openstack.org/api-ref/block-storage/v3/index.html#api-versions/a> | Version 3.0 |

### 5.2.4. Swift
| **OpenStack Service** | **Link for API and CLI** | **API/CLI Baseline Version** |
|------------------|----------------------------------------------------|-------------------|
| Object Storage: Swift | https://docs.openstack.org/api-ref/object-store/ | Version 1.0 |
| Object Storage: Swift |https://docs.openstack.org/python-swiftclient/latest/ | Version 1.0 |

### 5.2.5. Neutron
| **OpenStack Service** | **Link for API and CLI** | **API/CLI Baseline Version** |
|------------------|----------------------------------------------------|-------------------|
| Networking: Neutron | https://docs.openstack.org/api-ref/network/ | Version 2.0 |
| Networking: Neutron | https://docs.openstack.org/python-neutronclient/latest/cli/index.html | Version 2.0 |

### 5.2.6. Nova
| **OpenStack Service** | **Link for API and CLI** | **API/CLI Baseline Version** |
|--------------|------------------|---------------------------------------|
| Compute: Nova | https://docs.openstack.org/api-ref/compute/ | Version 2.1 |
| Compute: Nova | https://docs.openstack.org/python-novaclient/latest/cli/index.html | Version 2.1 |

### 5.2.7. Ironic
| **OpenStack Service** | **Link for API and CLI** | **API/CLI Baseline Version** |
|------------------|----------------------------------------------------|-------------------|
| Bare Metal: Ironic | https://docs.openstack.org/api-ref/baremetal/ | Version 1.0 |
| Bare Metal: Ironic | https://docs.openstack.org/python-ironicclient/latest/cli/index.html | Version 1.25 |

### 5.2.8. Heat
|**OpenStack Service** | **Link for API and CLI** | **API/CLI Baseline Version** |
|------------------|----------------------------------------------------|-------------------|
| Bare Metal: Heat | https://docs.openstack.org/api-ref/orchestration/v1/index.html#api-versions | Version 1.0 |
| Bare Metal: Heat | https://docs.openstack.org/python-heatclient/latest/ | Version 1.25 |


<a name="5.3"></a>
## 5.3. Consolidated Set of APIs.

### 5.3.1. OpenStack Interfaces
This section illustrates some of the Interfaces provided by OpenStack; the exhaustive list of APIs is available at https://docs.openstack.org/api-ref/ and CNTT standard is to use the latest version v3. OpenStack REST APIs are simple to interact with using either of two options. Clients can either call the APIs directly using the HTTP or REST library, or they can use one of the many programming language specific cloud libraries. 

**APIs**
| OpenStack Service | Link for API list | API Baseline Version |
|------------------|--------------------|------------------------|
| Identity: Keystone | https://docs.openstack.org/api-ref/identity/v3/index.html?expanded=#identity-api-operations  | Version 3.10 |
| Compute: Nova | https://docs.openstack.org/api-ref/compute/  | Version 2.1 |
| Networking: Neutron | https://docs.openstack.org/api-ref/network/  | Version 2.0 |
| Imaging: Glance | https://docs.openstack.org/api-ref/image/v2/index.html#images  | Version 2.0 |
| Block Storage: Cinder | https://docs.openstack.org/api-ref/block-storage/v3/index.html#api-versions  | Version 3.0 |
| Object Storage: Swift | https://docs.openstack.org/api-ref/object-store/  | Version 1.0 |
| Orchestration: Heat | https://docs.openstack.org/api-ref/orchestration/v1/index.html#api-versions  | Version 1.0 |
| Bare Metal: Ironic |  |  |
| Acceleration: Cyborg | https://docs.openstack.org/api-ref/accelerator/v1/index.html  | Version 1.0 |

**CLIs**
| OpenStack Service | Link to Client | Client Baseline Version |
|------------------|--------------------|------------------------|
| Identity: Keystone | https://docs.openstack.org/python-keystoneclient/latest/using-api-v3.html | Version 3.10 |
| Compute: Nova | https://docs.openstack.org/python-novaclient/latest/cli/index.html | Version 2.1 |
| Networking: Neutron | https://docs.openstack.org/python-neutronclient/latest/cli/index.html | Version 2.0 |
| Imaging: Glance | https://docs.openstack.org/python-glanceclient/latest/ | Version 2.0 |
| Block Storage: Cinder | https://docs.openstack.org/python-cinderclient/latest/ | Version 3.0 |
| Object Storage: Swift | https://docs.openstack.org/python-swiftclient/latest/ | Version 1.0 |
| Orchestration: Heat | https://docs.openstack.org/python-heatclient/latest/ | Version 1.0 |
| Bare Metal: Ironic | https://docs.openstack.org/python-ironicclient/latest/cli/index.html  | Version 1.25 |
| Acceleration: Cyborg | https://docs.openstack.org/python-cyborgclient/latest/ | Version 1.0 |
| OpenStack Client (python) | https://docs.openstack.org/python-openstackclient/pike/index.html  | Version 3.2.1 |

### 5.3.2. Kubernetes Interfaces
The Kubernetes APIs are available at https://kubernetes.io/docs/concepts/overview/kubernetes-api/. 

### 5.3.3. KVM Interfaces
The KVM APIs are documented in Section 4 of the document https://www.kernel.org/doc/Documentation/virtual/kvm/api.txt. 

#### 5.3.3.1. Libvirt Interfaces
The Libvirt APIs are documented in https://libvirt.org/html/index.html.

<!--
### 5.3.4. vSphere/ESXi APIs
The ESXi APIs are documented together with vCenter and available at https://code.vmware.com/apis/62/vcenter-management
-->
