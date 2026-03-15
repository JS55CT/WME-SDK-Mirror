---
title: SDK.Venue interface
source: interfaces/index.SDK.Venue.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Venue

```typescript
interface Venue {
  Â Â Â Â aliases: string [] ;
  Â Â Â Â approved: boolean ;
  Â Â Â Â brand: null | string ;
  Â Â Â Â categories: VenueCategoryId [] ;
  Â Â Â Â externalProviderIds: string [] ;
  Â Â Â Â geometry: Point | Polygon ;
  Â Â Â Â id: string ;
  Â Â Â Â images: VenueImage [] ;
  Â Â Â Â isAdLocked: boolean ;
  Â Â Â Â isResidential: boolean ;
  Â Â Â Â lockRank: number ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â name: string ;
  Â Â Â Â navigationPoints: NavigationPoint [] ;
  Â Â Â Â openingHours: OpeningHour [] ;
  Â Â Â Â phone: string ;
  Â Â Â Â services: ServiceType [] ;
  Â Â Â Â url: string ;
  Â Â Â Â venueUpdateRequests: VenueUpdateRequest [] ;
}
```
## Properties
### `aliases`

```typescript
aliases: string []
```
### `approved`

```typescript
approved: boolean
```
### `brand`

```typescript
brand: null | string
```
### `categories`

```typescript
categories: VenueCategoryId []
```
### `externalProviderIds`

```typescript
externalProviderIds: string []
```
### `geometry`

```typescript
geometry: Point | Polygon
```
### `id`

```typescript
id: string
```
### `images`

```typescript
images: VenueImage []
```
### `isAdLocked`

```typescript
isAdLocked: boolean
```
### `isResidential`

```typescript
isResidential: boolean
```
### `lockRank`

```typescript
lockRank: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
### `navigationPoints`

```typescript
navigationPoints: NavigationPoint []
```
### `openingHours`

```typescript
openingHours: OpeningHour []
```
### `phone`

```typescript
phone: string
```
### `services`

```typescript
services: ServiceType []
```
### `url`

```typescript
url: string
```
### `venueUpdateRequests`

```typescript
venueUpdateRequests: VenueUpdateRequest []
```
