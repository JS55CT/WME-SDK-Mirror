---
title: SDK.Segments class
source: classes/index.SDK.Segments.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Segments

```typescript
addAlternateStreet ( args: { segmentIds: number [] ; streetId: number } ) : void
```
Methods for dealing with Segments.
## Methods
### `addAlternateStreet`

```typescript
addAlternateStreet ( args: { segmentIds: number [] ; streetId: number } ) : void
```

### `addIntersection`

```typescript
addIntersection (
  Â Â Â Â args: { segmentIds: [ number , number ] } ,
  ) : { sourceSplits: [ number , number ] ; targetSplits: [ number , number ] }
```
the ids of the four newly created segments.
### `addSegment`

```typescript
addSegment ( args: { geometry: LineString ; roadType: RoadTypeId } ) : number
```
segment id of the new segment
### `createRoundabout`

```typescript
createRoundabout ( args: { center: LonLat ; rx: number ; ry: number } ) : number []
```
ids of roundabout segments
### `deleteSegment`

```typescript
deleteSegment ( args: { segmentId: number } ) : void
```

### `findSegment`

```typescript
findSegment ( args: { segmentId: number } ) : Promise < Segment >
```
A promise that resolves to the found segment.
### `getAddress`

```typescript
getAddress ( args: { segmentId: number } ) : SegmentAddress
```
an address of the segment with provided id.
### `getAll`

```typescript
getAll () : Segment []
```
an array of all the segments in the WME data model
### `getById`

```typescript
getById ( args: { segmentId: number } ) : null | Segment
```
segment with id, or null if not found in the WME data model
### `getConnectedSegments`

```typescript
getConnectedSegments (
  Â Â Â Â args: { reverseDirection ?: boolean ; segmentId: number } ,
  ) : Segment []
```
connected segments in specified direction
### `getReversedSegments`

```typescript
getReversedSegments ( args: { segmentIds: number [] } ) : Segment []
```
An array of segments that are considered reversed within the provided list.
### `getRoadTypes`

```typescript
getRoadTypes () : RoadType []
```
all possible road types and their localised names.
### `getVirtualNodes`

```typescript
getVirtualNodes ( args: { segmentId: number } ) : Node []
```
array of nodes virtually connected to the specified segment.
### `getWKTGeometry`

```typescript
getWKTGeometry ( args: { segmentId: number } ) : string
```
the WKT string representation of the segment's geometry
### `hasPermissions`

```typescript
hasPermissions (
  Â Â Â Â args: { permission ?: SegmentPermission ; segmentId: number } ,
  ) : boolean
```
whether the current user has a permission for this segment or not.
### `isContainedInBigJunction`

```typescript
isContainedInBigJunction ( args: { segmentId: number } ) : boolean
```
true if the segment is completely within a big junction
### `isRoadTypeDrivable`

```typescript
isRoadTypeDrivable ( args: { roadType: RoadTypeId } ) : boolean
```
boolean indicating whether specified road type is drivable.
### `isTollSegment`

```typescript
isTollSegment ( args: { segmentId: number } ) : boolean
```
true if the segment is a toll road or has a toll-free restriction
### `mergeSegments`

```typescript
mergeSegments ( args: { segmentIds: number [] } ) : void
```

### `splitSegment`

```typescript
splitSegment ( args: { segmentId: number ; splitPoint: Point } ) : [ number , number ]
```
two segments the original segment was split into.
### `updateAddress`

```typescript
updateAddress (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â alternateStreetIds ?: number [] ;
  Â Â Â Â Â Â Â Â primaryStreetId ?: number ;
  Â Â Â Â Â Â Â Â segmentId: number ;
  Â Â Â Â } ,
  ) : void
```

### `updateSegment`

```typescript
updateSegment (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â direction ?: SegmentDirection ;
  Â Â Â Â Â Â Â Â elevationLevel ?: number ;
  Â Â Â Â Â Â Â Â flagAttributes ?: Pick <
  Â Â Â Â Â Â Â Â Â Â Â Â SegmentFlagAttributes ,
  Â Â Â Â Â Â Â Â Â Â Â Â "tunnel"
  Â Â Â Â Â Â Â Â Â Â Â Â | "unpaved"
  Â Â Â Â Â Â Â Â Â Â Â Â | "headlights"
  Â Â Â Â Â Â Â Â Â Â Â Â | "nearbyHOV" ,
  Â Â Â Â Â Â Â Â > ;
  Â Â Â Â Â Â Â Â fromLanesInfo ?: null | SegmentLanesInfo ;
  Â Â Â Â Â Â Â Â fwdSpeedLimit ?: null | number ;
  Â Â Â Â Â Â Â Â geometry ?: LineString ;
  Â Â Â Â Â Â Â Â hasToll ?: boolean ;
  Â Â Â Â Â Â Â Â lockRank ?: UserRank ;
  Â Â Â Â Â Â Â Â revSpeedLimit ?: null | number ;
  Â Â Â Â Â Â Â Â roadType ?: RoadTypeId ;
  Â Â Â Â Â Â Â Â routingRoadType ?: 1 | 2 | 3 | 6 | 7 ;
  Â Â Â Â Â Â Â Â segmentId: number ;
  Â Â Â Â Â Â Â Â toLanesInfo ?: null | SegmentLanesInfo ;
  Â Â Â Â } ,
  ) : void
```

### `verifyTurns`

```typescript
verifyTurns ( args: { isForward: boolean ; segmentId: number } ) : void
```
