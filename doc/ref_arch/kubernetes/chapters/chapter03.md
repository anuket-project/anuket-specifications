[<< Back](../../openstack)

# 3. High Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [3.1 Introduction](#3.1)
* [3.2 Infrastructure Services](#3.2)
    * [3.2.1 Container Runtime Services](#3.2.1)
    * [3.2.2 Container Networking Services](#3.2.2)
    * [3.2.3 Container Package Managers](#3.2.3)
* [3.3 Heading](#3.3)

<a name="3.1"></a>
## 3.1 Introduction

<a name="3.2"></a>
## 3.2 Infrastructure Services

> This chapter shall list the services provided by the infrastructure. Some example of these services can be: log collection, monitoring, health check, load balancer. For the shake of clarity CaaS services should be also listed, like container lifecycle management or networking services.

<a name="3.2.1"></a>
### 3.2.1 Container Runtime Services

> This chapter should describe considerations about the services of container runtimes.

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
### 3.2.3 Container Package Managers

> This chapter shoud describe what type of container package manager (e.g.: Helm, [CNAB](https://cnab.io/)) related considerations 

<a name="3.3"></a>
## 3.3 Heading
