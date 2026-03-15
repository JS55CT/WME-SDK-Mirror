---
title: SDK.SdkFeature interface
source: interfaces/index.SDK.SdkFeature.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkFeature<G>

```typescript
interface SdkFeature < G extends SdkFeatureGeometry = SdkFeatureGeometry > {
  Â Â Â Â geometry: G ;
  Â Â Â Â id: string | number ;
  Â Â Â Â properties ?: SdkFeatureProperties ;
  Â Â Â Â type: "Feature" ;
}
```
## Properties
### `geometry`

```typescript
geometry: G
```
### `id`

```typescript
id: string | number
```
### **Optional** `properties`

```typescript
properties ?: SdkFeatureProperties
```
### `type`

```typescript
type: "Feature"
```
