[<< Back](https://cntt-n.github.io/CNTT/)
# Common NFVI Telco Taskforce Roadmap

## Table of Contents
 * [Overview](#1)
 * [Roadmap](#2)
   * [High Level Roadmap](#2.1)
   * [Detailed Roadmap](#2.2)
   * [Detailed Milestones](#2.3)
 * [Dependencies between various Workstreams ](#3)
 * [Dependencies with Industry Communities](#4)

<a name="1"></a>
## Overview
* The activities of the CNTT community are articulated around [Projects](#project), [Milestones](#2.3) and [Releases](#release).
* CNTT is embracing simultaneous delivery model, meaning that all contributing projects have to follow the cadence and intermediate milestones.
* CNTT is single-release vehicle for all projects.
* The CNTT current release plan is available [here](./release_notes/release_process.md).



<p align="center"><img src="./figures/Release Lifecycle.png" alt="scope" title="Milestones" width="100%"/></p>
<p align="center"><b>Figure 1:</b> Milestones</p>

**Definitions**

<a name="project"></a>
A project is:
  * Long term endeavour setup to deliver features across multiple releases as shown [here](./release_notes/)
  * Led by leads/co-leads, contributors and committers with expertise in the relevant areas
  * Scripted and documented in repositories
  
<a name="release"></a>
A Release is:
  * Short term endeavour setup to deliver a specific features/functionalities as shown [here](./release_notes/baldy.md).
  * An agreed common framework (template, criteria, best practice) for all projects
  * An unique release planning calendar with pre-defined milestones for each project
  * A vehicle to coordinate multiple projects and multiple type of projects (reference model and architecture, documentation, integration, packaging, deployment)
  
<a name="2"></a>
## Roadmap

<a name="2.1"></a>
### High Level Roadmap
<p align="center"><img src="./figures/cntt_roadmap.png" alt="scope" title="Roadmap" width="100%"/></p>
<p align="center"><b>Figure 1:</b> CNTT Technical Specification Roadmap</p>

<a name="2.2"></a>
### Detailed Roadmap
Please refer to individual [release plan](./release_notes/) and features for detailed roadmap.

<a name="2.3"></a>
### Detailed Milestones
| Review | Milestone | Description | Activities | Comments |
|--------|-----------|--------------|------------|---------|
| Kick-Off | M0 | The goal of the release Kick-Off is to open the innovation platform for the intent to participate in the CNTT release. Release Kick-Off review takes place for each releases. | Name the Release and create appropriate labels in GitHub. ||
| Planning & Scoping | | The goal of the Release Planning & Scoping is to capture the initial set of features and functionality that should be part of the release along with prioritisation. | <ul><li> Identity a list of features and functionality including from the backlog will be developed and documented as part of the current release. N.B. Feature/functionality, errors etc. are logged in GitHub as Issues.</li>  <li> Identify what is in or out of scope for the release. </li> <li> Escalate any issues to the TSC. </li></ul>| |
| Release Plan Review | M1 | The goal of the Release Planning review is to ensure the plan is complete, sufficient, and aligned with release milestones. All people resources are identified, documented and committed. | <ul><li> After the review cut-off date any major features & functionalities changes will be added to the backlog unless it is approved by the TSC to be added into the current scope of release. </li> <li> Bug fixes or any minor changes identified during the development will be allowed. </li> <li> For any other content changes to be approved by TSC. </ul></li>||
| Scope Changes | |  Feature/Functionality changes to be part of current Release |<ul><li> Feature/Functionality changes (in Github) for the current scope of release. </li> <li> Project leads ensure feature/functionality are correctly labelled, mapped to the corresponding project and milestone, etc.</ul></li>  | |
| Scope Freeze | M2 | The goal of the Scope Freeze is to mark the end of adding new features/functionalites in the Release. | <ul><li> All the project leads authorise the issues are correctly labelled, mapped to the corresponding project and milestone, etc., </li> <li> Features/Functionalities changes (except for bugs fixes) identified post-freeze will be added to the Backlog. </li> <li>Exceptions to the above need TSC approval. </ul></li> | |
| Feature/Functionality/Content Development | | The goal is to ensure that changes to features and functionalities are captured and all content necessary for the In-Scope features & functionalities will be developed as part of the release scope. |<ul><li> Update Feature/Functionality as we evolve. </li> <li> Develop / Update the contents for the release in-scope listed features & functionalities </ul></li> | |
| Content Freeze | M3 | The goal of the Content Freeze is to mark the end of the features documented and provided the resolution for all impacting defects. After Content Freeze, there will be no new features/functionalities are allowed into the current release. Only the critical fixes are allowed. | <ul><li> All the project leads review the document and ensure all the planned features are documented and fixes are available before end of the Content Freeze. </li> <li> Uncompleted features/functionality will be added to the Backlog. After discussed and approved by the TSC. </ul></li> | |
| Content Review | | The goal is to carefully review and validate the contents and check for errors in the document. | <ul><li>  Validate content is within Release Scope and is technically correct. </li><li> Check document for grammatical errors, extraneous items, etc. </li> <li> Close all In-Scope & reviewed projects/issues and move all others to Backlog after discussed and approved by the TSC. <ul><li> | |
| Content Review Freeze | M4 | The goal of the Proof Reading is to carefully review and validate the contents and check for errors in the document before it is released. This is the final and last stage of the milestone. This is the release content completion milestone.| All Projects are closed or else are marked Backlog. Discuss with TSC for any exceptional approval. | |
| Release Packaging | | The goal is to package the precise and reviewed document versions into a new release branch. | Create new Release Branch after content review ends. | |
| Release Candidate | RC0 | The goal of the Release Candidate is to ensure the documentations are properly aligned, fully reviewed in the new release branch. | Prioritise the required fixes and address them. If there are any critical fixes required then the fixes will be provided and it will be tagged with minor release. (Eg. Baldy 4.0.1) | |
| Release Sign-Off | | The goal of the Release Sign-Off review is to ensure all the projects are successfully passed all the review. All the committed deliverables are available and passed the quality criteria. | | |

<p align="center"><b>Table 1:</b> Detailed Milestones</p>

<a name="3"></a>
## Dependencies between various Workstreams

<a name="4"></a>
## Dependencies with Industry Communities
