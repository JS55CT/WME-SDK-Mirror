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
