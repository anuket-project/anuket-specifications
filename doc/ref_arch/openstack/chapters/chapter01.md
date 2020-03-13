[<< Back](../../openstack)

# 1. Overview
<p align="right"><img src="../figures/bogo_dfp.png" alt="Dickering over Fine Points" title="Bogo: Dickering over Fine Points" width="35%"/></p>

## Table of Contents
* [1.1 Introduction.](#1.1)
  * [1.1.1 Vision](#1.1.1)
* [1.2 Use Cases](#1.2)
* [1.3 Terminology.](#1.3)
* [1.4 Principles](#1.4)
* [1.5 CNTT OpenStack Reference Release](#1.5)
* [1.6 Document Organisation](#1.6)


<a name="1.1"></a>
## 1.1 Introduction
This Reference Architectures is focussed on OpenStack as the VIM chosen based on the criteria laid out in the [Reference Model](../../../ref_model/chapters/chapter01.md). OpenStack has the advantages of being a mature and widely accepted Open Source technology; a strong ecosystem of vendors that support it, the OpenStack Foundation for managing the community, and, most importantly, it is widely deployed by the global operator community for both internal infrastructure and external facing products and services.  This means that the operators have existing staff with the right skill sets to support an NFVI deployment into development, test and production. Another reason to chose OpenStack is that it has a large active community of vendors and operators, which means that any code or component changes needed to support the Common Telecon NFVI requirements can be managed through the existing project communities processes to add and validate the required features through well established mechanisms.

<a name="1.1.1"></a>
## 1.1.1. Vision
The ultimate goal is that the OpenStack-based CNTT Reference Architecture will host NFV workloads, primarily VNFs, of interest to the Common NFVI Telco community.  Initially the OpenStack-based Reference Architecture would be used for testing and validating VNFs that can then be deployed in compatible operator clouds.   The Reference Architecture document can be used by operators to deploy compliant production infrastructure.  

<a name="1.2"></a>
## 1.2 Use Cases
Several NFV use cases are documented in OpenStack. For more examples and details refer to the OpenStack docs found at the following link: https://docs.openstack.org/arch-design/use-cases.html  Examples include:

  - **Overlay networks**: The overlay functionality design includes OpenStack Networking in Open vSwitch GRE tunnel mode. In this case, the layer-3 external routers pair with VRRP, and switches pair with an implementation of MLAG to ensure that you do not lose connectivity with the upstream routing infrastructure.

  - **Performance tuning**: Network level tuning for this workload is minimal. Quality of Service (QoS) applies to these workloads for a middle ground Class Selector depending on existing policies. It is higher than a best effort queue but lower than an Expedited Forwarding or Assured Forwarding queue. Since this type of application generates larger packets with longer-lived connections, you can optimize bandwidth utilization for long duration TCP. Normal bandwidth planning applies here with regards to benchmarking a session’s usage multiplied by the expected number of concurrent sessions with overhead.

  - **Network functions**: Network functions is a broad category but encompasses workloads that support the rest of a system’s network. These workloads tend to consist of large amounts of small packets that are very short lived, such as DNS queries or SNMP traps. These messages need to arrive quickly and do not deal with packet loss as there can be a very large volume of them. There are a few extra considerations to take into account for this type of workload and this can change a configuration all the way to the hypervisor level. For an application that generates 10 TCP sessions per user with an average bandwidth of 512 kilobytes per second per flow and expected user count of ten thousand concurrent users, the expected bandwidth plan is approximately 4.88 gigabits per second. The supporting network for this type of configuration needs to have a low latency and evenly distributed availability. This workload benefits from having services local to the consumers of the service. Use a multi-site approach as well as deploying many copies of the application to handle load as close as possible to consumers. Since these applications function independently, they do not warrant running overlays to interconnect tenant networks. Overlays also have the drawback of performing poorly with rapid flow setup and may incur too much overhead with large quantities of small packets and therefore we do not recommend them. QoS is desirable for some workloads to ensure delivery. DNS has a major impact on the load times of other services and needs to be reliable and provide rapid responses. Configure rules in upstream devices to apply a higher Class Selector to DNS to ensure faster delivery or a better spot in queuing algorithms.

<a name="1.3"></a>
## 1.3 Terminology
Unless specific OpenStack terms are used, the terminology can be found [CNTT Reference Model Terminology](../../../ref_model/chapters/glossary.md#1.1).  

Add add any OpenStack specific terms here.

<!-- <p align="center"><img src="../figures/ref_arch_ch01_e2e.png" alt="E2E" title="E2E" width="100%"/></p><p align="center"><b>Figure 1-1:</b> E2E</p> -->

<a name="1.4"></a>
## 1.4 Principles

Open Stack Reference Architecture must obey to the following set of principles:
- [CNTT Reference Model Principles](../../../ref_model/chapters/chapter01.md#1.3)
- [CNTT Reference Architecture Principles](../../#principles)

**Open Stack specific principles**

OpenStack considers the following Four Opens essential for success:
- Open Source
- Open design
- Open Development
- Open Community

This OpenStack Reference Architecture is organised around the three major NFVI resource types as core services of compute, storage and networking, and a set of shared services of identity management, image management, graphical user interface, orchestration engine, etc. 


<a name="1.5"></a>
## 1.5 CNTT OpenStack Reference Release

This Reference Architecture document conforms to the OpenStack Pike release. While many features and capabilities are conformant with many OpenStack releases, this document will refer to features, capabilities and APIs that are part of the OpenStack Pike release. For ease, this CNTT Reference Architecture version can be referred to as "RA-1 OSTK Pike."

<a name="1.6"></a>
## 1.6 Document Organisation

The Reference Architecture requirements and the traceability where in this document the requirement is addressed is documented in Chapter 2. The intent of this document is to address all of the mandatory ("must") requirements and the most useful of the other optional ("should") requirements. Chapter 3 and 4 cover the NFVI resources and the core OpenStack services, while the APIs are covered in Chapter 5. Chapter 6 covers the implementation and enforcement of security capabilities and controls. Life Cycle Management of the NFVI and VIM are covered in Chapter 7 with stress on Logging, Monitoring and Analytics (LMA), configuration management and some other operational items, Please note that Chapter 7 is not a replacement for the implementation, configuration and operational documentation that accompanies the different OpenStack distributions. Chapter 8 identifies certain Gaps that currently exist and plans on how to address them. For example, Service Function Chaining support needs to be addressed to realise the full potential and value of SDN and NFV.



