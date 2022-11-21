CNF Test Cases and Requirements Traceability
============================================

Introduction
------------

The scope of this chapter is to identify and list test cases based on
requirements defined in :doc:`ref_arch_kubernetes:index`.
This will serve as traceability between test cases and requirements for
Kubernetes platform interoperability.

Note that each requirement may have one or more test cases associated
with it.

Selection Criteria
------------------

Test cases, tools and their dependencies must be open source. The test
cases (or test suite with the test case) as well as the environment
needed to run the test should be reproducible by any party following
publicly available documentation.

Examples of initiatives (having testing tools, test suites, etc) with
test cases which could be used include K8s Conformance, K8s e2e,
Sonobuoy, Anuket Functest, CNF Conformance.

Traceability Matrix
-------------------

The following is a Requirements Traceability Matrix (RTM) mapping Test
Case, and/or Test Case Coverage, to RM and RA requirements –
configuration, deployment, runtime.

Test Case Traceability to RA2 Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section focuses on the test cases covering the requirements in
:ref:`ref_arch_kubernetes:chapters/chapter04:kubernetes workloads`
for Kubernetes workloads.

.. list-table:: Traceability to RA2 Requirements
   :widths: 35 35 30 30
   :header-rows: 1

   * - RM/RA Ref
     - High-level test definition
     - Test name and project
     - Priority
   * - ra2.app.001
     - Specifies the container's root filesystem.
     - `Root <https://github.com/opencontainers/runtime-spec/blob/master/config.md>`__ Parameter Group (OCI Spec)
     - Must
   * - ra2.app.002
     - Specifies additional mounts beyond root.
     - `Mounts <https://github.com/opencontainers/runtime-spec/blob/master/config.md#mounts>`__ Parameter Group
       (OCI Spec)
     - Must
   * - ra2.app.003
     - Specifies the container process.
     - `Process <https://github.com/opencontainers/runtime-spec/blob/master/config.md#process>`__ Parameter Group
       (OCI Spec)
     - Must
   * - ra2.app.004
     - Specifies the container's hostname as seen by processes running inside the container.
     - `Hostname <https://github.com/opencontainers/runtime-spec/blob/master/config.md#hostname>`__ Parameter Group
       (OCI Spec)
     - Must
   * - ra2.app.005
     - User for the process is a platform-specific structure that allows specific control over which user the process
       runs as.
     - `User <https://github.com/opencontainers/runtime-spec/blob/master/config.md#user>`__ Parameter Group (OCI Spec)
     - Must
   * - ra2.app.006
     - Consumption of additional, non-default connection points. Any additional non-default connection points must be requested through the use of workload annotations
       or resource requests and limits within the container spec passed to the Kubernetes API Server.
     - :ref:`int.api.01 <chapters/chapter02:Kubernetes Architecture Requirements>`
     - Must
   * - ra2.app.007
     - Host Volumes:  Workloads should not use hostPath volumes, as `Pods with identical configuration
       <https://kubernetes.io/docs/concepts/storage/volumes/#hostpath>`__ (such as those created from a PodTemplate)
       may behave differently on different nodes due to different files on the nodes.
     - :ref:`kcm.gen.02 <chapters/chapter02:Kubernetes Architecture Requirements>`
     - Must
   * - ra2.app.008
     - Infrastructure dependency
     - Workloads must not rely on the availability of the master nodes for the successful execution of their
       functionality (i.e. loss of the master nodes may affect non-functional behaviours such as healing and scaling,
       but components that are already running will continue to do so without issue).     
     - Must
   * - ra2.app.009
     - Device plugins
     - Workload descriptors must use the resources advertised by the device plugins to indicate their need for an FPGA,
       SR-IOV or other acceleration device.
     - Must   
   * - ra2.app.010
     - Node Feature Discovery (NFD)
     - Workload descriptors must use the labels advertised by `Node Feature Discovery
       <https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html>`__ to indicate which
       node software of hardware features they need.
     - Must
   * - ra2.app.011
     - Published helm chart:  Helm charts of the CNF must be published into a helm registry and must not be used from local copies.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-helm-chart-is-publi
       shed-helm_chart_published>`__
     - Must      
