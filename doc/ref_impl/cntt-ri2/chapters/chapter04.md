[<< Back](../)

# 4. Operational Runbook
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Prerequisites](#4.2)
* [4.3 Installation of the Reference Implementation](#4.3)
  * [4.3.1 Host Provisioning](#4.3.1)
  * [4.3.2 Kubernetes Provisioning](#4.3.2)
* [4.4 Validation of the Reference Implementation](#4.4)
* [4.5 Automation Tooling](#4.5)

<a name="4.1"></a>
## 4.1 Introduction

This chapter documents the steps to deploy Kubernetes based Reference Implementation (RI-2) according to RA-2. The entire deployment has been tested in Anuket Labs as a part of the [Anuket Kuberef project](https://wiki.anuket.io/display/HOME/Kuberef), that aims to deliver RI-2 based on RA-2 specifications. The Kuberef project stores all the code needed to deploy RI-2 and hence serves as a reference platform for CNF vendors to develop and test against. Currently, Kuberef supports deployments on both baremetal, as well as pre-provisioned infrastructure (for e.g. offered by baremetal providers like Equinix Metal, etc.).

The entire installation is divided into two stages - Host provisioning and Kubernetes provisioning. Host provisioning is the operation of preparing a host before the software stack can be installed on them. This includes (and not limited to) installing an operating system, configuring network so that the hosts are reachable via SSH, configuring storage, etc. This stage can be skipped when using pre-provisioned hardware, infrastructure providers, etc. The Kubernetes provisioning stage is agnostic to the host provisioning stage, in that there is no dependency between the installer used for the Kubernetes provisioning stage and any tools used in the host provisioning stage.

<a name="4.2"></a>
## 4.2 Prerequisites

You need one physical server acting as a jump server along with minimum of two additional servers on which RI-2 will be deployed. Please refer to [Chapter 3](./chapter03.md) for detailed information on the server and network specifications.

<a name="4.3"></a>
## 4.3 Installation of the Reference Implementation

This section describes how to get started with RI-2 deployment via [Kuberef](https://gerrit.opnfv.org/gerrit/q/project:kuberef).

For the host provisioning stage, the [Cloud Infra Automation Framework](https://docs.nordix.org/submodules/infra/engine/docs/user-guide.html#framework-user-guide) hosted by Nordix Foundation is used. This framework uses [Bifrost](https://docs.openstack.org/bifrost/latest/) for provisioning virtual and bare-metal hosts. It performs this automated deployment by using Ansible playbooks and [Ironic](https://docs.openstack.org/ironic/latest/). For Kubernetes provisioning, [Bare Metal Reference Architecture (BMRA)](https://builders.intel.com/docs/networkbuilders/container-bare-metal-for-2nd-generation-intel-xeon-scalable-processor.pdf) is being used. This framework uses scripts available on [Github](https://github.com/intel/container-experience-kits/tree/v21.03) (version v21.03).

<a name="4.3.1"></a>
### 4.3.1 Installation on Bare Metal Infratructure

Start by cloning the Kuberef repository. Before you are able to run the installer some prerequisites must be installed. Details and installation steps can be found in `docs/release/installation/deployment-guide.rst`. 

Before initiating a deployment, two configuration templates, referred to as POD Descriptor File (PDF) and Installer Descriptor File (IDF) in Anuket terminology need to be defined under `hw_config/<vendor>`. Both PDF and IDF files are modeled as YAML schema.

A PDF is a hardware configuration template that includes hardware characteristics of the jumphost host and the set of compute/controller hosts. For each host, the following characteristics should be defined:
- CPU, disk and memory information
- Remote management parameters
- Network interfaces list including name, MAC address, IP address, link speed

IDF includes information about network information required by the installer. All the networks along with possible VLAN, DNS, and gateway information should be defined here. The IDF file also contains configuration options for the Kubernetes deployment using BMRA. These options are described in greater detail below.

More details regarding these descriptor files as well as their schema are very well documented in [RI-1 Chapter 8](../../cntt-ri/chapters/chapter08.md#opnfv-descriptor-files-1).

For the high availability requirement at least 3 nodes should be running as master with etcd enabled, but only a single master (and worker) is required to deploy the cluster. Node roles are configured through the vendor specific IDF file.

Most of the configuration options in `hw_config/{deployment}/idf.yaml` shown below are set to specific values according to RA-2 requirements. Some of them might need to be changed depending on the hardware, such as the NIC and CPU configuration.

```
bmra:
  profile: full_nfv               # BMRA profile for K8s provisioning - Should not be changed
  network_roles:
    sriov:
      - name: eno2                # PF interface name
        pci: "19:00.1"            # PCI ID of the interface (bus:device.function)
        pf_driver: i40e           # Driver for the physical function (PF)
        vf_driver: iavf           # Driver for the virtual function (VF)
    sriov_dpdk:
      - name: eno4
        pci: "19:00.3"
        pf_driver: i40e
        vf_driver: vfio-pci
  device_roles:
#    qat:                         # Only uncomment if QAT is enabled
#      - name: crypto01           # QAT device name
#        pci: "0000:ab:00.0"      # PCI ID of the device (bus:device.function)
#        mod_type: qat_c62x       # Kernel module [qat_dh895xcc,qat_c62x,qat_c3xxx,qat_200xx,qat_c4xxx,qat_d15xx]
#        pci_type c6xx            # PCI driver ID [dh895xcc,c6xx,c3xxx,d15xx,200xx,c4xxx]
#        vfs: 4                   # Number of VFs to be created for PCI ID
  features:
    sriov:
      enable: true                # Enable SR-IOV
      sriov_vfs_per_port: 2       # Number of VFs to be created for each interface in network_roles:sriov above
      sriov_dpdk_vfs_per_port: 4  # Number of VFs to be created for each interface in network_roles:sriov_dpdk above
    sriov_cni: true               # Enable SR-IOV CNI plugin
    sriov_net_dp: true            # Enable SR-IOV Network Device Plugin
    hugepages:
      enable: true                # Enable hugepages
      default: 2M                 # Default hugepage size [2M, 1G]
      hugepages_1G: 0             # Number of 1G hugepages to allocate
      hugepages_2M: 10240         # Number of 2M hugepages to allocate
    isolcpus:
      enable: true                # Enable CPU isolation in the host
      autogenerate: true          # Automatically generate list of CPUs to isolate
      cpus: "8-27,36-55"          # List of CPUs (cores/threads) to isolate (not used when autogenerate: true)
    nfd: true                     # Enable Node Feature Discovery
    cmk:
      enable: true                # Enable CPU Manager for Kubernetes
      num_shared_cores: 3         # Number of CPU cores to assign to the "shared pool" on each node 
      num_exclusive_cores: 3      # Number of CPU cores to assign to the "exclusive pool" on each node
    topology_manager:
      enable: true                # Enable Kubernetes built-in Topology Manager
      policy: "best-effort"       # Policy to use with Topology Manager ["none", "best-effort", "restricted", "single-numa-node"]
    tas:
      enable: true                # Enable Telemetry Aware Scheduling
      demo_policy: false          # Enable demo policy for Telemetry Aware Scheduling (default: false)
    bond_cni: true                # Install CNI for network interface bonding
    psp: true                     # Enable Pod Security Policy (admission controller and basic set of rules)
    qat:
      enable: false               # Enable QAT Device Plugin - Configure devices under "device_roles"
      update_drivers: false       # Update drivers for QAT devices
```

References for the above features:
* [CPU Manager for Kubernetes](https://github.com/intel/CPU-Manager-for-Kubernetes)
* [SR-IOV Network device plugin for Kubernetes](https://github.com/intel/sriov-network-device-plugin)
* [Intel Device Plugins for Kubernetes](https://github.com/intel/intel-device-plugins-for-kubernetes)
* [Telemtry Aware Scheduling](https://github.com/intel/telemetry-aware-scheduling)

Additional settings are available in the BMRA templates located in `playbooks/roles/bmra-config/templates`. Changing these might have unexpected results and should generally not be done.

You will also have to modify environmental variables defined in `deploy.env` to match your setup. For deploying Kuberef on pre-provisioned infrastructure, set `deployment_type=k8s`.

Once ready, issue the following command to initiate the deployment

`./deploy.sh`

Once the deployment is successful, you will have a fully functional RI-2 setup!

The cluster is accessible through the `kubectl` CLI from the master nodes. It is possible to interact with the cluster from a jumphost outside of the cluster by using the kubeconfig file found in `$HOME/.kube/config`. The environment path for using the kubeconfig file on the jumphost can be set with `export KUBECONFIG=/path/to/config`. Steps for installing `kubectl` can be found [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

Verify that everything is running using the following commands:
```
$ kubectl get all --all-namespaces
$ kubectl get nodes
$ kubectl get node <node> -o json | jq '.status.allocatable'
  # Install jq if needed: yum install -y jq
```

The list of allocatable resources will vary depending on the configuration, but an example output could look as follows:
```
{
  "cmk.intel.com/exclusive-cores": "3",
  "cpu": "61",
  "ephemeral-storage": "210667024855",
  "hugepages-1Gi": "0",
  "hugepages-2Mi": "20Gi",
  "intel.com/intel_sriov_dpdk_700_series": "4",
  "intel.com/intel_sriov_netdevice": "2",
  "memory": "373489916Ki",
  "pods": "110"
}
```

### 4.3.2 [Placeholder for other Deployment Scenarios]

<a name="4.4"></a>
## 4.4 Validation of the Reference Implementation

In order to ensure that a given RI-2 meets the requirements specified in the RA-2, a set of test cases specified in RC-2 should be executed. A selection of these test cases is documented in [RC-2 Chapter 2](../../../ref_cert/RC2/chapters/chapter02.md).

Currently, Kuberef is validated by running the RC-2 testsuite in GitLab. This RC-2 testsuite version is determined based on the Kuberenetes version deployed by Kuberef. The list of testcases can be found in the Kuberef `.gitlab-ci.yml` file.

For deploying your own RC-2 toolchain, please refer to the steps mentioned in [RC-2 Kubernetes Testing Cookbook](../../../ref_cert/RC2/chapters/chapter03.md).

<a name="4.5"></a>
## 4.5 Automation Tooling

> Describe the automation tooling used and any specific configurations needed.
