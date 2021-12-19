Anuket Reference Conformance
============================

Requirements and Testing Principles
-----------------------------------

The objective of each RC workstream is to provide an automated mechanism
to validate either a network function (NF) or a cloud infrastructure
against a standard set of requirements defined by the Reference Model
(RM) and associated Reference Architecture (RA). Through this validation
mechanism, a provider of either NFs or cloud infrastructure will be able
to test their conformance to the RM and RA. This will ease the
integration of NFs into operator environments that host compatible cloud
infrastructures, thereby reducing cost, complexity, and time of
integration.

The overall workstream requires the close coordination of the following:

-  **Requirements** - The agreed upon capabilities and conditions that a
   compliant NF or cloud infrastructure must provide or satisfy. All
   requirements will be hosted and maintained in the RA.
-  **Tests** - The verification mechanism that determines that a given
   NF or cloud infrastructure complies with one or more requirements.
-  **Conformance Specifications** - The definition of the requirements,
   tests, and circumstances (test case integration, etc.) that must be
   met to be deemed conformant.

If there is no clear traceability and strong links between these 3
components, then it becomes difficult to determine if a NF or cloud
infrastructure is compliant. With this in mind, below are the set of
recommended principles for each of the three components to follow.
Adherence to these principles will provide the following:

-  Enable clear progress tracking and linkage between independent
   projects (i.e. know what has and hasn’t been covered, and track
   changes over time)
-  Help users better understand if they meet requirements
-  Provide a stable set of point-in-time requirements and tests to
   achieve conformance
-  Reduce ambiguity in testing, requirements, and conformance

Requirement Principles
~~~~~~~~~~~~~~~~~~~~~~

Requirement Principles can be found in the `Anuket
Principles <https://cntt.readthedocs.io/en/latest/common/chapter00.html#requirements-principles>`__

Testing Principles
~~~~~~~~~~~~~~~~~~

-  There must be traceability between test cases and requirement being
   validated
-  Failures should provide additional content to inform the user where
   or how the requirement was violated (e.g. which file or resource
   violated the requirement). Put another way, don’t require the user to
   read the test to understand what went wrong
-  Testing tools should support selection of tests based on category or
   profile.
-  Tests must be available to run locally by both CNF and cloud
   infrastructure providers
-  Testing tools must produce machine-readable result formats that can
   be used as input into the badging program (OVP already defines a
   format)

Conformance Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

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

All Anuket conformance suites must utilize the Anuket test case
integration toolchain to deliver overall integration, the same end user
actions, and a unique test result format (e.g. Anuket test result
database) needed by the end users and the test case result verification
programs (e.g. `OVP <https://www.opnfv.org/verification>`__).
Historically, these rules were agreed by RC1 team and have been applied
since. The Anuket test integration toolchains will be used by all
conformance suites.

Anuket RI and RC toolchains
---------------------------

Anuket has built a complete CI/CD toolchain for continuously deploying
and testing cloud infrastructure.

As for all installer projects,
`Jenkins <https://build.opnfv.org/ci/view/cntt/>`__ triggers scenario
deployments, runs the Anuket gating test cases and then publishes all
test results in the `centralized test
database <https://docs.opnfv.org/en/stable-hunter/_images/OPNFV_testing_working_group.png>`__
and all artifacts (reports, logs, etc.) to `an S3 compatible storage
service <http://artifacts.opnfv.org/>`__.

The Anuket verification, validation, and conformance processes leverage
existing Anuket testing knowledge (projects) and experience (history) by
utilising the Anuket toolchain design already in-place. The RC toolchain
only requires for the local deployment of the components instead of
leveraging the common Anuket centralized services. However, the
interfaces remain unchanged for leveraging test jobs, the common test
case execution, the test result database and the S3 protocol to publish
the artifacts. It’s worth mentioning that dumping all results and logs
required for conformance is already in place in CIRV (see
`cntt-latest-zip <https://build.opnfv.org/ci/job/cntt-latest-zip/>`__)
and Functest daily jobs (see
`functest-wallaby-zip <https://build.opnfv.org/ci/job/functest-wallaby-zip/4/console>`__).

It should be noted that `Xtesting
CI <https://galaxy.ansible.com/collivier/xtesting>`__ supports both
centralized and distributed deployment models as described before. It
has deployed the full toolchain in one small virtual machine to verify
ONAP Openlab via Functest.

Test Case Integration
---------------------

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

It’s worth mentioning that :doc:ref_cert/RC1/chapters/chapter03`__
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
-----------------

`Xtesting CI <https://galaxy.ansible.com/collivier/xtesting>`__
leverages the common test case execution proposed by Xtesting. Thanks to
a simple test case list, this tool deploys plug-and-play `CI/CD
toolchains in a few
commands <https://wiki.opnfv.org/pages/viewpage.action?pageId=32015004>`__.
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
   Releng <https://git.opnfv.org/releng/tree/jjb/airship/cntt.yaml>`__
   to verify Anuket RI
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

`Xtesting CI <https://galaxy.ansible.com/collivier/xtesting>`__ only
requires GNU/Linux as Operating System and asks for a few dependencies
as described in `Deploy your own Xtesting CI/CD
toolchains <https://wiki.opnfv.org/pages/viewpage.action?pageId=32015004>`__:

-  python-virtualenv
-  git

Please note the next two points depending on the GNU/Linux distributions
and the network settings:

-  SELinux: you may have to add --system-site-packages when creating the
   virtualenv (“Aborting, target uses selinux but python bindings
   (libselinux-python) aren’t installed!”)
-  Proxy: you may set your proxy in env for Ansible and in systemd for
   Docker https://docs.docker.com/config/daemon/systemd/#httphttps-proxy

Available Programs
------------------

-  :doc:`ref_cert/RC1/index`
-  :doc:`ref_cert/RC2/index`
