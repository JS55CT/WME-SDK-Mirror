---
title: SDK.TurnClosure interface
source: interfaces/index.SDK.TurnClosure.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnClosure

```typescript
interface TurnClosure {
  Â Â Â Â description: null | string ;
  Â Â Â Â endDate: null | string ;
  Â Â Â Â fromSegmentId: number ;
  Â Â Â Â id: string ;
  Â Â Â Â majorTrafficEventId: null | string ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â startDate: null | string ;
  Â Â Â Â status: ClosureStatus ;
  Â Â Â Â toSegmentId: number ;
}
```
## Properties
### `description`

```typescript
description: null | string
```
### `endDate`

```typescript
endDate: null | string
```
### `fromSegmentId`

```typescript
fromSegmentId: number
```
### `id`

```typescript
id: string
```
### `majorTrafficEventId`

```typescript
majorTrafficEventId: null | string
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `startDate`

```typescript
startDate: null | string
```
### `status`

```typescript
status: ClosureStatus
```
### `toSegmentId`

```typescript
toSegmentId: number
```
