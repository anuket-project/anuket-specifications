# CNTT OpenStack Baseline Release Selection

This section specifies policies for the selection of the next CNTT OpenStack baseline release and the number of releases that CNTT shall support:
-	criteria for the triggering of the next baseline selection
-	criteria to use in choosing the next OpenStack release, and 
-	the number of OpenStack releases to be supported by CNTT

The selection of a new OpenStack baseline release will be associated with a new CNTT release and a whole set of documents (RA1, RI1 and RC1) with new versions.. Please note that while a new OpenStack release selection may only trigger updates to certain sections, all document releases will be complete and can be utilised on their own independent of previous releases.

## Triggering Events for next release selection
This section specifies events that may trigger the selection of the next OpenStack release.
-	Complete change in architecture: OpenStack, OpenStack Service or major API change of an OpenStack RA-1 required service
-	New OpenStack features, services or projects needed by CNTT workloads
-	Major Security Fix (not fixed through a patch; OpenStack or OS) that affect APIs
-	Current CNTT [OpenStack release]( https://releases.openstack.org/) entered “[Extended Maintenance]( https://docs.openstack.org/project-team-guide/stable-branches.html#maintenance-phases)” phase approximately 18 months ago

## OpenStack Release Selection Committee
On the occurrence of any of the triggering events, the TSC shall constitute an OpenStack Release Selection Committee composed of a maximum of 7 (seven) members representing both operators and vendors. These committee members shall be from active CNTT member organisations and meet the criteria specified for “[Voting Representatives]( https://github.com/cntt-n/CNTT/blob/master/doc/gov/chapters/chapter05.md#52-voting-representatives)”. 
The committee decisions shall be by consensus and no decision shall be made without at least 5 members agreeing.
The committee may agree by unanimous agreement to adjust the OpenStack Release Selection Criteria.

## OpenStack Release Selection Criteria
The OpenStack Release Selection Committee shall utilize the following criteria, and any other criteria that it unanimously agrees to, in selecting the next CNTT OpenStack baseline release:
-	The latest OpenStack release that was released approximately 6 months ago
    - The Committee may agree to relax or extend the 6 months period based on its knowledge of OpenStack releases
-	The OpenStack release should be supported by the OPNFV Installer (Airship)
-	Backward Compatibility: ensure API support
-	Consider OpenStack Distribution vendors and their extended support versions

## Deprecation of CNTT OpenStack Releases
CNTT shall support no more than 2 (two) OpenStack releases at any given time. Thus, on selection of a new CNTT OpenStack baseline release, an existing CNTT OpenStack release may be deprecated. The selection of new CNTT OpenStack release n, triggers the deprecation of the n-2 release. On the completion of the Reference Architecture for release n, the release n-2 will stand deprecated.
Please note that reference to releases in this subsection is to CNTT’s OpenStack release where Pike is release 1. 
