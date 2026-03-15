---
title: SDK.HouseNumbers class
source: classes/index.SDK.HouseNumbers.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class HouseNumbers

```typescript
addHouseNumber ( args: { number: string ; point: Point ; segmentId ?: number } ) : void
```
Methods for dealing with HouseNumbers
## Methods
### `addHouseNumber`

```typescript
addHouseNumber ( args: { number: string ; point: Point ; segmentId ?: number } ) : void
```

### `clearHouseNumbers`

```typescript
clearHouseNumbers () : void
```

### `deleteHouseNumber`

```typescript
deleteHouseNumber ( args: { houseNumberId: string } ) : void
```

### `fetchHouseNumbers`

```typescript
fetchHouseNumbers ( options: { segmentIds: number [] } ) : Promise < HouseNumber [] >
```
A Promise that resolves to an array of HouseNumber objects.
### `moveHouseNumber`

```typescript
moveHouseNumber (
  Â Â Â Â args: { houseNumberId: string ; point: Point ; segmentId ?: number } ,
  ) : void
```

### `moveHouseNumberFractionPoint`

```typescript
moveHouseNumberFractionPoint (
  Â Â Â Â args: { fractionPoint: Point ; houseNumberId: string } ,
  ) : void
```

### `updateHouseNumber`

```typescript
updateHouseNumber (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â fractionPoint ?: Point ;
  Â Â Â Â Â Â Â Â houseNumberId: string ;
  Â Â Â Â Â Â Â Â number ?: string ;
  Â Â Â Â Â Â Â Â point ?: Point ;
  Â Â Â Â Â Â Â Â segmentId ?: number ;
  Â Â Â Â } ,
  ) : void
```
