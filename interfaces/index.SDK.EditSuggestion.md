---
title: SDK.EditSuggestion interface
source: interfaces/index.SDK.EditSuggestion.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface EditSuggestion

```typescript
interface EditSuggestion {
  Â Â Â Â bbox: BBox ;
  Â Â Â Â id: string ;
  Â Â Â Â isRead: boolean ;
  Â Â Â Â isStarred: boolean ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â source: EditSuggestionSource ;
  Â Â Â Â status: EditSuggestionStatus ;
  Â Â Â Â suggestions: Suggestion [] ;
}
```
Represents an edit suggestion, potentially containing multiple individual suggestions.
## Properties
### `bbox`

```typescript
bbox: BBox
```
### `id`

```typescript
id: string
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `source`

```typescript
source: EditSuggestionSource
```
### `status`

```typescript
status: EditSuggestionStatus
```
### `suggestions`

```typescript
suggestions: Suggestion []
```
