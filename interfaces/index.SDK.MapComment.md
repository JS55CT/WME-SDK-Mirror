---
title: SDK.MapComment interface
source: interfaces/index.SDK.MapComment.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapComment

```typescript
interface MapComment {
  Â Â Â Â body: string ;
  Â Â Â Â conversation: ConversationElement [] ;
  Â Â Â Â endDate: null | string ;
  Â Â Â Â geometry: Point | Polygon ;
  Â Â Â Â id: string ;
  Â Â Â Â isFollowing: boolean ;
  Â Â Â Â isPoint: boolean ;
  Â Â Â Â lockRank: UserRank ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â subject: string ;
}
```
## Properties
### `body`

```typescript
body: string
```
### `conversation`

```typescript
conversation: ConversationElement []
```
### `endDate`

```typescript
endDate: null | string
```
### `geometry`

```typescript
geometry: Point | Polygon
```
### `id`

```typescript
id: string
```
### `isFollowing`

```typescript
isFollowing: boolean
```
### `isPoint`

```typescript
isPoint: boolean
```
### `lockRank`

```typescript
lockRank: UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `subject`

```typescript
subject: string
```
