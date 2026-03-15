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
