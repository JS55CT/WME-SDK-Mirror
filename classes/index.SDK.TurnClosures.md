---
title: SDK.TurnClosures class
source: classes/index.SDK.TurnClosures.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class TurnClosures

```typescript
addClosure (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â description: string ;
  Â Â Â Â Â Â Â Â endDate: number ;
  Â Â Â Â Â Â Â Â majorTrafficEventId ?: string ;
  Â Â Â Â Â Â Â Â startDate: number ;
  Â Â Â Â Â Â Â Â turnId: string ;
  Â Â Â Â } ,
  ) : TurnClosure
```
Methods for dealing with TurnClosures.
## Methods
### `addClosure`

```typescript
addClosure (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â description: string ;
  Â Â Â Â Â Â Â Â endDate: number ;
  Â Â Â Â Â Â Â Â majorTrafficEventId ?: string ;
  Â Â Â Â Â Â Â Â startDate: number ;
  Â Â Â Â Â Â Â Â turnId: string ;
  Â Â Â Â } ,
  ) : TurnClosure
```
The newly created turn closure object.
### `getAll`

```typescript
getAll () : TurnClosure []
```
an array of all the turn closures in the WME data model
### `getById`

```typescript
getById ( args: { turnClosureId: string } ) : null | TurnClosure
```
turn closure with id, or null if not found in the WME data model
