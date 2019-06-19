[<< Back](../../ref_model)
# 3	Infrastructure Abstraction
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Model.](#model)
* [3.2 Exposed vs Internal.](#expint)
* [3.3 Exposed NFVI capabilities, metrics, and constraints.](#expcap)

There is the necessity to clearly define which kind of infrastructure resources a shared network function virtualisation infrastructure (NFVI) will provide for hosting virtual network functions (VNFs) and/or cloud-native network functions (CNF), so that the requirements of each of the VNFs and CNFs match the capabilities of the NFVI.

<< Figure 3 >>

The lack of a common understanding of which resources and corresponding capabilities a suitable NFVI should provide may lead to several issues which could negatively impact the time and cost for onboarding and maintaining these solutions on top of a virtualised infrastructure e.g.:
- supporting any kind of VNF specific requirements (e.g. regarding network acceleration or API access) might result in having to establish different silo NFVIs for each VNF
- synchronising the release cycles of a large set of different technologies will sooner or later lead to situations in which required upgrades cannot be applied easily due to incompatibilities.

The abstraction model presented in this chapter specifies a common set of virtual infrastructure resources which a NFVI will need to provide to be able to host most of the typical VNF workloads required by the operator community.
Although a couple of explicit and implicit abstraction models (e.g. in the context of ETSI/NFV) are already available they fall short when address following design principles:
-	**Scope**: the model should describe the most relevant virtualised infrastructure resources (incl. acceleration technologies) an NFVI needs to provide for hosting Telco VNF workloads
-	**Separation of Concern**: the model should support a clear distinction between the responsibilities related to maintaining the network function virtualisation infrastructure and the responsibilities related to managing the various VNF workloads
-	**Simplicity**: the amount of different types of resources (including their attributes and relationships amongst one another) should be kept to a minimum to reduce the configuration spectrum which needs to be considered
-	**Declarative**: the model should allow for a declarative description of the required NFVI capabilities for onboarding and maintaining VNFs
-	**Explicit**: the model needs to be rich enough to allow for a direct mapping towards the APIs of NFVIs for the instantiation of virtual infrastructure elements without requiring any additional parameters
-	**Lifecycle**: the model must distinguish between resources which have independent lifecycles but should group together those resources which share a common lifecycle
-	**Aligned**: the model should clearly highlight the dependencies between the elements to allow for a well-defined and simplified synchronisation of independent automation tasks.

To summarise: the abstraction model presented in this paper will build upon existing modelling concepts and simplify and streamline them to the needs of telco operators who intend to distinguish between infrastructure related and VNF related responsibilities.

<a name="model"></a>
## 3.1	Model
The abstraction model for the NFVI makes use of following layers (only the virtual infrastructure layer will be directly exposed to the VNFs/CNFs):

<<Figure 4 >>
  
The functionalities of each layer are as follows:
- NFVI hardware profile: This layer consists of physical hardware components such as servers, random access memory, storage devices, network ports, hardware acceleration devices, etc. and their corresponding basic operating systems (BIOS).
- NFVI software profile: This layer consists of both the host Operating System (OS) responsible for managing the hardware resources of the layer below as well as the virtualization/containerization technology which turns hardware components into a pool of logical resources and dynamically allocates them to the layer above.
- Virtual infrastructure resources: This layer represents all the infrastructure resources which the NFVI provides to the VNFs/CNFs such as tenants, compute hosts, storage and networks These resources can be managed by the layer above directly or indirectly via an application programming interface or graphical user interface.
- VNFs/CNFs: This layer consists of virtualized and/or containerized network functions that run on top of a VM or as a Container.
The virtual infrastructure resources provided by the NFVI can be grouped into four categories as shown in the diagram below:

<<Figure 5>>

- tenant: tenants represent an independently manageable logical pool of compute, storage and network resources
- compute resources: represent virtualised hosts for operating systems and applications
- storage resources: represent virtualised resources for persisting data
- network resources: represent virtual resources providing layer 2 and layer 3 connectivity

The virtualised infrastructure resources related to these categories are listed below:

### Tenant

A network function virtualisation infrastructure needs to be capable of supporting multiple tenants and has to isolate sets of infrastructure resources dedicated to specific VNF/CNF workloads from one another. Tenants represent an independently manageable logical pool of compute, storage and network resources abstracted from physical hardware. **Example**: a tenant within an OpenStack environment or a Kubernetes cluster.

| Attribute                     | Description                              |
|-------------------------------|------------------------------------------|
| `name` | name of the logical resource pool |
| `type` | type of tenant (e.g. OpenStack tenant, Kubernetes cluster, …) |
| `vcpus` | max. number of virtual CPUs |
| `ram` | max. size of random access memory in GB |
| `disc` | max. size of ephemeral disc in GB |
| `networks` | description of external networks required for inter-domain connectivity |
| `metadata` | key/value pairs for selection of the appropriate physical context (e.g. location, availability zone, …) |
<p align="center"><b>Table 3-1:</b> Attributes of a tenant.</p>

### Compute Host
A virtual machine or a container/pod belonging to a tenant capable of hosting the application components of VNFs. A compute host therefore requires a tenant context and since it will need to communicate with other communication partners it is assumed that the networks have been provisioned in advance. **Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV.

| Attribute | Description |
| --- | --- |
| `name` | name of the virtual host |
| `vcpus` | number of virtual cpus |
| `ram` | size of random access memory in GB |
| `disc` | size of root disc in GB |
| `nics` | sorted list of network interfaces connecting the host to the virtual networks |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |
| `metadata` | key/value pairs for selection of the appropriate redundancy domain |
<p align="center"><b>Table 3-2:</b> Attributes of compute resources.</p>

### Storage
A block device of a certain size for persisting information which can be created and dynamically attached to/detached from a compute host. A storage device resides in a tenant context and exists independently from any compute host. **Example**: an OpenStack cinder volume.

| Attribute | Description |
| --- | --- |
| `name` | name of storage resources |
| `size` | size of disc in GB |
| `attachments` | list of compute hosts to which the device is currently attached |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |
| `metadata` | key/value pairs for selection of the appropriate redundancy domain |
<p align="center"><b>Table 3-3:</b> Attributes of storage resources.</p>

_**Comments**: we need to be more specific regarding acceleration and metadata._

### Network
A layer 2 / layer 3 communication domain within a tenant. A network requires a tenant context. **Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV.

| Attribute | Description |
| --- | --- |
| `name` | name of the network resource |
| `subnet` | classless inter-domain routing of the subnet |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |
<p align="center"><b>Table 3-4:</b> Attributes of network resources.</p>

<a name="expint"></a>
## 3.2	Exposed vs Internal
Mark S./Tom investigating.
1.	(Explanation)
2.	E.g. this is how I expose my NFVi storage to the VNF = External

<a name="expcap"></a>
## 3.3	Exposed NFVI capabilities, metrics, and constraints

### 3.3.1	Exposed NFVI capabilities
This section covers a list of explicit NFVI capabilities and metrics that defines an NFVI. These capabilities and metrics are well known to VNFs as they provide capabilities which VNFs rely on.

> _**Note**: 	It is expected that NFVI capabilities and metrics will evolve with time as more capabilities are added as technology enhances and matures._

#### 3.3.1.1	Exposed resource capabilities
Table xx below shows resource capabilities of NFVI. Those indicate resources offered to VNFs by NFVI.


