---
title: SDK.TileLayerOptions interface
source: interfaces/index.SDK.TileLayerOptions.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TileLayerOptions

```typescript
interface TileLayerOptions {
  Â Â Â Â tileHeight: number ;
  Â Â Â Â tileWidth: number ;
  Â Â Â Â url: {
  Â Â Â Â Â Â Â Â fileName: string ;
  Â Â Â Â Â Â Â Â params ?: Record < string , unknown > ;
  Â Â Â Â Â Â Â Â servers: string [] ;
  Â Â Â Â } ;
}
```
#### Members
| Name | Type/Value | Tags |
|------|------------|------|
| fileName | string |  |
| params | string | Optional |
| servers | string |  |
## Properties
### `tileHeight`

```typescript
tileHeight: number
```
### `tileWidth`

```typescript
tileWidth: number
```
### `url`

```typescript
url: { fileName: string ; params ?: Record < string , unknown > ; servers: string [] }
```
