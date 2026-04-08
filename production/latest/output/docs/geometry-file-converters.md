# GeoSHPer: shapefile to GeoJSON Converter

GeoSHPer is a JavaScript library designed to convert shapefile data into GeoJSON format effortlessly. It reads ZIP archives containing various components of shapefiles (.shp, .dbf, and .prj files), parses geographic features and attributes, and supports coordinate transformations using Proj4js. The final result is a GeoJSON FeatureCollection, which can be easily integrated with web mapping libraries.

## Features

- **Convert Shapefile to GeoJSON**: Reads compressed shapefile formats and outputs GeoJSON, a standard format used by mapping libraries.
- **Coordinate Transformation**: Utilize Proj4js to handle complex map projections.
- **Support for Multi-layer Files**: Automatically processes multiple shapefile layers within a single ZIP archive.
- **Parsing Support**: Extracts data from .shp (geometry), .dbf (attributes), and .prj (projection information) files.

## Installation Dependency

To use GeoSHPer, you need to include the Proj4js library as a dependency:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.15.0/proj4-src.js"></script>
```
or via Tamplermonkey / GreasyFork

```html
// @require  https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.15.0/proj4-src.js
```

## Usage

### Basic Example

Here is a simple example of how to use GeoSHPer to convert shapefile data to GeoJSON:

```javascript
// @require  https://update.greasyfork.org/scripts/526996/1537647/GeoSHPer.js
// @require  https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.15.0/proj4-src.js

(async () => {
    const response = await fetch('path/to/your/shapefile.zip');
    const buffer = await response.arrayBuffer();

    const geoSHPer = new GeoSHPer();
    await geoSHPer.read(buffer);
    const geoJSON = geoSHPer.toGeoJSON();
    console.log(geoJSON);
})();
```

### Handling Different Encodings

GeoSHPer supports different string encoding formats specified in .cpg files for .dbf attributes.

```javascript
// Assuming a `.cpg` file exists in your .zip providing character encoding details.
```

## Error Handling

GeoSHPer provides error messages for common issues:
- Forgot buffer: "forgot to pass buffer"
- Invalid buffer: "invalid buffer like object"
- Missing shapefile layers: "no layers found"

Ensure you handle these errors appropriately in your application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Dependencies

- [Proj4js](http://proj4js.org/) (MIT License) - For map projection transformations.

---

# GeoKMLer / GeoKMZer KML and KMZ to GeoJSON Converter

A JavaScript library comprising two main components: GeoKMLer and GeoKMZer. These tools are designed to facilitate the conversion of KML data into GeoJSON format and handle the extraction of KML data from KMZ archives efficiently.

## License

This project is free software licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Overview

GeoKMLer / GeoKMZer provides a comprehensive API to parse, extract, and convert KML/KMZ files into a GeoJSON FeatureCollection. It is suitable for use in geographic data visualization and web mapping applications.

## Features

- **Convert KML to GeoJSON**: Supports points, linestrings, polygons, and multigeometries through GeoKMLer.
- **Extract KML from KMZ**: Unzip and read KML files from KMZ archives using GeoKMZer.
- **Handle Extended Data**: Converts KML `<ExtendedData>` elements into GeoJSON properties.
- **Robust XML Handling**: Efficient parsing and normalization of XML data.
- **No External Dependencies**: Lightweight and easy to integrate into various projects.

## Usage

GeoKMLer / GeoKMZer makes it easy to work with both KML files directly and KMZ archives.
Here’s how you can use these tools in your application:

### Example for GeoKMLer

```javascript
// @require             https://update.greasyfork.org/scripts/524747/1542062/GeoKMLer.js
// @require             https://update.greasyfork.org/scripts/527113/1538395/GeoKMZer.js

var geoKMLer = new GeoKMLer(); // Create a new instance of GeoKMLer

// Sample KML data input
const kmlData = `...KML data string...`;

// Parse the KML data
const xmlDoc = geoKMLer.read(kmlData);

// Convert to GeoJSON
const geoJson = geoKMLer.toGeoJSON(xmlDoc);

console.log(geoJson);
```

### Example for GeoKMZer

```javascript
(async () => {
    // Assume your KMZ file is loaded and represented as `fileBuffer`

    const fileBuffer = ...; // Load your KMZ file here (e.g., from a fetch request or a file input)

    try {
        // Initialize instances of GeoKMZer and GeoKMLer
        const geoKMZer = new GeoKMZer();
        const geoKMLer = new GeoKMLer();

        // Extract KML contents from the KMZ buffer
        const kmlContentsArray = await geoKMZer.read(fileBuffer);

        // Process each KML and convert to GeoJSON
        kmlContentsArray.forEach(({ filename, content }) => {
            console.log(`Processing file: ${filename}`);
            
            // Parse the KML content
            const kmlDoc = geoKMLer.read(content);
            
            // Convert the KML document to a GeoJSON object
            const geoJson = geoKMLer.toGeoJSON(kmlDoc);

            // Output the GeoJSON to the console
            console.log(`GeoJSON for ${filename}:`, geoJson);
        });

    } catch (error) {
        console.error("Error processing KMZ file:", error);
    }
})();
```

### GeoKMLer

- read(kmlText): Parses a KML string into an XML Document using DOMParser.
- toGeoJSON(document): Converts an XML Document into a GeoJSON FeatureCollection.
- extractExtendedData(placemark): Extracts extended data from a KML Placemark and includes it as GeoJSON properties.

### GeoKMZer

- read(buffer): Reads a KMZ buffer and extracts KML files.
- unzipKMZ(buffer, parentFile = ''): Unzips a KMZ buffer, potentially recursively, to retrieve KML files.

---

# GeoWKTer: WKT to GeoJSON Converter

GeoWKTer is a JavaScript library designed to facilitate the conversion of Well-Known Text (WKT) geometries into GeoJSON format. This library is especially beneficial for developers and GIS specialists working with geographic data across varying standards. By implementing robust methods for parsing and conversion, GeoWKTer ensures seamless transitions between WKT and GeoJSON representations.

## Features

- **Support for Various WKT Types**: Accurately converts diverse geometry types, including `POINT`, `LINESTRING`, `POLYGON`, `MULTIPOINT`, `MULTILINESTRING`, `MULTIPOLYGON`, and `GEOMETRYCOLLECTION`.
- **Streamlined API**: Provides a simple and intuitive interface for converting WKT inputs into GeoJSON `FeatureCollections`.

## Usage

Below is a basic example of how to use the GeoWKTer library:

```javascript
// @require             https://update.greasyfork.org/scripts/523986/1575829/GeoWKTer.js

// Initialize the GeoWKTer instance
let geoWKTer = new GeoWKTer();

// Example WKT input
let wktText = "GEOMETRYCOLLECTION(POINT(4 6), LINESTRING(4 6, 7 10))";

// Convert WKT to GeoJSON
let wktDataArray = geoWKTer.read(wktText, 'Example Label');
let geoJsonData = geoWKTer.toGeoJSON(wktDataArray);

// Output GeoJSON
console.log(JSON.stringify(geoJsonData, null, 2));
```

## API

### GeoWKTer

- **read(wktText, label):** 
  - **Description**: Parses a WKT string into an array of geometry objects. Assigns a specified label to each parsed geometry.
  - **Parameters**:
    - `wktText` (string): The Well-Known Text string representing the geometries.
    - `label` (string): An optional label to associate with the geometries for identification or classification.

- **toGeoJSON(dataArray):**
  - **Description**: Converts an array of parsed WKT data into a GeoJSON `FeatureCollection`.
  - **Parameters**:
    - `dataArray` (Object[]): The internal data array produced by the `read` method, ready for transformation into GeoJSON format.

---

# GeoGMLer

GeoGMLer is a JavaScript library designed to efficiently convert GML (Geography Markup Language) data into GeoJSON format. It supports a wide range of GML geometries, making it ideal for integrating GML spatial data into web mapping applications and geographic data visualization tools.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Overview

GeoGMLer offers a comprehensive API to parse GML files and convert them into a GeoJSON `FeatureCollection`. It is suitable for use in geographic data visualization and web mapping applications, providing support for various geometry types and coordinate reference systems.

## Features

- **Convert GML to GeoJSON**: Supports conversion of Points, LineStrings, Polygons, and complex structures like `gml:MultiCurve` and `gml:MultiSurface` into GeoJSON.
- **CRS Support**: Handles coordinate reference systems by extracting CRS information from GML and utilizing it during conversion.
- **Robust XML Parsing**: Utilizes DOMParser for efficient parsing and handling of XML data, ensuring accurate extraction of geographical features and attributes.
- **Geometry Processing**: Parses and processes both simple and complex geometries, including multi-geometries.
- **No External Dependencies**: Lightweight and easy to integrate into various projects without requiring additional libraries.

## Usage

To use GeoGMLer, create an instance of `GeoGMLer` and utilize its methods to perform conversions from GML strings to GeoJSON objects.

### Example

```javascript
// @require             https://update.greasyfork.org/scripts/526229/1537672/GeoGMLer.js

var geoGMLer = new GeoGMLer(); // Create a new instance of GeoGMLer

// Sample GML data input
const gmlData = `...GML data string...`;

// Parse the GML data
const { xmlDoc, crsName } = geoGMLer.read(gmlData);

// Convert to GeoJSON
const geoJson = geoGMLer.toGeoJSON({ xmlDoc, crsName });

console.log(geoJson);
```

## Key Methods

- read(gmlText): Parses a GML string into an XML Document and extracts the CRS using DOMParser.
- toGeoJSON({ xmlDoc, crsName }): Converts a parsed XML Document along with CRS information into a GeoJSON FeatureCollection.
- getFeatureEleProperties(featureEle): Extracts properties from a GML feature element.
- processMultiSurface(multiSurfaceElement, crsName): Processes gml:MultiSurface elements to extract polygon data.
- processMultiCurve(multiCurveElement, crsName): Processes gml:MultiCurve elements to extract line string data.

---
# GeoGPXer

GeoGPXer is a JavaScript library designed to convert GPX data into GeoJSON format efficiently. It supports the conversion of waypoints, tracks, and routes, with additional handling for GPX extensions.

## License

This project is free software licensed under the GNU LESSER GENERAL PUBLIC LICENS v3. See the [LICENSE](LICENSE) file for more details.

## Overview

GeoGPXer provides an easy-to-use API to parse GPX files and convert them into a GeoJSON FeatureCollection, making it suitable for use in web mapping applications and geographic data visualization.

## Features

- **Convert GPX to GeoJSON**: Supports waypoints, tracks, and routes.
- **Handle Extensions**: Converts GPX `<extensions>` to prefixed GeoJSON properties to avoid conflicts.
- **No External Dependencies**: Lightweight and easy to integrate into various projects.

## Usage

To use GeoGPXer, create an instance of `GeoGPXer` and use its methods to perform the conversion from GPX strings to GeoJSON objects.

### Example

```javascript
// @require             https://update.greasyfork.org/scripts/523870/1534525/GeoGPXer.js

var geoGPXer = new GeoGPXer(); // Create a new instance of GeoGPXer

// Sample GPX data input
const gpxData = `...GPX data string...`;

// Parse the GPX data
const xmlDoc = geoGPXer.read(gpxData);

// Convert to GeoJSON
const geoJson = geoGPXer.toGeoJSON(xmlDoc);

console.log(geoJson);
```

## Key Methods
- read(gpxText): Parses a GPX string into an XML Document using DOMParser.
- toGeoJSON(document): Converts an XML Document into a GeoJSON FeatureCollection.
- extractProperties(node): Extracts properties from a GPX node, including handling of <extensions> by prefixing property names.