---
title: SDK.RoadClosure interface
source: interfaces/index.SDK.RoadClosure.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadClosure

```typescript
interface RoadClosure {
  Â Â Â Â description: null | string ;
  Â Â Â Â endDate: null | string ;
  Â Â Â Â id: string ;
  Â Â Â Â isForward: boolean ;
  Â Â Â Â isPermanent: boolean ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â segmentId: number ;
  Â Â Â Â startDate: null | string ;
  Â Â Â Â status: ClosureStatus ;
  Â Â Â Â trafficEventId: null | string ;
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
### `id`

```typescript
id: string
```
### `isForward`

```typescript
isForward: boolean
```
### `isPermanent`

```typescript
isPermanent: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentId`

```typescript
segmentId: number
```
### `startDate`

```typescript
startDate: null | string
```
### `status`

```typescript
status: ClosureStatus
```
### `trafficEventId`

```typescript
trafficEventId: null | string
```
