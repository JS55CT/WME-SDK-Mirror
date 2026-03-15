---
title: SDK.Country interface
source: interfaces/index.SDK.Country.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Country

```typescript
interface Country {
  Â Â Â Â abbr: string ;
  Â Â Â Â defaultLaneWidthPerRoadType: 
  Â Â Â Â Â Â Â Â | null
  Â Â Â Â Â Â Â Â | Partial <
  Â Â Â Â Â Â Â Â Â Â Â Â {
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "1": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "10": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "15": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "16": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "17": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "18": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "19": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "2": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "20": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "22": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "3": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "4": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "5": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "6": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "7": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "8": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â "9": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â } ,
  Â Â Â Â Â Â Â Â > ;
  Â Â Â Â id: number ;
  Â Â Â Â isLeftHandTraffic: boolean ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â name: string ;
  Â Â Â Â regionCode: null
  Â Â Â Â | RegionCode ;
  Â Â Â Â restrictionSubscriptions: Subscription [] ;
}
```
## Properties
### `abbr`

```typescript
abbr: string
```
### `defaultLaneWidthPerRoadType`

```typescript
defaultLaneWidthPerRoadType: 
  Â Â Â Â | null
  Â Â Â Â | Partial <
  Â Â Â Â Â Â Â Â {
  Â Â Â Â Â Â Â Â Â Â Â Â "1": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "10": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "15": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "16": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "17": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "18": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "19": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "2": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "20": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "22": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "3": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "4": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "5": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "6": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "7": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "8": number ;
  Â Â Â Â Â Â Â Â Â Â Â Â "9": number ;
  Â Â Â Â Â Â Â Â } ,
  Â Â Â Â >
```
### `id`

```typescript
id: number
```
### `isLeftHandTraffic`

```typescript
isLeftHandTraffic: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
### `regionCode`

```typescript
regionCode: null | RegionCode
```
### `restrictionSubscriptions`

```typescript
restrictionSubscriptions: Subscription []
```
