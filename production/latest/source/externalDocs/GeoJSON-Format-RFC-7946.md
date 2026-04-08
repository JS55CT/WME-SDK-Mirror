# RFC 7946: The GeoJSON Format

**Internet Engineering Task Force (IETF)**  
**Request for Comments: 7946**  
**Category:** Standards Track  
**ISSN:** 2070-1721  

**Authors:**  
- H. Butler (Hobu Inc.)  
- M. Daly (Cadcorp)  
- A. Doyle  
- S. Gillies (Mapbox)  
- S. Hagen  
- T. Schaub (Planet Labs)  

*August 2016*

---

## Abstract

GeoJSON is a geospatial data interchange format based on JavaScript Object Notation (JSON). It defines several types of JSON objects and the manner in which they are combined to represent data about geographic features, their properties, and their spatial extents. GeoJSON uses the World Geodetic System 1984 and units of decimal degrees.

---

## Status of This Memo

This is an Internet Standards Track document and a product of the Internet Engineering Task Force (IETF).

Further information, errata, and feedback:  
http://www.rfc-editor.org/info/rfc7946

---

## Copyright Notice

Copyright (c) 2016 IETF Trust and the persons identified as the document authors. All rights reserved.  
See [IETF Trust Legal Provisions](http://trustee.ietf.org/license-info).

---

## Table of Contents

- [RFC 7946: The GeoJSON Format](#rfc-7946-the-geojson-format)
  - [Abstract](#abstract)
  - [Status of This Memo](#status-of-this-memo)
  - [Copyright Notice](#copyright-notice)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [1.1 Requirements Language](#11-requirements-language)
    - [1.2 Conventions Used](#12-conventions-used)
    - [1.3 Specification of GeoJSON](#13-specification-of-geojson)
    - [1.4 Definitions](#14-definitions)
    - [1.5 Example](#15-example)
  - [2. GeoJSON Text](#2-geojson-text)
  - [3. GeoJSON Object](#3-geojson-object)
    - [3.1 Geometry Object](#31-geometry-object)
      - [3.1.1 Position](#311-position)
      - [3.1.2 Point](#312-point)
      - [3.1.3 MultiPoint](#313-multipoint)
      - [3.1.4 LineString](#314-linestring)
      - [3.1.5 MultiLineString](#315-multilinestring)
      - [3.1.6 Polygon](#316-polygon)
      - [3.1.7 MultiPolygon](#317-multipolygon)
      - [3.1.8 GeometryCollection](#318-geometrycollection)
      - [3.1.9 Antimeridian Cutting](#319-antimeridian-cutting)
      - [3.1.10 Uncertainty and Precision](#3110-uncertainty-and-precision)
    - [3.2 Feature Object](#32-feature-object)
    - [3.3 FeatureCollection Object](#33-featurecollection-object)
  - [4. Coordinate Reference System](#4-coordinate-reference-system)
  - [5. Bounding Box](#5-bounding-box)
    - [5.1 The Connecting Lines](#51-the-connecting-lines)
    - [5.2 The Antimeridian](#52-the-antimeridian)
    - [5.3 The Poles](#53-the-poles)
  - [6. Extending GeoJSON](#6-extending-geojson)
    - [6.1 Foreign Members](#61-foreign-members)
  - [7. GeoJSON Types Are Not Extensible](#7-geojson-types-are-not-extensible)
    - [7.1 Semantics of GeoJSON Members and Types Are Not Changeable](#71-semantics-of-geojson-members-and-types-are-not-changeable)
  - [8. Versioning](#8-versioning)
  - [9. Mapping 'geo' URIs](#9-mapping-geo-uris)
  - [10. Security Considerations](#10-security-considerations)
  - [11. Interoperability Considerations](#11-interoperability-considerations)
    - [11.1 I-JSON](#111-i-json)
    - [11.2 Coordinate Precision](#112-coordinate-precision)
  - [12. IANA Considerations](#12-iana-considerations)
  - [13. References](#13-references)
    - [13.1 Normative References](#131-normative-references)
    - [13.2 Informative References](#132-informative-references)
  - [Appendix A. Geometry Examples](#appendix-a-geometry-examples)
    - [A.1 Points](#a1-points)
    - [A.2 LineStrings](#a2-linestrings)
    - [A.3 Polygons](#a3-polygons)
    - [A.4 MultiPoints](#a4-multipoints)
    - [A.5 MultiLineStrings](#a5-multilinestrings)
    - [A.6 MultiPolygons](#a6-multipolygons)
    - [A.7 GeometryCollections](#a7-geometrycollections)
  - [Appendix B: Changes from Pre-IETF Spec](#appendix-b-changes-from-pre-ietf-spec)
    - [Normative Changes](#normative-changes)
    - [Informative Changes](#informative-changes)
  - [Appendix C: GeoJSON Text Sequences](#appendix-c-geojson-text-sequences)
  - [Acknowledgements](#acknowledgements)
  - [Authors' Addresses](#authors-addresses)

---

## 1. Introduction

GeoJSON is a format for encoding a variety of geographic data structures using JavaScript Object Notation (JSON) ([RFC7159]). A GeoJSON object may represent a region of space (a Geometry), a spatially bounded entity (a Feature), or a list of Features (a FeatureCollection). Supported geometry types: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection.

Features contain a Geometry object and additional properties, and a FeatureCollection contains a list of Features.

---

### 1.1 Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are interpreted as described in [RFC2119].

---

### 1.2 Conventions Used

- JSON object member order is irrelevant ([RFC7159]).
- Some examples use `// ...` as placeholder notation, which should be deleted before validation.
- Whitespace is used for clarity, not required by JSON.

---

### 1.3 Specification of GeoJSON

This document supersedes the original GeoJSON format specification ([GJ2008]).

---

### 1.4 Definitions

- JSON terms as defined in [RFC7159].
- Geometry types: `"Point"`, `"MultiPoint"`, `"LineString"`, `"MultiLineString"`, `"Polygon"`, `"MultiPolygon"`, `"GeometryCollection"`.
- GeoJSON types: geometry types plus `"Feature"`, `"FeatureCollection"`.
- "Collection" just means a JSON array.

---

### 1.5 Example

**GeoJSON FeatureCollection Example:**

    {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [102.0, 0.5]
          },
          "properties": { "prop0": "value0" }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "LineString",
            "coordinates": [
              [102.0, 0.0],
              [103.0, 1.0],
              [104.0, 0.0],
              [105.0, 1.0]
            ]
          },
          "properties": { "prop0": "value0", "prop1": 0.0 }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Polygon",
            "coordinates": [
              [
                [100.0, 0.0],
                [101.0, 0.0],
                [101.0, 1.0],
                [100.0, 1.0],
                [100.0, 0.0]
              ]
            ]
          },
          "properties": { "prop0": "value0", "prop1": { "this": "that" } }
        }
      ]
    }

---

## 2. GeoJSON Text

A GeoJSON text is a JSON text and consists of a single GeoJSON object.

---

## 3. GeoJSON Object

- Must have a `"type"` member, value is one of the GeoJSON types.
- MAY have a `"bbox"` member (bounding box array).
- MAY have foreign members.

---

### 3.1 Geometry Object

Represents points, curves, and surfaces in coordinate space.

- Must specify `"type"` (one of geometry types).
- Except `"GeometryCollection"`, must have `"coordinates"` (structure depends on geometry type).

#### 3.1.1 Position

Basic construct (array of two or more numbers).  
First two elements are longitude and latitude (in that order), optional third element is altitude.

A straight line between two positions (not geodesic):

    F(lon, lat) = (lon0 + (lon1 - lon0) * t, lat0 + (lat1 - lat0) * t)
    where t ∈ [0, 1]

#### 3.1.2 Point

For `"Point"`, `"coordinates"` is a single position.

#### 3.1.3 MultiPoint

For `"MultiPoint"`, `"coordinates"` is an array of positions.

#### 3.1.4 LineString

For `"LineString"`, `"coordinates"` is an array of two or more positions.

#### 3.1.5 MultiLineString

For `"MultiLineString"`, `"coordinates"` is an array of LineString coordinate arrays.

#### 3.1.6 Polygon

A polygon is an array of linear rings.  
The first ring is the exterior, subsequent rings are holes.

#### 3.1.7 MultiPolygon

An array of Polygon coordinate arrays.

#### 3.1.8 GeometryCollection

An array (`"geometries"`) of Geometry objects.  
Avoid nested GeometryCollections.

#### 3.1.9 Antimeridian Cutting

Geometries crossing the antimeridian should be split.

**Example MultiLineString:**

    {
      "type": "MultiLineString",
      "coordinates": [
        [
          [170.0, 45.0], [180.0, 45.0]
        ],
        [
          [-180.0, 45.0], [-170.0, 45.0]
        ]
      ]
    }

**Example MultiPolygon:**

    {
      "type": "MultiPolygon",
      "coordinates": [
        [
          [
            [180.0, 40.0], [180.0, 50.0], [170.0, 50.0],
            [170.0, 40.0], [180.0, 40.0]
          ]
        ],
        [
          [
            [-170.0, 40.0], [-170.0, 50.0], [-180.0, 50.0],
            [-180.0, 40.0], [-170.0, 40.0]
          ]
        ]
      ]
    }

#### 3.1.10 Uncertainty and Precision

Number of digits does not indicate uncertainty.

---

### 3.2 Feature Object

- `"type": "Feature"`
- `"geometry"`: a Geometry object or null (if unlocated)
- `"properties"`: an object or null
- `"id"`: string or number (optional)

---

### 3.3 FeatureCollection Object

Type `"FeatureCollection"`; `"features"` is an array of Feature objects.

---

## 4. Coordinate Reference System

- CRS is WGS 84, (longitude, latitude) in decimal degrees.
- Optional third position is height (meters).
- Alternative CRS is **NOT SUPPORTED**.

---

## 5. Bounding Box

- `"bbox"` member: length 2*n array (where n = dimension) using same axis order as geometry.
- BBox follows edges of constant longitude, latitude, elevation.

**Examples:**

2D bbox on Feature:

    {
      "type": "Feature",
      "bbox": [-10.0, -10.0, 10.0, 10.0],
      "geometry": { ... }
      //...
    }

2D bbox on FeatureCollection:

    {
      "type": "FeatureCollection",
      "bbox": [100.0, 0.0, 105.0, 1.0],
      "features": [
        //...
      ]
    }

3D bbox (with depth):

    {
      "type": "FeatureCollection",
      "bbox": [100.0, 0.0, -100.0, 105.0, 1.0, 0.0],
      "features": [
        //...
      ]
    }

### 5.1 The Connecting Lines

Northernmost line:

    (lon, lat) = (west + (east - west) * t, north), 0 <= t <= 1

### 5.2 The Antimeridian

Bounding box crossing antimeridian might look like:  
`"bbox": [177.0, -20.0, -178.0, -16.0]`

### 5.3 The Poles

North pole:

    "bbox": [-180.0, minlat, 180.0, 90.0]

South pole:

    "bbox": [-180.0, -90.0, 180.0, maxlat]

---

## 6. Extending GeoJSON

### 6.1 Foreign Members

Foreign (non-spec) members allowed, but support varies.

**Example with a foreign member:**

    {
      "type": "Feature",
      "id": "f1",
      "geometry": { ... },
      "properties": { ... },
      "title": "Example Feature"
    }

---

## 7. GeoJSON Types Are Not Extensible

Types cannot be extended:  
FeatureCollection, Feature, Point, LineString, MultiPoint, Polygon, MultiLineString, MultiPolygon, GeometryCollection.

### 7.1 Semantics of GeoJSON Members and Types Are Not Changeable

Members must not be repurposed or moved across types.

---

## 8. Versioning

No explicit versioning scheme.  
Changing semantics creates a new format, not a new version.

---

## 9. Mapping 'geo' URIs

Geo URIs ([RFC5870]) map to GeoJSON Point geometries.

Geo URI:

    geo:lat,lon,alt

GeoJSON:

    {"type": "Point", "coordinates": [lon, lat, alt]}

GeoJSON does not represent uncertainty.

---

## 10. Security Considerations

See [RFC7159].  
GeoJSON does not provide privacy or integrity services.  
Sensitive location data must be protected by the transport layer (e.g., TLS).  
Location obscuration is generally not an effective defense ([Sweeney], [RFC6772]).

---

## 11. Interoperability Considerations

### 11.1 I-JSON

GeoJSON texts should follow [RFC7493] constraints.

### 11.2 Coordinate Precision

Higher precision means larger files; 6 decimals (~10 cm) usually sufficient.

---

## 12. IANA Considerations

- Media type: `application/geo+json`
- File extensions: `.geojson`, `.json`
- Contact: Sean Gillies (sean.gillies@gmail.com)

---

## 13. References

### 13.1 Normative References

- [RFC2119](http://www.rfc-editor.org/info/rfc2119)
- [RFC6838](http://www.rfc-editor.org/info/rfc6838)
- [RFC7159](http://www.rfc-editor.org/info/rfc7159)
- [RFC7493](http://www.rfc-editor.org/info/rfc7493)
- [WGS84] NIMA, "Department of Defense World Geodetic System 1984..."

### 13.2 Informative References

- [GJ2008] "The GeoJSON Format Specification", June 2008
- [KMLv2.2] OGC KML 2.2.0, April 2008
- [RFC5870](http://www.rfc-editor.org/info/rfc5870)
- [RFC6772](http://www.rfc-editor.org/info/rfc6772)
- [RFC7464](http://www.rfc-editor.org/info/rfc7464)
- [SFSQL] "OpenGIS Simple Features Specification For SQL Revision 1.1,"
- [Sweeney] k-anonymity, Int. J. Uncertainty, Fuzziness, Knowledge-based Systems 10 (5)
- [WFSv1] "Web Feature Service Implementation Specification", OGC 04-094

---

## Appendix A. Geometry Examples

### A.1 Points

    {
      "type": "Point",
      "coordinates": [100.0, 0.0]
    }

### A.2 LineStrings

    {
      "type": "LineString",
      "coordinates": [
        [100.0, 0.0],
        [101.0, 1.0]
      ]
    }

### A.3 Polygons

_No holes:_

    {
      "type": "Polygon",
      "coordinates": [
        [
          [100.0, 0.0],
          [101.0, 0.0],
          [101.0, 1.0],
          [100.0, 1.0],
          [100.0, 0.0]
        ]
      ]
    }

_With holes:_

    {
      "type": "Polygon",
      "coordinates": [
        [
          [100.0, 0.0],
          [101.0, 0.0],
          [101.0, 1.0],
          [100.0, 1.0],
          [100.0, 0.0]
        ],
        [
          [100.8, 0.8],
          [100.8, 0.2],
          [100.2, 0.2],
          [100.2, 0.8],
          [100.8, 0.8]
        ]
      ]
    }

### A.4 MultiPoints

    {
      "type": "MultiPoint",
      "coordinates": [
        [100.0, 0.0],
        [101.0, 1.0]
      ]
    }

### A.5 MultiLineStrings

    {
      "type": "MultiLineString",
      "coordinates": [
        [
          [100.0, 0.0],
          [101.0, 1.0]
        ],
        [
          [102.0, 2.0],
          [103.0, 3.0]
        ]
      ]
    }

### A.6 MultiPolygons

    {
      "type": "MultiPolygon",
      "coordinates": [
        [
          [
            [102.0, 2.0],
            [103.0, 2.0],
            [103.0, 3.0],
            [102.0, 3.0],
            [102.0, 2.0]
          ]
        ],
        [
          [
            [100.0, 0.0],
            [101.0, 0.0],
            [101.0, 1.0],
            [100.0, 1.0],
            [100.0, 0.0]
          ],
          [
            [100.2, 0.2],
            [100.2, 0.8],
            [100.8, 0.8],
            [100.8, 0.2],
            [100.2, 0.2]
          ]
        ]
      ]
    }

### A.7 GeometryCollections

    {
      "type": "GeometryCollection",
      "geometries": [
        {
          "type": "Point",
          "coordinates": [100.0, 0.0]
        },
        {
          "type": "LineString",
          "coordinates": [
            [101.0, 0.0],
            [102.0, 1.0]
          ]
        }
      ]
    }

---

## Appendix B: Changes from Pre-IETF Spec

### Normative Changes

- Removed "crs" member.
- In absence of elevation, assume ground/sea level.
- Positions should not extend beyond three elements.
- Lines between positions are straight Cartesian.
- Right-hand rule for polygon rings.
- "bbox" array is `[west, south, east, north]`.
- Feature `"id"` is string or number.
- Extensions must not change semantics.
- Strict member containment.
- New media type: `application/geo+json`.

### Informative Changes

- Definition of GeoJSON text.
- Geo URI mapping rules.
- I-JSON recommendation.
- Coordinate precision concerns.
- Noted GeometryCollection interoperability issues.

---

## Appendix C: GeoJSON Text Sequences

GeoJSON objects are single JSON objects; streaming or sequencing requires a different media type ([RFC7464]).

---

## Acknowledgements

The GeoJSON format is the product of open discussion (GeoJSON mailing list, IETF).  
Material adapted from [geojson.org spec](http://geojson.org/geojson-spec.html) ([GJ2008]), licensed CC BY 3.0 US.

---

## Authors' Addresses

- Howard Butler (howard@hobu.co)
- Martin Daly (martin.daly@cadcorp.com)
- Allan Doyle (adoyle@intl-interfaces.com)
- Sean Gillies (sean.gillies@gmail.com) [http://sgillies.net](http://sgillies.net)
- Stefan Hagen (stefan@hagen.link) [http://stefan-hagen.website/](http://stefan-hagen.website/)
- Tim Schaub (tim.schaub@gmail.com)

---

*This Markdown digest summarizes RFC 7946; see original RFC for normative specification and legal details.*
