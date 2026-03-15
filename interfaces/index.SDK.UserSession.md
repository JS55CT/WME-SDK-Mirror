---
title: SDK.UserSession interface
source: interfaces/index.SDK.UserSession.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserSession

```typescript
interface UserSession {
  Â Â Â Â isAreaManager: boolean ;
  Â Â Â Â isCountryManager: boolean ;
  Â Â Â Â managedAreas: ManagedAreaShort [] ;
  Â Â Â Â rank: UserRank ;
  Â Â Â Â userName: string ;
}
```
## Properties
### `isAreaManager`

```typescript
isAreaManager: boolean
```
### `isCountryManager`

```typescript
isCountryManager: boolean
```
### `managedAreas`

```typescript
managedAreas: ManagedAreaShort []
```
### `rank`

```typescript
rank: UserRank
```
### `userName`

```typescript
userName: string
```
