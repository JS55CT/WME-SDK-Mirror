---
title: SDK.MapComments class
source: classes/index.SDK.MapComments.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MapComments

```typescript
addComment (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â body: string ;
  Â Â Â Â Â Â Â Â endDate: number ;
  Â Â Â Â Â Â Â Â geometry: Point | Polygon ;
  Â Â Â Â Â Â Â Â subject: string ;
  Â Â Â Â } ,
  ) : MapComment
```
Methods for dealing with MapComments.
## Methods
### `addComment`

```typescript
addComment (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â body: string ;
  Â Â Â Â Â Â Â Â endDate: number ;
  Â Â Â Â Â Â Â Â geometry: Point | Polygon ;
  Â Â Â Â Â Â Â Â subject: string ;
  Â Â Â Â } ,
  ) : MapComment
```
the created map comment.
### `getAll`

```typescript
getAll () : MapComment []
```
an array of all the map comments in the WME data model
### `getById`

```typescript
getById ( args: { mapCommentId: string } ) : null | MapComment
```
map comment with id, or null if not found in the WME data model
### `updateComment`

```typescript
updateComment (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â body ?: string ;
  Â Â Â Â Â Â Â Â endDate ?: null | number ;
  Â Â Â Â Â Â Â Â geometry ?: Point | Polygon ;
  Â Â Â Â Â Â Â Â mapCommentId: string ;
  Â Â Â Â Â Â Â Â subject ?: string ;
  Â Â Â Â } ,
  ) : MapComment
```
the updated map comment.
