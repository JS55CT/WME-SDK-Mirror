---
title: SDK.MapProblem interface
source: interfaces/index.SDK.MapProblem.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapProblem

```typescript
interface MapProblem {
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: string ;
  Â Â Â Â isEditable: boolean ;
  Â Â Â Â isOpen: boolean ;
  Â Â Â Â isRead: boolean ;
  Â Â Â Â isStarred: boolean ;
  Â Â Â Â problemType: MapProblemType ;
  Â Â Â Â resolvedOn: null | number ;
  Â Â Â Â severity: IssueSeverity ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: string
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
### `problemType`

```typescript
problemType: MapProblemType
```
### `resolvedOn`

```typescript
resolvedOn: null | number
```
### `severity`

```typescript
severity: IssueSeverity
```
