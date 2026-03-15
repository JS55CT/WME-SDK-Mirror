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
