Interfaces and APIs
===================


This chapter presents a consolidated set of OpenStack Service APIs
corresponding to the ETSI NFV Nf-Vi, Vi-Vnfm and Or-Vi interfaces. The
OpenStack Wallaby version is used as the baseline for these APIs and
CLIs in this Reference Architecture (RA-1) version. Any Cloud
Infrastructure + VIM reference implementations that **get certified by
RC** (Reference Conformance) can be considered as Anuket RA Conformant.

The Chapter presents the APIs for the core OpenStack services defined in
Chapter 3 and a consolidated view of these and other APIs that are of
interest.

OpenStack is a multi-project framework composed of independently
evolving services. It is not enough to rely only on the OpenStack
release to characterise the capabilities supported by these services.
Regarding OpenStack services APIs, an "API version" is associated with
each OpenStack service. In addition to major API versions, some
OpenStack services (Nova, Glance, Keystone, Cinder…) support
microversions. The microversions allow new features to be introduced
over time. In this chapter, the **major version** and **microversion**
are specified per service. The specified microversion is the minimal
microversion that supports the features requested for this RA. For the
purpose of conformance tests, this chapter also identifies the set of
features, offered by a service, that are mandatory for Anuket compliant
implementation.

Core OpenStack Services APIs
----------------------------

Please note that OpenStack provides a maximum microversion to be used
with an OpenStack release. In the following sections the "Maximal API
Version" refers to this maximum microversion specified for the OpenStack
Wallaby release. Please note that in Reference Conformance (RC-1)
testing, the System Under Test (SUT) can utilise newer microversions
because of the OpenStack microversion policies. As per multiple
OpenStack services documentation, for example the Compute Service
:cite:p:`oscomputemicroversions`,
"A cloud that is upgraded to support newer microversions will still
support all older microversions to maintain the backward compatibility
for those users who depend on older microversions."

Keystone API
~~~~~~~~~~~~

.. table:: Keystone
   :widths: auto

   ===================== =============== ============================
   **OpenStack Service** **API Version** **Maximal API Microversion**
   ===================== =============== ============================
   Identity: Keystone    v3              3.14
   ===================== =============== ============================

.. table:: Keystone Features
   :widths: auto

   ======================= =============
   **Keystone Features**   **Mandatory**
   ======================= =============
   access_rules
   application_credentials X
   external_idp
   federation
   oauth1
   project_tags            X
   security_compliance     X
   trust                   X
   ======================= =============

Identity API v3: :cite:p:`osidentityapiv3`

Identity API v3 extensions: :cite:p:`osidentityapiv3ext`

Security compliance and PCI-DSS: :cite:p:`ossecuritycomplianceandpcidss`

Glance API
~~~~~~~~~~

.. table:: Glance
   :widths: auto

   ===================== =============== ============================
   **OpenStack Service** **API Version** **Maximal API Microversion**
   ===================== =============== ============================
   Image: Glance         v2              2.9
   ===================== =============== ============================

.. table:: Glance Features
   :widths: auto

   =================== =============
   **Glance Features** **Mandatory**
   =================== =============
   import_image
   os_glance_reserved
   web-download import
   =================== =============

Image Service API: :cite:p:`osimageserviceapi`

Image Service Versions: :cite:p:`osimageserviceversions`

Cinder API
~~~~~~~~~~

.. table:: Cinder
   :widths: auto

   ===================== =============== ============================
   **OpenStack Service** **API Version** **Maximal API Microversion**
   ===================== =============== ============================
   Block Storage: Cinder v3              3.64
   ===================== =============== ============================

.. table:: Cinder Features
   :widths: auto

   ================================ =============
   **Cinder Features**              **Mandatory**
   ================================ =============
   backup                           X
   clone                            X
   consistency_group
   extend_attached_volume
   extend_attached_encrypted_volume
   manage_snapshot                  X
   manage_volume                    X
   multi_backend
   snapshot                         X
   volume_revert                    X
   ================================ =============

Block Storage API: :cite:p:`osblockstorageapi`

Cinder REST API Version History: :cite:p:`oscinderrestapiversionhistory`

Swift API
~~~~~~~~~

.. table:: Swift
   :widths: auto

   ===================== ===============
   **OpenStack Service** **API Version**
   ===================== ===============
   Object Storage: Swift v1
   ===================== ===============

.. table:: Swift Features
   :widths: auto

   ================== =============
   **Swift Features** **Mandatory**
   ================== =============
   account_quotas     X
   bulk_delete        X
   bulk_upload        X
   container_quotas   X
   container_sync
   crossdomain        X
   discoverability    X
   form_post          X
   ratelimit          X
   s3api
   slo                X
   staticweb          X
   symlink            X
   temp_url           X
   tempauth           X
   versioned_writes   X
   ================== =============

Object Storage API: :cite:p:`osobjectstorageapi`

Discoverability: :cite:p:`osdiscoverability`

Neutron API
~~~~~~~~~~~

.. table:: Neutron
   :widths: auto

   ===================== ===============
   **OpenStack Service** **API Version**
   ===================== ===============
   Networking: Neutron   v2.0
   ===================== ===============

.. table:: Neutron Extensions
   :widths: auto

   ============================== =============
   **Neutron Extensions**         **Mandatory**
   ============================== =============
   address-scope                  X
   agent                          X
   allowed-address-pairs          X
   auto-allocated-topology        X
   availability_zone              X
   availability_zone_filter       X
   binding                        X
   binding-extended               X
   default-subnetpools            X
   dhcp_agent_scheduler
   dns-domain-ports
   dns-integration
   dvr
   empty-string-filtering         X
   ext-gw-mode                    X
   external-net                   X
   extra_dhcp_opt                 X
   extraroute                     X
   extraroute-atomic
   flavors                        X
   filter-validation
   fip-port-details
   floating-ip-port-forwarding
   floatingip-pools
   ip-substring-filtering         X
   l3_agent_scheduler
   l3-flavors
   l3-ha
   logging
   metering
   multi-provider                 X
   net-mtu                        X
   net-mtu-writable               X
   network_availability_zone      X
   network-ip-availability        X
   network-segment-range
   pagination                     X
   port-mac-address-regenerate
   port-resource-request
   port-security                  X
   port-security-groups-filtering X
   project-id                     X
   provider                       X
   rbac-policies                  X
   router                         X
   router_availability_zone       X
   qos                            X
   qos-bw-limit-direction         X
   qos-bw-minimum-ingress         X
   qos-default                    X
   qos-fip                        X
   qos-gateway-ip                 X
   qos-rule-type-details          X
   qos-rules-alias                X
   quotas                         X
   quota_details                  X
   revision-if-match              X
   rbac-address-scope
   rbac-security-groups
   rbac-subnetpool
   router-interface-fip
   security-group                 X
   service-type                   X
   sorting                        X
   standard-attr-description      X
   standard-attr-revisions        X
   standard-attr-tag              X
   standard-attr-timestamp        X
   subnet_allocation              X
   subnet-service-types           X
   subnetpool-prefix-ops
   tag-ext
   tag-ports-during-bulk-creation
   trunk                          X
   trunk-details                  X
   uplink-status-propagation
   ============================== =============

.. table:: Neutron Type Drivers
   :widths: auto

   ======================== =============
   **Neutron Type Drivers** **Mandatory**
   ======================== =============
   geneve
   gre
   vlan                     X
   vxlan
   ======================== =============

Networking Service APIs: :cite:p:`osnetworkingserviceapis`

The exhaustive list of extensions is available at
:cite:p:`osnetworkingapiv20`

Nova API
~~~~~~~~

.. table:: Nova
   :widths: auto

   ===================== =============== ============================
   **OpenStack Service** **API Version** **Maximal API Microversion**
   ===================== =============== ============================
   Compute: Nova         v2.1            2.88
   ===================== =============== ============================

.. table:: Nova Features
   :widths: auto

   ======================= =============
   **Nova Features**       **Mandatory**
   ======================= =============
   attach_encrypted_volume
   cert
   change_password
   cold_migration          X
   console_output          X
   disk_config             X
   instance_password       X
   interface_attach        X
   live_migration          X
   metadata_service        X
   pause                   X
   personality
   rdp_console
   rescue                  X
   resize                  X
   serial_console
   shelve                  X
   shelve_migrate
   snapshot                X
   stable_rescue
   spice_console
   suspend                 X
   swap_volume
   vnc_console
   volume_multiattach
   xenapi_apis
   ======================= =============

Compute API: :cite:p:`oscomputeapi`

Compute REST API Version History: :cite:p:`oscomputerestapiversionhistory`

Placement API
~~~~~~~~~~~~~

.. table:: Placement
   :widths: auto

   ===================== =============== ============================
   **OpenStack Service** **API Version** **Maximal API Microversion**
   ===================== =============== ============================
   Placement             v1              1.36
   ===================== =============== ============================

Placement API: :cite:p:`osplacementapi`

Placement REST API Version History: :cite:p:`osplacementrestapiversionhistory`

Heat API
~~~~~~~~

.. table:: Heat
   :widths: auto

   ===================== =============== ============================
   **OpenStack Service** **API Version** **Maximal Template Version**
   ===================== =============== ============================
   Orchestration: Heat   v1              2021-04-16
   ===================== =============== ============================

Orchestration Service API: :cite:p:`osorchestrationserviceapi`

Template version history: :cite:p:`ostemplateversionhistory`

Heat Orchestration Template (HOT) specification: :cite:p:`oshotspecification`


Consolidated Set of APIs
------------------------

OpenStack Interfaces
~~~~~~~~~~~~~~~~~~~~

This section illustrates some of the Interfaces provided by OpenStack;
the exhaustive list of APIs is available at
:cite:p:`osapis`.

OpenStack REST APIs are simple to interact with using either of two
options. Clients can either call the APIs directly using the HTTP or
REST library, or they can use one of the many cloud specific programming
language libraries.

**APIs**

.. list-table:: APIs
   :widths: 20 50 15 15
   :header-rows: 1

   * - OpenStack Service
     - Link for API list
     - API Version
     - Maximal API Microversion
   * - Identity: Keystone
     - :cite:p:`osidentityapiv3`
     - v3
     - 3.14
   * - Compute: Nova
     - :cite:p:`oscomputeapi`
     - v2.1
     - 2.88
   * - Networking: Neutron
     - :cite:p:`osnetworkingapiv20`
     - v2.0
     -
   * - Image: Glance
     - :cite:p:`osimageserviceapi`
     - v2
     - 2.9
   * - Block Storage: Cinder
     - :cite:p:`osblockstorageapi`
     - v3
     - 3.64
   * - Placement
     - :cite:p:`osplacementapi`
     - v1
     - 1.36
   * - Orchestration: Heat
     - :cite:p:`osorchestrationserviceapi`
     - v1
     - 2021-04-06 (template)

Kubernetes Interfaces
~~~~~~~~~~~~~~~~~~~~~

The Kubernetes APIs are available at
:cite:p:`kubernetesapis`.

KVM Interfaces
~~~~~~~~~~~~~~

The KVM APIs are documented in Section 4 of the document
:cite:p:`kvmapis`.

Libvirt Interfaces
~~~~~~~~~~~~~~~~~~

The Libvirt APIs are documented in :cite:p:`libvirtapis`.

Barbican API
~~~~~~~~~~~~

.. table:: Barbican
   :widths: auto

   ===================== ===============
   **OpenStack Service** **API Version**
   ===================== ===============
   Key Manager: Barbican v1
   ===================== ===============

Barbican API: :cite:p:`osbarbicanapi`
