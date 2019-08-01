### Logistics
* [Meeting times.](#meeting_times)
* [How to contribute.](#how_to_contribute)
* [Approval process.](#approval_process)

<a name="meeeting_times"></a>
## Meeting times

### Master meeting

TBA.

### Reference Model

| Chapter | Meeting Time |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Chapter 1 - Introduction | TBA. |
| Chapter 2 - VNF requirements and analysis | TBA.|
| Chapter 3 - Modelling | TBA. |
| Chapter 4 - Infrastructure Abstraction | TBA |
| Chapter 5 - Featureset and Requirements from Infrastructure | TBA |
| Chapter 6 - External Interfaces | TBA |
| Chapter 7 - Security Guidelines | TBA |
| Chapter 8 - Compliance and Verification | TBA |
| Chapter 9 - Life Cycle Management | TBA |
| Chapter 10 - GAPS | TBA |

### Reference Architecture

will be posted here soon.

### Upcoming F2F 
Will be announced soon.

### Previous F2F
July 23rd - July 25th
Orange Gardens
44 avenue de la République
Châtillon, Paris

Wiki: https://wiki.lfnetworking.org/display/LN/July+2019+CNTT+Face+to+Face+Working+Session

<a name="how_to_contribute"></a>
## How to contribute

**Any contribution content should align with CNTT [principles](../doc/ref_model/chapters/chapter01.md#1.4) and [Terminologies](../doc/ref_model/chapters/chapter01.md#1.3).**

if you would like to contribute to CNTT work, please follow these steps:

1. Create an issue describing your contribution in details and assign it to the Chapter Lead.
    - if your issue touches more than one Chapter, please create multiple ones for each chapter it impacts.
1. Discuss your issue with the Chapter Lead during the Chapter meeting. (or by Chat in Github).
1. Get The issue assigned to you and get asked by the Chapter lead to create a PR.
    - This is to make sure that there is not any existing PR addressing the same issue.
    - This is also make sure dependencies with other chapter or between RM and RA are spotted and addressed.
    - An issue might get assigned to someone else.
1. Create PR for your proposed changes/additions.
    - Pull Requests should clearly specify the Chapter and the section number(s) in the title.
    - Please use also the description field to clarify the nature of your contribution. (and link it to the issue this relates to).
    - Address and resolve any comments/suggestions you receive by the community.

For **help** in how to create an issue or Pull Request, or with Markdown language, please refer to GitHub [documentation](https://guides.github.com).


<a name="approval_process"></a>
## Approval process

Pull Requests will be approved in two stages:

- **Stage 1 - By Chapter Leads:** The Chapter Lead need to approve your PR before it is considered to be merged with the **master**. this can be done through different ways:
  - **Prompt Approval**
    - This can be requested/hinted by you by labelling it as **"minor"**
    - Pull Requests that are introducing editorial fixes and/or very minor changes **can** be approved by chapter leads without discussion in meetings.
      - Best Effort Judgement will be made on this by the chapter lead.
      - Pull Requests approved this way can be **re-opened/reversed** if proved to be controversial.
  - **Online Approval** within 48 hours of PR creation provided that:
    - It does not conflict with CNTT principles or uses conflicting terminology.
    - It does not suggest fundamental changes or majour addition/modification.
    - All comments and questions on the pull request has been addressed.
    - It has passed the cool off period of **48 hours** where there has been no active discussions or objections to approve it.
    - it is up to the Chapter lead to decide Whether to approve a PR online (if passed above criteria) or defer it to more discussion during weekly meetings.
  - **Approvals during Weekly meetings**:
    - For those Pull requests that require further discussion will be discussed/approved during weekly meetings.
- **Stage 2 - During Master meetings:** PRs that are approved by Chapter Leads will be approved and merged during weekly master meeting.
  - This is to make sure dependencies are spotted and addressed between chapters or between Reference Model and Reference Architecture.
  - PRs that has been approved by their Chapter leads **can** be approved and merged into master promptly if considered minor.