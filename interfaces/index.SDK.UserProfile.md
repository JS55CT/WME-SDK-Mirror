---
title: SDK.UserProfile interface
source: interfaces/index.SDK.UserProfile.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserProfile

```typescript
interface UserProfile {
  Â Â Â Â dailyEditCount: number [] ;
  Â Â Â Â editCountByType: {
  Â Â Â Â Â Â Â Â mapProblems: number ;
  Â Â Â Â Â Â Â Â placeUpdateRequests: number ;
  Â Â Â Â Â Â Â Â segmentHouseNumbers: number ;
  Â Â Â Â Â Â Â Â segments: number ;
  Â Â Â Â Â Â Â Â updateRequests: number ;
  Â Â Â Â Â Â Â Â venues: number ;
  Â Â Â Â } ;
  Â Â Â Â totalEditCount: number ;
}
```
## Properties
### `dailyEditCount`

```typescript
dailyEditCount: number []
```
### `editCountByType`

```typescript
editCountByType: {
  Â Â Â Â mapProblems: number ;
  Â Â Â Â placeUpdateRequests: number ;
  Â Â Â Â segmentHouseNumbers: number ;
  Â Â Â Â segments: number ;
  Â Â Â Â updateRequests: number ;
  Â Â Â Â venues: number ;
}
```
### `totalEditCount`

```typescript
totalEditCount: number
```
