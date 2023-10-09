API and Feature Testing requirements
====================================

Introduction to API and Feature Testing requirement
---------------------------------------------------

The CNCF has defined a :cite:t:`k8s-testing-sig_ra2` to help the community to write and run tests, and to contribute,
analyze, and act upon test results. This chapter maps the requirements written in the previous chapters as mandatory
Special Interest Group features. It enforces the overall requirements traceability to testing, especially those offered
for :cite:t:`k8s-testing-sig-e2e-tests_ra2`.
The Anuket Reference Conformance (RC2) testing matches the features and tests defined here.

Kubernetes feature gate policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cite:t:`k8s-feature-gates_ra2` are a set of key-value pairs that describe the Kubernetes features. The components of the
control plane of the Kubernetes Clusters can be run with different Feature Gate settings.

A feature can be in the Alpha, Beta, or General Availability (GA) stage:

- Alpha features are disabled by default. Breaking API changes may be expected. They may contain bugs, and support may
  be dropped.
- Beta features are disabled by default. They are well tested, and support will not be dropped, although breaking API
  changes may happen. As of 1.24, any existing Beta feature will continue to be enabled by default. However, new beta
  APIs and features will not be enabled by default after Kubernetes 1.24.
  For more information, see :cite:t:`k8s-kep-3136_ra2`
- GA features are stable. They are always enabled and cannot be disabled.

Only those Kubernetes features can be made mandatory in this Reference Architecture which are GA or were Beta before
Kubernetes 1.24.

A list of feature gates is available here :cite:p:`k8s-feature-gates_ra2`.

Kubernetes API policy
~~~~~~~~~~~~~~~~~~~~~

The :cite:t:`k8s-api_ra2` supports all operations and communications between components, and external user commands.
Everything in the Kubernetes platform is treated as an API object. Different API versions indicate different levels of
stability and support. An API can have Alpha, Beta or Stable versions. The version of APIs that are backed by a feature
will match the stage of the feature itself (i.e. Alpha, Beta or GA or Stable).

The policy for RA2 to include Kubernetes APIs as mandatory is as follows:

In these Reference Architecture APIs, only those APIs which are in any of the following stages are mandatory:

- Stable.
- Beta when introduced before Kubernetes version 1.24.
- Alpha or Beta when required by RA2 Ch4 specifications, or when included on the list of Mandatory API Groups below.

The Kubernetes API reference is available here :cite:p:`k8s-api-reference_ra2`.

The list of :cite:t:`k8s-v1.26-api-groups` that are mandatory is as follows:

.. list-table:: Mandatory API Groups
   :widths: 30 30
   :header-rows: 1

   * - Group
     - Version
   * - admissionregistration.k8s.io
     - v1
   * - apiextensions.k8s.io
     - v1
   * - apiregistration.k8s.io
     - v1
   * - apps
     - v1
   * - authentication.k8s.io
     - v1
   * - authorization.k8s.io
     - v1
   * - autoscaling
     - v1, v2
   * - batch
     - v1
   * - certificates.k8s.io
     - v1
   * - coordination.k8s.io
     - v1
   * - core
     - v1
   * - discovery.k8s.io
     - v1
   * - events.k8s.io
     - v1
   * - flowcontrol.apiserver.k8s.io
     - v1beta2
   * - networking.k8s.io
     - v1
   * - node.k8s.io
     - v1
   * - policy
     - v1
   * - rbac.authorization.k8s.io
     - v1
   * - scheduling.k8s.io
     - v1
   * - storage.k8s.io
     - v1

API Machinery Special Interest Group :cite:p:`k8s-api-sig-api-machinery_ra2`
----------------------------------------------------------------------------

.. list-table:: API Machinery Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test
   * - None
     - X
     - Kubernetes mainstream features
   * - Feature:ComprehensiveNamespaceDraining
     - X
     - The deletion of namespaces should always be fast (all 100 namespaces in 150 seconds).
   * - Feature: CrossNamespacePodAffinity :cite:p:`k8s-feature-crossnamespacepodaffinity_ra2`
     -
     - The CrossNamespacePodAffinity feature verifies the ResourceQuota with the cross namespace pod affinity scope
       using scope-selectors.
   * - Feature: PodPriority :cite:p:`k8s-feature-crossnamespacepodaffinity_ra2`
     - X
     - The PodPriority feature verifies the ResourceQuota's priority class scope against a pod with a different
       priority class.
   * - Feature:ScopeSelectors
     - X
     - Verify ResourceQuota with terminating scopes through scope selectors
   * - Feature: StorageVersionAPI :cite:p:`k8s-feature-storageversionapi_ra2`
     -
     -

Apps  :cite:p:`k8s-api-sig-apps_ra2`
------------------------------------

.. list-table:: Apps Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test
   * - None
     - X
     - Kubernetes mainstream features
   * - Feature: DaemonSetUpdateSurge :cite:p:`k8s-feature-daemonsetupdatesurge_ra2`
     -
     - The Daemon set should surge the pods onto the nodes when the specification is updated and the update strategy is
       RollingUpdate.
   * - Feature: IndexedJob :cite:p:`k8s-feature-indexedjob_ra2`
     -
     - The IndexedJob feature should create pods for an indexed job with completion indexes.
   * - Feature: StatefulSet :cite:p:`k8s-feature-statefulset_ra2`
     -
     - The StatefulSet feature should create a working zookeeper cluster.
   * - Feature:StatefulUpgrade
     -
     - The StatefulUpgrade feature should maintain a functioning cluster.
   * - Feature: SuspendJob :cite:p:`k8s-feature-suspendjob_ra2`
     -
     - The SuspendJob feature should not create pods when they have been created in a suspended state.
   * - Feature: TaintEviction :cite:p:`k8s-feature-tainteviction_ra2`
     -
     - All pods on the unreachable node should be marked as NotReady when the node condition is set to NotReady. All
       pods should be evicted after eviction timeout has passed.
   * - Feature: TTLAfterFinished :cite:p:`k8s-feature-ttlafterfinished_ra2`
     - X
     - The job should be deleted once it has finished, after the TTL has elapsed.

Auth Special Interest Group :cite:p:`k8s-api-sig-auth_ra2`
----------------------------------------------------------

.. list-table:: Auth Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test
   * - None
     - X
     - Kubernetes mainstream features
   * - Feature: BoundServiceAccountTokenVolume :cite:p:`k8s-feature-boundserviceaccounttokenvolume_ra2`
     -
     - The ServiceAccount admission controller migration upgrade should maintain a functioning cluster.
   * - Feature:NodeAuthenticator
     - X
     - The kubelet's main port 10250 should reject requests with no credentials.
   * - Feature:NodeAuthorizer
     - X
     - Setting existing and non-existent attributes should return with a Forbidden error, not a NotFound error.
   * - NodeFeature:FSGroup
     - X
     - ServiceAccounts should set ownership and permission when RunAsUser or FsGroup is present.

Cluster Lifecycle Special Interest Group :cite:p:`k8s-api-sig-cluster-lifecycle_ra2`
------------------------------------------------------------------------------------

.. list-table:: Cluster Lifecycle Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test
   * - None
     - X
     - Kubernetes mainstream features
   * - Feature:BootstrapTokens
     - X
     - The BootstrapTokens feature should delete the token secret when the secret has expired.


Instrumentation Special Interest Group :cite:p:`k8s-api-sig-instrumentation_ra2`
--------------------------------------------------------------------------------

.. list-table:: Instrumentation Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test
   * - None
     - X
     - Kubernetes mainstream features
   * - Feature:Elasticsearch
     -
     - The Elasticsearch feature should check that the Kibana logging instance is alive.
   * - Feature: StackdriverAcceleratorMonitoring
     -
     - Stackdriver Monitoring should have accelerator metrics.
   * - Feature:StackdriverCustomMetrics
     -
     - Stackdriver Monitoring should run Custom Metrics - Stackdriver Adapter for the new resource model.
   * - Feature:StackdriverExternalMetrics
     -
     - Stackdriver Monitoring should run Custom Metrics - Stackdriver Adapter for external metrics.
   * - Feature:StackdriverMetadataAgent
     -
     - Stackdriver Monitoring should run Stackdriver Metadata Agent.
   * - Feature:StackdriverMonitoring
     -
     -

Network Special Interest Group :cite:p:`k8s-api-sig-network_ra2`
----------------------------------------------------------------

.. list-table:: Network Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test.
   * - None
     - X
     - Kubernetes mainstream features.
   * - Feature:Example
     -
     - The example feature should create a pod that uses DNS.
   * - Feature:Ingress
     -
     - The Ingress feature should prevent ingress creation if more than one IngressClass is marked as a default.
   * - Feature: IPv6DualStack :cite:p:`k8s-feature-ipv6dualstack_ra2`
     -
     - IPv4/IPv6 dual-stack networking enables the allocation of both IPv4 and IPv6 addresses to Pods and Services.
       IPv4/IPv6 dual-stack networking is enabled by default for your Kubernetes cluster from 1.21 onwards, allowing
       the simultaneous assignment of IPv4 and IPv6 addresses.
   * - Feature:kubemci
     -
     - The kubemci feature should create ingress with a preshared certificate.
   * - Feature:KubeProxyDaemonSetMigration
     -
     - The upgrade of kube-proxy from static pods to a DaemonSet should maintain a functioning cluster.
   * - Feature:KubeProxyDaemonSetUpgrade
     -
     - The upgrade of kube-proxy from static pods to a DaemonSet should maintain a functioning cluster.
   * - Feature:NEG
     -
     - The NEG feature should sync the endpoints to NEG.
   * - Feature:NoSNAT
     - X
     - The NoSNAT feature should be able to send traffic between the Pods without SNAT.
   * - Feature:Networking-IPv4
     - X
     - Networking-IPv4 should provide an IPv4 connection for the containers.
   * - Feature:Networking-IPv6
     -
     - Networking-IPv6 should provide an IPv6 connection for the containers.
   * - Feature:Networking-Performance
     - X
     - Measure network responsiveness, latency (both RTT and OWD), and throughput with the iperf2 tool.
   * - Feature:NetworkPolicy
     -
     - NetworkPolicy between the server and the client should enforce a policy to allow traffic only from a different
       namespace, based on NamespaceSelector.
   * - Feature:PerformanceDNS
     -
     - The PerformanceNDS feature should answer DNS queries for a maximum number of services per cluster.
   * - Feature:SCTP
     -
     - SCTP should allow the creation of a basic SCTP service with the pod and the endpoints.
   * - Feature:SCTPConnectivity
     -
     - The Pods should function for intra-pod communication: sctp.

Node Special Interest Group :cite:p:`k8s-api-sig-node_ra2`
----------------------------------------------------------

.. list-table:: Node Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test.
   * - None
     - X
     - Kubernetes mainstream features.
   * - Feature:Example
     - X
     - The liveness pods should be automatically restarted.
   * - Feature: ExperimentalResourceUsageTracking
     -
     - Resource tracking for 100 pods per node.
   * - Feature:GPUUpgrade
     -
     - The Control Plane node upgrade should not disrupt the GPU Pod.
   * - Feature:PodGarbageCollector
     -
     - The PodGarbageCollector feature should handle the creation of 1000 pods.
   * - Feature:RegularResourceUsageTracking
     -
     - Resource tracking for 0 pods per node.
   * - Feature: ProbeTerminationGracePeriod :cite:p:`k8s-feature-probeterminationgraceperiod_ra2`
     - X
     - The probing container should override timeoutGracePeriodSeconds when the LivenessProbe field is set.
   * - NodeFeature: DownwardAPIHugePages :cite:p:`k8s-feature-downwardapihugepages_ra2`
     -
     - Downward API tests for huge pages should provide the container's limits.hugepages-pagesize, and
       requests.hugepages-pagesize as environmental variables.
   * - NodeFeature: PodReadinessGate :cite:p:`k8s-feature-podreadinessgate_ra2`
     - X
     - The Pods should support the pod readiness gates.
   * - NodeFeature:RuntimeHandler
     -
     - The RuntimeClass feature should run a Pod requesting a RuntimeClass with a configured handler.
   * - NodeFeature: Sysctls :cite:p:`k8s-feature-sysctls_ra2`
     - X
     - The Sysctls feature should not launch unsafe, but not explicitly enabled sysctls on the node.

Scheduling Special Interest Group :cite:p:`k8s-api-sig-scheduling_ra2`
----------------------------------------------------------------------

.. list-table:: Scheduling Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test.
   * - None
     - X
     - Kubernetes mainstream features.
   * - Feature:GPUDevicePlugin
     -
     - The GPUDevicePlugin feature runs Nvidia GPU Device Plugin tests.
   * - Feature: LocalStorageCapacityIsolation :cite:p:`k8s-feature-localstoragecapacityisolation_ra2`
     - X
     - The LocalStorageCapacityIsolation feature validates local ephemeral storage resource limits of pods
       that are allowed to run.
   * - Feature:Recreate
     -
     - The Recreate feature runs Nvidia GPU Device Plugin tests with a recreation.

Storage Special Interest Group :cite:p:`k8s-api-sig-storage_ra2`
----------------------------------------------------------------

.. list-table:: Storage Special Interest Group
   :widths: 30 10 60
   :header-rows: 1

   * - Labels
     - Mandatory
     - Description
   * - Conformance
     - X
     - Kubernetes conformance test.
   * - None
     - X
     - Kubernetes mainstream features.
   * - Feature:ExpandInUsePersistentVolumes
     -
     -
   * - Feature:Flexvolumes
     -
     -
   * - Feature:GKELocalSSD
     -
     -
   * - Feature:VolumeSnapshotDataSource
     -
     -
   * - Feature:Volumes
     - X
     -
   * - Feature:vsphere
     -
     -
   * - Feature:Windows
     -
     -
   * - NodeFeature:EphemeralStorage
     - X
     -
   * - NodeFeature:FSGroup
     - X
     -
