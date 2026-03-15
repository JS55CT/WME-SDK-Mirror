---
title: SDK.TrackedLayer interface
source: interfaces/index.SDK.TrackedLayer.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TrackedLayer

```typescript
interface TrackedLayer {
  Â Â Â Â events: {
  Â Â Â Â Â Â Â Â visibilitychanged: () = > void ;
  Â Â Â Â Â Â Â Â "waze-feature-clicked": ( e: { feature: WMEFeature } ) = > void ;
  Â Â Â Â Â Â Â Â "waze-feature-in": ( e: { feature: WMEFeature } ) = > void ;
  Â Â Â Â Â Â Â Â "waze-feature-out": ( e: { feature: WMEFeature } ) = > void ;
  Â Â Â Â } ;
}
```
## Properties
### `events`

```typescript
events: {
  Â Â Â Â visibilitychanged: () = > void ;
  Â Â Â Â "waze-feature-clicked": ( e: { feature: WMEFeature } ) = > void ;
  Â Â Â Â "waze-feature-in": ( e: { feature: WMEFeature } ) = > void ;
  Â Â Â Â "waze-feature-out": ( e: { feature: WMEFeature } ) = > void ;
}
```
