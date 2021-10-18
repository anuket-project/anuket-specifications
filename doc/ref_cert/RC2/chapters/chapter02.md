# Kubernetes Test Cases and Requirements Traceability

![Scope](../figures/bogo_ifo.png)

## Introduction

All of the requirements for RC2 have been defined in the Reference Model (RM) and Reference Architecture (RA2). The scope of this chapter is to identify and list down test cases based on these requirements. Users of this chapter will be able to use it to determine which test cases they must run in order to test compliance with the requirements. This will enable traceability between the test cases and requirements. They should be able to clearly see which requirements are covered by which tests and the mapping from a specific test result (pass or fail) to a requirement. Each requirement may have one or more test case associated with it.

### Goals
- Clear mapping between requirements and test cases
- Provide a stable set of point-in-time requirements and tests to achieve conformance
- Enable clear traceability of the coverage of requirements across consecutive releases of this document
- Clickable links from test cases to requirements
- One or more tests for every MUST requirement
- A set of test cases to serve as a template for Anuket Assured

### Non-Goals
- Defining any requirements
- Providing coverage for non-testable requirements

### Definitions
*must*: Test Cases that are marked as must are considered mandatory and must pass successfully

*should*: Test Cases that are marked as should are expected to be fulfilled by the cloud infrastructure but it is up to each service provider whether to accept a cloud infrastructure that is not fulfilling any of these requirements. The same applies to should not.

*may*: Test cases that are marked as may are considered optional. The same applies to may not.

## Traceability Matrix

### Kubernetes API testing

The primary objectives of the
[e2e tests](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md)
are to ensure a consistent and reliable behavior of the Kubernetes code base,
and to catch hard-to-test bugs before users do, when unit and integration tests
are insufficient. They are partially selected for the
[Software Conformance Certification program](https://github.com/cncf/k8s-conformance)
run by the Kubernetes community (under the aegis of the CNCF).

Anuket shares the same goal to give end users the confidence that when they use
a certified product they can rely on a high level of common functionality.
Then Anuket RC2 starts with the test list defined by
[K8s Conformance](https://github.com/cncf/k8s-conformance) which is expected to
grow according to the ongoing requirement traceability.

[End-to-End Testing](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md)
basically asks for focus and skip regexes to select or to blacklist
single tests:
  - focus basically matches
    Conformance or [Testing Special Interest Groups](https://github.com/kubernetes/community/blob/master/sig-testing/charter.md)
    in sub-sections below
  - skip excludes the SIG labels listed as optional in
    [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)

The Reference Conformance suites must be stable and executed on real
deployments. Then all the following labels are defacto skipped in
[End-to-End Testing](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md):
  - alpha
  - Disruptive
  - Flaky

It's worth mentioning that no alpha or Flaky test can be included in
Conformance as per the rules.

#### Conformance

It must be noted that the default
[K8s Conformance](https://github.com/cncf/k8s-conformance) testing is
disruptive thus Anuket RC2 rather picks
[non-disruptive-conformance](https://sonobuoy.io/docs/master/e2eplugin/)
testing as defined by [Sonobuoy](https://sonobuoy.io/).

focus: [Conformance]

skip:
  - [Disruptive]
  - NoExecuteTaintManager

#### API Machinery Testing

focus: [sig-api-machinery]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]
  - [Feature:CrossNamespacePodAffinity]
  - [Feature:StorageVersionAPI]

See [API Machinery Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-api-machinery)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)
for more details.

#### Apps Testing

focus: [sig-apps]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]
  - [Feature:DaemonSetUpdateSurge]
  - [Feature:IndexedJob]
  - [Feature:StatefulSet]
  - [Feature:StatefulUpgrade]
  - [Feature:SuspendJob]

See [Apps Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-apps)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)
for more details.

#### Auth Testing

focus: [sig-auth]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]
  - [Feature:BoundServiceAccountTokenVolume]
  - [Feature:PodSecurityPolicy]

See [Auth Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-auth)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)
for more details.

#### Cluster Lifecycle Testing

focus: [sig-cluster-lifecycle]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]

See [Cluster Lifecycle Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-cluster-lifecycle)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)
for more details.

#### Instrumentation Testing

focus: [sig-instrumentation]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]
  - [Feature:Elasticsearch]
  - [Feature:StackdriverAcceleratorMonitoring]
  - [Feature:StackdriverCustomMetrics]
  - [Feature:StackdriverExternalMetrics]
  - [Feature:StackdriverMetadataAgent]
  - [Feature:StackdriverMonitoring]

See [Instrumentation Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-instrumentation)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)
for more details.

#### Network Testing

The regexes load.balancer, LoadBalancer and
Network.should.set.TCP.CLOSE_WAIT.timeout are currently skipped because they
haven't been covered successfully neither by
[sig-release-1.22-blocking](https://github.com/kubernetes/test-infra/blob/master/config/jobs/kubernetes/sig-release/release-branch-jobs/1.22.yaml)
nor by
[Anuket RC2 verification](https://build.opnfv.org/ci/view/functest-kubernetes/job/functest-kubernetes-v1.22-daily/8/)

Please note that a couple of tests must be skipped by name below as they are no
appropriate labels.

focus: [sig-network]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]
  - [Feature:Example]
  - [Feature:Ingress]
  - [Feature:IPv6DualStack]
  - [Feature:kubemci]
  - [Feature:KubeProxyDaemonSetMigration]
  - [Feature:KubeProxyDaemonSetUpgrade]
  - [Feature:NEG]
  - [Feature:Networking-IPv6]
  - [Feature:NetworkPolicy]
  - [Feature:PerformanceDNS]
  - [Feature:SCTP]
  - [Feature:SCTPConnectivity]
  - DNS configMap nameserver
  - load.balancer
  - LoadBalancer
  - Network.should.set.TCP.CLOSE_WAIT.timeout

See [Network Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-network)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)

#### Node Testing

focus: [sig-node]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]
  - [Feature:ExperimentalResourceUsageTracking]
  - [Feature:GPUUpgrade]
  - [Feature:PodGarbageCollector]
  - [Feature:RegularResourceUsageTracking]
  - [NodeFeature:DownwardAPIHugePages]
  - [NodeFeature:RuntimeHandler]

See [Node Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-node)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)

#### Scheduling Testing

focus: [sig-scheduling]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]
  - [Feature:GPUDevicePlugin]
  - [Feature:Recreate]

See [Scheduling Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-scheduling)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)

#### Storage Testing

It should be noted that all in-tree driver testing, [Driver:+], is skipped.
Conforming to
[the upstream gate](https://github.com/kubernetes/test-infra/blob/master/config/jobs/kubernetes/sig-release/release-branch-jobs/1.22.yaml),
all PersistentVolumes NFS testing is also skipped.
The following exclusions are about
[the deprecated in-tree GitRepo volume type](https://github.com/kubernetes-sigs/kind/issues/2356):
  - should provision storage with different parameters
  - should not cause race condition when used for git_repo

Please note that a couple of tests must be skipped by name below as they are no
appropriate labels.

focus: [sig-storage]

skip:
  - [alpha]
  - [Disruptive]
  - [Flaky]
  - [Driver:+]
  - [Feature:ExpandInUsePersistentVolumes]
  - [Feature:Flexvolumes]
  - [Feature:GKELocalSSD]
  - [Feature:VolumeSnapshotDataSource]
  - [Feature:Flexvolumes]
  - [Feature:vsphere]
  - [Feature:Volumes]
  - [Feature:Windows]
  - [NodeFeature:EphemeralStorage]
  - PersistentVolumes.NFS
  - should provision storage with different parameters
  - should not cause race condition when used for git_repo

See [Storage Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-storage)
and [Reference Architecture-2 (RA-2) Chapter 6](../../../ref_arch/kubernetes/chapters/chapter06.md)

### Kubernetes API benchmarking

[Rally](https://github.com/openstack/rally) is a tool and framework that
performs Kubernetes API benchmarking.

[Functest Kubernetes Benchmarking](https://git.opnfv.org/functest-kubernetes/tree/docker/benchmarking/testcases.yaml?h=stable%2Fv1.22)
proposed a Rally-based test case,
[xrally_kubernetes_full](http://artifacts.opnfv.org/functest-kubernetes/96Y19H7RR0T5/functest-kubernetes-opnfv-functest-kubernetes-benchmarking-v1.22-xrally_kubernetes_full-run-3/xrally_kubernetes_full/xrally_kubernetes_full.html),
which iterates 10 times the mainline
[xrally-kubernetes](https://github.com/xrally/xrally-kubernetes) scenarios.

At the time of writing, no KPI is defined in
[Kubernetes based Reference Architecture](../../../ref_arch/kubernetes/chapters/chapter02.md)
which would have asked for an update of the default SLA (maximum failure rate
of 0%) proposed in
[Functest Kubernetes Benchmarking](https://git.opnfv.org/functest-kubernetes/tree/docker/benchmarking/testcases.yaml?h=stable%2Fv1.22)

[Functest xrally_kubernetes_full](http://artifacts.opnfv.org/functest-kubernetes/96Y19H7RR0T5/functest-kubernetes-opnfv-functest-kubernetes-benchmarking-v1.22-xrally_kubernetes_full-run-3/xrally_kubernetes_full/xrally_kubernetes_full.html):

| Scenarios                                                          | Iterations |
|--------------------------------------------------------------------|:----------:|
| Kubernetes.create_and_delete_deployment                            | 10         |
| Kubernetes.create_and_delete_job                                   | 10         |
| Kubernetes.create_and_delete_namespace                             | 10         |
| Kubernetes.create_and_delete_pod                                   | 10         |
| Kubernetes.create_and_delete_pod_with_configmap_volume             | 10         |
| Kubernetes.create_and_delete_pod_with_configmap_volume [2]         | 10         |
| Kubernetes.create_and_delete_pod_with_emptydir_volume              | 10         |
| Kubernetes.create_and_delete_pod_with_emptydir_volume [2]          | 10         |
| Kubernetes.create_and_delete_pod_with_hostpath_volume              | 10         |
| Kubernetes.create_and_delete_pod_with_secret_volume                | 10         |
| Kubernetes.create_and_delete_pod_with_secret_volume [2]            | 10         |
| Kubernetes.create_and_delete_replicaset                            | 10         |
| Kubernetes.create_and_delete_replication_controller                | 10         |
| Kubernetes.create_and_delete_statefulset                           | 10         |
| Kubernetes.create_check_and_delete_pod_with_cluster_ip_service     | 10         |
| Kubernetes.create_check_and_delete_pod_with_cluster_ip_service [2] | 10         |
| Kubernetes.create_check_and_delete_pod_with_node_port_service      | 10         |
| Kubernetes.create_rollout_and_delete_deployment                    | 10         |
| Kubernetes.create_scale_and_delete_replicaset                      | 10         |
| Kubernetes.create_scale_and_delete_replication_controller          | 10         |
| Kubernetes.create_scale_and_delete_statefulset                     | 10         |
| Kubernetes.list_namespaces                                         | 10         |

The following software versions are considered to benchmark Kubernetes v1.22
(latest stable release) selected by Anuket:

| software                | version     |
|-------------------------|-------------|
| Functest                | v1.22       |
| xrally-kubernetes       | 1.1.1.dev12 |

### Dataplane benchmarking

[Kubernetes perf-tests repository](https://github.com/kubernetes/perf-tests)
hosts various Kubernetes-related performance test related tools especially
[netperf](https://github.com/kubernetes/perf-tests/tree/master/network/benchmarks/netperf)
which benchmarks Kubernetes networking performance.

As listed in [netperf's README](https://github.com/kubernetes/perf-tests/tree/master/network/benchmarks/netperf#readme),
the 5 major network traffic paths are combination of pod IP vs virtual IP and
whether the pods are co-located on the same node versus a remotely located
pod:
  - same node using pod IP
  - same node using cluster/virtual IP
  - remote node using pod IP
  - remote node using cluster/virtual IP
  - same node pod hairpin to itself using cluster/virtual IP

It should be noted that
[netperf](https://github.com/kubernetes/perf-tests/tree/master/network/benchmarks/netperf)
leverages [iperf](https://github.com/esnet/iperf) (both TCP and UDP modes) and
[Netperf](https://github.com/HewlettPackard/netperf/).

At the time of writing, no KPI is defined in Anuket chapters which would have
asked for an update of the default SLA proposed in
[Functest Kubernetes Benchmarking](https://git.opnfv.org/functest-kubernetes/tree/docker/benchmarking?h=stable/v1.22).

### Security testing

There are a couple of opensource tools that help securing the Kubernetes stack.
Amongst them,
[Functest Kubernetes Security](https://git.opnfv.org/functest-kubernetes/tree/docker/security/testcases.yaml?h=stable%2Fv1.22)
offers two test cases based on
[kube-hunter](https://github.com/aquasecurity/kube-hunter) and
[kube-bench](https://github.com/aquasecurity/kube-bench).

[kube-hunter](https://github.com/aquasecurity/kube-hunter) hunts for security
weaknesses in Kubernetes clusters and
[kube-bench](https://github.com/aquasecurity/kube-bench) checks
whether Kubernetes is deployed securely by running the checks documented in the
[CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/).

[kube-hunter](https://github.com/aquasecurity/kube-hunter) classifies all
vulnerabilities as low, medium, and high. In context of this conformance suite,
only the high vulnerabilities lead to a test case failure. Then all low and
medium vulnerabilities are only printed for information.

Here are the
[vulnerability categories](https://github.com/aquasecurity/kube-hunter/blob/v0.3.1/kube_hunter/core/events/types.py)
tagged as high by
[kube-hunter](https://github.com/aquasecurity/kube-hunter):
- RemoteCodeExec
- IdentityTheft
- PrivilegeEscalation

At the time of writing, none of the  Center for Internet Security (CIS) rules
are defined as mandatory (e.g. sec.std.001: The Cloud Operator **should**
comply with Center for Internet Security CIS Controls) else it would have
required an update of the default kube-bench behavior (all failures and
warnings are only printed) as integrated in
[Functest Kubernetes Security](https://git.opnfv.org/functest-kubernetes/tree/docker/security/testcases.yaml?h=stable%2Fv1.22).

The following software versions are considered to verify Kubernetes v1.22
(latest stable release) selected by Anuket:

| software                | version     |
|-------------------------|-------------|
| Functest                | v1.22       |
| kube-hunter             | 0.3.1       |
| kube-bench              | 0.3.1       |

### Opensource CNF onboarding and testing

Running opensource containerized network functions (CNF) is a key technical
solution to ensure that the platforms meet Network Functions Virtualization
requirements.

Functest CNF offers 2 test cases which automatically onboard and test
[Clearwater IMS](https://github.com/Metaswitch/clearwater-docker)
via kubecltl and Helm. It's worth mentioning that this CNF is covered by the
upstream tests (see
[clearwater-live-test](https://github.com/Metaswitch/clearwater-live-test)).

The following software versions are considered to verify Kubernetes v1.22
(latest stable release) selected by Anuket:

| software                | version     |
|-------------------------|-------------|
| Functest                | v1.22       |
| clearwater              | release-130 |
| Helm                    | v3.3.1      |

## Test Cases Traceability to Requirements

The following test case must pass as they are for Reference Conformance:

| container                                     | test case                | criteria | requirements                          |
|-----------------------------------------------|--------------------------|:--------:|---------------------------------------|
| opnfv/functest-kubernetes-smoke:v1.22         | xrally_kubernetes        | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | k8s_conformance          | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | k8s_conformance_serial   | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_api_machinery        | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_api_machinery_serial | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_apps                 | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_apps_serial          | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_auth                 | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_cluster_lifecycle    | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_instrumentation      | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_network              | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_node                 | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_scheduling_serial    | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_storage              | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:v1.22         | sig_storage_serial       | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-security:v1.22      | kube_hunter              | PASS     | Security testing                      |
| opnfv/functest-kubernetes-security:v1.22      | kube_bench_master        | PASS     | Security testing                      |
| opnfv/functest-kubernetes-security:v1.22      | kube_bench_node          | PASS     | Security testing                      |
| opnfv/functest-kubernetes-benchmarking:v1.22  | xrally_kubernetes_full   | PASS     | Kubernetes API benchmarking           |
| opnfv/functest-kubernetes-benchmarking:v1.22  | netperf                  | PASS     | Dataplane benchmarking                |
| opnfv/functest-kubernetes-cnf:v1.22           | k8s_vims                 | PASS     | Opensource CNF onboarding and testing |
| opnfv/functest-kubernetes-cnf:v1.22           | helm_vims                | PASS     | Opensource CNF onboarding and testing |
