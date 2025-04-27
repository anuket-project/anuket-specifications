Glossary
========

Terminology
-----------

To assist the reader, this glossary provides a list of key terms used in this document, together
with their definitions. These definitions are, with a few exceptions, based on the
*ETSI GR NFV 003 V1.5.1 [1]* definitions. In some cases, to avoid confusion, the definitions have
been modified to avoid deployment technology dependencies.

The terms covered in this glossary fall into eight categories:

- Software layer terminology
- Hardware layer terminology
- Operational and administrative terminology
- Container-related terminology
- OpenStack-related terminology
- Cloud platform abstraction-related terminology
- Test-related terminology
- Other referenced terminology

Software layer terminology
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Cloud infrastructure**
   The cloud infrastructure is a generic term that covers the **network function virtualization
   infrastructure** (**NFVI**), Infrastructure-as-a-Service (**IaaS**), and Container-as-a-Service
   (**CaaS**) capabilities. It is the infrastructure on which a **workload** can be executed.
..

   *Note:* The **NFVI**, **IaaS**, and **CaaS** layers can be built on top of each other. In the
   case of **CaaS**, some cloud infrastructure features, such as hardware management and
   multitenancy, are implemented by using an underlying **IaaS** layer.

-  **Cloud infrastructure profile**
   The cloud infrastructure profile is a combination of the cloud infrastructure software profile
   and the cloud infrastructure hardware profile. The cloud infrastructure profile defines the
   capabilities and the configuration of the cloud infrastructure resources that are available for
   the workloads.

-  **Cloud infrastructure software configuration**
   The cloud infrastructure software configuration is a set of settings (Key:Value) that are
   applied or mapped to the cloud infrastructure software deployment.

-  **Cloud Infrastructure Software Profile**
   The cloud infrastructure software profile defines the behaviour, capabilities, and metrics
   provided by a cloud infrastructure software layer on the resources that are available for the
   workloads.

-  **Cloud-native network function (CNF)**
   A cloud-native network function is a cloud-native application that implements the network
   functionality. A CNF consists of one or more microservices. All the layers of a CNF are
   developed using cloud-native principles. These include immutable infrastructure, declarative
   APIs, and a repeatable deployment process.

      *Note:* This definition is derived from the Cloud Native Thinking for Telecommunications
      Whitepaper (`https://github.com/cncf/telecom-user-group/blob/master/whitepaper/cloud_native_thinking_for_telecommunications.md#1.4 <https://github.com/cncf/telecom-user-group/blob/master/whitepaper/cloud_native_thinking_for_telecommunications.md#1.4>`__)
      This publication also includes further details and examples.

-  **Compute flavour**
   The compute flavour defines the sizing of the virtualized resources (namely, compute, memory,
   and storage) that are required to run a workload.

      *Note:* The compute flavour is also used to define the configuration/capacity limit of a
      virtualized container.

-  **Hypervisor**
   A hypervisor is a type of software that abstracts and isolates the workloads with their own
   operating systems from the underlying physical resources. A hypervisor is also known as a virtual
   machine monitor (VMM).

-  **Instance**
   An instance is a virtual compute resource, in a known state, such as running or suspended, that
   can be used in a similar way to a physical server. *Instance* is used interchangeably with
   *Compute node* and *Server*.

      *Note:* The term *instance* can be used to specify a virtual machine (VM) instance or a
      container instance.

-  **Network function (NF)**
   A network function is a functional block or application that has well-defined external interfaces
   and functional behaviour.
   Within the network function virtualization (**NFV**), a **network function** is implemented in
   the form of a **virtualized network function** (VNF) or a **cloud-native network function**
   (CNF).

-  **Network function virtualization (NFV)**
   Network function virtualization is the concept of separating network functions from the hardware
   on which they run by using a virtual hardware abstraction layer.

-  **Network function virtualization infrastructure (NFVI)**
   The network function virtualization infrastructure is the totality of all the hardware and
   software components that are used to build the environment in which a set of virtual applications
   (VAs) is deployed. It is also referred to as the cloud infrastructure.

      *Note:* The NFVI can encompass many locations, such as places where datacentres or edge nodes
      are operated. The network providing connectivity between these locations is considered to be a
      part of the cloud infrastructure. The NFVI and VNF are the top-level conceptual entities in
      the scope of network function virtualization. All other components are subentities of these
      two main entities.

-  **Network service (NS)**
   A network service is a composition of **network functions** or **network services**, or both. It
   is defined by its functional and behavioural specifications, including the service lifecycle.

-  **Software-defined storage (SDS)**
   Software-defined storage is an architecture in which the storage software is independent from the
   underlying storage hardware. The storage access software provides data request interfaces, or
   APIs. The SDS controller software provides storage access services and networking.
   
-  **Virtual application (VA)**
   A virtual application is a general term for software which can be loaded into a virtual machine.

      *Note:* A **VNF** is a type of virtual application.

-  **Virtual central processing unit (vCPU)**
   A virtual CPU represents a portion of the host’s computing resources allocated to a virtualized
   resource, for example, to a virtual machine or a container. One or more vCPUs can be assigned to
   a virtualized resource.

-  **Virtual machine (VM)**
   A virtual machine is a virtualized computation environment that behaves like a physical computer
   or server.

      *Note:* A **VM** consists of all the components (CPU, memory, storage, interfaces/ports, and
      so on) of a physical computer or server. It is created using sizing information or compute
      flavour.

-  **Virtual network function (VNF)**
   A virtual network function is a software implementation of a **network function**, capable of
   running on the **cloud infrastructure**. **VNF**s are built from one or more VNF components
   (**VNFC**s). In most cases, VNFCs are hosted on single VMs or containers.

   -  **Virtual resources**
      The virtual resources consist of the following:

   -  **Virtual compute resource (also known as a virtualization container)**
      A virtual compute resource is a partition of a compute node that provides an isolated
      virtualized computation environment.
   -  **Virtual storage resource**
      A virtual storage resource is a virtualized non-volatile storage allocated to a virtualized
      computation environment hosting a **VNFC**.
   -  **Virtual networking resource**
      A virtual networking resource routes information among the network interfaces of a virtual
      compute resource and the physical network interfaces, providing the necessary connectivity.

-  **Workload**
   A workload is an application, such as a **VNF** or a **CNF**, that performs certain tasks for the
   users. In the cloud infrastructure, these applications run on top of compute resources such as
   **VMs** or **containers**. There are several categories of workload. The most relevant categories
   in the context of the cloud infrastructure are the following:

   -  **Data plane workloads**
      Data plane workloads perform tasks related to packet handling of the end-to-end communication
      between applications. These tasks are expected to be I/O and memory read/write operations
      intensive.
   -  **Control plane workloads**
      Control plane workloads perform tasks related to any other communication between NFs that is
      not directly related to the end-to-end data communication between applications. This category
      includes, for example, session management, routing, and authentication.
   -  **Storage workloads**
      Storage workloads perform tasks related to disk storage (SSD or HDD, or other disk types).
      Examples range from non-intensive router logging to more intensive database read/write
      operations.

Hardware layer terminology
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Cloud infrastructure hardware configuration**
   A cloud infrastructure hardware configuration is a set of settings (Key:Value) that are applied
   or mapped to **cloud infrastructure** hardware deployment.

-  **Cloud infrastructure hardware profile**
   The cloud infrastructure hardware profile defines the behaviour, capabilities, configuration, and
   metrics provided by the cloud infrastructure hardware layer resources available for the
   workloads.

   -  **Host profile**
      The host profile is another term for a **cloud infrastructure hardware profile**.

-  **CPU type**
   A CPU type is a classification of CPUs by features required for the execution of computer
   programs, such as instruction sets, cache size, and the number of cores.

-  **Hardware resources**
   Hardware resources refer to the compute, storage, and network hardware resources on which the
   cloud infrastructure platform software, virtual machines, and containers run.

-  **Physical network function (PNF)**
   The physical network function (PNF) is the implementation of a network function via a tightly
   coupled dedicated hardware and software system.

      *Note:* This is a physical cloud infrastructure resource with the NF software.

-  **Simultaneous multithreading**
   Simultaneous multithreading (SMT) is a technique for improving the overall efficiency of
   superscalar CPUs with hardware multithreading. SMT permits multiple independent threads of
   execution on a single core to make better use of the resources provided by modern processor
   architectures.

Operational and administrative terminology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Cloud service user**
   A cloud service user is a person, or an entity acting on behalf thereof, who is associated with a
   cloud service customer that uses cloud services.

      *Note* Examples of such entities include devices and applications.

-  **Compute node**
   A compute node is an abstract definition of a *server*. This term is used interchangeably with
   *instance* and *server*.

      *Note:* A compute node can refer to hardware and software that support the VMs or containers
      that are running on it.

-  **External network**
   External networks provide network connectivity between the cloud infrastructure tenants and the
   resources outside the tenant space.

-  **Fluentd (**\ `https://www.fluentd.org/ <https://www.fluentd.org/>`__\ **)**
   Fluentd is an open-source data collector for the unified logging layer. It allows data collection
   and consumption for better use and understanding of data. **Fluentd** is a CNCF-graduated
   project.

-  **Kibana**
   Kibana is an open-source data visualization system.

-  **Multitenancy**
   Multitenancy is a feature where physical, virtual, or service resources are allocated in such a
   way that multiple tenants, and their computations and data, are isolated from each other and are
   inaccessible to each other.

-  **Prometheus**
   Prometheus is an open-source monitoring and alerting system.

-  **Quota**
   A quota is an imposed upper limit on specific types of resources. Quotas are usually used to
   prevent excessive resource consumption by a consumer (a tenant, a VM, or a container).

-  **Resource pool**
   A resource pool is a logical grouping of cloud infrastructure hardware and software resources. A
   resource pool can be based on a certain resource type (for example, compute, storage, and
   network) or a combination of resource types. A **cloud infrastructure** resource can be part of
   one or more resource pools, or no resource pools at all.

-  **Service assurance (SA)**
   Service assurance is responsible for collecting alarm and monitoring data. Applications within
   SA or interfacing with SA can then use this data for fault correlation, root cause analysis,
   service impact analysis, SLA management, security, monitoring and analytics, and so on.

-  **Tenant**
   Tenants are cloud service users that share access to a set of physical and virtual resources.
   (For details, see `Y.3500: Information technology - Cloud computing - Overview and
   vocabulary <https://www.itu.int/rec/T-REC-Y.3500-201408-I>`__).

      *Note* Tenants represent an independently manageable logical pool of compute, storage, and
      network resources abstracted from physical hardware.

-  **Tenant instance**
   A tenant instance refers to a single **Tenant**.

-  **Tenant (internal) networks**
   Tenant (internal) networks are virtual networks that are internal to **tenant instances**.

Container-related terminology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   *Note:* Relevant terms have been added here from RA2. Most of these term definitions have been
   taken from the Kubernetes glossary
   (`https://kubernetes.io/docs/reference/glossary <https://kubernetes.io/docs/reference/glossary>`__).
   However, some of the terms are independent from Kubernetes as a specific container orchestration
   engine.

-  **CaaS manager**
   A CaaS manager is a management plane function that manages the lifecycle (namely instantiation,
   scaling, healing, and so on) of one or more CaaS instances. This includes communication with the
   virtualized instruction manager (VIM) for master/node lifecycle management.

-  **Container**
   A container is a lightweight and portable executable image that contains software and all of its
   dependencies.

      *Note:* OCI defines **container** as "An environment for executing processes with configurable
      isolation and resource limitations. For example, namespaces, resource limits, and mounts are
      all part of the container environment."
      A **container** provides operating-system-level virtualization by abstracting the user space.
      One key difference between **containers** and **VMs** is that, unlike VMs, where each **VM**
      is self-contained with all the operating system components within the **VM** package,
      containers share the host system’s kernel with other containers.

-  **Container engine**
   A container engine is a set of software components that are used to create, destroy, and manage
   containers on top of an operating system.

-  **Container image**
   A container image is a stored instance of a container that holds the software that is needed to
   run an application.

-  **Container runtime**
   The container runtime is the software that is responsible for running the containers.

      *Note:* As explained in the OCI Glossary (`https://github.com/opencontainers/runtime-spec/blob/master/glossary.md <https://github.com/opencontainers/runtime-spec/blob/master/glossary.md>`__),
      the container runtime reads the configuration files of a **container** from a directory
      structure, uses that information to create a container, and launches a process inside the
      container, as well as performing other lifecycle actions.
      
-  **Container as a Service (CaaS)**
   Container as a Service is a set of technologies that enable the management of containerized
   software. It includes a Kubernetes cluster, container networking, storage, routing, service mesh,
   and so on.

-  **Kubernetes cluster**
   A Kubernetes cluster is a set of machines called nodes, or worker nodes, and masters, that run
   containerized applications managed by Kubernetes. A cluster has at least one worker node and at
   least one master.

      *Note:* This definition was adapted from the Kubernetes Glossary
      (\ `https://kubernetes.io/docs/reference/glossary/?all=true#term-cluster <https://kubernetes.io/docs/reference/glossary/?all=true#term-cluster>`__).

-  **Kubernetes control plane**
   The Kubernetes control plane is a container orchestration layer that exposes the API and
   interfaces to define, deploy, and manage the lifecycle of the containers.

-  **Kubernetes master**
   The Kubernetes master manages the worker nodes and the Pods in a cluster. The master may run on
   a virtual machine or on a physical machine. Multiple masters can be used to provide a cluster
   with failover and high availability.

-  **Kubernetes node**
   A Kubernetes node is a worker node in Kubernetes that is managed by the master (see **Kubernetes
   master**). A worker node may be a virtual machine or a physical machine, depending on the
   cluster. It has local daemons or services that are necessary to run the Pods and is managed by
   the control plane.

-  **Kubernetes service**
   A Kubernetes service is an abstract way of exposing an application running on a set of Pods as a
   network service.

      *Note:* This definition from the Kubernetes Glossary (\ `https://kubernetes.io/docs/reference/glossary/?all=true#term-service <https://kubernetes.io/docs/reference/glossary/?all=true#term-service>`__)
      uses the term **network service** differently from the way it is used in *ETSI NFV*.

-  **Pod:**
   A Pod is the smallest and simplest Kubernetes object. A Pod represents a set of running
   containers in the cluster. A Pod is typically set up to run a single primary container. It can
   also run optional sidecar containers that add supplementary features, such as logging.

OpenStack-related terminology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   *Note:* The official OpenStack Glossary ( `https://docs.openstack.org/image-guide/common/glossary.html <https://docs.openstack.org/image-guide/common/glossary.html>`__)
   provides an exhaustive list of OpenStack-related concepts. Some additional terms are used in
   Reference Architecture RA-1, or are used to relate RA-1 terms to terms defined elsewhere.

-  **Core (physical)**
   A core is an independent computer processing unit that can independently execute CPU
   instructions. It is integrated with other cores on a multiprocessor (such as the chip and
   integrated circuit die).

      *Note:* The multiprocessor chip is also referred to as a CPU that is placed in the socket of a
      computer motherboard.

-  **Flavour capability**
   Flavour capability refers to the capability of the cloud infrastructure profile, such as CPU
   pinning, NUMA, or **huge pages**.

-  **Flavour geometry**
   Flavour geometry refers to flavour sizing, such as the number of vCPUs and disks, the size of
   the RAM, and so on.

-  **Huge pages**
   Physical memory is partitioned and accessed using basic page units (in Linux, the default size
   is 4 KB). Huge pages, typically 2 MB and 1 GB in size, allow large amounts of memory to be used
   with reduced overheads. In an NFV environment, huge pages are critical for supporting large
   memory pool allocations for data packet buffers. This results in fewer Translation Lookaside
   Buffers (TLB) lookups, which reduces the virtual to physical pages address translations. Without
   huge pages enabled, high TLB miss rates would occur, thereby degrading performance.

-  **Server**
   For the OpenStack compute API, a **server** is a virtual machine (VM), a physical machine
   (bare-metal), or a container.

Cloud platform abstraction-related terminology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Abstraction**
   Abstraction is the process of removing concrete, fine-grained, or lower-level details or
   attributes, or common properties in the study of systems, to focus attention on topics of greater
   importance or general concepts. It can be the result of decoupling. This text was adapted from
   Wikipedia:Abstraction (`https://en.wikipedia.org/wiki/Abstraction_(computer_science) <https://en.wikipedia.org/wiki/Abstraction_(computer_science)>`__),
   Wikipedia:Generalization(`https://en.wikipedia.org/wiki/Generalization <https://en.wikipedia.org/wiki/Generalization>`__).

-  **Appliance deployment model**
   The appliance deployment model is an application that is tightly coupled to the underlying
   platform, even if the application is virtualized or containerized.

-  **Application control**
   Application control refers to any method or system of controlling applications (VNFs). Depending
   on the Reference Architecture and the technologies used, this can be a VNF manager, or an NFV
   orchestrator provided as a VNF or platform capability.

-  **Cloud deployment model**
   With the cloud deployment model, the applications are decoupled from the platform provided by the
   cloud operator.

-  **Decomposition**
   Also known as factoring, decomposition can be defined as the breaking of a complex system into
   parts that are easier to program and maintain. This text was adapted from Wikipedia:Decomposition
   (`https://en.wikipedia.org/wiki/Decomposition_(computer_science) <https://en.wikipedia.org/wiki/Decomposition_(computer_science)>`__).
   
-  **Encapsulation**
   Encapsulation refers to the restricting of direct access to some of an object’s components. This
   text was adapted from Wikipedia:Encapsulation (`https://en.wikipedia.org/wiki/Encapsulation_(computer_programming) <https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)>`__).

-  **Loose coupling** or **decoupling**
   A loosely coupled system is one in which each of its components has, or makes use of, little or
   no knowledge of the implementation details of other separate components. Loose coupling, also
   known as decoupling, is the opposite of tight coupling. This text was adapted from
   Wikipedia:Loose Coupling (`https://en.wikipedia.org/wiki/Loose_coupling <https://en.wikipedia.org/wiki/Loose_coupling>`__).

-  **Observability**
   Observability is a measure of how well the internal states of a system can be inferred from the
   knowledge of its external outputs. This text was adapted from Wikipedia:Observability
   (`https://en.wikipedia.org/wiki/Observability <https://en.wikipedia.org/wiki/Observability>`__).

-  **Resilience**
   Resilience is the ability to provide and maintain an acceptable level of service in the face of
   various faults and challenges to normal operation. This text was adapted from
   Wikipedia:Resilience (`https://en.wikipedia.org/wiki/Resilience_(network) <https://en.wikipedia.org/wiki/Resilience_(network)>`__).

Test-related terminology
~~~~~~~~~~~~~~~~~~~~~~~~

-  **Calibration**
   Calibration is the process of checking and/or adjusting a stimulus generation or measurement
   device with a known reference value, to improve the overall quality of the measured results.
   Calibration may be a simple task, for example, a comparison of the configured traffic generator
   sending rate and the measured rate using a simple System Under Test (SUT), such as a loop-back
   cable between the interfaces, so that the known reference value is the published nominal
   interface rate.

-  **Reference value**
   The reference value is a measured or established outcome for comparison with new measurements.
   For example, the reference value or expected outcome of a functional test is PASS. The reference
   value or expected outcome of a performance measurement or benchmarking test may be the value
   measured for the previous SUT release, or the published value or theoretical limit of a simple
   SUT.

-  **API testing**
   API testing refers to testing against a protocol specification for conformance.

-  **Functional testing**
   The main objective of functional testing is the verification of compliance against specific
   functional requirements using a specific stimulus or response within the SUT. This includes the
   expected behaviour. These tests generally result in a binary outcome, that is, *pass* or *fail*.
   Examples include the verification of an API call and its associated response, such as the
   instantiation of a VM or container, and the verification of the existence of the VM or container
   (expected behaviour), or the ability to activate a specific feature of the SUT, such as SR-IOV.

-  **Performance measurement**
   Performance measurement can be defined as the procedure or set of operations having the objective
   of determining a measured value or measurement result of an infrastructure in operation,
   according to a defined metric. In the context of telemetry, performance measurements reflect data
   generated and collected within the cloud infrastructure that reflects a performance aspect of the
   cloud infrastructure. Examples include a count of frames or packets traversing an interface per
   unit of time, memory usage information, and other types of resource usage and availability. This
   data may be instantaneous or accumulated, and made available (that is, exposed) based on
   permissions and contexts, such as workload versus infra. Other performance measurements are
   designed to assess the efficiency of SUT functions, such as the time to successfully instantiate
   one or more virtual machines (VMs) or containers, or the percentage of failures in a set of many
   instantiation attempts. Other performance measurements are conducted under controlled conditions
   using calibrated test systems in such a way that the measured results are more likely to be
   comparable to other such measurements.

-  **Performance testing**
   The main objective of performance testing is to understand if the system under test (SUT) can
   achieve the expected performance, by conducting a series of performance measurements and
   comparing the results against a reference value. Performance testing is needed to help dimension
   a solution or to assess that a platform (particular hardware and software combination) is
   configured correctly and performing as expected, that is, as compared with the capacity or
   performance claims made by the infrastructure and VNF/CNF vendors. Performance testing may be
   useful for comparing infrastructure capabilities between a particular SUT and a reference
   implementation with well-understood and sound configurations, and previously established
   performance ranges. Performance testing for the purpose of comparing different commercial
   implementations is not a goal here and is therefore out of scope for the purposes of this
   definition. Performance testing relies on well-established benchmark specifications to help
   establish appropriate methodologies and accuracy tolerances.

-  **Benchmarking**
   Benchmarking is a type of performance test that assesses a key aspect of the computing
   environment in its role as the infrastructure for network functions, using calibrated test
   systems and controlled conditions. In general, the benchmark testing attempts to isolate the
   feature or parameter under test, to reduce the impact of other system components or operations on
   the test result. The benchmark, and related metrics, have been agreed by the industry and
   documented in publications of an accredited standards body. As a result, benchmarks are a subset
   of all possible performance tests and metrics, that is, they are selected measurements which are
   more important than others. Example benchmarks include zero-loss throughput, latency, and loss
   ratio (see *ETSI NFV TST009, RFC 2544*) of various components of the environment, expressed in
   quantitative units to allow direct comparison between different systems treated as a black box
   (vendor-independence). Because the demands on a particular system may vary from deployment to
   deployment, benchmarking assessments do not define acceptance criteria or numerical performance
   requirements. Benchmark testing and conformance testing intersect when a specific requirement in
   the reference architecture specification is crucial to the performance of the system. Correct
   execution of the performance test with the valid result constitutes conformance. The completion
   time for a single conforming execution, or the number of conforming executions per second, are
   potential benchmark metrics, and sources of known reference values.

Other referenced terminology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Anuket Assured Program (AAP)**
   The Anuket Assured Program is an open-source, community-led program whose task is to verify
   compliance of the telecom applications and the cloud infrastructures to the Anuket
   specifications.

-  **Carrier grade**
   Carrier grade refers to network functions and infrastructure that are characterised by all or some of the following attributes: High reliability allowing near 100% uptime, typically measured as better than “five nines”; Quality of Service (QoS) allowing prioritization of traffic; High Performance optimized for low latency/packet loss, and high bandwidth; Scalability to handle demand growth by adding virtual and/or physical resources; Security to be able to withstand natural and man-made attacks.
   Carrier grade refers to network functions and infrastructure that are characterized by some or
   all of the following attributes:

   - High reliability, allowing nearly 100% uptime, typically measured as better than “five nines”.
   - Quality of service (QoS), allowing prioritization of traffic.
   - High performance optimized for low latency/packet loss, and high bandwidth.
   - Scalability to handle demand growth by adding virtual and/or physical resources.
   - Security to be able to withstand natural and man-made attacks.

-  **Monitoring (capability)**
   Monitoring capabilities are used for the passive observation of workload-specific traffic
   traversing the cloud infrastructure.

      *Note:* As with all capabilities, monitoring may be unavailable or intentionally disabled for
      security reasons in a given cloud infrastructure instance.   

-  **NFV orchestrator (NFVO)**
   The NFV orchestrator manages the VNF lifecycle and **cloud infrastructure** resources, supported
   by the **virtualized infrastructure manager** (**VIM**), to ensure an optimized allocation of the
   necessary resources and connectivity.

-  **Platform:**
   A platform is a cloud capabilities type in which the cloud service user can deploy, manage, and
   run customer-created or customer-acquired applications using one or more programming languages,
   and one or more execution environments supported by the cloud service provider. This text was
   adapted from ITU (`Y.3500: Information technology - Cloud computing - Overview and vocabulary <https://www.itu.int/rec/T-REC-Y.3500-201408-I>`__).
   
      *Note:* This includes the physical infrastructure, operating systems, virtualization or
      containerization software, and other orchestration, security, monitoring and logging, and
      lifecycle management software.

-  **Vendor implementation:**
   Vendor implementation is a commercial implementation of a cloud platform.

-  **Virtualized infrastructure manager (VIM)**
   The virtualized infrastructure manager is responsible for controlling and managing the **network
   function virtualization infrastructure** compute, storage, and network resources.
