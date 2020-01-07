[<< Back](../)

# 9. NFVI Tests Traceability to TC Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [9.1 Introduction](#9.1)
* [9.2 RM/RA-1 Requirements](#9.2)
* [9.3 TC Mapping to Requirements](#9.3)

<a name="9.1"></a>
## 9.1 Introduction

Define, and describe the purpose of this chapter to be:

- Define RM/RA-1 Openstack requirements
- Map Framework to Requirements

<a name="9.2"></a>
## 9.2 RM/RA-1 Requirements

According to [RC1 Chapter04](/doc/ref_cert/lfn/chapters/chapter04.html) the
following test cases must pass as they are for CNTT NFVI
Conformance/Certification:

| container                               | test case                  | criteria |
|-----------------------------------------|----------------------------|:--------:|
| opnfv/functest-smoke-cntt:hunter        | neutron-tempest-plugin-api | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_cinder             | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_keystone           | PASS     |
| opnfv/functest-smoke-cntt:hunter        | rally_sanity               | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_full               | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_scenario           | PASS     |
| opnfv/functest-smoke-cntt:hunter        | tempest_slow               | PASS     |
| opnfv/functest-benchmarking-cntt:hunter | rally_full                 | PASS     |
| opnfv/functest-benchmarking-cntt:hunter | rally_jobs                 | PASS     |
| opnfv/functest-benchmarking-cntt:hunter | vmtp                       | PASS     |
| opnfv/functest-benchmarking-cntt:hunter | shaker                     | PASS     |
| opnfv/functest-vnf:hunter               | cloudify                   | PASS     |
| opnfv/functest-vnf:hunter               | cloudify_ims               | PASS     |
| opnfv/functest-vnf:hunter               | heat_ims                   | PASS     |
| opnfv/functest-vnf:hunter               | vyos_vrouter               | PASS     |
| opnfv/functest-vnf:hunter               | juju_epc                   | PASS     |

<a name="9.3"></a>
## 9.3 TC Mapping to Requirements

| test case                  | requirements                                                             |
|----------------------------|--------------------------------------------------------------------------|
| neutron-tempest-plugin-api | Neutron API testing                                                      |
| tempest_cinder             | Cinder API testing                                                       |
| tempest_keystone           | Keystone API testing                                                     |
| rally_sanity               | Keystone, Glance, Cinder, Swift, Neutron, Nova and Heat API testing      |
| tempest_full               | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| tempest_scenario           | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| tempest_slow               | Keystone, Glance, Cinder, Swift, Neutron and Nova API testing            |
| rally_full                 | Keystone, Glance, Cinder, Swift, Neutron, Nova and Heat API benchmarking |
| rally_jobs                 | Neutron API benchmarking                                                 |
| vmtp                       | Dataplane benchmarking                                                   |
| shaker                     | Dataplane benchmarking                                                   |
| cloudify                   | opensource VNF onboarding and testing                                    |
| cloudify_ims               | opensource VNF onboarding and testing                                    |
| heat_ims                   | opensource VNF onboarding and testing                                    |
| vyos_vrouter               | opensource VNF onboarding and testing                                    |
| juju_epc                   | opensource VNF onboarding and testing                                    |
