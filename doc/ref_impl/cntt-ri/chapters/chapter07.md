[<< Back](../)

# 7. Integration
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [7.1 Introduction](#7.1)
* [7.2 Pre-requisites](#7.2)
* [7.3 Requirements Gathering](#7.3)
* [7.4 Access and Connectivity](#7.4)
* [7.5 Descriptor File Preparations](#7.5)
* [7.6 Deployment Installer & Install Steps](#7.6)
* [7.7 Deployment Validations](#7.7)
* [7.8 CICD Tool Chain (use of, process, and scripts)](#7.8)
* [7.9 Jenkins Setup & Job Creation](#7.9)
* [7.10 Compliance Validation (steps, process)](#7.10)

<a name="7.1"></a>
## 7.1 Introduction

The purpose of this chapter is to establish an operational run-book containing sequences and steps explaining, with enough detail, how to install a Reference Implementation (RI).

The term Run-Book is synonymous with "Cookbook", and either term will be used interchangeably to indicate that if a user follows the steps or procedures in the "book", the expected result will be an RI identical to the lab utilized by CNTT for the instantiation and certification of RI-1.

It is assumed that the reader of this chapter has the skill set to install Common NFVI on their own labs.

*   Covers installers, automation, etc.
*   Integration of installers and components.

<a name="7.2"></a>
## 7.2 Prerequisites

The following are pre-requisites to be completed in advance of software deployments:

1.  Bare-metal validations: confirming delivery, rack, stack, of env and that env is "ready" for software deployments (e.g. BIOS, firmware, boot order, health, disk config, port / socket validations, MAC/NIC status, etc)

<a name="7.3"></a>
## 7.3 Requirements Gathering

Requirements gathering processes and steps:

1.  RA Requirements Gathering process
2.  Infra Requirements and Selection Process

<a name="7.4"></a>
## 7.4 Access & Connectivity

Logical steps for lab access and connectivity.

Sample steps provided mimic those utilized for POD10 test lab access.

<a name="7.5"></a>
## 7.5 Descriptor File Preparations

Before getting into the details of descriptor file preparation, it is important to discuss what constitutes infrastructure description, and what are the options available- the related works. The term infrastructure is used to refer to both hardware and software components that form the NFV environment, on which the virualized network functions are run.
As an end-user, one can define/describe the infrastructure using a select set of parameters. The below table categorizes these set of parameters, using which a user can describe the infrastructure, and which constitute any infrastructure definition. These parameters applies to any Installer available to the end-users, however, some installers may allow user to configure all parameters within a category, whereas some would allow just a subset of it. In addition, not all the categories would apply to all the installers.

|   |   |   |
| --- | --- | --- |
| GENERIC: Management (location, owner, etc.), Strategy, Globals, Tooling, Versioning, | HARDWARE: Vendor, Gen., BIOS, CPUs, Memory, Disks, NICs (PCI, MAC), etc. | PROFILES (HOST): Name, Disks &amp; Partitions, N/W-\&gt;NIC Mapping, OS, |
| NETWORK: Names, vlans, cidr, routes, ip, g/w, speed, mtu, bonding, etc. cidrs for diff. n/ws, container n/w, SRIOV, etc. | NODES: Networks and address, profile-mapping, metadata | SECRETS: Certificates, passphrases, publickeys, etc. |
| SOFTWARE: Software and nodes mapping, versions, registry | ACTIONS: Bootactions- custom scripts, drivers, etc. | OTHERS: Jumphosts-Defn., Network Services (NTP, DNS, etc) |

There have been various efforts around infrastructure description. Below list is the example of few such efforts:

1. OPNFV PDF/IDF
2. Airship Treasuremap Manifests
3. TripleO Heat Templates
4. Kayobe&#39;s YAML files.
5. Fuel Configuration in OPNFV-IDF.
6. GUI-Based configuration in compass.
7. OPNFV Apex&#39;s -  inventory, network and deploy settings.
8. Kubernetes CRDs

In this document, we will focus on first two OPNFV's descriptor files and Airship manifests.

### OPNFV Descriptor Files
The descriptor files – platform, infrastructure and software descriptor files – as used in OPNFV, provides an installer-agnostic way of describing both the hardware and software infrastructure. The main consumer of these descriptor files is the openstack (OPNFV) installer. For example, Fuel consumes these descriptor files to create its own set of templates/manifests, which will be used for deployment. The below figure summarizes how these descriptor files are consumed by the installers.


It is important for the generic descriptor files, apart from being generic, to be exhaustive enough to cover the parameters that are important and user-configurable. The importance of the parameters can be decided by various factors, and below we mention 3 of them:

1. New Use-Cases: If the parameter(s) helps in creating new use-cases. Ex: Different networking scenarios.
2. Feature: If the parameter(s) adds new feature to the installation. Ex: Security.
3. Simplify: If the parameter(s) simplifies the auto-creation of custom manifests. Ex: Metadata.

## **OPNFV Descriptor Files**

Currently, OPNFV descriptor files is generic, but not exhaustive enough. There is an ongoing effort to enhance the descriptor file schema. As mentioned in preceding section, there are three files – PDF, IDF and SDF. SDF is currently not well defined and used among the Installers. Below section describe the schema of these files, and enlists the parameters that are configurable by the user.

#### PDF

The below table summarizes the configurable parameters under PDF. Most of these parameters are self-explanatory.

| **Pod Details** |
| --- |
|   pod\_owner: Lab Owner |
|   contact: [email@address.com](mailto:email@address.com) |
|   lab: Linux Foundation |
|   location: Portland, Oregon, USA |
|   type: {production, development} |
|   link: http://wiki.opnfv.org/ |
|** #node** |
|   name: pod1-jump |
|   *node:* |
|     type: {baremetal or virtual} |
|     vendor: supermicro |
|     model: S2600JF |
|     arch: {x86\_64 or aarch64} |
|     cpus: 2 |
|     cpu\_cflags: {broadwell, haswell etc} |
|     cores: 10 |
|     memory: 32G |
|   *disks:* |
|     - name: {disk#number} |
|       disk\_capacity: {M,MB,G,GB,T,TB} |
|       disk\_type: {hdd,ssd,cdrom,tape} |
|       disk\_interface: {sata,sas,ssd,nvme,scsi,iscsi} |
|       disk\_rotation: {0,5400,7200,10000,15000} |
|   # operation system installed |
|   *os:* ubuntu-14.04 |
|   remote\_params: &amp;remote\_params |
|     type: {ipmi,amt,libvirt} |
|     versions: |
|       - 1.0 |
|       - 2.0 |
|     user: root |
|     pass: root |
|   *remote\_management:* |
|     \&lt;\&lt;: \*remote\_params |
|     address: 10.4.7.3/24 |
|     mac\_address:  |
|   # physical interface list |
|   *interfaces:* |
|     - name: {nic#number} |
|       address: 192.168.100.1 |
|       mac\_address:  |
|       vlan: {native or 1-4095} |

#### IDF

The Installer Descriptor File extends the PDF with POD related parameters required by the installer. This information may differ per each installer type and it is not considered part of the POD infrastructure. Currently, this file has only one section that is &#39;generic&#39; – the net\_config section. The below table describes the fields of the net\_config section.

The other section(s) in IDF are Installer specific.

| **key** | **Details** |
| --- | --- |
| interface | The index of the interface to use for this net. |
| vlan | VLAN tag (integer) or the string native. Required for each network. |
| ip-range | For now, only range start address is used. |
| network | Network segment address. Required for each network, except oob. |
| mask | Network segment mask. Required for each network, except oob. |
| gateway | Gateway IP address. Required for public, N/A for others. |
| dns | List of DNS IP addresses. Required for public, N/A for others. |

### **OPNFV Airship Manifests**

Airship is a collection of loosely coupled and interoperable open source tools that declaratively automate cloud provisioning - Infrastructure Deployment and Lifecycle Management of cloud.

Airship is a robust delivery mechanism for organizations who want to embrace containers as the new unit of infrastructure delivery at scale. Starting from raw bare metal infrastructure, Airship manages the full lifecycle of data center infrastructure to deliver a production-grade Kubernetes cluster with Helm deployed artifacts, including OpenStack-Helm. OpenStack-Helm is a set of Helm charts that enable deployment, maintenance, and upgrading of loosely coupled OpenStack services and their dependencies individually or as part of complex environments.

Airship allows operators to manage their infrastructure deployments and lifecycle through the declarative YAML documents that describe an Airship environment.

OPNFV-Airship, is an Airship-based installer project, which aims to come up with Reference Implementation of cloud and NFV infrastructure according to industry infrastructure architecture model(s), and support the VNF Testing and Certification running on top of the cloud and NFV infrastructure if so specified in the model(s).

The process of creating manifests that would be used for deployment will involve following steps:

1. Preparation - Collect the hardware, network topology, public keys, etc.
2. Authoring - Customizing the templates using the information collected in preparation phase.
3. Auto-Generation - Generating certificates.
4. Publishing - In OPNFV-Airship&#39;s Repository.

#### Preparation

The user needs to collect following information before starting the authoring process.

- IPMI details of the Nodes. For Intel pods, this information is available in the wiki. For ex:  Intel POD15.
- The Disk Information: User can boot into any system and run the below command: sudo lshw -c disk
- PCI Ids of NICs: User can boot into any system and run the below command: sudo lshw -c network businfo.
- The topology and underlay networking details. For Intel pods, this information is available in the wiki. For ex:  Intel POD15
- Public Keys of Users.
- Any custom requirements w.r.t  software.

#### Authoring Manifests

Airship is a declarative way of automating the deployment of a site. Therefore, all the deployment details are defined in the manifests.

The manifests are divided into three layers: global, type, and site. They are hierarchical and meant as overrides from one layer to another. This means that global is baseline for all sites, type is a subset of common overrides for a number of sites with common configuration patterns (such as similar hardware, specific feature settings, and so on), and finally the site is the last layer of site-specific overrides and configuration (such as specific IP addresses, hostnames, and so on). See [Deckhand](https://airship-deckhand.readthedocs.io/en/latest/overview.html#layering)[documentation](https://airship-deckhand.readthedocs.io/en/latest/overview.html#layering)here: [https://airshipit.readthedocs.io/projects/deckhand/en/latest/](https://airshipit.readthedocs.io/projects/deckhand/en/latest/) for more details on layering.

The global and type manifests can be used _as is_ unless any major differences from a reference deployment are required. In the latter case, this may introduce a new type, or even contributions to the global manifests.

The site manifests are specific for each site and are required to be customized for each new deployment. The specific documentation for customizing these documents is located here - [https://wiki.opnfv.org/display/AIR/Airship+Manifest+Creation+For+New+Sites](https://wiki.opnfv.org/display/AIR/Airship+Manifest+Creation+For+New+Sites)

Mainly, the customization is done for the following categories:

1. Deployment Configuration and Strategy
2. Profiles: Hardware Profile (Server, NICs, Disks, etc.) and Host Profiles
3. Nodes:
4. Network Definition: Network and Network Link
5. Software: Charts (Kubernetes, Undercloud Platform, Ceph, Openstack helm Infra, Open Stack Helm, Tenant-Ceph).
6. PKI-Catalog
7. Secrets: Publickeys and Passphrases of the users
8. Boot Actions
9. Rack
10. Region

#### Auto-Generation

Auto-generation phase involves generating certificates, which will be used by Kubernetes.  The process of generation of these certificates can be summarized with the steps, and the corresponding figure, below.

- Get airship treasuremap to the jumpserver. git clone [https://github.com/airshipit/treasuremap.git](https://github.com/airshipit/treasuremap.git)
- copy type/cntt folder opnfv-airship to treasuremap under type
- mv site defn. For pod10 to treasremap
- sudo tools/airship pegleg site -r /target collect intel-pod10 -s intel-pod10\_collected
- mkdir intel-pod10\_certs
- sudo tools/airship promenade generate-certs -o /target/intel-pod10\_certs /target/intel-pod10\_collected/\*.yaml
- cp intel-pod10\_certs/\*.yaml site/intel-pod10/secrets/certificates/
- mv site/intel-pod10 ../airship/site/


#### Publishing

The process of publishing involves submitting the manifests to opnfv-airship gerrit repo. It is important that the site-specific manifest, along with certificates, is present in &#39;site&#39; folder in opnfv-airship repository. This will be used for the deployment process and described in the subsequent section.

<a name="7.6"></a>
## 7.6 Deployment: Installer & Install Steps
The deployment is performed and managed from the 'jump-host' node. Any authorized user can login to this node.
### DNS Registration

### Setting up the Genesis Node
Install Ubuntu 16.04 (Standard ISO) on the genesis node (Ex: Node-1 in Intel-Pod10), this node will be used as seed for the rest of the environment. During installation ensure the following:
- UTC Timezone
- Proper hostname - As defined in site-definition
- Partitioning - As defined in site-definition
- Disable automatic updates

After Installation, perform the following:
- Configure networks according to the site-definition.
- Install proper kernel version - As defined in site-definition
- Install ntpdate/ntp
- Ensure password-less login from jumphost

### Install
As Airship is tooling to declaratively automate site deployment, the automation from the installer side is light. See [deploy.sh](https://github.com/opnfv/airship/blob/master/tools/deploy.sh).

User will need to export environment variables that correspond to the new site (keystone URL, node IPs, and so on). All these are captured in the site environment file - as described in the wiki page.

Once the prerequisites that are described in the Airship deployment guide (such as setting up Genesis node), and the manifests are created, you are ready to execute deploy.sh that supports Shipyard actions: deploy\_site and update\_site.

  $ tools/deploy.sh
  Usage: deploy.sh \&lt;site\_name\&gt; \&lt;deploy\_site|update\_site\&gt;

### Keeping track of the progress

The complete installation involves following process:

- Genesis node setup.
  - Software deployment.
- Baremetal provisioning of the nodes by Drydock
  - Control plane nodes
  - Dataplane nodes.
- Software deployment.

Once the Baremetal provisioning starts, user can use this link to check for the status:

http://&lt;IP-OF-GENESIS-NODE&gt;:31900/MAAS/#/nodes

Ex: for Pod10 - [http://10.10.100.21:31900/MAAS/#/nodes](http://10.10.100.21:31900/MAAS/#/nodes)

The software deployment process includes setting up multiple services on Kubernetes, under following namespaces – in that particular order:

- kube-system
- ceph
- ucp
- osh-infra
- tenant-ceph
- openstack

Below table provides some commands to run on **genesis node** to keep track of the software deployment.

| **Description** | **Command** |
| --- | --- |
| Show all pods for a particular namespace, that has completed. Check for any crashlookBackoff states | kubectl get pods -n \&lt;namespace-name\&gt; -o wide |grep -v Completed |
| Look at the logs of a any pod in any namespaceYou can follow it with --follow |  kubectl logs -n \&lt;namespace-name\&gt; \&lt;pod-name\&gt;   |
| Monitoring Ceph StatusShould be HEALTH\_OK  | kubectl exec -it -n ceph \&lt;ceph-mon-\*\*\*\&gt; -- ceph -sceph-mon-\*\*\*: Name of any monitor instance. |
| Get services running, and describe a service | kubectl get svc -n openstackkubectl describe svc -n openstack ingress |

This link [https://airship-treasuremap.readthedocs.io/en/latest/troubleshooting\_guide.html](https://airship-treasuremap.readthedocs.io/en/latest/troubleshooting_guide.html) will provide all the details for trouble shooting any issues.

Once successfully deployed, user can use this link to access the horizon dashboard.
- http://dashboard-airship.\&lt;pod-name\&gt;.opnfv.org

In addition to that, users can also use these links to track the metrics and logs, respectively:

- http://kibana-airship.\&lt;pod-name\&gt;.opnfv.org/

- http://grafana-airship.\&lt;pod-name\&gt;.opnfv.org/login

<a name="7.7"></a>
## 7.7 Deployment Validations

Details explaining:
- Validation Tests Run
- Expected outpus
- Explanation of Pass/Fail
- Disposition, or next steps, based on test results (e.g. handling of failures, handoff to next tier with passing results)

<a name="7.8"></a>
## 7.8 CICD Tool Chain (use of, process, and scripts)]

Placeholder to describe the CICD tool chain used in RI validations.

Include flow diagram.

<a name="7.9"></a>
## 7.9 Jenkins Setup & Job Creation

Placeholder to describe the process, access, steps, instance, etc, information for the setup of Jenkins, the jobs required for validation, and the results dashboard.

<a name="7.10"></a>
## 7.10 Compliance Validation (steps, process)

Placholder to describe the purpose, steps, and process, using the Jenkins Jobs, Tool Chain, and Test Case requirements mapping to perform validations.
