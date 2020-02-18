# Common NFVI Telco Taskforce Technical Release Process

## Table of Contents
* [Scope](#scope)
* [Release Model](#releasemodel)
* [Roadmap](#roadmap)
* [Events](#events)
* [Release Sign-off](#signoff)


<a name="scope"></a>
## Scope

The scope of this document is to define the release management and its process for planning, scheduling and controlling the build, in addition to proof reading and release deployment. This document defines the release model by organising the git branches and managing the code and other artefacts efficiently in well-structured format.
It should be considered a living document until it is agreed and signed by all the parties.

<a name="releasemodel"></a>
## Release Model

As a guiding principle, all the development occurs in “Master” branch. All the contribution for the milestone (especially M3) goes into ”Master”. After M4 (Proof Reading), at one point in the release candidate (RC) (for now maintain RC0) for Baldy and based on experience we shall increase or limit what get into the final release. To make this happen, branch out from “Master”, create a delivery branch (“Baldy”,”Hallasan”, “Baraque”, etc). Developers can continue their next release branch work in “Master”. At the end of each release, artifacts are “tagged” in GitHub according to the guideline and principles defined.

To deliver a hot fix (also known as patch) into the latest release, simply apply the hot fix in the delivery branch and tag it (4.0.1-Baldy). Once the hot fix is delivered, cherry pick technique will be applied to carry over the changes into the current release. As shown in the below diagram.

<p align="center"><img src="./figure/proposedmodel.png" alt="Proposed Model" title="Proposed Release Model" width="80%"/></p>
<p align="center"><b>Figure 1:</b> Proposed Release Model</p>

During the development cycle when working with release branches, developers or architects should open up a “pull request” in GitHub so that team members can see what you are preparing to release.

<a name="roadmap"></a>
## Roadmap

The table below captured the list of events, long holidays only, release plan and sign off with corresponding dates. The release plan consists of all the milestones associated with the release candidate (RC).

<p align="center"><img src="./figure/proposeddate.png" alt="Baldy Roadmap" title="Baldy Roadmap" width="80%"/></p>
<p align="center"><b>Figure 1:</b> Baldy Roadmap</p>

<a name="events"></a>
## Events

The list of events for the technical F2F planning captured from LGN events. <br>
•	ONES NA 2020 (Los Angeles, California) - April 20 & 21. Technical meetings April 22 & 23rd. <br>
•	LFN DDF (Seoul, South Korea) - June 1-4. <br>
•	ONES Europe 2020 (Antwerp, Belgium) - September 29 & 30. Technical meetings October 1 & 2.

<a name="signoff"></a>
## Release Sign-off

|   Name and Title of Approver   |   Decision       |    Reason for Rejection      |     Date     |
|--------------------------------|------------------|------------------------------|--------------|
|                                |                  |      &#9744; Approved <br> &#9744; Rejected  |              |
|                                |                  |      &#9744; Approved <br> &#9744; Rejected  |              |
|                                |                  |      &#9744; Approved <br> &#9744; Rejected  |              |

