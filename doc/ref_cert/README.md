[<< Back](../)

# CNTT Reference Conformance (RC) Requirements and Testing Principles

The objective of each RC workstream is to provide an automated mechanism to validate either a network function (NF) or a cloud infrastructure against a standard set of requirements defined by the Reference Model (RM) and associated Reference Architecture (RA).  Through this validation mechanism, a provider of either NFs or cloud infrastructure will be able to test their conformance to the RM and RA.  This will ease the integration of NFs into operator environments that host compatible cloud infrastructures, thereby reducing cost, complexity, and time of integration.

The overall workstream requires the close coordination of the following:

**Requirements** - The agreed upon capabilities and conditions that a compliant NF or cloud infrastructure must provide or satisfy. All requirements will be hosted and maintained in the RA.
**Tests** - The verification mechanism that determines that a given NF or cloud infrastructure complies with one or more requirements.
**Conformance Specifications** - The definition of the requirements, tests, and circumstances (test case integration, etc.) that must be met to be deemed conformant.

If there is no clear traceability and strong links between these 3 components, then it becomes difficult to determine if a NF or cloud infrastructure is compliant. With this in mind, below are the set of recommended principles for each of the three components to follow. Adherence to these principles will provide the following:

* Enable clear progress tracking and linkage between independent projects (i.e. know what has and hasn't been covered, and track changes over time)
* Help users better understand if they meet requirements
* Provide a stable set of point-in-time requirements and tests to achieve conformance
* Reduce ambiguity in testing, requirements, and conformance


## Requirement Principles
Requirements Principles can be found in the [RM Principles](https://github.com/cntt-n/CNTT/blob/master/doc/common/chapter00.md#2.0)

## Testing Principles
* There must be traceability between test cases and requirement being validated
* Failures should provide additional content to inform the user where or how the requirement was violated (e.g. which file or resource violated the requirement). Put another way, don’t require the user to read the test to understand what went wrong
* Testing tools should support selection of tests based on category or profile.
* Tests must be available to run locally by both CNF and cloud infrastructure providers
* Testing tools must produce machine-readable result formats that can be used as input into the badging program (OVP already defines a format)

## Conformance Specifications
* Conformance specifications must refer to or define the *versioned* requirements that must be satisfied
* Conformance specifications must refer to the *versioned* test implementations that must be used to validate the requirements
* Conformance specifications must define the expected preconditions and environment requirements for any test tooling
* Conformance specifications must define which tests must be executed in the given testing tools to achieve conformance
* The conformance specifications must provide the mapping between tests and requirements to demonstrate traceability and coverage.

# CNTT Reference Conformance (RC) Test Case Integration

All CNTT conformance suites must utilize the OPNFV test case integration
toolchain to deliver overall integration, the same end user
actions, and a unique test result format (e.g. OPNFV test result database)
needed by the end users and the test case result verification programs (e.g.
[OVP](https://www.opnfv.org/verification)). Historically, these rules were
agreed by RC1 team and have been applied since.
The OPNFV test integration toolchains will be used by all CNTT conformance suites.

<a name="ri-rc-toolchaings"></a>
## CNTT RI and RC toolchains

[OPNFV](https://www.opnfv.org/) has built a complete CI/CD toolchain
for continuously deploying and testing cloud infrastructure.

As for all OPNFV installer projects,
[Jenkins](https://build.opnfv.org/ci/view/cntt/) triggers scenario deployments,
runs the OPNFV gating test cases and then publishes all test results in the
[centralized test database](https://docs.opnfv.org/en/stable-hunter/_images/OPNFV_testing_working_group.png)
and all artifacts (reports, logs, etc.) to
[an S3 compatible storage service](http://artifacts.opnfv.org/).

The CNTT verification, validation, and conformance processes leverage
existing OPNFV testing knowledge (projects) and experience (history) by utilising
the OPNFV toolchain design already in-place. The RC toolchain
only requires for the local deployment of the components instead of leveraging
the common OPNFV centralized services. However, the interfaces remain unchanged
for leveraging test jobs, the common test case execution, the test
result database and the S3 protocol to publish the artifacts. It's worth
mentioning that dumping all results and logs required for conformance is
already in place in CIRV (see
[cntt-latest-zip](https://build.opnfv.org/ci/job/cntt-latest-zip/)) and
Functest daily jobs (see
[functest-hunter-zip](https://build.opnfv.org/ci/job/functest-hunter-zip/3/console)).

It should be noted that
[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) supports both
centralized and distributed deployment models as described before. It has
deployed the full toolchain in one small virtual machine to verify ONAP Openlab
via Functest.

<a name="testing-integration-requirements"></a>
## Test Case Integration

To reach all goals (verification, validation, compliance, and conformance)
expected by CNTT, all test cases must be delivered as
[Docker containers](https://www.docker.com/) to simplify the CI toolchain setup including:
- the common test case execution
- the unified way to manage all the interactions with the CI/CD components and
  with third-parties (e.g. dump all test case logs and results for
  conformance)

For their part, the Docker containers simply enforce that the test cases are
delivered with all runtime dependencies. This prevents lots of manual
operations when configuring the servers running the test cases and prevents
conflicts between the test cases due to any dependencies.

It's worth mentioning that current
[test cases selected by CNTT](RC1/chapters/chapter03.md)
already leverage [Xtesting](https://xtesting.readthedocs.io/en/latest/)
which is a simple framework to assemble sparse test cases and to accelerate the
adoption of CI/CD best practices. By managing all the interactions with the
CI/CD components (test scheduler, test results database, artifact repository),
it allows the developer to work only on the test suites without diving into
CI/CD integration. Even more, it brings the capability to run heterogeneous
test cases in the same CI toolchains thanks to a few,
[quickly achievable](https://www.sdxcentral.com/articles/news/opnfvs-6th-release-brings-testing-capabilities-that-orange-is-already-using/2018/05/),
constraints.

The Docker containers proposed by the test projects must also embed
[the Xtesting Python package](https://pypi.org/project/xtesting/) and
[the related test case execution description files](https://git.opnfv.org/functest-xtesting/tree/docker/testcases.yaml)
as required by Xtesting.

Here are the issues tracking the updates of the existing OPNFV test
projects:
- Bottlenecks: https://github.com/cntt-n/CNTT/issues/510
- NFVBench: https://github.com/cntt-n/CNTT/issues/865
- StorPerf: https://github.com/cntt-n/CNTT/issues/673
- VSPERF: https://github.com/cntt-n/CNTT/issues/511
- YardStick: https://github.com/cntt-n/CNTT/issues/509

<a name="testing-cookbooks"></a>
## Testing Cookbooks

[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) leverages the
common test case execution proposed by Xtesting. Thanks to a simple test case
list, this tool deploys plug-and-play
[CI/CD toolchains in a few commands](https://wiki.opnfv.org/pages/viewpage.action?pageId=32015004).
In addition, it supports multiple components such as Jenkins and Gitlab CI
(test schedulers) and
[multiple deployment models](https://lists.opnfv.org/g/opnfv-tsc/message/5702)
such as all-in-one or centralized services.

[Xtesting](https://xtesting.readthedocs.io/en/latest/) and
[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) combined meet the
CNTT requirements about verification, validation, compliance, and conformance:
- smoothly assemble multiple heterogeneous test cases
- generate the Jenkins jobs in
  [OPNFV Releng](https://git.opnfv.org/releng/tree/jjb/airship/cntt.yaml) to
  verify CNTT RI
- deploy local CI/CD toolchains everywhere to check compliance with CNTT
- [dump all test case results and logs](http://artifacts.opnfv.org/functest/9ID39XK47PMZ.zip)
  for third-party conformance review

Here are a couple of publicly available playbooks :
- [Xtesting samples](https://git.opnfv.org/functest-xtesting/plain/ansible/site.yml?h=stable/leguer)
- [OpenStack verification](https://git.opnfv.org/functest/plain/ansible/site.yml?h=stable/leguer)
- [CNTT RC1](https://git.opnfv.org/functest/plain/ansible/site.cntt.yml?h=stable/hunter)
- [Kubernetes verification](https://git.opnfv.org/functest-kubernetes/plain/ansible/site.yml?h=stable/leguer)

[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) only requires
GNU/Linux as Operating System and asks for a few dependencies as described in
[Deploy your own Xtesting CI/CD toolchains](https://wiki.opnfv.org/pages/viewpage.action?pageId=32015004):
- python-virtualenv
- docker.io
- git

Please note the next two points depending on the GNU/Linux distributions and
the network settings:
- SELinux: you may have to add -\-system-site-packages when creating the
  virtualenv ("Aborting, target uses selinux but python bindings
  (libselinux-python) aren't installed!")
- Proxy: you may set your proxy in env for Ansible and in systemd for Docker
  https://docs.docker.com/config/daemon/systemd/#httphttps-proxy

<a name="available-rc"></a>
## Available Programs
* [RC1 - Openstack Based](RC1)
* [RC2 - Kubernetes Based](RC2)
