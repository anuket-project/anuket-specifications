Appendix A - Guidelines For Application Vendors
===============================================

Goals
-----

This Appendix has two goals:

1. Provide guidance to VNF or more generally Application vendors on how to consume CNTT Reference Model and Architectures
2. Provide usable definitions of maturity levels for VNF software architecture between Physical-to-Virtual migration and “Cloud Native”.

The goal is not to be prescriptive on how to re-architect existing or architect new applications but rather staying within scope of focusing on interface and interaction between applications and platform.

Intro and Terminology
---------------------

Taking advantage of RM and RA environments with common capabilities, applications can be developed and deployed more rapidly, providing more service agility and easier operations. The extent to which this can be achieved will depend on levels of decoupling between application and infrastructure or platform underneath the application:

**1. Infrastructure**:

-  a. Application functionality or application control requires infrastructure components beyond RM profiles or infrastructure configuration changes beyond RA exposed APIs. Generally, such an application is tightly coupled with the infrastructure which results in an Appliance deployment model.
-  b. Application control using RA APIs finds node (already configured in support of the profiles) with required infrastructure component(s), and in that node using RA APIs configures infrastructure components that make application work. Example is application that to achieve latency requirements needs certain acceleration adapter available in RM profile and is exposed through RA APIs.
-  c. Application control using RA APIs finds node (already configured in support of the profiles) with optional infrastructure component(s), and in that node using RA APIs configures infrastructure component(s) that make application work better (like more performant) than without that infrastructure component. Example is application that would have better TCO with certain acceleration adapter but can also work without it.
-  d. Application control using RA APIs finds general profile node without any specific infrastructure component.

**2. Platform Services**

-  a. Application functionality or application control can work only with its own components instead of using RA-defined Platform Services.
-  b. With custom integration effort, application can be made to use RA-defined Platform Services.
-  c. Application is designed and can be configured for running with RA-defined Platform Services.

**3. Application Resiliency**

-  a. Application was designed and tested to run only on Carrier Grade platform with predictable infrastructure availability and performance.
-  b. Application was designed and tested for full failures of infrastructure HW and SW components, but not for infrastructure impairment as the Application still needs predictable infrastructure performance (like CPU cycles and network latencies).
-  c. Application was designed to run on shared Cloud platforms and tested for resilience to infrastructure impairments.

Relevant for sizing infrastructure and application operations (which often is another telco organizational unit or external 3rd party) is also how much is application decomposed from:

**4. Other application functionality** (decomposition and manageability for scaling, availability and upgrades):

-  a. Application consists of huge monolithic components including algorithms that have different scaling (for example depending on type of traffic) and/or availability requirements.
-  b. Application consists of smaller tightly coupled components.
-  c. Decomposed application with loosely- or decoupled components.
-  d. Availability like N+K or 1+1 is defined during application design and not configurable at deployment time.
-  e. Mutable or immutable instances of application components.

VNF Design Guidelines
---------------------

A number of software design guidelines (industry best practices) have been developed over the years including micro-services, cohesion and coupling.
In addition to the industry best-practices, there are additonal guidelines and requirements specified by ONAP in 
"`VNF or PNF Requirements Documentation <https://docs.onap.org/projects/onap-vnfrqts-requirements/en/istanbul/>`__." This section
does not supplant these well-known guidelines and practices. The content here only draws attention to some other design consideration that VNF
Developers need to incorporate in their practices. Please note that some of these guidelines may be incorporated by operators in their contracts with
VNF Vendors.

These guidelines are written in an informal style and any resemblance to requirements is incidental. The VNF Developer **should** ensure that their
software and the resultant VNF image:

1. does not contain malicious code (e.g., malware, logic bombs, etc.).
2. does not contain code such as daemons that exposes them to risk.
3. does not contain clear text secrets.
4. are only created with content and files from trusted sources.
5. are only packaged with files that have been found free of malware and vulnerabilities.

Additionally, in the design and implementation of their software, the VNF Developer **should** follow the guidance in the:

1. `CSA Security Guidance for Critical Areas of Focus in Cloud Computing (latest version) <https://cloudsecurityalliance.org>`__.
2. `OWASP Cheat Sheet Series (OCSS) <https://github.com/OWASP/CheatSheetSeries>`__ from the `Open Web Application Security Project <https://www.owasp.org>`__.
3. :ref:`ref_model/chapters/chapter07:Workload Security - Vendor Responsibility` section of the Reference Model.

The VNF Developer **should** ensure that their code is not vulnerable to the `OWASP Top Ten Security Risks <https://owasp.org/www-project-top-ten/>`__ created
by the `Open Web Application Security Project <https://www.owasp.org>`__.

Miscellaneous
-------------

.. _vnf-network-monitoring-capabilities---usecase:

VNF Network Monitoring Capabilities - UseCase.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Network Monitoring capabilities exposed by NFVI Platform are used for the passive observation of VNF-specific traffic traversing the NFVI when:

-  Performance issues and/or packet drops reported in VNF
-  Determining performance bottle necks at VNF level
-  Doing anomaly detection and network forensics

**Note:** It is responsibility of NFVI Platform to expose capability to create virtual interface having mirrored traffic from monitored VNF. This port can be attached to Monitoring VNF so that all traffic from Monitored VNF would be available for troubleshooting/debugging purpose.
