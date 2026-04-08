
# How to get started with the WME SDK

# Prerequisites
Before starting, ensure you have:
- **Tampermonkey extension** installed in your browser ([Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/), [Edge](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd))
- Basic familiarity with browser developer tools (F12) for viewing console messages
- Access to the Waze Map Editor (requires a Waze account with editor permissions)

# Starting Your Script
When creating user scripts for the Waze Map Editor (WME), you must either create a browser extension or a user script that can be installed through Greasemonkey or Tampermonkey. Tampermonkey is the recommended extension due to recent changes in how Greasemonkey functions.

This guide focuses on scripts installed via Tampermonkey. Creating browser extensions is similar, but a separate topic. We'll build a simple script to demonstrate the basics of interacting with the Waze object and the WME SDK.

## Tampermonkey Script Headers
Every Tampermonkey script begins with a special header block that tells the browser extension:
- **What** the script does (@name, @description)
- **Where** it should run (@include, @exclude)
- **What permissions** it needs (@grant)
- **How to identify** it for updates (@namespace, @version)

Here is a sample default header:

```javascript
// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://*/*
// @grant        none
// ==/UserScript==
```
> 💡 **Learn More**: [Greasy Fork's rules for posted scripts!](https://greasyfork.org/en/help/code-rules)

Here you’ll assign a script name, set a namespace (often your GreasyFork profile link for auto-updates), add version, description, author, and specify what pages the script will run on.

Here’s an example for from the WME Wazebar Script:

```javascript
// ==UserScript==
// @name         WME Wazebar
// @namespace    https://greasyfork.org/users/30701-justins83-waze
// @version      2025.05.30.01
// @description  Displays a bar at the top of the editor that displays inbox, forum & wiki links
// @author       JustinS83
// @include      https://beta.waze.com/*
// @include      https://www.waze.com/discuss/*
// @include      https://webnew.waze.com/discuss/*
// @include      https://www.waze.com/editor*
// @include      https://www.waze.com/*/editor*
// @exclude      https://www.waze.com/user/editor*
// @require      https://greasyfork.org/scripts/27254-clipboard-js/code/clipboardjs.js
// @connect      storage.googleapis.com
// @connect      greasyfork.org
// @grant        none
// ==/UserScript==
```

Best practice: Use @exclude for any pages you do not want your script to run on to avoid unexpected issues.

> 💡 **Learn More**: [User Script Meta Keys!](https://greasyfork.org/en/help/meta-keys)

For your first script, use this header:
```javascript
// ==UserScript==
// @name         WazeDev First Script              // Display name in Tampermonkey dashboard
// @namespace    http://tampermonkey.net/          // Unique identifier (use your GreasyFork profile for updates)
// @version      0.1                               // Version number for update tracking
// @description  Learning to script!               // Brief description of functionality
// @author       You                               // Your name or username
// @include      https://beta.waze.com/*           // Run on beta WME (testing environment)
// @include      https://www.waze.com/editor*      // Run on production WME
// @include      https://www.waze.com/*/editor*    // Run on localized WME URLs
// @exclude      https://www.waze.com/user/editor* // Don't run on user profile pages
// @exclude      https://www.waze.com/editor/sdk/* // Don't run on SDK documentation
// @grant        none                              // No special permissions needed
// ==/UserScript==
```

This allows your script to run in both production and beta WME, but not on editor profile or SDK pages.

## Boilerplate Script Structure

Below the header, Tampermonkey inserts a wrapper for your script:

```javascript
(function() {
    'use strict';

    // Your code here...
})();
```
Your script logic goes inside this function.

## Bootstrap: Initializing the WME SDK

A bootstrap routine ensures WME and its SDK are fully loaded before your script runs, preventing errors.

**SDK Initialization and Bootstrap Example**

```javascript
const SCRIPT_NAME = GM_info.script.name; // Get the Script name from the @name tag of the UserScript Meta Keys
let wmeSDK; // Declare wmeSDK globally

// Initialization of the WME SDK
if (window.SDK_INITIALIZED) {
    console.log(`${SCRIPT_NAME}: SDK initialized...`);

    window.SDK_INITIALIZED.then(bootstrap).catch((err) => {
        console.error(`${SCRIPT_NAME}: SDK initialization failed`, err);
    });
} else {
    console.warn(`${SCRIPT_NAME}: SDK_INITIALIZED is undefined`);
}

function bootstrap() {
    try {
        wmeSDK = getWmeSdk({
            scriptId: SCRIPT_NAME.replaceAll(" ", ""),
            scriptName: SCRIPT_NAME,
        });

        Promise.all([wmeReady()])
            .then(() => {
                console.log(`${SCRIPT_NAME}: All dependencies are ready.`);
                init();
            })
            .catch((error) => {
                console.error(`${SCRIPT_NAME}: Error during bootstrap`, error);
            });
    } catch (error) {
        console.error(`${SCRIPT_NAME}: Failed to initialize SDK`, error);
    }
}

function wmeReady() {
    return new Promise((resolve) => {
        if (wmeSDK.State.isReady()) {
            console.log(`${SCRIPT_NAME}: WME is ready.`);
            resolve();
        } else {
            console.log(`${SCRIPT_NAME}: Waiting for WME to be ready...`);

            wmeSDK.Events.once({ eventName: "wme-ready" })
                .then(() => {
                    console.log(`${SCRIPT_NAME}: WME is ready now.`);
                    resolve();
                })
                .catch((error) => {
                    console.error(`${SCRIPT_NAME}: Error while waiting for WME to be ready:`, error);
                });
        }
    });
}
```
> 💡 **Learn More**: For complete SDK documentation, visit the [WME SDK Reference Sight](https://www.waze.com/editor/sdk/) 

What this achieves:

1. **SDK Initialization Check**: First, it verifies that `window.SDK_INITIALIZED` exists and waits for the SDK initialization promise to resolve.

2. **WME SDK Setup**: Once the SDK is initialized, the `bootstrap()` function creates the WME SDK instance using `getWmeSdk()` with your script's name and ID.

3. **WME Ready Check**: The `wmeReady()` function ensures the WME environment is fully loaded. This prevents errors that occur when scripts try to access WME data before it's available. The function checks if:
   - WME has initialized completely
   - User authentication is confirmed  
   - Initial map data for the current view has loaded
   - All WME UI components are ready for interaction

4. **Event-Based Waiting**: If WME isn't ready immediately, the script listens for the special "wme-ready" event using `wmeSDK.Events.once()`. This event only fires once after all initialization, login, and initial data loading is complete.

5. **Script Initialization**: Once all dependencies are confirmed ready, the `init()` function is called (you can name this whatever you want). This is where you would set up your script using SDK modules like:
   - `wmeSDK.DataModel` - Access segments, venues, nodes, etc.
   - `wmeSDK.Map` - Control map view and add layers
   - `wmeSDK.Sidebar` - Create custom UI panels
   - `wmeSDK.Events` - Register for WME events
   - `wmeSDK.Settings` - Manage user preferences

# Why Use a Bootstrap Pattern?

You might wonder why we need this seemingly complex initialization process instead of just writing our script code directly. The bootstrap pattern is essential for WME scripts because of how web applications load:

## The Problem: Race Conditions
When a web page loads, many things happen simultaneously:
- The HTML page structure loads
- JavaScript files download and execute  
- The WME application initializes its components
- User authentication occurs
- Map data downloads
- Your userscript starts running

**Without a bootstrap pattern**, your script might try to access WME data or create UI elements before they exist, causing errors like:
```javascript
// ❌ This fails if WME isn't ready yet
const segments = wmeSDK.DataModel.Segments.getAll(); // Error: Cannot read property 'Segments' of undefined
```
## The Solution: Wait for Dependencies
The bootstrap pattern ensures everything your script needs is available before it runs:

- Prevents Crashes: No more "undefined" errors when accessing WME objects
- Reliable Execution: Your script works consistently, regardless of network speed or system performance
- Clean Error Handling: Problems during initialization are caught and logged clearly
- Professional Behavior: Your script behaves predictably for all users

Real-World Analogy
Think of it like cooking a meal:
- Without bootstrap: Start cooking immediately (but the oven might not be preheated, ingredients might not be ready)
- With bootstrap: Wait for the oven to preheat, check all ingredients are available, then start cooking

# Complete First Script
Your script should look like this so far:
```javascript
// ==UserScript==
// @name         WazeDev First Script              // Display name in Tampermonkey dashboard
// @namespace    http://tampermonkey.net/          // Unique identifier (use your GreasyFork profile for updates)
// @version      0.1                               // Version number for update tracking
// @description  Learning to script!               // Brief description of functionality
// @author       You                               // Your name or username
// @include      https://beta.waze.com/*           // Run on beta WME (testing environment)
// @include      https://www.waze.com/editor*      // Run on production WME
// @include      https://www.waze.com/*/editor*    // Run on localized WME URLs
// @exclude      https://www.waze.com/user/editor* // Don't run on user profile pages
// @exclude      https://www.waze.com/editor/sdk/* // Don't run on SDK documentation
// @grant        none                              // No special permissions needed
// ==/UserScript==

(function() {
    'use strict';

    const SCRIPT_NAME = GM_info.script.name; // Get the Script name from the @name tag of the UserScript Meta Keys
    let wmeSDK; // Declare wmeSDK globally

    if (window.SDK_INITIALIZED) {
    console.log(`${SCRIPT_NAME}: SDK initialized...`);
    
    window.SDK_INITIALIZED.then(bootstrap).catch((err) => {
      console.error(`${SCRIPT_NAME}: SDK initialization failed`, err);
    });
  } else {
    console.warn(`${SCRIPT_NAME}: SDK_INITIALIZED is undefined`);
  }

  function bootstrap() {
    try {
      wmeSDK = getWmeSdk({
        scriptId: SCRIPT_NAME.replaceAll(' ', ''),
        scriptName: SCRIPT_NAME,
      });

      Promise.all([wmeReady()])
        .then(() => {
          console.log(`${SCRIPT_NAME}: All dependencies are ready.`);
          init();
        })
        .catch((error) => {
          console.error(`${SCRIPT_NAME}: Error during bootstrap`, error);
        });
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Failed to initialize SDK`, error);
    }
  }

  function wmeReady() {
    return new Promise((resolve) => {
      if (wmeSDK.State.isReady()) {
        console.log(`${SCRIPT_NAME}: WME is ready.`);
        resolve();
      } else {
        console.log(`${SCRIPT_NAME}: Waiting for WME to be ready...`);
        wmeSDK.Events.once({ eventName: 'wme-ready' })
          .then(() => {
            console.log(`${SCRIPT_NAME}: WME is ready now.`);
            resolve();
          })
          .catch((error) => {
            console.error(`${SCRIPT_NAME}: Error while waiting for WME to be ready:`, error);
          });
      }
    });
  }

  function init() {
    // Your code here
    console.log(`${SCRIPT_NAME}: Script initialized successfully!`);
  }

})();
```

Expected console output:

```
WazeDev First Script: SDK initialized...
WazeDev First Script: WME is ready now.
WazeDev First Script: All dependencies are ready.
WazeDev First Script: Script initialized successfully!
```
## Testing Your Script

1. **Install the script** in Tampermonkey
2. **Open WME** in a new tab
3. **Open Developer Tools** (F12) and navigate to the Console tab
4. **Look for your script's messages** - you should see the expected output above

### Common Issues:
- **No console output**: Check that the script is enabled in Tampermonkey dashboard
- **"SDK_INITIALIZED is undefined"**: WME may not have loaded the SDK yet - refresh the page
- **Script not running**: Verify the @include URLs match the WME URL in your address bar

This covers the very basics for getting started on a script.  In the [next section](Creating-our-tab) we will look at setting up a tab in the side panel where our script can create controls to toggle settings.

---

# Creating Our Tab

Now that your script loads properly, let's create a user interface where users can interact with your script. The WME SDK provides several UI locations, but the **sidebar tab** is the most common and user-friendly option.

## Why Use Sidebar Tabs?
- **Familiar Location**: Users expect to find script settings in the sidebar
- **Non-Intrusive**: Doesn't interfere with the main map editing workflow  
- **Organized**: Each script gets its own dedicated space
- **SDK Support**: Built-in methods handle all the complex integration

Now let's create your first sidebar tab using the SDK's `registerScriptTab` method.

## Setting Up the Tab
First, modify the init() method to register your sidebar tab and create an empty `main()` function:

```javascript
function init() {
    console.log(`${SCRIPT_NAME}: Script initialized successfully!`);

    // Build HTML content for our tab
    const section = document.createElement('div');
    section.innerHTML = `
        <div>
            <h2>Our First Script!</h2>
        </div>
    `;

    // Register the script tab using the SDK
    wmeSDK.Sidebar.registerScriptTab()
        .then(({ tabLabel, tabPane }) => {
            tabLabel.textContent = 'WazeDev';
            tabLabel.title = SCRIPT_NAME;
            tabPane.appendChild(section);

            // Initialize the main() function after tab is created
            main();
        })
        .catch((error) => {
            console.error(`${SCRIPT_NAME}: Error creating script tab`, error);
        });
}

function main() {
    // Settings initialization code will go here
    console.log(`${SCRIPT_NAME}: Settings initialized!`);
}
```

## Understanding the Code Structure

### HTML Content Creation

```javascript
const section = document.createElement('div');
section.innerHTML = `
    <div>
        <h2>Our First Script!</h2>
    </div>
`;
```
This creates our tab's content using a [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) (notice the backticks ` ). Template literals allow multi-line strings and variable interpolation, making HTML creation cleaner than string concatenation.

### Promise-Based Tab Registration

```javascript
wmeSDK.Sidebar.registerScriptTab()
    .then(({ tabLabel, tabPane }) => {
        // Success: Tab created successfully
    })
    .catch((error) => {
        // Error: Something went wrong
    });
```
***Why use Promises here?*** Tab creation involves DOM manipulation and potential conflicts with other scripts. The Promise pattern ensures your script handles both success and failure scenarios gracefully.

### Tab Components Explained

When `registerScriptTab()` succeeds, it provides two DOM elements through [destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring):

- **`tabLabel`** - The clickable tab button in the sidebar
  - Set the display name: `tabLabel.textContent = 'WazeDev'`
  - Add hover tooltip: `tabLabel.title = SCRIPT_NAME`
  - Keep names short (8-12 characters work best)

- **`tabPane** - The content area that appears when users click your tab
  - This is where your HTML content goes: `tabPane.appendChild(section)`
  - Can contain any standard HTML: forms, buttons, lists, etc.
  - Styled automatically to match WME's appearance

There are multiple ways to define the HTML for the page - you are not locked into doing it the same as the above example, it is just a way to define the tab HTML.


### Alternative HTML Creation Methods
While we used createElement() and innerHTML, you have several options:

**Method 1: Template Literals (Our Example)**
```javascript
const section = document.createElement('div');
section.innerHTML = `<div><h2>Our First Script!</h2></div>`;
```
Best for: Complex HTML with multiple elements

**Method 2: Pure DOM Methods**
```javascript
const section = document.createElement('div');
const wrapper = document.createElement('div');
const header = document.createElement('h2');
header.textContent = 'Our First Script!';
wrapper.appendChild(header);
section.appendChild(wrapper);
```
Best for: Simple structures or when you need element references

**Method 3: Document Fragments**
```javascript
const fragment = document.createDocumentFragment();
// Build multiple elements, then append fragment
```
Best for: Performance-critical scenarios with many elements

**Method 4: jQuery**
```javascript
const $section = $('<div>').html(`
    <div>
        <h2>Our First Script!</h2>
        <p>Built with jQuery!</p>
    </div>
`);

tabPane.appendChild($section[0]); // Convert jQuery object to DOM element
```
Best for: Developers familiar with jQuery syntax (shorter, more readable code)

In the future choose the method that feels most comfortable for your coding style. But we will use Method 1: Template Literals in this exsample.

## Key Takeaways
This example demonstrates several important WME scripting concepts:
- ✅ **Promise handling** for async SDK operations
- ✅ **DOM manipulation** using modern JavaScript
- ✅ **Error handling** with try/catch patterns
- ✅ **SDK integration** using the sidebar API

These patterns will serve as the foundation for more complex script features.

Your tab should look like the following:

![](https://imgur.com/e1guPAb.png)

### Testing Your Tab

After saving and reloading WME:
1. **Look for your tab** in the left sidebar - it should appear as "WazeDev"
2. **Click the tab** - you should see "Our First Script!" as the header  
3. **Check the console** - you should see: `WazeDev First Script: Settings initialized!`

**Troubleshooting:**
- **Tab doesn't appear**: Check console for errors in the `registerScriptTab()` call
- **Content is blank**: Verify your HTML syntax in the template literal
- **Tab appears but clicking does nothing**: Check that `tabPane.appendChild(section)` executed successfully

> 💡 **Tip**: Use your browser's Element Inspector (F12 → Elements) to examine the generated HTML structure and debug styling issues.

## Complete Script So Far:
```javascript
// ==UserScript==
// @name         WazeDev First Script              // Display name in Tampermonkey dashboard
// @namespace    http://tampermonkey.net/          // Unique identifier (use your GreasyFork profile for updates)
// @version      0.1                               // Version number for update tracking
// @description  Learning to script!               // Brief description of functionality
// @author       You                               // Your name or username
// @include      https://beta.waze.com/*           // Run on beta WME (testing environment)
// @include      https://www.waze.com/editor*      // Run on production WME
// @include      https://www.waze.com/*/editor*    // Run on localized WME URLs
// @exclude      https://www.waze.com/user/editor* // Don't run on user profile pages
// @exclude      https://www.waze.com/editor/sdk/* // Don't run on SDK documentation
// @grant        none                              // No special permissions needed
// ==/UserScript==

(function() {
    'use strict';

    const SCRIPT_NAME = GM_info.script.name; // Get the Script name from the @name tag of the UserScript Meta Keys
    let wmeSDK; // Declare wmeSDK globally

    if (window.SDK_INITIALIZED) {
    console.log(`${SCRIPT_NAME}: SDK initialized...`);
    
    window.SDK_INITIALIZED.then(bootstrap).catch((err) => {
      console.error(`${SCRIPT_NAME}: SDK initialization failed`, err);
    });
  } else {
    console.warn(`${SCRIPT_NAME}: SDK_INITIALIZED is undefined`);
  }

  function bootstrap() {
    try {
      wmeSDK = getWmeSdk({
        scriptId: SCRIPT_NAME.replaceAll(' ', ''),
        scriptName: SCRIPT_NAME,
      });

      Promise.all([wmeReady()])
        .then(() => {
          console.log(`${SCRIPT_NAME}: All dependencies are ready.`);
          init();
        })
        .catch((error) => {
          console.error(`${SCRIPT_NAME}: Error during bootstrap`, error);
        });
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Failed to initialize SDK`, error);
    }
  }

  function wmeReady() {
    return new Promise((resolve) => {
      if (wmeSDK.State.isReady()) {
        console.log(`${SCRIPT_NAME}: WME is ready.`);
        resolve();
      } else {
        console.log(`${SCRIPT_NAME}: Waiting for WME to be ready...`);
        wmeSDK.Events.once({ eventName: 'wme-ready' })
          .then(() => {
            console.log(`${SCRIPT_NAME}: WME is ready now.`);
            resolve();
          })
          .catch((error) => {
            console.error(`${SCRIPT_NAME}: Error while waiting for WME to be ready:`, error);
          });
      }
    });
  }

  function init() {
    console.log(`${SCRIPT_NAME}: Script initialized successfully!`);

    // Build HTML content for our tab
    const section = document.createElement('div');
    section.innerHTML = `
        <div>
            <h2>Our First Script!</h2>
        </div>
    `;

    // Register the script tab using the SDK
    wmeSDK.Sidebar.registerScriptTab()
        .then(({ tabLabel, tabPane }) => {
            tabLabel.textContent = 'WazeDev';
            tabLabel.title = SCRIPT_NAME;
            tabPane.appendChild(section);

            // Initialize the main() function after tab is created
            main();
        })
        .catch((error) => {
            console.error(`${SCRIPT_NAME}: Error creating script tab`, error);
        });
}

function main() {
    // Settings initialization code will go here
    console.log(`${SCRIPT_NAME}: Settings initialized!`);
}

})();
```

In the [next section](Interacting-with-SDK) we will start interacting with the Waze SDK and display some data in our tab.

---

# Interacting with the SDK

With your tab ready, let's display user information by using the SDK. This will demonstrate how to:
- Fetch data from the WME SDK
- Handle asynchronous operations 
- Update the UI dynamically
- Provide user feedback during loading

Learn more at [Waze Map Editor JavaScript SDK](https://www.waze.com/editor/sdk/index.html)

### Getting Basic User Info
Lets pull some User information from the SDK using the `wmeSDK.State.getUserInfo()` method and display it in our tab.

```javascript
const userSession = wmeSDK.State.getUserInfo();
/*
Returns UserSession object:
{
    isAreaManager: boolean;
    isCountryManager: boolean;
    rank: UserRank;
    userName: string;
}
*/
```

As you can see, most of the information isn't too useful for us in terms of creating a WME script - the important bits are already displayed in the User panel within WME. Let's create a small User information section within our script.

### Expanding the Tab HTML

First, we are going to need to change our tab so we have a space to add this information.

```javascript
// Build HTML content for our tab
const section = document.createElement('div');
section.innerHTML = `
    <div>
        <h2>Our First Script!</h2>
        <hr>
        <div>
            <h3>User Info</h3>
            Username: <span id="wazedevUsername"></span><br>
            Rank: <span id="wazedevRank"></span><br>
            Area manager: <span id="wazedevAM"></span><br>
            Country manager: <span id="wazedevCM"></span>
        </div>
    </div>
`;
```
We are adding spans so we can easily dynamically add the values from the SDK's user session and we give them all unique IDs. I like to use the script name (or abbreviation) + a recognizable name for what it is. This serves two purposes:

1. It guarantees the ID we use will be unique (don't want to risk stepping on any other script's toes)
2. If someone wants to see what script is modifying/adding the information, you can see this in the ID of the element.

So, in order to set these values we need to change our `main()` method. This is the method that gets called once the tab has been created in the side panel, by the SDK. 

### Populating the User Information
We'll change our `main()` method to the below in order to fill in the information above.

Populate the user info in `main()`:

```javascript
function main() {
    const userSession = wmeSDK.State.getUserInfo();
    document.getElementById('wazedevUsername').textContent = userSession.userName;
    document.getElementById('wazedevRank').textContent = userSession.rank;
    document.getElementById('wazedevAM').textContent = userSession.isAreaManager ? 'Yes' : 'No';
    document.getElementById('wazedevCM').textContent = userSession.isCountryManager ? 'Yes' : 'No';
    console.log(`${SCRIPT_NAME}: Settings initialized!`);
}
```

### Getting Detailed User Profile Data
The basic user session information is helpful, but what if we want more detailed statistics about a user's editing activity? The WME SDK provides `wmeSDK.DataModel.Users.getUserProfile()` which gives us access to much more comprehensive user data.

`wmeSDK.DataModel.Users.getUserProfile({ userName: "username" })` returns a Promise that resolves to a UserProfile object:

```javascript
const userProfile = await wmeSDK.DataModel.Users.getUserProfile({ userName: userSession.userName });
/*
UserProfile {
    dailyEditCount: number[];
    editCountByType: {
        mapProblems: number;
        placeUpdateRequests: number;
        segmentHouseNumbers: number;
        segments: number;
        updateRequests: number;
        venues: number;
    };
    totalEditCount: number;
}
*/
```
This gives us:
- dailyEditCount: An array of edit counts for the last 90 days (today is the last element)
- editCountByType: A breakdown of edits by category
- totalEditCount: The user's lifetime edit count

The SDK also provides `wmeSDK.DataModel.Users.getUserProfileLink({ userName: "username" })` which returns a direct URL to that user's profile page, allowing us to make the username clickable.  Let's take the user's username from our `userSession` object as the input to getUserProfileLink().

```javascript
const profileLink = wmeSDK.DataModel.Users.getUserProfileLink({ userName: userSession.userName });
```

Expand your tab HTML to display this additional information and make the username a clickable link:

```javascript
const section = document.createElement('div');
section.innerHTML = `
    <div>
        <h2>Our First Script!</h2>
        <hr>
        <section>
            <h3>User Info</h3>
            Username: <a href="#" id="wazedevUsernameLink" target="_blank"><span id="wazedevUsername"></span></a><br>
            Rank: <span id="wazedevRank"></span><br>
            Area manager: <span id="wazedevAM"></span><br>
            Country manager: <span id="wazedevCM"></span>
        </section>
        <hr>
        <section>
            <h3>Detailed Profile</h3>
            <div id="wazedevProfileLoading">Loading profile data...</div>
            <div id="wazedevProfileData" style="display: none;">
                Total Edits: <span id="wazedevTotalEdits"></span><br>
                Today's Edits: <span id="wazedevTodayEdits"></span>
            </div>
        </section>
        <hr>
        <section id="wazedevEditsByType" style="display: none;">
            <h3>Edits by Type</h3>
            Segments: <span id="wazedevSegments"></span><br>
            Venues: <span id="wazedevVenues"></span><br>
            Map Problems: <span id="wazedevMapProblems"></span><br>
            Update Requests: <span id="wazedevUpdateRequests"></span><br>
            Place Update Requests: <span id="wazedevPlaceUpdateRequests"></span><br>
            Segment House Numbers: <span id="wazedevSegmentHouseNumbers"></span>
        </section>
    </div>
`;
```
Notice we've added a loading indicator and initially hide the profile data section. This provides better user experience since the profile data requires an API call that takes time to complete.

### Handling Asynchronous Data
Now we need to update our `main()` method to handle the asynchronous profile data fetching:

```javascript
async function main() {
    const userSession = wmeSDK.State.getUserInfo();

    // Set basic user info
    document.getElementById('wazedevUsername').textContent = userSession.userName;
    document.getElementById('wazedevRank').textContent = userSession.rank;
    document.getElementById('wazedevAM').textContent = userSession.isAreaManager ? 'Yes' : 'No';
    document.getElementById('wazedevCM').textContent = userSession.isCountryManager ? 'Yes' : 'No';

    // Set profile link
    const profileLink = wmeSDK.DataModel.Users.getUserProfileLink({ userName: userSession.userName });
    document.getElementById('wazedevUsernameLink').href = profileLink;

    // Fetch detailed user profile
    try {
        const userProfile = await wmeSDK.DataModel.Users.getUserProfile({ userName: userSession.userName });

        document.getElementById('wazedevProfileLoading').style.display = 'none';
        document.getElementById('wazedevProfileData').style.display = 'block';
        document.getElementById('wazedevEditsByType').style.display = 'block';

        document.getElementById('wazedevTotalEdits').textContent = userProfile.totalEditCount.toLocaleString();
        const todayEdits = userProfile.dailyEditCount[userProfile.dailyEditCount.length - 1] || 0;
        document.getElementById('wazedevTodayEdits').textContent = todayEdits;

        const editTypes = userProfile.editCountByType;
        document.getElementById('wazedevSegments').textContent = editTypes.segments.toLocaleString();
        document.getElementById('wazedevVenues').textContent = editTypes.venues.toLocaleString();
        document.getElementById('wazedevMapProblems').textContent = editTypes.mapProblems.toLocaleString();
        document.getElementById('wazedevUpdateRequests').textContent = editTypes.updateRequests.toLocaleString();
        document.getElementById('wazedevPlaceUpdateRequests').textContent = editTypes.placeUpdateRequests.toLocaleString();
        document.getElementById('wazedevSegmentHouseNumbers').textContent = editTypes.segmentHouseNumbers.toLocaleString();

        console.log(`${SCRIPT_NAME}: Profile data loaded successfully`);

    } catch (error) {
        console.error(`${SCRIPT_NAME}: Error fetching user profile:`, error);
        document.getElementById('wazedevProfileLoading').textContent = 'Error loading profile data';
    }
    console.log(`${SCRIPT_NAME}: Settings initialized!`);
}
```
### Key Changes and Concepts Introduced

**Async/Await Pattern:**
- We changed `main()` to an `async function` to handle the Promise returned by `getUserProfile()`
- **Important:** Not all WME SDK calls return Promises - only some API calls do (like `getUserProfile()`)
- `getUserInfo()` returns data immediately (synchronous), while `getUserProfile()` returns a Promise (asynchronous)
- `await` pauses execution until the Promise resolves, making asynchronous code read like synchronous code

```javascript
// Synchronous SDK calls (immediate data):
const userSession = wmeSDK.State.getUserInfo(); // Returns data immediately
const isReady = wmeSDK.State.isReady(); // Returns boolean immediately

// Asynchronous SDK calls (return Promises):
const userProfile = await wmeSDK.DataModel.Users.getUserProfile({ userName: "user" }); // Returns Promise
const events = await wmeSDK.Events.once({ eventName: 'wme-ready' }); // Returns Promise
```

#### When to Use Async/Await:
- Only use async/await when the SDK method returns a Promise
- Check the SDK documentation to see if a method is asynchronous
- Methods that fetch data from servers (like user profiles) are typically async
- State checking methods (like getUserInfo()) are typically synchronous

#### Error Handling Best Practices:
- We wrap asynchronous API calls in try/catch blocks to handle potential failures
- Synchronous calls can fail too, but they throw errors immediately rather than rejecting Promises
- If an async API call fails, we show a user-friendly error message instead of breaking the script
- This prevents network issues or API changes from crashing your entire script

#### Mixed Sync/Async Pattern:
Our function demonstrates handling both types of SDK calls:

```javascript
async function main() {
    // Synchronous call - no await needed
    const userSession = wmeSDK.State.getUserInfo();
    
    // Use the sync data immediately
    document.getElementById('wazedevUsername').textContent = userSession.userName;
    
    // Asynchronous call - needs await and error handling
    try {
        const userProfile = await wmeSDK.DataModel.Users.getUserProfile({ userName: userSession.userName });
        // Handle async data...
    } catch (error) {
        // Handle async errors...
    }
}
```

#### Progressive UI Updates:
- We show a loading indicator immediately while the async API call is in progress
- Synchronous data (basic user info) appears instantly
- Asynchronous data (detailed profile) appears after the API call completes
- This provides immediate feedback and prevents confusion about whether the script is working


API Call Pattern for WME Scripts:
- Use this pattern based on whether the SDK method returns a Promise:

```javascript
// For synchronous SDK calls:
const data = wmeSDK.Some.synchronousMethod();
document.getElementById('element').textContent = data.property;

// For asynchronous SDK calls:
try {
    const data = await wmeSDK.Some.asynchronousMethod();
    document.getElementById('loading').style.display = 'none';
    document.getElementById('content').textContent = data.property;
} catch (error) {
    console.error('Async call failed:', error);
    document.getElementById('loading').textContent = 'Error loading data';
}
```
#### Testing Your Enhanced Tab

After implementing these changes, your tab should display:
1. **Basic user info** loads immediately (username, rank, manager status)
2. **Loading indicator** appears while fetching detailed profile
3. **Detailed statistics** populate once the API call completes
4. **Clickable username** that opens the user's profile page

**Expected output:**
- Total edits with proper number formatting (e.g., "1,234")
- Today's edit count from the daily array
- Breakdown by edit type with formatted numbers

**Troubleshooting:**
- **"Loading profile data..." never disappears**: Check console for API errors
- **Numbers show as "0"**: User might be new or have no edits in that category
- **Profile link doesn't work**: Verify the username is being passed correctly


### Complete Script So Far
```javascript
// ==UserScript==
// @name         WazeDev First Script              // Display name in Tampermonkey dashboard
// @namespace    http://tampermonkey.net/          // Unique identifier (use your GreasyFork profile for updates)
// @version      0.1                               // Version number for update tracking
// @description  Learning to script!               // Brief description of functionality
// @author       You                               // Your name or username
// @include      https://beta.waze.com/*           // Run on beta WME (testing environment)
// @include      https://www.waze.com/editor*      // Run on production WME
// @include      https://www.waze.com/*/editor*    // Run on localized WME URLs
// @exclude      https://www.waze.com/user/editor* // Don't run on user profile pages
// @exclude      https://www.waze.com/editor/sdk/* // Don't run on SDK documentation
// @grant        none                              // No special permissions needed
// ==/UserScript==

(function () {
  'use strict';

  const SCRIPT_NAME = GM_info.script.name; // Get the Script name from the @name tag of the UserScript Meta Keys
  let wmeSDK; // Declare wmeSDK globally

  if (window.SDK_INITIALIZED) {
    console.log(`${SCRIPT_NAME}: SDK initialized...`);

    window.SDK_INITIALIZED.then(bootstrap).catch((err) => {
      console.error(`${SCRIPT_NAME}: SDK initialization failed`, err);
    });
  } else {
    console.warn(`${SCRIPT_NAME}: SDK_INITIALIZED is undefined`);
  }

  function bootstrap() {
    try {
      wmeSDK = getWmeSdk({
        scriptId: SCRIPT_NAME.replaceAll(' ', ''),
        scriptName: SCRIPT_NAME,
      });

      Promise.all([wmeReady()])
        .then(() => {
          console.log(`${SCRIPT_NAME}: All dependencies are ready.`);
          init();
        })
        .catch((error) => {
          console.error(`${SCRIPT_NAME}: Error during bootstrap`, error);
        });
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Failed to initialize SDK`, error);
    }
  }

  function wmeReady() {
    return new Promise((resolve) => {
      if (wmeSDK.State.isReady()) {
        console.log(`${SCRIPT_NAME}: WME is ready.`);
        resolve();
      } else {
        console.log(`${SCRIPT_NAME}: Waiting for WME to be ready...`);
        wmeSDK.Events.once({ eventName: 'wme-ready' })
          .then(() => {
            console.log(`${SCRIPT_NAME}: WME is ready now.`);
            resolve();
          })
          .catch((error) => {
            console.error(`${SCRIPT_NAME}: Error while waiting for WME to be ready:`, error);
          });
      }
    });
  }

  function init() {
    console.log(`${SCRIPT_NAME}: Script initialized successfully!`);

    // Build HTML content for our tab
    const section = document.createElement('div');
    section.innerHTML = `
    <div>
        <h2>Our First Script!</h2>
        <hr>
        <section>
            <h3>User Info</h3>
            Username: <a href="#" id="wazedevUsernameLink" target="_blank"><span id="wazedevUsername"></span></a><br>
            Rank: <span id="wazedevRank"></span><br>
            Area manager: <span id="wazedevAM"></span><br>
            Country manager: <span id="wazedevCM"></span>
        </section>
        <hr>
        <section>
            <h3>Detailed Profile</h3>
            <div id="wazedevProfileLoading">Loading profile data...</div>
            <div id="wazedevProfileData" style="display: none;">
                Total Edits: <span id="wazedevTotalEdits"></span><br>
                Today's Edits: <span id="wazedevTodayEdits"></span>
            </div>
        </section>
        <hr>
        <section id="wazedevEditsByType" style="display: none;">
            <h3>Edits by Type</h3>
            Segments: <span id="wazedevSegments"></span><br>
            Venues: <span id="wazedevVenues"></span><br>
            Map Problems: <span id="wazedevMapProblems"></span><br>
            Update Requests: <span id="wazedevUpdateRequests"></span><br>
            Place Update Requests: <span id="wazedevPlaceUpdateRequests"></span><br>
            Segment House Numbers: <span id="wazedevSegmentHouseNumbers"></span>
        </section>
    </div>
`;

    // Register the script tab using the SDK
    wmeSDK.Sidebar.registerScriptTab()
      .then(({ tabLabel, tabPane }) => {
        tabLabel.textContent = 'WazeDev';
        tabLabel.title = SCRIPT_NAME;
        tabPane.appendChild(section);

        // Initialize the main() function after tab is created
        main();
      })
      .catch((error) => {
        console.error(`${SCRIPT_NAME}: Error creating script tab`, error);
      });
  }

  async function main() {
    const userSession = wmeSDK.State.getUserInfo();

    // Set basic user info
    document.getElementById('wazedevUsername').textContent = userSession.userName;
    document.getElementById('wazedevRank').textContent = userSession.rank;
    document.getElementById('wazedevAM').textContent = userSession.isAreaManager ? 'Yes' : 'No';
    document.getElementById('wazedevCM').textContent = userSession.isCountryManager ? 'Yes' : 'No';

    // Set profile link
    const profileLink = wmeSDK.DataModel.Users.getUserProfileLink({ userName: userSession.userName });
    document.getElementById('wazedevUsernameLink').href = profileLink;

    // Fetch detailed user profile
    try {
      const userProfile = await wmeSDK.DataModel.Users.getUserProfile({ userName: userSession.userName });

      document.getElementById('wazedevProfileLoading').style.display = 'none';
      document.getElementById('wazedevProfileData').style.display = 'block';
      document.getElementById('wazedevEditsByType').style.display = 'block';

      document.getElementById('wazedevTotalEdits').textContent = userProfile.totalEditCount.toLocaleString();
      const todayEdits = userProfile.dailyEditCount[userProfile.dailyEditCount.length - 1] || 0;
      document.getElementById('wazedevTodayEdits').textContent = todayEdits;

      const editTypes = userProfile.editCountByType;
      document.getElementById('wazedevSegments').textContent = editTypes.segments.toLocaleString();
      document.getElementById('wazedevVenues').textContent = editTypes.venues.toLocaleString();
      document.getElementById('wazedevMapProblems').textContent = editTypes.mapProblems.toLocaleString();
      document.getElementById('wazedevUpdateRequests').textContent = editTypes.updateRequests.toLocaleString();
      document.getElementById('wazedevPlaceUpdateRequests').textContent = editTypes.placeUpdateRequests.toLocaleString();
      document.getElementById('wazedevSegmentHouseNumbers').textContent = editTypes.segmentHouseNumbers.toLocaleString();

      console.log(`${SCRIPT_NAME}: Profile data loaded successfully`);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error fetching user profile:`, error);
      document.getElementById('wazedevProfileLoading').textContent = 'Error loading profile data';
    }
    console.log(`${SCRIPT_NAME}: Settings initialized!`);
  }
})();
```

In the [next section](State-Management-and-Saving-Settings) we add interactivity to our script. We'll add an "Enabled" checkbox that users can toggle on/off, and we'll save this preference so it persists between WME sessions.

---

# State Management and Saving Settings

As your WME scripts grow more complex, you'll want to give users control over how they behave. Most scripts include settings that users can toggle on/off, configure thresholds, or customize behavior. Without proper state management, users would have to reconfigure their preferences every time they reload WME - a poor user experience.

In this section, we'll build a robust settings system that:
- **Persists user preferences** between browser sessions using localStorage
- **Provides immediate feedback** when settings change
- **Scales easily** as you add more options to your script
- **Handles errors gracefully** when storage isn't available

We'll start by adding a simple "Enable/Disable" checkbox to give users control over whether the script is active. This is a common pattern in WME scripts - allowing users to quickly toggle functionality without having to disable the entire script in Tampermonkey.

By the end of this section, you'll have a foundation for settings management that you can expand for any future script features.

---

We'll need to expand our HTML to include a checkbox control, and then set up event listeners to respond to user interactions with our script.

```javascript
// Build HTML content for our tab
const section = document.createElement('div');
section.innerHTML = `
    <div>
        <h2>Our First Script!</h2>
        <section>
            <input type="checkbox" id="wazedevEnabled" class="wazedevSettingsCheckbox">
            <label for="wazedevEnabled">Enable WazeDev Script</label>
        </section>
        <hr>
        <section>
            <h3>User Info</h3>
            Username: <a href="#" id="wazedevUsernameLink" target="_blank"><span id="wazedevUsername"></span></a><br>
            Rank: <span id="wazedevRank"></span><br>
            Area manager: <span id="wazedevAM"></span><br>
            Country manager: <span id="wazedevCM"></span>
        </section>
        <hr>
        <section>
            <h3>Detailed Profile</h3>
            <div id="wazedevProfileLoading">Loading profile data...</div>
            <div id="wazedevProfileData" style="display: none;">
                Total Edits: <span id="wazedevTotalEdits"></span><br>
                Today's Edits: <span id="wazedevTodayEdits"></span>
            </div>
        </section>
        <hr>
        <section id="wazedevEditsByType" style="display: none;">
            <h3>Edits by Type</h3>
            Segments: <span id="wazedevSegments"></span><br>
            Venues: <span id="wazedevVenues"></span><br>
            Map Problems: <span id="wazedevMapProblems"></span><br>
            Update Requests: <span id="wazedevUpdateRequests"></span><br>
            Place Update Requests: <span id="wazedevPlaceUpdateRequests"></span><br>
            Segment House Numbers: <span id="wazedevSegmentHouseNumbers"></span>
        </section>
    </div>
`;
```
## Settings Object and Helper Functions
Now we need to add our state management system. First, let's declare a settings object and helpers in your script's top-level scope:

```javascript
(function() {
    'use strict';

    const SCRIPT_NAME = GM_info.script.name; // Get the Script name from the @name tag of the UserScript Meta Keys
    const STORAGE_KEY = 'wazedev_Settings'; // Local Storage key
    
    let wmeSDK; // Declare wmeSDK globally
    let settings = {}; // Global settings object

    // Initialization of the WME SDK
```
## Save and Load Methods  
With adding this option we are going to want to add a save and load method so we can save this to the browser's `localStorage` and retrieve it into an object that we can use to check against in the script.

Lets start with the save method:
```javascript
// Save settings to localStorage
function saveSettings() {
    try {
        const localSettings = { Enabled: settings.Enabled };
        localStorage.setItem(STORAGE_KEY, JSON.stringify(localSettings));
        console.log(`${SCRIPT_NAME}: Settings saved`, localSettings);
    } catch (error) {
        console.error(`${SCRIPT_NAME}: Error saving settings:`, error);
    }
}

```
We create a saveSettings method and which defines a `localsettings` object which pulls the settings from a `settings` object defined globally in the script. Once the `localsettings` object's settings have been set, set the `localStorage` setting and change the `localsettings` object to JSON as a parameter to the `setItem` method.  Your settings are now stored in localStorage in the browser.  Now we need to handle the user enabling/disabling the Enabled checkebox and save it to our settings.

Now that we have saving set up, lets get loading working.  For this we will create a `loadSettings` method which will retrieve our script's settings from `localStorage`.  To do this we will use JavaScript's built-in JSON.parse() method to parse our `localStorage` settings into an object that we can interact with.  We will then set up an object with default settings, in case a storage object doesn't exist or we have added options to the script that do not exist locally.  We will start with the script disabled, so the user doesn't experience strange behavior after installing/updating (*usually* a good practice, depending on what your script is doing).  Once that is set up, the function will loop the settings object property and add any missing settings to our `settings` object that we will define globally in our script.
```javascript
// Load settings from localStorage
function loadSettings() {
    try {
        const loadedSettings = JSON.parse(localStorage.getItem(STORAGE_KEY));
        const defaultSettings = { Enabled: false };
        settings = loadedSettings ? loadedSettings : defaultSettings;

        // Add missing default settings
        for (const prop in defaultSettings) {
            if (!settings.hasOwnProperty(prop)) {
                settings[prop] = defaultSettings[prop];
            }
        }
        console.log(`${SCRIPT_NAME}: Settings loaded`, settings);
    } catch (error) {
        console.error(`${SCRIPT_NAME}: Error loading settings:`, error);
        settings = { Enabled: false };
    }
}
```
This method should be called once our script's tab is added to the side bar, before set add any event handlers.  To do this, we will call `loadSettings` at the start of the `main` method and then set the Enabled checkbox based on the loaded settings.  In order to set the checkbox state, we will create a helper method called `setChecked` which will make it easy to check/uncheck any checkboxes we use on the settings tab.

## Setting Up Checkbox Event Handling
In order to detect when the user changes the Enabled setting, we will add a handler for the change event for the checkbox. This will automagically pull the settings name from the id that we set and set the settings object to the current checkbox status and then save to localStorage.  This will allow you to add multiple checkboxes with properly named id's and using the "wazedevSettingsCheckbox" class and have the setting be automatically detected and saved, without having to write code to do it for every checkbox.

```javascript
// Setup event handlers for our controls
function setupEventHandlers() {
    const checkboxes = document.querySelectorAll('.wazedevSettingsCheckbox');
    checkboxes.forEach((checkbox) => {
      checkbox.addEventListener('change', function () {
        // Extract the setting name from the checkbox ID by removing the 'wazedev' prefix
        // Example: 'wazedevEnabled' -> 'Enabled'
        const settingName = this.id.substring(7);
        settings[settingName] = this.checked;
        saveSettings();
      });
    });
  }

// Helper to set checkbox state
function setChecked(checkboxId, checked) {
    const checkbox = document.getElementById(checkboxId);
    if (checkbox) checkbox.checked = checked;
}
```
## Updated `main()` with State Logic

Now we need to update our `main()` function to load settings, set the checkbox state, and add event handlers:

```javascript
async function main() {
    // Load saved settings first
    loadSettings();

    // Set the default state of the "Enable" checkbox at script startup
    setChecked('wazedevEnabled', settings.Enabled);

    // Continue with user info/profile update as before...

    // Setup event handlers for checkboxes
    setupEventHandlers();

    console.log(`${SCRIPT_NAME}: Settings initialized!`);
}
```
---
## Key Concepts Introduced

**localStorage Persistence:**
- Browser-based storage that persists between sessions
- Stores data as strings, so we use JSON.stringify/parse for objects
- Try/catch blocks protect against storage quota or browser restrictions

**Event-Driven Architecture:**  
- Checkbox changes trigger immediate saves
- Generic event handler works for multiple checkboxes using CSS classes
- ID naming convention allows automatic setting name extraction

**Default Settings Pattern:**
- Always provide fallback defaults for new installations
- Merge defaults with loaded settings to handle script updates
- Graceful degradation when localStorage fails

**Scalable Settings System:**
- Adding new checkboxes only requires proper ID/class naming
- Settings object can grow without modifying event handlers
- Centralized save/load functions handle all settings uniformly

---

## Testing Your Settings System
After implementing these changes, verify:
1. **Checkbox state persists** after refreshing WME
2. **Console shows save/load messages** when toggling the checkbox  
3. **localStorage contains your data** (check DevTools → Application → Local Storage)

**Troubleshooting:**
- **Settings don't persist**: Check browser's localStorage quota and permissions
- **Checkbox doesn't respond**: Verify the CSS class and ID naming match exactly
- **Console errors on save**: localStorage might be disabled in private browsing mode

---
# Putting It All Together
Below is a full working example combining everything so far.

```javascript
// ==UserScript==
// @name         WazeDev First Script              // Display name in Tampermonkey dashboard
// @namespace    http://tampermonkey.net/          // Unique identifier (use your GreasyFork profile for updates)
// @version      0.1                               // Version number for update tracking
// @description  Learning to script!               // Brief description of functionality
// @author       You                               // Your name or username
// @include      https://beta.waze.com/*           // Run on beta WME (testing environment)
// @include      https://www.waze.com/editor*      // Run on production WME
// @include      https://www.waze.com/*/editor*    // Run on localized WME URLs
// @exclude      https://www.waze.com/user/editor* // Don't run on user profile pages
// @exclude      https://www.waze.com/editor/sdk/* // Don't run on SDK documentation
// @grant        none                              // No special permissions needed
// ==/UserScript==

(function () {
  'use strict';

  const SCRIPT_NAME = GM_info.script.name; // Get the Script name from the @name tag of the UserScript Meta Keys
  const STORAGE_KEY = 'wazedev_Settings'; // Local Storage key

  let wmeSDK; // Declare wmeSDK globally
  let settings = {}; // Global settings object

  if (window.SDK_INITIALIZED) {
    console.log(`${SCRIPT_NAME}: SDK initialized...`);

    window.SDK_INITIALIZED.then(bootstrap).catch((err) => {
      console.error(`${SCRIPT_NAME}: SDK initialization failed`, err);
    });
  } else {
    console.warn(`${SCRIPT_NAME}: SDK_INITIALIZED is undefined`);
  }

  function bootstrap() {
    try {
      wmeSDK = getWmeSdk({
        scriptId: SCRIPT_NAME.replaceAll(' ', ''),
        scriptName: SCRIPT_NAME,
      });

      Promise.all([wmeReady()])
        .then(() => {
          console.log(`${SCRIPT_NAME}: All dependencies are ready.`);
          init();
        })
        .catch((error) => {
          console.error(`${SCRIPT_NAME}: Error during bootstrap`, error);
        });
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Failed to initialize SDK`, error);
    }
  }

  function wmeReady() {
    return new Promise((resolve) => {
      if (wmeSDK.State.isReady()) {
        console.log(`${SCRIPT_NAME}: WME is ready.`);
        resolve();
      } else {
        console.log(`${SCRIPT_NAME}: Waiting for WME to be ready...`);
        wmeSDK.Events.once({ eventName: 'wme-ready' })
          .then(() => {
            console.log(`${SCRIPT_NAME}: WME is ready now.`);
            resolve();
          })
          .catch((error) => {
            console.error(`${SCRIPT_NAME}: Error while waiting for WME to be ready:`, error);
          });
      }
    });
  }

  function init() {
    console.log(`${SCRIPT_NAME}: Script initialized successfully!`);

    // Build HTML content for our tab
    const section = document.createElement('div');
    section.innerHTML = `
    <div>
        <h2>Our First Script!</h2>
        <section>
            <input type="checkbox" id="wazedevEnabled" class="wazedevSettingsCheckbox">
            <label for="wazedevEnabled">Enable WazeDev Script</label>
        </section>
        <hr>
        <section>
            <h3>User Info</h3>
            Username: <a href="#" id="wazedevUsernameLink" target="_blank"><span id="wazedevUsername"></span></a><br>
            Rank: <span id="wazedevRank"></span><br>
            Area manager: <span id="wazedevAM"></span><br>
            Country manager: <span id="wazedevCM"></span>
        </section>
        <hr>
        <section>
            <h3>Detailed Profile</h3>
            <div id="wazedevProfileLoading">Loading profile data...</div>
            <div id="wazedevProfileData" style="display: none;">
                Total Edits: <span id="wazedevTotalEdits"></span><br>
                Today's Edits: <span id="wazedevTodayEdits"></span>
            </div>
        </section>
        <hr>
        <section id="wazedevEditsByType" style="display: none;">
            <h3>Edits by Type</h3>
            Segments: <span id="wazedevSegments"></span><br>
            Venues: <span id="wazedevVenues"></span><br>
            Map Problems: <span id="wazedevMapProblems"></span><br>
            Update Requests: <span id="wazedevUpdateRequests"></span><br>
            Place Update Requests: <span id="wazedevPlaceUpdateRequests"></span><br>
            Segment House Numbers: <span id="wazedevSegmentHouseNumbers"></span>
        </section>
    </div>
`;

    // Register the script tab using the SDK
    wmeSDK.Sidebar.registerScriptTab()
      .then(({ tabLabel, tabPane }) => {
        tabLabel.textContent = 'WazeDev';
        tabLabel.title = SCRIPT_NAME;
        tabPane.appendChild(section);

        // Initialize the main() function after tab is created
        main();
      })
      .catch((error) => {
        console.error(`${SCRIPT_NAME}: Error creating script tab`, error);
      });
  }

  // Save settings to localStorage
  function saveSettings() {
    try {
      const localSettings = { Enabled: settings.Enabled };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(localSettings));
      console.log(`${SCRIPT_NAME}: Settings saved`, localSettings);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error saving settings:`, error);
    }
  }

  // Load settings from localStorage
  function loadSettings() {
    try {
      const loadedSettings = JSON.parse(localStorage.getItem(STORAGE_KEY));
      const defaultSettings = { Enabled: false };
      settings = loadedSettings ? loadedSettings : defaultSettings;

      // Add missing default settings
      for (const prop in defaultSettings) {
        if (!settings.hasOwnProperty(prop)) {
          settings[prop] = defaultSettings[prop];
        }
      }
      console.log(`${SCRIPT_NAME}: Settings loaded`, settings);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error loading settings:`, error);
      settings = { Enabled: false };
    }
  }

  // Setup event handlers for our controls
  function setupEventHandlers() {
    const checkboxes = document.querySelectorAll('.wazedevSettingsCheckbox');
    checkboxes.forEach((checkbox) => {
      checkbox.addEventListener('change', function () {
        // Extract the setting name from the checkbox ID by removing the 'wazedev' prefix
        // Example: 'wazedevEnabled' -> 'Enabled'
        const settingName = this.id.substring(7);
        settings[settingName] = this.checked;
        saveSettings();
      });
    });
  }

  // Helper to set checkbox state
  function setChecked(checkboxId, checked) {
    const checkbox = document.getElementById(checkboxId);
    if (checkbox) checkbox.checked = checked;
  }

  async function main() {
    // Load saved settings first
    loadSettings();

    // Set the default state of the "Enable" checkbox at script startup
    setChecked('wazedevEnabled', settings.Enabled);

    // Continue with user info/profile update
    const userSession = wmeSDK.State.getUserInfo();

    // Set basic user info
    document.getElementById('wazedevUsername').textContent = userSession.userName;
    document.getElementById('wazedevRank').textContent = userSession.rank;
    document.getElementById('wazedevAM').textContent = userSession.isAreaManager ? 'Yes' : 'No';
    document.getElementById('wazedevCM').textContent = userSession.isCountryManager ? 'Yes' : 'No';

    // Set profile link
    const profileLink = wmeSDK.DataModel.Users.getUserProfileLink({ userName: userSession.userName });
    document.getElementById('wazedevUsernameLink').href = profileLink;

    // Fetch detailed user profile
    try {
      const userProfile = await wmeSDK.DataModel.Users.getUserProfile({ userName: userSession.userName });

      document.getElementById('wazedevProfileLoading').style.display = 'none';
      document.getElementById('wazedevProfileData').style.display = 'block';
      document.getElementById('wazedevEditsByType').style.display = 'block';

      document.getElementById('wazedevTotalEdits').textContent = userProfile.totalEditCount.toLocaleString();
      const todayEdits = userProfile.dailyEditCount[userProfile.dailyEditCount.length - 1] || 0;
      document.getElementById('wazedevTodayEdits').textContent = todayEdits;

      const editTypes = userProfile.editCountByType;
      document.getElementById('wazedevSegments').textContent = editTypes.segments.toLocaleString();
      document.getElementById('wazedevVenues').textContent = editTypes.venues.toLocaleString();
      document.getElementById('wazedevMapProblems').textContent = editTypes.mapProblems.toLocaleString();
      document.getElementById('wazedevUpdateRequests').textContent = editTypes.updateRequests.toLocaleString();
      document.getElementById('wazedevPlaceUpdateRequests').textContent = editTypes.placeUpdateRequests.toLocaleString();
      document.getElementById('wazedevSegmentHouseNumbers').textContent = editTypes.segmentHouseNumbers.toLocaleString();

      console.log(`${SCRIPT_NAME}: Profile data loaded successfully`);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error fetching user profile:`, error);
      document.getElementById('wazedevProfileLoading').textContent = 'Error loading profile data';
    }

    // Setup event handlers for checkboxes
    setupEventHandlers();

    console.log(`${SCRIPT_NAME}: Settings initialized!`);
  }
})();
```

Our script is now saving & loading the Enabled setting! Hooray!

In the [next section](Drawing-our-lines) we will add drawing of the lines when segments & Places are selected.

---

# Drawing our lines

Now that we have a solid settings foundation, let's make our script interact with the WME map itself! This is where scripts become truly useful - by providing visual feedback and enhancing the editing experience.

In this section, we'll create a segment highlighter that:
- **Responds to user selections** by listening to WME events
- **Provides visual feedback** with custom map layers and styling  
- **Manages resources efficiently** by cleaning up when not needed
- **Integrates with our settings** to give users control

This introduces core concepts you'll use in almost every WME script: event handling, map layers, geometry manipulation, and real-time visual feedback.

At this point we have a script that reads & loads some user information into a tab, and saves & loads the checked state of our Enabled checkbox.  Now we’ll learn how to make your script react when you select segments on the map: it will highlight the selected segments in red, and remove the highlights when nothing is selected or the script is turned off.

## Logic Overview
-  When enabled:
   - We listen for map selection changes using the SDK.
   - When you select a segment, the script gets its geometry (shape/line) and draws a highlight on it.
   - If nothing is selected, remove highlights.
- When disabled:
  - The script stops listening for selection changes.
  - Removes any highlights.

### Step 1: Declare Layer Name

Before you start, you’ll want to pick a name for your highlight layer and something to track if your event listener is active.

This makes your code easier to update later and helps keep track of things.

```javascript
(function () {
  'use strict';

  const SCRIPT_NAME = GM_info.script.name; // Get the Script name from the @name tag of the UserScript Meta Keys
  const STORAGE_KEY = 'wazedev_Settings'; // Local Storage key

  let wmeSDK; // Declare wmeSDK globally
  let settings = {}; // Global settings object
  
  const SELECTED_LAYER_NAME = "wazedev_SelectedLayer"; // Declare map layer name globally
  let selectionSubscription = null; // Declare variable to store the event listener state

  // <rest of the code>
})();
```
What/Why:
- The layer name is how you’ll refer to your custom highlight layer throughout your script.
- The selectionSubscription variable will store the event listener, so you can remove it cleanly later.


### Step 2: Create Highlight Layer (with Basic Styling)

Now, create a layer that will display your highlights. You only need to do this once when your script starts, we can put this inside the `main()` method after `setupEventHandlers()`;

```javascript
async function main() {
 ...
 // Setup event handlers for checkboxes
 setupEventHandlers();

// Add the Layer to the Map!
 wmeSDK.Map.addLayer({
    layerName: SELECTED_LAYER_NAME,
    styleRules: [{
        style: {
            strokeColor: "red",      // Highlight color (red)
            strokeWidth: 12,         // Thickness (12px)
            strokeLinecap: "round",  // Rounded ends
            fillOpacity: 0           // No fill needed for lines
        }
    }]
 });

 console.log(`${SCRIPT_NAME}: Settings initialized!`);
}
```
💡 **Tip**:  Full list of FeatureStyles can be found at [SDK: Interface FeatureStyle](https://www.waze.com/editor/sdk/interfaces/index.SDK.FeatureStyle.html)

What/Why:
- This sets up a new drawing layer.
- The style makes highlights easy to see: a thick (12px), red line with rounded ends.
- fillOpacity: 0 means no fill color (just the line itself).
- Creating the layer only once avoids errors from trying to re-add it.

### Step 3: Attach Selection Change Handler

Now, set up your script to listen when a user selects (or unselects) something.

This should be done when your script is enabled (e.g. a checkbox is on).

```javascript
function enableSelectionHighlighting() {
    if (selectionSubscription) {
      selectionSubscription(); // Safely cleanup previous before subscribing!
      selectionSubscription = null;
    }
    selectionSubscription = wmeSDK.Events.on({
      eventName: 'wme-selection-changed',
      eventHandler: drawSelectionHighlight,
    });
  }
```

When your script is turned off, undo any listening and clear highlights:

```javascript
function disableSelectionHighlighting() {
    if (selectionSubscription) {
      selectionSubscription(); // This unregisters the event handler!
      selectionSubscription = null;
    }
    wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });
  }
```

What/Why:
- The event handler will be triggered every time your selection changes.
- When you’re done (checkbox off), we unsubscribe (turn off) the event handler so the script stops reacting.

### Step 4: Drawing Highlights

This function actually does the work of displaying highlights.

When the selection changes, it erases the old highlight and draws a new one, if needed, but only if the Enable checkbox is "on".

```javascript
function drawSelectionHighlight() {
    // Check if the script's "Enable" setting is ON
    if (!settings.Enabled) {
        wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });
        return;
    }

    // Get the current selection object from the SDK
    const selection = wmeSDK.Editing.getSelection();

    // Always remove all previous features from our layer
    wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });

    // Check if there are any segments actively selected in the selection object
    if (!selection || !selection.ids || selection.objectType !== 'segment') return;

    // Add the selected segments as features to the layer
    selection.ids.forEach((segmentId) => {
        const segment = wmeSDK.DataModel.Segments.getById({ segmentId });
        if (segment && segment.geometry) {
            wmeSDK.Map.addFeatureToLayer({
                layerName: SELECTED_LAYER_NAME,
                feature: {
                    id: `highlighted-${segmentId}`,
                    type: 'Feature',
                    geometry: segment.geometry,
                    properties: {},
                },
            });
        }
    });
}

```
What/Why:
- Erases highlights so you only see the latest selection.
- Checks that you actually have a segment selected (skips places/nodes for now).
- For every selected segment, gets its shape and adds it as a feature to your highlight layer.
- The result: whenever you select a segment, it’s outlined in red.

### Step 5: Tie to Settings (Checkbox Logic)

Connect highlighting to your script’s on/off setting.

Whenever your enable checkbox or option is changed, activate or deactivate highlighting.

```javascript
function onEnabledCheckboxChanged(value) {
    if (settings.Enabled) {
      enableSelectionHighlighting();
      drawSelectionHighlight();
    } else {
      disableSelectionHighlighting();
    }
  }
```

So now let's hook it up in the `setupEventHandlers()` method:

```javascript
function setupEventHandlers() {
    // Find all checkboxes with the settings class in the DOM
    const checkboxes = document.querySelectorAll('.wazedevSettingsCheckbox');
    
    // For each settings checkbox, add a change event listener
    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', function () {
            // Extract the setting name from the checkbox ID by removing the 'wazedev' prefix
            // Example: 'wazedevEnabled' -> 'Enabled'
            const settingName = this.id.substring(7);
            
            // Update the corresponding value in the settings object
            settings[settingName] = this.checked;
            
            // Save the updated settings (persist changes, e.g., to storage)
            saveSettings();
            
            // If the 'Enabled' setting changed, trigger additional actions to update highlighting
            if (settingName === 'Enabled') {
                onEnabledCheckboxChanged(this.checked);
            }
        });
    });
}
```

What/Why:
- This lets users control whether the highlight feature is on.
- If enabled, highlighting is immediately shown for any currently selected segments.
- If disabled, the script stops reacting and removes any highlights.


### Step 6: Clean-up

Whenever your script disables (checkbox off), `disableSelectionHighlighting()` makes sure:
- The script isn’t listening for selection changes anymore.
- All highlight lines are immediately removed from the map.

What/Why:
- Prevents your script from using resources it doesn’t need.
- Keeps the map clean with no leftover highlights.

## Key Concepts Introduced

**Event-Driven Map Interaction:**
- WME fires events when selections change (`wme-selection-changed`)
- Event subscriptions return cleanup functions for proper resource management
- Always check if script is enabled before processing events

**Map Layers and Styling:**
- Custom layers separate your features from WME's built-in elements
- Style rules define appearance (color, width, opacity, etc.)
- Features are GeoJSON-compliant objects with geometry and properties

**Geometry and Features:**
- Segments have geometry objects that define their shape on the map
- Features combine geometry with styling to create visual elements
- Layer management prevents memory leaks and visual clutter

**Resource Management:**
- Event listeners consume memory and CPU - clean them up when not needed
- Remove all features from layers when disabling functionality
- Subscription pattern allows easy enable/disable of event handling

---
## Testing Your Map Integration

After implementing these changes, test the functionality:

1. **Enable the script** and select a segment - you should see a red highlight
2. **Select multiple segments** - all should be highlighted simultaneously
3. **Disable the script** - highlights should disappear immediately
4. **Select other objects** (places, nodes) - no highlights should appear

**Expected Behavior:**
- Highlights appear instantly when selecting segments
- Only segments are highlighted (places/nodes are ignored)
- Highlights are removed when selection changes or script is disabled
- Console shows no errors during selection changes

**Troubleshooting:**
- **No highlights appear**: Check console for errors, verify layer was created successfully
- **Highlights don't disappear**: Ensure `disableSelectionHighlighting()` is called when disabling
- **Multiple highlights persist**: Verify `removeAllFeaturesFromLayer()` is called before adding new ones
- **Script affects performance**: Check that event listeners are properly cleaned up when disabled

# Our script should now look like the following
```javascript
// ==UserScript==
// @name         WazeDev First Script              // Display name in Tampermonkey dashboard
// @namespace    http://tampermonkey.net/          // Unique identifier (use your GreasyFork profile for updates)
// @version      0.1                               // Version number for update tracking
// @description  Learning to script!               // Brief description of functionality
// @author       You                               // Your name or username
// @include      https://beta.waze.com/*           // Run on beta WME (testing environment)
// @include      https://www.waze.com/editor*      // Run on production WME
// @include      https://www.waze.com/*/editor*    // Run on localized WME URLs
// @exclude      https://www.waze.com/user/editor* // Don't run on user profile pages
// @exclude      https://www.waze.com/editor/sdk/* // Don't run on SDK documentation
// @grant        none                              // No special permissions needed
// ==/UserScript==

(function () {
  'use strict';

  const SCRIPT_NAME = GM_info.script.name; // Get the Script name from the @name tag of the UserScript Meta Keys
  const STORAGE_KEY = 'wazedev_Settings'; // Local Storage key

  let wmeSDK; // Declare wmeSDK globally
  let settings = {}; // Global settings object

  const SELECTED_LAYER_NAME = 'wazedev_SelectedLayer'; // Declare map layer name globally
  let selectionSubscription = null; // Declare variable to store the event listener state

  if (window.SDK_INITIALIZED) {
    console.log(`${SCRIPT_NAME}: SDK initialized...`);

    window.SDK_INITIALIZED.then(bootstrap).catch((err) => {
      console.error(`${SCRIPT_NAME}: SDK initialization failed`, err);
    });
  } else {
    console.warn(`${SCRIPT_NAME}: SDK_INITIALIZED is undefined`);
  }

  function bootstrap() {
    try {
      wmeSDK = getWmeSdk({
        scriptId: SCRIPT_NAME.replaceAll(' ', ''),
        scriptName: SCRIPT_NAME,
      });

      Promise.all([wmeReady()])
        .then(() => {
          console.log(`${SCRIPT_NAME}: All dependencies are ready.`);
          init();
        })
        .catch((error) => {
          console.error(`${SCRIPT_NAME}: Error during bootstrap`, error);
        });
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Failed to initialize SDK`, error);
    }
  }

  function wmeReady() {
    return new Promise((resolve) => {
      if (wmeSDK.State.isReady()) {
        console.log(`${SCRIPT_NAME}: WME is ready.`);
        resolve();
      } else {
        console.log(`${SCRIPT_NAME}: Waiting for WME to be ready...`);
        wmeSDK.Events.once({ eventName: 'wme-ready' })
          .then(() => {
            console.log(`${SCRIPT_NAME}: WME is ready now.`);
            resolve();
          })
          .catch((error) => {
            console.error(`${SCRIPT_NAME}: Error while waiting for WME to be ready:`, error);
          });
      }
    });
  }

  function init() {
    console.log(`${SCRIPT_NAME}: Script initialized successfully!`);

    // Build HTML content for our tab
    const section = document.createElement('div');
    section.innerHTML = `
    <div>
        <h2>Our First Script!</h2>
        <section>
            <input type="checkbox" id="wazedevEnabled" class="wazedevSettingsCheckbox">
            <label for="wazedevEnabled">Enable WazeDev Script</label>
        </section>
        <hr>
        <section>
            <h3>User Info</h3>
            Username: <a href="#" id="wazedevUsernameLink" target="_blank"><span id="wazedevUsername"></span></a><br>
            Rank: <span id="wazedevRank"></span><br>
            Area manager: <span id="wazedevAM"></span><br>
            Country manager: <span id="wazedevCM"></span>
        </section>
        <hr>
        <section>
            <h3>Detailed Profile</h3>
            <div id="wazedevProfileLoading">Loading profile data...</div>
            <div id="wazedevProfileData" style="display: none;">
                Total Edits: <span id="wazedevTotalEdits"></span><br>
                Today's Edits: <span id="wazedevTodayEdits"></span>
            </div>
        </section>
        <hr>
        <section id="wazedevEditsByType" style="display: none;">
            <h3>Edits by Type</h3>
            Segments: <span id="wazedevSegments"></span><br>
            Venues: <span id="wazedevVenues"></span><br>
            Map Problems: <span id="wazedevMapProblems"></span><br>
            Update Requests: <span id="wazedevUpdateRequests"></span><br>
            Place Update Requests: <span id="wazedevPlaceUpdateRequests"></span><br>
            Segment House Numbers: <span id="wazedevSegmentHouseNumbers"></span>
        </section>
    </div>
`;

    // Register the script tab using the SDK
    wmeSDK.Sidebar.registerScriptTab()
      .then(({ tabLabel, tabPane }) => {
        tabLabel.textContent = 'WazeDev';
        tabLabel.title = SCRIPT_NAME;
        tabPane.appendChild(section);

        // Initialize the main() function after tab is created
        main();
      })
      .catch((error) => {
        console.error(`${SCRIPT_NAME}: Error creating script tab`, error);
      });
  }

  // Save settings to localStorage
  function saveSettings() {
    try {
      const localSettings = { Enabled: settings.Enabled };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(localSettings));
      console.log(`${SCRIPT_NAME}: Settings saved`, localSettings);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error saving settings:`, error);
    }
  }

  // Load settings from localStorage
  function loadSettings() {
    try {
      const loadedSettings = JSON.parse(localStorage.getItem(STORAGE_KEY));
      const defaultSettings = { Enabled: false };
      settings = loadedSettings ? loadedSettings : defaultSettings;

      // Add missing default settings
      for (const prop in defaultSettings) {
        if (!settings.hasOwnProperty(prop)) {
          settings[prop] = defaultSettings[prop];
        }
      }
      console.log(`${SCRIPT_NAME}: Settings loaded`, settings);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error loading settings:`, error);
      settings = { Enabled: false };
    }
  }

  // Helper to set checkbox state
  function setChecked(checkboxId, checked) {
    const checkbox = document.getElementById(checkboxId);
    if (checkbox) checkbox.checked = checked;
  }

  // Setup event handlers for our controls
  function setupEventHandlers() {
    // Find all checkboxes with the settings class in the DOM
    const checkboxes = document.querySelectorAll('.wazedevSettingsCheckbox');

    // For each settings checkbox, add a change event listener
    checkboxes.forEach((checkbox) => {
      checkbox.addEventListener('change', function () {
        // Extract the setting name from the checkbox ID by removing the 'wazedev' prefix
        // Example: 'wazedevEnabled' -> 'Enabled'
        const settingName = this.id.substring(7);

        // Update the corresponding value in the settings object
        settings[settingName] = this.checked;

        // Save the updated settings (persist changes, e.g., to storage)
        saveSettings();

        // If the 'Enabled' setting changed, trigger additional actions to update highlighting
        if (settingName === 'Enabled') {
          onEnabledCheckboxChanged(this.checked);
        }
      });
    });
  }

  function enableSelectionHighlighting() {
    if (selectionSubscription) {
      selectionSubscription(); // Safely cleanup previous before subscribing!
      selectionSubscription = null;
    }
    selectionSubscription = wmeSDK.Events.on({
      eventName: 'wme-selection-changed',
      eventHandler: drawSelectionHighlight,
    });
  }

  function disableSelectionHighlighting() {
    if (selectionSubscription) {
      selectionSubscription(); // This unregisters the event handler!
      selectionSubscription = null;
    }
    wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });
  }

  function drawSelectionHighlight() {
    // Check if the script's "Enable" setting is ON
    if (!settings.Enabled) {
      wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });
      return;
    }

    // Get the current selection object from the SDK
    const selection = wmeSDK.Editing.getSelection();

    // Always remove all previous features from our layer
    wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });

    // Check if there are any segments actively selected in the selection object
    if (!selection || !selection.ids || selection.objectType !== 'segment') return;

    // Add the selected segments as features to the layer
    selection.ids.forEach((segmentId) => {
      const segment = wmeSDK.DataModel.Segments.getById({ segmentId });
      if (segment && segment.geometry) {
        wmeSDK.Map.addFeatureToLayer({
          layerName: SELECTED_LAYER_NAME,
          feature: {
            id: `highlighted-${segmentId}`,
            type: 'Feature',
            geometry: segment.geometry,
            properties: {},
          },
        });
      }
    });
  }

  function onEnabledCheckboxChanged(value) {
    if (settings.Enabled) {
      enableSelectionHighlighting();
      drawSelectionHighlight();
    } else {
      disableSelectionHighlighting();
    }
  }

  async function main() {
    // Load saved settings first
    loadSettings();

    // Set the default state of the "Enable" checkbox at script startup
    setChecked('wazedevEnabled', settings.Enabled);

    // Continue with user info/profile update
    const userSession = wmeSDK.State.getUserInfo();

    // Set basic user info
    document.getElementById('wazedevUsername').textContent = userSession.userName;
    document.getElementById('wazedevRank').textContent = userSession.rank;
    document.getElementById('wazedevAM').textContent = userSession.isAreaManager ? 'Yes' : 'No';
    document.getElementById('wazedevCM').textContent = userSession.isCountryManager ? 'Yes' : 'No';

    // Set profile link
    const profileLink = wmeSDK.DataModel.Users.getUserProfileLink({ userName: userSession.userName });
    document.getElementById('wazedevUsernameLink').href = profileLink;

    // Fetch detailed user profile
    try {
      const userProfile = await wmeSDK.DataModel.Users.getUserProfile({ userName: userSession.userName });

      document.getElementById('wazedevProfileLoading').style.display = 'none';
      document.getElementById('wazedevProfileData').style.display = 'block';
      document.getElementById('wazedevEditsByType').style.display = 'block';

      document.getElementById('wazedevTotalEdits').textContent = userProfile.totalEditCount.toLocaleString();
      const todayEdits = userProfile.dailyEditCount[userProfile.dailyEditCount.length - 1] || 0;
      document.getElementById('wazedevTodayEdits').textContent = todayEdits;

      const editTypes = userProfile.editCountByType;
      document.getElementById('wazedevSegments').textContent = editTypes.segments.toLocaleString();
      document.getElementById('wazedevVenues').textContent = editTypes.venues.toLocaleString();
      document.getElementById('wazedevMapProblems').textContent = editTypes.mapProblems.toLocaleString();
      document.getElementById('wazedevUpdateRequests').textContent = editTypes.updateRequests.toLocaleString();
      document.getElementById('wazedevPlaceUpdateRequests').textContent = editTypes.placeUpdateRequests.toLocaleString();
      document.getElementById('wazedevSegmentHouseNumbers').textContent = editTypes.segmentHouseNumbers.toLocaleString();

      console.log(`${SCRIPT_NAME}: Profile data loaded successfully`);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error fetching user profile:`, error);
      document.getElementById('wazedevProfileLoading').textContent = 'Error loading profile data';
    }

    // Setup event handlers for checkboxes
    setupEventHandlers();

    // Add the Layer to the Map!
    wmeSDK.Map.addLayer({
      layerName: SELECTED_LAYER_NAME,
      styleRules: [
        {
          style: {
            strokeColor: 'red', // Highlight color (red)
            strokeWidth: 12, // Thickness (12px)
            strokeLinecap: 'round', // Rounded ends
            fillOpacity: 0, // No fill needed for lines
          },
        },
      ],
    });

    onEnabledCheckboxChanged(settings.Enabled); // Activate script effect if previously enabled

    console.log(`${SCRIPT_NAME}: Settings initialized!`);
  }
})();
```

# Use a Modern code editors like VS Code, WebStorm, and many browser-based IDEs?

Then check out the final version of the script wiht JSDOC support [here!](Final-vsCode-with-JSDOC)

---

# Adding JSDoc Comments for Smarter Code Editing

Modern code editors like VS Code, WebStorm, and many browser-based IDEs can leverage special code comments called JSDoc to give you powerful features such as:
- Type hints & autocomplete
- Inline documentation tooltips
- Better code navigation and refactoring

## What is JSDoc?

JSDoc is a standard for documenting JavaScript code. You add special comments above your functions, classes, and variables, and your code editor will use them to:

- Show descriptions for functions or parameters
- Show expected types (objects, arrays, numbers, etc.)
- Warn you about bugs before you run your code
- Improve your code understanding

## JSDoc Examples from Our Script

Here are some examples showing different JSDoc patterns used in our WazeDev script:

### Example: Annotating a Function

```javascript
/**
 * Draws highlight overlay for currently selected segments
 * Only highlights segments when the script is enabled
 * @returns {void}
 */
function drawSelectionHighlight() {
    // ... function code as before ...
}
```

### Documenting Function Parameters
```javascript
/**
 * Sets the checked state of a checkbox element
 * @param {string} checkboxId - The ID of the checkbox element
 * @param {boolean} checked - Whether the checkbox should be checked
 * @returns {void}
 */
function setChecked(checkboxId, checked) {
    const checkbox = document.getElementById(checkboxId);
    if (checkbox) checkbox.checked = checked;
}
```
### Documenting Complex Objects
```javascript
/**
 * Global settings object containing user preferences
 * @type {Object}
 * @property {boolean} Enabled - Whether the script highlighting is active
 */
let settings = {};
```

### Documenting Async Functions
```javascript
/**
 * Main initialization function that sets up the complete user interface
 * Loads settings, populates user information, fetches profile data, and initializes map layer
 * @async
 * @returns {Promise<void>} Promise that resolves when initialization is complete
 */
async function main() {
    // ... function code
}
```

## Benefits You'll See in Your Editor

With JSDoc comments added, modern editors provide:

**IntelliSense/Autocomplete:**
- Function names, parameters, and return types appear as you type
- Descriptions appear in popup tooltips
- Reduces typos and API lookup time

**Parameter Validation:**
- Warnings when you pass wrong types (string instead of number, etc.)
- Highlighted missing required parameters
- Better error detection before running code

**Code Navigation:**
- Click-to-definition works better
- Find all references to functions
- Easier refactoring with confidence

**Team Collaboration:**
- New team members understand function purposes immediately
- Self-documenting code reduces need for external documentation
- Consistent parameter naming and typing across the project

---

## Common JSDoc Tags Reference

| Tag | Purpose | Example |
|-----|---------|---------|
| `@param {type} name - description` | Document parameters | `@param {string} userId - The user's ID` |
| `@returns {type} description` | Document return value | `@returns {boolean} True if successful` |
| `@throws {type} description` | Document exceptions | `@throws {Error} When network fails` |
| `@async` | Mark async functions | `@async` |
| `@example` | Show usage examples | `@example setChecked('myId', true)` |
| `@since` | Version when added | `@since 1.2.0` |
| `@deprecated` | Mark as deprecated | `@deprecated Use newFunction() instead` |

**Pro tip:** Most editors will auto-generate JSDoc templates when you type `/**` above a function and press Enter!

---

## Setting Up Your Editor

**Visual Studio Code:**
- JSDoc support is built-in - just start typing `/**` above functions
- Install "JavaScript (ES6) code snippets" extension for more templates
- Enable "typescript.suggest.autoImports" in settings for better IntelliSense

**WebStorm/IntelliJ:**
- JSDoc support is built-in and very comprehensive
- Use Ctrl+Shift+D (Windows) or Cmd+Shift+D (Mac) to generate JSDoc templates
- Configure JSDoc validation in Settings → Languages & Frameworks → JavaScript

**Browser-based Editors (CodePen, JSFiddle, etc.):**
- Most modern browser editors support basic JSDoc IntelliSense
- May have limited features compared to desktop editors

# Below is out complete script with JSDOC support

```javascript
// ==UserScript==
// @name         WazeDev First Script              // Display name in Tampermonkey dashboard
// @namespace    http://tampermonkey.net/          // Unique identifier (use your GreasyFork profile for updates)
// @version      0.1                               // Version number for update tracking
// @description  Learning to script!               // Brief description of functionality
// @author       You                               // Your name or username
// @include      https://beta.waze.com/*           // Run on beta WME (testing environment)
// @include      https://www.waze.com/editor*      // Run on production WME
// @include      https://www.waze.com/*/editor*    // Run on localized WME URLs
// @exclude      https://www.waze.com/user/editor* // Don't run on user profile pages
// @exclude      https://www.waze.com/editor/sdk/* // Don't run on SDK documentation
// @grant        none                              // No special permissions needed
// ==/UserScript==

/**
 * @typedef {Object} UserSession
 * @property {string} userName - The user's display name
 * @property {number} rank - The user's editing rank
 * @property {boolean} isAreaManager - Whether user is an area manager
 * @property {boolean} isCountryManager - Whether user is a country manager
 */

/**
 * @typedef {Object} EditCountByType
 * @property {number} segments - Number of segment edits
 * @property {number} venues - Number of venue edits
 * @property {number} mapProblems - Number of map problem edits
 * @property {number} updateRequests - Number of update request edits
 * @property {number} placeUpdateRequests - Number of place update request edits
 * @property {number} segmentHouseNumbers - Number of segment house number edits
 */

/**
 * @typedef {Object} UserProfile
 * @property {number} totalEditCount - Total number of edits made by user
 * @property {number[]} dailyEditCount - Array of daily edit counts
 * @property {EditCountByType} editCountByType - Breakdown of edits by type
 */

/**
 * @typedef {Object} ScriptSettings
 * @property {boolean} Enabled - Whether the script functionality is enabled
 */

/**
 * @typedef {Object} WmeSelection
 * @property {string} objectType - Type of selected object (e.g., 'segment')
 * @property {number[]} ids - Array of selected object IDs
 */

/**
 * @typedef {Object} WmeSegment
 * @property {number} id - Segment ID
 * @property {Object} geometry - Segment geometry data
 */

/**
 * @typedef {Object} MapFeature
 * @property {string} id - Feature ID
 * @property {string} type - Feature type (always 'Feature')
 * @property {Object} geometry - Feature geometry
 * @property {Object} properties - Feature properties
 */

(function () {
  'use strict';

  /** @type {string} Script name from UserScript metadata */
  const SCRIPT_NAME = GM_info.script.name;

  /** @type {string} Local storage key for persisting settings */
  const STORAGE_KEY = 'wazedev_Settings';

  /** @type {string} Map layer name for selection highlighting */
  const SELECTED_LAYER_NAME = 'wazedev_SelectedLayer';

  /** @type {Object|null} WME SDK instance - initialized during bootstrap */
  let wmeSDK = null;

  /** @type {ScriptSettings} Global settings object */
  let settings = {};

  /** @type {Function|null} Event subscription cleanup function */
  let selectionSubscription = null;

  // Initialize the script when SDK is ready

  if (window.SDK_INITIALIZED) {
    console.log(`${SCRIPT_NAME}: SDK initialized...`);

    window.SDK_INITIALIZED.then(bootstrap).catch((err) => {
      console.error(`${SCRIPT_NAME}: SDK initialization failed`, err);
    });
  } else {
    console.warn(`${SCRIPT_NAME}: SDK_INITIALIZED is undefined`);
  }

  /**
   * Initializes the WME SDK and starts the bootstrap process
   * @throws {Error} When SDK initialization fails
   */
  function bootstrap() {
    try {
      wmeSDK = getWmeSdk({
        scriptId: SCRIPT_NAME.replaceAll(' ', ''),
        scriptName: SCRIPT_NAME,
      });

      Promise.all([wmeReady()])
        .then(() => {
          console.log(`${SCRIPT_NAME}: All dependencies are ready.`);
          init();
        })
        .catch((error) => {
          console.error(`${SCRIPT_NAME}: Error during bootstrap`, error);
        });
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Failed to initialize SDK`, error);
    }
  }

  /**
   * Waits for WME to be fully ready before proceeding
   * @returns {Promise<void>} Promise that resolves when WME is ready
   */
  function wmeReady() {
    return new Promise((resolve) => {
      if (wmeSDK.State.isReady()) {
        console.log(`${SCRIPT_NAME}: WME is ready.`);
        resolve();
      } else {
        console.log(`${SCRIPT_NAME}: Waiting for WME to be ready...`);
        wmeSDK.Events.once({ eventName: 'wme-ready' })
          .then(() => {
            console.log(`${SCRIPT_NAME}: WME is ready now.`);
            resolve();
          })
          .catch((error) => {
            console.error(`${SCRIPT_NAME}: Error while waiting for WME to be ready:`, error);
          });
      }
    });
  }

  /**
   * Initializes the script UI and registers the sidebar tab
   * Creates the HTML structure for the script interface
   */
  function init() {
    console.log(`${SCRIPT_NAME}: Script initialized successfully!`);

    // Build HTML content for our tab
    /** @type {HTMLDivElement} */
    const section = document.createElement('div');
    section.innerHTML = `
    <div>
        <h2>Our First Script!</h2>
        <section>
            <input type="checkbox" id="wazedevEnabled" class="wazedevSettingsCheckbox">
            <label for="wazedevEnabled">Enable WazeDev Script</label>
        </section>
        <hr>
        <section>
            <h3>User Info</h3>
            Username: <a href="#" id="wazedevUsernameLink" target="_blank"><span id="wazedevUsername"></span></a><br>
            Rank: <span id="wazedevRank"></span><br>
            Area manager: <span id="wazedevAM"></span><br>
            Country manager: <span id="wazedevCM"></span>
        </section>
        <hr>
        <section>
            <h3>Detailed Profile</h3>
            <div id="wazedevProfileLoading">Loading profile data...</div>
            <div id="wazedevProfileData" style="display: none;">
                Total Edits: <span id="wazedevTotalEdits"></span><br>
                Today's Edits: <span id="wazedevTodayEdits"></span>
            </div>
        </section>
        <hr>
        <section id="wazedevEditsByType" style="display: none;">
            <h3>Edits by Type</h3>
            Segments: <span id="wazedevSegments"></span><br>
            Venues: <span id="wazedevVenues"></span><br>
            Map Problems: <span id="wazedevMapProblems"></span><br>
            Update Requests: <span id="wazedevUpdateRequests"></span><br>
            Place Update Requests: <span id="wazedevPlaceUpdateRequests"></span><br>
            Segment House Numbers: <span id="wazedevSegmentHouseNumbers"></span>
        </section>
    </div>
`;

    // Register the script tab using the SDK
    wmeSDK.Sidebar.registerScriptTab()
      .then(({ tabLabel, tabPane }) => {
        tabLabel.textContent = 'WazeDev';
        tabLabel.title = SCRIPT_NAME;
        tabPane.appendChild(section);

        // Initialize the main() function after tab is created
        main();
      })
      .catch((error) => {
        console.error(`${SCRIPT_NAME}: Error creating script tab`, error);
      });
  }

  /**
   * Saves current settings to localStorage
   * @throws {Error} When localStorage is unavailable or quota exceeded
   */
  function saveSettings() {
    try {
      /** @type {ScriptSettings} */
      const localSettings = { Enabled: settings.Enabled };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(localSettings));
      console.log(`${SCRIPT_NAME}: Settings saved`, localSettings);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error saving settings:`, error);
    }
  }

  /**
   * Loads settings from localStorage and applies defaults for missing properties
   * @returns {void}
   */
  function loadSettings() {
    try {
      /** @type {ScriptSettings|null} */
      const loadedSettings = JSON.parse(localStorage.getItem(STORAGE_KEY));

      /** @type {ScriptSettings} */
      const defaultSettings = { Enabled: false };

      settings = loadedSettings ? loadedSettings : defaultSettings;

      // Add missing default settings
      for (const prop in defaultSettings) {
        if (!settings.hasOwnProperty(prop)) {
          settings[prop] = defaultSettings[prop];
        }
      }
      console.log(`${SCRIPT_NAME}: Settings loaded`, settings);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error loading settings:`, error);
      settings = { Enabled: false };
    }
  }

  /**
   * Sets the checked state of a checkbox element
   * @param {string} checkboxId - The ID of the checkbox element to modify
   * @param {boolean} checked - Whether the checkbox should be checked
   * @returns {void}
   */
  function setChecked(checkboxId, checked) {
    /** @type {HTMLInputElement|null} */
    const checkbox = document.getElementById(checkboxId);
    if (checkbox) checkbox.checked = checked;
  }

  /**
   * Sets up event listeners for all settings checkboxes
   * Automatically handles setting updates and persistence
   * @returns {void}
   */
  function setupEventHandlers() {
    // Find all checkboxes with the settings class in the DOM
    /** @type {NodeListOf<HTMLInputElement>} */
    const checkboxes = document.querySelectorAll('.wazedevSettingsCheckbox');

    // For each settings checkbox, add a change event listener
    checkboxes.forEach((checkbox) => {
      checkbox.addEventListener('change', function () {
        // Extract the setting name from the checkbox ID by removing the 'wazedev' prefix
        // Example: 'wazedevEnabled' -> 'Enabled'
        /** @type {string} */
        const settingName = this.id.substring(7);

        // Update the corresponding value in the settings object
        settings[settingName] = this.checked;

        // Save the updated settings (persist changes, e.g., to storage)
        saveSettings();

        // If the 'Enabled' setting changed, trigger additional actions to update highlighting
        if (settingName === 'Enabled') {
          onEnabledCheckboxChanged(this.checked);
        }
      });
    });
  }

  /**
   * Enables selection highlighting by subscribing to selection change events
   * Safely cleans up any existing subscription before creating a new one
   * @returns {void}
   */
  function enableSelectionHighlighting() {
    if (selectionSubscription) {
      selectionSubscription(); // Safely cleanup previous before subscribing!
      selectionSubscription = null;
    }
    selectionSubscription = wmeSDK.Events.on({
      eventName: 'wme-selection-changed',
      eventHandler: drawSelectionHighlight,
    });
  }

  /**
   * Disables selection highlighting by unregistering event handler and clearing highlights
   * @returns {void}
   */
  function disableSelectionHighlighting() {
    if (selectionSubscription) {
      selectionSubscription(); // This unregisters the event handler!
      selectionSubscription = null;
    }
    wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });
  }

  /**
   * Draws highlight overlay for currently selected segments
   * Only highlights segments when the script is enabled
   * @returns {void}
   */
  function drawSelectionHighlight() {
    // Check if the script's "Enable" setting is ON
    if (!settings.Enabled) {
      wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });
      return;
    }

    // Get the current selection object from the SDK
    /** @type {WmeSelection|null} */
    const selection = wmeSDK.Editing.getSelection();

    // Always remove all previous features from our layer
    wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: SELECTED_LAYER_NAME });

    // Check if there are any segments actively selected in the selection object
    if (!selection || !selection.ids || selection.objectType !== 'segment') return;

    // Add the selected segments as features to the layer
    selection.ids.forEach((segmentId) => {
      /** @type {WmeSegment|null} */
      const segment = wmeSDK.DataModel.Segments.getById({ segmentId });

      if (segment && segment.geometry) {
        /** @type {MapFeature} */
        const feature = {
          id: `highlighted-${segmentId}`,
          type: 'Feature',
          geometry: segment.geometry,
          properties: {},
        };

        wmeSDK.Map.addFeatureToLayer({
          layerName: SELECTED_LAYER_NAME,
          feature: feature,
        });
      }
    });
  }

  /**
   * Handles changes to the main "Enabled" checkbox
   * Toggles selection highlighting functionality based on the new state
   * @param {boolean} value - The new enabled state (currently unused, reads from settings)
   * @returns {void}
   */
  function onEnabledCheckboxChanged(value) {
    if (settings.Enabled) {
      enableSelectionHighlighting();
      drawSelectionHighlight();
    } else {
      disableSelectionHighlighting();
    }
  }

  /**
   * Main initialization function that sets up the complete user interface
   * Loads settings, populates user information, fetches profile data, and initializes map layer
   * @async
   * @returns {Promise<void>} Promise that resolves when initialization is complete
   */
  async function main() {
    // Load saved settings first
    loadSettings();

    // Set the default state of the "Enable" checkbox at script startup
    setChecked('wazedevEnabled', settings.Enabled);

    // Continue with user info/profile update
    /** @type {UserSession} */
    const userSession = wmeSDK.State.getUserInfo();

    // Set basic user info in the UI
    /** @type {HTMLElement|null} */
    const usernameElement = document.getElementById('wazedevUsername');
    /** @type {HTMLElement|null} */
    const rankElement = document.getElementById('wazedevRank');
    /** @type {HTMLElement|null} */
    const amElement = document.getElementById('wazedevAM');
    /** @type {HTMLElement|null} */
    const cmElement = document.getElementById('wazedevCM');

    if (usernameElement) usernameElement.textContent = userSession.userName;
    if (rankElement) rankElement.textContent = userSession.rank.toString();
    if (amElement) amElement.textContent = userSession.isAreaManager ? 'Yes' : 'No';
    if (cmElement) cmElement.textContent = userSession.isCountryManager ? 'Yes' : 'No';

    // Set profile link
    /** @type {string} */
    const profileLink = wmeSDK.DataModel.Users.getUserProfileLink({ userName: userSession.userName });
    /** @type {HTMLAnchorElement|null} */
    const profileLinkElement = document.getElementById('wazedevUsernameLink');
    if (profileLinkElement) profileLinkElement.href = profileLink;

    // Fetch detailed user profile
    try {
      /** @type {UserProfile} */
      const userProfile = await wmeSDK.DataModel.Users.getUserProfile({ userName: userSession.userName });

      // Hide loading indicator and show profile data
      /** @type {HTMLElement|null} */
      const loadingElement = document.getElementById('wazedevProfileLoading');
      /** @type {HTMLElement|null} */
      const profileDataElement = document.getElementById('wazedevProfileData');
      /** @type {HTMLElement|null} */
      const editsByTypeElement = document.getElementById('wazedevEditsByType');

      if (loadingElement) loadingElement.style.display = 'none';
      if (profileDataElement) profileDataElement.style.display = 'block';
      if (editsByTypeElement) editsByTypeElement.style.display = 'block';

      // Update total and today's edit counts
      /** @type {HTMLElement|null} */
      const totalEditsElement = document.getElementById('wazedevTotalEdits');
      /** @type {HTMLElement|null} */
      const todayEditsElement = document.getElementById('wazedevTodayEdits');

      if (totalEditsElement) {
        totalEditsElement.textContent = userProfile.totalEditCount.toLocaleString();
      }

      /** @type {number} */
      const todayEdits = userProfile.dailyEditCount[userProfile.dailyEditCount.length - 1] || 0;
      if (todayEditsElement) {
        todayEditsElement.textContent = todayEdits.toString();
      }

      // Update edit counts by type
      /** @type {EditCountByType} */
      const editTypes = userProfile.editCountByType;

      /** @type {Array<{elementId: string, count: number}>} */
      const editTypeMapping = [
        { elementId: 'wazedevSegments', count: editTypes.segments },
        { elementId: 'wazedevVenues', count: editTypes.venues },
        { elementId: 'wazedevMapProblems', count: editTypes.mapProblems },
        { elementId: 'wazedevUpdateRequests', count: editTypes.updateRequests },
        { elementId: 'wazedevPlaceUpdateRequests', count: editTypes.placeUpdateRequests },
        { elementId: 'wazedevSegmentHouseNumbers', count: editTypes.segmentHouseNumbers },
      ];

      editTypeMapping.forEach(({ elementId, count }) => {
        /** @type {HTMLElement|null} */
        const element = document.getElementById(elementId);
        if (element) element.textContent = count.toLocaleString();
      });

      console.log(`${SCRIPT_NAME}: Profile data loaded successfully`);
    } catch (error) {
      console.error(`${SCRIPT_NAME}: Error fetching user profile:`, error);
      /** @type {HTMLElement|null} */
      const loadingElement = document.getElementById('wazedevProfileLoading');
      if (loadingElement) {
        loadingElement.textContent = 'Error loading profile data';
      }
    }

    // Setup event handlers for checkboxes
    setupEventHandlers();

    // Add the Layer to the Map with styling configuration
    wmeSDK.Map.addLayer({
      layerName: SELECTED_LAYER_NAME,
      styleRules: [
        {
          style: {
            strokeColor: 'red', // Highlight color (red)
            strokeWidth: 12, // Thickness (12px)
            strokeLinecap: 'round', // Rounded ends
            fillOpacity: 0, // No fill needed for lines
          },
        },
      ],
    });

    // Activate script effect if previously enabled
    onEnabledCheckboxChanged(settings.Enabled);

    console.log(`${SCRIPT_NAME}: Settings initialized!`);
  }
})();
```