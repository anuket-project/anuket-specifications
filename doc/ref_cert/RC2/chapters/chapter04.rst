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

The Anuket Assured Workload badge requires that workloads are expected
to return **Must/Must Not** results all of the tests/suites identified
as priority (see table).

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
   * - ra2.app.006
     - Consumption of additional, non-default connection points.
       Any additional non-default connection points must be requested
       through the use of workload annotations
       or resource requests and limits within the container spec passed to the
       Kubernetes API Server.
     - :ref:`int.api.01 <chapters/chapter02:Kubernetes Architecture Requirements>`
     - Must
   * - ra2.app.007
     - Workloads must not use `hostPath volumes <https://kubernetes.io/docs/concepts/storage/volumes/#hostpath>`__, as
       Pods with identical configuration (such as those created from a PodTemplate) may behave differently on different
       nodes due to different files on the nodes.
     - :ref:`kcm.gen.02 <chapters/chapter02:Kubernetes Architecture Requirements>`
     - Must
   * - ra2.app.008
     - Infrastructure dependency
     - Workloads **must not** rely on the availability of the master nodes for
       the successful execution of their functionality (i.e. loss of the
       master nodes may affect non-functional behaviours such as healing and
       scaling, but components that are already running will continue to do so
       without issue).
     - Must (Not)
   * - ra2.app.009
     - Device plugins
     - Workload descriptors must use the resources advertised by the device
       plugins to indicate their need for an FPGA, SR-IOV or other
       acceleration device.
     - Must
   * - ra2.app.010
     - Node Feature Discovery (NFD)
     - Workload descriptors must use the labels advertised by
       `Node Feature Discovery
       <https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html>`__
       to indicate which node software of hardware features they need.
     - Must
   * - ra2.app.011
     - Published helm chart:  Helm charts of the CNF must be published into a
       helm registry and must not be used from local copies.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-helm-chart-is-published-helm_chart_published>`__
     - Should
   * - ra2.app.012
     - Valid Helm chart:  Helm charts of the CNF must be valid and should pass
       the helm lint validation.
     - `CNCF CNF Testsuite
       <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-helm-chart-is-valid-helm_chart_valid>`__
     - Should
   * - ra2.app.013
     - Rolling update: Rolling update of the CNF must be possible using
       Kubernetes deployments.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-the-cnf-can-perform-a-rolling-update-rolling_update>`__
     - Must
   * - ra2.app.014
     - Rolling downgrade: Rolling downgrade of the CNF must be possible using
       Kubernetes deployments.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-a-cnf-version-can-be-downgraded-through-a-rolling_downgrade-rolling_downgrade>`__
     - Must
   * - ra2.app.015
     - CNI compatibility: The CNF must use CNI compatible networking plugins.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-the-cnf-is-compatible-with-different-cnis-cni_compatibility>`__
     - Must
   * - ra2.app.016
     - Kubernetes API stability: The CNF must not use any Kubernetes alpha
       API-s.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#poc-to-check-if-a-cnf-uses-kubernetes-alpha-apis-alpha_k8s_apis-alpha_k8s_apis>`__
     - Must (Not)
   * - ra2.app.017
     - CNF resiliency (node drain): CNF must not loose data, must continue to
       run and its readiness probe outcome must be Success even in case of a
       node drain and rescheduling occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-no
       de-drain-occurs-node_drain>`__
     - Must (Not)
   * - ra2.app.018
     - CNF resiliency (network latency): CNF must not loose data, must
       continue to run and its readiness probe outcome must be Success even
       in case of network latency up to 2000 ms occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-network-latency-occurs-pod_network_latency>`__
     - Must (Not)
   * - ra2.app.019
     - CNF resiliency (pod delete) CNF must not loose data, must continue to
       run and its readiness probe outcome must be Success even in case of pod
       delete occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-disk-fill-occurs-disk_fill>`__
     - Must (not)
   * - ra2.app.020
     - CNF resiliency (pod memory hog): CNF must not loose data, must continue
       to run and its readiness probe outcome must be Success even in case of
       pod memory hog occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-pod-memory-hog-occurs-pod_memory_hog>`__
     - Must (Not)
   * - ra2.app.021
     - CNF resiliency (pod I/O stress): CNF must not loose data, must continue
       to run and its readiness probe outcome must be Success even in case of
       pod I/O stress occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-pod-io-stress-occurs-pod_io_stress>`__
     - Must (Not)
   * - ra2.app.022
     - CNF resiliency (pod network corruption): CNF must not loose data, must
       continue to run and its readiness probe outcome must be Success even in
       case of pod network corruption occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-po
       d-network-corruption-occurs-pod_network_corruptio  n>`__
     - Must (Not)
   * - ra2.app.023
     - CNF resiliency (pod network duplication):  CNF must not loose data,
       must continue to run and its readiness probe outcome must be Success
       even in case of pod network duplication occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-pod-network-duplication-occurs-pod_network_duplication>`__
     - Must (Not)
   * - ra2.app.024
     - CNF resiliency (pod DNS error): CNF must not lose data, must continue
       to run and its readiness probe outcome must be Success even in case of
       pod DNS error occurs.
     - N/A
     - Must (Not)
   * - ra2.app.025
     - CNF local storage: CNF must not use local storage.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-the-cnf-uses-local-s
       torage-no_local_volume_configuration>`__
     - Must (Not)
   * - ra2.app.026
     - Liveness probe: All Pods of the CNF must have livenessProbe defined.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-there-is-a-liveness-entry-in-the-helm-chart-liveness>`__
     - Must
   * - ra2.app.027
     - Readiness probe: All Pods of the CNF must have readinessProbe defined.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-there-is-a-readiness-entry-in-the-helm-chart-readiness>`__
     - Must
   * - ra2.app.028
     - No access to container daemon sockets: The CNF must not have any of the
       container daemon sockets (e.g.: /var/run/docker.sock,
       /var/run/containerd.sock or /var/run/crio.sock) mounted.
     - N/A
     - Must (Not)
   * - ra2.app.029
     - No automatic service account mapping: Non specified service accounts
       must not be automatically mapped. To prevent this the
       automountServiceAccountToken: false flag must be set in all Pods of the
       CNF.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-there-are-service-accounts-that-are-automatically-mapped-application_credentials>`__
     - Must (Not)
   * - ra2.app.030
     - No host network access: Host network must not be attached to any of the
       Pods of the CNF. hostNetwork attribute of the Pod specifications
       must be False or should not be specified.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-there-is-a-host-network-attached-to-a-pod-host_network>`__
     - Must (Not)
   * - ra2.app.031
     - Host process namespace separation: Pods of the CNF must not share the
       host process ID namespace or the host IPC namespace. Pod manifests must
       not have the hostPID or the hostIPC attribute set to true.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-containers-are-running-with-hostpid-or-hostipc-privileges-host_pid_ipc_privileges>`__
     - Must (Not)
   * - ra2.app.032
     - Resource limits: All containers and namespaces of the CNF must have
       defined resource limits for at least CPU and memory resources.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-containers-have-resource-limits-defined-resource_policies>`__
     - Must
   * - ra2.app.033
     - Read only filesystem: All containers of the CNF must have a read only
       filesystem. The readOnlyRootFilesystem attribute of the Pods in
       the their securityContext should be set to true.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-containers-have-immutable-file-systems-immutable_file_systems>`__
     - Must
   * - ra2.app.034
     - Container image tags: All referred container images in the Pod
       manifests must be referred by a version tag pointing to a concrete
       version of the image. latest tag must not be used
     - N/A
     - Must
   * - ra2.app.035
     - No hardcoded IP addresses: The CNF must not have any hardcoded IP
       addresses in its Pod specifications.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-there-are-any-non-declarative-hardcoded-ip-addresses-or-subnet-masks-in-the-k8s-runtime-configuration>`__
     - Must (Not)
   * - ra2.app.036
     - No node ports: Service declarations of the CNF must not contain
       nodePort definition.
     - `Kubernetes documentation <https://kubernetes.io/docs/concepts/services-networking/service/>`__
     - Must (Not)
   * - ra2.app.037
     - Immutable config maps: ConfigMaps used by the CNF must be immutable.
     - `Kubernetes documentation <https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-immutable>`__
     - Must
   * - ra2.app.038
     - If the CNF supports scaling, increasing and decreasing its capacity must be implemented using horizontal scaling.
       If horizontal scaling is supported, automatic scaling must be possible using Kubernetes Horizontal Pod Autoscale
       `Horizontal Pod Autoscale (HPA) <https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/>`__
       feature.
     - TBD
     - Must
   * - ra2.app.039
     - CNF image size: The different container images of the CNF should not be
       bigger than 5GB.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-the-cnf-has-a-reasonable-image-size-reasonable_image_size>`__
     - Should (Not)
   * - ra2.app.040
     - CNF startup time: Startup time of the Pods of a CNF should not be more
       than 60s where startup time is the time between starting the
       Pod until the readiness probe outcome is Success.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-the-cnf-have-a-reasonable-startup-time-reasonable_startup_time>`__
     - Should (Not)
   * - ra2.app.041
     - Pods of the CNF must not run in privileged mode.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-there-are-any-privileged-containers-kubscape-version-privileged_containers>`__
     - Must (Not)
   * - ra2.app.042
     - No root user: None of the Pods of the CNF should run as a root user.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-any-containers-are-running-as-a-root-user-checks-the-user-outside-the-container-that-is-running-dockerd-non_root_user>`__
     - Should (Not)
   * - ra2.app.043
     - No privilege escalation: None of the containers of the CNF should allow
       privilege escalation.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-there-are-any-privi
       leged-containers-kubscape-version-privileged_containers>`__
     - Should (Not)
   * - ra2.app.044
     - All the Pods of the CNF must be able to execute with a non-root user having a non-root group. Both the
       runAsUser and the runAsGroup attributes must be set to a value greater than 999.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-containers-are-running-with-non-root-user-with-non-root-membership-non_root_containers>`__
     - Must
   * - ra2.app.045
     - Labels: Pods of the CNF should define at least the following labels:
       app.kubernetes.io/name, app.kubernetes.io/version
       and app.kubernetes.io/part-of
     - `Kubernetes documentation <https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/>`__
     - Should
   * - ra2.app.046
     - The Pods of the CNF must direct their logs to sdout or stderr. This enables the treatment of the logs as event
       steams.
     - `Kubernetes documentation <https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/>`__
     - Must
   * - ra2.app.047
     - The Pods of the CNF should not use the host ports. Using the host ports ties the CNF to a specific node, thereby
       making the CNF less portable and scalable.
     -
     - Must
   * - ra2.app.048
     - If SELinux is used in the Pods of the CNF, the options used to escalate privileges should not be allowed. The
       options spec.securityContext.seLinuxOptions.type, spec.containers[*].securityContext.seLinuxOptions.type,
       spec.initContainers[*].securityContext.seLinuxOptions, and
       spec.ephemeralContainers[*].securityContext.seLinuxOptions.type must either be unset altogether or set to one of
       the following allowed values container_t, container_init_t, or container_kvm_t.
     -
     - Must
