[<< Back](../)

# 2. Reference Implementation Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction](#21-introduction)
  * [2.1.1 Definitions](#211-definitions)
* [2.2 Reference Architecture Specification](#2.2)
* [2.3 Reference Implementation Requirements](#2.3)

## 2.1 Introduction

This chapter will use the requirements defined in the Kubernetes Reference
Architecture and only make additional entries in section [2.3](#2.3) if there
are additional requirements needed for this Reference Implementation.

## 2.1.1 Definitions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

## 2.2 Reference Architecture Specification

| RA2 Section | RA2 Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| RI2 Traceability |
|---|---|---|---|---|---|
|Kubernetes Nodes|`ra2.ch.001`|Huge Pages|Not required|It must be possible to enable Huge Pages (2048KiB and 1048576KiB) within the Kubernetes Node OS, exposing schedulable resources `hugepages-2Mi` and `hugepages-1Gi`.|_TBC_|
|||||||

## 2.3 Reference Implementation Requirements

| RI2 Ref # | Category | Sub-category | Description | RI2 Traceability |
|---|---|---|---|---|
||||||
