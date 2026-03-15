---
title: SDK.EditSuggestionChange interface
source: interfaces/index.SDK.EditSuggestionChange.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface EditSuggestionChange

```typescript
interface EditSuggestionChange {
  Â Â Â Â attributeChanges: SuggestionAttributeChange < unknown > [] ;
  Â Â Â Â createdOn: null | number ;
  Â Â Â Â rejectionReason: null | SuggestionResolutionRejectionReason ;
  Â Â Â Â status: SuggestionResolutionStatus ;
  Â Â Â Â suggestionId: string ;
}
```
Represents a change suggested in an edit suggestion, containing an attribute change per each changed attribute.
## Properties
### `attributeChanges`

```typescript
attributeChanges: SuggestionAttributeChange < unknown > []
```
### `createdOn`

```typescript
createdOn: null | number
```
### `rejectionReason`

```typescript
rejectionReason: null | SuggestionResolutionRejectionReason
```
### `status`

```typescript
status: SuggestionResolutionStatus
```
### `suggestionId`

```typescript
suggestionId: string
```
