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
