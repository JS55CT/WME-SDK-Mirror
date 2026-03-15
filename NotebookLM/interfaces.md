# index.SDK.AffectedObject

---
title: SDK.AffectedObject interface
source: interfaces/index.SDK.AffectedObject.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface AffectedObject

```typescript
interface AffectedObject {
  Â Â Â Â objectId: null | string | number ;
  Â Â Â Â objectType: ObjectType ;
}
```
## Properties
### `objectId`

```typescript
objectId: null | string | number
```
### `objectType`

```typescript
objectType: ObjectType
```

---

# index.SDK.BaseAddress

---
title: SDK.BaseAddress interface
source: interfaces/index.SDK.BaseAddress.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BaseAddress

```typescript
interface BaseAddress {
  Â Â Â Â city: null | City ;
  Â Â Â Â country: null | Country ;
  Â Â Â Â isEmpty: boolean ;
  Â Â Â Â state: null | State ;
  Â Â Â Â street: null | Street ;
}
```
## Properties
### `city`

```typescript
city: null | City
```
### `country`

```typescript
country: null | Country
```
### `isEmpty`

```typescript
isEmpty: boolean
```
### `state`

```typescript
state: null | State
```
### `street`

```typescript
street: null | Street
```

---

# index.SDK.BaseRestriction

---
title: SDK.BaseRestriction interface
source: interfaces/index.SDK.BaseRestriction.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BaseRestriction

```typescript
interface BaseRestriction {
  Â Â Â Â driveProfiles: DriveProfiles ;
  Â Â Â Â isExpired: boolean ;
}
```
## Properties
### `driveProfiles`

```typescript
driveProfiles: DriveProfiles
```
### `isExpired`

```typescript
isExpired: boolean
```

---

# index.SDK.BigJunction

---
title: SDK.BigJunction interface
source: interfaces/index.SDK.BigJunction.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BigJunction

```typescript
interface BigJunction {
  Â Â Â Â cityId: null | number ;
  Â Â Â Â geometry: Polygon ;
  Â Â Â Â id: number ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â name: null | string ;
  Â Â Â Â segmentIds: number [] ;
}
```
## Properties
### `cityId`

```typescript
cityId: null | number
```
### `geometry`

```typescript
geometry: Polygon
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: null | string
```
### `segmentIds`

```typescript
segmentIds: number []
```

---

# index.SDK.CallSite

---
title: SDK.CallSite interface
source: interfaces/index.SDK.CallSite.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface CallSite

```typescript
interface CallSite {
  Â Â Â Â getColumnNumber () : null | number ;
  Â Â Â Â getEnclosingColumnNumber () : null | number ;
  Â Â Â Â getEnclosingLineNumber () : null | number ;
  Â Â Â Â getEvalOrigin () : undefined | string ;
  Â Â Â Â getFileName () : null | string ;
  Â Â Â Â getFunction () : undefined | Function ;
  Â Â Â Â getFunctionName () : null | string ;
  Â Â Â Â getLineNumber () : null | number ;
  Â Â Â Â getMethodName () : null | string ;
  Â Â Â Â getPosition () : number ;
  Â Â Â Â getPromiseIndex () : null | number ;
  Â Â Â Â getScriptHash () : string ;
  Â Â Â Â getScriptNameOrSourceURL () : null | string ;
  Â Â Â Â getThis () : unknown ;
  Â Â Â Â getTypeName () : null | string ;
  Â Â Â Â isAsync () : boolean ;
  Â Â Â Â isConstructor () : boolean ;
  Â Â Â Â isEval () : boolean ;
  Â Â Â Â isNative () : boolean ;
  Â Â Â Â isPromiseAll () : boolean ;
  Â Â Â Â isToplevel () : boolean ;
}
```
## Methods

---

# index.SDK.Camera

---
title: SDK.Camera interface
source: interfaces/index.SDK.Camera.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Camera

```typescript
interface Camera {
  Â Â Â Â direction: null | RestrictionSegmentDirection ;
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: number ;
  Â Â Â Â lockRank: null | number ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â segmentId: null | number ;
  Â Â Â Â types: CameraType [] ;
}
```
## Properties
### `direction`

```typescript
direction: null | RestrictionSegmentDirection
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `lockRank`

```typescript
lockRank: null | number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentId`

```typescript
segmentId: null | number
```
### `types`

```typescript
types: CameraType []
```

---

# index.SDK.ChangedField

---
title: SDK.ChangedField interface
source: interfaces/index.SDK.ChangedField.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ChangedField

```typescript
interface ChangedField {
  Â Â Â Â fieldName: undefined | string ;
}
```
## Properties
### `fieldName`

```typescript
fieldName: undefined | string
```

---

# index.SDK.ChangedIDsInfo

---
title: SDK.ChangedIDsInfo interface
source: interfaces/index.SDK.ChangedIDsInfo.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ChangedIDsInfo

```typescript
interface ChangedIDsInfo {
  Â Â Â Â newID: null | string | number ;
  Â Â Â Â oldID: null | string | number ;
}
```
## Properties
### `newID`

```typescript
newID: null | string | number
```
### `oldID`

```typescript
oldID: null | string | number
```

---

# index.SDK.City

---
title: SDK.City interface
source: interfaces/index.SDK.City.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface City

```typescript
interface City {
  Â Â Â Â countryId: null | number ;
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: number ;
  Â Â Â Â isEmpty: boolean ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â name: null | string ;
  Â Â Â Â stateId: null | number ;
}
```
## Properties
### `countryId`

```typescript
countryId: null | number
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `isEmpty`

```typescript
isEmpty: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: null | string
```
### `stateId`

```typescript
stateId: null | number
```

---

# index.SDK.ConversationElement

---
title: SDK.ConversationElement interface
source: interfaces/index.SDK.ConversationElement.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ConversationElement

```typescript
interface ConversationElement {
  Â Â Â Â createdOn: number ;
  Â Â Â Â text: string ;
  Â Â Â Â userName: null | string ;
}
```
## Properties
### `createdOn`

```typescript
createdOn: number
```
### `text`

```typescript
text: string
```
### `userName`

```typescript
userName: null | string
```

---

# index.SDK.Country

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

---

# index.SDK.DriveProfile

---
title: SDK.DriveProfile interface
source: interfaces/index.SDK.DriveProfile.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface DriveProfile

```typescript
interface DriveProfile {
  Â Â Â Â licensePlateNumber: string ;
  Â Â Â Â numPassengers: number ;
  Â Â Â Â subscriptions: string [] ;
  Â Â Â Â vehicleTypes: VehicleType [] ;
}
```
## Properties
### `licensePlateNumber`

```typescript
licensePlateNumber: string
```
### `numPassengers`

```typescript
numPassengers: number
```
### `subscriptions`

```typescript
subscriptions: string []
```
### `vehicleTypes`

```typescript
vehicleTypes: VehicleType []
```

---

# index.SDK.EditSuggestion

---
title: SDK.EditSuggestion interface
source: interfaces/index.SDK.EditSuggestion.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface EditSuggestion

```typescript
interface EditSuggestion {
  Â Â Â Â bbox: BBox ;
  Â Â Â Â id: string ;
  Â Â Â Â isRead: boolean ;
  Â Â Â Â isStarred: boolean ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â source: EditSuggestionSource ;
  Â Â Â Â status: EditSuggestionStatus ;
  Â Â Â Â suggestions: Suggestion [] ;
}
```
Represents an edit suggestion, potentially containing multiple individual suggestions.
## Properties
### `bbox`

```typescript
bbox: BBox
```
### `id`

```typescript
id: string
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `source`

```typescript
source: EditSuggestionSource
```
### `status`

```typescript
status: EditSuggestionStatus
```
### `suggestions`

```typescript
suggestions: Suggestion []
```

---

# index.SDK.EditSuggestionChange

---
title: SDK.EditSuggestionChange interface
source: interfaces/index.SDK.EditSuggestionChange.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface EditSuggestionChange

```typescript
interface EditSuggestionChange {
  Â Â Â Â attributeChanges: SuggestionAttributeChange < unknown > [] ;
  Â Â Â Â createdOn: null | number ;
  Â Â Â Â rejectionReason: null | SuggestionResolutionRejectionReason ;
  Â Â Â Â status: SuggestionResolutionStatus ;
  Â Â Â Â suggestionId: string ;
}
```
Represents a change suggested in an edit suggestion, containing an attribute change per each changed attribute.
## Properties
### `attributeChanges`

```typescript
attributeChanges: SuggestionAttributeChange < unknown > []
```
### `createdOn`

```typescript
createdOn: null | number
```
### `rejectionReason`

```typescript
rejectionReason: null | SuggestionResolutionRejectionReason
```
### `status`

```typescript
status: SuggestionResolutionStatus
```
### `suggestionId`

```typescript
suggestionId: string
```

---

# index.SDK.ErrorOptions

---
title: SDK.ErrorOptions interface
source: interfaces/index.SDK.ErrorOptions.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ErrorOptions

```typescript
interface ErrorOptions {
  Â Â Â Â cause ?: unknown ;
}
```
## Properties

---

# index.SDK.FeatureStyle

---
title: SDK.FeatureStyle interface
source: interfaces/index.SDK.FeatureStyle.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface FeatureStyle

```typescript
interface FeatureStyle {
  Â Â Â Â backgroundGraphic ?: string ;
  Â Â Â Â backgroundGraphicZIndex ?: number ;
  Â Â Â Â backgroundHeight ?: string | number ;
  Â Â Â Â backgroundWidth ?: string | number ;
  Â Â Â Â backgroundXOffset ?: string | number ;
  Â Â Â Â backgroundYOffset ?: string | number ;
  Â Â Â Â cursor ?: string ;
  Â Â Â Â display ?: string ;
  Â Â Â Â externalGraphic ?: null | string ;
  Â Â Â Â fill ?: boolean ;
  Â Â Â Â fillColor ?: string ;
  Â Â Â Â fillOpacity ?: number ;
  Â Â Â Â fontColor ?: string ;
  Â Â Â Â fontFamily ?: string ;
  Â Â Â Â fontOpacity ?: number ;
  Â Â Â Â fontSize ?: string ;
  Â Â Â Â fontStyle ?: string ;
  Â Â Â Â fontWeight ?: string ;
  Â Â Â Â graphic ?: boolean ;
  Â Â Â Â graphicHeight ?: string | number ;
  Â Â Â Â graphicName ?: string ;
  Â Â Â Â graphicOpacity ?: string | number ;
  Â Â Â Â graphicWidth ?: string | number ;
  Â Â Â Â graphicXOffset ?: number ;
  Â Â Â Â graphicYOffset ?: string | number ;
  Â Â Â Â graphicZIndex ?: string | number ;
  Â Â Â Â hoverFillColor ?: string ;
  Â Â Â Â hoverFillOpacity ?: number ;
  Â Â Â Â hoverPointRadius ?: number ;
  Â Â Â Â hoverPointUnit ?: string ;
  Â Â Â Â hoverStrokeColor ?: string ;
  Â Â Â Â hoverStrokeOpacity ?: number ;
  Â Â Â Â hoverStrokeWidth ?: number ;
  Â Â Â Â label ?: string ;
  Â Â Â Â labelAlign ?: string ;
  Â Â Â Â labelOutlineColor ?: string ;
  Â Â Â Â labelOutlineOpacity ?: number ;
  Â Â Â Â labelOutlineWidth ?: number ;
  Â Â Â Â labelSelect ?: boolean ;
  Â Â Â Â labelXOffset ?: number ;
  Â Â Â Â labelYOffset ?: number ;
  Â Â Â Â pointerEvents ?: string ;
  Â Â Â Â pointRadius ?: string | number ;
  Â Â Â Â rotation ?: string | number ;
  Â Â Â Â stroke ?: boolean ;
  Â Â Â Â strokeColor ?: string ;
  Â Â Â Â strokeDashstyle ?:
  Â Â Â Â Â Â Â Â | "solid"
  Â Â Â Â Â Â Â Â | "dot"
  Â Â Â Â Â Â Â Â | "dash"
  Â Â Â Â Â Â Â Â | "dashdot"
  Â Â Â Â Â Â Â Â | "longdash"
  Â Â Â Â Â Â Â Â | "longdashdot" ;
  Â Â Â Â strokeLinecap ?: "butt"
  Â Â Â Â | "round"
  Â Â Â Â | "square" ;
  Â Â Â Â strokeOpacity ?: string | number ;
  Â Â Â Â strokeWidth ?: string | number ;
  Â Â Â Â title ?: string ;
}
```
List of OpenLayers supported styles taken from OL 2 docs
Seehttps://amirn.users.x20web.corp.google.com/www/dev.openlayers.org/docs/files/OpenLayers/Feature/Vector-js.html#OpenLayers.Feature.Vector.OpenLayers.Feature.Vector.stylehttp://cs/waze-dev/web-common/packages/web-map/src/third_party/OpenLayers/Feature/Vector.js;l=373-434;rcl=b5d307754927a6944baa9bdd3f2ba802ebffdbc3Param: backgroundGraphicUrl to a graphic to be used as the background under an externalGraphic.Param: backgroundGraphicZIndexThe integer z-index value to use in rendering the background graphic.Param: backgroundHeightThe height of the background graphic. If not provided, the graphicHeight will be used.Param: backgroundWidthThe width of the background width. If not provided, the graphicWidth will be used.Param: backgroundXOffsetThe x offset (in pixels) for the background graphic.Param: backgroundYOffsetThe y offset (in pixels) for the background graphic.Param: cursorDefault is "".Param: displaySymbolizers will have no effect if display is set to "none".  All other values have no effect.Param: externalGraphicUrl to an external graphic that will be used for rendering points.Param: fillSet to false if no fill is desired.Param: fillColorHex fill color.  Default is "#ee9900".Param: fillOpacityFill opacity (0-1).  Default is 0.4Param: fontColorThe font color for the label, to be provided like CSS.Param: fontFamilyThe font family for the label, to be provided like in CSS.Param: fontOpacityOpacity (0-1) for the labelParam: fontSizeThe font size for the label, to be provided like in CSS.Param: fontStyleThe font style for the label, to be provided like in CSS.Param: fontWeightThe font weight for the label, to be provided like in CSS.Param: graphicSet to false if no graphic is desired.Param: graphicHeightPixel height for sizing an external graphic.Param: graphicNameNamed graphic to use when rendering points.  Supported values include "circle" (default), "square", "star", "x", "cross", "triangle".Param: graphicOpacityOpacity (0-1) for an external graphic.Param: graphicWidthPixel width for sizing an external graphic.Param: graphicXOffsetPixel offset along the positive x axis for displacing an external graphic.Param: graphicYOffsetPixel offset along the positive y axis for displacing an external graphic.Param: graphicZIndexThe integer z-index value to use in rendering.Param: labelThe text for an optional label. For browsers that use the canvas renderer, this requires either fillText or mozDrawText to be available.Param: labelAlignLabel alignment. This specifies the insertion point relative to the text. It is a string
composed of two characters. The first character is for the horizontal alignment, the second for the vertical
alignment. Valid values for horizontal alignment: "l"=left, "c"=center, "r"=right. Valid values for vertical
alignment: "t"=top, "m"=middle, "b"=bottom. Example values: "lt", "cm", "rb". Default is "cm".Param: labelOutlineColorThe color of the label outline. Default is 'white'. Only supported by the canvas & SVG renderers.Param: labelOutlineOpacityThe opacity (0-1) of the label outline. Default is fontOpacity. Only supported by the canvas & SVG renderers.Param: labelOutlineWidthThe width of the label outline. Default is 3, set to 0 or null to disable. Only supported by the  SVG renderers.Param: labelSelectIf set to true, labels will be selectable using SelectFeature or similar controls. Default is false.Param: labelXOffsetPixel offset along the positive x axis for displacing the label. Not supported by the canvas renderer.Param: labelYOffsetPixel offset along the positive y axis for displacing the label. Not supported by the canvas renderer.Param: pointRadiusPixel point radius.  Default is 6.Param: pointerEventsDefault is "visiblePainted".Param: rotationFor point symbolizers, this is the rotation of a graphic in the clockwise direction about its center point (or any point off center as specified by graphicXOffset and graphicYOffset).Param: strokeSet to false if no stroke is desired.Param: strokeColorHex stroke color.  Default is "#ee9900".Param: strokeDashstyleStroke dash style.  Default is "solid". [dot | dash | dashdot | longdash | longdashdot | solid]Param: strokeLinecapStroke cap type.  Default is "round".  [butt | round | square]Param: strokeOpacityStroke opacity (0-1).  Default is 1.Param: strokeWidthPixel stroke width.  Default is 1.Param: titleTooltip when hovering over a feature. Not supported by the canvas renderer.
## Properties

---

# index.SDK.GeoJsonObject

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

---

# index.SDK.HouseNumber

---
title: SDK.HouseNumber interface
source: interfaces/index.SDK.HouseNumber.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface HouseNumber

```typescript
interface HouseNumber {
  Â Â Â Â fractionPoint: null | Point ;
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: string ;
  Â Â Â Â isForced: boolean ;
  Â Â Â Â number: string ;
  Â Â Â Â segmentId: number ;
  Â Â Â Â updatedBy: null | string ;
}
```
Represents a house number associated with a segment.
It provides information about the house number itself, its location, and its relation to the segment.
## Properties
### `fractionPoint`

```typescript
fractionPoint: null | Point
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: string
```
### `isForced`

```typescript
isForced: boolean
```
### `number`

```typescript
number: string
```
### `segmentId`

```typescript
segmentId: number
```
### `updatedBy`

```typescript
updatedBy: null | string
```

---

# index.SDK.Junction

---
title: SDK.Junction interface
source: interfaces/index.SDK.Junction.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Junction

```typescript
interface Junction {
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: number ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â segmentIds: number [] ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentIds`

```typescript
segmentIds: number []
```

---

# index.SDK.KeyboardShortcut

---
title: SDK.KeyboardShortcut interface
source: interfaces/index.SDK.KeyboardShortcut.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface KeyboardShortcut

```typescript
interface KeyboardShortcut {
  Â Â Â Â callback: () = > void ;
  Â Â Â Â description: string ;
  Â Â Â Â shortcutId: string ;
  Â Â Â Â shortcutKeys: null | string ;
}
```
A keyboard shortcut for userscript action.
## Properties
### `callback`

```typescript
callback: () = > void
```
### `description`

```typescript
description: string
```
### `shortcutId`

```typescript
shortcutId: string
```
### `shortcutKeys`

```typescript
shortcutKeys: null | string
```

---

# index.SDK.LineString

---
title: SDK.LineString interface
source: interfaces/index.SDK.LineString.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface LineString

```typescript
interface LineString {
  Â Â Â Â bbox ?: BBox ;
  Â Â Â Â coordinates: Position [] ;
  Â Â Â Â type: "LineString" ;
}
```
LineString geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.4
## Properties

---

# index.SDK.LocalizedString

---
title: SDK.LocalizedString interface
source: interfaces/index.SDK.LocalizedString.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface LocalizedString

```typescript
interface LocalizedString {
  Â Â Â Â locale: string ;
  Â Â Â Â value: string ;
}
```
## Properties
### `locale`

```typescript
locale: string
```
### `value`

```typescript
value: string
```

---

# index.SDK.LonLat

---
title: SDK.LonLat interface
source: interfaces/index.SDK.LonLat.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface LonLat

```typescript
interface LonLat {
  Â Â Â Â lat: number ;
  Â Â Â Â lon: number ;
}
```
## Properties
### `lat`

```typescript
lat: number
```
### `lon`

```typescript
lon: number
```

---

# index.SDK.MajorTrafficEvent

---
title: SDK.MajorTrafficEvent interface
source: interfaces/index.SDK.MajorTrafficEvent.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MajorTrafficEvent

```typescript
interface MajorTrafficEvent {
  Â Â Â Â category: null | MajorTrafficEventCategory ;
  Â Â Â Â cityId: null | number ;
  Â Â Â Â endDate: null | string ;
  Â Â Â Â id: string ;
  Â Â Â Â isPublished: boolean ;
  Â Â Â Â isReady: boolean ;
  Â Â Â Â lockRank: null | UserRank ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â names: LocalizedString [] ;
  Â Â Â Â startDate: null | string ;
}
```
## Properties
### `category`

```typescript
category: null | MajorTrafficEventCategory
```
### `cityId`

```typescript
cityId: null | number
```
### `endDate`

```typescript
endDate: null | string
```
### `id`

```typescript
id: string
```
### `isPublished`

```typescript
isPublished: boolean
```
### `isReady`

```typescript
isReady: boolean
```
### `lockRank`

```typescript
lockRank: null | UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `names`

```typescript
names: LocalizedString []
```
### `startDate`

```typescript
startDate: null | string
```

---

# index.SDK.ManagedArea

---
title: SDK.ManagedArea interface
source: interfaces/index.SDK.ManagedArea.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ManagedArea

```typescript
interface ManagedArea {
  Â Â Â Â geometry: Polygon ;
  Â Â Â Â id: string ;
  Â Â Â Â userName: string ;
}
```
## Properties
### `geometry`

```typescript
geometry: Polygon
```
### `id`

```typescript
id: string
```
### `userName`

```typescript
userName: string
```

---

# index.SDK.ManagedAreaShort

---
title: SDK.ManagedAreaShort interface
source: interfaces/index.SDK.ManagedAreaShort.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ManagedAreaShort

```typescript
interface ManagedAreaShort {
  Â Â Â Â id: number ;
  Â Â Â Â name: string ;
}
```
## Properties
### `id`

```typescript
id: number
```
### `name`

```typescript
name: string
```

---

# index.SDK.MapComment

---
title: SDK.MapComment interface
source: interfaces/index.SDK.MapComment.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapComment

```typescript
interface MapComment {
  Â Â Â Â body: string ;
  Â Â Â Â conversation: ConversationElement [] ;
  Â Â Â Â endDate: null | string ;
  Â Â Â Â geometry: Point | Polygon ;
  Â Â Â Â id: string ;
  Â Â Â Â isFollowing: boolean ;
  Â Â Â Â isPoint: boolean ;
  Â Â Â Â lockRank: UserRank ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â subject: string ;
}
```
## Properties
### `body`

```typescript
body: string
```
### `conversation`

```typescript
conversation: ConversationElement []
```
### `endDate`

```typescript
endDate: null | string
```
### `geometry`

```typescript
geometry: Point | Polygon
```
### `id`

```typescript
id: string
```
### `isFollowing`

```typescript
isFollowing: boolean
```
### `isPoint`

```typescript
isPoint: boolean
```
### `lockRank`

```typescript
lockRank: UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `subject`

```typescript
subject: string
```

---

# index.SDK.MapProblem

---
title: SDK.MapProblem interface
source: interfaces/index.SDK.MapProblem.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapProblem

```typescript
interface MapProblem {
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: string ;
  Â Â Â Â isEditable: boolean ;
  Â Â Â Â isOpen: boolean ;
  Â Â Â Â isRead: boolean ;
  Â Â Â Â isStarred: boolean ;
  Â Â Â Â problemType: MapProblemType ;
  Â Â Â Â resolvedOn: null | number ;
  Â Â Â Â severity: IssueSeverity ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: string
```
### `isEditable`

```typescript
isEditable: boolean
```
### `isOpen`

```typescript
isOpen: boolean
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `problemType`

```typescript
problemType: MapProblemType
```
### `resolvedOn`

```typescript
resolvedOn: null | number
```
### `severity`

```typescript
severity: IssueSeverity
```

---

# index.SDK.MapUpdateRequest

---
title: SDK.MapUpdateRequest interface
source: interfaces/index.SDK.MapUpdateRequest.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapUpdateRequest

```typescript
interface MapUpdateRequest {
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: number ;
  Â Â Â Â isEditable: boolean ;
  Â Â Â Â isOpen: boolean ;
  Â Â Â Â isRead: boolean ;
  Â Â Â Â isStarred: boolean ;
  Â Â Â Â reportedOn: number ;
  Â Â Â Â resolutionState: null | string ;
  Â Â Â Â resolvedOn: null | number ;
  Â Â Â Â severity: IssueSeverity ;
  Â Â Â Â source: UpdateRequestSource ;
  Â Â Â Â updateRequestType: UpdateRequestType ;
  Â Â Â Â userPreferences: UpdateRequestUserPreferences ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `isEditable`

```typescript
isEditable: boolean
```
### `isOpen`

```typescript
isOpen: boolean
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `reportedOn`

```typescript
reportedOn: number
```
### `resolutionState`

```typescript
resolutionState: null | string
```
### `resolvedOn`

```typescript
resolvedOn: null | number
```
### `severity`

```typescript
severity: IssueSeverity
```
### `source`

```typescript
source: UpdateRequestSource
```
### `updateRequestType`

```typescript
updateRequestType: UpdateRequestType
```
### `userPreferences`

```typescript
userPreferences: UpdateRequestUserPreferences
```

---

# index.SDK.ModificationMetadata

---
title: SDK.ModificationMetadata interface
source: interfaces/index.SDK.ModificationMetadata.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ModificationMetadata

```typescript
interface ModificationMetadata {
  Â Â Â Â createdBy: null | string ;
  Â Â Â Â createdOn: null | number ;
  Â Â Â Â updatedBy: null | string ;
  Â Â Â Â updatedOn: null | number ;
}
```
## Properties
### `createdBy`

```typescript
createdBy: null | string
```
### `createdOn`

```typescript
createdOn: null | number
```
### `updatedBy`

```typescript
updatedBy: null | string
```
### `updatedOn`

```typescript
updatedOn: null | number
```

---

# index.SDK.MultiLineString

---
title: SDK.MultiLineString interface
source: interfaces/index.SDK.MultiLineString.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MultiLineString

```typescript
interface MultiLineString {
  Â Â Â Â bbox ?: BBox ;
  Â Â Â Â coordinates: Position [] [] ;
  Â Â Â Â type: "MultiLineString" ;
}
```
MultiLineString geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.5
## Properties

---

# index.SDK.MultiPolygon

---
title: SDK.MultiPolygon interface
source: interfaces/index.SDK.MultiPolygon.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MultiPolygon

```typescript
interface MultiPolygon {
  Â Â Â Â bbox ?: BBox ;
  Â Â Â Â coordinates: Position [] [] [] ;
  Â Â Â Â type: "MultiPolygon" ;
}
```
MultiPolygon geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.7
## Properties

---

# index.SDK.NavigationPoint

---
title: SDK.NavigationPoint interface
source: interfaces/index.SDK.NavigationPoint.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface NavigationPoint

```typescript
interface NavigationPoint {
  Â Â Â Â isEntry: boolean ;
  Â Â Â Â isExit: boolean ;
  Â Â Â Â isPrimary: boolean ;
  Â Â Â Â name: string ;
  Â Â Â Â point: Point ;
}
```
## Properties
### `isEntry`

```typescript
isEntry: boolean
```
### `isExit`

```typescript
isExit: boolean
```
### `isPrimary`

```typescript
isPrimary: boolean
```
### `name`

```typescript
name: string
```
### `point`

```typescript
point: Point
```

---

# index.SDK.Node

---
title: SDK.Node interface
source: interfaces/index.SDK.Node.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Node

```typescript
interface Node {
  Â Â Â Â connectedSegmentIds: number [] ;
  Â Â Â Â geometry: Point ;
  Â Â Â Â id: number ;
}
```
## Properties
### `connectedSegmentIds`

```typescript
connectedSegmentIds: number []
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```

---

# index.SDK.OpeningHour

---
title: SDK.OpeningHour interface
source: interfaces/index.SDK.OpeningHour.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface OpeningHour

```typescript
interface OpeningHour {
  Â Â Â Â days: number [] ;
  Â Â Â Â fromHour: string ;
  Â Â Â Â toHour: string ;
}
```
## Properties
### `days`

```typescript
days: number []
```
### `fromHour`

```typescript
fromHour: string
```
### `toHour`

```typescript
toHour: string
```

---

# index.SDK.Pixel

---
title: SDK.Pixel interface
source: interfaces/index.SDK.Pixel.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Pixel

```typescript
interface Pixel {
  Â Â Â Â x: number ;
  Â Â Â Â y: number ;
}
```
## Properties
### `x`

```typescript
x: number
```
### `y`

```typescript
y: number
```

---

# index.SDK.Point

---
title: SDK.Point interface
source: interfaces/index.SDK.Point.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Point

```typescript
interface Point {
  Â Â Â Â bbox ?: BBox ;
  Â Â Â Â coordinates: Position ;
  Â Â Â Â type: "Point" ;
}
```
Point geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.2
## Properties

---

# index.SDK.Polygon

---
title: SDK.Polygon interface
source: interfaces/index.SDK.Polygon.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Polygon

```typescript
interface Polygon {
  Â Â Â Â bbox ?: BBox ;
  Â Â Â Â coordinates: Position [] [] ;
  Â Â Â Â type: "Polygon" ;
}
```
Polygon geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.6
## Properties

---

# index.SDK.RegisterSidebarTabResult

---
title: SDK.RegisterSidebarTabResult interface
source: interfaces/index.SDK.RegisterSidebarTabResult.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RegisterSidebarTabResult

```typescript
interface RegisterSidebarTabResult {
  Â Â Â Â tabLabel: HTMLElement ;
  Â Â Â Â tabPane: HTMLElement ;
}
```
## Properties
### `tabLabel`

```typescript
tabLabel: HTMLElement
```
### `tabPane`

```typescript
tabPane: HTMLElement
```

---

# index.SDK.RestrictedDrivingArea

---
title: SDK.RestrictedDrivingArea interface
source: interfaces/index.SDK.RestrictedDrivingArea.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RestrictedDrivingArea

```typescript
interface RestrictedDrivingArea {
  Â Â Â Â center: Point ;
  Â Â Â Â geometry: Polygon ;
  Â Â Â Â id: number ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â name: string ;
  Â Â Â Â restrictionName: string ;
}
```
## Properties
### `center`

```typescript
center: Point
```
### `geometry`

```typescript
geometry: Polygon
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
### `restrictionName`

```typescript
restrictionName: string
```

---

# index.SDK.RoadClosure

---
title: SDK.RoadClosure interface
source: interfaces/index.SDK.RoadClosure.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadClosure

```typescript
interface RoadClosure {
  Â Â Â Â description: null | string ;
  Â Â Â Â endDate: null | string ;
  Â Â Â Â id: string ;
  Â Â Â Â isForward: boolean ;
  Â Â Â Â isPermanent: boolean ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â segmentId: number ;
  Â Â Â Â startDate: null | string ;
  Â Â Â Â status: ClosureStatus ;
  Â Â Â Â trafficEventId: null | string ;
}
```
## Properties
### `description`

```typescript
description: null | string
```
### `endDate`

```typescript
endDate: null | string
```
### `id`

```typescript
id: string
```
### `isForward`

```typescript
isForward: boolean
```
### `isPermanent`

```typescript
isPermanent: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentId`

```typescript
segmentId: number
```
### `startDate`

```typescript
startDate: null | string
```
### `status`

```typescript
status: ClosureStatus
```
### `trafficEventId`

```typescript
trafficEventId: null | string
```

---

# index.SDK.RoadType

---
title: SDK.RoadType interface
source: interfaces/index.SDK.RoadType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadType

```typescript
interface RoadType {
  Â Â Â Â id: RoadTypeId ;
  Â Â Â Â localizedName: string ;
  Â Â Â Â name: string ;
}
```
## Properties
### `id`

```typescript
id: RoadTypeId
```
### `localizedName`

```typescript
localizedName: string
```
### `name`

```typescript
name: string
```

---

# index.SDK.SdkEvents

---
title: SDK.SdkEvents interface
source: interfaces/index.SDK.SdkEvents.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkEvents

```typescript
interface SdkEvents {
  Â Â Â Â "wme-after-edit": { affectedObjects: AffectedObject [] } ;
  Â Â Â Â "wme-after-redo-clear": undefined ;
  Â Â Â Â "wme-after-undo": undefined ;
  Â Â Â Â "wme-data-model-object-changed-id": {
  Â Â Â Â Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â Â Â Â Â objectIds: ChangedIDsInfo ;
  Â Â Â Â } ;
  Â Â Â Â "wme-data-model-object-state-deleted": {
  Â Â Â Â Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â Â Â Â Â objectIds: ( string | number ) [] ;
  Â Â Â Â } ;
  Â Â Â Â "wme-data-model-objects-added": {
  Â Â Â Â Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â Â Â Â Â objectIds: ( string | number ) [] ;
  Â Â Â Â } ;
  Â Â Â Â "wme-data-model-objects-changed": {
  Â Â Â Â Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â Â Â Â Â objectIds: ( string | number ) [] ;
  Â Â Â Â } ;
  Â Â Â Â "wme-data-model-objects-removed": {
  Â Â Â Â Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â Â Â Â Â objectIds: ( string | number ) [] ;
  Â Â Â Â } ;
  Â Â Â Â "wme-data-model-objects-saved": {
  Â Â Â Â Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â Â Â Â Â objectIds: ( string | number ) [] ;
  Â Â Â Â } ;
  Â Â Â Â "wme-editing-house-numbers": { isEditingHouseNumbers: false } ;
  Â Â Â Â "wme-feature-editor-opened": {
  Â Â Â Â Â Â Â Â featureType: 
  Â Â Â Â Â Â Â Â Â Â Â Â | "bigJunction"
  Â Â Â Â Â Â Â Â Â Â Â Â | "city"
  Â Â Â Â Â Â Â Â Â Â Â Â | "mapComment"
  Â Â Â Â Â Â Â Â Â Â Â Â | "node"
  Â Â Â Â Â Â Â Â Â Â Â Â | "permanentHazard"
  Â Â Â Â Â Â Â Â Â Â Â Â | "restrictedDrivingArea"
  Â Â Â Â Â Â Â Â Â Â Â Â | "segment"
  Â Â Â Â Â Â Â Â Â Â Â Â | "segmentSuggestion"
  Â Â Â Â Â Â Â Â Â Â Â Â | "venue" ;
  Â Â Â Â } ;
  Â Â Â Â "wme-house-number-added": { houseNumberId: string } ;
  Â Â Â Â "wme-house-number-deleted": { houseNumberId: string } ;
  Â Â Â Â "wme-house-number-moved": { houseNumberId: string } ;
  Â Â Â Â "wme-house-number-updated": { houseNumberId: string } ;
  Â Â Â Â "wme-initialized": undefined ;
  Â Â Â Â "wme-layer-checkbox-toggled": { checked: boolean ; name: string } ;
  Â Â Â Â "wme-layer-feature-clicked": {
  Â Â Â Â Â Â Â Â featureId: string | number ;
  Â Â Â Â Â Â Â Â layerName: string ;
  Â Â Â Â } ;
  Â Â Â Â "wme-layer-feature-mouse-enter": {
  Â Â Â Â Â Â Â Â featureId: string
  Â Â Â Â Â Â Â Â | number ;
  Â Â Â Â Â Â Â Â layerName: string ;
  Â Â Â Â } ;
  Â Â Â Â "wme-layer-feature-mouse-leave": {
  Â Â Â Â Â Â Â Â featureId: string
  Â Â Â Â Â Â Â Â | number ;
  Â Â Â Â Â Â Â Â layerName: string ;
  Â Â Â Â } ;
  Â Â Â Â "wme-layer-visibility-changed": { layerName: string } ;
  Â Â Â Â "wme-logged-in": undefined ;
  Â Â Â Â "wme-logged-out": undefined ;
  Â Â Â Â "wme-map-data-loaded": undefined ;
  Â Â Â Â "wme-map-house-number-marker-added": undefined ;
  Â Â Â Â "wme-map-initial-data-loaded": undefined ;
  Â Â Â Â "wme-map-layer-added": { layerName: string } ;
  Â Â Â Â "wme-map-layer-changed": { layerName: string } ;
  Â Â Â Â "wme-map-layer-removed": { layerName: string } ;
  Â Â Â Â "wme-map-mouse-click": SdkMouseEvent ;
  Â Â Â Â "wme-map-mouse-down": SdkMouseEvent ;
  Â Â Â Â "wme-map-mouse-move": SdkMouseEvent ;
  Â Â Â Â "wme-map-mouse-out": SdkMouseEvent ;
  Â Â Â Â "wme-map-mouse-up": SdkMouseEvent ;
  Â Â Â Â "wme-map-move": undefined ;
  Â Â Â Â "wme-map-move-end": undefined ;
  Â Â Â Â "wme-map-zoom-changed": undefined ;
  Â Â Â Â "wme-no-edits": undefined ;
  Â Â Â Â "wme-ready": undefined ;
  Â Â Â Â "wme-save-finished": { success: boolean } ;
  Â Â Â Â "wme-save-mode-changed": { saveMode: SaveMode } ;
  Â Â Â Â "wme-selection-changed": undefined ;
  Â Â Â Â "wme-sidebar-tab-opened": { domId: string ; tabName: SidebarTabName } ;
  Â Â Â Â "wme-street-view-button-activated": undefined ;
  Â Â Â Â "wme-street-view-button-deactivated": undefined ;
  Â Â Â Â "wme-street-view-panel-visibility-changed": { isVisible: boolean } ;
  Â Â Â Â "wme-update-request-panel-opened": { updateRequestId: number } ;
  Â Â Â Â "wme-user-settings-changed": undefined ;
}
```
SDK events and their payload (if any).
## Properties
### `wme-after-edit`

```typescript
"wme-after-edit": { affectedObjects: AffectedObject [] }
```
### `wme-after-redo-clear`

```typescript
"wme-after-redo-clear": undefined
```
### `wme-after-undo`

```typescript
"wme-after-undo": undefined
```
### `wme-data-model-object-changed-id`

```typescript
"wme-data-model-object-changed-id": {
  Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â objectIds: ChangedIDsInfo ;
}
```
### `wme-data-model-object-state-deleted`

```typescript
"wme-data-model-object-state-deleted": {
  Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-added`

```typescript
"wme-data-model-objects-added": {
  Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-changed`

```typescript
"wme-data-model-objects-changed": {
  Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-removed`

```typescript
"wme-data-model-objects-removed": {
  Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-saved`

```typescript
"wme-data-model-objects-saved": {
  Â Â Â Â dataModelName: DataModelName ;
  Â Â Â Â objectIds: ( string | number ) [] ;
}
```
### `wme-editing-house-numbers`

```typescript
"wme-editing-house-numbers": { isEditingHouseNumbers: false }
```
### `wme-feature-editor-opened`

```typescript
"wme-feature-editor-opened": {
  Â Â Â Â featureType: 
  Â Â Â Â Â Â Â Â | "bigJunction"
  Â Â Â Â Â Â Â Â | "city"
  Â Â Â Â Â Â Â Â | "mapComment"
  Â Â Â Â Â Â Â Â | "node"
  Â Â Â Â Â Â Â Â | "permanentHazard"
  Â Â Â Â Â Â Â Â | "restrictedDrivingArea"
  Â Â Â Â Â Â Â Â | "segment"
  Â Â Â Â Â Â Â Â | "segmentSuggestion"
  Â Â Â Â Â Â Â Â | "venue" ;
}
```
### `wme-house-number-added`

```typescript
"wme-house-number-added": { houseNumberId: string }
```
### `wme-house-number-deleted`

```typescript
"wme-house-number-deleted": { houseNumberId: string }
```
### `wme-house-number-moved`

```typescript
"wme-house-number-moved": { houseNumberId: string }
```
### `wme-house-number-updated`

```typescript
"wme-house-number-updated": { houseNumberId: string }
```
### `wme-initialized`

```typescript
"wme-initialized": undefined
```
### `wme-layer-checkbox-toggled`

```typescript
"wme-layer-checkbox-toggled": { checked: boolean ; name: string }
```
### `wme-layer-feature-clicked`

```typescript
"wme-layer-feature-clicked": { featureId: string | number ; layerName: string }
```
### `wme-layer-feature-mouse-enter`

```typescript
"wme-layer-feature-mouse-enter": {
  Â Â Â Â featureId: string | number ;
  Â Â Â Â layerName: string ;
}
```
### `wme-layer-feature-mouse-leave`

```typescript
"wme-layer-feature-mouse-leave": {
  Â Â Â Â featureId: string | number ;
  Â Â Â Â layerName: string ;
}
```
### `wme-layer-visibility-changed`

```typescript
"wme-layer-visibility-changed": { layerName: string }
```
### `wme-logged-in`

```typescript
"wme-logged-in": undefined
```
### `wme-logged-out`

```typescript
"wme-logged-out": undefined
```
### `wme-map-data-loaded`

```typescript
"wme-map-data-loaded": undefined
```
### `wme-map-house-number-marker-added`

```typescript
"wme-map-house-number-marker-added": undefined
```
### `wme-map-initial-data-loaded`

```typescript
"wme-map-initial-data-loaded": undefined
```
### `wme-map-layer-added`

```typescript
"wme-map-layer-added": { layerName: string }
```
### `wme-map-layer-changed`

```typescript
"wme-map-layer-changed": { layerName: string }
```
### `wme-map-layer-removed`

```typescript
"wme-map-layer-removed": { layerName: string }
```
### `wme-map-mouse-click`

```typescript
"wme-map-mouse-click": SdkMouseEvent
```
### `wme-map-mouse-down`

```typescript
"wme-map-mouse-down": SdkMouseEvent
```
### `wme-map-mouse-move`

```typescript
"wme-map-mouse-move": SdkMouseEvent
```
### `wme-map-mouse-out`

```typescript
"wme-map-mouse-out": SdkMouseEvent
```
### `wme-map-mouse-up`

```typescript
"wme-map-mouse-up": SdkMouseEvent
```
### `wme-map-move`

```typescript
"wme-map-move": undefined
```
### `wme-map-move-end`

```typescript
"wme-map-move-end": undefined
```
### `wme-map-zoom-changed`

```typescript
"wme-map-zoom-changed": undefined
```
### `wme-no-edits`

```typescript
"wme-no-edits": undefined
```
### `wme-ready`

```typescript
"wme-ready": undefined
```
### `wme-save-finished`

```typescript
"wme-save-finished": { success: boolean }
```
### `wme-save-mode-changed`

```typescript
"wme-save-mode-changed": { saveMode: SaveMode }
```
### `wme-selection-changed`

```typescript
"wme-selection-changed": undefined
```
### `wme-sidebar-tab-opened`

```typescript
"wme-sidebar-tab-opened": { domId: string ; tabName: SidebarTabName }
```
### `wme-street-view-button-activated`

```typescript
"wme-street-view-button-activated": undefined
```
### `wme-street-view-button-deactivated`

```typescript
"wme-street-view-button-deactivated": undefined
```
### `wme-street-view-panel-visibility-changed`

```typescript
"wme-street-view-panel-visibility-changed": { isVisible: boolean }
```
### `wme-update-request-panel-opened`

```typescript
"wme-update-request-panel-opened": { updateRequestId: number }
```
### `wme-user-settings-changed`

```typescript
"wme-user-settings-changed": undefined
```

---

# index.SDK.SdkFeature

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

---

# index.SDK.SdkFeatureStyleRule

---
title: SDK.SdkFeatureStyleRule interface
source: interfaces/index.SDK.SdkFeatureStyleRule.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkFeatureStyleRule

```typescript
interface SdkFeatureStyleRule {
  Â Â Â Â predicate ?: SdkFeatureStylePredicate ;
  Â Â Â Â style: FeatureStyle ;
}
```
## Properties
### **Optional** `predicate`

```typescript
predicate ?: SdkFeatureStylePredicate
```
### `style`

```typescript
style: FeatureStyle
```

---

# index.SDK.SdkMouseEvent

---
title: SDK.SdkMouseEvent interface
source: interfaces/index.SDK.SdkMouseEvent.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkMouseEvent

```typescript
interface SdkMouseEvent {
  Â Â Â Â lat: number ;
  Â Â Â Â lon: number ;
  Â Â Â Â viewportX: number ;
  Â Â Â Â viewportY: number ;
  Â Â Â Â x: number ;
  Â Â Â Â y: number ;
}
```
## Properties
### `lat`

```typescript
lat: number
```
### `lon`

```typescript
lon: number
```
### `viewportX`

```typescript
viewportX: number
```
### `viewportY`

```typescript
viewportY: number
```
### `x`

```typescript
x: number
```
### `y`

```typescript
y: number
```

---

# index.SDK.SdkWazeFeature

---
title: SDK.SdkWazeFeature interface
source: interfaces/index.SDK.SdkWazeFeature.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkWazeFeature

```typescript
interface SdkWazeFeature {
  Â Â Â Â featureType: "SDKFeature" ;
  Â Â Â Â properties: SdkFeatureProperties ;
}
```
## Properties
### `featureType`

```typescript
featureType: "SDKFeature"
```
### `properties`

```typescript
properties: SdkFeatureProperties
```

---

# index.SDK.Segment

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

---

# index.SDK.SegmentAddress

---
title: SDK.SegmentAddress interface
source: interfaces/index.SDK.SegmentAddress.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentAddress

```typescript
interface SegmentAddress {
  Â Â Â Â altStreets: SegmentAddress [] ;
  Â Â Â Â city: null | City ;
  Â Â Â Â country: null | Country ;
  Â Â Â Â isEmpty: boolean ;
  Â Â Â Â state: null | State ;
  Â Â Â Â street: null | Street ;
}
```
## Properties
### `altStreets`

```typescript
altStreets: SegmentAddress []
```

---

# index.SDK.SegmentFlagAttributes

---
title: SDK.SegmentFlagAttributes interface
source: interfaces/index.SDK.SegmentFlagAttributes.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentFlagAttributes

```typescript
interface SegmentFlagAttributes {
  Â Â Â Â beacons: boolean ;
  Â Â Â Â fwdLanesEnabled: boolean ;
  Â Â Â Â fwdSpeedCamera: boolean ;
  Â Â Â Â headlights: boolean ;
  Â Â Â Â nearbyHOV: boolean ;
  Â Â Â Â revLanesEnabled: boolean ;
  Â Â Â Â revSpeedCamera: boolean ;
  Â Â Â Â tunnel: boolean ;
  Â Â Â Â unpaved: boolean ;
}
```
## Properties
### `beacons`

```typescript
beacons: boolean
```
### `fwdLanesEnabled`

```typescript
fwdLanesEnabled: boolean
```
### `fwdSpeedCamera`

```typescript
fwdSpeedCamera: boolean
```
### `headlights`

```typescript
headlights: boolean
```
### `nearbyHOV`

```typescript
nearbyHOV: boolean
```
### `revLanesEnabled`

```typescript
revLanesEnabled: boolean
```
### `revSpeedCamera`

```typescript
revSpeedCamera: boolean
```
### `tunnel`

```typescript
tunnel: boolean
```
### `unpaved`

```typescript
unpaved: boolean
```

---

# index.SDK.SegmentLanesInfo

---
title: SDK.SegmentLanesInfo interface
source: interfaces/index.SDK.SegmentLanesInfo.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentLanesInfo

```typescript
interface SegmentLanesInfo {
  Â Â Â Â laneWidth: null | number ;
  Â Â Â Â numberOfLanes: number ;
}
```
## Properties
### `laneWidth`

```typescript
laneWidth: null | number
```
### `numberOfLanes`

```typescript
numberOfLanes: number
```

---

# index.SDK.State

---
title: SDK.State interface
source: interfaces/index.SDK.State.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface State

```typescript
interface State {
  Â Â Â Â geometry: null | Polygon | MultiPolygon ;
  Â Â Â Â id: number ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â name: string ;
}
```
## Properties
### `geometry`

```typescript
geometry: null | Polygon | MultiPolygon
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```

---

# index.SDK.Street

---
title: SDK.Street interface
source: interfaces/index.SDK.Street.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Street

```typescript
interface Street {
  Â Â Â Â cityId: null | number ;
  Â Â Â Â direction: null | string ;
  Â Â Â Â englishName: null | string ;
  Â Â Â Â id: number ;
  Â Â Â Â isEmpty: boolean ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â name: null | string ;
  Â Â Â Â signText: null | string ;
  Â Â Â Â signType: null | number ;
}
```
## Properties
### `cityId`

```typescript
cityId: null | number
```
### `direction`

```typescript
direction: null | string
```
### `englishName`

```typescript
englishName: null | string
```
### `id`

```typescript
id: number
```
### `isEmpty`

```typescript
isEmpty: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: null | string
```
### `signText`

```typescript
signText: null | string
```
### `signType`

```typescript
signType: null | number
```

---

# index.SDK.Subscription

---
title: SDK.Subscription interface
source: interfaces/index.SDK.Subscription.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Subscription

```typescript
interface Subscription {
  Â Â Â Â id: string ;
  Â Â Â Â name: string ;
}
```
## Properties
### `id`

```typescript
id: string
```
### `name`

```typescript
name: string
```

---

# index.SDK.Suggestion

---
title: SDK.Suggestion interface
source: interfaces/index.SDK.Suggestion.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Suggestion

```typescript
interface Suggestion {
  Â Â Â Â createdOn: null | number ;
  Â Â Â Â edits: SuggestionEntityEdit [] ;
  Â Â Â Â id: string ;
  Â Â Â Â resolutionData: SuggestionResolution [] ;
}
```
Represents a suggestion for an edit.
## Properties
### `createdOn`

```typescript
createdOn: null | number
```
### `edits`

```typescript
edits: SuggestionEntityEdit []
```
### `id`

```typescript
id: string
```
### `resolutionData`

```typescript
resolutionData: SuggestionResolution []
```

---

# index.SDK.SuggestionAttributeChange

---
title: SDK.SuggestionAttributeChange interface
source: interfaces/index.SDK.SuggestionAttributeChange.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionAttributeChange<T>

```typescript
interface SuggestionAttributeChange < T = unknown > {
  Â Â Â Â id: string ;
  Â Â Â Â name: string ;
  Â Â Â Â newValue: T ;
  Â Â Â Â objectType: ObjectType ;
  Â Â Â Â oldValue: T ;
  Â Â Â Â timestamp: null | number ;
}
```
Represents a single attribute change in an edit suggestion change.
## Properties
### `id`

```typescript
id: string
```
### `name`

```typescript
name: string
```
### `newValue`

```typescript
newValue: T
```
### `objectType`

```typescript
objectType: ObjectType
```
### `oldValue`

```typescript
oldValue: T
```
### `timestamp`

```typescript
timestamp: null | number
```

---

# index.SDK.SuggestionEntityEdit

---
title: SDK.SuggestionEntityEdit interface
source: interfaces/index.SDK.SuggestionEntityEdit.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionEntityEdit

```typescript
interface SuggestionEntityEdit {
  Â Â Â Â actionType: SuggestibleActionType ;
  Â Â Â Â objectId: null | string | number ;
  Â Â Â Â objectType: ObjectType ;
}
```
Represents an edit to an entity within a suggestion.
## Properties
### `actionType`

```typescript
actionType: SuggestibleActionType
```
### `objectId`

```typescript
objectId: null | string | number
```
### `objectType`

```typescript
objectType: ObjectType
```

---

# index.SDK.SuggestionResolution

---
title: SDK.SuggestionResolution interface
source: interfaces/index.SDK.SuggestionResolution.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionResolution

```typescript
interface SuggestionResolution {
  Â Â Â Â createdBy: null | string ;
  Â Â Â Â createdOn: number ;
  Â Â Â Â rejectionReason: null | SuggestionResolutionRejectionReason ;
  Â Â Â Â resolution: SuggestionResolutionStatus ;
}
```
Represents the resolution details for a suggestion.
## Properties
### `createdBy`

```typescript
createdBy: null | string
```
### `createdOn`

```typescript
createdOn: number
```
### `rejectionReason`

```typescript
rejectionReason: null | SuggestionResolutionRejectionReason
```
### `resolution`

```typescript
resolution: SuggestionResolutionStatus
```

---

# index.SDK.TileLayerOptions

---
title: SDK.TileLayerOptions interface
source: interfaces/index.SDK.TileLayerOptions.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TileLayerOptions

```typescript
interface TileLayerOptions {
  Â Â Â Â tileHeight: number ;
  Â Â Â Â tileWidth: number ;
  Â Â Â Â url: {
  Â Â Â Â Â Â Â Â fileName: string ;
  Â Â Â Â Â Â Â Â params ?: Record < string , unknown > ;
  Â Â Â Â Â Â Â Â servers: string [] ;
  Â Â Â Â } ;
}
```
#### Members
| Name | Type/Value | Tags |
|------|------------|------|
| fileName | string |  |
| params | string | Optional |
| servers | string |  |
## Properties
### `tileHeight`

```typescript
tileHeight: number
```
### `tileWidth`

```typescript
tileWidth: number
```
### `url`

```typescript
url: { fileName: string ; params ?: Record < string , unknown > ; servers: string [] }
```

---

# index.SDK.TrackedDataModel

---
title: SDK.TrackedDataModel interface
source: interfaces/index.SDK.TrackedDataModel.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TrackedDataModel

```typescript
interface TrackedDataModel {
  Â Â Â Â events: {
  Â Â Â Â Â Â Â Â "objects-state-deleted": (
  Â Â Â Â Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â Â Â Â Â ) = > void ;
  Â Â Â Â Â Â Â Â objectsadded: (
  Â Â Â Â Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â Â Â Â Â ) = > void ;
  Â Â Â Â Â Â Â Â objectschanged: (
  Â Â Â Â Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â Â Â Â Â ) = > void ;
  Â Â Â Â Â Â Â Â "objectschanged-id": ( changedIds: ChangedIDsInfo ) = > void ;
  Â Â Â Â Â Â Â Â objectsremoved: (
  Â Â Â Â Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â Â Â Â Â ) = > void ;
  Â Â Â Â Â Â Â Â objectssynced: (
  Â Â Â Â Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â Â Â Â Â ) = > void ;
  Â Â Â Â } ;
}
```
## Properties
### `events`

```typescript
events: {
  Â Â Â Â "objects-state-deleted": (
  Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â ) = > void ;
  Â Â Â Â objectsadded: (
  Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â ) = > void ;
  Â Â Â Â objectschanged: (
  Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â ) = > void ;
  Â Â Â Â "objectschanged-id": ( changedIds: ChangedIDsInfo ) = > void ;
  Â Â Â Â objectsremoved: (
  Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â ) = > void ;
  Â Â Â Â objectssynced: (
  Â Â Â Â Â Â Â Â objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  Â Â Â Â ) = > void ;
}
```

---

# index.SDK.TrackedLayer

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

---

# index.SDK.Turn

---
title: SDK.Turn interface
source: interfaces/index.SDK.Turn.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Turn

```typescript
interface Turn {
  Â Â Â Â fromSegmentFwd: boolean ;
  Â Â Â Â fromSegmentId: number ;
  Â Â Â Â hasCustomTTS: boolean ;
  Â Â Â Â hasShieldsPopulated: boolean ;
  Â Â Â Â hasTowardsGuidance: boolean ;
  Â Â Â Â hasTurnGuidance: boolean ;
  Â Â Â Â hasVisualInstruction: boolean ;
  Â Â Â Â id: string ;
  Â Â Â Â instructionOpCode: null | InstructionOpCode ;
  Â Â Â Â isAllowed: boolean ;
  Â Â Â Â isJunctionBoxTurn: boolean ;
  Â Â Â Â isPathTurn: boolean ;
  Â Â Â Â isUTurn: boolean ;
  Â Â Â Â lanes: null | TurnLanes ;
  Â Â Â Â restrictions: BaseRestriction [] ;
  Â Â Â Â segmentPath: number [] ;
  Â Â Â Â toSegmentFwd: boolean ;
  Â Â Â Â toSegmentId: number ;
}
```
## Properties
### `fromSegmentFwd`

```typescript
fromSegmentFwd: boolean
```
### `fromSegmentId`

```typescript
fromSegmentId: number
```
### `hasCustomTTS`

```typescript
hasCustomTTS: boolean
```
### `hasShieldsPopulated`

```typescript
hasShieldsPopulated: boolean
```
### `hasTowardsGuidance`

```typescript
hasTowardsGuidance: boolean
```
### `hasTurnGuidance`

```typescript
hasTurnGuidance: boolean
```
### `hasVisualInstruction`

```typescript
hasVisualInstruction: boolean
```
### `id`

```typescript
id: string
```
### `instructionOpCode`

```typescript
instructionOpCode: null | InstructionOpCode
```
### `isAllowed`

```typescript
isAllowed: boolean
```
### `isJunctionBoxTurn`

```typescript
isJunctionBoxTurn: boolean
```
### `isPathTurn`

```typescript
isPathTurn: boolean
```
### `isUTurn`

```typescript
isUTurn: boolean
```
### `lanes`

```typescript
lanes: null | TurnLanes
```
### `restrictions`

```typescript
restrictions: BaseRestriction []
```
### `segmentPath`

```typescript
segmentPath: number []
```
### `toSegmentFwd`

```typescript
toSegmentFwd: boolean
```
### `toSegmentId`

```typescript
toSegmentId: number
```

---

# index.SDK.TurnClosure

---
title: SDK.TurnClosure interface
source: interfaces/index.SDK.TurnClosure.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnClosure

```typescript
interface TurnClosure {
  Â Â Â Â description: null | string ;
  Â Â Â Â endDate: null | string ;
  Â Â Â Â fromSegmentId: number ;
  Â Â Â Â id: string ;
  Â Â Â Â majorTrafficEventId: null | string ;
  Â Â Â Â modificationData: ModificationMetadata ;
  Â Â Â Â startDate: null | string ;
  Â Â Â Â status: ClosureStatus ;
  Â Â Â Â toSegmentId: number ;
}
```
## Properties
### `description`

```typescript
description: null | string
```
### `endDate`

```typescript
endDate: null | string
```
### `fromSegmentId`

```typescript
fromSegmentId: number
```
### `id`

```typescript
id: string
```
### `majorTrafficEventId`

```typescript
majorTrafficEventId: null | string
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `startDate`

```typescript
startDate: null | string
```
### `status`

```typescript
status: ClosureStatus
```
### `toSegmentId`

```typescript
toSegmentId: number
```

---

# index.SDK.TurnLanes

---
title: SDK.TurnLanes interface
source: interfaces/index.SDK.TurnLanes.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnLanes

```typescript
interface TurnLanes {
  Â Â Â Â angleOverride: null | number ;
  Â Â Â Â arrowAngle: null | number ;
  Â Â Â Â fromLaneIndex: number ;
  Â Â Â Â guidanceMode: LaneGuidanceMode ;
  Â Â Â Â instructionStrategy: LaneInstructionStrategy ;
  Â Â Â Â toLaneIndex: number ;
}
```
## Properties
### `angleOverride`

```typescript
angleOverride: null | number
```
### `arrowAngle`

```typescript
arrowAngle: null | number
```
### `fromLaneIndex`

```typescript
fromLaneIndex: number
```
### `guidanceMode`

```typescript
guidanceMode: LaneGuidanceMode
```
### `instructionStrategy`

```typescript
instructionStrategy: LaneInstructionStrategy
```
### `toLaneIndex`

```typescript
toLaneIndex: number
```

---

# index.SDK.TurnRestriction

---
title: SDK.TurnRestriction interface
source: interfaces/index.SDK.TurnRestriction.html
created: 2026-03-08
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnRestriction

```typescript
interface TurnRestriction {
  driveProfiles: DriveProfiles ;
  isExpired: boolean ;
}
```
## Properties

---

# index.SDK.UpdateRequestDetails

---
title: SDK.UpdateRequestDetails interface
source: interfaces/index.SDK.UpdateRequestDetails.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UpdateRequestDetails

```typescript
interface UpdateRequestDetails {
  Â Â Â Â comments: ConversationElement [] ;
  Â Â Â Â driveGeometry: null | MultiLineString ;
  Â Â Â Â id: number ;
}
```
## Properties
### `comments`

```typescript
comments: ConversationElement []
```
### `driveGeometry`

```typescript
driveGeometry: null | MultiLineString
```
### `id`

```typescript
id: number
```

---

# index.SDK.UpdateRequestUserPreferences

---
title: SDK.UpdateRequestUserPreferences interface
source: interfaces/index.SDK.UpdateRequestUserPreferences.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UpdateRequestUserPreferences

```typescript
interface UpdateRequestUserPreferences {
  Â Â Â Â activeHovSubscriptions: string [] ;
  Â Â Â Â avoidDangerousTurns: null | boolean ;
  Â Â Â Â avoidFerries: null | boolean ;
  Â Â Â Â avoidPrimaryRoads: null | boolean ;
  Â Â Â Â avoidTollRoads: null | boolean ;
  Â Â Â Â hasEv: null | boolean ;
  Â Â Â Â isEmailVerified: null | boolean ;
  Â Â Â Â language: null | string ;
  Â Â Â Â licensePlateSuffix: null | string ;
  Â Â Â Â os: null | string ;
  Â Â Â Â unpavedRoads: null | UnpavedRoadsSetting ;
  Â Â Â Â vehicleType: null | VehicleType ;
}
```
## Properties
### `activeHovSubscriptions`

```typescript
activeHovSubscriptions: string []
```
### `avoidDangerousTurns`

```typescript
avoidDangerousTurns: null | boolean
```
### `avoidFerries`

```typescript
avoidFerries: null | boolean
```
### `avoidPrimaryRoads`

```typescript
avoidPrimaryRoads: null | boolean
```
### `avoidTollRoads`

```typescript
avoidTollRoads: null | boolean
```
### `hasEv`

```typescript
hasEv: null | boolean
```
### `isEmailVerified`

```typescript
isEmailVerified: null | boolean
```
### `language`

```typescript
language: null | string
```
### `licensePlateSuffix`

```typescript
licensePlateSuffix: null | string
```
### `os`

```typescript
os: null | string
```
### `unpavedRoads`

```typescript
unpavedRoads: null | UnpavedRoadsSetting
```
### `vehicleType`

```typescript
vehicleType: null | VehicleType
```

---

# index.SDK.UserProfile

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

---

# index.SDK.UserSession

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

---

# index.SDK.UserSettings

---
title: SDK.UserSettings interface
source: interfaces/index.SDK.UserSettings.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserSettings

```typescript
interface UserSettings {
  Â Â Â Â isCompactMode: boolean ;
  Â Â Â Â isCreateRoadsAsTwoWay: boolean ;
  Â Â Â Â isCreateRoadsWithAllTurnsAllowed: boolean ;
  Â Â Â Â isDisplayTransparentTurnArrows: boolean ;
  Â Â Â Â isImperial ?: boolean ;
  Â Â Â Â isSelectOnlyOnEmptySelection: boolean ;
  Â Â Â Â isSpreadOverlappingTurnArrows: boolean ;
}
```
User settings set in the settings tab of the WME UI
## Properties
### `isCompactMode`

```typescript
isCompactMode: boolean
```
### `isCreateRoadsAsTwoWay`

```typescript
isCreateRoadsAsTwoWay: boolean
```
### `isCreateRoadsWithAllTurnsAllowed`

```typescript
isCreateRoadsWithAllTurnsAllowed: boolean
```
### `isDisplayTransparentTurnArrows`

```typescript
isDisplayTransparentTurnArrows: boolean
```
### **Optional** `isImperial`

```typescript
isImperial ?: boolean
```
### `isSelectOnlyOnEmptySelection`

```typescript
isSelectOnlyOnEmptySelection: boolean
```
### `isSpreadOverlappingTurnArrows`

```typescript
isSpreadOverlappingTurnArrows: boolean
```

---

# index.SDK.Venue

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

---

# index.SDK.VenueAddress

---
title: SDK.VenueAddress interface
source: interfaces/index.SDK.VenueAddress.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueAddress

```typescript
interface VenueAddress {
  Â Â Â Â city: null | City ;
  Â Â Â Â country: null | Country ;
  Â Â Â Â houseNumber: null | string ;
  Â Â Â Â isEmpty: boolean ;
  Â Â Â Â state: null | State ;
  Â Â Â Â street: null | Street ;
}
```
## Properties
### `houseNumber`

```typescript
houseNumber: null | string
```

---

# index.SDK.VenueCategory

---
title: SDK.VenueCategory interface
source: interfaces/index.SDK.VenueCategory.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueCategory

```typescript
interface VenueCategory {
  Â Â Â Â id: VenueCategoryId ;
  Â Â Â Â localizedName: string ;
}
```
## Properties
### `id`

```typescript
id: VenueCategoryId
```
### `localizedName`

```typescript
localizedName: string
```

---

# index.SDK.VenueImage

---
title: SDK.VenueImage interface
source: interfaces/index.SDK.VenueImage.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueImage

```typescript
interface VenueImage {
  Â Â Â Â creationDate: number ;
  Â Â Â Â id: string ;
  Â Â Â Â isApproved: boolean ;
  Â Â Â Â url: string ;
}
```
## Properties
### `creationDate`

```typescript
creationDate: number
```
### `id`

```typescript
id: string
```
### `isApproved`

```typescript
isApproved: boolean
```
### `url`

```typescript
url: string
```

---

# index.SDK.VenueSubCategory

---
title: SDK.VenueSubCategory interface
source: interfaces/index.SDK.VenueSubCategory.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueSubCategory

```typescript
interface VenueSubCategory {
  Â Â Â Â categoryId: VenueCategoryId ;
  Â Â Â Â localizedName: string ;
  Â Â Â Â subCategoryId: VenueCategoryId ;
}
```
## Properties
### `categoryId`

```typescript
categoryId: VenueCategoryId
```
### `localizedName`

```typescript
localizedName: string
```
### `subCategoryId`

```typescript
subCategoryId: VenueCategoryId
```

---

# index.SDK.VenueUpdateRequest

---
title: SDK.VenueUpdateRequest interface
source: interfaces/index.SDK.VenueUpdateRequest.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueUpdateRequest

```typescript
interface VenueUpdateRequest {
  Â Â Â Â changedFields ?: ChangedField [] ;
  Â Â Â Â createdBy: null | string ;
  Â Â Â Â dateAdded: number ;
  Â Â Â Â id: null | string | number ;
  Â Â Â Â subject: PLACE_UPDATE_SUBJECT ;
  Â Â Â Â updateType: PlaceUpdateType ;
}
```
## Properties
### **Optional** `changedFields`

```typescript
changedFields ?: ChangedField []
```
### `createdBy`

```typescript
createdBy: null | string
```
### `dateAdded`

```typescript
dateAdded: number
```
### `id`

```typescript
id: null | string | number
```
### `subject`

```typescript
subject: PLACE_UPDATE_SUBJECT
```
### `updateType`

```typescript
updateType: PlaceUpdateType
```

---

