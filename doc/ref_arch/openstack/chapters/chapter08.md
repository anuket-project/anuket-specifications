[<< Back](../../openstack)

# 8. Gaps, Innovation, and Development

## Table of Contents
* [8.1 Introduction](#8.1)
* [8.2 The Gaps](#8.2)
  * [8.2.1 Autoscaling](#8.2.1)

<a name="8.1"></a>
## 8.1 Introduction
The purpose of this chapter is to identify the gaps between what is required for automated deployment of VNFs on Cloud Infrastructure frameworks and the framework offered by OpenStack. 
Once gaps are identified, the next step will be to propose a plan to address these gaps. 
The most obvious way to address the gaps will be to propose a set of APIs in the upstream OpenStack community

<a name="8.2"></a>
## 8.2 The Gap

<a name="8.2.1"></a>
### 8.2.1 Autoscaling
With regards to resource autoscaling ([gen.scl.01](./chapter02.md#241-general-recommendations)) it is recommended that the NFVO/VNFM manages the policy and triggers a scale-up or scale-down action based on application telemetry, event, AI, or ML etc. While the use of telemetry and alarming system can trigger a scaling operation based on resource utilisation, without application context this may not provide the granularity or reaction time required by the application. It is therefore suggested that an OpenStack scaling operation is called using an appropriate autoscaling web-hook by the NFVO/VNFM.

For more information on auto-scaling with Heat please see: https://docs.openstack.org/senlin/latest/scenarios/autoscaling_heat.html. Please note that the OpenStack Senlin service is still under development with major architectural changes made in the OpenStack Ussuri release.

Please note: physical compute node autoscaling is out of scope.
