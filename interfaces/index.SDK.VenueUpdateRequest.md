---
title: SDK.VenueUpdateRequest interface
source: interfaces/index.SDK.VenueUpdateRequest.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueUpdateRequest

```typescript
interface VenueUpdateRequest {
  Â Â Â Â changedFields ?: ChangedField [] ;
  Â Â Â Â createdBy: null | string ;
  Â Â Â Â dateAdded: number ;
  Â Â Â Â id: null | string | number ;
  Â Â Â Â subject: PLACE_UPDATE_SUBJECT ;
  Â Â Â Â updateType: PlaceUpdateType ;
}
```
## Properties
### **Optional** `changedFields`

```typescript
changedFields ?: ChangedField []
```
### `createdBy`

```typescript
createdBy: null | string
```
### `dateAdded`

```typescript
dateAdded: number
```
### `id`

```typescript
id: null | string | number
```
### `subject`

```typescript
subject: PLACE_UPDATE_SUBJECT
```
### `updateType`

```typescript
updateType: PlaceUpdateType
```
