# ohsome API — API Reference

This REST-based API aims to leverage the tools of the <a href="https://github.com/GIScience/oshdb" target="_blank">OSHDB</a> through allowing to access some of its functionalities via HTTP requests. 
The official documentation can be found <a href="https://docs.ohsome.org/ohsome-api/stable" target="_blank">here</a>.

**Version:** 1.2.3  
**Base URL:** `https://api.ohsome.org/v1`

## Area

Compute the area of polygonal OSM elements

### GET /elements/area

**Area of OSM elements**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area

**Area of OSM elements**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/density

**Density of OSM elements (area of elements divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/density

**Density of OSM elements (area of elements divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/density/groupBy/boundary

**Density of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/density/groupBy/boundary

**Density of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/density/groupBy/boundary/groupBy/tag

**Density of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/density/groupBy/boundary/groupBy/tag

**Density of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/density/groupBy/tag

**Density of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/density/groupBy/tag

**Density of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/density/groupBy/type

**Density of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/density/groupBy/type

**Density of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/groupBy/boundary

**Area of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/groupBy/boundary

**Area of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/groupBy/boundary/groupBy/tag

**Area of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/groupBy/boundary/groupBy/tag

**Area of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/groupBy/key

**Area of OSM elements grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `building`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/groupBy/key

**Area of OSM elements grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `building`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/groupBy/tag

**Area of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/groupBy/tag

**Area of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/groupBy/type

**Area of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/groupBy/type

**Area of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/ratio

**Ratio of the area of OSM elements satisfying filter2 within items selected by filter**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:relation and building=*`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `ratioResult` (array of object, required) — ElementsResult for /ratio requests
    - `ratio` (number (double), required) — Ratio of value2/value
    - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
    - `value` (number (double), required) — Value corresponding to the initial filter parameters
    - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/ratio

**Ratio of the area of OSM elements satisfying filter2 within items selected by filter**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:relation and building=*`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `ratioResult` (array of object, required) — ElementsResult for /ratio requests
    - `ratio` (number (double), required) — Ratio of value2/value
    - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
    - `value` (number (double), required) — Value corresponding to the initial filter parameters
    - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/area/ratio/groupBy/boundary

**Ratio of the area of OSM elements grouped by the boundary**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `building=*`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByBoundaryResult` (array of object, required) — RatioGroupByResult array holding the respective objects with their timestamp-value-value2-ratio values
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `ratioResult` (array of object, required) — RatioResult array holding timestamp, whole and part values
      - `ratio` (number (double), required) — Ratio of value2/value
      - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
      - `value` (number (double), required) — Value corresponding to the initial filter parameters
      - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/area/ratio/groupBy/boundary

**Ratio of the area of OSM elements grouped by the boundary**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `building=*`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByBoundaryResult` (array of object, required) — RatioGroupByResult array holding the respective objects with their timestamp-value-value2-ratio values
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `ratioResult` (array of object, required) — RatioResult array holding timestamp, whole and part values
      - `ratio` (number (double), required) — Ratio of value2/value
      - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
      - `value` (number (double), required) — Value corresponding to the initial filter parameters
      - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

## Count

Compute the count of point/linear/polygonal OSM elements

### GET /elements/count

**Count of OSM elements**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count

**Count of OSM elements**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/density

**Density of OSM elements (number of elements divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/density

**Density of OSM elements (number of elements divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/density/groupBy/boundary

**Density of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/density/groupBy/boundary

**Density of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/density/groupBy/boundary/groupBy/tag

**Density of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/density/groupBy/boundary/groupBy/tag

**Density of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/density/groupBy/tag

**Density of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/density/groupBy/tag

**Density of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/density/groupBy/type

**Density of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/density/groupBy/type

**Density of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/groupBy/boundary

**Count of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/groupBy/boundary

**Count of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/groupBy/boundary/groupBy/tag

**Count of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/groupBy/boundary/groupBy/tag

**Count of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/groupBy/key

**Count of OSM elements grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `building`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/groupBy/key

**Count of OSM elements grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `building`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/groupBy/tag

**Count of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/groupBy/tag

**Count of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/groupBy/type

**Count of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/groupBy/type

**Count of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/ratio

**Ratio of OSM elements satisfying filter2 within items selected by filter**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:node and "addr:housenumber=*"`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `ratioResult` (array of object, required) — ElementsResult for /ratio requests
    - `ratio` (number (double), required) — Ratio of value2/value
    - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
    - `value` (number (double), required) — Value corresponding to the initial filter parameters
    - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/ratio

**Ratio of OSM elements satisfying filter2 within items selected by filter**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:node and "addr:housenumber=*"`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `ratioResult` (array of object, required) — ElementsResult for /ratio requests
    - `ratio` (number (double), required) — Ratio of value2/value
    - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
    - `value` (number (double), required) — Value corresponding to the initial filter parameters
    - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/count/ratio/groupBy/boundary

**Ratio of OSM elements grouped by the boundary**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:node and "addr:housenumber=*"`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByBoundaryResult` (array of object, required) — RatioGroupByResult array holding the respective objects with their timestamp-value-value2-ratio values
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `ratioResult` (array of object, required) — RatioResult array holding timestamp, whole and part values
      - `ratio` (number (double), required) — Ratio of value2/value
      - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
      - `value` (number (double), required) — Value corresponding to the initial filter parameters
      - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/count/ratio/groupBy/boundary

**Ratio of OSM elements grouped by the boundary**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:node and "addr:housenumber=*"`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByBoundaryResult` (array of object, required) — RatioGroupByResult array holding the respective objects with their timestamp-value-value2-ratio values
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `ratioResult` (array of object, required) — RatioResult array holding timestamp, whole and part values
      - `ratio` (number (double), required) — Ratio of value2/value
      - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
      - `value` (number (double), required) — Value corresponding to the initial filter parameters
      - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

## Length

Compute the length of linear OSM elements

### GET /elements/length

**Length of OSM elements**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length

**Length of OSM elements**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/density

**Density of OSM elements (length of elements divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/density

**Density of OSM elements (length of elements divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/density/groupBy/boundary

**Density of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/density/groupBy/boundary

**Density of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/density/groupBy/boundary/groupBy/tag

**Density of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/density/groupBy/boundary/groupBy/tag

**Density of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/density/groupBy/tag

**Density of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `highway`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/density/groupBy/tag

**Density of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `highway`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/density/groupBy/type

**Density of OSM elements grouped by the OSM type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/density/groupBy/type

**Density of OSM elements grouped by the OSM type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/groupBy/boundary

**Length of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/groupBy/boundary

**Length of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/groupBy/boundary/groupBy/tag

**Length of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/groupBy/boundary/groupBy/tag

**Length of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/groupBy/key

**Length of OSM elements grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `highway`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/groupBy/key

**Length of OSM elements grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `highway`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/groupBy/tag

**Length of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `highway`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/groupBy/tag

**Length of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `highway`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/groupBy/type

**Length of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/groupBy/type

**Length of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/ratio

**Ratio of OSM elements satisfying filter2 within items selected by filter**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `highway=residential`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `ratioResult` (array of object, required) — ElementsResult for /ratio requests
    - `ratio` (number (double), required) — Ratio of value2/value
    - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
    - `value` (number (double), required) — Value corresponding to the initial filter parameters
    - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/ratio

**Ratio of OSM elements satisfying filter2 within items selected by filter**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `highway=residential`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `ratioResult` (array of object, required) — ElementsResult for /ratio requests
    - `ratio` (number (double), required) — Ratio of value2/value
    - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
    - `value` (number (double), required) — Value corresponding to the initial filter parameters
    - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/length/ratio/groupBy/boundary

**Ratio of the length of OSM elements grouped by the boundary**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `highway=residential`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByBoundaryResult` (array of object, required) — RatioGroupByResult array holding the respective objects with their timestamp-value-value2-ratio values
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `ratioResult` (array of object, required) — RatioResult array holding timestamp, whole and part values
      - `ratio` (number (double), required) — Ratio of value2/value
      - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
      - `value` (number (double), required) — Value corresponding to the initial filter parameters
      - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/length/ratio/groupBy/boundary

**Ratio of the length of OSM elements grouped by the boundary**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `highway=residential`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByBoundaryResult` (array of object, required) — RatioGroupByResult array holding the respective objects with their timestamp-value-value2-ratio values
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `ratioResult` (array of object, required) — RatioResult array holding timestamp, whole and part values
      - `ratio` (number (double), required) — Ratio of value2/value
      - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
      - `value` (number (double), required) — Value corresponding to the initial filter parameters
      - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

## Perimeter

Compute the perimeter of polygonal OSM elements

### GET /elements/perimeter

**Perimeter of OSM elements**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter

**Perimeter of OSM elements**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/density

**Density of OSM elements (perimeter of elements divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/density

**Density of OSM elements (perimeter of elements divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/density/groupBy/boundary

**Density of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/density/groupBy/boundary

**Density of OSM elements grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/density/groupBy/boundary/groupBy/tag

**Density of grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/density/groupBy/boundary/groupBy/tag

**Density of grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/density/groupBy/tag

**Density of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/density/groupBy/tag

**Density of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/density/groupBy/type

**Density of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/density/groupBy/type

**Density of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/groupBy/boundary

**Perimeter of OSM elements in grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/groupBy/boundary

**Perimeter of OSM elements in grouped by the boundary (bboxes, bcircles, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/groupBy/boundary/groupBy/tag

**Perimeter of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/groupBy/boundary/groupBy/tag

**Perimeter of OSM elements grouped by the boundary and the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/groupBy/key

**Perimeter of OSM elements grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `building`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/groupBy/key

**Perimeter of OSM elements grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `building`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/groupBy/tag

**Perimeter of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/groupBy/tag

**Perimeter of OSM elements grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/groupBy/type

**Perimeter of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/groupBy/type

**Perimeter of OSM elements grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/ratio

**Ratio of OSM elements satisfying filter2 within items selected by filter**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `ratioResult` (array of object, required) — ElementsResult for /ratio requests
    - `ratio` (number (double), required) — Ratio of value2/value
    - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
    - `value` (number (double), required) — Value corresponding to the initial filter parameters
    - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/ratio

**Ratio of OSM elements satisfying filter2 within items selected by filter**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `ratioResult` (array of object, required) — ElementsResult for /ratio requests
    - `ratio` (number (double), required) — Ratio of value2/value
    - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
    - `value` (number (double), required) — Value corresponding to the initial filter parameters
    - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /elements/perimeter/ratio/groupBy/boundary

**Ratio of the perimeter of OSM elements grouped by the boundary**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByBoundaryResult` (array of object, required) — RatioGroupByResult array holding the respective objects with their timestamp-value-value2-ratio values
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `ratioResult` (array of object, required) — RatioResult array holding timestamp, whole and part values
      - `ratio` (number (double), required) — Ratio of value2/value
      - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
      - `value` (number (double), required) — Value corresponding to the initial filter parameters
      - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /elements/perimeter/ratio/groupBy/boundary

**Ratio of the perimeter of OSM elements grouped by the boundary**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `filter2` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `keys2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `types2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values2` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter2' instead. |

**Parameter dependencies:** `OnlyOne(bboxes, bcircles, bpolys);`; `ZeroOrOne(filter, Or(types, keys, values));`; `IF values THEN keys;`; `IF values2 THEN keys2;`

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByBoundaryResult` (array of object, required) — RatioGroupByResult array holding the respective objects with their timestamp-value-value2-ratio values
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `ratioResult` (array of object, required) — RatioResult array holding timestamp, whole and part values
      - `ratio` (number (double), required) — Ratio of value2/value
      - `timestamp` (string, required) — Timestamp in the format YYYY-MM-DDThh:mm:ssZ
      - `value` (number (double), required) — Value corresponding to the initial filter parameters
      - `value2` (number (double), required) — Value corresponding to the second (2) filter parameters
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

## Users

Compute data aggregation functions on users

### GET /users/count

**Count of OSM users**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count

**Count of OSM users**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /users/count/density

**Density of OSM users (number of users divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count/density

**Density of OSM users (number of users divided by the total area in square-kilometers)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `result` (array of object, required) — ElementsResult holding timestamp-value pairs
    - `value` (number (double))
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /users/count/density/groupBy/boundary

**Count of OSM users grouped by boundary (bboxes, bcirlces, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count/density/groupBy/boundary

**Count of OSM users grouped by boundary (bboxes, bcirlces, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /users/count/density/groupBy/tag

**Density of OSM users grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count/density/groupBy/tag

**Density of OSM users grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /users/count/density/groupBy/type

**Density of OSM users grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count/density/groupBy/type

**Density of OSM users grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /users/count/groupBy/boundary

**Count of OSM users grouped by boundary (bboxes, bcirlces, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count/groupBy/boundary

**Count of OSM users grouped by boundary (bboxes, bcirlces, or bpolys)**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /users/count/groupBy/key

**Count of OSM users grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `building`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count/groupBy/key

**Count of OSM users grouped by the key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKeys` | query | string | No | OSM key(s) e.g.: 'highway', 'building'; default: no key. Default: `building`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /users/count/groupBy/tag

**Count of OSM users grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count/groupBy/tag

**Count of OSM users grouped by the tag**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `groupByKey` | query | string | No | OSM key e.g.: 'highway', 'building'; no default value (one groupByKey parameter must be defined). Default: `building`. |
| `groupByValues` | query | string | No | OSM value(s) e.g.: 'primary', 'residential'; default: no value |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### GET /users/count/groupBy/type

**Count of OSM users grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable

### POST /users/count/groupBy/type

**Count of OSM users grouped by the type**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bboxes` | query | string | No | WGS84 coordinates in the following format: id1:lon1,lat1,lon2,lat2\|id2:lon1,lat1,lon2,lat2\|... OR lon1,lat1,lon2,lat2\|lon1,lat1,lon2,lat2\|...; no default value (one boundary parameter must be defined). Default: `8.625,49.3711,8.7334,49.4397`. |
| `bcircles` | query | string | No | WGS84 coordinates + radius in meter in the following format: id1:lon,lat,r\|id2:lon,lat,r\|... OR lon,lat,r\|lon,lat,r\|...; no default value (one boundary parameter must be defined) |
| `bpolys` | query | string | No | WGS84 coordinates given as a list of coordinate pairs (as for bboxes) or GeoJSON FeatureCollection. The first point has to be the same as the last point and MultiPolygons are only supported in GeoJSON; no default value (one boundary parameter must be defined) |
| `filter` | query | string | No | Combines several attributive filters, e.g. OSM type, the geometry (simple feature) type, as well as the OSM tag; no default value. Default: `type:way`. |
| `format` | query | string | No | Output format geojson (for /groupBy/boundary resources only), csv, or json; default: json. Default: `json`. |
| `keys` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `showMetadata` | query | string | No | Boolean operator 'true' or 'false'; default: 'false' |
| `time` | query | string | No | ISO-8601 conform timestring(s); default: latest timestamp within dataset. Default: `2014-01-01/2017-01-01/P1Y`. |
| `timeout` | query | string | No | Custom timeout in seconds; no default value |
| `types` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |
| `values` | query | string | No | This parameter has been deprecated since v1.0. We encourage you to use the new parameter 'filter' instead. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `apiVersion` (string, required) — Version of this api
  - `attribution` (object, required)
    - `text` (string, required) — Copyright info about the used data
    - `url` (string, required) — URL to the copyright and license info
  - `features` (array of object, required) — GeoJSON Features
    - `bbox` (array of number (double))
    - `crs` (object)
      - `properties` (object)
      - `type` (string) — Allowed values: `name`, `link`.
    - `geometry` (object)
      - `bbox` (array of number (double))
      - `crs` (object)
        - `properties` (object)
        - `type` (string) — Allowed values: `name`, `link`.
    - `id` (string)
    - `properties` (object)
  - `groupByResult` (array of object, required) — GroupByResult array holding the respective objects with their timestamp-value pairs
    - `groupByObject` (object, required) — Object on which the results are grouped on
    - `result` (array of object, required) — Result array holding timestamp-value pairs
      - `value` (number (double))
  - `metadata` (object)
    - `description` (string, required) — Text describing the result in a sentence
    - `executionTime` (integer (int64), required) — Time the server needed to execute the request
    - `requestUrl` (string, required) — Request URL to which this whole output JSON was generated
  - `type` (string, required) — Type of the GeoJSON
- **400** — Bad request
- **401** — Unauthorized
- **404** — Not found
- **405** — Method not allowed
- **413** — Payload too large
- **500** — Internal server error
- **501** — Not implemented
- **503** — Service Unavailable
