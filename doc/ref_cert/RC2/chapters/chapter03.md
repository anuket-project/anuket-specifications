[<< Back](../)

# 3. Kubernetes Testing Cookbook

## Table of Contents
* [3.1 Deploy your own conformance toolchain](#3.1)
* [3.2 Configure Kubernetes API testing](#3.2)
* [3.3 Run Kubernetes conformance suite](#3.3)

<a name="3.1"></a>
## 3.1 Deploy your own conformance toolchain

At the time of writing, the CI description file is hosted in Functest and only
runs the containers selected by CNTT RC2. It will be completed by the
next CNTT mandatory test cases and then a new CI description file will be
proposed in a shared tree.

[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting) only requires
internet access, GNU/Linux as Operating System and asks for a few
dependencies as described in
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

To deploy your own CI toolchain running CNTT Compliance:
```bash
virtualenv functest-kubernetes
. functest-kubernetes/bin/activate
pip install ansible
ansible-galaxy install collivier.xtesting
ansible-galaxy collection install ansible.posix community.general community.grafana community.kubernetes
git clone https://gerrit.opnfv.org/gerrit/functest-kubernetes functest-kubernetes-src
(cd functest-kubernetes-src && git checkout -b stable/leguer origin/stable/leguer)
ansible-playbook functest-kubernetes-src/ansible/site.cntt.yml
```

<a name="3.2"></a>
### 3.2 Configure Kubernetes API testing

Place the kubeconfig configuration file corresponding to the Kubernetes cluster
under test in the following location on the machine running the cookbook:

`/home/opnfv/functest-kubernetes/config`


<a name="3.3"></a>
### 3.3 Run Kubernetes conformance suite

Open http://127.0.0.1:8080/job/functest-kubernetes-leguer-daily/ in a web
browser, login as admin/admin and click on "Build with Parameters" (keep the
default values).

If the System under test (SUT) is CNTT compliant, a link to the full archive
containing all test results and artifacts will be printed in
functest-kubernetes-leguer-zip's console. Be free to download it and then to send
it to any reviewer committee.

To clean your working dir:
```bash
deactivate
rm -rf functest-kubernetes-src functest-kubernetes
```
