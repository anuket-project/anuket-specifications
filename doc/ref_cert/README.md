[<< Back](../)

# CNTT Reference Conformance

All CNTT conformance suites fulfill the following test case integration
requirements to guarantee a smooth overall integration, the same end user
actions and a unique test result format (e.g. OPNFV test result database)
needed by the end users and the test case result verification programs (e.g.
[OVP](https://www.opnfv.org/verification)). Historically, these rules were
agreed by RC1 team and have been applied since
[CNTT Snezka](https://github.com/cntt-n/CNTT/wiki/Snezka). The new RC2 stream
asks to move them in this common place applicable to all CNTT conformance
suites.

<a name="ri-rc-toolchaings"></a>
## CNTT RI and RC toolchains

[OPNFV](https://www.opnfv.org/) has built a complete CI/CD toolchain
for continuously deploying and testing cloud infrastructure.

As for all OPNFV installer projects,
[Jenkins](https://build.opnfv.org/ci/view/cntt/) triggers scenario deployments,
runs the OPNFV gating test cases and then publishes all
test results in the
[centralized test database](https://docs.opnfv.org/en/stable-hunter/_images/OPNFV_testing_working_group.png)
and all artifacts (reports, logs, etc.) to
[an S3 compatible storage service](http://artifacts.opnfv.org/).

The CNTT verification and conformance processes will leverage existing OPNFV
testing knowledge (projects) and experience (history) and then will conform
to the overall toolchain design already in-place. The RC toolchain only
requires for the local deployment of the components instead of leveraging
the common OPNFV centralized services. But the interfaces remain unchanged
mainly leveraging jenkins jobs, the common test case execution, the test
result database and the S3 protocol to publish the artifacts. It's worth
mentioning that dumping all results and logs required by conformance is already
in place in CIRV (see
[cntt-latest-zip](https://build.opnfv.org/ci/job/cntt-latest-zip/)) and
Functest daily jobs (see
[functest-hunter-zip](https://build.opnfv.org/ci/job/functest-hunter-zip/3/console))

It should be noted that
[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) supports both
centralized and distributed deployment models as described below. It has
deployed the full toolchain in one small virtual machine to verify ONAP Openlab
via Functest.

<a name="testing-integration-requirements"></a>
## Test case integration requirements

To reach all goals (verification, compliance and conformance) expected by
CNTT, all test cases must be delivered as
[Docker containers](https://www.docker.com/) and meet the requirements to
simplify the CI toolchain setups:
- the common test case execution
- the unified way to manage all the interactions with the CI/CD components and
  with third-parties (e.g. dump all test case logs and results for
  conformance)

For their parts, the Docker containers simply enforce that the test cases are
delivered with all runtime dependencies. Then it prevents lots of manual
operations when configuring the server running the test cases and prevent
conflicts between all test case dependencies.

It's worth mentioning that current
[test cases selected by CNTT](./chapter03.md)
already leverages on [Xtesting](https://xtesting.readthedocs.io/en/latest/)
which is a simple framework to assemble sparse test cases and to accelerate the
adoption of CI/CD best practices. By managing all the interactions with the
CI/CD components (test scheduler, test results database, artifact repository),
it allows the developer to work only on the test suites without diving into
CI/CD integration. Even more, it brings the capability to run heterogeneous
test cases in the same CI toolchains thanks to a few low constraints
[quickly achievable](https://www.sdxcentral.com/articles/news/opnfvs-6th-release-brings-testing-capabilities-that-orange-is-already-using/2018/05/).

Following the design in use, the Docker containers proposed by the test
projects must also embed
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
In addition of this teaching capability needed by the Network Automation
it supports multiple components such as Jenkins and Gitlab CI (test
schedulers) and
[multiple deployment models](https://lists.opnfv.org/g/opnfv-tsc/message/5702)
such as all-in-one or centralized services.

[Xtesting](https://xtesting.readthedocs.io/en/latest/) and
[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) combined meet the
CNTT requirements about verification, validation, compliance and conformance:
- smoothly assemble multiple heterogeneous test cases
- generate the Jenkins jobs in
  [OPNFV Releng](https://git.opnfv.org/releng/tree/jjb/airship/cntt.yaml) to
  verify CNTT RI
- deploy local CI/CD toolchains everywhere to check compliance with CNTT
- [dump all test case results and logs](http://artifacts.opnfv.org/functest/9ID39XK47PMZ.zip)
  for third-party conformance review

Here are a couple of playbooks publically available:
- [Xtesting samples](https://git.opnfv.org/functest-xtesting/plain/ansible/site.yml?h=stable/kali)
- [OpenStack verification](https://git.opnfv.org/functest/plain/ansible/site.yml?h=stable/kali)
- [CNTT RC1](https://git.opnfv.org/functest/plain/ansible/site.cntt.yml?h=stable/hunter)
- [Kubernetes verification](https://git.opnfv.org/functest-kubernetes/plain/ansible/site.yml?h=stable/kali)

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

<a name="available-cr"></a>
## Available Programs
* [RC1 - LFN Based](lfn)
* [RC2 - Kubernetes Based](RC2)
