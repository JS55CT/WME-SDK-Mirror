---
title: SDK.RoadClosures class
source: classes/index.SDK.RoadClosures.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class RoadClosures

```typescript
addClosure (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â description: string ;
  Â Â Â Â Â Â Â Â endDate: number ;
  Â Â Â Â Â Â Â Â fromNodeClosed: boolean ;
  Â Â Â Â Â Â Â Â isForward: boolean ;
  Â Â Â Â Â Â Â Â isPermanent: boolean ;
  Â Â Â Â Â Â Â Â segmentId: number ;
  Â Â Â Â Â Â Â Â startDate: number ;
  Â Â Â Â Â Â Â Â trafficEventId: null | string ;
  Â Â Â Â } ,
  ) : RoadClosure
```
Methods for dealing with RoadClosures.
## Methods
### `addClosure`

```typescript
addClosure (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â description: string ;
  Â Â Â Â Â Â Â Â endDate: number ;
  Â Â Â Â Â Â Â Â fromNodeClosed: boolean ;
  Â Â Â Â Â Â Â Â isForward: boolean ;
  Â Â Â Â Â Â Â Â isPermanent: boolean ;
  Â Â Â Â Â Â Â Â segmentId: number ;
  Â Â Â Â Â Â Â Â startDate: number ;
  Â Â Â Â Â Â Â Â trafficEventId: null | string ;
  Â Â Â Â } ,
  ) : RoadClosure
```
the created road closure.
### `getAll`

```typescript
getAll () : RoadClosure []
```
an array of all the road closures in the WME data model
### `getById`

```typescript
getById ( args: { roadClosureId: string } ) : null | RoadClosure
```
road closure with id, or null if not found in the WME data model
