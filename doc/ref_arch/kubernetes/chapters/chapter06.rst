API and Feature Testing requirements
====================================

Introduction to API and Feature Testing requirement
---------------------------------------------------

The CNCF has defined a :cite:t:`k8s-testing-sig` to help the community to write and run tests, and to contribute,
analyse and act upon test results. This chapter maps the requirements written in the previous chapters as mandatory
Special Interest Group Features. It enforces the overall requirements traceability to testing, especially those offered
for :cite:t:`k8s-testing-sig-e2e-tests`.
The Anuket Reference Conformance (RC2) testing matches the Features and tests defined here.

Kubernetes feature gate policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cite:t:`k8s-feature-gates` are a set of key-value pairs that describe Kubernetes features. The components of the
control plane of Kubernetes Clusters can be run with different Feature Gate settings.

A feature can be in Alpha, Beta or General Availability (GA) stage:

- Alpha features are disabled by default, breaking API changes may be expected, may be buggy, and support may be dropped
- Beta features are disabled by default, are well tested, and support will not be dropped (although breaking API
  changes may happen). Any existing Beta feature as of 1.24 will continue to be enabled by default, but new beta APIs
  and features will not be enabled by default after Kubernetes 1.24.
  More in :cite:t:`k8s-kep-3136`
- GA features are stable, always enabled and cannot be disabled.

Only those Kubernetes features can be made mandatory in this Reference Architecture which are GA or were Beta before
Kubernetes 1.24.

A list of feature gates is available here :cite:p:`k8s-feature-gates`.

Kubernetes API policy
~~~~~~~~~~~~~~~~~~~~~

The :cite:t:`k8s-api` supports all operations and communications between components, and external user commands.
Everything in the Kubernetes platform is treated as an API object. Different API versions indicate different levels of
stability and support. An API can have Alpha, Beta or Stable versions. The version of APIs that are backed by a feature
will match the stage of the feature itself (i.e. Alpha, Beta or GA or Stable).

The policy for RA2 to include Kubernetes APIs as mandatory is:

In this Reference Architecture APIsonly those API can be mandatory which are in any of the following stages:

- Stable
- Beta when introduced before Kubernetes version 1.24
- Alpha or Beta when required by RA2 Ch4 Specifications or when included below on list of Mandatory API Groups.

The Kubernetes API reference is available here :cite:p:`k8s-api-reference`.

The list of :cite:t:`k8s-v1.26-api-groups` that are mandatory is:

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

API Machinery Special Interest Group :cite:p:`k8s-api-sig-api-machinery`
------------------------------------------------------------------------

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
     - Namespaces should always delete fast (ALL of 100 namespaces in 150 seconds)
   * - Feature: CrossNamespacePodAffinity :cite:p:`k8s-feature-crossnamespacepodaffinity`
     -
     - Should verify ResourceQuota with cross namespace pod affinity scope using scope-selectors
   * - Feature: PodPriority :cite:p:`k8s-feature-crossnamespacepodaffinity`
     - X
     - Verify ResourceQuota's priority class scope against a pod with different priority class
   * - Feature:ScopeSelectors
     - X
     - Verify ResourceQuota with terminating scopes through scope selectors
   * - Feature: StorageVersionAPI :cite:p:`k8s-feature-storageversionapi`
     -
     -

Apps Special Interest Group :cite:p:`k8s-api-sig-apps`
------------------------------------------------------

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
   * - Feature: DaemonSetUpdateSurge :cite:p:`k8s-feature-daemonsetupdatesurge`
     -
     - Daemon set should surge pods onto nodes when spec was updated and update strategy is RollingUpdate
   * - Feature: IndexedJob :cite:p:`k8s-feature-indexedjob`
     -
     - Should create pods for an Indexed job with completion indexes
   * - Feature: StatefulSet :cite:p:`k8s-feature-statefulset`
     -
     - Should creating a working zookeeper cluster
   * - Feature:StatefulUpgrade
     -
     - Stateful upgrade should maintain a functioning cluster
   * - Feature: SuspendJob :cite:p:`k8s-feature-suspendjob`
     -
     - Should not create pods when created in suspend state
   * - Feature: TaintEviction :cite:p:`k8s-feature-tainteviction`
     -
     - All pods on the unreachable node should be marked as NotReady upon the node turn NotReady AND all pods should be
       evicted after eviction timeout passes
   * - Feature: TTLAfterFinished :cite:p:`k8s-feature-ttlafterfinished`
     - X
     - Job should be deleted once it finishes after TTL seconds

Auth Special Interest Group :cite:p:`k8s-api-sig-auth`
------------------------------------------------------

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
   * - Feature: BoundServiceAccountTokenVolume :cite:p:`k8s-feature-boundserviceaccounttokenvolume`
     -
     - ServiceAccount admission controller migration upgrade should maintain a functioning cluster
   * - Feature:NodeAuthenticator
     - X
     - The kubelet's main port 10250 should reject requests with no credentials
   * - Feature:NodeAuthorizer
     - X
     - Setting existing and non-existent attributes should exit with the Forbidden error, not a NotFound error
   * - NodeFeature:FSGroup
     - X
     - ServiceAccounts should set ownership and permission when RunAsUser or FsGroup is present

Cluster Lifecycle Special Interest Group :cite:p:`k8s-api-sig-cluster-lifecycle`
--------------------------------------------------------------------------------

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
     - Should delete the token secret when the secret expired


Instrumentation Special Interest Group :cite:p:`k8s-api-sig-instrumentation`
----------------------------------------------------------------------------

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
     - Should check that the Kibana logging instance is alive
   * - Feature: StackdriverAcceleratorMonitoring
     -
     - Stackdriver Monitoring should have accelerator metrics
   * - Feature:StackdriverCustomMetrics
     -
     - Stackdriver Monitoring should run Custom Metrics - Stackdriver Adapter for new resource model
   * - Feature:StackdriverExternalMetrics
     -
     - Stackdriver Monitoring should run Custom Metrics - Stackdriver Adapter for external metrics
   * - Feature:StackdriverMetadataAgent
     -
     - Stackdriver Monitoring should run Stackdriver Metadata Agent
   * - Feature:StackdriverMonitoring
     -
     -

Network Special Interest Group :cite:p:`k8s-api-sig-network`
------------------------------------------------------------

.. list-table:: Network Special Interest Group
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
   * - Feature:Example
     -
     - Should create pod that uses DNS
   * - Feature:Ingress
     -
     - Should prevent Ingress creation if more than 1 IngressClass marked as default
   * - Feature: IPv6DualStack :cite:p:`k8s-feature-ipv6dualstack`
     -
     - IPv4/IPv6 dual-stack networking enables the allocation of both IPv4 and IPv6 addresses to Pods and Services.
       IPv4/IPv6 dual-stack networking is enabled by default for your Kubernetes cluster starting in 1.21, allowing the
       simultaneous assignment of both IPv4 and IPv6 addresses.
   * - Feature:kubemci
     -
     - Should create ingress with pre-shared certificate
   * - Feature:KubeProxyDaemonSetMigration
     -
     - Upgrade kube-proxy from static pods to a DaemonSet should maintain a functioning cluster
   * - Feature:KubeProxyDaemonSetUpgrade
     -
     - Upgrade kube-proxy from static pods to a DaemonSet should maintain a functioning cluster
   * - Feature:NEG
     -
     - Should sync endpoints to NEG
   * - Feature:NoSNAT
     - X
     - Should be able to send traffic between Pods without SNAT
   * - Feature:Networking-IPv4
     - X
     - Networking should provide Internet connection for containers
   * - Feature:Networking-IPv6
     -
     - Networking should provide Internet connection for containers
   * - Feature:Networking-Performance
     - X
     - run iperf2
   * - Feature:NetworkPolicy
     -
     - NetworkPolicy between server and client should enforce policy to allow traffic only from a different namespace,
       based on NamespaceSelector
   * - Feature:PerformanceDNS
     -
     - Should answer DNS query for maximum number of services per cluster
   * - Feature:SCTP
     -
     - should allow creating a basic SCTP service with pod and endpoints
   * - Feature:SCTPConnectivity
     -
     - Pods should function for intra-pod communication: sctp

Node Special Interest Group :cite:p:`k8s-api-sig-node`
------------------------------------------------------

.. list-table:: Node Special Interest Group
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
   * - Feature:Example
     - X
     - Liveness pods should be automatically restarted
   * - Feature: ExperimentalResourceUsageTracking
     -
     - Resource tracking for 100 pods per node
   * - Feature:GPUUpgrade
     -
     - Control Plane node upgrade should NOT disrupt GPU Pod
   * - Feature:PodGarbageCollector
     -
     - Should handle the creation of 1000 pods
   * - Feature:RegularResourceUsageTracking
     -
     - Resource tracking for 0 pods per node
   * - Feature: ProbeTerminationGracePeriod :cite:p:`k8s-feature-probeterminationgraceperiod`
     - X
     - Probing container should override timeoutGracePeriodSeconds when LivenessProbe field is set
   * - NodeFeature: DownwardAPIHugePages :cite:p:`k8s-feature-downwardapihugepages`
     -
     - Downward API tests for huge pages should provide container's limits.hugepages-pagesize; and requests.hugepages-pa
       gesize& as env vars
   * - NodeFeature: PodReadinessGate :cite:p:`k8s-feature-podreadinessgate`
     - X
     - Pods should support pod readiness gates
   * - NodeFeature:RuntimeHandler
     -
     - RuntimeClass should run a Pod requesting a RuntimeClass with a configured handler
   * - NodeFeature: Sysctls :cite:p:`k8s-feature-sysctls`
     - X
     - Should not launch unsafe, but not explicitly enabled sysctls on the node

Scheduling Special Interest Group :cite:p:`k8s-api-sig-scheduling`
------------------------------------------------------------------

.. list-table:: Scheduling Special Interest Group
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
   * - Feature:GPUDevicePlugin
     -
     - Run Nvidia GPU Device Plugin tests
   * - Feature: LocalStorageCapacityIsolation :cite:p:`k8s-feature-localstoragecapacityisolation`
     - X
     - Validates local ephemeral storage resource limits of pods that are allowed to run
   * - Feature:Recreate
     -
     - Run Nvidia GPU Device Plugin tests with a recreation

Storage Special Interest Group :cite:p:`k8s-api-sig-storage`
------------------------------------------------------------

.. list-table:: Storage Special Interest Group
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
