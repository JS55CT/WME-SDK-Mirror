---
title: SDK.SdkEventBus class
source: classes/index.SDK.SdkEventBus.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class SdkEventBus

```typescript
clear () : void
```
Event bus for SDK events. For the list of events and their payload checkSdkEvents.
## Methods
### `clear`

```typescript
clear () : void
```

### `off`

```typescript
off < EventName extends keyof SdkEvents > (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â eventHandler: EventHandler < SdkEvents [ EventName ] > ;
  Â Â Â Â Â Â Â Â eventName: EventName ;
  Â Â Â Â } ,
  ) : void
```

### `on`

```typescript
on < EventName extends keyof SdkEvents > (
  Â Â Â Â args: {
  Â Â Â Â Â Â Â Â eventHandler: EventHandler < SdkEvents [ EventName ] > ;
  Â Â Â Â Â Â Â Â eventName: EventName ;
  Â Â Â Â } ,
  ) : () = > void
```
a cleanup function that will unregister the handler from the event.
### `once`

```typescript
once < EventName extends keyof SdkEvents > (
  Â Â Â Â args: { eventName: EventName } ,
  ) : Promise < SdkEvents [ EventName ] >
```
a promise that gets resolved once the event happens.
### `stopDataModelEventsTracking`

```typescript
stopDataModelEventsTracking ( args: { dataModelName: DataModelName } ) : void
```

### `stopLayerEventsTracking`

```typescript
stopLayerEventsTracking ( args: { layerName: string } ) : void
```

### `trackDataModelEvents`

```typescript
trackDataModelEvents ( args: { dataModelName: DataModelName } ) : void
```

### `trackLayerEvents`

```typescript
trackLayerEvents ( args: { layerName: string } ) : void
```
