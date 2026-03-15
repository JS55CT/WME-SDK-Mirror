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
