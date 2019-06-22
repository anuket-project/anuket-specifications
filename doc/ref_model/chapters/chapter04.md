[<< Back](../../ref_model)
# 4	Catalogue
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

Infrastructure profiles are collection of capabilities, metrics, compute flavours, interface options, storage extensions, and acceleration capabilities that are offered by the infrastructure to VNFs. Infrastructure profiles are offered to VNFs in form of instance types with their corresponding options and extensions.

The idea of the infrastructure profiles catalogue is to have a predefined set of instance types with a predefined set of compute flavours (sometimes referred to as T-shirt sizes) which VNF vendors use to build their VNFs. Each VNF uses one or more of those compute flavours (with one or more of offered instance types) to build its overall functionality as illustrated in **Figure 4-1**.

##  4.1	Compute flavours
Flavours represent the compute, memory, storage capacity, and management network resource templates that are used to create the VMs on the compute hosts. Each VM instance is given a flavour (resource template), which determines the instance’s core, memory and storage characteristics. Flavours can also specify secondary ephemeral storage, swap disk, metadata to restrict usage, or special project access. In other terms, Flavours are grouping of hosts typically sharing same characteristics or metadata. 
A compute flavour geometry consists of the following elements:

Element |Description 
--------|----------
Name	|A descriptive name
Virtual compute resources (aka vCPUs) |Number of virtual compute resources (vCPUs) presented to the instance.
Memory MB	|Instance memory in megabytes. 
Ephemeral/Local Disk |Specifies the size of an ephemeral data disk that exists only for the life of the instance. Default value is 0.<br />The ephemeral disk may be partitioned into boot (base image) and swap space disks. 
Is Public	|Boolean value, whether flavor is available to all users or private to the project it was created in. Defaults to True.
Extra Specs	|Key and value pairs that define on which compute nodes a flavor can run. These pairs must match corresponding pairs on the compute nodes. Use to implement special resources, such as flavors that run on only compute nodes with GPU hardware.

**Table 14: Flavour Geometry Specification**
<br />
Flavour Capabilities
1.	**CPU Oversubscription Ratio**: is based on the number of threads available.   For example, on a 24-core host with HT, there are 48 vCPUs with 1:1 CPU Ratio and 96 vCPUs with 2:1 CPU Ratio.
2. **HT (Hyper Threading support)**: Enabled on all servers. Gets 2 hyper threads per physical CPU.  Always ON. 
3. **CPU Pinning**: vCPU is pinned to a physical core and dedicated to the requesting VM. 
4. **NUMA (Non-Uniform Memory Access) Alignment**: Indicates that vCPU will be on a Socket that is aligned with the associated NIC card and memory.  Important for performance optimized VNFs. 
5. **Huge Pages**: By default, CPU allocate RAM in 4K chunks. Huge Pages enable to allocate in larger Chunks (such as 2MB, 1GB).  This helps improve performance in some cases. 
6. **SR-IOV (Single-Root Input/Output Virtualization)**: Allows SR-IOV ports to be used in VM. 
7. **DPDK vRouter**: Virtual Router integrated with the Intel DPDK (Data Plane Development Kit) libraries. 
8. **Kernel vRouter**: Virtual Router that runs in the Kernel space

##  4.2 4.2	Predefined Compute flavours
The intent of the following flavours list is to be comprehensive and yet effective to cover both IT and NFV workloads. The compute flavours are specified relative to the standardised “large” flavour. The standard “large” flavour configuration consists of 4 vCPUs, 8 GB of RAM and 80 GB of local disk, and the resulting instance will have a management interface of 1 Gbps. The “medium” flavour is half the size of a large and small is half the size of medium. The tiny flavour is a special sized flavour.

.conf |vCPU ("c") |RAM ("r") |Local Disk ("d") | Managmenet Interface
-----|------------|----------|-----|-----
.tiny	|1	|512 MB	|1 GB	|1 Gbps
.small	|1	|2 GB	|20 GB 	|1 Gbps
.medium	|2	|4 GB	|40 GB	|1 Gbps
.large	|4	|8 GB	|80 GB	|1 Gbps
.2xlarge*	|8	|16 GB	|160 GB	|1 Gbps
.4xlarge*	|16	|32 GB	|320 GB	|1 Gbps

**Table 15: Compute flavours**
>\* These compute flavours are intended to be used for transitional purposes and VNF vendors are expected to consume smaller flavours and adopt micro server’s designs for their VNFs.

###  4.2.1 Flavour Customization
The predefined flavours can be customized by specifying key-value pairs for the “r” (RAM in GB) and “d” (local disk in GB) parameters as customization options to the predefined flavours:
```
<predefined flavour name> [<customization options>]'
<customization options> :: <”.”> < [<”r”><number>] [<”d”><number>] >]
```
In the above, it is optional to specify the customization options (are enclosed within “[“ and “]” parentheses. The customization options may specify one or more key-value pair of options. The Table shows examples of some customizations.
Customization	|vCPU	|RAM	|Local Disk	|Management Interface
----|---|---|---|----
.medium.r12d80	|2	|12 GB	|80 GB	|1 Gbps
.large.r16	|4	|14 GB	|80 GB	|1 Gbps
.2xlarge.r32d80	|8	|32 GB	|80 GB	|1 Gbps
.2xlarge.464	|8	|64 GB	|160 GB	|1 Gbps

**Table 16: Flavour Customization Examples**

##  4.3 Parametized Flavours
The pre-define flavours are associated with specific fixed vCPU and RAM (GB) configurations. For example, vCPU:RAM (GB) combinations of 1:2, 2:4, 4:8 etc. which specify flavours with 1 vCPU and 2 GB of RAM, 1 vCPU and 2 GB of RAM, and 4 vCPU and 8 GB of RAM. These pre-defined vCPU and RAM configurations do not allow the flexibility to deploy VMs with, say, 6 vCPU and 10 GB of RAM. Parametrized flavour requests allow great flexibility on specifying the various parameters for creation of nodes.

**Flavour Naming**: Flavours are named with the first letter representing the Instance Type – either “b”, ”n”, “c” or “s”, with the second letter representing the networking technology used “d” for DPDK, “s” for SR-IOV or “v” for kernel vRouter.
**Flavor Names**
  Flavor Names are composed:<br />
    `<Flavor Series><.><c><vCPU><r><RAM><d><disk><s><swap><e><ephemeral><.><options>`

**Flavor Options**

**NUMA Options (“nx”)**
NUMA alignment is enabled by default and hence the option nE doesn’t need to be explicitly specified.  VMs that need to cross NUMA boundaries need to specify the option nX and nD to disable NUMA alignment.

**CPU Pinning Override (“cx”)**
This option can be used to change the default CPU Oversubscription Ratio of a VM Flavor Series.  When the c2 or c4 options are used, the VM will land on a host configured with the desired CPU Oversubscription Ratio and with CPU-Pinning; c2 specifies an over-subscription ratio of 2:1 while c4 specifies an over-subscription ratio of 4:1.

**PCI cross NUMA affinity (“ix”)**
I2 allows PCI resources from cross NUMA and should be used with cross NUMA alignment option “nX”

**Thread Policy (“tx”)**
t0 specifies that only a single thread from each physical core be used for VM. Each allocated vCPU shall get mapped to a different physical core and no vCPUs from other guests will be placed on the same physical core. Only permitted in private flavors.

**Flavour Series**

Flavor Series	|Description	|CPU  sub ratio	|HT	|CPU Pinning	|NUMA	|Huge Pages (1GB) |SR-IOV	|DPDK| vRouter	|Kernel vRouter	|Tenant Data Traffic	|Tenant OAM Traffic 
--|---|---|---|---|---|---|---|---|---|---|---|---
bv	|General Purpose 	|2:1	|Y	|N	|N	|N	|N	|N	|Y	|Kernel-VR	|Kernel-VR
nd	|Network Optimized with DPDK vRouter	|1:1	|Y	|Y	|Y	|Y	|N	|Y	|N	|DPDK-VR	|DPDK-VR
ns	|Network Optimized with SR-IOV	|1:1	|Y	|Y	|Y	|Y	|Y	|N	|Y	|SR-IOV, Kernel-VR	|Kernel-VR
ss	|Storage Optimized with SRIOV 	|1:1	|Y	|Y	|Y	|Y	|Y	|N	|Y	|SR-IOV, Kernel-VR	|Kernel-VR
sd	|Storage Optimized with DPDK vRouter 	|1:1	|Y	|Y	|Y	|Y	|N	|Y	|N |DPDK-VR	|DPDK-VR

**Tabale 17: Parameterized Flavour Examples**

##  4.4 Network Interface SPecifications

The network interface specifications extend the flavour customization to specify the network interface “n” followed by the interface bandwidth (in Gbps) and an alphabetic character defining the number of interfaces with that bandwidth; multiple network interface bandwidths, where network interfaces of different bandwidths exist, can be specified by repeating the “n” option.
```
<network interface bandwidth option> :: <”n”><number (bandwidth in Gbps)>< # of interfaces of that bandwidth>
<number of interfaces> :: <”” | “D” | “T” | “Q” | “P” | “H”> 
where “” represents 1x, “D” 2x, “T” 3x, “Q” 4x, “p” 5x and “H” 6x interfaces of the given bandwidth.
```

Virtual interface option	|Description (Bandwidth in Gbps)
---|---
n10, n10D, n10T, n10Q, n10P, n10H	|1x 10, 2x 10, 3x 10, 4x 10, 5x 10, 6x 10 Gbps
n25, n25D, n25T, n25Q, n25P, n25H	|1x 25, 2x 25, 3x 25, 4x 25, 5x 25, 6x 25 Gbps
n50, n50D, n50T, n50Q, n50P, n50H	|1x 50, 2x 50, 36x 50, 4x 50, 5x 50, 6x 50 Gbps

**Table 19: Virtual Interface Specification Examples

##  4.5 Storage Extensions

Multiplee non-ephemeral storage volumes can be attached to virtual computes (*replace with decided term*) for persistent data storage. Each of those volumes can be configured with the required performance catagories (*storage performance prfiles*).
***Add comment about CEPH distributed storage. (Potentially create new profile for it).***

.conf	|Read IO/s	|Write IO/s	Read |Throughput (MB/s)	|Write Throughput (MB/s)
---|---|---|---|---
.bronze	|Up to 3K	|Up to 15K	|Up to 180	|Up to 120
.silver	|Up to 60K	|Up to 30K	|Up to 1200	|Up to 400
.gold	|Up to 680K	|Up to 360K	|Up to 2650	|Up to 1400

**Table 20: Storage Performance Profiles**

