# API Reference - Postcodes.io — API Reference

Postcodes.io is a free postcode lookup API and geocoder for the UK.

## Endpoint

All services can be accessed from the following endpoint.

```
https://api.postcodes.io
```

The API accepts GET and POST requests. POST methods use content type `application/json`.

## Responses

Each response comes with an appropriate HTTP Status code (except for JSONP requests). These include 200 for success, 400 for a bad request, 404 for not found and 500 for server error. The HTTP Status code is also included in the response body.

## Authentication

Postcodes.io does not require authentication.

**Version:** 20.0.0  
**Base URL:** `https://api.postcodes.io`

## Postcodes

### GET /postcodes/{postcode}

**Lookup Postcode**

### Postcode Data

Lookup a UK postcode against the ONS Postcode Directory (ONSPD). The response is a fully resolved record — every administrative, electoral, statistical and health geography that ONSPD ships for the postcode is returned at the top level by its human-readable name, with the equivalent GSS / official codes mirrored under the `codes` object.

The same shape is returned by `/postcodes` (bulk + search) and the reverse-geocoding endpoints. `/outcodes` returns a separate, aggregated [Outcode](#tag/Outward-Codes) shape — one row per outward code, with admin / parish / constituency arrays summarising the postcodes inside.

Returns `404` if the postcode does not exist or is not valid.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `postcode` | path | any | Yes | Postcode to retrieve |

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (object, required) — Comprehensive location data including geographic coordinates, administrative boundaries, and electoral information for the requested postcode
    - `postcode` (string, required) — UK postcode format: 2-4 character outward code, a space, and a 3-character inward code (e.g., SW1A 2AA). Updated monthly from Royal Mail.
    - `outcode` (string, required) — The first part of a postcode before the space (2-4 characters). This generally identifies the postal town or district.
    - `incode` (string, required) — The second part of a postcode after the space (always 3 characters). Helps identify specific streets or buildings within a postal area.
    - `quality` (integer, required) — Positional Quality Indicator (1-9). Shows the status of the assigned grid reference: * 1: Within the building of the matched address closest to the postcode mean * 2: As for 1, except by visual inspection of Landline maps (Scotland only) * 3: Approximate to within 50 metres * 4: Postcode unit mean (averaged from addresses with same postcode) * 5: Estimated by ONS using surrounding postcodes * 6: Postcode sector mean (mainly PO Boxes) * 8: Terminated postcode (last known ONS grid reference) * 9: No coordinates available
    - `eastings` (integer (int32), required) — The OS grid reference easting (X-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `northings` (integer (int32), required) — The OS grid reference northing (Y-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `country` (string, required) — The UK constituent country for this postcode (England, Scotland, Wales, Northern Ireland, Channel Islands, or Isle of Man).
    - `nhs_ha` (string, required) — The NHS health authority area for this postcode. May be null.
    - `admin_county` (string, required) — The administrative county for this postcode. Null where the postcode falls outside a county-level authority (the underlying GSS code is then a pseudo such as `E99999999`, surfaced under `codes.admin_county`). May be null.
    - `admin_district` (string, required) — The administrative district or unitary authority for this postcode. May be null.
    - `admin_ward` (string, required) — The electoral/administrative ward for this postcode. May be null.
    - `longitude` (number (double), required) — WGS84 longitude coordinate (east-west position). May be null if geolocation unavailable. May be null.
    - `latitude` (number (double), required) — WGS84 latitude coordinate (north-south position). May be null if geolocation unavailable. May be null.
    - `parliamentary_constituency` (string, required) — The UK Parliamentary constituency for this postcode. May be null.
    - `european_electoral_region` (string, required) — The European Electoral Region for this postcode. May be null.
    - `primary_care_trust` (string, required) — The healthcare administrative area for this postcode. Different naming conventions apply across UK regions. May be null.
    - `region` (string, required) — The regional designation for this postcode (formerly Government Office Regions or GORs). May be null.
    - `parish` (string, required) — The civil parish (England) or community (Wales) for this postcode. May be null.
    - `lsoa` (string, required) — 2021 Census LSOA code (smaller statistical area, typically 1,000-1,500 residents). Now points to 2021 data. May be null.
    - `msoa` (string, required) — 2021 Census MSOA code (mid-size statistical area, typically 5,000-7,000 residents). Now points to 2021 data. May be null.
    - `ced` (string, required) — The county electoral division for English postcodes. Will be null for postcodes without a grid reference or in other UK regions. May be null.
    - `ccg` (string, required) — NHS Clinical Commissioning Group responsible for planning healthcare services in England. May be null.
    - `pfa` (string, required) — The police force area for this postcode. May be null.
    - `date_of_introduction` (string, required) — The date the postcode was introduced in YYYYMM format. May be null.
    - `date_of_termination` (string, required) — The date the postcode was terminated in YYYYMM format. Null for live postcodes. May be null.
    - `index_of_multiple_deprivation` (integer (int32), required) — ONS Index of Multiple Deprivation (IMD) rank for this postcode's LSOA. Lower ranks correspond to more deprived areas. England, Wales, Scotland and Northern Ireland use independent IMD scales — values are not directly comparable across countries. May be null.
    - `parliamentary_constituency_2024` (string, required) — The UK Parliamentary constituency for this postcode based on July 2024 boundaries. May be null.
    - `senedd_constituency` (string, required) — The Senedd Cymru (Welsh Parliament) constituency for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `senedd_constituency_no` (integer (int32), required) — The Senedd Cymru (Welsh Parliament) constituency number for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `nhs_region` (string, required) — The NHS England Region for this postcode. Only applicable to English postcodes. May be null.
    - `ttwa` (string, required) — The Travel to Work Area for this postcode. TTWAs are areas where most people both live and work. May be null.
    - `national_park` (string, required) — The National Park this postcode falls within, if any. May be null.
    - `bua` (string, required) — The Built-up Area (2022) for this postcode. Built-up areas are land which has been 'irreversibly urbanised'. May be null.
    - `icb` (string, required) — The NHS Integrated Care Board responsible for healthcare planning in this area. May be null.
    - `cancer_alliance` (string, required) — The Cancer Alliance for this postcode. Cancer Alliances bring together NHS providers and commissioners to improve cancer care. May be null.
    - `lsoa11` (string, required) — 2011 Census LSOA code. Alias for the 'lsoa' field. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa11` (string, required) — 2011 Census MSOA code. Alias for the 'msoa' field. In Scotland this is the Intermediate Zone. May be null.
    - `lsoa21` (string, required) — 2021 Census LSOA code. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa21` (string, required) — 2021 Census MSOA code. In Scotland this is the Intermediate Zone. May be null.
    - `oa21` (string, required) — 2021 Census Output Area code - the smallest census geography. May be null.
    - `ruc11` (string, required) — The 2011 Census Rural-Urban Classification for this postcode. May be null.
    - `ruc21` (string, required) — The 2021 Census Rural-Urban Classification for this postcode. May be null.
    - `lep1` (string, required) — The primary Local Enterprise Partnership for this postcode. LEPs are partnerships between local authorities and businesses. May be null.
    - `lep2` (string, required) — The secondary Local Enterprise Partnership for this postcode, if it falls within overlapping LEP areas. May be null.
    - `nuts` (string, required) — Statistical geography code for international comparisons (formerly NUTS - Nomenclature of Units for Territorial Statistics). As of January 2021, following Brexit, NUTS was replaced by ITL (International Territorial Levels) in the UK. For backward compatibility, Postcodes.io continues to provide this data under the "nuts" field name. May be null.
    - `codes` (object, required) — Contains the GSS (Government Statistical Service) codes for administrative areas. Note: Returns 'Pseudo codes' (e.g., L99999999 for Channel Islands, M99999999 for Isle of Man, N99999999 for Northern Ireland, S99999999 for Scotland) for areas where a statutory geography does not exist. Client logic should handle these codes as 'Not Applicable' rather than treating them as valid IDs.
      - `admin_district` (string, required) — Official 9-character GSS code for this administrative district. May be null.
      - `admin_county` (string, required) — Official 9-character GSS code for this administrative county. May be null.
      - `admin_ward` (string, required) — Official 9-character GSS code for this administrative ward. May be null.
      - `parish` (string, required) — Official 9-character GSS code for this parish. May be null.
      - `ccg` (string, required) — Official 9-character GSS code for this Clinical Commissioning Group. May be null.
      - `ccg_id` (string, required) — Short code identifier for this Clinical Commissioning Group. May be null.
      - `ced` (string, required) — Official 9-character GSS code for this County Electoral District. May be null.
      - `nuts` (string, required) — Official code for this International Territorial Level area. May be null.
      - `lau2` (string, required) — Local Administrative Unit level 2 code for this area. May be null.
      - `lsoa` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `pfa` (string, required) — Official 9-character GSS code for this Police Force Area. May be null.
      - `parliamentary_constituency` (string, required) — Official 9-character GSS code for this Parliamentary Constituency (July 2024 boundaries). Alias for codes.parliamentary_constituency_2024. May be null.
      - `parliamentary_constituency_2024` (string, required) — Official 9-character GSS code for this Parliamentary Constituency based on July 2024 boundaries. May be null.
      - `nhs_region` (string, required) — Official 9-character GSS code for this NHS England Region. May be null.
      - `ttwa` (string, required) — Travel to Work Area code. May be null.
      - `national_park` (string, required) — Official 9-character GSS code for this National Park. May be null.
      - `bua` (string, required) — Built-up Area (2022) code. May be null.
      - `icb` (string, required) — Official 9-character GSS code for this Integrated Care Board. May be null.
      - `cancer_alliance` (string, required) — Official 9-character GSS code for this Cancer Alliance. May be null.
      - `lsoa11` (string, required) — Official 9-character GSS code for this 2011 Census LSOA. Alias for codes.lsoa. May be null.
      - `msoa11` (string, required) — Official 9-character GSS code for this 2011 Census MSOA. Alias for codes.msoa. May be null.
      - `lsoa21` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa21` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `oa21` (string, required) — 2021 Census Output Area code. May be null.
      - `ruc11` (string, required) — 2011 Census Rural-Urban Classification code. May be null.
      - `ruc21` (string, required) — 2021 Census Rural-Urban Classification code. May be null.
      - `lep1` (string, required) — Official 9-character GSS code for the primary Local Enterprise Partnership. May be null.
      - `lep2` (string, required) — Official 9-character GSS code for the secondary Local Enterprise Partnership. May be null.

### GET /postcodes

**Autocomplete Search a Postcode**

Query for a postcode either by:

- The postcode itself (with `query=`) or by,
- A geolocation (`lat=` and `lon=`).

## Query with Postcode

Submit a postcode query and receive a complete list of postcode matches and all associated postcode data. This is triggered when `query=` is supplied.

This is essentially a postcode search which prefix matches and returns postcodes in sorted order (case insensitive).

This method is space sensitive, i.e. it detects for spaces between outward and inward parts of the postcode (some examples detailed in this [issue](https://github.com/ideal-postcodes/postcodes.io/issues/44)).

The result set can either be empty or populated with up to 100 postcode entities. Either way it will always return a 200 response code.

## Query with Geolocation

Returns nearest postcodes for a given longitude and latitude. This is triggered when `lat=` and `lon=` are supplied.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `query` | query | any | No |  |
| `limit` | query | any | No | Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100. Default: `10`. Minimum: 1. Maximum: 100. |
| `longitude` | query | number (double) | No | Geographic coordinate that specifies the east-west position of a point. Minimum: -180. Maximum: 180. |
| `latitude` | query | number (double) | No | Minimum: -90. Maximum: 90. |
| `radius` | query | integer | No | Limits number of postcodes matches to return. Defaults to 100m. Needs to be less than 2,000m. Default: `100`. Minimum: 1. Maximum: 2000. |
| `widesearch` | query | boolean | No | Default: `false`. |
| `filter` | query | string | No |  |

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (array of one of several types, required) — Array containing detailed location information for the requested postcode or nearest postcodes
    - `postcode` (string, required) — UK postcode format: 2-4 character outward code, a space, and a 3-character inward code (e.g., SW1A 2AA). Updated monthly from Royal Mail.
    - `outcode` (string, required) — The first part of a postcode before the space (2-4 characters). This generally identifies the postal town or district.
    - `incode` (string, required) — The second part of a postcode after the space (always 3 characters). Helps identify specific streets or buildings within a postal area.
    - `quality` (integer, required) — Positional Quality Indicator (1-9). Shows the status of the assigned grid reference: * 1: Within the building of the matched address closest to the postcode mean * 2: As for 1, except by visual inspection of Landline maps (Scotland only) * 3: Approximate to within 50 metres * 4: Postcode unit mean (averaged from addresses with same postcode) * 5: Estimated by ONS using surrounding postcodes * 6: Postcode sector mean (mainly PO Boxes) * 8: Terminated postcode (last known ONS grid reference) * 9: No coordinates available
    - `eastings` (integer (int32), required) — The OS grid reference easting (X-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `northings` (integer (int32), required) — The OS grid reference northing (Y-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `country` (string, required) — The UK constituent country for this postcode (England, Scotland, Wales, Northern Ireland, Channel Islands, or Isle of Man).
    - `nhs_ha` (string, required) — The NHS health authority area for this postcode. May be null.
    - `admin_county` (string, required) — The administrative county for this postcode. Null where the postcode falls outside a county-level authority (the underlying GSS code is then a pseudo such as `E99999999`, surfaced under `codes.admin_county`). May be null.
    - `admin_district` (string, required) — The administrative district or unitary authority for this postcode. May be null.
    - `admin_ward` (string, required) — The electoral/administrative ward for this postcode. May be null.
    - `longitude` (number (double), required) — WGS84 longitude coordinate (east-west position). May be null if geolocation unavailable. May be null.
    - `latitude` (number (double), required) — WGS84 latitude coordinate (north-south position). May be null if geolocation unavailable. May be null.
    - `parliamentary_constituency` (string, required) — The UK Parliamentary constituency for this postcode. May be null.
    - `european_electoral_region` (string, required) — The European Electoral Region for this postcode. May be null.
    - `primary_care_trust` (string, required) — The healthcare administrative area for this postcode. Different naming conventions apply across UK regions. May be null.
    - `region` (string, required) — The regional designation for this postcode (formerly Government Office Regions or GORs). May be null.
    - `parish` (string, required) — The civil parish (England) or community (Wales) for this postcode. May be null.
    - `lsoa` (string, required) — 2021 Census LSOA code (smaller statistical area, typically 1,000-1,500 residents). Now points to 2021 data. May be null.
    - `msoa` (string, required) — 2021 Census MSOA code (mid-size statistical area, typically 5,000-7,000 residents). Now points to 2021 data. May be null.
    - `ced` (string, required) — The county electoral division for English postcodes. Will be null for postcodes without a grid reference or in other UK regions. May be null.
    - `ccg` (string, required) — NHS Clinical Commissioning Group responsible for planning healthcare services in England. May be null.
    - `pfa` (string, required) — The police force area for this postcode. May be null.
    - `date_of_introduction` (string, required) — The date the postcode was introduced in YYYYMM format. May be null.
    - `date_of_termination` (string, required) — The date the postcode was terminated in YYYYMM format. Null for live postcodes. May be null.
    - `index_of_multiple_deprivation` (integer (int32), required) — ONS Index of Multiple Deprivation (IMD) rank for this postcode's LSOA. Lower ranks correspond to more deprived areas. England, Wales, Scotland and Northern Ireland use independent IMD scales — values are not directly comparable across countries. May be null.
    - `parliamentary_constituency_2024` (string, required) — The UK Parliamentary constituency for this postcode based on July 2024 boundaries. May be null.
    - `senedd_constituency` (string, required) — The Senedd Cymru (Welsh Parliament) constituency for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `senedd_constituency_no` (integer (int32), required) — The Senedd Cymru (Welsh Parliament) constituency number for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `nhs_region` (string, required) — The NHS England Region for this postcode. Only applicable to English postcodes. May be null.
    - `ttwa` (string, required) — The Travel to Work Area for this postcode. TTWAs are areas where most people both live and work. May be null.
    - `national_park` (string, required) — The National Park this postcode falls within, if any. May be null.
    - `bua` (string, required) — The Built-up Area (2022) for this postcode. Built-up areas are land which has been 'irreversibly urbanised'. May be null.
    - `icb` (string, required) — The NHS Integrated Care Board responsible for healthcare planning in this area. May be null.
    - `cancer_alliance` (string, required) — The Cancer Alliance for this postcode. Cancer Alliances bring together NHS providers and commissioners to improve cancer care. May be null.
    - `lsoa11` (string, required) — 2011 Census LSOA code. Alias for the 'lsoa' field. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa11` (string, required) — 2011 Census MSOA code. Alias for the 'msoa' field. In Scotland this is the Intermediate Zone. May be null.
    - `lsoa21` (string, required) — 2021 Census LSOA code. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa21` (string, required) — 2021 Census MSOA code. In Scotland this is the Intermediate Zone. May be null.
    - `oa21` (string, required) — 2021 Census Output Area code - the smallest census geography. May be null.
    - `ruc11` (string, required) — The 2011 Census Rural-Urban Classification for this postcode. May be null.
    - `ruc21` (string, required) — The 2021 Census Rural-Urban Classification for this postcode. May be null.
    - `lep1` (string, required) — The primary Local Enterprise Partnership for this postcode. LEPs are partnerships between local authorities and businesses. May be null.
    - `lep2` (string, required) — The secondary Local Enterprise Partnership for this postcode, if it falls within overlapping LEP areas. May be null.
    - `nuts` (string, required) — Statistical geography code for international comparisons (formerly NUTS - Nomenclature of Units for Territorial Statistics). As of January 2021, following Brexit, NUTS was replaced by ITL (International Territorial Levels) in the UK. For backward compatibility, Postcodes.io continues to provide this data under the "nuts" field name. May be null.
    - `codes` (object, required) — Contains the GSS (Government Statistical Service) codes for administrative areas. Note: Returns 'Pseudo codes' (e.g., L99999999 for Channel Islands, M99999999 for Isle of Man, N99999999 for Northern Ireland, S99999999 for Scotland) for areas where a statutory geography does not exist. Client logic should handle these codes as 'Not Applicable' rather than treating them as valid IDs.
      - `admin_district` (string, required) — Official 9-character GSS code for this administrative district. May be null.
      - `admin_county` (string, required) — Official 9-character GSS code for this administrative county. May be null.
      - `admin_ward` (string, required) — Official 9-character GSS code for this administrative ward. May be null.
      - `parish` (string, required) — Official 9-character GSS code for this parish. May be null.
      - `ccg` (string, required) — Official 9-character GSS code for this Clinical Commissioning Group. May be null.
      - `ccg_id` (string, required) — Short code identifier for this Clinical Commissioning Group. May be null.
      - `ced` (string, required) — Official 9-character GSS code for this County Electoral District. May be null.
      - `nuts` (string, required) — Official code for this International Territorial Level area. May be null.
      - `lau2` (string, required) — Local Administrative Unit level 2 code for this area. May be null.
      - `lsoa` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `pfa` (string, required) — Official 9-character GSS code for this Police Force Area. May be null.
      - `parliamentary_constituency` (string, required) — Official 9-character GSS code for this Parliamentary Constituency (July 2024 boundaries). Alias for codes.parliamentary_constituency_2024. May be null.
      - `parliamentary_constituency_2024` (string, required) — Official 9-character GSS code for this Parliamentary Constituency based on July 2024 boundaries. May be null.
      - `nhs_region` (string, required) — Official 9-character GSS code for this NHS England Region. May be null.
      - `ttwa` (string, required) — Travel to Work Area code. May be null.
      - `national_park` (string, required) — Official 9-character GSS code for this National Park. May be null.
      - `bua` (string, required) — Built-up Area (2022) code. May be null.
      - `icb` (string, required) — Official 9-character GSS code for this Integrated Care Board. May be null.
      - `cancer_alliance` (string, required) — Official 9-character GSS code for this Cancer Alliance. May be null.
      - `lsoa11` (string, required) — Official 9-character GSS code for this 2011 Census LSOA. Alias for codes.lsoa. May be null.
      - `msoa11` (string, required) — Official 9-character GSS code for this 2011 Census MSOA. Alias for codes.msoa. May be null.
      - `lsoa21` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa21` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `oa21` (string, required) — 2021 Census Output Area code. May be null.
      - `ruc11` (string, required) — 2011 Census Rural-Urban Classification code. May be null.
      - `ruc21` (string, required) — 2021 Census Rural-Urban Classification code. May be null.
      - `lep1` (string, required) — Official 9-character GSS code for the primary Local Enterprise Partnership. May be null.
      - `lep2` (string, required) — Official 9-character GSS code for the secondary Local Enterprise Partnership. May be null.

### GET /postcodes/{postcode}/nearest

**Find the Nearest Postcodes**

Returns a list of postcodes geographically nearest to the specified postcode, ordered by proximity (closest first).

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `postcode` | path | any | Yes | Valid UK postcode to use as the geographic center point for the proximity search |

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (array of one of several types, required) — Array of nearest postcodes sorted by distance
    - `postcode` (string, required) — UK postcode format: 2-4 character outward code, a space, and a 3-character inward code (e.g., SW1A 2AA). Updated monthly from Royal Mail.
    - `outcode` (string, required) — The first part of a postcode before the space (2-4 characters). This generally identifies the postal town or district.
    - `incode` (string, required) — The second part of a postcode after the space (always 3 characters). Helps identify specific streets or buildings within a postal area.
    - `quality` (integer, required) — Positional Quality Indicator (1-9). Shows the status of the assigned grid reference: * 1: Within the building of the matched address closest to the postcode mean * 2: As for 1, except by visual inspection of Landline maps (Scotland only) * 3: Approximate to within 50 metres * 4: Postcode unit mean (averaged from addresses with same postcode) * 5: Estimated by ONS using surrounding postcodes * 6: Postcode sector mean (mainly PO Boxes) * 8: Terminated postcode (last known ONS grid reference) * 9: No coordinates available
    - `eastings` (integer (int32), required) — The OS grid reference easting (X-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `northings` (integer (int32), required) — The OS grid reference northing (Y-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `country` (string, required) — The UK constituent country for this postcode (England, Scotland, Wales, Northern Ireland, Channel Islands, or Isle of Man).
    - `nhs_ha` (string, required) — The NHS health authority area for this postcode. May be null.
    - `admin_county` (string, required) — The administrative county for this postcode. Null where the postcode falls outside a county-level authority (the underlying GSS code is then a pseudo such as `E99999999`, surfaced under `codes.admin_county`). May be null.
    - `admin_district` (string, required) — The administrative district or unitary authority for this postcode. May be null.
    - `admin_ward` (string, required) — The electoral/administrative ward for this postcode. May be null.
    - `longitude` (number (double), required) — WGS84 longitude coordinate (east-west position). May be null if geolocation unavailable. May be null.
    - `latitude` (number (double), required) — WGS84 latitude coordinate (north-south position). May be null if geolocation unavailable. May be null.
    - `parliamentary_constituency` (string, required) — The UK Parliamentary constituency for this postcode. May be null.
    - `european_electoral_region` (string, required) — The European Electoral Region for this postcode. May be null.
    - `primary_care_trust` (string, required) — The healthcare administrative area for this postcode. Different naming conventions apply across UK regions. May be null.
    - `region` (string, required) — The regional designation for this postcode (formerly Government Office Regions or GORs). May be null.
    - `parish` (string, required) — The civil parish (England) or community (Wales) for this postcode. May be null.
    - `lsoa` (string, required) — 2021 Census LSOA code (smaller statistical area, typically 1,000-1,500 residents). Now points to 2021 data. May be null.
    - `msoa` (string, required) — 2021 Census MSOA code (mid-size statistical area, typically 5,000-7,000 residents). Now points to 2021 data. May be null.
    - `ced` (string, required) — The county electoral division for English postcodes. Will be null for postcodes without a grid reference or in other UK regions. May be null.
    - `ccg` (string, required) — NHS Clinical Commissioning Group responsible for planning healthcare services in England. May be null.
    - `pfa` (string, required) — The police force area for this postcode. May be null.
    - `date_of_introduction` (string, required) — The date the postcode was introduced in YYYYMM format. May be null.
    - `date_of_termination` (string, required) — The date the postcode was terminated in YYYYMM format. Null for live postcodes. May be null.
    - `index_of_multiple_deprivation` (integer (int32), required) — ONS Index of Multiple Deprivation (IMD) rank for this postcode's LSOA. Lower ranks correspond to more deprived areas. England, Wales, Scotland and Northern Ireland use independent IMD scales — values are not directly comparable across countries. May be null.
    - `parliamentary_constituency_2024` (string, required) — The UK Parliamentary constituency for this postcode based on July 2024 boundaries. May be null.
    - `senedd_constituency` (string, required) — The Senedd Cymru (Welsh Parliament) constituency for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `senedd_constituency_no` (integer (int32), required) — The Senedd Cymru (Welsh Parliament) constituency number for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `nhs_region` (string, required) — The NHS England Region for this postcode. Only applicable to English postcodes. May be null.
    - `ttwa` (string, required) — The Travel to Work Area for this postcode. TTWAs are areas where most people both live and work. May be null.
    - `national_park` (string, required) — The National Park this postcode falls within, if any. May be null.
    - `bua` (string, required) — The Built-up Area (2022) for this postcode. Built-up areas are land which has been 'irreversibly urbanised'. May be null.
    - `icb` (string, required) — The NHS Integrated Care Board responsible for healthcare planning in this area. May be null.
    - `cancer_alliance` (string, required) — The Cancer Alliance for this postcode. Cancer Alliances bring together NHS providers and commissioners to improve cancer care. May be null.
    - `lsoa11` (string, required) — 2011 Census LSOA code. Alias for the 'lsoa' field. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa11` (string, required) — 2011 Census MSOA code. Alias for the 'msoa' field. In Scotland this is the Intermediate Zone. May be null.
    - `lsoa21` (string, required) — 2021 Census LSOA code. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa21` (string, required) — 2021 Census MSOA code. In Scotland this is the Intermediate Zone. May be null.
    - `oa21` (string, required) — 2021 Census Output Area code - the smallest census geography. May be null.
    - `ruc11` (string, required) — The 2011 Census Rural-Urban Classification for this postcode. May be null.
    - `ruc21` (string, required) — The 2021 Census Rural-Urban Classification for this postcode. May be null.
    - `lep1` (string, required) — The primary Local Enterprise Partnership for this postcode. LEPs are partnerships between local authorities and businesses. May be null.
    - `lep2` (string, required) — The secondary Local Enterprise Partnership for this postcode, if it falls within overlapping LEP areas. May be null.
    - `nuts` (string, required) — Statistical geography code for international comparisons (formerly NUTS - Nomenclature of Units for Territorial Statistics). As of January 2021, following Brexit, NUTS was replaced by ITL (International Territorial Levels) in the UK. For backward compatibility, Postcodes.io continues to provide this data under the "nuts" field name. May be null.
    - `codes` (object, required) — Contains the GSS (Government Statistical Service) codes for administrative areas. Note: Returns 'Pseudo codes' (e.g., L99999999 for Channel Islands, M99999999 for Isle of Man, N99999999 for Northern Ireland, S99999999 for Scotland) for areas where a statutory geography does not exist. Client logic should handle these codes as 'Not Applicable' rather than treating them as valid IDs.
      - `admin_district` (string, required) — Official 9-character GSS code for this administrative district. May be null.
      - `admin_county` (string, required) — Official 9-character GSS code for this administrative county. May be null.
      - `admin_ward` (string, required) — Official 9-character GSS code for this administrative ward. May be null.
      - `parish` (string, required) — Official 9-character GSS code for this parish. May be null.
      - `ccg` (string, required) — Official 9-character GSS code for this Clinical Commissioning Group. May be null.
      - `ccg_id` (string, required) — Short code identifier for this Clinical Commissioning Group. May be null.
      - `ced` (string, required) — Official 9-character GSS code for this County Electoral District. May be null.
      - `nuts` (string, required) — Official code for this International Territorial Level area. May be null.
      - `lau2` (string, required) — Local Administrative Unit level 2 code for this area. May be null.
      - `lsoa` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `pfa` (string, required) — Official 9-character GSS code for this Police Force Area. May be null.
      - `parliamentary_constituency` (string, required) — Official 9-character GSS code for this Parliamentary Constituency (July 2024 boundaries). Alias for codes.parliamentary_constituency_2024. May be null.
      - `parliamentary_constituency_2024` (string, required) — Official 9-character GSS code for this Parliamentary Constituency based on July 2024 boundaries. May be null.
      - `nhs_region` (string, required) — Official 9-character GSS code for this NHS England Region. May be null.
      - `ttwa` (string, required) — Travel to Work Area code. May be null.
      - `national_park` (string, required) — Official 9-character GSS code for this National Park. May be null.
      - `bua` (string, required) — Built-up Area (2022) code. May be null.
      - `icb` (string, required) — Official 9-character GSS code for this Integrated Care Board. May be null.
      - `cancer_alliance` (string, required) — Official 9-character GSS code for this Cancer Alliance. May be null.
      - `lsoa11` (string, required) — Official 9-character GSS code for this 2011 Census LSOA. Alias for codes.lsoa. May be null.
      - `msoa11` (string, required) — Official 9-character GSS code for this 2011 Census MSOA. Alias for codes.msoa. May be null.
      - `lsoa21` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa21` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `oa21` (string, required) — 2021 Census Output Area code. May be null.
      - `ruc11` (string, required) — 2011 Census Rural-Urban Classification code. May be null.
      - `ruc21` (string, required) — 2021 Census Rural-Urban Classification code. May be null.
      - `lep1` (string, required) — Official 9-character GSS code for the primary Local Enterprise Partnership. May be null.
      - `lep2` (string, required) — Official 9-character GSS code for the secondary Local Enterprise Partnership. May be null.
    - `distance` (number (double), required) — Distance in metres from specified postcode

### GET /random/postcodes

**Get a Random Postcode**

Returns a randomly selected postcode along with comprehensive geographic, administrative, and statistical data associated with that postcode.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `outcode` | query | string | No | Filters random postcodes by outcode. Returns null if invalid outcode. |

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (object, required) — Comprehensive location data including geographic coordinates, administrative boundaries, and electoral information for the requested postcode
    - `postcode` (string, required) — UK postcode format: 2-4 character outward code, a space, and a 3-character inward code (e.g., SW1A 2AA). Updated monthly from Royal Mail.
    - `outcode` (string, required) — The first part of a postcode before the space (2-4 characters). This generally identifies the postal town or district.
    - `incode` (string, required) — The second part of a postcode after the space (always 3 characters). Helps identify specific streets or buildings within a postal area.
    - `quality` (integer, required) — Positional Quality Indicator (1-9). Shows the status of the assigned grid reference: * 1: Within the building of the matched address closest to the postcode mean * 2: As for 1, except by visual inspection of Landline maps (Scotland only) * 3: Approximate to within 50 metres * 4: Postcode unit mean (averaged from addresses with same postcode) * 5: Estimated by ONS using surrounding postcodes * 6: Postcode sector mean (mainly PO Boxes) * 8: Terminated postcode (last known ONS grid reference) * 9: No coordinates available
    - `eastings` (integer (int32), required) — The OS grid reference easting (X-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `northings` (integer (int32), required) — The OS grid reference northing (Y-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `country` (string, required) — The UK constituent country for this postcode (England, Scotland, Wales, Northern Ireland, Channel Islands, or Isle of Man).
    - `nhs_ha` (string, required) — The NHS health authority area for this postcode. May be null.
    - `admin_county` (string, required) — The administrative county for this postcode. Null where the postcode falls outside a county-level authority (the underlying GSS code is then a pseudo such as `E99999999`, surfaced under `codes.admin_county`). May be null.
    - `admin_district` (string, required) — The administrative district or unitary authority for this postcode. May be null.
    - `admin_ward` (string, required) — The electoral/administrative ward for this postcode. May be null.
    - `longitude` (number (double), required) — WGS84 longitude coordinate (east-west position). May be null if geolocation unavailable. May be null.
    - `latitude` (number (double), required) — WGS84 latitude coordinate (north-south position). May be null if geolocation unavailable. May be null.
    - `parliamentary_constituency` (string, required) — The UK Parliamentary constituency for this postcode. May be null.
    - `european_electoral_region` (string, required) — The European Electoral Region for this postcode. May be null.
    - `primary_care_trust` (string, required) — The healthcare administrative area for this postcode. Different naming conventions apply across UK regions. May be null.
    - `region` (string, required) — The regional designation for this postcode (formerly Government Office Regions or GORs). May be null.
    - `parish` (string, required) — The civil parish (England) or community (Wales) for this postcode. May be null.
    - `lsoa` (string, required) — 2021 Census LSOA code (smaller statistical area, typically 1,000-1,500 residents). Now points to 2021 data. May be null.
    - `msoa` (string, required) — 2021 Census MSOA code (mid-size statistical area, typically 5,000-7,000 residents). Now points to 2021 data. May be null.
    - `ced` (string, required) — The county electoral division for English postcodes. Will be null for postcodes without a grid reference or in other UK regions. May be null.
    - `ccg` (string, required) — NHS Clinical Commissioning Group responsible for planning healthcare services in England. May be null.
    - `pfa` (string, required) — The police force area for this postcode. May be null.
    - `date_of_introduction` (string, required) — The date the postcode was introduced in YYYYMM format. May be null.
    - `date_of_termination` (string, required) — The date the postcode was terminated in YYYYMM format. Null for live postcodes. May be null.
    - `index_of_multiple_deprivation` (integer (int32), required) — ONS Index of Multiple Deprivation (IMD) rank for this postcode's LSOA. Lower ranks correspond to more deprived areas. England, Wales, Scotland and Northern Ireland use independent IMD scales — values are not directly comparable across countries. May be null.
    - `parliamentary_constituency_2024` (string, required) — The UK Parliamentary constituency for this postcode based on July 2024 boundaries. May be null.
    - `senedd_constituency` (string, required) — The Senedd Cymru (Welsh Parliament) constituency for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `senedd_constituency_no` (integer (int32), required) — The Senedd Cymru (Welsh Parliament) constituency number for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `nhs_region` (string, required) — The NHS England Region for this postcode. Only applicable to English postcodes. May be null.
    - `ttwa` (string, required) — The Travel to Work Area for this postcode. TTWAs are areas where most people both live and work. May be null.
    - `national_park` (string, required) — The National Park this postcode falls within, if any. May be null.
    - `bua` (string, required) — The Built-up Area (2022) for this postcode. Built-up areas are land which has been 'irreversibly urbanised'. May be null.
    - `icb` (string, required) — The NHS Integrated Care Board responsible for healthcare planning in this area. May be null.
    - `cancer_alliance` (string, required) — The Cancer Alliance for this postcode. Cancer Alliances bring together NHS providers and commissioners to improve cancer care. May be null.
    - `lsoa11` (string, required) — 2011 Census LSOA code. Alias for the 'lsoa' field. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa11` (string, required) — 2011 Census MSOA code. Alias for the 'msoa' field. In Scotland this is the Intermediate Zone. May be null.
    - `lsoa21` (string, required) — 2021 Census LSOA code. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa21` (string, required) — 2021 Census MSOA code. In Scotland this is the Intermediate Zone. May be null.
    - `oa21` (string, required) — 2021 Census Output Area code - the smallest census geography. May be null.
    - `ruc11` (string, required) — The 2011 Census Rural-Urban Classification for this postcode. May be null.
    - `ruc21` (string, required) — The 2021 Census Rural-Urban Classification for this postcode. May be null.
    - `lep1` (string, required) — The primary Local Enterprise Partnership for this postcode. LEPs are partnerships between local authorities and businesses. May be null.
    - `lep2` (string, required) — The secondary Local Enterprise Partnership for this postcode, if it falls within overlapping LEP areas. May be null.
    - `nuts` (string, required) — Statistical geography code for international comparisons (formerly NUTS - Nomenclature of Units for Territorial Statistics). As of January 2021, following Brexit, NUTS was replaced by ITL (International Territorial Levels) in the UK. For backward compatibility, Postcodes.io continues to provide this data under the "nuts" field name. May be null.
    - `codes` (object, required) — Contains the GSS (Government Statistical Service) codes for administrative areas. Note: Returns 'Pseudo codes' (e.g., L99999999 for Channel Islands, M99999999 for Isle of Man, N99999999 for Northern Ireland, S99999999 for Scotland) for areas where a statutory geography does not exist. Client logic should handle these codes as 'Not Applicable' rather than treating them as valid IDs.
      - `admin_district` (string, required) — Official 9-character GSS code for this administrative district. May be null.
      - `admin_county` (string, required) — Official 9-character GSS code for this administrative county. May be null.
      - `admin_ward` (string, required) — Official 9-character GSS code for this administrative ward. May be null.
      - `parish` (string, required) — Official 9-character GSS code for this parish. May be null.
      - `ccg` (string, required) — Official 9-character GSS code for this Clinical Commissioning Group. May be null.
      - `ccg_id` (string, required) — Short code identifier for this Clinical Commissioning Group. May be null.
      - `ced` (string, required) — Official 9-character GSS code for this County Electoral District. May be null.
      - `nuts` (string, required) — Official code for this International Territorial Level area. May be null.
      - `lau2` (string, required) — Local Administrative Unit level 2 code for this area. May be null.
      - `lsoa` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `pfa` (string, required) — Official 9-character GSS code for this Police Force Area. May be null.
      - `parliamentary_constituency` (string, required) — Official 9-character GSS code for this Parliamentary Constituency (July 2024 boundaries). Alias for codes.parliamentary_constituency_2024. May be null.
      - `parliamentary_constituency_2024` (string, required) — Official 9-character GSS code for this Parliamentary Constituency based on July 2024 boundaries. May be null.
      - `nhs_region` (string, required) — Official 9-character GSS code for this NHS England Region. May be null.
      - `ttwa` (string, required) — Travel to Work Area code. May be null.
      - `national_park` (string, required) — Official 9-character GSS code for this National Park. May be null.
      - `bua` (string, required) — Built-up Area (2022) code. May be null.
      - `icb` (string, required) — Official 9-character GSS code for this Integrated Care Board. May be null.
      - `cancer_alliance` (string, required) — Official 9-character GSS code for this Cancer Alliance. May be null.
      - `lsoa11` (string, required) — Official 9-character GSS code for this 2011 Census LSOA. Alias for codes.lsoa. May be null.
      - `msoa11` (string, required) — Official 9-character GSS code for this 2011 Census MSOA. Alias for codes.msoa. May be null.
      - `lsoa21` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa21` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `oa21` (string, required) — 2021 Census Output Area code. May be null.
      - `ruc11` (string, required) — 2011 Census Rural-Urban Classification code. May be null.
      - `ruc21` (string, required) — 2021 Census Rural-Urban Classification code. May be null.
      - `lep1` (string, required) — Official 9-character GSS code for the primary Local Enterprise Partnership. May be null.
      - `lep2` (string, required) — Official 9-character GSS code for the secondary Local Enterprise Partnership. May be null.

## Postcode Query

### POST /postcodes

**Bulk Postcode Lookup**

Accepts a JSON object containing an array of postcodes. Returns a list of matching postcodes and respective available data.

Be sure to submit JSON requests setting `Content-Type` to `application/json`.

Accepts up to 100 postcodes.

### Post Data

This method requires a JSON object containing an array of postcodes to be posted, e.g.

```json
{
  "postcodes": ["PR3 0SG", "M45 6GN", "EX16 5BL"]
}
```

## Bulk Reverse Geocoding

Bulk translates geolocations into Postcodes. Accepts up to 100 geolocations.

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (object, required) — Comprehensive location data including geographic coordinates, administrative boundaries, and electoral information for the requested postcode
    - `postcode` (string, required) — UK postcode format: 2-4 character outward code, a space, and a 3-character inward code (e.g., SW1A 2AA). Updated monthly from Royal Mail.
    - `outcode` (string, required) — The first part of a postcode before the space (2-4 characters). This generally identifies the postal town or district.
    - `incode` (string, required) — The second part of a postcode after the space (always 3 characters). Helps identify specific streets or buildings within a postal area.
    - `quality` (integer, required) — Positional Quality Indicator (1-9). Shows the status of the assigned grid reference: * 1: Within the building of the matched address closest to the postcode mean * 2: As for 1, except by visual inspection of Landline maps (Scotland only) * 3: Approximate to within 50 metres * 4: Postcode unit mean (averaged from addresses with same postcode) * 5: Estimated by ONS using surrounding postcodes * 6: Postcode sector mean (mainly PO Boxes) * 8: Terminated postcode (last known ONS grid reference) * 9: No coordinates available
    - `eastings` (integer (int32), required) — The OS grid reference easting (X-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `northings` (integer (int32), required) — The OS grid reference northing (Y-coordinate) to 1 metre resolution. Relates to the British National Grid for GB and the Irish National Grid for Northern Ireland. Will be null for Channel Islands and Isle of Man. May be null.
    - `country` (string, required) — The UK constituent country for this postcode (England, Scotland, Wales, Northern Ireland, Channel Islands, or Isle of Man).
    - `nhs_ha` (string, required) — The NHS health authority area for this postcode. May be null.
    - `admin_county` (string, required) — The administrative county for this postcode. Null where the postcode falls outside a county-level authority (the underlying GSS code is then a pseudo such as `E99999999`, surfaced under `codes.admin_county`). May be null.
    - `admin_district` (string, required) — The administrative district or unitary authority for this postcode. May be null.
    - `admin_ward` (string, required) — The electoral/administrative ward for this postcode. May be null.
    - `longitude` (number (double), required) — WGS84 longitude coordinate (east-west position). May be null if geolocation unavailable. May be null.
    - `latitude` (number (double), required) — WGS84 latitude coordinate (north-south position). May be null if geolocation unavailable. May be null.
    - `parliamentary_constituency` (string, required) — The UK Parliamentary constituency for this postcode. May be null.
    - `european_electoral_region` (string, required) — The European Electoral Region for this postcode. May be null.
    - `primary_care_trust` (string, required) — The healthcare administrative area for this postcode. Different naming conventions apply across UK regions. May be null.
    - `region` (string, required) — The regional designation for this postcode (formerly Government Office Regions or GORs). May be null.
    - `parish` (string, required) — The civil parish (England) or community (Wales) for this postcode. May be null.
    - `lsoa` (string, required) — 2021 Census LSOA code (smaller statistical area, typically 1,000-1,500 residents). Now points to 2021 data. May be null.
    - `msoa` (string, required) — 2021 Census MSOA code (mid-size statistical area, typically 5,000-7,000 residents). Now points to 2021 data. May be null.
    - `ced` (string, required) — The county electoral division for English postcodes. Will be null for postcodes without a grid reference or in other UK regions. May be null.
    - `ccg` (string, required) — NHS Clinical Commissioning Group responsible for planning healthcare services in England. May be null.
    - `pfa` (string, required) — The police force area for this postcode. May be null.
    - `date_of_introduction` (string, required) — The date the postcode was introduced in YYYYMM format. May be null.
    - `date_of_termination` (string, required) — The date the postcode was terminated in YYYYMM format. Null for live postcodes. May be null.
    - `index_of_multiple_deprivation` (integer (int32), required) — ONS Index of Multiple Deprivation (IMD) rank for this postcode's LSOA. Lower ranks correspond to more deprived areas. England, Wales, Scotland and Northern Ireland use independent IMD scales — values are not directly comparable across countries. May be null.
    - `parliamentary_constituency_2024` (string, required) — The UK Parliamentary constituency for this postcode based on July 2024 boundaries. May be null.
    - `senedd_constituency` (string, required) — The Senedd Cymru (Welsh Parliament) constituency for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `senedd_constituency_no` (integer (int32), required) — The Senedd Cymru (Welsh Parliament) constituency number for this postcode. Only applicable to Welsh postcodes; null elsewhere. May be null.
    - `nhs_region` (string, required) — The NHS England Region for this postcode. Only applicable to English postcodes. May be null.
    - `ttwa` (string, required) — The Travel to Work Area for this postcode. TTWAs are areas where most people both live and work. May be null.
    - `national_park` (string, required) — The National Park this postcode falls within, if any. May be null.
    - `bua` (string, required) — The Built-up Area (2022) for this postcode. Built-up areas are land which has been 'irreversibly urbanised'. May be null.
    - `icb` (string, required) — The NHS Integrated Care Board responsible for healthcare planning in this area. May be null.
    - `cancer_alliance` (string, required) — The Cancer Alliance for this postcode. Cancer Alliances bring together NHS providers and commissioners to improve cancer care. May be null.
    - `lsoa11` (string, required) — 2011 Census LSOA code. Alias for the 'lsoa' field. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa11` (string, required) — 2011 Census MSOA code. Alias for the 'msoa' field. In Scotland this is the Intermediate Zone. May be null.
    - `lsoa21` (string, required) — 2021 Census LSOA code. In Scotland this is the Data Zone, in Northern Ireland the Small Area. May be null.
    - `msoa21` (string, required) — 2021 Census MSOA code. In Scotland this is the Intermediate Zone. May be null.
    - `oa21` (string, required) — 2021 Census Output Area code - the smallest census geography. May be null.
    - `ruc11` (string, required) — The 2011 Census Rural-Urban Classification for this postcode. May be null.
    - `ruc21` (string, required) — The 2021 Census Rural-Urban Classification for this postcode. May be null.
    - `lep1` (string, required) — The primary Local Enterprise Partnership for this postcode. LEPs are partnerships between local authorities and businesses. May be null.
    - `lep2` (string, required) — The secondary Local Enterprise Partnership for this postcode, if it falls within overlapping LEP areas. May be null.
    - `nuts` (string, required) — Statistical geography code for international comparisons (formerly NUTS - Nomenclature of Units for Territorial Statistics). As of January 2021, following Brexit, NUTS was replaced by ITL (International Territorial Levels) in the UK. For backward compatibility, Postcodes.io continues to provide this data under the "nuts" field name. May be null.
    - `codes` (object, required) — Contains the GSS (Government Statistical Service) codes for administrative areas. Note: Returns 'Pseudo codes' (e.g., L99999999 for Channel Islands, M99999999 for Isle of Man, N99999999 for Northern Ireland, S99999999 for Scotland) for areas where a statutory geography does not exist. Client logic should handle these codes as 'Not Applicable' rather than treating them as valid IDs.
      - `admin_district` (string, required) — Official 9-character GSS code for this administrative district. May be null.
      - `admin_county` (string, required) — Official 9-character GSS code for this administrative county. May be null.
      - `admin_ward` (string, required) — Official 9-character GSS code for this administrative ward. May be null.
      - `parish` (string, required) — Official 9-character GSS code for this parish. May be null.
      - `ccg` (string, required) — Official 9-character GSS code for this Clinical Commissioning Group. May be null.
      - `ccg_id` (string, required) — Short code identifier for this Clinical Commissioning Group. May be null.
      - `ced` (string, required) — Official 9-character GSS code for this County Electoral District. May be null.
      - `nuts` (string, required) — Official code for this International Territorial Level area. May be null.
      - `lau2` (string, required) — Local Administrative Unit level 2 code for this area. May be null.
      - `lsoa` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `pfa` (string, required) — Official 9-character GSS code for this Police Force Area. May be null.
      - `parliamentary_constituency` (string, required) — Official 9-character GSS code for this Parliamentary Constituency (July 2024 boundaries). Alias for codes.parliamentary_constituency_2024. May be null.
      - `parliamentary_constituency_2024` (string, required) — Official 9-character GSS code for this Parliamentary Constituency based on July 2024 boundaries. May be null.
      - `nhs_region` (string, required) — Official 9-character GSS code for this NHS England Region. May be null.
      - `ttwa` (string, required) — Travel to Work Area code. May be null.
      - `national_park` (string, required) — Official 9-character GSS code for this National Park. May be null.
      - `bua` (string, required) — Built-up Area (2022) code. May be null.
      - `icb` (string, required) — Official 9-character GSS code for this Integrated Care Board. May be null.
      - `cancer_alliance` (string, required) — Official 9-character GSS code for this Cancer Alliance. May be null.
      - `lsoa11` (string, required) — Official 9-character GSS code for this 2011 Census LSOA. Alias for codes.lsoa. May be null.
      - `msoa11` (string, required) — Official 9-character GSS code for this 2011 Census MSOA. Alias for codes.msoa. May be null.
      - `lsoa21` (string, required) — Official 9-character GSS code for this 2021 Census LSOA. May be null.
      - `msoa21` (string, required) — Official 9-character GSS code for this 2021 Census MSOA. May be null.
      - `oa21` (string, required) — 2021 Census Output Area code. May be null.
      - `ruc11` (string, required) — 2011 Census Rural-Urban Classification code. May be null.
      - `ruc21` (string, required) — 2021 Census Rural-Urban Classification code. May be null.
      - `lep1` (string, required) — Official 9-character GSS code for the primary Local Enterprise Partnership. May be null.
      - `lep2` (string, required) — Official 9-character GSS code for the secondary Local Enterprise Partnership. May be null.

## Terminated Postcodes

### GET /terminated_postcodes/{postcode}

**Lookup Terminated Postcodes**

Lookup a terminated postcode.

If the terminated postcode exists, this API returns the year and month of termination plus its last known WGS84 coordinates. Channel Islands and Isle of Man postcodes do not carry coordinates — `longitude` and `latitude` will be `null` for those.

Returns `404` if the postcode does not exist in our database of terminated postcodes or is not valid.

Source: ONS Postcode Directory (ONSPD). Live and terminated postcodes share the same underlying table; a postcode is terminated when `date_of_termination` is set.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `postcode` | path | string | Yes | Postcode to query |

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (object, required) — Data for the requested terminated postcode.
    - `postcode` (string, required) — UK postal code format that has been terminated. Follows the standard format of 2-4 character outward code, a space, then 3-character inward code. Pattern: `^[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][A-Z]{2}$`.
    - `year_terminated` (integer (int32), required) — The year when the postcode was terminated (YYYY format). Minimum: 1900.
    - `month_terminated` (integer (int32), required) — Month when the postcode was terminated (1-12, where 1=January, 12=December). Allowed values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`. Minimum: 1. Maximum: 12.
    - `eastings` (integer (int32), required) — OS National Grid easting (1m resolution). Null for postcodes without a grid reference (e.g. Channel Islands, Isle of Man) or that were terminated before a reference was assigned. May be null.
    - `northings` (integer (int32), required) — OS National Grid northing (1m resolution). Null for postcodes without a grid reference (e.g. Channel Islands, Isle of Man) or that were terminated before a reference was assigned. May be null.
    - `longitude` (number (double), required) — WGS84 longitude coordinate of the postcode location. Null if no grid reference is available. Minimum: -180. Maximum: 180. May be null.
    - `latitude` (number (double), required) — WGS84 latitude coordinate of the postcode location. Null if no grid reference is available. Minimum: -90. Maximum: 90. May be null.
- **404** — Postcode not found

## Scottish Postcodes

### GET /scotland/postcodes/{postcode}

**Lookup Scottish Postcode**

Lookup a Scottish postcode.

Returns Scottish Postcode Directory (SPD) data associated with the postcode. The response covers the full SPD field set: council area, electoral ward, Scottish and UK parliamentary geographies, health board, integration authority, data zone, intermediate zone, output area, locality, settlement, civil parish, island, national park, travel-to-work area, ITL/LAU, urban-rural classification, SIMD rank, ROA, census counts, and the corresponding GSS / official codes under the `codes` object.

Top-level fields hold the latest (canonical) value for each datapoint. Year-suffixed fields surface prior versions where the SPD publishes them.

Returns `404` if the postcode does not exist in SPD or is not valid.

For postcodes not in SPD but present in ONSPD (i.e. non-Scottish postcodes), a `404` is returned with the error message "Postcode exists in ONSPD but not in SPD."

Source: Scottish Postcode Directory (National Records of Scotland).

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `postcode` | path | string | Yes | Specifies the postcode you wish to query |

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (object, required) — Scottish Postcode Directory (SPD) data for the requested postcode.
    - `postcode` (string, required) — The Royal Mail postcode (e.g., AB10 1XG). Pattern: `^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$`.
    - `pc_compact` (string) — Postcode with all spaces removed.
    - `outcode` (string) — First part of the postcode (before the space).
    - `incode` (string) — Second part of the postcode (after the space).
    - `postcode_district` (string) — Equivalent to the outward code.
    - `postcode_sector` (string) — Outward code plus the first character of the inward code.
    - `user_type` (string) — SPD user-type indicator ("0" = small user, "1" = large user). May be null.
    - `date_of_introduction` (string) — Date the postcode was introduced (YYYYMM). May be null.
    - `date_of_deletion` (string) — Date the postcode was deleted (YYYYMM). Null for live postcodes. May be null.
    - `linked_small_user_postcode` (string) — For large-user postcodes, the linked small-user postcode (if any). May be null.
    - `longitude` (number (double), required) — WGS84 longitude. May be null.
    - `latitude` (number (double), required) — WGS84 latitude. May be null.
    - `eastings` (integer (int32)) — OS National Grid easting (1m resolution). May be null.
    - `northings` (integer (int32)) — OS National Grid northing (1m resolution). May be null.
    - `split_indicator` (string) — SPD split indicator. Marks postcodes that span more than one administrative unit. May be null.
    - `grid_link_indicator` (string) — How the postcode was linked to its grid reference (1 = match by address, 2 = match by visual inspection, 3 = approximate match, etc.). May be null.
    - `grid_link_positional_accuracy` (string) — Positional accuracy of the grid reference. May be null.
    - `council_area` (string, required) — 2019 council area name. The current single-tier local authority. May be null.
    - `electoral_ward` (string, required) — 2022 electoral ward name. May be null.
    - `registration_district` (string) — 2007 registration district code. (Names are not provided in SPD.). May be null.
    - `enterprise_region` (string) — 2008 enterprise region name. May be null.
    - `strategic_development_planning_area` (string) — 2013 SDPA code. Names are not provided in SPD. May be null.
    - `local_government_district` (string) — 1995 local government district name (the most recent boundary before unitary council areas). May be null.
    - `local_government_district_1991` (string) — 1991 local government district name (historical). May be null.
    - `uk_parliamentary_constituency` (string) — 2024 UK Parliamentary constituency name. May be null.
    - `scottish_parliamentary_region` (string, required) — 2026 Scottish Parliamentary region name (Second Review of Scottish Parliament Boundaries, SSI 2025/285, in effect since the 7 May 2026 Holyrood election). This is the current designation. May be null.
    - `scottish_parliamentary_constituency` (string, required) — 2026 Scottish Parliamentary constituency name (Second Review of Scottish Parliament Boundaries, SSI 2025/285, in effect since the 7 May 2026 Holyrood election). This is the current designation. May be null.
    - `health_board_area` (string, required) — 2019 NHS health board area name. Current operational boundary. May be null.
    - `health_board_area_2006` (string) — 2006 health board area name (historical). May be null.
    - `health_board_area_1995` (string) — 1995 health board area name (historical). May be null.
    - `integration_authority` (string) — 2019 health and social care integration authority name. May be null.
    - `output_area` (string, required) — 2022 census Output Area code. The smallest census geography. May be null.
    - `output_area_2011` (string) — 2011 census Output Area code. May be null.
    - `output_area_2001` (string) — 2001 census Output Area code. May be null.
    - `output_area_1991` (string) — 1991 census Output Area code. May be null.
    - `data_zone` (string, required) — 2022 Data Zone name. Scottish equivalent of LSOA. May be null.
    - `data_zone_2011` (string) — 2011 Data Zone code. May be null.
    - `data_zone_2001` (string) — 2001 Data Zone code. May be null.
    - `intermediate_zone` (string, required) — 2022 Intermediate Zone name. Scottish equivalent of MSOA. May be null.
    - `intermediate_zone_2011` (string) — 2011 Intermediate Zone code. May be null.
    - `intermediate_zone_2001` (string) — 2001 Intermediate Zone code. May be null.
    - `locality` (string) — 2022 Settlement-and-Locality locality name. May be null.
    - `locality_2020` (string) — 2020 locality name (historical). May be null.
    - `locality_2001` (string) — 2001 locality name (historical). May be null.
    - `locality_1991` (string) — 1991 locality name (historical). May be null.
    - `settlement` (string) — 2022 settlement name. May be null.
    - `settlement_2020` (string) — 2020 settlement name (historical). May be null.
    - `settlement_2001` (string) — 2001 settlement name (historical). May be null.
    - `civil_parish` (string) — 1930 Scottish civil parish name (the latest historical baseline; civil parishes were abolished as administrative units in 1975). May be null.
    - `island` (string) — Island name where the postcode is located. "Mainland of Scotland" for non-island postcodes. May be null.
    - `national_park` (string) — 2010 national park name (Cairngorms / Loch Lomond and the Trossachs). Null for non-park postcodes. May be null.
    - `travel_to_work_area` (string) — 2011 Travel to Work Area name. May be null.
    - `lau_level_1` (string) — 2025 LAU level 1 name. Replaces the previous NUTS classifications. May be null.
    - `itl_level_2` (string) — 2025 ITL level 2 name. Mid-tier UK statistical geography (replaces NUTS 2). May be null.
    - `itl_level_3` (string) — 2025 ITL level 3 name. The most granular ITL geography (replaces NUTS 3). May be null.
    - `urban_rural_6_fold` (string) — 2022 Scottish Government 6-fold urban-rural classification code: * 1: Large Urban Areas * 2: Other Urban Areas * 3: Accessible Small Towns * 4: Remote Small Towns * 5: Accessible Rural * 6: Remote Rural. May be null.
    - `urban_rural_8_fold` (string) — 2022 Scottish Government 8-fold urban-rural classification code (1–8). Splits "Remote" categories into "Remote" and "Very Remote". May be null.
    - `scottish_index_of_multiple_deprivation` (integer (int32)) — SIMD 2020 rank for the postcode's Data Zone (1 = most deprived, 6976 = least deprived). May be null.
    - `roa_community_planning_partnership` (string) — 2006 Community Planning Partnership name (Regional Outcome Agreement geography). May be null.
    - `roa_local` (string) — 2006 Regional Outcome Agreement local authority name. May be null.
    - `census_household_count` (integer (int32)) — Number of households recorded against this postcode at the 2022 census. May be 0 for empty or zero-suppressed postcodes. May be null.
    - `census_household_count_2011` (integer (int32)) — Number of households recorded at the 2011 census. May be null.
    - `census_household_count_2001` (integer (int32)) — Number of households recorded at the 2001 census. May be null.
    - `census_household_count_1991` (integer (int32)) — Number of households recorded at the 1991 census. May be null.
    - `census_population_count` (integer (int32)) — Resident population recorded against this postcode at the 2022 census. May be null.
    - `census_population_count_2011` (integer (int32)) — Resident population recorded at the 2011 census. May be null.
    - `census_population_count_2001` (integer (int32)) — Resident population recorded at the 2001 census. May be null.
    - `census_population_count_1991` (integer (int32)) — Resident population recorded at the 1991 census. May be null.
    - `never_digitised` (boolean) — True if the postcode has never been digitised (no grid reference established).
    - `codes` (object, required) — GSS / official codes for the corresponding name fields above.
      - `council_area` (string) — 9-character GSS code for the 2019 council area. May be null.
      - `electoral_ward` (string) — 9-character GSS code for the 2022 electoral ward. May be null.
      - `enterprise_region` (string) — Code for the 2008 enterprise region. May be null.
      - `local_government_district` (string) — Code for the 1995 local government district. May be null.
      - `local_government_district_1991` (string) — Code for the 1991 local government district. May be null.
      - `uk_parliamentary_constituency` (string) — 9-character GSS code for the 2024 UK Parliamentary constituency. May be null.
      - `scottish_parliamentary_region` (string) — 9-character GSS code for the 2026 Scottish Parliamentary region (current designation). May be null.
      - `scottish_parliamentary_constituency` (string) — 9-character GSS code for the 2026 Scottish Parliamentary constituency (current designation). Pattern: `^S[0-9]{8}$`. May be null.
      - `health_board_area` (string) — 9-character GSS code for the 2019 NHS health board area. May be null.
      - `health_board_area_2006` (string) — GSS code for the 2006 health board area. May be null.
      - `health_board_area_1995` (string) — Code for the 1995 health board area. May be null.
      - `integration_authority` (string) — 9-character GSS code for the 2019 integration authority. May be null.
      - `data_zone` (string) — GSS code for the 2022 Data Zone. May be null.
      - `data_zone_2011` (string) — GSS code for the 2011 Data Zone. May be null.
      - `data_zone_2001` (string) — Code for the 2001 Data Zone. May be null.
      - `intermediate_zone` (string) — GSS code for the 2022 Intermediate Zone. May be null.
      - `intermediate_zone_2011` (string) — GSS code for the 2011 Intermediate Zone. May be null.
      - `intermediate_zone_2001` (string) — Code for the 2001 Intermediate Zone. May be null.
      - `locality` (string) — Code for the 2022 locality. May be null.
      - `settlement` (string) — Code for the 2022 settlement. May be null.
      - `civil_parish` (string) — Code for the 1930 civil parish. May be null.
      - `island` (string) — Island identifier code. May be null.
      - `national_park` (string) — Code for the 2010 national park. May be null.
      - `travel_to_work_area` (string) — Code for the 2011 Travel to Work Area. May be null.
      - `lau_level_1` (string) — Code for the 2025 LAU level 1 area. May be null.
      - `itl_level_2` (string) — Code for the 2025 ITL level 2 area. May be null.
      - `itl_level_3` (string) — Code for the 2025 ITL level 3 area. May be null.
      - `registration_district` (string) — Code for the 2007 registration district. May be null.
      - `strategic_development_planning_area` (string) — Code for the 2013 strategic development planning area. May be null.
      - `roa_community_planning_partnership` (string) — Code for the 2006 community planning partnership. May be null.
      - `roa_local` (string) — Code for the 2006 ROA local authority. May be null.
- **404** — Postcode not found

## Outward Codes

### GET /outcodes/{outcode}

**Find an Outward Code**

Returns aggregated information for postcodes grouped by their shared outward code.

The outward code is the first half of any postcode (3-4 characters and followed by a space). E.g. `SW1A` is the outward code for `SW1A 1AA`.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `outcode` | path | string | Yes | Specifies the outward code you wish to query. |

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (one of several types, required) — Comprehensive geographical and administrative data for the specified outcode, including location coordinates, administrative boundaries, and related postal information
    - `outcode` (string, required) — First part of the postcode before the space (e.g., "SW1A" in "SW1A 1AA"). Usually 2-4 characters.
    - `eastings` (number (int32), required) — Ordnance Survey eastings coordinate (1m resolution). Returns 0 if location unavailable. May be null.
    - `northings` (number (int32), required) — Ordnance Survey northings coordinate (1m resolution). Returns 0 if location unavailable. May be null.
    - `admin_county` (array of string, required) — Administrative counties within this outcode.
    - `admin_district` (array of string, required) — District/unitary authorities within this outcode.
    - `admin_ward` (array of string, required) — Administrative/electoral wards within this outcode.
    - `longitude` (number (double), required) — WGS84 longitude coordinate. May be null if location unavailable. May be null.
    - `latitude` (number (double), required) — WGS84 latitude coordinate. May be null if location unavailable. May be null.
    - `country` (array of string, required) — Countries within this outcode.
    - `parish` (array of string, required) — Parishes (England) or communities (Wales) within this outcode.
    - `parliamentary_constituency` (array of string, required) — UK Parliamentary constituencies (July 2024 boundaries) that intersect this outcode.

## Places

### GET /places

**Find a Place**

Submit a place query and receive a complete list of places matches and associated data.

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (array of object, required) — Data for a given place
    - `code` (string, required) — Unique identifier for the place record (persistent except for Section of Named/Numbered Roads)
    - `name_1` (string, required) — Official name of the place (preserves original format, e.g., "The Pennines" not "Pennines, The")
    - `name_1_lang` (string, required) — Language code for name_1 (cym=Welsh, eng=English, gla=Scottish Gaelic). May be null.
    - `name_2` (string, required) — Alternative name in a different language. May be null.
    - `name_2_lang` (string, required) — Language code for name_2 (cym=Welsh, eng=English, gla=Scottish Gaelic). May be null.
    - `local_type` (string, required) — Ordnance Survey classification (City, Town, Village, Hamlet, etc.)
    - `outcode` (string, required) — Postcode district (first part of the postcode)
    - `county_unitary` (string, required) — County, Unitary Authority or Greater London Authority that contains this place. May be null.
    - `county_unitary_type` (string, required) — Type of administrative unit (e.g., County, UnitaryAuthority). May be null.
    - `district_borough` (string, required) — District, Metropolitan District or London Borough containing this place. May be null.
    - `district_borough_type` (string) — Type of district/borough administrative unit. May be null.
    - `region` (string, required) — European Region (formerly Government Office Region) containing this place
    - `country` (string, required) — Country within Great Britain (England, Scotland, or Wales)
    - `longitude` (number (double), required) — WGS84 longitude coordinate
    - `latitude` (number (double), required) — WGS84 latitude coordinate
    - `eastings` (integer, required) — Ordnance Survey grid reference Easting (1m resolution, not available for Channel Islands/Isle of Man)
    - `northings` (integer, required) — Ordnance Survey grid reference Northing (1m resolution, not available for Channel Islands/Isle of Man)
    - `min_eastings` (integer, required) — Western edge of the place's bounding box (Minimum Bounding Rectangle)
    - `min_northings` (integer, required) — Southern edge of the place's bounding box (Minimum Bounding Rectangle)
    - `max_eastings` (integer, required) — Eastern edge of the place's bounding box (Minimum Bounding Rectangle)
    - `max_northings` (integer, required) — Northern edge of the place's bounding box (Minimum Bounding Rectangle)

### GET /places/{code}

**Find a Place by ID**

Submit a place query and receive a complete list of place matches and associated data.

This API uses the Ordnance Survey Open Names Dataset. Places are not available for Northern Ireland.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `code` | path | string | Yes | Specifies the place you wish to query |

**Responses**

- **200** — Success
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (object, required) — Data for a given place
    - `code` (string, required) — Unique identifier for the place record (persistent except for Section of Named/Numbered Roads)
    - `name_1` (string, required) — Official name of the place (preserves original format, e.g., "The Pennines" not "Pennines, The")
    - `name_1_lang` (string, required) — Language code for name_1 (cym=Welsh, eng=English, gla=Scottish Gaelic). May be null.
    - `name_2` (string, required) — Alternative name in a different language. May be null.
    - `name_2_lang` (string, required) — Language code for name_2 (cym=Welsh, eng=English, gla=Scottish Gaelic). May be null.
    - `local_type` (string, required) — Ordnance Survey classification (City, Town, Village, Hamlet, etc.)
    - `outcode` (string, required) — Postcode district (first part of the postcode)
    - `county_unitary` (string, required) — County, Unitary Authority or Greater London Authority that contains this place. May be null.
    - `county_unitary_type` (string, required) — Type of administrative unit (e.g., County, UnitaryAuthority). May be null.
    - `district_borough` (string, required) — District, Metropolitan District or London Borough containing this place. May be null.
    - `district_borough_type` (string) — Type of district/borough administrative unit. May be null.
    - `region` (string, required) — European Region (formerly Government Office Region) containing this place
    - `country` (string, required) — Country within Great Britain (England, Scotland, or Wales)
    - `longitude` (number (double), required) — WGS84 longitude coordinate
    - `latitude` (number (double), required) — WGS84 latitude coordinate
    - `eastings` (integer, required) — Ordnance Survey grid reference Easting (1m resolution, not available for Channel Islands/Isle of Man)
    - `northings` (integer, required) — Ordnance Survey grid reference Northing (1m resolution, not available for Channel Islands/Isle of Man)
    - `min_eastings` (integer, required) — Western edge of the place's bounding box (Minimum Bounding Rectangle)
    - `min_northings` (integer, required) — Southern edge of the place's bounding box (Minimum Bounding Rectangle)
    - `max_eastings` (integer, required) — Eastern edge of the place's bounding box (Minimum Bounding Rectangle)
    - `max_northings` (integer, required) — Northern edge of the place's bounding box (Minimum Bounding Rectangle)

### GET /random/places

**Retrieve a Random Place**

Returns a randomly selected place from the database along with all its associated geographical and administrative data. Useful for testing or displaying sample location data.

**Responses**

- **200** — Successfully retrieved a random place
  Body (`application/json`, object):
  - `status` (integer (int32), required) — Allowed values: `200`.
  - `result` (object, required) — Data for a given place
    - `code` (string, required) — Unique identifier for the place record (persistent except for Section of Named/Numbered Roads)
    - `name_1` (string, required) — Official name of the place (preserves original format, e.g., "The Pennines" not "Pennines, The")
    - `name_1_lang` (string, required) — Language code for name_1 (cym=Welsh, eng=English, gla=Scottish Gaelic). May be null.
    - `name_2` (string, required) — Alternative name in a different language. May be null.
    - `name_2_lang` (string, required) — Language code for name_2 (cym=Welsh, eng=English, gla=Scottish Gaelic). May be null.
    - `local_type` (string, required) — Ordnance Survey classification (City, Town, Village, Hamlet, etc.)
    - `outcode` (string, required) — Postcode district (first part of the postcode)
    - `county_unitary` (string, required) — County, Unitary Authority or Greater London Authority that contains this place. May be null.
    - `county_unitary_type` (string, required) — Type of administrative unit (e.g., County, UnitaryAuthority). May be null.
    - `district_borough` (string, required) — District, Metropolitan District or London Borough containing this place. May be null.
    - `district_borough_type` (string) — Type of district/borough administrative unit. May be null.
    - `region` (string, required) — European Region (formerly Government Office Region) containing this place
    - `country` (string, required) — Country within Great Britain (England, Scotland, or Wales)
    - `longitude` (number (double), required) — WGS84 longitude coordinate
    - `latitude` (number (double), required) — WGS84 latitude coordinate
    - `eastings` (integer, required) — Ordnance Survey grid reference Easting (1m resolution, not available for Channel Islands/Isle of Man)
    - `northings` (integer, required) — Ordnance Survey grid reference Northing (1m resolution, not available for Channel Islands/Isle of Man)
    - `min_eastings` (integer, required) — Western edge of the place's bounding box (Minimum Bounding Rectangle)
    - `min_northings` (integer, required) — Southern edge of the place's bounding box (Minimum Bounding Rectangle)
    - `max_eastings` (integer, required) — Eastern edge of the place's bounding box (Minimum Bounding Rectangle)
    - `max_northings` (integer, required) — Northern edge of the place's bounding box (Minimum Bounding Rectangle)
