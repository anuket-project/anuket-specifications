[<< Back](../../openstack)

# 8. Gaps, Innovation, and Development
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction](#8.1)
* [8.2 The Gaps](#8.2)
  * [8.2.1 Autoscaling](#8.2.1)
* [8.3 OpenStack Release Gaps](#8.3)

<a name="8.1"></a>
## 8.1 Introduction
The purpose of this chapter is to identify the gaps between what is required for automated deployment of VNFs on NFVI frameworks and framework offered by OpenStack. 
Once gaps are identified, the next step will be to propose a plan to address these gaps. 
The most obvious way to address the gaps will be to propose a set of APIs in the upstream OpenStack community

<a name="8.2"></a>
## 8.2 The Gap

<a name="8.2"></a>
### 8.2.1 Autoscaling
With regards to resource autoscaling (req.gen.scl.01) it is recommended that the NFVO/VNFM manages the policy and triggers a scale-up or scale-down action based on application telemetry, event, AI, or ML etc. While the use of telemetry and alarming system can trigger a scaling operation based on resource utilisation, without application context this may not provide the granularity or reaction time required by the application. It is therefore suggested that an OpenStack scaling operation is called using an appropriate autoscaling web-hook by the NFVO/VNFM.

For more information on auto-scaling please see: https://docs.openstack.org/senlin/latest/scenarios/autoscaling_heat.html. Please note that the OpenStack Senlin service is still under development with major architectural changes made in the OpenStack Ussuri release. It might be possible for the next version of this RA to recommend Senlin for auto-scaling.

Please note: physical compute node autoscaling is out of scope.

<a name="8.3"></a>
## 8.3 OpenStack Release Gaps
Section contains the key differences between the chosen baseline version (Pike) and chosen version for RI (Ocata).
Along with those two versions, it also documents the differences of Pike and Stein. The table below gives only an
overview of the differences. For detailed changes, please check the
[https://releases.openstack.org](https://releases.openstack.org).

| Service Name | OpenStack (Ocata) (RI version) | OpenStack (Pike) (CNTT baseline) | OpenStack (Stein) |
| --- | --- | --- | --- |
| Keystone | 3.8 | 3.8 | 3.12<br>- Support for project tags, application credential, domain level resource limits, JSON Web Tokens.<br> - Introduced system scoped roles<br> - Introduced new role 'reader' along with 'member' and 'admin' |
| Glance | 2.5 | 2.5 | 2.7<br>- Version v1 is removed<br>- Support for hidden images, interoperable image import using image data (glance-direct) or image URL(web-download), <br>- Fixed OpenStack Security Note [OSSN-0075](https://wiki.openstack.org/wiki/OSSN/OSSN-0075)<br>- Multi backend support to configure multiple stores|
| Cinder | 3.27 | 3.43 | 3.59<br>- Support for multi attach and deferred deletion for RBD driver<br>- Support for image signature verification when creating volume from image |
| Nova | 2.42 | 2.53<br>- os-hosts has been removed and accomodated by os-hypervisors and os-services<br> | 2.72<br>- Support for vGPUs<br>- Support for volume type in server create API<br>- Support to create servers with ports that have QoS minimum bandwidth rule<br>- Security enhancements when using Glance signed images |
| Swift | 1.0 | 1.0 | 1.0 |
| Neutron | 2.0 | 2.0 | 2.0 |
| Orchestration | 1.0 | 1.0 | 1.0 |

Additionally, Stein release also provide an upgrade check before actually upgrading any of the services. 
See more details on [upgrade-check](https://governance.openstack.org/tc/goals/selected/stein/upgrade-checkers.html).
