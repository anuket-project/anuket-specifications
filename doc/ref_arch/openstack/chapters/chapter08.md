[<< Back](../../openstack)

# 8. Gaps, Innovation, and Development
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction](#8.1)
* [8.2 The Gaps](#8.2)
* [8.3 OpenStack Release Gaps](#8.3)

<a name="8.1"></a>
## 8.1 Introduction
The purpose of this chapter is to identify the gaps between what is required for automated deployment of VNFs on NFVI frameworks and framework offered by OpenStack. 
Once gaps are identified, the next step will be to propose a plan to address these gaps. 
The most obvious way to address the gaps will be to propose a set of APIs in the upstream OpenStack community

<a name="8.2"></a>
## 8.2 The Gaps


<a name="8.3"></a>
## 8.3 OpenStack Release Gaps
Section contains the key differences between the chosen CNTT baseline version (Train), the current version for RI (Ocata) and the potential future version for RI (Stein).
The table below gives only an
overview of the differences. For detailed changes, please check the
[https://releases.openstack.org](https://releases.openstack.org).

| Service Name | OpenStack (Ocata) (RI version) | OpenStack (Train)) (CNTT baseline) | OpenStack (Stein) (potential future RI version) |
| --- | --- | --- | --- |
| Keystone | 3.8 | 3.13<br>- Support for delegating fine-grained privileges.<br>- Supports the admin, member, and reader default roles across system-scope, domain-scope, and project-scope.<br>- Different role API uses new default policies that make it more accessible to end users and administrators in a secure way.  | 3.12<br>- Support for project tags, application credential, domain level resource limits, JSON Web Tokens.<br> - Introduced system scoped roles<br> - Introduced new role 'reader' along with 'member' and 'admin' |
| Glance | 2.5 | 2.9<br>- Support for compressed  container formats.<br>- Block Storage service always creates a new secret in Barbican when it uploads a volume as an image.<br- > | 2.7<br>- Version v1 is removed<br>- Support for hidden images, interoperable image import using image data (glance-direct) or image URL(web-download), <br>- Fixed OpenStack Security Note [OSSN-0075](https://wiki.openstack.org/wiki/OSSN/OSSN-0075)<br>- Multi backend support to configure multiple stores|
| Cinder | 3.27 | 3.59| 3.59<br>- Support for multi attach and deferred deletion for RBD driver<br>- Support for image signature verification when creating volume from image |
| Nova | 2.42 | 2.79<br>- Support for servers with a NUMA topology, pinned CPUs and/or huge pages, and SR-IOV ports attached when using the libvirt compute driver.<br>- Support for hardware-based encryption of guest memory to protect users against attackers or rogue administrators snooping on their workloads. | 2.72<br>- Support for vGPUs<br>- Support for volume type in server create API<br>- Support to create servers with ports that have QoS minimum bandwidth rule<br>- Security enhancements when using Glance signed images |
| Swift | 1.0 | 1.0 | 1.0 |
| Neutron | 2.0 | 2.0<br- Support for Smart NIC in ML2/OVS mechanism driver to bind the Neutron port for the baremetal host with Smart NIC.<br>- Introrduced support for a notifier that sends notifications on relevant resource events/changes to the Openstack Baremetal service (ironic). | 2.0 |
| Orchestration | 1.0 | 1.0 | 1.0 |

Additionally, Stein release also provide an upgrade check before actually upgrading any of the services. 
See more details on [upgrade-check](https://governance.openstack.org/tc/goals/selected/stein/upgrade-checkers.html).

