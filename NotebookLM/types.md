# index.SDK.BBox

---
title: SDK.BBox type
source: types/index.SDK.BBox.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias BBox

```typescript
BBox: 
  Â Â Â Â | [ number , number , number , number ]
  Â Â Â Â | [ number , number , number , number , number , number ]
```

---

# index.SDK.CameraType

---
title: SDK.CameraType type
source: types/index.SDK.CameraType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias CameraType

```typescript
CameraType: 
  Â Â Â Â | "BUS_LANE"
  Â Â Â Â | "CARPOOL_LANE"
  Â Â Â Â | "DISTANCE"
  Â Â Â Â | "DUMMY"
  Â Â Â Â | "HOV_LANE"
  Â Â Â Â | "MOBILE_PHONE"
  Â Â Â Â | "NOISE"
  Â Â Â Â | "RED_LIGHT"
  Â Â Â Â | "SEATBELT"
  Â Â Â Â | "SPEED"
  Â Â Â Â | "STOP"
```

---

# index.SDK.ChargersAccessType

---
title: SDK.ChargersAccessType type
source: types/index.SDK.ChargersAccessType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ChargersAccessType

```typescript
ChargersAccessType: 
  Â Â Â Â | "CHARGERS_ACCESS_TYPE_UNKNOWN"
  Â Â Â Â | "PRIVATE"
  Â Â Â Â | "PUBLIC"
  Â Â Â Â | "RESTRICTED"
```

---

# index.SDK.ChargingStationCostType

---
title: SDK.ChargingStationCostType type
source: types/index.SDK.ChargingStationCostType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ChargingStationCostType

```typescript
ChargingStationCostType: "COST_TYPE_UNSPECIFIED" | "FEE" | "FREE"
```

---

# index.SDK.ClosureStatus

---
title: SDK.ClosureStatus type
source: types/index.SDK.ClosureStatus.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ClosureStatus

```typescript
ClosureStatus: 
  Â Â Â Â | "ACTIVE"
  Â Â Â Â | "FINISHED"
  Â Â Â Â | "FINISHED_EARLY_DUE_TO_DELETION"
  Â Â Â Â | "FINISHED_EARLY_DUE_TO_OVERLAPPING_CLOSURES"
  Â Â Â Â | "NOT_STARTED"
  Â Â Â Â | "SUSPENDED"
  Â Â Â Â | "UNVERIFIED"
  Â Â Â Â | "FAILED"
  Â Â Â Â | "UNKNOWN"
```

---

# index.SDK.DataModelName

---
title: SDK.DataModelName type
source: types/index.SDK.DataModelName.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias DataModelName

```typescript
DataModelName: Values < typeof DATA_MODEL_NAMES >
```

---

# index.SDK.DriveProfiles

---
title: SDK.DriveProfiles type
source: types/index.SDK.DriveProfiles.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias DriveProfiles

```typescript
DriveProfiles: { [ key in RESTRICTION_TYPE ] : DriveProfile [] }
```

---

# index.SDK.EditSuggestionSource

---
title: SDK.EditSuggestionSource type
source: types/index.SDK.EditSuggestionSource.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias EditSuggestionSource

```typescript
EditSuggestionSource: "CLIENT" | "GEO" | "OTHER" | "WME"
```

---

# index.SDK.EditSuggestionStatus

---
title: SDK.EditSuggestionStatus type
source: types/index.SDK.EditSuggestionStatus.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias EditSuggestionStatus

```typescript
EditSuggestionStatus: Values < typeof EditSuggestionStatus >
```

---

# index.SDK.Extract

---
title: SDK.Extract type
source: types/index.SDK.Extract.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Extract<T, U>

```typescript
Extract: T extends U ? T: never
```

---

# index.SDK.GENERAL_SERVICE_TYPE

---
title: SDK.GENERAL_SERVICE_TYPE type
source: types/index.SDK.GENERAL_SERVICE_TYPE.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias GENERAL_SERVICE_TYPE

```typescript
GENERAL_SERVICE_TYPE: Values < typeof GENERAL_SERVICE_TYPE >
```

---

# index.SDK.InstructionOpCode

---
title: SDK.InstructionOpCode type
source: types/index.SDK.InstructionOpCode.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias InstructionOpCode

```typescript
InstructionOpCode: 
  Â Â Â Â | typeof CONTINUE
  Â Â Â Â | typeof EXIT_LEFT
  Â Â Â Â | typeof EXIT_RIGHT
  Â Â Â Â | typeof KEEP_LEFT
  Â Â Â Â | typeof KEEP_RIGHT
  Â Â Â Â | typeof NONE
  Â Â Â Â | typeof ROUNDABOUT_ENTER
  Â Â Â Â | typeof TURN_LEFT
  Â Â Â Â | typeof TURN_RIGHT
  Â Â Â Â | typeof UTURN
```

---

# index.SDK.IssueSeverity

---
title: SDK.IssueSeverity type
source: types/index.SDK.IssueSeverity.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias IssueSeverity

```typescript
IssueSeverity: "low" | "medium" | "high"
```

---

# index.SDK.LaneGuidanceMode

---
title: SDK.LaneGuidanceMode type
source: types/index.SDK.LaneGuidanceMode.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias LaneGuidanceMode

```typescript
LaneGuidanceMode: "default" | "display" | "display-and-voice"
```

---

# index.SDK.LaneInstructionStrategy

---
title: SDK.LaneInstructionStrategy type
source: types/index.SDK.LaneInstructionStrategy.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias LaneInstructionStrategy

```typescript
LaneInstructionStrategy: "default" | "pull" | "push"
```

---

# index.SDK.LotType

---
title: SDK.LotType type
source: types/index.SDK.LotType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias LotType

```typescript
LotType: "MULTI_LEVEL" | "STREET_LEVEL" | "STREET_LEVEL_COVERED" | "UNDERGROUND"
```

---

# index.SDK.MajorTrafficEventCategory

---
title: SDK.MajorTrafficEventCategory type
source: types/index.SDK.MajorTrafficEventCategory.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias MajorTrafficEventCategory

```typescript
MajorTrafficEventCategory: 
  Â Â Â Â | "CONCERT"
  Â Â Â Â | "CONSTRUCTION"
  Â Â Â Â | "CRISIS"
  Â Â Â Â | "DEMONSTRATION"
  Â Â Â Â | "DRIVING_ADVISORY"
  Â Â Â Â | "HOLIDAY/FESTIVAL"
  Â Â Â Â | "OTHER"
  Â Â Â Â | "PARADE"
  Â Â Â Â | "SPORTING_EVENT"
  Â Â Â Â | "SUMMIT"
  Â Â Â Â | "PARTNER_USER_COMMS"
  Â Â Â Â | "UNPLANNED_DISRUPTION"
```

---

# index.SDK.MapProblemType

---
title: SDK.MapProblemType type
source: types/index.SDK.MapProblemType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias MapProblemType

```typescript
MapProblemType: "DATA" | "DISCONNECTION" | "ROAD_CLOSURE" | "TURN"
```

---

# index.SDK.OLMouseEventName

---
title: SDK.OLMouseEventName type
source: types/index.SDK.OLMouseEventName.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias OLMouseEventName

```typescript
OLMouseEventName: "click" | "mousedown" | "mouseup" | "mousemove" | "mouseout"
```

---

# index.SDK.ObjectType

---
title: SDK.ObjectType type
source: types/index.SDK.ObjectType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ObjectType

```typescript
ObjectType: Values < typeof ObjectType >
```

---

# index.SDK.PARKING_LOT_SERVICE_TYPE

---
title: SDK.PARKING_LOT_SERVICE_TYPE type
source: types/index.SDK.PARKING_LOT_SERVICE_TYPE.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PARKING_LOT_SERVICE_TYPE

```typescript
PARKING_LOT_SERVICE_TYPE: Values < typeof PARKING_LOT_SERVICE_TYPE >
```

---

# index.SDK.PLACE_UPDATE_ACTION

---
title: SDK.PLACE_UPDATE_ACTION type
source: types/index.SDK.PLACE_UPDATE_ACTION.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PLACE_UPDATE_ACTION

```typescript
PLACE_UPDATE_ACTION: Values < typeof PLACE_UPDATE_ACTION >
```

---

# index.SDK.PLACE_UPDATE_SUBJECT

---
title: SDK.PLACE_UPDATE_SUBJECT type
source: types/index.SDK.PLACE_UPDATE_SUBJECT.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PLACE_UPDATE_SUBJECT

```typescript
PLACE_UPDATE_SUBJECT: Values < typeof PLACE_UPDATE_SUBJECT >
```

---

# index.SDK.ParkingLotCostType

---
title: SDK.ParkingLotCostType type
source: types/index.SDK.ParkingLotCostType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ParkingLotCostType

```typescript
ParkingLotCostType: "FREE" | "LOW" | "MODERATE" | "EXPENSIVE" | "UNKNOWN"
```

---

# index.SDK.ParkingType

---
title: SDK.ParkingType type
source: types/index.SDK.ParkingType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ParkingType

```typescript
ParkingType: "PRIVATE" | "PUBLIC" | "RESTRICTED" | null
```

---

# index.SDK.Partial

---
title: SDK.Partial type
source: types/index.SDK.Partial.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Partial<T>

```typescript
Partial: { [ P in keyof T ] ?: T [ P ] }
```

---

# index.SDK.PaymentMethod

---
title: SDK.PaymentMethod type
source: types/index.SDK.PaymentMethod.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PaymentMethod

```typescript
PaymentMethod: 
  Â Â Â Â | "APP"
  Â Â Â Â | "CREDIT"
  Â Â Â Â | "DEBIT"
  Â Â Â Â | "MEMBERSHIP_CARD"
  Â Â Â Â | "ONLINE_PAYMENT"
  Â Â Â Â | "OTHER"
  Â Â Â Â | "PAYMENT_METHOD_UNKNOWN"
  Â Â Â Â | "PLUG_IN_AUTO_CHARGE"
```

---

# index.SDK.PaymentType

---
title: SDK.PaymentType type
source: types/index.SDK.PaymentType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PaymentType

```typescript
PaymentType: 
  Â Â Â Â | "CASH"
  Â Â Â Â | "CHECKS"
  Â Â Â Â | "CREDIT"
  Â Â Â Â | "DEBIT_CARD"
  Â Â Â Â | "DIGITAL_WALLET"
  Â Â Â Â | "ELECTRONIC_PASS"
  Â Â Â Â | "MEMBERSHIP"
  Â Â Â Â | "PARKING_APP"
  Â Â Â Â | "PERMIT"
  Â Â Â Â | "PREPAID"
  Â Â Â Â | "SMS_CALL"
```

---

# index.SDK.Pick

---
title: SDK.Pick type
source: types/index.SDK.Pick.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Pick<T, K>

```typescript
Pick: { [ P in K ] : T [ P ] }
```

---

# index.SDK.PlaceUpdateType

---
title: SDK.PlaceUpdateType type
source: types/index.SDK.PlaceUpdateType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PlaceUpdateType

```typescript
PlaceUpdateType: ` ${ PLACE_UPDATE_ACTION } _ ${ PLACE_UPDATE_SUBJECT } ` | "flag"
```

---

# index.SDK.Position

---
title: SDK.Position type
source: types/index.SDK.Position.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Position

```typescript
Position: number []
```

---

# index.SDK.RESTRICTION_TYPE

---
title: SDK.RESTRICTION_TYPE type
source: types/index.SDK.RESTRICTION_TYPE.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias RESTRICTION_TYPE

```typescript
RESTRICTION_TYPE: Values < typeof RESTRICTION_TYPE >
```

---

# index.SDK.Record

---
title: SDK.Record type
source: types/index.SDK.Record.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Record<K, T>

```typescript
Record: { [ P in K ] : T }
```

---

# index.SDK.RegionCode

---
title: SDK.RegionCode type
source: types/index.SDK.RegionCode.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias RegionCode

```typescript
RegionCode: 
  Â Â Â Â | typeof REGION_CODE_USA
  Â Â Â Â | typeof REGION_CODE_ROW
  Â Â Â Â | typeof REGION_CODE_IL
```

---

# index.SDK.RestrictionSegmentDirection

---
title: SDK.RestrictionSegmentDirection type
source: types/index.SDK.RestrictionSegmentDirection.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias RestrictionSegmentDirection

```typescript
RestrictionSegmentDirection: "BOTH" | "FWD" | "REV"
```

---

# index.SDK.RoadTypeId

---
title: SDK.RoadTypeId type
source: types/index.SDK.RoadTypeId.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias RoadTypeId

```typescript
RoadTypeId: Values < typeof ROAD_TYPE >
```

---

# index.SDK.SaveMode

---
title: SDK.SaveMode type
source: types/index.SDK.SaveMode.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SaveMode

```typescript
SaveMode: "DISALLOWED" | "EDITING" | "IDLE" | "SUGGESTING"
```

---

# index.SDK.SdkFeatureGeometry

---
title: SDK.SdkFeatureGeometry type
source: types/index.SDK.SdkFeatureGeometry.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkFeatureGeometry

```typescript
SdkFeatureGeometry: Point | LineString | Polygon
```

---

# index.SDK.SdkFeatureProperties

---
title: SDK.SdkFeatureProperties type
source: types/index.SDK.SdkFeatureProperties.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkFeatureProperties

```typescript
SdkFeatureProperties: Record <
  Â Â Â Â string ,
  Â Â Â Â string
  Â Â Â Â | number
  Â Â Â Â | null
  Â Â Â Â | undefined
  Â Â Â Â | SdkFeatureGeometry ,
  >
```

---

# index.SDK.SdkFeatureStyleContext

---
title: SDK.SdkFeatureStyleContext type
source: types/index.SDK.SdkFeatureStyleContext.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkFeatureStyleContext

```typescript
SdkFeatureStyleContext: Record <
  Â Â Â Â string ,
  Â Â Â Â (
  Â Â Â Â Â Â Â Â context: { feature ?: SdkWazeFeature ; zoomLevel: number } ,
  Â Â Â Â ) = > string | number | undefined ,
  >
```

---

# index.SDK.SdkFeatureStylePredicate

---
title: SDK.SdkFeatureStylePredicate type
source: types/index.SDK.SdkFeatureStylePredicate.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkFeatureStylePredicate

```typescript
SdkFeatureStylePredicate: (
  Â Â Â Â properties: SdkFeatureProperties ,
  Â Â Â Â zoomLevel: number ,
  ) = > boolean
```

---

# index.SDK.SdkMouseEventName

---
title: SDK.SdkMouseEventName type
source: types/index.SDK.SdkMouseEventName.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkMouseEventName

```typescript
SdkMouseEventName: 
  Â Â Â Â | typeof SDK_EVENT_NAME.MAP_MOUSE_CLICK
  Â Â Â Â | typeof SDK_EVENT_NAME.MAP_MOUSE_DOWN
  Â Â Â Â | typeof SDK_EVENT_NAME.MAP_MOUSE_UP
  Â Â Â Â | typeof SDK_EVENT_NAME.MAP_MOUSE_MOVE
  Â Â Â Â | typeof SDK_EVENT_NAME.MAP_MOUSE_OUT
```

---

# index.SDK.SegmentDirection

---
title: SDK.SegmentDirection type
source: types/index.SDK.SegmentDirection.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SegmentDirection

```typescript
SegmentDirection: Values < typeof SegmentDirection >
```

---

# index.SDK.SegmentLaneGuidanceDirection

---
title: SDK.SegmentLaneGuidanceDirection type
source: types/index.SDK.SegmentLaneGuidanceDirection.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SegmentLaneGuidanceDirection

```typescript
SegmentLaneGuidanceDirection: Extract < SegmentDirection , "A_TO_B" | "B_TO_A" >
```

---

# index.SDK.SegmentPermission

---
title: SDK.SegmentPermission type
source: types/index.SDK.SegmentPermission.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SegmentPermission

```typescript
SegmentPermission: Values < typeof SegmentPermission >
```

---

# index.SDK.Selection

---
title: SDK.Selection type
source: types/index.SDK.Selection.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Selection

```typescript
Selection: 
  Â Â Â Â | { ids: number [] ; objectType: typeof SEGMENT }
  Â Â Â Â | { ids: string [] ; objectType: typeof VENUE }
  Â Â Â Â | { ids: number [] ; objectType: typeof BIG_JUNCTION }
  Â Â Â Â | { ids: number [] ; objectType: typeof CITY }
  Â Â Â Â | { ids: string [] ; objectType: typeof MAP_COMMENT }
  Â Â Â Â | { ids: number [] ; objectType: typeof NODE }
  Â Â Â Â | { ids: number [] ; objectType: typeof PERMANENT_HAZARD }
  Â Â Â Â | { ids: number [] ; objectType: typeof RESTRICTED_DRIVING_AREA }
  Â Â Â Â | { ids: number [] ; objectType: typeof SEGMENT_SUGGESTION }
```

---

# index.SDK.SelectionWithLocalizedTypeName

---
title: SDK.SelectionWithLocalizedTypeName type
source: types/index.SDK.SelectionWithLocalizedTypeName.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SelectionWithLocalizedTypeName

```typescript
SelectionWithLocalizedTypeName: Selection & { localizedTypeName: string }
```

---

# index.SDK.ServiceType

---
title: SDK.ServiceType type
source: types/index.SDK.ServiceType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ServiceType

```typescript
ServiceType: GENERAL_SERVICE_TYPE | PARKING_LOT_SERVICE_TYPE
```

---

# index.SDK.SidebarTabName

---
title: SDK.SidebarTabName type
source: types/index.SDK.SidebarTabName.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SidebarTabName

```typescript
SidebarTabName: Values < typeof SidebarTabName >
```

---

# index.SDK.SnapTo

---
title: SDK.SnapTo type
source: types/index.SDK.SnapTo.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SnapTo

```typescript
SnapTo: "segment" | "none"
```

---

# index.SDK.SpotsEstimate

---
title: SDK.SpotsEstimate type
source: types/index.SDK.SpotsEstimate.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SpotsEstimate

```typescript
SpotsEstimate: 
  Â Â Â Â | "R_1_TO_10"
  Â Â Â Â | "R_11_TO_30"
  Â Â Â Â | "R_31_TO_60"
  Â Â Â Â | "R_61_TO_100"
  Â Â Â Â | "R_101_TO_300"
  Â Â Â Â | "R_301_TO_600"
  Â Â Â Â | "R_600_PLUS"
```

---

# index.SDK.SuggestibleActionType

---
title: SDK.SuggestibleActionType type
source: types/index.SDK.SuggestibleActionType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SuggestibleActionType

```typescript
SuggestibleActionType: "ADD" | "DELETE" | "UPDATE" | "SPLIT"
```

---

# index.SDK.SuggestionResolutionRejectionReason

---
title: SDK.SuggestionResolutionRejectionReason type
source: types/index.SDK.SuggestionResolutionRejectionReason.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SuggestionResolutionRejectionReason

```typescript
SuggestionResolutionRejectionReason: 
  Â Â Â Â | "EDIT_IS_WRONG"
  Â Â Â Â | "EDIT_NOT_ALIGNED_TO_GUIDELINES"
  Â Â Â Â | "GENERAL_NO_LONGER_RELEVANT"
  Â Â Â Â | "GENERAL_OTHER"
  Â Â Â Â | "EDIT_ABUSE"
  Â Â Â Â | "EDIT_LOW_QUALITY"
```

---

# index.SDK.SuggestionResolutionStatus

---
title: SDK.SuggestionResolutionStatus type
source: types/index.SDK.SuggestionResolutionStatus.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SuggestionResolutionStatus

```typescript
SuggestionResolutionStatus: 
  Â Â Â Â | "ACCEPTED"
  Â Â Â Â | "OPEN"
  Â Â Â Â | "REJECTED"
  Â Â Â Â | "REJECTED_APPEALABLE"
```

---

# index.SDK.UnpavedRoadsSetting

---
title: SDK.UnpavedRoadsSetting type
source: types/index.SDK.UnpavedRoadsSetting.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UnpavedRoadsSetting

```typescript
UnpavedRoadsSetting: "ALLOW" | "DISALLOW" | "AVOID_LONG_ONES"
```

---

# index.SDK.UpdateRequestSource

---
title: SDK.UpdateRequestSource type
source: types/index.SDK.UpdateRequestSource.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UpdateRequestSource

```typescript
UpdateRequestSource: "MOBILE_CLIENT" | "MOBILE_WEB" | "WEB" | "REPORTING_AGENT"
```

---

# index.SDK.UpdateRequestType

---
title: SDK.UpdateRequestType type
source: types/index.SDK.UpdateRequestType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UpdateRequestType

```typescript
UpdateRequestType: 
  Â Â Â Â | "BLOCKED_ROAD"
  Â Â Â Â | "INCORRECT_ADDRESS"
  Â Â Â Â | "INCORRECT_GENERAL_ERROR"
  Â Â Â Â | "INCORRECT_JUNCTION"
  Â Â Â Â | "INCORRECT_MISSING_ROUNDABOUT"
  Â Â Â Â | "INCORRECT_ROUTE"
  Â Â Â Â | "INCORRECT_TURN"
  Â Â Â Â | "MISSING_BRIDGE_OVERPASS"
  Â Â Â Â | "MISSING_EXIT"
  Â Â Â Â | "MISSING_ROAD"
  Â Â Â Â | "TURN_NOT_ALLOWED"
  Â Â Â Â | "WRONG_DRIVING_DIRECTIONS"
```

---

# index.SDK.UpdateableMapProblemState

---
title: SDK.UpdateableMapProblemState type
source: types/index.SDK.UpdateableMapProblemState.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UpdateableMapProblemState

```typescript
UpdateableMapProblemState: Values < typeof UpdateableMapProblemState >
```

---

# index.SDK.UserRank

---
title: SDK.UserRank type
source: types/index.SDK.UserRank.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UserRank

```typescript
UserRank: 0 | 1 | 2 | 3 | 4 | 5 | 6
```

---

# index.SDK.VehicleType

---
title: SDK.VehicleType type
source: types/index.SDK.VehicleType.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VehicleType

```typescript
VehicleType: 
  Â Â Â Â | "BUS"
  Â Â Â Â | "CAV"
  Â Â Â Â | "CLEAN_FUEL"
  Â Â Â Â | "EV"
  Â Â Â Â | "HAZARDOUS_MATERIALS"
  Â Â Â Â | "HOV_2"
  Â Â Â Â | "HOV_3"
  Â Â Â Â | "HYBRID"
  Â Â Â Â | "MOTORCYCLE"
  Â Â Â Â | "PRIVATE"
  Â Â Â Â | "PUBLIC_TRANSPORTATION"
  Â Â Â Â | "RV"
  Â Â Â Â | "TAXI"
  Â Â Â Â | "TOWING_VEHICLE"
  Â Â Â Â | "TRUCK"
```

---

# index.SDK.VenueCategoryId

---
title: SDK.VenueCategoryId type
source: types/index.SDK.VenueCategoryId.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueCategoryId

```typescript
VenueCategoryId: VenueSubCategoryId | VenueResidentialId | VenueMainCategoryId
```

---

# index.SDK.VenueMainCategoryId

---
title: SDK.VenueMainCategoryId type
source: types/index.SDK.VenueMainCategoryId.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueMainCategoryId

```typescript
VenueMainCategoryId: Values < typeof VENUE_MAIN_CATEGORY >
```

---

# index.SDK.VenuePermission

---
title: SDK.VenuePermission type
source: types/index.SDK.VenuePermission.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenuePermission

```typescript
VenuePermission: Values < typeof VenuePermission >
```

---

# index.SDK.VenueResidentialId

---
title: SDK.VenueResidentialId type
source: types/index.SDK.VenueResidentialId.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueResidentialId

```typescript
VenueResidentialId: typeof VENUE_RESIDENTIAL
```

---

# index.SDK.VenueSubCategoryId

---
title: SDK.VenueSubCategoryId type
source: types/index.SDK.VenueSubCategoryId.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueSubCategoryId

```typescript
VenueSubCategoryId: ArrayElement < Values < typeof VENUE_SUBCATEGORIES > >
```

---

# index.SDK.WME_LAYER_NAMES

---
title: SDK.WME_LAYER_NAMES type
source: types/index.SDK.WME_LAYER_NAMES.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias WME_LAYER_NAMES

```typescript
WME_LAYER_NAMES: Values < typeof WME_LAYER_NAMES >
```

---

# index.SDK.ZoomLevel

---
title: SDK.ZoomLevel type
source: types/index.SDK.ZoomLevel.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ZoomLevel

```typescript
ZoomLevel: 
  Â Â Â Â | 4
  Â Â Â Â | 5
  Â Â Â Â | 6
  Â Â Â Â | 7
  Â Â Â Â | 8
  Â Â Â Â | 9
  Â Â Â Â | 10
  Â Â Â Â | 11
  Â Â Â Â | 12
  Â Â Â Â | 13
  Â Â Â Â | 14
  Â Â Â Â | 15
  Â Â Â Â | 16
  Â Â Â Â | 17
  Â Â Â Â | 18
  Â Â Â Â | 19
  Â Â Â Â | 20
  Â Â Â Â | 21
  Â Â Â Â | 22
```

---

