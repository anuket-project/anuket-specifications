Conformance
===========

The objective of this chapter is to provide an automated mechanism
to validate OpenStack based cloud infrastructure
against the standard set of requirements defined in
:ref:`chapters/chapter02:Architecture Requirements`. Through this validation
mechanism, a provider of cloud infrastructure will be able
to test their conformance to this reference architecture. This will ease the
integration of network functions into operator environments that host
compatible cloud infrastructures, thereby reducing cost, complexity, and time
of integration.

The overall workstream requires the close coordination of the following:

-  **Requirements** - The agreed upon capabilities and conditions that a
   compliant cloud infrastructure must provide or satisfy.
-  **Tests** - The verification mechanism that determines that a given
   cloud infrastructure complies with one or more requirements.
-  **Conformance Specifications** - The definition of the requirements,
   tests, and circumstances (test case integration, etc.) that must be
   met to be deemed conformant.

Requirements and Testing Principles
-----------------------------------

If there is no clear traceability and strong links between **Requirements**,
**Tests** and **Conformance Specifications**, then it becomes difficult to
determine if a cloud infrastructure is compliant. With this in mind, below are
the set of recommended principles for each of the three components to follow.
Adherence to these principles will provide the following:

-  Enable clear progress tracking and linkage between independent
   projects (i.e. know what has and hasn’t been covered, and track
   changes over time)
-  Help users better understand if they meet requirements
-  Provide a stable set of point-in-time requirements and tests to
   achieve conformance
-  Reduce ambiguity in testing, requirements, and conformance

Testing Principles:

- There must be traceability between test cases and requirement being
  validated
- Failures should provide additional content to inform the user where
  or how the requirement was violated (e.g. which file or resource
  violated the requirement). Put another way, don't require the user to
  read the test to understand what went wrong
- Testing tools should support selection of tests based on category or
  profile.
- Tests must be available to run locally by both VNF and cloud
  infrastructure providers
- Testing tools must produce machine-readable result formats that can
  be used as input into any badging program

Conformance Specifications:

-  Conformance specifications must refer to or define the *versioned*
   requirements that must be satisfied
-  Conformance specifications must refer to the *versioned* test
   implementations that must be used to validate the requirements
-  Conformance specifications must define the expected preconditions and
   environment requirements for any test tooling
-  Conformance specifications must define which tests must be executed
   in the given testing tools to achieve conformance
-  The conformance specifications must provide the mapping between tests
   and requirements to demonstrate traceability and coverage.

Test Case Integration and Tooling
---------------------------------

The OpenStack based cloud infrastructure suite must utilize the Anuket test
case integration toolchain to deliver overall integration, the same end user
actions, and a unique test result format (e.g. Anuket test result
database) needed by the end users and any test case result verification
program (e.g. `OVP <https://www.opnfv.org/verification>`__).

Anuket Toolchains
~~~~~~~~~~~~~~~~~

Anuket, previously named OPNFV, has built a complete CI/CD toolchain for
continuously deploying and testing cloud infrastructure.

As for all installer projects,
`Jenkins <https://build.opnfv.org/>`__ triggers scenario
deployments, runs the Anuket gating test cases and then publishes all
test results in the `centralized test
database <https://docs.opnfv.org/en/stable-hunter/_images/OPNFV_testing_working_group.png>`__
and all artifacts (reports, logs, etc.) to `an S3 compatible storage
service <http://artifacts.opnfv.org/>`__.

The verification, validation, and conformance processes leverage
existing Anuket testing knowledge (projects) and experience (history) by
utilising the toolchain design already in-place. The conformance
toolchain only requires for the local deployment of the components instead of
leveraging the common Anuket centralized services. However, the
interfaces remain unchanged for leveraging test jobs, the common test
case execution, the test result database and the S3 protocol to publish
the artifacts. It’s worth mentioning that dumping all results and logs
required for conformance is already in place in Functest daily jobs (see
`functest-wallaby-zip <https://build.opnfv.org/ci/job/functest-wallaby-zip/4/console>`__).

It should be noted that `Xtesting
CI <https://galaxy.ansible.com/collivier/xtesting>`__ supports both
centralized and distributed deployment models as described before. It
has deployed the full toolchain in one small virtual machine to verify
ONAP Openlab via Functest.

Test Case Integration
~~~~~~~~~~~~~~~~~~~~~

To reach all goals in terms of verification, validation, compliance, and
conformance, all test cases must be delivered as `Docker
containers <https://www.docker.com/>`__ to simplify the CI toolchain
setup including:

-  the common test case execution
-  the unified way to manage all the interactions with the CI/CD
   components and with third-parties (e.g. dump all test case logs and
   results for conformance)

For their part, the Docker containers simply enforce that the test cases
are delivered with all runtime dependencies. This prevents lots of
manual operations when configuring the servers running the test cases
and prevents conflicts between the test cases due to any dependencies.

It’s worth mentioning that all the conformance test cases
already leverage `Xtesting <https://xtesting.readthedocs.io/en/latest/>`__
which is a simple framework to assemble sparse test cases and to accelerate the
adoption of CI/CD best practices. By managing all the interactions with
the CI/CD components (test scheduler, test results database, artifact
repository), it allows the developer to work only on the test suites
without diving into CI/CD integration. Even more, it brings the
capability to run heterogeneous test cases in the same CI toolchains
thanks to a few, `quickly
achievable <https://www.sdxcentral.com/articles/news/opnfvs-6th-release-brings-testing-capabilities-that-orange-is-already-using/2018/05/>`__,
constraints.

The Docker containers proposed by the test projects must also embed `the
Xtesting Python package <https://pypi.org/project/xtesting/>`__ and `the
related test case execution description
files <https://git.opnfv.org/functest-xtesting/tree/docker/core/testcases.yaml>`__
as required by Xtesting.

Testing Cookbooks
~~~~~~~~~~~~~~~~~

`Xtesting CI <https://galaxy.ansible.com/collivier/xtesting>`__
leverages the common test case execution proposed by Xtesting. Thanks to
a simple test case list, this tool deploys plug-and-play `CI/CD
toolchains in a few
commands <https://github.com/collivier/ansible-role-xtesting#readme>`__.
In addition, it supports multiple components such as Jenkins and Gitlab
CI (test schedulers) and `multiple deployment
models <https://lists.opnfv.org/g/opnfv-tsc/message/5702>`__ such as
all-in-one or centralized services.

`Xtesting <https://xtesting.readthedocs.io/en/latest/>`__ and `Xtesting
CI <https://galaxy.ansible.com/collivier/xtesting>`__ combined meet the
requirements about verification, validation, compliance, and
conformance:

-  smoothly assemble multiple heterogeneous test cases
-  generate the Jenkins jobs in `Anuket
   Releng <https://git.opnfv.org/releng/tree/jjb/functest>`__
   to verify Anuket RC1 and RC2
-  deploy local CI/CD toolchains everywhere to check compliance with
   Anuket
-  `dump all test case results and
   logs <http://artifacts.opnfv.org/functest/9ID39XK47PMZ.zip>`__ for
   third-party conformance review

Here are a couple of publicly available playbooks :

-  `Xtesting
   samples <https://git.opnfv.org/functest-xtesting/plain/ansible/site.yml?h=stable/wallaby>`__
-  `OpenStack
   verification <https://git.opnfv.org/functest/plain/ansible/site.yml?h=stable/wallaby>`__
-  `Anuket
   RC1 <https://git.opnfv.org/functest/plain/ansible/site.cntt.yml?h=stable/wallaby>`__
-  `Kubernetes
   verification <https://git.opnfv.org/functest-kubernetes/plain/ansible/site.yml?h=stable/v1.22>`__

Conformance Test Suite
----------------------

Functest in a nutshell
~~~~~~~~~~~~~~~~~~~~~~

`Functest <https://functest.readthedocs.io/en/stable-xena/>`__ was
initially created to verify OPNFV Installers and Scenarios and then to
publish fair, trustable and public results regarding the status of the
different opensource technologies, especially for Neutron backends
(e.g., Neutron agents, OpenDaylight, OVN, etc.). It has been continuously
updated to offer the best testing coverage for any kind of OpenStack and
Kubernetes deployments including production environments. It also
ensures that the platforms meet Network Functions Virtualization
requirements by running and testing VNFs amongst all tests available.

Functest is driven by a true verification of the platform under test as
opposed to the interoperability programs such as
`RefStack <https://refstack.openstack.org/>`__ or `OPNFV Verification
Program <https://www.opnfv.org/verification>`__ which select a small
subset of Functional tests passing in many different opensource software
combinations:

-  tests are skipped if an optional support is missing (e.g.
   `Barbican <https://docs.openstack.org/barbican/latest/>`__ or
   networking features such as `BGPVPN
   interconnection <https://docs.openstack.org/networking-bgpvpn/latest/>`__
   or `Service Function
   Chaining <https://docs.openstack.org/networking-sfc/latest/>`__)
-  tests are parameterized (e.g. shared vs non-shared live migration)
-  blacklist mechanisms are available if needed

It should be noted that `the RefStack
lists <https://refstack.openstack.org/>`__ are included as
they are in Functest in the next 3 dedicated testcases:

-  refstack_compute (OpenStack Powered Compute)
-  refstack_object (OpenStack Powered Object Storage)
-  refstack_platform (OpenStack Powered Platform)

Functest also integrates `Kubernetes End-to-end
tests <https://kubernetes.io/blog/2019/03/22/kubernetes-end-to-end-testing-for-everyone/>`__
and allows verifying Kubernetes Conformance (see
`k8s-conformance <https://build.opnfv.org/ci/job/functest-kubernetes-opnfv-functest-kubernetes-smoke-v1.22-k8s_conformance-run/25/console>`__).

Then Functest conforms with the upstream rules (versions, code quality,
etc.) and especially their
`gates <https://docs.opendev.org/opendev/system-config/latest/devstack-gate.html>`__
(a.k.a. the automatic verification prior to any code review) to preserve
the quality between code and deployment. In that case, Functest can be
considered as a smooth and lightweight integration of tests developed
upstream (and the Functest team directly contributes in these projects:
`Rally <https://github.com/openstack/rally-openstack>`__,
`Tempest <https://github.com/openstack/tempest>`__, etc.). It’s worth
mentioning that, as opposed to the OpenStack Gates leveraging on
`DevStack <https://docs.openstack.org/devstack/latest/>`__, it can check
the same already deployed SUT over and over even from a `Raspberry
PI <https://www.raspberrypi.org/>`__. Here the testcases can be executed
in parallel vs the same deployment instead of being executed vs
different pools of virtual machines.

Here are the functional tests (>2000) running in OpenStack gates
integrated in Functest Smoke (see `Functest daily
jobs <https://build.opnfv.org/ci/view/functest/job/functest-wallaby-daily/17/>`__
for more details):

.. table:: Functional tests
   :widths: auto

   ================= ==================
   Testcases         Gates
   ================= ==================
   tempest_neutron   Neutron
   tempest_cinder    Cinder
   tempest_keystone  Keystone
   rally_sanity      General
   refstack_defcore  General
   tempest_full      General
   tempest_slow      General
   tempest_scenario  General
   patrole           Patrole
   tempest_barbican  Barbican
   networking-bgpvpn Networking BGP VPN
   networking-sfc    Networking SFC
   ================= ==================

To complete functional testing, Functest also integrates a few
`performance
tools <https://docs.openstack.org/developer/performance-docs/methodologies/tools.html>`__
(2-3 hours) as proposed by OpenStack:

.. table:: Performance tools
   :widths: auto

   ========== ===========================
   Testcases  Benchmarking
   ========== ===========================
   rally_full Control Plane (API) testing
   rally_jobs Control Plane (API) testing
   vmtp       Data Plane testing
   shaker     Data Plane testing
   ========== ===========================

And VNFs automatically deployed and tested :

.. table:: VNFs
   :widths: auto

   ============ ===================================
   Testcases    Benchmarking
   ============ ===================================
   cloudify     Cloudify deployment
   cloudify_ims Clearwater IMS deployed via Coudify
   heat_ims     Clearwater IMS deployed via Heat
   vyos_vrouter VyOS deployed via Cloudify
   juju_epc     OAI deployed via Juju
   ============ ===================================

Functest should be considered as a whole as it meets multiple objectives
about the reference implementation:

-  verify all APIs (services, advances, features, etc.) exposed by the
   reference implementation
-  compare the reference implementation and local deployments from a
   functional standpoint and from OpenStack control plane and dataplane
   capabilities

Additional links:

-  `Homepage <https://functest.readthedocs.io/en/stable-iruya/>`__
-  `Run Alpine Functest containers
   (Wallaby) <https://wiki.anuket.io/display/HOME/Functest+Wallaby>`__
-  `Deploy your own Functest CI/CD
   toolchains <https://github.com/collivier/ansible-role-xtesting#readme>`__
-  `Functest gates <https://build.opnfv.org/ci/view/functest/>`__

Test Case traceability
~~~~~~~~~~~~~~~~~~~~~~

Interfaces & APIs
^^^^^^^^^^^^^^^^^

The `OpenStack Gates <https://opendev.org/openstack/devstack-gate>`__
verify all changes proposed mostly by running thousands of Tempest tests
completed by Rally scenarios in a few cases. Skipping tests is allowed
in all OpenStack Gates and only failures rate the review -1 because of
the multiple capabilities and backends selected in the different Gate
jobs. The classical `Functest
containers <https://wiki.anuket.io/display/HOME/Functest+Wallaby>`__
conform to this model which also fits the heterogeneous user
deployments.

From an OpenStack based cloud infrastructure conformance state point,
the capabilities are well described in
:ref:`chapters/chapter05:interfaces and apis` which allows tuning the test
configurations and the test lists to avoid
skipping any test. It results that all tests covering optional
capabilities and all upstream skipped tests due to known bugs are not
executed. All remaining tests must be executed and must pass
successfully.

New `Functest
containers <https://lists.opnfv.org/g/opnfv-tsc/message/5717>`__ have
been proposed for Anuket Compliance which simply override the default
test configurations and the default test lists. Any optional capability
or services (e.g. Barbican) can be still verified by the classical
Functest containers.

The next subsections detail the Tempest tests which must not be
executed from a compliance state point. The remaining tests have to pass
successfully. They cover all together the API testing requirements as
asked by :ref:`chapters/chapter05:interfaces and apis`

The following software versions are considered here to verify OpenStack
Wallaby selected by Anuket:

.. list-table:: Software versions
   :widths: 60 40
   :header-rows: 1

   * - Software
     - Version
   * - Functest
     - wallaby
   * - Cinder Tempest plugin
     - 1.4.0
   * - Keystone Tempest plugin
     - 0.7.0
   * - Heat Tempest plugin
     - 1.2.0
   * - Neutron Tempest plugin
     - 1.4.0
   * - Rally OpenStack
     - 2.2.1.dev11
   * - Tempest
     - 27.0.0

Identity - Keystone API testing
'''''''''''''''''''''''''''''''

Keystone API is covered in the OpenStack Gates via
`Tempest <https://opendev.org/openstack/tempest>`__ and
`keystone-tempest-plugin <https://opendev.org/openstack/keystone-tempest-plugin>`__
as integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__.

According to :ref:`chapters/chapter05:interfaces and apis`
the following test names must not be executed:

.. list-table:: Keystone API testing
   :widths: 60 40
   :header-rows: 1

   * - Test rejection regular expressions
     - Reasons
   * - .*api.identity.v3.test_oauth1_tokens
     - oauth1
   * - .*scenario.test_federated_authentication
     - federation
   * - .*identity.admin.v2
     - API v2
   * - .*identity.v2
     - API v2
   * - .*identity.v3.test_access_rules
     - access_rules
   * - .*identity.v3.test_application_credentials.\\

       ApplicationCredentialsV3Test.\\

       test_create_application_credential_access_rules
     - access_rules

Keystone API is also covered by
`Rally <https://opendev.org/openstack/rally>`__.

Here are the mainline tasks integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__:

-  Authenticate.keystone
-  KeystoneBasic.add_and_remove_user_role
-  KeystoneBasic.create_add_and_list_user_roles
-  KeystoneBasic.create_and_list_tenants
-  KeystoneBasic.create_and_delete_role
-  KeystoneBasic.create_and_delete_service
-  KeystoneBasic.get_entities
-  KeystoneBasic.create_update_and_delete_tenant
-  KeystoneBasic.create_user
-  KeystoneBasic.create_tenant
-  KeystoneBasic.create_and_list_users
-  KeystoneBasic.create_tenant_with_users

Image - Glance API testing
''''''''''''''''''''''''''

Glance API is covered in the OpenStack Gates via
`Tempest <https://opendev.org/openstack/tempest>`__ as integrated in
`Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml>`__.

According to :ref:`chapters/chapter05:interfaces and apis`
the following test names must not be executed:

.. list-table:: Glance API testing
   :widths: 60 40
   :header-rows: 1

   * - Test rejection regular expressions
     - Reasons
   * - .*image.v1
     - API v1
   * - .*image.v2.admin.test_images.ImportCopyImagesTest
     - import_image
   * - .*image.v2.test_images_negative.ImagesNegativeTest.\\

       test_create_image_reserved_property
     - os_glance_reserved
   * - .*image.v2.test_images_negative.ImagesNegativeTest.\\

       test_update_image_reserved_property
     - os_glance_reserved
   * - .*image.v2.test_images_negative.ImportImagesNegativeTest.\\

       test_image_web_download_import_with_bad_url
     - web-downloadimport
   * - .*image.v2.test_images.ImportImagesTest
     - import_image
   * - .*image.v2.test_images.MultiStoresImportImages
     - import_image

Glance API is also covered by
`Rally <https://opendev.org/openstack/rally>`__.

Here are the mainline tasks integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__:

-  Authenticate.validate_glance
-  GlanceImages.create_and_delete_image
-  GlanceImages.create_and_list_image
-  GlanceImages.list_images
-  GlanceImages.create_image_and_boot_instances

Block Storage - Cinder API testing
''''''''''''''''''''''''''''''''''

Cinder API is covered in the OpenStack Gates via
`Tempest <https://opendev.org/openstack/tempest>`__ and
`cinder-tempest-plugin <https://opendev.org/openstack/cinder-tempest-plugin>`__
as integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__.

According to :ref:`chapters/chapter05:interfaces and apis`
the following test names must not be executed:

.. list-table:: Cinder API testing
   :widths: 60 40
   :header-rows: 1

   * - Test rejection regular expressions
     - Reasons
   * - .*test_incremental_backup
     - https://gerrit.opnfv.org/gerrit/68881
   * - .*test_consistencygroups
     - consistency_group
   * - .*test_backup_crossproject_admin_negative
     - https://gerrit.opnfv.org/gerrit/71011
   * - .*test_backup_crossproject_user_negative
     - https://gerrit.opnfv.org/gerrit/71011
   * - .*test_volume_encrypted.TestEncryptedCinderVolumes
     - attach_encrypted_volume
   * - .*test_encrypted_volumes_extend
     - extend_attached_encrypted_volume
   * - .*test_group_snapshots.GroupSnapshotsV319Test.\\

       test_reset_group_snapshot_status
     - https://launchpad.net/bugs/1770179
   * - .*test_multi_backend
     - multi-backend
   * - .*test_volume_retype.VolumeRetypeWithMigrationTest
     - multi-backend
   * - .*test_volume_delete_cascade.VolumesDeleteCascade.\\

       test_volume_from_snapshot_cascade_delete
     - https://launchpad.net/bugs/1677525
   * - .*test_volumes_backup.VolumesBackupsTest.\\

       test_volume_backup_create_get_detailed_list_restore_delete
     - ceph
   * - .*test_volumes_extend.VolumesExtendAttachedTest.\\

       test_extend_attached_volume
     - extend_attached_volume
   * - .*tempest.scenario.test_volume_migrate_attached
     - multi-backend

Cinder API is also covered by
`Rally <https://opendev.org/openstack/rally>`__.

Here are the mainline tasks integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__:

-  Authenticate.validate_cinder
-  CinderVolumes.create_and_delete_snapshot
-  CinderVolumes.create_and_delete_volume
-  CinderVolumes.create_and_extend_volume
-  CinderVolumes.create_from_volume_and_delete_volume
-  CinderQos.create_and_list_qos
-  CinderQos.create_and_set_qos
-  CinderVolumeTypes.create_and_list_volume_types
-  CinderVolumeTypes.create_volume_type_and_encryption_type
-  Quotas.cinder_update_and_delete
-  Quotas.cinder_update

Object Storage - Swift API testing
''''''''''''''''''''''''''''''''''

Swift API is covered in the OpenStack Gates via
`Tempest <https://opendev.org/openstack/tempest>`__ as integrated in
`Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__.

According to :ref:`chapters/chapter05:interfaces and apis`
the following test names must not be executed:

.. list-table:: Swift API testing
   :widths: 60 40
   :header-rows: 1

   * - Test rejection regular expressions
     - Reasons
   * - .*test_container_sync.ContainerSyncTest.\\

       test_container_synchronization
     - https://launchpad.net/bugs/1317133
   * - .*test_container_sync_middleware.ContainerSyncMiddlewareTest.\\

       test_container_synchronization
     - container_sync
   * - .*test_object_services.ObjectTest.\\

       test_create_object_with_transfer_encoding
     - https://launchpad.net/bugs/1905432

Swift API is also covered by
`Rally <https://opendev.org/openstack/rally>`__.

Here are the mainline tasks integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__:

-  SwiftObjects.create_container_and_object_then_list_objects
-  SwiftObjects.list_objects_in_containers
-  SwiftObjects.create_container_and_object_then_download_object
-  SwiftObjects.create_container_and_object_then_delete_all
-  SwiftObjects.list_and_download_objects_in_containers

Networking - Neutron API testing
''''''''''''''''''''''''''''''''

Neutron API is covered in the OpenStack Gates via
`Tempest <https://opendev.org/openstack/tempest>`__ and
`neutron-tempest-plugin <https://opendev.org/openstack/neutron-tempest-plugin>`__
as integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__.

According to :ref:`chapters/chapter05:interfaces and apis`
the following test names must not be executed:

.. list-table:: Neutron API testing
   :widths: 60 40
   :header-rows: 1

   * - Test rejection regular expressions
     - Reasons
   * - .*admin.test_agent_availability_zone
     - DHCP agent and L3 agent
   * - .*admin.test_dhcp_agent_scheduler
     - dhcp_agent_scheduler
   * - .*admin.test_l3_agent_scheduler
     - l3_agent_scheduler
   * - .*admin.test_logging
     - logging
   * - .*admin.test_logging_negative
     - logging
   * - .*admin.test_network_segment_range
     - network-segment-range
   * - .*admin.test_ports.PortTestCasesAdmin.\\

       test_regenerate_mac_address
     - port-mac-address-regenerate
   * - .*admin.test_ports.PortTestCasesResourceRequest
     - port-resource-request
   * - .*admin.test_routers_dvr
     - dvr
   * - .*admin.test_routers_flavors
     - l3-flavors
   * - .*admin.test_routers_ha
     - l3-ha
   * - .*test_floating_ips.FloatingIPPoolTestJSON
     - floatingip-pools
   * - .*test_floating_ips.FloatingIPTestJSON.\\

       test_create_update_floatingip_port_details
     - fip-port-details
   * - .*test_metering_extensions
     - metering
   * - .*test_metering_negative
     - metering
   * - .*test_networks.NetworksSearchCriteriaTest.\\

       test_list_validation_filters
     - filter-validation
   * - .*test_networks.NetworksTestAdmin.\\

       test_create_tenant_network_vxlan
     - vxlan
   * - .*test_networks.NetworksTestJSON.\\

       test_create_update_network_dns_domain
     - dns-integration
   * - .*test_port_forwardings
     - floating-ip-port-forwarding
   * - .*test_port_forwarding_negative
     - floating-ip-port-forwarding
   * - .*test_ports.PortsTaggingOnCreation
     - tag-ports-during-bulk-creation
   * - .*test_ports.PortsTestJSON.\\

       test_create_port_with_propagate_uplink_status
     - uplink-status-propagation
   * - .*test_ports.PortsTestJSON.\\

       test_create_port_without_propagate_uplink_status
     - uplink-status-propagation
   * - .*test_ports.PortsTestJSON.\\

       test_create_update_port_with_dns_domain
     - dns-domain-ports
   * - .*test_ports.PortsTestJSON.\\

       test_create_update_port_with_dns_name
     - dns-integration
   * - .*test_ports.PortsTestJSON.\\

       test_create_update_port_with_no_dns_name
     - dns-integration
   * - .*test_revisions.TestRevisions.\\

       test_update_dns_domain_bumps_revision
     - dns-integration
   * - .*test_revisions.TestRevisions.\\

       test_update_router_extra_attributes\_\\

       bumps_revision
     - l3-ha
   * - .*test_router_interface_fip
     - router-interface-fip
   * - .*test_routers.DvrRoutersTest
     - dvr
   * - .*test_routers.HaRoutersTest
     - l3-ha
   * - .*test_routers.RoutersIpV6Test.\\

       test_extra_routes_atomic
     - extraroute-atomic
   * - .*test_routers.RoutersTest.\\

       test_extra_routes_atomic
     - extraroute-atomic
   * - .*test_routers_negative.DvrRoutersNegativeTest
     - dvr
   * - .*test_routers_negative.\\

       DvrRoutersNegativeTestExtended
     - dvr
   * - .*test_routers_negative.HaRoutersNegativeTest
     - l3-ha
   * - .*test_security_groups.RbacSharedSecurityGroupTest
     - rbac-security-groups
   * - .*test_subnetpool_prefix_ops
     - subnetpool-prefix-ops
   * - .*test_subnetpools.RbacSubnetPoolTest
     - rbac-subnetpool
   * - .*test_subnetpools_negative.SubnetPoolsNegativeTestJSON.\\

       test_tenant_create_subnetpool_associate_shared_address_scope
     - rbac-subnetpool
   * - .*test_subnetpools.SubnetPoolsSearchCriteriaTest.\\

       test_list_validation_filters
     - filter-validation
   * - .*test_subnets.SubnetsSearchCriteriaTest.\\

       test_list_validation_filters
     - filter-validation
   * - .*test_timestamp.TestTimeStamp.\\

       test_segment_with_timestamp
     - standard-attr-segment
   * - .*test_trunk.TrunkTestInheritJSONBase.\\

       test_add_subport
     - https://launchpad.net/bugs/1863707
   * - .*test_trunk.TrunkTestMtusJSON
     - vxlan
   * - .*test_trunk_negative.TrunkTestJSON.\\

       test_create_subport_invalid_inherit_network\_\\

       segmentation_type
     - vxlan
   * - .*test_trunk_negative.TrunkTestMtusJSON
     - vxlan
   * - .*test_qos.QosMinimumBandwidthRuleTestJSON
     - https://gerrit.opnfv.org/gerrit/69105
   * - .*network.test_tags
     - tag-ext
   * - .*test_routers.RoutersIpV6Test.\\

       test_create_router_set_gateway_with_fixed_ip
     - https://launchpad.net/bugs/1676207
   * - .*test_routers.RoutersTest.\\

       test_create_router_set_gateway_with_fixed_ip
     - https://launchpad.net/bugs/1676207
   * - .*test_network_basic_ops.\\

       TestNetworkBasicOps.test_router_rescheduling
     - l3_agent_scheduler
   * - .*test_network_advanced_server_ops.\\

       TestNetworkAdvancedServerOps.\\

       test_server_connectivity_cold_migration_revert
     - https://launchpad.net/bugs/1836595

Neutron API is also covered by
`Rally <https://opendev.org/openstack/rally>`__.

Here are the mainline tasks integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__:

-  Authenticate.validate_neutron
-  NeutronNetworks.create_and_delete_networks
-  NeutronNetworks.create_and_delete_ports
-  NeutronNetworks.create_and_delete_routers
-  NeutronNetworks.create_and_delete_subnets
-  NeutronNetworks.create_and_list_networks
-  NeutronNetworks.create_and_list_ports
-  NeutronNetworks.create_and_list_routers
-  NeutronNetworks.create_and_list_subnets
-  NeutronSecurityGroup.create_and_delete_security_groups
-  NeutronSecurityGroup.create_and_delete_security_group_rule
-  NeutronNetworks.set_and_clear_router_gateway
-  Quotas.neutron_update

Compute - Nova API testing
''''''''''''''''''''''''''

Nova API is covered in the OpenStack Gates via
`Tempest <https://opendev.org/openstack/tempest>`__ as integrated in
`Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__.

According to :ref:`chapters/chapter05:interfaces and apis`
the following test names must not be executed:

.. list-table:: Nova API testing
   :widths: 60 40
   :header-rows: 1

   * - Test rejection regular expressions
     - Reasons
   * - .*admin.test_agents
     - xenapi_apis
   * - .*test_fixed_ips
     - neutron
   * - .*test_fixed_ips_negative
     - neutron
   * - .*test_auto_allocate_network
     - shared networks
   * - .*test_flavors_microversions.FlavorsV255TestJSON
     - max_microversion: 2.53
   * - .*test_flavors_microversions.FlavorsV261TestJSON
     - max_microversion: 2.53
   * - .*test_floating_ips_bulk
     - nova-network
   * - .*test_live_migration.\\

       LiveAutoBlockMigrationV225Test.test_iscsi_volume
     - block live migration
   * - .*test_live_migration.\\

       LiveAutoBlockMigrationV225Test.\\

       test_live_block_migration
     - block live migration
   * - .*test_live_migration.\\

       LiveAutoBlockMigrationV225Test.\\

       test_live_block_migration_paused
     - block live migration
   * - .*test_live_migration.\\

       LiveAutoBlockMigrationV225Test.\\

       test_volume_backed_live_migration
     - volume-backed live migration
   * - .*test_live_migration.LiveMigrationTest.\\

       test_iscsi_volume
     - block live migration
   * - .*test_live_migration.LiveMigrationTest.\\

       test_live_block_migration
     - block live migration
   * - .*test_live_migration.LiveMigrationTest.\\

       test_live_block_migration_paused
     - block live migration
   * - .*test_live_migration.LiveMigrationTest.\\

       test_volume_backed_live_migration
     - volume-backed live migration
   * - .*test_live_migration.\\

       LiveMigrationRemoteConsolesV26Test
     - serial_console
   * - .*test_quotas.QuotasAdminTestV257
     - max_microversion: 2.53
   * - .*test_servers.ServersAdminTestJSON.\\

       test_reset_network_inject_network_info
     - xenapi_apis
   * - .*certificates.test_certificates
     - cert
   * - .*test_quotas_negative.\\

       QuotasSecurityGroupAdminNegativeTest
     - https://launchpad.net/bugs/1186354
   * - .*test_novnc
     - vnc_console
   * - .*test_server_personality
     - personality
   * - .*test_servers.ServerShowV263Test.\\

       test_show_update_rebuild_list_server
     - certified_image_ref
   * - .*test_servers_microversions.ServerShowV254Test
     - max_microversion: 2.53
   * - .*test_servers_microversions.ServerShowV257Test
     - max_microversion: 2.53
   * - .*test_servers_negative.ServersNegativeTestJSON.\\

       test_personality_file_contents_not_encoded
     - personality
   * - .*test_server_actions.ServerActionsTestJSON.\\

       test_change_server_password
     - change_password
   * - .*test_server_actions.ServerActionsTestJSON.\\

       test_get_vnc_console
     - vnc_console
   * - .*test_server_actions.ServerActionsTestJSON.\\

       test_reboot_server_soft
     - https://launchpad.net/bugs/1014647
   * - .*test_server_rescue.\\

       ServerBootFromVolumeStableRescueTest
     - stable_rescue
   * - .*test_server_rescue.ServerStableDeviceRescueTest
     - stable_rescue
   * - .*test_security_group_default_rules
     - https://launchpad.net/bugs/1311500
   * - .*test_security_groups_negative.\\

        SecurityGroupsNegativeTestJSON.\\

        test_security_group_create_with_duplicate_name
     - neutron
   * - .*test_security_groups_negative.\\

       SecurityGroupsNegativeTestJSON.\\

       test_security_group_create_with\_\\

       invalid_group_description
     - https://launchpad.net/bugs/1161411
   * - .*test_security_groups_negative.\\

       SecurityGroupsNegativeTestJSON.\\

       test_security_group_create_with_invalid_group_name
     - https://launchpad.net/bugs/1161411
   * - .*test_security_groups_negative.\\

       SecurityGroupsNegativeTestJSON.\\

       test_update_security_group_with_invalid_sg_description
     - neutron
   * - .*test_security_groups_negative.\\

       SecurityGroupsNegativeTestJSON.\\

       test_update_security_group_with_invalid_sg_description
     - neutron
   * - .*test_security_groups_negative.\\

       SecurityGroupsNegativeTestJSON.\\

       test_update_security_group_with_invalid_sg_id
     - neutron
   * - .*test_security_groups_negative.\\

       SecurityGroupsNegativeTestJSON.\\

       test_update_security_group_with_invalid_sg_name
     - neutron
   * - .*test_server_metadata.ServerMetadataTestJSON
     -  xenapi_apis
   * - .*test_server_metadata_negative.\\


       ServerMetadataNegativeTestJSON.\\

       test_delete_metadata_non_existent_server
     - xenapi_apis
   * - .*test_server_metadata_negative.\\

       ServerMetadataNegativeTestJSON.\\

       test_metadata_items_limit
     - xenapi_apis
   * - .*test_server_metadata_negative.\\

       ServerMetadataNegativeTestJSON.\\

       test_set_metadata_invalid_key
     - xenapi_apis
   * - .*test_server_metadata_negative.\\

       ServerMetadataNegativeTestJSON.\\

       test_set_metadata_non_existent_server
     - xenapi_apis

   * - .*test_server_metadata_negative.\\

       ServerMetadataNegativeTestJSON.\\

       test_set_server_metadata_blank_key
     - xenapi_apis
   * - .*test_server_metadata_negative.\\

       ServerMetadataNegativeTestJSON.\\

       test_set_server_metadata_missing_metadata
     - xenapi_apis

   * - .*test_server_metadata_negative.\\

       ServerMetadataNegativeTestJSON.\\

       test_update_metadata_non_existent_server
     - xenapi_apis
   * - .*test_server_metadata_negative.\\

       ServerMetadataNegativeTestJSON.\\

       test_update_metadata_with_blank_key
     - xenapi_apis
   * - .*test_list_server_filters.\\

       ListServerFiltersTestJSON.\\

       test_list_servers_filtered_by_ip_regex
     - https://launchpad.net/bugs/1540645
   * - .*servers.test_virtual_interfaces
     - nova-network
   * - .*compute.test_virtual_interfaces_negative
     - nova-network
   * - .*compute.test_networks
     - nova-network
   * - .*test_attach_volume.AttachVolumeMultiAttach
     - volume_multiattach
   * - .*test_volume_boot_pattern.\\

       TestVolumeBootPattern.\\

       test_boot_server_from_encrypted_volume_luks
     - attach_encrypted_volume
   * - .*test_volume_swap
     - swap_volume
   * - .*test_encrypted_cinder_volumes
     - attach_encrypted_volume
   * - .*test_minbw_allocation_placement
     - microversion
   * - .\*test_volumes_negative.\\

       UpdateMultiattachVolumeNegativeTest.\\

       test_multiattach_rw_volume_update_failure
     - volume_multiattach
   * - .*test_shelve_instance.TestShelveInstance.\\

       test_cold_migrate_unshelved_instance
     - shelve_migrate

Nova API is also covered by
`Rally <https://opendev.org/openstack/rally>`__.

Here are the mainline tasks integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__:

-  Authenticate.validate_nova
-  NovaServers.boot_and_live_migrate_server
-  NovaServers.boot_server_attach_created_volume_and_live_migrate
-  NovaServers.boot_server_from_volume_and_live_migrate
-  NovaKeypair.boot_and_delete_server_with_keypair
-  NovaServers.boot_server_from_volume_and_delete
-  NovaServers.pause_and_unpause_server
-  NovaServers.boot_and_migrate_server
-  NovaServers.boot_server_and_list_interfaces
-  NovaServers.boot_server_associate_and_dissociate_floating_ip
-  NovaServerGroups.create_and_delete_server_group
-  Quotas.nova_update

Orchestration - Heat API testing
''''''''''''''''''''''''''''''''

Heat API is covered in the OpenStack Gates via
`heat-tempest-plugin <https://opendev.org/openstack/heat-tempest-plugin>`__
as integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__

According to :ref:`chapters/chapter05:interfaces and apis`
the following test names must not be executed:

.. list-table:: Heat API testing
   :widths: 60 40
   :header-rows: 1

   * - Test rejection regular expressions
     - Reasons
   * - .*functional.test_lbaasv2
     - lbaasv2
   * - .*functional.test_encryption_vol_type
     - https://storyboard.openstack.org/#!/story/2007804
   * - .*RemoteStackTest.\\

       test_stack_create_with_cloud_credential
     - https://gerrit.opnfv.org/gerrit/c/functest/+/69926
   * - .*scenario.test_aodh_alarm
     - aodh
   * - .*tests.scenario.test_autoscaling_lb
     - lbaas
   * - .*scenario.test_autoscaling_lbv2
     - lbaasv2
   * - .*scenario.test_server_software_config
     - https://gerrit.opnfv.org/gerrit/c/functest/+/69926
   * - .*test_volumes.\\

       VolumeBackupRestoreIntegrationTest
     - https://gerrit.opnfv.org/gerrit/c/functest/+/69931
   * - .*scenario.test_octavia_lbaas
     - octavia
   * - .*scenario.test_server_cfn_init
     - https://gerrit.opnfv.org/gerrit/c/functest/+/70004

Heat API is also covered by
`Rally <https://opendev.org/openstack/rally>`__.

Here are the mainline tasks integrated in `Functest Smoke
CNTT <https://git.opnfv.org/functest/tree/docker/smoke-cntt/testcases.yaml?h=stable%2Fwallaby>`__:

-  Authenticate.validate_heat
-  HeatStacks.create_update_delete_stack
-  HeatStacks.create_check_delete_stack
-  HeatStacks.create_suspend_resume_delete_stack
-  HeatStacks.list_stacks_and_resources

Dashboard
^^^^^^^^^

Horizon is covered in the OpenStack Gates via
`tempest-horizon <https://github.com/openstack/tempest-horizon>`__ as
integrated in `Functest
Healthcheck <https://git.opnfv.org/functest/tree/docker/healthcheck/testcases.yaml?h=stable%2Fwallaby>`__.

OpenStack API benchmarking
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Rally <https://opendev.org/openstack/rally>`__ is tool and framework
that allows to perform OpenStack API benchmarking.

Here are the Rally-based test cases proposed by `Functest Benchmarking
CNTT <https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml?h=stable%2Fwallaby>`__:

-  `rally_full <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:
   Functest scenarios iterating 10 times the mainline Rally scenarios
-  `rally_jobs <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_jobs_cntt-run-5/rally_jobs_cntt/rally_jobs_cntt.html>`__:
   Neutron scenarios executed in the OpenStack gates

At the time of writing, no KPI is defined in
:ref:`chapters/chapter05:interfaces and apis`
which would have asked for an update of the default SLA (maximum failure
rate of 0%) proposed in `Functest Benchmarking
CNTT <https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml?h=stable%2Fwallaby>`__

Identity - Keystone API benchmarking
''''''''''''''''''''''''''''''''''''

`Functest
rally_full_cntt <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:

.. table:: Keystone API benchmarking
   :widths: auto

   ============================================== ==========
   Scenarios                                      Iterations
   ============================================== ==========
   Authenticate.keystone                          10
   KeystoneBasic.add_and_remove_user_role         10
   KeystoneBasic.create_add_and_list_user_roles   10
   KeystoneBasic.create_and_list_tenants          10
   KeystoneBasic.create_and_delete_role           10
   KeystoneBasic.create_and_delete_service        10
   KeystoneBasic.get_entities                     10
   KeystoneBasic.create_update_and_delete_tenant  10
   KeystoneBasic.create_user                      10
   KeystoneBasic.create_tenant                    10
   KeystoneBasic.create_and_list_users            10
   KeystoneBasic.create_tenant_with_users         10
   ============================================== ==========

Image - Glance API benchmarking
'''''''''''''''''''''''''''''''

`Functest
rally_full_cntt <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:

.. table:: Glance API benchmarking
   :widths: auto

   ============================================ ==========
   Scenarios                                    Iterations
   ============================================ ==========
   Authenticate.validate_glance                 10
   GlanceImages.create_and_delete_image         10
   GlanceImages.create_and_list_image           10
   GlanceImages.list_images                     10
   GlanceImages.create_image_and_boot_instances 10
   GlanceImages.create_and_deactivate_image     10
   GlanceImages.create_and_download_image       10
   GlanceImages.create_and_get_image            10
   GlanceImages.create_and_update_image         10
   ============================================ ==========

Block Storage - Cinder API benchmarking
'''''''''''''''''''''''''''''''''''''''

`Functest
rally_full_cntt <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:

.. table:: Cinder API benchmarking
   :widths: auto

   ============================================================= ==========
   Scenarios                                                     Iterations
   ============================================================= ==========
   Authenticate.validate_glance                                  10
   CinderVolumes.create_and_attach_volume                        10
   CinderVolumes.create_and_list_snapshots                       10
   CinderVolumes.create_and_list_volume                          10
   CinderVolumes.create_and_upload_volume_to_image               10
   CinderVolumes.create_nested_snapshots_and_attach_volume       10
   CinderVolumes.create_snapshot_and_attach_volume               10
   CinderVolumes.create_volume                                   10
   CinderVolumes.list_volumes                                    10
   CinderVolumes.create_and_delete_snapshot                      10
   CinderVolumes.create_and_delete_volume                        10
   CinderVolumes.create_and_extend_volume                        10
   CinderVolumes.create_from_volume_and_delete_volume            10
   CinderQos.create_and_get_qos                                  10
   CinderQos.create_and_list_qos                                 10
   CinderQos.create_and_set_qos                                  10
   CinderVolumeTypes.create_and_get_volume_type                  10
   CinderVolumeTypes.create_and_list_volume_types                10
   CinderVolumeTypes.create_and_update_volume_type               10
   CinderVolumeTypes.create_volume_type_and_encryption_type      10
   CinderVolumeTypes.create_volume_type_add_and_list_type_access 10
   Quotas.cinder_update_and_delete                               10
   Quotas.cinder_update                                          10
   ============================================================= ==========

Object Storage - Swift API benchmarking
'''''''''''''''''''''''''''''''''''''''

`Functest
rally_full_cntt <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:

.. table:: Swift API benchmarking
   :widths: auto

   ============================================================= ==========
   Scenarios                                                     Iterations
   ============================================================= ==========
   SwiftObjects.create_container_and_object_then_list_objects    10
   SwiftObjects.list_objects_in_containers                       10
   SwiftObjects.create_container_and_object_then_download_object 10
   SwiftObjects.create_container_and_object_then_delete_all      10
   SwiftObjects.list_and_download_objects_in_containers          10
   ============================================================= ==========

Networking - Neutron API benchmarking
'''''''''''''''''''''''''''''''''''''

`Functest
rally_full_cntt <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:

.. table:: Neutron API benchmarking
   :widths: auto

   ========================================================== ==========
   Scenarios                                                  Iterations
   ========================================================== ==========
   Authenticate.validate_neutron                              10
   NeutronNetworks.create_and_update_networks                 10
   NeutronNetworks.create_and_update_ports                    10
   NeutronNetworks.create_and_update_routers                  10
   NeutronNetworks.create_and_update_subnets                  10
   NeutronNetworks.create_and_delete_networks                 10
   NeutronNetworks.create_and_delete_ports                    10
   NeutronNetworks.create_and_delete_routers                  10
   NeutronNetworks.create_and_delete_subnets                  10
   NeutronNetworks.create_and_list_networks                   10
   NeutronNetworks.create_and_list_ports                      10
   NeutronNetworks.create_and_list_routers                    10
   NeutronNetworks.create_and_list_subnets                    10
   NeutronSecurityGroup.create_and_delete_security_groups     10
   NeutronSecurityGroup.create_and_delete_security_group_rule 10
   NeutronSecurityGroup.create_and_list_security_group_rules  10
   NeutronSecurityGroup.create_and_show_security_group        10
   NeutronNetworks.set_and_clear_router_gateway               10
   NeutronNetworks.create_and_show_ports                      10
   NeutronNetworks.create_and_show_routers                    10
   NeutronNetworks.create_and_show_subnets                    10
   Quotas.neutron_update                                      10
   ========================================================== ==========

`Functest
rally_jobs_cntt <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:

.. table:: Neutron API benchmarking
   :widths: auto

   ========================================== ==========
   Scenarios                                  Iterations
   ========================================== ==========
   NeutronNetworks.create_and_delete_networks 40
   NeutronNetworks.create_and_delete_ports    40
   NeutronNetworks.create_and_delete_routers  40
   NeutronNetworks.create_and_delete_subnets  40
   NeutronNetworks.create_and_list_networks   100
   NeutronNetworks.create_and_list_ports      8
   NeutronNetworks.create_and_list_routers    40
   NeutronNetworks.create_and_list_subnets    40
   NeutronNetworks.create_and_update_networks 40
   NeutronNetworks.create_and_update_ports    40
   NeutronNetworks.create_and_update_routers  40
   NeutronNetworks.create_and_update_subnets  100
   NeutronTrunks.create_and_list_trunks       4
   Quotas.neutron_update                      40
   ========================================== ==========

Compute - Nova API benchmarking
'''''''''''''''''''''''''''''''

`Functest
rally_full_cntt <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:

.. list-table:: Nova API benchmarking
   :widths: 70 30
   :header-rows: 1

   * - Scenarios
     - Iterations
   * - Authenticate.validate_nova
     - 10
   * - NovaKeypair.create_and_delete_keypair
     - 10
   * - NovaKeypair.create_and_list_keypairs
     - 10
   * - NovaServers.boot_and_bounce_server
     - 10
   * - NovaServers.boot_and_delete_server
     - 10
   * - NovaServers.boot_and_list_server
     - 10
   * - NovaServers.boot_and_rebuild_server
     - 10
   * - NovaServers.snapshot_server
     - 10
   * - NovaServers.boot_server_from_volume
     - 10
   * - NovaServers.boot_server
     - 10
   * - NovaServers.list_servers
     - 10
   * - NovaServers.resize_server
     - 10
   * - NovaServers.boot_and_live_migrate_server
     - 10
   * - NovaServers.boot_server_attach_created_volume_and_live_migrate
     - 10
   * - NovaServers.boot_server_from_volume_and_live_migrate
     - 10
   * - NovaKeypair.boot_and_delete_server_with_keypair
     - 10
   * - NovaServers.boot_server_from_volume_and_delete
     - 10
   * - NovaServers.pause_and_unpause_server
     - 10
   * - NovaServers.boot_and_migrate_server
     - 10
   * - NovaServers.boot_server_and_list_interfaces
     - 10
   * - NovaServers.boot_and_get_console_url
     - 10
   * - NovaServers.boot_server_and_attach_interface
     - 10
   * - NovaServers.boot_server_attach_volume_and_list_attachments
     - 10
   * - NovaServers.boot_server_associate_and_dissociate_floating_ip
     - 10
   * - NovaServers.boot_and_associate_floating_ip
     - 10
   * - NovaServerGroups.create_and_delete_server_group
     - 10
   * - NovaServerGroups.create_and_get_server_group
     - 10
   * - NovaServerGroups.create_and_list_server_groups
     - 10
   * - Quotas.nova_update
     - 10

Orchestration - Heat API benchmarking
'''''''''''''''''''''''''''''''''''''

`Functest
rally_full_cntt <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-cntt-wallaby-rally_full_cntt-run-5/rally_full_cntt/rally_full_cntt.html>`__:

.. table:: Heat API benchmarking
   :widths: auto

   ============================================= ==========
   Scenarios                                     Iterations
   ============================================= ==========
   Authenticate.validate_heat                    10
   HeatStacks.create_and_delete_stack            10
   HeatStacks.create_and_list_stack              10
   HeatStacks.create_update_delete_stack         10
   HeatStacks.create_check_delete_stack          10
   HeatStacks.create_suspend_resume_delete_stack 10
   HeatStacks.list_stacks_and_resources          10
   ============================================= ==========

Dataplane benchmarking
^^^^^^^^^^^^^^^^^^^^^^

`Functest Benchmarking
CNTT <https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml?h=stable%2Fwallaby>`__
offers two benchmarking dataplane test cases leveraging on:

-  `VMTP <http://vmtp.readthedocs.io/en/latest>`__
-  `Shaker <https://pyshaker.readthedocs.io/en/latest/>`__

`VMTP <https://vmtp.readthedocs.io/en/latest/>`__ is a small python
application that will automatically perform ping connectivity, round
trip time measurement (latency) and TCP/UDP throughput measurement on
any OpenStack deployment.

`Shaker <https://pyshaker.readthedocs.io/en/latest/>`__ wraps around
popular system network testing tools like iperf, iperf3 and netperf
(with help of flent).
`Shaker <https://pyshaker.readthedocs.io/en/latest/>`__ is able to deploy
OpenStack instances and networks in different topologies.
`Shaker <https://pyshaker.readthedocs.io/en/latest/>`__ scenario
specifies the deployment and list of tests to execute.

At the time of writing, no KPIs are defined in Anuket specifications
which would have asked for an update of the default SLA proposed in
`Functest Benchmarking
CNTT <https://git.opnfv.org/functest/tree/docker/benchmarking-cntt/testcases.yaml?h=stable%2Fwallaby>`__

On top of this dataplane benchmarking described in VMTP & Shaker, we
need to integrate testing as described in `ETSI GS NFV-TST 009:
Specification of Networking Benchmarks and Measurement Methods for
NFVI <https://www.etsi.org/deliver/etsi_gs/NFV-TST/001_099/009/03.01.01_60/gs_NFV-TST009v030101p.pdf>`__.
This type of testing is better suited to measure the networking
capabilities of a compute node. The `rapid
scripts <https://git.opnfv.org/samplevnf>`__ in
conjunction with the `PROX
tool <https://docs.anuket.io/projects/samplevnf/en/latest/testing/user/userguide/index.html>`__
offers an open source implementation for this type of testing.

VMTP
''''

Here are the
`scenarios <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-wallaby-vmtp-run-8/vmtp/vmtp.json>`__
executed by `Functest
vmtp <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-wallaby-vmtp-run-8/vmtp/vmtp.html>`__:
- VM to VM same network fixed IP (intra-node) - VM to VM different
network fixed IP (intra-node) - VM to VM different network floating IP
(intra-node) - VM to VM same network fixed IP (inter-node) - VM to VM
different network fixed IP (inter-node) - VM to VM different network
floating IP (inter-node)

Here are all results per scenario:

.. table:: All results per scenario
   :widths: auto

   ======== ======== ===============
   protocol pkt_size results
   ======== ======== ===============
   ICMP     64       rtt_avg_ms
   ICMP     64       rtt_max_ms
   ICMP     64       rtt_min_ms
   ICMP     64       rtt_stddev
   ICMP     391      rtt_avg_ms
   ICMP     391      rtt_max_ms
   ICMP     391      rtt_min_ms
   ICMP     391      rtt_stddev
   ICMP     1500     rtt_avg_ms
   ICMP     1500     rtt_max_ms
   ICMP     1500     rtt_min_ms
   ICMP     1500     rtt_stddev
   UDP      128      loss_rate
   UDP      128      throughput_kbps
   UDP      1024     loss_rate
   UDP      1024     throughput_kbps
   UDP      8192     loss_rate
   UDP      8192     throughput_kbps
   TCP      65536    rtt_ms
   TCP      65536    throughput_kbps
   ======== ======== ===============

Shaker
''''''

Here are the
`scenarios <http://artifacts.opnfv.org/functest/KDBNITEN317M/functest-opnfv-functest-benchmarking-wallaby-shaker-run-8/shaker/report.json>`__
executed by Shaker:

-  OpenStack L2
-  OpenStack L3 East-West
-  OpenStack L3 North-South
-  OpenStack L3 North-South Performance

Here are all samples:

.. table:: All samples
   :widths: auto

   ============== ======================
   test           samples
   ============== ======================
   Bi-directional ping_icmp (ms)
   Bi-directional tcp_download (Mbits/s)
   Bi-directional tcp_upload (Mbits/s)
   Download       ping_icmp (ms)
   Download       tcp_download (Mbits/s)
   Upload         ping_icmp (ms)
   Upload         tcp_upload (Mbits/s)
   Ping           ping_icmp (ms)
   Ping           ping_udp (ms)
   TCP            bandwidth (bit/s)
   TCP            retransmits
   UDP            packets (pps)
   ============== ======================

Opensource VNF onboarding and testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Running opensource VNFs is a key technical solution to ensure that the
platforms meet Network Functions Virtualization requirements. `Functest
VNF <https://git.opnfv.org/functest/tree/docker/vnf/testcases.yaml?h=stable%2Fwallaby>`__
offers 5 test cases which automatically onboard and test the following 3
opensource VNFs:

-  `Clearwater IMS <https://clearwater.readthedocs.io/en/stable/>`__
-  `VyOS vRouter <https://www.vyos.io/>`__
-  `OpenAirInterface vEPC <https://www.openairinterface.org/>`__

Here are the full list of orchestrators used for all these deployments:

-  `Cloudify <https://cloudify.co/>`__
-  `Heat <https://wiki.openstack.org/wiki/Heat>`__
-  `Juju <https://jaas.ai/>`__

The VNF are covered by upstream tests when possible (see
`clearwater-live-test <https://github.com/Metaswitch/clearwater-live-test>`__)
and by Functest VNF tests in the other cases.

Test Cases Traceability to Requirements
---------------------------------------

RM/RA-1 Requirements
~~~~~~~~~~~~~~~~~~~~

The following test cases must pass as they are for OpenStack based cloud
infrastructure Conformance:

.. table:: OpenStack based cloud infrastructure Conformance
   :widths: auto

   ======================================== ===================== ========
   container                                test case             criteria
   ======================================== ===================== ========
   opnfv/functest-healthcheck:wallaby       tempest_horizon       PASS
   opnfv/functest-smoke-cntt:wallaby        tempest_neutron_cntt  PASS
   opnfv/functest-smoke-cntt:wallaby        tempest_cinder_cntt   PASS
   opnfv/functest-smoke-cntt:wallaby        tempest_keystone_cntt PASS
   opnfv/functest-smoke-cntt:wallaby        rally_sanity_cntt     PASS
   opnfv/functest-smoke-cntt:wallaby        tempest_full_cntt     PASS
   opnfv/functest-smoke-cntt:wallaby        tempest_scenario_cntt PASS
   opnfv/functest-smoke-cntt:wallaby        tempest_slow_cntt     PASS
   opnfv/functest-benchmarking-cntt:wallaby rally_full_cntt       PASS
   opnfv/functest-benchmarking-cntt:wallaby rally_jobs_cntt       PASS
   opnfv/functest-benchmarking-cntt:wallaby vmtp                  PASS
   opnfv/functest-benchmarking-cntt:wallaby shaker                PASS
   opnfv/functest-vnf:wallaby               cloudify              PASS
   opnfv/functest-vnf:wallaby               cloudify_ims          PASS
   opnfv/functest-vnf:wallaby               heat_ims              PASS
   opnfv/functest-vnf:wallaby               vyos_vrouter          PASS
   opnfv/functest-vnf:wallaby               juju_epc              PASS
   ======================================== ===================== ========

TC Mapping to Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+----------------------------------------------------+
| test case             | requirements                                       |
+=======================+====================================================+
| tempest_horizon       | Horizon testing                                    |
+-----------------------+----------------------------------------------------+
| tempest_neutron_cntt  | Neutron API testing                                |
+-----------------------+----------------------------------------------------+
| tempest_cinder_cntt   | Cinder API testing                                 |
+-----------------------+----------------------------------------------------+
| tempest_keystone_cntt | Keystone API testing                               |
+-----------------------+----------------------------------------------------+
| rally_sanity_cntt     | Keystone, Glance, Cinder, Swift, Neutron, Nova and |
|                       | Heat API testing                                   |
+-----------------------+----------------------------------------------------+
| tempest_full_cntt     | Keystone, Glance, Cinder, Swift, Neutron and Nova  |
|                       | API testing                                        |
+-----------------------+----------------------------------------------------+
| tempest_scenario_cntt | Keystone, Glance, Cinder, Swift, Neutron and Nova  |
|                       | API testing                                        |
+-----------------------+----------------------------------------------------+
| tempest_slow_cntt     | Keystone, Glance, Cinder, Swift, Neutron and Nova  |
|                       | API testing                                        |
+-----------------------+----------------------------------------------------+
| rally_full_cntt       | Keystone, Glance, Cinder, Swift, Neutron, Nova and |
|                       | Heat API benchmarking                              |
+-----------------------+----------------------------------------------------+
| rally_jobs_cntt       | Neutron API benchmarking                           |
+-----------------------+----------------------------------------------------+
| vmtp                  | Dataplane benchmarking                             |
+-----------------------+----------------------------------------------------+
| shaker                | Dataplane benchmarking                             |
+-----------------------+----------------------------------------------------+
| cloudify              | opensource VNF onboarding and testing              |
+-----------------------+----------------------------------------------------+
| cloudify_ims          | opensource VNF onboarding and testing              |
+-----------------------+----------------------------------------------------+
| heat_ims              | opensource VNF onboarding and testing              |
+-----------------------+----------------------------------------------------+
| vyos_vrouter          | opensource VNF onboarding and testing              |
+-----------------------+----------------------------------------------------+
| juju_epc              | opensource VNF onboarding and testing              |
+-----------------------+----------------------------------------------------+

OpenStack Testing Cookbook
--------------------------

Please note the next two points depending on the GNU/Linux distributions
and the network settings:

-  SELinux: you may have to add --system-site-packages when creating the
   virtualenv (“Aborting, target uses selinux but python bindings
   (libselinux-python) aren’t installed!”)
-  Proxy: you may set your proxy in env for Ansible and in systemd for
   Docker https://docs.docker.com/config/daemon/systemd/#httphttps-proxy

To deploy your own CI toolchain running OpenStack based cloud infrastructure
Conformance:

.. code:: bash

   virtualenv functest --system-site-packages
   . functest/bin/activate
   pip install ansible
   ansible-galaxy install collivier.xtesting
   ansible-galaxy collection install ansible.posix community.general community.grafana kubernetes.core community.docker community.postgresql
   git clone https://gerrit.opnfv.org/gerrit/functest functest-src
   (cd functest-src && git checkout -b stable/wallaby origin/stable/wallaby)
   ansible-playbook functest-src/ansible/site.cntt.yml

OpenStack API testing configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the default Functest tree as proposed in `Functest
Wallaby <https://wiki.anuket.io/display/HOME/Functest+Wallaby>`__:

-  /home/opnfv/functest/openstack.creds
-  /home/opnfv/functest/images

Download the images and fill /home/opnfv/functest/openstack.creds as
proposed in `Functest
Wallaby <https://wiki.anuket.io/display/HOME/Functest+Wallaby>`__

You may have to modify a few Functest env vars according to the SUT (see
env in `Functest
Wallaby <https://wiki.anuket.io/display/HOME/Functest+Wallaby>`__). Be
free to modify functest-src/ansible/host_vars/127.0.0.1 at your
convenience and then to reconfigure the toolchain:

.. code:: bash

   ansible-playbook functest-src/ansible/site.cntt.yml

Run OpenStack based cloud infrastructure Conformance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open http://127.0.0.1:8080/job/functest-wallaby-daily/ in a web browser,
login as admin/admin and click on “Build with Parameters” (keep the
default build_tag value).

If the System under test (SUT) is compliant, a link to the full
archive containing all test results and artifacts will be printed in
functest-wallaby-zip’s console. Be free to download it and then to send
it to any reviewer committee.

To clean your working dir:

.. code:: bash

   deactivate
   rm -rf functest-src functest
