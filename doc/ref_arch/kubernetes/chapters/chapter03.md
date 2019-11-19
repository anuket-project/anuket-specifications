[<< Back](../../openstack)

# 3. High Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [3.1 Introduction](#3.1)
* [3.2 Infrastructure Services](#3.2)
    * [3.2.1 Container Runtime Services](#3.2.1)
    * [3.2.2 Container Networking Services](#3.2.2)
    * [3.2.3 Container Storage Services](#3.2.3)
    * [3.2.4 Container Package Managers](#3.2.4)
* [3.3 Heading](#3.3)

<a name="3.1"></a>
## 3.1 Introduction

<a name="3.2"></a>
## 3.2 Infrastructure Services

> This chapter shall list the services provided by the infrastructure. Some example of these services can be: log collection, monitoring, health check, load balancer. For the shake of clarity CaaS services should be also listed, like container lifecycle management or networking services.

<a name="3.2.1"></a>
### 3.2.1 Container Runtime Services

The Container Runtime is the component that runs within a Host Operating System (OS) and manages the underlying OS functionality such as cgroups and namespaces (in Linux) in order to provide a service within which container images can be launched.  For the purposes of this document the Container Runtime is not just the true 'runtime' but also the container 'engine' that manages the container-related infrastructure such as networking, security, storage and distributed state.  Essentially the component that pulls an image from a registry, unpacks it and runs it.

There are a number of different container runtimes, ranging from low-level runtimes that are essentially scripts that manage the low-level OS primitives, through to full application-centric "high level" container runtimes that include a comprehensive API and other developer-friendly features.

A Container Runtime used in a Reference Implementation that is conformant with this Reference Architecture is compliant with the Kubernetes Container Runtime Interface (https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md).

Any container runtime sed in a Reference Implementation that is conformant with this Reference Architecture is compliant with the Open Container Initiative (OCI) runtime specification (https://github.com/opencontainers/runtime-spec/blob/master/spec.md).



<a name="3.2.2"></a>
### 3.2.2 Container Networking Services

> This chapter should discuss networking related considerations of container network services, like:
> * Ingress and any limitations on protocol or raw interface support
> * Dependencies on external loadbalancers
> * Regular service mesh related considerations
> * Network Service Mesh related considerations
> * Number of interfaces and IP addresses to be supported by a pod
> * IPv6 single and dual stack needs

<a name="3.2.3"></a>
### 3.2.3 Container Storage Services

> This shapter should discuss storage services provided by the reference architecture.

<a name="3.2.4"></a>
### 3.2.4 Kubernetes Application package manager

To manage complex applications consisting from several pods the reference architecture may provide support for a Kubernetes Application package manager. The package manager may be able to manage the lifecycle a set of pods and provide a framework to customize a set of parameters for the deployment.

<a name="3.3"></a>
## 3.3 Heading
