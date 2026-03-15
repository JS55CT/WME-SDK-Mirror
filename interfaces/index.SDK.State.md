---
title: SDK.State interface
source: interfaces/index.SDK.State.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface State

```typescript
interface State {
  Â Â Â Â geometry: null | Polygon | MultiPolygon ;
  Â Â Â Â id: number ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â name: string ;
}
```
## Properties
### `geometry`

```typescript
geometry: null | Polygon | MultiPolygon
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
