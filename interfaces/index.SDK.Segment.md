---
title: SDK.Segment interface
source: interfaces/index.SDK.Segment.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Segment

```typescript
interface Segment {
  Â Â Â Â allowNoDirection: boolean ;
  Â Â Â Â alternateStreetIds: number [] ;
  Â Â Â Â areFwdTurnsVerified: boolean ;
  Â Â Â Â areRevTurnsVerified: boolean ;
  Â Â Â Â elevationLevel: null | number ;
  Â Â Â Â flagAttributes: SegmentFlagAttributes ;
  Â Â Â Â fromLanesInfo: null | SegmentLanesInfo ;
  Â Â Â Â fromNodeId: null | number ;
  Â Â Â Â fromNodeLanesCount: number ;
  Â Â Â Â fwdSpeedLimit: null | number ;
  Â Â Â Â geometry: LineString ;
  Â Â Â Â hasClosures: boolean ;
  Â Â Â Â hasHouseNumbers: boolean ;
  Â Â Â Â hasRestrictions: boolean ;
  Â Â Â Â hasSeparator: boolean ;
  Â Â Â Â id: number ;
  Â Â Â Â isAtoB: boolean ;
  Â Â Â Â isBtoA: boolean ;
  Â Â Â Â isFwdSpeedLimitVerified: boolean ;
  Â Â Â Â isRevSpeedLimitVerified: boolean ;
  Â Â Â Â isTwoWay: boolean ;
  Â Â Â Â junctionId: null | number ;
  Â Â Â Â length: number ;
  Â Â Â Â lockRank: UserRank ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â primaryStreetId: null | number ;
  Â Â Â Â rank: UserRank ;
  Â Â Â Â restrictions: BaseRestriction [] ;
  Â Â Â Â revSpeedLimit: null | number ;
  Â Â Â Â roadType: RoadTypeId ;
  Â Â Â Â routingRoadType: null | 1 | 2 | 3 | 6 | 7 ;
  Â Â Â Â toLanesInfo: null | SegmentLanesInfo ;
  Â Â Â Â toNodeId: null | number ;
  Â Â Â Â toNodeLanesCount: number ;
}
```
## Properties
### `allowNoDirection`

```typescript
allowNoDirection: boolean
```
### `alternateStreetIds`

```typescript
alternateStreetIds: number []
```
### `areFwdTurnsVerified`

```typescript
areFwdTurnsVerified: boolean
```
### `areRevTurnsVerified`

```typescript
areRevTurnsVerified: boolean
```
### `elevationLevel`

```typescript
elevationLevel: null | number
```
### `flagAttributes`

```typescript
flagAttributes: SegmentFlagAttributes
```
### `fromLanesInfo`

```typescript
fromLanesInfo: null | SegmentLanesInfo
```
### `fromNodeId`

```typescript
fromNodeId: null | number
```
### `fromNodeLanesCount`

```typescript
fromNodeLanesCount: number
```
### `fwdSpeedLimit`

```typescript
fwdSpeedLimit: null | number
```
### `geometry`

```typescript
geometry: LineString
```
### `hasClosures`

```typescript
hasClosures: boolean
```
### `hasHouseNumbers`

```typescript
hasHouseNumbers: boolean
```
### `hasRestrictions`

```typescript
hasRestrictions: boolean
```
### `hasSeparator`

```typescript
hasSeparator: boolean
```
### `id`

```typescript
id: number
```
### `isAtoB`

```typescript
isAtoB: boolean
```
### `isBtoA`

```typescript
isBtoA: boolean
```
### `isFwdSpeedLimitVerified`

```typescript
isFwdSpeedLimitVerified: boolean
```
### `isRevSpeedLimitVerified`

```typescript
isRevSpeedLimitVerified: boolean
```
### `isTwoWay`

```typescript
isTwoWay: boolean
```
### `junctionId`

```typescript
junctionId: null | number
```
### `length`

```typescript
length: number
```
### `lockRank`

```typescript
lockRank: UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `primaryStreetId`

```typescript
primaryStreetId: null | number
```
### `rank`

```typescript
rank: UserRank
```
### `restrictions`

```typescript
restrictions: BaseRestriction []
```
### `revSpeedLimit`

```typescript
revSpeedLimit: null | number
```
### `roadType`

```typescript
roadType: RoadTypeId
```
### `routingRoadType`

```typescript
routingRoadType: null | 1 | 2 | 3 | 6 | 7
```
### `toLanesInfo`

```typescript
toLanesInfo: null | SegmentLanesInfo
```
### `toNodeId`

```typescript
toNodeId: null | number
```
### `toNodeLanesCount`

```typescript
toNodeLanesCount: number
```
