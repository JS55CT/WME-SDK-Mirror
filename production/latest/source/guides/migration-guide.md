# Waze Map Editor JavaScript SDK: Migration & Prompt Guide

> **Audience:** Tampermonkey script authors, front-end developers, AI-assisted code porters

---

## Description
The Waze Map Editor (WME) JavaScript SDK provides a seamless way to execute community userscripts over the WME.

Using the SDK allows scripts to query the WME data model, interact with the map, read application settings, apply changes to features, register to events and more.

**Features**
- Powerful Functionality: Access capabilities of the WME directly from your JavaScript code.
- Easy Integration: Get up and running quickly with our intuitive API.
- Well-Documented: Comprehensive documentation and examples to help you every step of the way.
- Community Support: Join our active community for help and discussions.

**Usage**
This SDK provides a structured and convenient way for userscripts to interact with and extend the functionality of the Waze Map Editor (WME). It offers a collection of modules and methods that streamline common tasks and facilitate seamless integration of custom scripts within the WME environment.

The following example shows how to initialize the SDK in your script:

### Initialize the SDK

```javascript
window.SDK_INITIALIZED.then(initScript);

function initScript() {
  const sdk = getWmeSdk({
    scriptId: "your-userscript-id",
    scriptName: "Script Display Name"
  });
  // Now, use sdk.* modules for all further interaction!
}
```
---

### Example: Query Data

```javascript
const center = sdk.Map.getMapCenter();
const segment = sdk.DataModel.Segments.getById({ segmentId: 123 });
```

---

## Events

| Event                                 | Description |
|----------------------------------------|-------------|
| **wme-initialized** | Dispatched when WME has initialized the `window.W` global object and its internals, and the UI has been rendered. Note that at this point, map data has not yet been fetched. |
| **wme-logged-in** | Dispatched after the `wme-initialized` event when WME fetches the user info of the currently logged-in user, or after the user logs in using the login form. |
| **wme-logged-out** | Dispatched when the user logs out of WME. |
| **wme-map-data-loaded** | Dispatched after the `wme-initialized` event whenever WME fetches map data from the server (e.g. when the user scrolls the map, changes the zoom level, or presses the refresh button). This is similar to the `mergeend` event triggered on `W.model`. |
| **wme-ready** | Dispatched only once, after the `wme-initialized`, `wme-logged-in`, and `wme-map-data-loaded` events have been dispatched. |
| **wme-selection-changed** | Dispatched when some entity gets selected or unselected on the map. |
| **wme-feature-editor-opened** | Dispatched when the feature editor is opened in the side panel with a new feature. Note: This means the feature editor is ready in the side panel. While you'll usually see it on screen, there's no guarantee--there might be a slight delay before it's actually visible. |
| **wme-map-zoom-changed** | Dispatched when the map is zoomed in or out. |
| **wme-map-layer-added** | Dispatched when a new layer is added to the map. |
| **wme-map-layer-changed** | Dispatched when a layer on the map changes visibility or name. |
| **wme-map-layer-removed** | Dispatched when a layer is removed from the map. |
| **wme-map-mouse-down** | Dispatched when the mouse button is pressed while the pointer is inside the map. |
| **wme-map-mouse-move** | Dispatched when the mouse is moved over the map. This event is continuously fired while moving the mouse. |
| **wme-map-mouse-up** | Dispatched when the mouse button is released while the pointer is inside the map. |
| **wme-map-move** | Dispatched when the map is panned. This event is continuously fired during pan. |
| **wme-map-move-end** | Dispatched when a map move is complete. |
| **wme-user-settings-changed** | Dispatched when WME user settings have changed. |
| **wme-save-finished** | Dispatched when the save attempt has been done by the user. The event is dispatched for both successful and failed save. The event detail contains a `success` boolean parameter which is true for a successful save and false otherwise. |
| **wme-layer-checkbox-toggled** | Dispatched when the custom Map layers checkbox, registered by the script, was toggled. The event detail contains the name of the checkbox and a `checked` parameter which is true if the checkbox became checked and false otherwise. |
| **wme-editing-house-numbers** | **[DEPRECATED - Use wme-map-house-number-marker-added instead]** Dispatched when the user starts or stops editing house numbers. |
| **wme-map-house-number-marker-added** | Dispatched when the user clicks and adds a house number marker to the map. |
| **wme-house-number-added** | Dispatched when a house number is added. |
| **wme-house-number-deleted** | Dispatched when a house number is deleted. |
| **wme-house-number-moved** | Dispatched when a house number is moved. |
| **wme-house-number-updated** | Dispatched when a house number is updated. |
| **wme-after-edit** | Dispatched after user performs a create/edit/delete of an object. |
| **wme-after-redo-clear** | Dispatched after user performs any new edit while being able to redo previous edits. |
| **wme-after-undo** | Dispatched after WME user performs an undo. |
| **wme-no-edits** | Dispatched after WME user performs the last undo or save indicating no edits left to be able to undo or save. |
| **wme-save-mode-changed** | Dispatched when the current state of the save button is changed. The event detail contains a `saveMode` parameter with current save mode. |
| **wme-update-request-panel-opened** | Dispatched when WME user clicks on the map update request or the map update request map marker. |
| **wme-street-view-panel-visibility-changed** | Dispatched when the street view panel changes its visibility. |
| **wme-street-view-button-activated** | Dispatched when WME user starts dragging the street view button. |
| **wme-street-view-button-deactivated** | Dispatched after WME user stops dragging the street view button. |

### Example: Registering to these events is done via the sdk.Events module:

```javascript
sdk.Events.once({ eventName: "wme-ready" }).then(() => {
  console.log("WME is initialized, user is logged in and map data loaded");
});
sdk.Events.on({
  eventName: "wme-map-data-loaded",
  eventHandler: () => {
    console.log("new data loaded");
  },
});
sdk.Events.on({
  eventName: "wme-map-zoom-changed",
  eventHandler: () => {
    sdk.Map.getZoomLevel();
  },
});
sdk.Events.on({
  eventName: "wme-user-settings-changed",
  eventHandler: () => {
    sdk.Settings.getUserSettings().isImperial;
  },
});
```

---

## Data model events

| Event                                 | Description |
|----------------------------------------|-------------|
| **wme-data-model-objects-added**       | Dispatched when objects have been added to a tracked model. |
| **wme-data-model-objects-changed**     | Dispatched when the attributes of an object or objects in a tracked model have been changed. |
| **wme-data-model-objects-removed**     | Dispatched when objects have been removed from a tracked model. |
| **wme-data-model-objects-saved**       | Dispatched when objects in a tracked data model have been saved to the server. |
| **wme-data-model-object-changed-id**   | Dispatched when an object ID in a tracked data model has been changed. |
| **wme-data-model-object-state-deleted**| Dispatched when objects have been marked as deleted but are not removed from the tracked data model. |


To listen to model events, they need to be activated first. The activation is done for each model individually via the sdk.Events module:

```javascript
sdk.Events.trackDataModelEvents({ dataModelName: "venues" });
```

After the events are activated for the model they can be handled in the same way as the global events:

```javascript
sdk.Events.on({
  eventName: "wme-data-model-objects-added",
  eventHandler: ({dataModelName, objectIds}) => { ... },
});
```

---

### Example: Add Features and Save

```javascript
sdk.DataModel.Venues.addVenue({ category, geometry });
sdk.Editing.save().then(() => { /* edits saved */ });
```

---

### TypeScript Types

**Install:**

```bash
npm install --save-dev https://web-assets.waze.com/wme_sdk_docs/production/latest/wme-sdk-typings.tgz
```

**Import:**

```typescript
import { WmeSDK } from "wme-sdk-typings";
```

---

# 🔄 Migration Guide: From WME Internals W. to the SDK

WME SDK provides structured modules to replace legacy usages.

| Pre-SDK Usage                                                               | SDK Method / Module                                                                                                         |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **W.accelerators**                                                          | Use methods in `Shortcuts` module                                                                                          |
| **W.app.getAppRegionCode**                                                   | Use `Settings.getRegionCode`                                                                                               |
| **W.Config.venues.categories** <br> **W.Config.venues.subcategories** <br> **W.model.categoryBrands** | `DataModel.Venues` contains methods for getting venue categories as well as category brands                                |
| **W.Config.user_profile.url**                                                | Use `DataModel.Users.getUserProfileLink`                                                                                   |
| **W.controller.reloadData**                                                  | Use `DataModel.refreshData`                                                                                                |
| **W.controller.save**                                                        | Use `Editing.save`                                                                                                         |
| **W.loginManager.user**                                                      | Use `State.userInfo` to get the logged in user information                                                                 |
| **W.loginManager.isLoggedIn**                                                | `State.userInfo` will be null if a user is not logged in                                                                   |
| **W.map.\***                                                                | The `Map` module contains methods to interact and query with the map, such as center, zoom, adding/removing layers, drawing, and more.<br>See the Map module documentation for details |
| **W.map.events**                                                             | The events `wme-map-zoom-changed`, `wme-map-move`, `wme-map-move-end` are triggered by the SDK                             |
| **W.model.*.on** / **W.model.*.off**                                         | Use the `Events` module which allows tracking changes in a data model                                                      |
| **W.model.*.getObjectArray** / **W.model.*.objects**                         | Use `DataModel.*.getAll`                                                                                                   |
| **W.model.*.getObjectById**                                                  | Use `DataModel.*.getById`                                                                                                  |
| **W.model.getTopCountry**                                                    | Use `DataModel.Countries.getTopCountry`                                                                                    |
| **W.model.getTopState**                                                      | Use `DataModel.States.getTopState`                                                                                         |
| **W.model.isImperial**                                                       | Use `Settings.getUserSettings().isImperial`                                                                                |
| **W.model.isLeftHand**                                                       | Use `isLeftHandTraffic` attribute on the Country SDK interface                                                             |
| **W.model.getTurnGraph**                                                     | Use methods in `DataModel.Turns`                                                                                           |
| **W.prefs.get** / **W.prefs.set** / **W.prefs.attributes**                   | Use `Settings.getUserSettings`, `Settings.setUserSettings`                                                                 |
| **W.prefs.on("change")**                                                     | Register to the event `wme-user-settings-changed` triggered by the SDK                                                     |
| **W.selectionManager.getSelectedFeatures** / **W.selectionManager.setSelectedModels** | The `Editing` module contains methods to get and set selected features. See the Editing module documentation for details   |
| **W.selectionManager.events**                                                | The event `wme-selection-changed` is triggered by the SDK when selection has changed                                       |
| **W.userscripts.state**                                                      | Use `State` included on the SDK instance                                                                                   |
| **W.userscripts.registerSidebarTab**                                         | Use `Sidebar.registerScriptTab`                                                                                            |
| **W.userscripts.waitForElementConnected**                                    | Not required, as the SDK method `Sidebar.registerScriptTab` returns a Promise which resolves when tabLabel & tabPane elements are in the DOM |
| **W.app.on('change:loadingIssueTrackerMapData', callback);**                 | Use `wme-map-data-loaded` event to determine whether the map data is loaded                                                |

## Usages of Waze/Action/*'

In general, the SDK will provide abstractions over actions and expose methods to update data models via their relevant modules.

| Pre-SDK Usage           | SDK Method / Module                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------|
| **AddAlternateStreet**  | Use `DataModel.Segments.addAlternateStreet`                                                |
| **AddLandmark**         | Use `DataModel.Venues.addVenue`                                                            |
| **AddOrGetCity**        | Use `DataModel.Cities.getCity` / `DataModel.Cities.addCity`                                |
| **AddOrGetStreet**      | Use `DataModel.Streets.getStreet` / `DataModel.Streets.addStreet`                         |
| **AddSegment**          | Use `DataModel.Segments.addSegment`                                                        |
| **CreateRoundabout**    | Use `DataModel.Segments.createRoundabout`                                                  |
| **DeleteSegment**       | Use `DataModel.Segments.deleteSegment`                                                     |
| **MergeSegments**       | Use `DataModel.Segments.mergeSegments`                                                     |
| **UpdateFeatureAddress**| Use `DataModel.Segments.updateAddress` / `DataModel.Venues.updateAddress`                  |

## Usages of OpenLayers or OL

| Pre-SDK Usage                                                                              | SDK Method / Module                                                                           |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **OpenLayers.Control.DrawFeature**                                                          | Use `Map.draw*` methods                                                                       |
| **OpenLayers.Geometry.LineString** <br> **OpenLayers.Geometry.Point** <br> **OpenLayers.Geometry.Polygon** | Use `Map.addFeatureToLayer` to add features or `Map.draw*` to draw                             |
| **OpenLayers.Layer.Vector** <br> **OpenLayers.Feature.Vector**                              | Use `Map.addLayer` & `Map.addFeatureToLayer`                                                  |
| **OpenLayers.Style** <br> **OpenLayers.StyleMap** <br> **OpenLayers.Rule**                  | Use `Map.addLayer` with style object                                                          |
| **OpenLayers.LonLat**                                                                      | SDK works with plain JS objects: `{ lon: number; lat: number; }`                              |

---

### Example: Migrating Segment Lookup

**Old:**

```javascript
const seg = W.model.segments.getById(123);
if (seg.isAtoB) { /* ... */ }
```

**New:**

```javascript
const mySegment = sdk.DataModel.Segments.getById({ segmentId: 123 });
if (mySegment.isAtoB) { /* ... */ }
```

---

#### Migrating complex geometry with Turf.js

```javascript
import { flatten } from "@turf/flatten";

// Example: Flatten MultiPolygon for SDK
const multiPolygonFeature = {
  type: "Feature",
  properties: { foo: "bar" },
  geometry: {
    type: "MultiPolygon",
    coordinates: [
      [
        [
          [0,0], [1,0], [1,1], [0,1], [0,0]
        ]
      ],
      [
        [
          [2,2], [3,2], [3,3], [2,3], [2,2]
        ]
      ],
    ]
  }
};

const flattened = flatten(multiPolygonFeature);

const featuresToAdd = flattened.features.map((feature, index) => ({
  geometry: feature.geometry,
  id: `complex-geometry-${index}`,
  properties: feature.properties,
  type: feature.type,
}));

sdk.Map.addFeaturesToLayer({
  features: featuresToAdd,
  layerName: "your_layer_name",
});
```

---

### Example: Migrating Settings & Preferences

**Old:**

```javascript
W.prefs.get("units")
W.prefs.set("units", "imperial")
```

**New:**

```javascript
sdk.Settings.getUserSettings();
sdk.Settings.setUserSettings({ units: "imperial" });
```

---

### Example: Migrating Selection Events

**Old:**

```javascript
W.selectionManager.events.on("selectionChanged", handler);
```

**New:**

```javascript
sdk.Events.on({
  eventName: "wme-selection-changed",
  eventHandler: handler
});
```

---

### Example: Sidebar Tab Registration

**Old:**

```javascript
W.userscripts.registerSidebarTab("MyTab", function(node) { ... });
```

**New:**

```javascript
sdk.Sidebar.registerScriptTab({ 
  tabLabel: "MyTab", 
  tabPane: node 
})
  .then(({ tabLabel, tabPane }) => { /* add UI as needed */ });
```

---

## 💡 AI Prompt Engineering Tips

### Best Practices

- **Set the developer role/context:**  
  _You are a front-end web developer maintaining a Tampermonkey userscript for Waze Map Editor. You are migrating it to use the WME SDK._

- **Ask for specific, incremental changes:**  
  _Find one usage of W.model and rewrite it using the SDK._

- **Ask for code output with explanations:**  
  _Output before-and-after code and describe the migration._

- **Stepwise migration:**  
  Migrate initialization first, then data queries, then map and geometry handling, then event listeners.

- **For geometry conversions:**  
  Replace OpenLayers geometry with Turf.js and SDK calls.

---

### Example Migration Prompts

- **Initialize the SDK**  
  Initialize the WME SDK instance correctly and expose it for other functions in the userscript.

- **Migrate segment queries**  
  Change `W.model.segments.getById` usages to the SDK equivalent and explain the change.

- **Convert OpenLayers code**  
  Identify one use of OpenLayers and convert it to Turf.js and a relevant SDK map method.

---

#### Example Ideal Output From LLM

> I replaced `W.model.segments.getById(123)` with `sdk.DataModel.Segments.getById({ segmentId: 123 })`.

**Initialization code:**

```javascript
window.SDK_INITIALIZED.then(initScript);

function initScript() {
  const sdk = getWmeSdk({
    scriptId: "your-id",
    scriptName: "My Script"
  });
}
```

---

## 🛠 Troubleshooting Common Issues

- **SDK doesn't initialize:**  
  Script may execute too early.  
  Use `@run-at document-end` in Tampermonkey.
- **If using GM_* grants:**  
  Add `@grant unsafeWindow` and use `unsafeWindow.SDK_INITIALIZED`.

```javascript
document.addEventListener("DOMContentLoaded", () => {
  window.SDK_INITIALIZED.then(initScript); // works!
});
```

If using GM\_* grants:

```javascript
// @grant GM_setClipboard
// @grant unsafeWindow

unsafeWindow.SDK_INITIALIZED.then(initScript); // works!
```
