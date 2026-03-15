---
title: SDK.MapUpdateRequest interface
source: interfaces/index.SDK.MapUpdateRequest.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapUpdateRequest

```typescript
interface MapUpdateRequest {
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: number ;
  Â Â Â Â isEditable: boolean ;
  Â Â Â Â isOpen: boolean ;
  Â Â Â Â isRead: boolean ;
  Â Â Â Â isStarred: boolean ;
  Â Â Â Â reportedOn: number ;
  Â Â Â Â resolutionState: null | string ;
  Â Â Â Â resolvedOn: null | number ;
  Â Â Â Â severity: IssueSeverity ;
  Â Â Â Â source: UpdateRequestSource ;
  Â Â Â Â updateRequestType: UpdateRequestType ;
  Â Â Â Â userPreferences: UpdateRequestUserPreferences ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `isEditable`

```typescript
isEditable: boolean
```
### `isOpen`

```typescript
isOpen: boolean
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `reportedOn`

```typescript
reportedOn: number
```
### `resolutionState`

```typescript
resolutionState: null | string
```
### `resolvedOn`

```typescript
resolvedOn: null | number
```
### `severity`

```typescript
severity: IssueSeverity
```
### `source`

```typescript
source: UpdateRequestSource
```
### `updateRequestType`

```typescript
updateRequestType: UpdateRequestType
```
### `userPreferences`

```typescript
userPreferences: UpdateRequestUserPreferences
```
