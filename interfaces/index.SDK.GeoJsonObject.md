---
title: SDK.GeoJsonObject interface
source: interfaces/index.SDK.GeoJsonObject.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface GeoJsonObject

```typescript
interface GeoJsonObject {
  Â Â Â Â bbox ?: BBox ;
  Â Â Â Â type: 
  Â Â Â Â Â Â Â Â | "Point"
  Â Â Â Â Â Â Â Â | "LineString"
  Â Â Â Â Â Â Â Â | "Polygon"
  Â Â Â Â Â Â Â Â | "MultiPolygon"
  Â Â Â Â Â Â Â Â | "MultiLineString"
  Â Â Â Â Â Â Â Â | "GeometryCollection"
  Â Â Â Â Â Â Â Â | "FeatureCollection"
  Â Â Â Â Â Â Â Â | "Feature"
  Â Â Â Â Â Â Â Â | "MultiPoint" ;
}
```
The base GeoJSON object.https://tools.ietf.org/html/rfc7946#section-3The GeoJSON specification also allows foreign members
(https://tools.ietf.org/html/rfc7946#section-6.1)
Developers should use "&" type in TypeScript or extend the interface
to add these foreign members.
## Properties
