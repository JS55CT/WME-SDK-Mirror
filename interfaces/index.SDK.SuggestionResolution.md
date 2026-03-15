---
title: SDK.SuggestionResolution interface
source: interfaces/index.SDK.SuggestionResolution.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionResolution

```typescript
interface SuggestionResolution {
  Â Â Â Â createdBy: null | string ;
  Â Â Â Â createdOn: number ;
  Â Â Â Â rejectionReason: null | SuggestionResolutionRejectionReason ;
  Â Â Â Â resolution: SuggestionResolutionStatus ;
}
```
Represents the resolution details for a suggestion.
## Properties
### `createdBy`

```typescript
createdBy: null | string
```
### `createdOn`

```typescript
createdOn: number
```
### `rejectionReason`

```typescript
rejectionReason: null | SuggestionResolutionRejectionReason
```
### `resolution`

```typescript
resolution: SuggestionResolutionStatus
```
