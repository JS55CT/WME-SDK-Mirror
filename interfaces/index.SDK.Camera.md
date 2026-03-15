---
title: SDK.Camera interface
source: interfaces/index.SDK.Camera.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Camera

```typescript
interface Camera {
  Â Â Â Â direction: null | RestrictionSegmentDirection ;
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: number ;
  Â Â Â Â lockRank: null | number ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â segmentId: null | number ;
  Â Â Â Â types: CameraType [] ;
}
```
## Properties
### `direction`

```typescript
direction: null | RestrictionSegmentDirection
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `lockRank`

```typescript
lockRank: null | number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentId`

```typescript
segmentId: null | number
```
### `types`

```typescript
types: CameraType []
```
