---
title: SDK.MajorTrafficEvent interface
source: interfaces/index.SDK.MajorTrafficEvent.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MajorTrafficEvent

```typescript
interface MajorTrafficEvent {
  Â Â Â Â category: null | MajorTrafficEventCategory ;
  Â Â Â Â cityId: null | number ;
  Â Â Â Â endDate: null | string ;
  Â Â Â Â id: string ;
  Â Â Â Â isPublished: boolean ;
  Â Â Â Â isReady: boolean ;
  Â Â Â Â lockRank: null | UserRank ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â names: LocalizedString [] ;
  Â Â Â Â startDate: null | string ;
}
```
## Properties
### `category`

```typescript
category: null | MajorTrafficEventCategory
```
### `cityId`

```typescript
cityId: null | number
```
### `endDate`

```typescript
endDate: null | string
```
### `id`

```typescript
id: string
```
### `isPublished`

```typescript
isPublished: boolean
```
### `isReady`

```typescript
isReady: boolean
```
### `lockRank`

```typescript
lockRank: null | UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `names`

```typescript
names: LocalizedString []
```
### `startDate`

```typescript
startDate: null | string
```
