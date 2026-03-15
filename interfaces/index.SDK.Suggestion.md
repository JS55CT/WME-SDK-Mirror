---
title: SDK.Suggestion interface
source: interfaces/index.SDK.Suggestion.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Suggestion

```typescript
interface Suggestion {
  Â Â Â Â createdOn: null | number ;
  Â Â Â Â edits: SuggestionEntityEdit [] ;
  Â Â Â Â id: string ;
  Â Â Â Â resolutionData: SuggestionResolution [] ;
}
```
Represents a suggestion for an edit.
## Properties
### `createdOn`

```typescript
createdOn: null | number
```
### `edits`

```typescript
edits: SuggestionEntityEdit []
```
### `id`

```typescript
id: string
```
### `resolutionData`

```typescript
resolutionData: SuggestionResolution []
```
