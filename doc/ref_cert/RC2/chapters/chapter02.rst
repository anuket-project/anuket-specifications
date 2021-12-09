Kubernetes Test Cases and Requirements Traceability
===================================================

Introduction
------------

All of the requirements for RC2 have been defined in the Reference Model
(RM) and Reference Architecture (RA2). The scope of this chapter is to
identify and list down test cases based on these requirements. Users of
this chapter will be able to use it to determine which test cases they
must run in order to test compliance with the requirements. This will
enable traceability between the test cases and requirements. They should
be able to clearly see which requirements are covered by which tests and
the mapping from a specific test result (pass or fail) to a requirement.
Each requirement may have one or more test case associated with it.

Goals
~~~~~

-  Clear mapping between requirements and test cases
-  Provide a stable set of point-in-time requirements and tests to
   achieve conformance
-  Enable clear traceability of the coverage of requirements across
   consecutive releases of this document
-  Clickable links from test cases to requirements
-  One or more tests for every MUST requirement
-  A set of test cases to serve as a template for Anuket Assured

Non-Goals
~~~~~~~~~

-  Defining any requirements
-  Providing coverage for non-testable requirements

Definitions
~~~~~~~~~~~

*must*: Test Cases that are marked as must are considered mandatory and
must pass successfully

*should*: Test Cases that are marked as should are expected to be
fulfilled by the cloud infrastructure but it is up to each service
provider whether to accept a cloud infrastructure that is not fulfilling
any of these requirements. The same applies to should not.

*may*: Test cases that are marked as may are considered optional. The
same applies to may not.

Traceability Matrix
-------------------

Kubernetes API testing
~~~~~~~~~~~~~~~~~~~~~~

The primary objectives of the `e2e
tests <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md>`__
are to ensure a consistent and reliable behavior of the Kubernetes code
base, and to catch hard-to-test bugs before users do, when unit and
integration tests are insufficient. They are partially selected for the
`Software Conformance Certification
program <https://github.com/cncf/k8s-conformance>`__ run by the
Kubernetes community (under the aegis of the CNCF).

Anuket shares the same goal to give end users the confidence that when
they use a certified product they can rely on a high level of common
functionality. Then Anuket RC2 starts with the test list defined by `K8s
Conformance <https://github.com/cncf/k8s-conformance>`__ which is
expected to grow according to the ongoing requirement traceability.

`End-to-End
Testing <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md>`__
basically asks for focus and skip regexes to select or to blacklist
single tests:

-  focus basically matches Conformance or `Testing Special Interest
   Groups <https://github.com/kubernetes/community/blob/master/sig-testing/charter.md>`__
   in sub-sections below
-  skip excludes the SIG labels listed as optional in `Reference
   Architecture-2 (RA-2) Chapter
   6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__

The Reference Conformance suites must be stable and executed on real
deployments. Then all the following labels are defacto skipped in
`End-to-End
Testing <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md>`__:

-  alpha
-  Disruptive
-  Flaky

It’s worth mentioning that no alpha or Flaky test can be included in
Conformance as per the rules.

Conformance
^^^^^^^^^^^

It must be noted that the default `K8s
Conformance <https://github.com/cncf/k8s-conformance>`__ testing is
disruptive thus Anuket RC2 rather picks
`non-disruptive-conformance <https://sonobuoy.io/docs/main/e2eplugin/>`__
testing as defined by `Sonobuoy <https://sonobuoy.io/>`__.

focus: `Conformance <#conformance>`__

skip:

-  [Disruptive]
-  NoExecuteTaintManager

API Machinery Testing
^^^^^^^^^^^^^^^^^^^^^

focus: [sig-api-machinery]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]
-  [Feature:CrossNamespacePodAffinity]
-  [Feature:StorageVersionAPI]

See `API Machinery Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-api-machinery>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__
for more details.

Apps Testing
^^^^^^^^^^^^

focus: [sig-apps]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]
-  [Feature:DaemonSetUpdateSurge]
-  [Feature:IndexedJob]
-  [Feature:StatefulSet]
-  [Feature:StatefulUpgrade]
-  [Feature:SuspendJob]

See `Apps Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-apps>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__
for more details.

Auth Testing
^^^^^^^^^^^^

focus: [sig-auth]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]
-  [Feature:BoundServiceAccountTokenVolume]
-  [Feature:PodSecurityPolicy]

See `Auth Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-auth>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__
for more details.

Cluster Lifecycle Testing
^^^^^^^^^^^^^^^^^^^^^^^^^

focus: [sig-cluster-lifecycle]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]

See `Cluster Lifecycle Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-cluster-lifecycle>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__
for more details.

Instrumentation Testing
^^^^^^^^^^^^^^^^^^^^^^^

focus: [sig-instrumentation]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]
-  [Feature:Elasticsearch]
-  [Feature:StackdriverAcceleratorMonitoring]
-  [Feature:StackdriverCustomMetrics]
-  [Feature:StackdriverExternalMetrics]
-  [Feature:StackdriverMetadataAgent]
-  [Feature:StackdriverMonitoring]

See `Instrumentation Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-instrumentation>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__
for more details.

Network Testing
^^^^^^^^^^^^^^^

The regexes load.balancer, LoadBalancer and
Network.should.set.TCP.CLOSE_WAIT.timeout are currently skipped because
they haven’t been covered successfully neither by
`sig-release-1.22-blocking <https://github.com/kubernetes/test-infra/blob/master/config/jobs/kubernetes/sig-release/release-branch-jobs/1.22.yaml>`__
nor by `Anuket RC2
verification <https://build.opnfv.org/ci/view/functest-kubernetes/job/functest-kubernetes-v1.22-daily/8/>`__

Please note that a couple of tests must be skipped by name below as they
are no appropriate labels.

focus: [sig-network]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]
-  [Feature:Example]
-  [Feature:Ingress]
-  [Feature:IPv6DualStack]
-  [Feature:kubemci]
-  [Feature:KubeProxyDaemonSetMigration]
-  [Feature:KubeProxyDaemonSetUpgrade]
-  [Feature:NEG]
-  [Feature:Networking-IPv6]
-  [Feature:NetworkPolicy]
-  [Feature:PerformanceDNS]
-  [Feature:SCTP]
-  [Feature:SCTPConnectivity]
-  DNS configMap nameserver
-  load.balancer
-  LoadBalancer
-  Network.should.set.TCP.CLOSE_WAIT.timeout

See `Network Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-network>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__

Node Testing
^^^^^^^^^^^^

focus: [sig-node]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]
-  [Feature:ExperimentalResourceUsageTracking]
-  [Feature:GPUUpgrade]
-  [Feature:PodGarbageCollector]
-  [Feature:RegularResourceUsageTracking]
-  [NodeFeature:DownwardAPIHugePages]
-  [NodeFeature:RuntimeHandler]

See `Node Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-node>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__

Scheduling Testing
^^^^^^^^^^^^^^^^^^

focus: [sig-scheduling]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]
-  [Feature:GPUDevicePlugin]
-  [Feature:Recreate]

See `Scheduling Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-scheduling>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__

Storage Testing
^^^^^^^^^^^^^^^

It should be noted that all in-tree driver testing, [Driver:+], is
skipped. Conforming to `the upstream
gate <https://github.com/kubernetes/test-infra/blob/master/config/jobs/kubernetes/sig-release/release-branch-jobs/1.22.yaml>`__,
all PersistentVolumes NFS testing is also skipped. The following
exclusions are about `the deprecated in-tree GitRepo volume
type <https://github.com/kubernetes-sigs/kind/issues/2356>`__:

-  should provision storage with different parameters
-  should not cause race condition when used for git_repo

Please note that a couple of tests must be skipped by name below as they
are no appropriate labels.

focus: [sig-storage]

skip:

-  [alpha]
-  [Disruptive]
-  [Flaky]
-  [Driver:+]
-  [Feature:ExpandInUsePersistentVolumes]
-  [Feature:Flexvolumes]
-  [Feature:GKELocalSSD]
-  [Feature:VolumeSnapshotDataSource]
-  [Feature:Flexvolumes]
-  [Feature:vsphere]
-  [Feature:Volumes]
-  [Feature:Windows]
-  [NodeFeature:EphemeralStorage]
-  PersistentVolumes.NFS
-  should provision storage with different parameters
-  should not cause race condition when used for git_repo

See `Storage Special Interest
Group <https://github.com/kubernetes/community/tree/master/sig-storage>`__
and `Reference Architecture-2 (RA-2) Chapter
6 <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/chapters/chapter06.html>`__

Kubernetes API benchmarking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Rally <https://github.com/openstack/rally>`__ is a tool and framework
that performs Kubernetes API benchmarking.

`Functest Kubernetes
Benchmarking <https://git.opnfv.org/functest-kubernetes/tree/docker/benchmarking/testcases.yaml?h=stable%2Fv1.22>`__
proposed a Rally-based test case,
`xrally_kubernetes_full <http://artifacts.opnfv.org/functest-kubernetes/96Y19H7RR0T5/functest-kubernetes-opnfv-functest-kubernetes-benchmarking-v1.22-xrally_kubernetes_full-run-3/xrally_kubernetes_full/xrally_kubernetes_full.html>`__,
which iterates 10 times the mainline
`xrally-kubernetes <https://github.com/xrally/xrally-kubernetes>`__
scenarios.

At the time of writing, no KPI is defined in `Kubernetes based Reference
Architecture <https://cntt.readthedocs.io/en/latest/ref_arch/kubernetes/>`__
which would have asked for an update of the default SLA (maximum failure
rate of 0%) proposed in `Functest Kubernetes
Benchmarking <https://git.opnfv.org/functest-kubernetes/tree/docker/benchmarking/testcases.yaml?h=stable%2Fv1.22>`__

`Functest
xrally_kubernetes_full <http://artifacts.opnfv.org/functest-kubernetes/96Y19H7RR0T5/functest-kubernetes-opnfv-functest-kubernetes-benchmarking-v1.22-xrally_kubernetes_full-run-3/xrally_kubernetes_full/xrally_kubernetes_full.html>`__:

+--------------------------------------------------------+------------+
| Scenarios                                              | Iterations |
+========================================================+============+
| Kubernetes.create_and_delete_deployment                | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_job                       | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_namespace                 | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_pod                       | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_pod_with_configmap_volume | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_pod_with_configmap_volume | 10         |
| [2]                                                    |            |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_pod_with_emptydir_volume  | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_pod_with_emptydir_volume  | 10         |
| [2]                                                    |            |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_pod_with_hostpath_volume  | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_pod_with_secret_volume    | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_pod_with_secret_volume    | 10         |
| [2]                                                    |            |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_replicaset                | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_replication_controller    | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_and_delete_statefulset               | 10         |
+--------------------------------------------------------+------------+
| Kubernet                                               | 10         |
| es.create_check_and_delete_pod_with_cluster_ip_service |            |
+--------------------------------------------------------+------------+
| Kubernet                                               | 10         |
| es.create_check_and_delete_pod_with_cluster_ip_service |            |
| [2]                                                    |            |
+--------------------------------------------------------+------------+
| Kuberne                                                | 10         |
| tes.create_check_and_delete_pod_with_node_port_service |            |
+--------------------------------------------------------+------------+
| Kubernetes.create_rollout_and_delete_deployment        | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.create_scale_and_delete_replicaset          | 10         |
+--------------------------------------------------------+------------+
| Kub                                                    | 10         |
| ernetes.create_scale_and_delete_replication_controller |            |
+--------------------------------------------------------+------------+
| Kubernetes.create_scale_and_delete_statefulset         | 10         |
+--------------------------------------------------------+------------+
| Kubernetes.list_namespaces                             | 10         |
+--------------------------------------------------------+------------+

The following software versions are considered to benchmark Kubernetes
v1.22 (latest stable release) selected by Anuket:

================= ===========
software          version
================= ===========
Functest          v1.22
xrally-kubernetes 1.1.1.dev12
================= ===========

Dataplane benchmarking
~~~~~~~~~~~~~~~~~~~~~~

`Kubernetes perf-tests
repository <https://github.com/kubernetes/perf-tests>`__ hosts various
Kubernetes-related performance test related tools especially
`netperf <https://github.com/kubernetes/perf-tests/tree/master/network/benchmarks/netperf>`__
which benchmarks Kubernetes networking performance.

As listed in `netperf’s
README <https://github.com/kubernetes/perf-tests/tree/master/network/benchmarks/netperf#readme>`__,
the 5 major network traffic paths are combination of pod IP vs virtual
IP and whether the pods are co-located on the same node versus a
remotely located pod:

-  same node using pod IP
-  same node using cluster/virtual IP
-  remote node using pod IP
-  remote node using cluster/virtual IP
-  same node pod hairpin to itself using cluster/virtual IP

It should be noted that
`netperf <https://github.com/kubernetes/perf-tests/tree/master/network/benchmarks/netperf>`__
leverages `iperf <https://github.com/esnet/iperf>`__ (both TCP and UDP
modes) and `Netperf <https://github.com/HewlettPackard/netperf/>`__.

At the time of writing, no KPI is defined in Anuket chapters which would
have asked for an update of the default SLA proposed in `Functest
Kubernetes
Benchmarking <https://git.opnfv.org/functest-kubernetes/tree/docker/benchmarking?h=stable/v1.22>`__.

Security testing
~~~~~~~~~~~~~~~~

There are a couple of opensource tools that help securing the Kubernetes
stack. Amongst them, `Functest Kubernetes
Security <https://git.opnfv.org/functest-kubernetes/tree/docker/security/testcases.yaml?h=stable%2Fv1.22>`__
offers two test cases based on
`kube-hunter <https://github.com/aquasecurity/kube-hunter>`__ and
`kube-bench <https://github.com/aquasecurity/kube-bench>`__.

`kube-hunter <https://github.com/aquasecurity/kube-hunter>`__ hunts for
security weaknesses in Kubernetes clusters and
`kube-bench <https://github.com/aquasecurity/kube-bench>`__ checks
whether Kubernetes is deployed securely by running the checks documented
in the `CIS Kubernetes
Benchmark <https://www.cisecurity.org/benchmark/kubernetes/>`__.

`kube-hunter <https://github.com/aquasecurity/kube-hunter>`__ classifies
all vulnerabilities as low, medium, and high. In context of this
conformance suite, only the high vulnerabilities lead to a test case
failure. Then all low and medium vulnerabilities are only printed for
information.

Here are the `vulnerability
categories <https://github.com/aquasecurity/kube-hunter/blob/v0.3.1/kube_hunter/core/events/types.py>`__
tagged as high by
`kube-hunter <https://github.com/aquasecurity/kube-hunter>`__:

-  RemoteCodeExec
-  IdentityTheft
-  PrivilegeEscalation

At the time of writing, none of the Center for Internet Security (CIS)
rules are defined as mandatory (e.g. sec.std.001: The Cloud Operator
**should** comply with Center for Internet Security CIS Controls) else
it would have required an update of the default kube-bench behavior (all
failures and warnings are only printed) as integrated in `Functest
Kubernetes
Security <https://git.opnfv.org/functest-kubernetes/tree/docker/security/testcases.yaml?h=stable%2Fv1.22>`__.

The following software versions are considered to verify Kubernetes
v1.22 (latest stable release) selected by Anuket:

=========== =======
software    version
=========== =======
Functest    v1.22
kube-hunter 0.3.1
kube-bench  0.3.1
=========== =======

Opensource CNF onboarding and testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running opensource containerized network functions (CNF) is a key
technical solution to ensure that the platforms meet Network Functions
Virtualization requirements.

Functest CNF offers 2 test cases which automatically onboard and test
`Clearwater IMS <https://github.com/Metaswitch/clearwater-docker>`__ via
kubecltl and Helm. It’s worth mentioning that this CNF is covered by the
upstream tests (see
`clearwater-live-test <https://github.com/Metaswitch/clearwater-live-test>`__).

The following software versions are considered to verify Kubernetes
v1.22 (latest stable release) selected by Anuket:

========== ===========
software   version
========== ===========
Functest   v1.22
clearwater release-130
Helm       v3.3.1
========== ===========

Test Cases Traceability to Requirements
---------------------------------------

The following test case must pass as they are for Reference Conformance:

+-------------------------------+-------------------+------+------------------+
| container                     | test suite        | cri\ | requirements     |
|                               |                   | ter\ |                  |
|                               |                   | ia   |                  |
+===============================+===================+======+==================+
| opnfv/functest-\              | xrally\_\         | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | kubernetes        |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | k8s\_\            | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | conformance       |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | k8s_confor\       | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | mance_serial      |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_api\_\        | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | machinery         |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_api\_\        | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | machinery_serial  |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_apps          | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        |                   |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig\_\            | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | apps_serial       |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_auth          | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        |                   |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_cluster\_\    | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | lifecycle         |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig\_\            | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | instrumentation   |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_network       | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        |                   |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_node          | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        |                   |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_scheduling\_\ | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | serial            |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig_storage       | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        |                   |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | sig\_\            | PASS | Kubernetes API   |
| kubernetes-smoke:v1.22        | storage_serial    |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | kube_hunter       | PASS | Security testing |
| kubernetes-security:v1.22     |                   |      |                  |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | kube\_\           | PASS | Security testing |
| kubernetes-security:v1.22     | bench_master      |      |                  |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | kube\_\           | PASS | Security testing |
| kubernetes-security:v1.22     | bench_node        |      |                  |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | xrally\_\         | PASS | Kubernetes API   |
| kubernetes-benchmarking:v1.22 | kubernetes_full   |      | benchmarking     |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | netperf           | PASS | Dataplane        |
| kubernetes-benchmarking:v1.22 |                   |      | benchmarking     |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | k8s_vims          | PASS | Opensource CNF   |
| kubernetes-cnf:v1.22          |                   |      | onboarding and   |
|                               |                   |      | testing          |
+-------------------------------+-------------------+------+------------------+
| opnfv/functest-\              | helm_vims         | PASS | Opensource CNF   |
| kubernetes-cnf:v1.22          |                   |      | onboarding and   |
|                               |                   |      | testing          |
+-------------------------------+-------------------+------+------------------+
