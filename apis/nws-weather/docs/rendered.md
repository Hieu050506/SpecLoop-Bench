# weather.gov API — API Reference

weather.gov API

**Version:** 3.12.2  
**Base URL:** `https://api.weather.gov`

## Authentication

- **userAgent**: API key sent in header parameter `User-Agent`.
  We require that all consumers of the API include a User-Agent header in requests. This is due to a high number of scripts exhibiting abusive behavior (intentional or unintentional). We recommend setting the value to something that identifies your application and includes a contact email. This will help us contact you if we notice unusual behavior and also aid in troubleshooting issues. The API remains open and free to use and there are no limits imposed based on the User-Agent string. This mechanism will be replaced with a more typical API key system at a later date.
- **apiKeyAuth**: API key sent in header parameter `API-Key`.
  We are testing including a more traditional API Key system on certain endpoints. This is due to a large change in the weather.gov site. The API remains open and free to use and there are no limits imposed based on the X-Api-Key string.

## Endpoints

### GET /alerts

Returns all alerts

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `active` | query | boolean | No | List only active alerts (use /alerts/active endpoints instead) |
| `start` | query | string (date-time) | No | Start time |
| `end` | query | string (date-time) | No | End time |
| `status` | query | array of string | No | Status (actual, exercise, system, test, draft) |
| `message_type` | query | array of string | No | Message type (alert, update, cancel) |
| `event` | query | array of string | No | Event name |
| `code` | query | array of string | No | Event code |
| `area` | query | array of one of several types | No | State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone |
| `point` | query | string | No | Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone. Pattern: `^(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)$`. |
| `region` | query | array of string | No | Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone |
| `region_type` | query | string | No | Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone. Allowed values: `land`, `marine`. |
| `zone` | query | array of string | No | Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type |
| `urgency` | query | array of string | No | Urgency (immediate, expected, future, past, unknown) |
| `severity` | query | array of string | No | Severity (extreme, severe, moderate, minor, unknown) |
| `certainty` | query | array of string | No | Certainty (observed, likely, possible, unlikely, unknown) |
| `limit` | query | integer | No | Limit. Default: `500`. Minimum: 1. Maximum: 500. |
| `cursor` | query | string | No | Pagination cursor |

**Responses**

- **200** — A collection of alerts.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object) — An object representing a public alert message. Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information. http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://vlab.noaa.gov/web/nws-common-alerting-protocol/cap-documentation
      - `id` (string) — The identifier of the alert message.
      - `areaDesc` (string) — A textual description of the area affected by the alert.
      - `geocode` (object) — Lists of codes for NWS public zones and counties affected by the alert.
        - `UGC` (array of string) — A list of NWS public zone or county identifiers.
        - `SAME` (array of string) — A list of SAME (Specific Area Message Encoding) codes for affected counties.
      - `affectedZones` (array of string (uri)) — An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification.
      - `references` (array of object) — A list of prior alerts that this alert updates or replaces.
        - `@id` (string (uri)) — An API link to the prior alert.
        - `identifier` (string) — The identifier of the alert message.
        - `sender` (string) — The sender of the prior alert.
        - `sent` (string (date-time)) — The time the prior alert was sent.
      - `sent` (string (date-time)) — The time of the origination of the alert message.
      - `effective` (string (date-time)) — The effective time of the information of the alert message.
      - `onset` (string (date-time)) — The expected time of the beginning of the subject event of the alert message. May be null.
      - `expires` (string (date-time)) — The expiry time of the information of the alert message.
      - `ends` (string (date-time)) — The expected end time of the subject event of the alert message. May be null.
      - `status` (string) — Allowed values: `Actual`, `Exercise`, `System`, `Test`, `Draft`.
      - `messageType` (string) — Allowed values: `Alert`, `Update`, `Cancel`, `Ack`, `Error`.
      - `category` (string) — The code denoting the category of the subject event of the alert message. Allowed values: `Met`, `Geo`, `Safety`, `Security`, `Rescue`, `Fire`, `Health`, `Env`, `Transport`, `Infra`, `CBRNE`, `Other`.
      - `severity` (string) — Allowed values: `Extreme`, `Severe`, `Moderate`, `Minor`, `Unknown`.
      - `certainty` (string) — Allowed values: `Observed`, `Likely`, `Possible`, `Unlikely`, `Unknown`.
      - `urgency` (string) — Allowed values: `Immediate`, `Expected`, `Future`, `Past`, `Unknown`.
      - `event` (string) — The text denoting the type of the subject event of the alert message.
      - `sender` (string) — Email address of the NWS webmaster.
      - `senderName` (string) — The text naming the originator of the alert message.
      - `headline` (string) — The text headline of the alert message. May be null.
      - `description` (string) — The text describing the subject event of the alert message.
      - `instruction` (string) — The text describing the recommended action to be taken by recipients of the alert message. May be null.
      - `note` (string) — The text note accompanying the alert message. Per CAP spec, this should accompany alerts with a status of "Test". May be null.
      - `response` (string) — The code denoting the type of action recommended for the target audience. This corresponds to responseType in the CAP specification. Allowed values: `Shelter`, `Evacuate`, `Prepare`, `Execute`, `Avoid`, `Monitor`, `Assess`, `AllClear`, `None`.
      - `parameters` (object) — System-specific additional parameters associated with the alert message. The keys in this object correspond to parameter definitions in the NWS CAP specification.
      - `scope` (string) — The code denoting the intended distribution of the alert message. Allowed values: `Public`, `Restricted`, `Private`.
      - `code` (string) — The code denoting the special handling of the alert message.
      - `language` (string) — The code denoting the language of the info sub-element of the alert message.
      - `web` (string) — The identifier of the hyperlink associating additional information within the alert message.
      - `eventCode` (object) — System-specific code identifiying the event type of the alert message The keys in this object correspond to eventCode definitions in the NWS CAP specification.
  - `title` (string) — A title describing the alert collection
  - `updated` (string (date-time)) — The last time a change occurred to this collection
  - `pagination` (object) — Links for retrieving more data from paged data sets
    - `next` (string (uri), required) — A link to the next page of records
- **301** — Certain common queries may be redirected to discrete URLs
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /alerts/active

Returns all currently active alerts

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `status` | query | array of string | No | Status (actual, exercise, system, test, draft) |
| `message_type` | query | array of string | No | Message type (alert, update, cancel) |
| `event` | query | array of string | No | Event name |
| `code` | query | array of string | No | Event code |
| `area` | query | array of one of several types | No | State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone |
| `point` | query | string | No | Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone. Pattern: `^(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)$`. |
| `region` | query | array of string | No | Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone |
| `region_type` | query | string | No | Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone. Allowed values: `land`, `marine`. |
| `zone` | query | array of string | No | Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type |
| `urgency` | query | array of string | No | Urgency (immediate, expected, future, past, unknown) |
| `severity` | query | array of string | No | Severity (extreme, severe, moderate, minor, unknown) |
| `certainty` | query | array of string | No | Certainty (observed, likely, possible, unlikely, unknown) |

**Responses**

- **200** — A collection of active alerts.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object) — An object representing a public alert message. Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information. http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://vlab.noaa.gov/web/nws-common-alerting-protocol/cap-documentation
      - `id` (string) — The identifier of the alert message.
      - `areaDesc` (string) — A textual description of the area affected by the alert.
      - `geocode` (object) — Lists of codes for NWS public zones and counties affected by the alert.
        - `UGC` (array of string) — A list of NWS public zone or county identifiers.
        - `SAME` (array of string) — A list of SAME (Specific Area Message Encoding) codes for affected counties.
      - `affectedZones` (array of string (uri)) — An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification.
      - `references` (array of object) — A list of prior alerts that this alert updates or replaces.
        - `@id` (string (uri)) — An API link to the prior alert.
        - `identifier` (string) — The identifier of the alert message.
        - `sender` (string) — The sender of the prior alert.
        - `sent` (string (date-time)) — The time the prior alert was sent.
      - `sent` (string (date-time)) — The time of the origination of the alert message.
      - `effective` (string (date-time)) — The effective time of the information of the alert message.
      - `onset` (string (date-time)) — The expected time of the beginning of the subject event of the alert message. May be null.
      - `expires` (string (date-time)) — The expiry time of the information of the alert message.
      - `ends` (string (date-time)) — The expected end time of the subject event of the alert message. May be null.
      - `status` (string) — Allowed values: `Actual`, `Exercise`, `System`, `Test`, `Draft`.
      - `messageType` (string) — Allowed values: `Alert`, `Update`, `Cancel`, `Ack`, `Error`.
      - `category` (string) — The code denoting the category of the subject event of the alert message. Allowed values: `Met`, `Geo`, `Safety`, `Security`, `Rescue`, `Fire`, `Health`, `Env`, `Transport`, `Infra`, `CBRNE`, `Other`.
      - `severity` (string) — Allowed values: `Extreme`, `Severe`, `Moderate`, `Minor`, `Unknown`.
      - `certainty` (string) — Allowed values: `Observed`, `Likely`, `Possible`, `Unlikely`, `Unknown`.
      - `urgency` (string) — Allowed values: `Immediate`, `Expected`, `Future`, `Past`, `Unknown`.
      - `event` (string) — The text denoting the type of the subject event of the alert message.
      - `sender` (string) — Email address of the NWS webmaster.
      - `senderName` (string) — The text naming the originator of the alert message.
      - `headline` (string) — The text headline of the alert message. May be null.
      - `description` (string) — The text describing the subject event of the alert message.
      - `instruction` (string) — The text describing the recommended action to be taken by recipients of the alert message. May be null.
      - `note` (string) — The text note accompanying the alert message. Per CAP spec, this should accompany alerts with a status of "Test". May be null.
      - `response` (string) — The code denoting the type of action recommended for the target audience. This corresponds to responseType in the CAP specification. Allowed values: `Shelter`, `Evacuate`, `Prepare`, `Execute`, `Avoid`, `Monitor`, `Assess`, `AllClear`, `None`.
      - `parameters` (object) — System-specific additional parameters associated with the alert message. The keys in this object correspond to parameter definitions in the NWS CAP specification.
      - `scope` (string) — The code denoting the intended distribution of the alert message. Allowed values: `Public`, `Restricted`, `Private`.
      - `code` (string) — The code denoting the special handling of the alert message.
      - `language` (string) — The code denoting the language of the info sub-element of the alert message.
      - `web` (string) — The identifier of the hyperlink associating additional information within the alert message.
      - `eventCode` (object) — System-specific code identifiying the event type of the alert message The keys in this object correspond to eventCode definitions in the NWS CAP specification.
  - `title` (string) — A title describing the alert collection
  - `updated` (string (date-time)) — The last time a change occurred to this collection
- **301** — Certain common queries may be redirected to discrete URLs
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /alerts/active/count

Returns info on the number of active alerts

**Responses**

- **200** — A data structure showing the counts of active alerts broken down by various categories
  Body (`application/ld+json`, object):
  - `total` (integer) — The total number of active alerts. Minimum: 0.
  - `land` (integer) — The total number of active alerts affecting land zones. Minimum: 0.
  - `marine` (integer) — The total number of active alerts affecting marine zones. Minimum: 0.
  - `regions` (object) — Active alerts by marine region
  - `areas` (object) — Active alerts by area (state/territory)
  - `zones` (object) — Active alerts by NWS public zone or county code
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /alerts/active/zone/{zoneId}

Returns active alerts for the given NWS public zone or county

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `zoneId` | path | string | Yes | NWS public zone/county identifier. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`. |

**Responses**

- **200** — A collection of active alerts.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object) — An object representing a public alert message. Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information. http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://vlab.noaa.gov/web/nws-common-alerting-protocol/cap-documentation
      - `id` (string) — The identifier of the alert message.
      - `areaDesc` (string) — A textual description of the area affected by the alert.
      - `geocode` (object) — Lists of codes for NWS public zones and counties affected by the alert.
        - `UGC` (array of string) — A list of NWS public zone or county identifiers.
        - `SAME` (array of string) — A list of SAME (Specific Area Message Encoding) codes for affected counties.
      - `affectedZones` (array of string (uri)) — An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification.
      - `references` (array of object) — A list of prior alerts that this alert updates or replaces.
        - `@id` (string (uri)) — An API link to the prior alert.
        - `identifier` (string) — The identifier of the alert message.
        - `sender` (string) — The sender of the prior alert.
        - `sent` (string (date-time)) — The time the prior alert was sent.
      - `sent` (string (date-time)) — The time of the origination of the alert message.
      - `effective` (string (date-time)) — The effective time of the information of the alert message.
      - `onset` (string (date-time)) — The expected time of the beginning of the subject event of the alert message. May be null.
      - `expires` (string (date-time)) — The expiry time of the information of the alert message.
      - `ends` (string (date-time)) — The expected end time of the subject event of the alert message. May be null.
      - `status` (string) — Allowed values: `Actual`, `Exercise`, `System`, `Test`, `Draft`.
      - `messageType` (string) — Allowed values: `Alert`, `Update`, `Cancel`, `Ack`, `Error`.
      - `category` (string) — The code denoting the category of the subject event of the alert message. Allowed values: `Met`, `Geo`, `Safety`, `Security`, `Rescue`, `Fire`, `Health`, `Env`, `Transport`, `Infra`, `CBRNE`, `Other`.
      - `severity` (string) — Allowed values: `Extreme`, `Severe`, `Moderate`, `Minor`, `Unknown`.
      - `certainty` (string) — Allowed values: `Observed`, `Likely`, `Possible`, `Unlikely`, `Unknown`.
      - `urgency` (string) — Allowed values: `Immediate`, `Expected`, `Future`, `Past`, `Unknown`.
      - `event` (string) — The text denoting the type of the subject event of the alert message.
      - `sender` (string) — Email address of the NWS webmaster.
      - `senderName` (string) — The text naming the originator of the alert message.
      - `headline` (string) — The text headline of the alert message. May be null.
      - `description` (string) — The text describing the subject event of the alert message.
      - `instruction` (string) — The text describing the recommended action to be taken by recipients of the alert message. May be null.
      - `note` (string) — The text note accompanying the alert message. Per CAP spec, this should accompany alerts with a status of "Test". May be null.
      - `response` (string) — The code denoting the type of action recommended for the target audience. This corresponds to responseType in the CAP specification. Allowed values: `Shelter`, `Evacuate`, `Prepare`, `Execute`, `Avoid`, `Monitor`, `Assess`, `AllClear`, `None`.
      - `parameters` (object) — System-specific additional parameters associated with the alert message. The keys in this object correspond to parameter definitions in the NWS CAP specification.
      - `scope` (string) — The code denoting the intended distribution of the alert message. Allowed values: `Public`, `Restricted`, `Private`.
      - `code` (string) — The code denoting the special handling of the alert message.
      - `language` (string) — The code denoting the language of the info sub-element of the alert message.
      - `web` (string) — The identifier of the hyperlink associating additional information within the alert message.
      - `eventCode` (object) — System-specific code identifiying the event type of the alert message The keys in this object correspond to eventCode definitions in the NWS CAP specification.
  - `title` (string) — A title describing the alert collection
  - `updated` (string (date-time)) — The last time a change occurred to this collection
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /alerts/active/area/{area}

Returns active alerts for the given area (state or marine area)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `area` | path | one of several types | Yes | State/area ID |

**Responses**

- **200** — A collection of active alerts.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object) — An object representing a public alert message. Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information. http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://vlab.noaa.gov/web/nws-common-alerting-protocol/cap-documentation
      - `id` (string) — The identifier of the alert message.
      - `areaDesc` (string) — A textual description of the area affected by the alert.
      - `geocode` (object) — Lists of codes for NWS public zones and counties affected by the alert.
        - `UGC` (array of string) — A list of NWS public zone or county identifiers.
        - `SAME` (array of string) — A list of SAME (Specific Area Message Encoding) codes for affected counties.
      - `affectedZones` (array of string (uri)) — An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification.
      - `references` (array of object) — A list of prior alerts that this alert updates or replaces.
        - `@id` (string (uri)) — An API link to the prior alert.
        - `identifier` (string) — The identifier of the alert message.
        - `sender` (string) — The sender of the prior alert.
        - `sent` (string (date-time)) — The time the prior alert was sent.
      - `sent` (string (date-time)) — The time of the origination of the alert message.
      - `effective` (string (date-time)) — The effective time of the information of the alert message.
      - `onset` (string (date-time)) — The expected time of the beginning of the subject event of the alert message. May be null.
      - `expires` (string (date-time)) — The expiry time of the information of the alert message.
      - `ends` (string (date-time)) — The expected end time of the subject event of the alert message. May be null.
      - `status` (string) — Allowed values: `Actual`, `Exercise`, `System`, `Test`, `Draft`.
      - `messageType` (string) — Allowed values: `Alert`, `Update`, `Cancel`, `Ack`, `Error`.
      - `category` (string) — The code denoting the category of the subject event of the alert message. Allowed values: `Met`, `Geo`, `Safety`, `Security`, `Rescue`, `Fire`, `Health`, `Env`, `Transport`, `Infra`, `CBRNE`, `Other`.
      - `severity` (string) — Allowed values: `Extreme`, `Severe`, `Moderate`, `Minor`, `Unknown`.
      - `certainty` (string) — Allowed values: `Observed`, `Likely`, `Possible`, `Unlikely`, `Unknown`.
      - `urgency` (string) — Allowed values: `Immediate`, `Expected`, `Future`, `Past`, `Unknown`.
      - `event` (string) — The text denoting the type of the subject event of the alert message.
      - `sender` (string) — Email address of the NWS webmaster.
      - `senderName` (string) — The text naming the originator of the alert message.
      - `headline` (string) — The text headline of the alert message. May be null.
      - `description` (string) — The text describing the subject event of the alert message.
      - `instruction` (string) — The text describing the recommended action to be taken by recipients of the alert message. May be null.
      - `note` (string) — The text note accompanying the alert message. Per CAP spec, this should accompany alerts with a status of "Test". May be null.
      - `response` (string) — The code denoting the type of action recommended for the target audience. This corresponds to responseType in the CAP specification. Allowed values: `Shelter`, `Evacuate`, `Prepare`, `Execute`, `Avoid`, `Monitor`, `Assess`, `AllClear`, `None`.
      - `parameters` (object) — System-specific additional parameters associated with the alert message. The keys in this object correspond to parameter definitions in the NWS CAP specification.
      - `scope` (string) — The code denoting the intended distribution of the alert message. Allowed values: `Public`, `Restricted`, `Private`.
      - `code` (string) — The code denoting the special handling of the alert message.
      - `language` (string) — The code denoting the language of the info sub-element of the alert message.
      - `web` (string) — The identifier of the hyperlink associating additional information within the alert message.
      - `eventCode` (object) — System-specific code identifiying the event type of the alert message The keys in this object correspond to eventCode definitions in the NWS CAP specification.
  - `title` (string) — A title describing the alert collection
  - `updated` (string (date-time)) — The last time a change occurred to this collection
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /alerts/active/region/{region}

Returns active alerts for the given marine region

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `region` | path | string | Yes | Marine region ID. Allowed values: `AL`, `AT`, `GL`, `GM`, `PA`, `PI`. |

**Responses**

- **200** — A collection of active alerts.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object) — An object representing a public alert message. Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information. http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://vlab.noaa.gov/web/nws-common-alerting-protocol/cap-documentation
      - `id` (string) — The identifier of the alert message.
      - `areaDesc` (string) — A textual description of the area affected by the alert.
      - `geocode` (object) — Lists of codes for NWS public zones and counties affected by the alert.
        - `UGC` (array of string) — A list of NWS public zone or county identifiers.
        - `SAME` (array of string) — A list of SAME (Specific Area Message Encoding) codes for affected counties.
      - `affectedZones` (array of string (uri)) — An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification.
      - `references` (array of object) — A list of prior alerts that this alert updates or replaces.
        - `@id` (string (uri)) — An API link to the prior alert.
        - `identifier` (string) — The identifier of the alert message.
        - `sender` (string) — The sender of the prior alert.
        - `sent` (string (date-time)) — The time the prior alert was sent.
      - `sent` (string (date-time)) — The time of the origination of the alert message.
      - `effective` (string (date-time)) — The effective time of the information of the alert message.
      - `onset` (string (date-time)) — The expected time of the beginning of the subject event of the alert message. May be null.
      - `expires` (string (date-time)) — The expiry time of the information of the alert message.
      - `ends` (string (date-time)) — The expected end time of the subject event of the alert message. May be null.
      - `status` (string) — Allowed values: `Actual`, `Exercise`, `System`, `Test`, `Draft`.
      - `messageType` (string) — Allowed values: `Alert`, `Update`, `Cancel`, `Ack`, `Error`.
      - `category` (string) — The code denoting the category of the subject event of the alert message. Allowed values: `Met`, `Geo`, `Safety`, `Security`, `Rescue`, `Fire`, `Health`, `Env`, `Transport`, `Infra`, `CBRNE`, `Other`.
      - `severity` (string) — Allowed values: `Extreme`, `Severe`, `Moderate`, `Minor`, `Unknown`.
      - `certainty` (string) — Allowed values: `Observed`, `Likely`, `Possible`, `Unlikely`, `Unknown`.
      - `urgency` (string) — Allowed values: `Immediate`, `Expected`, `Future`, `Past`, `Unknown`.
      - `event` (string) — The text denoting the type of the subject event of the alert message.
      - `sender` (string) — Email address of the NWS webmaster.
      - `senderName` (string) — The text naming the originator of the alert message.
      - `headline` (string) — The text headline of the alert message. May be null.
      - `description` (string) — The text describing the subject event of the alert message.
      - `instruction` (string) — The text describing the recommended action to be taken by recipients of the alert message. May be null.
      - `note` (string) — The text note accompanying the alert message. Per CAP spec, this should accompany alerts with a status of "Test". May be null.
      - `response` (string) — The code denoting the type of action recommended for the target audience. This corresponds to responseType in the CAP specification. Allowed values: `Shelter`, `Evacuate`, `Prepare`, `Execute`, `Avoid`, `Monitor`, `Assess`, `AllClear`, `None`.
      - `parameters` (object) — System-specific additional parameters associated with the alert message. The keys in this object correspond to parameter definitions in the NWS CAP specification.
      - `scope` (string) — The code denoting the intended distribution of the alert message. Allowed values: `Public`, `Restricted`, `Private`.
      - `code` (string) — The code denoting the special handling of the alert message.
      - `language` (string) — The code denoting the language of the info sub-element of the alert message.
      - `web` (string) — The identifier of the hyperlink associating additional information within the alert message.
      - `eventCode` (object) — System-specific code identifiying the event type of the alert message The keys in this object correspond to eventCode definitions in the NWS CAP specification.
  - `title` (string) — A title describing the alert collection
  - `updated` (string (date-time)) — The last time a change occurred to this collection
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /alerts/types

Returns a list of alert types

**Responses**

- **200** — A list of recognized event types
  Body (`application/ld+json`, object):
  - `eventTypes` (array of string) — A list of recognized event types
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /alerts/{id}

Returns a specific alert

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | Alert identifier |

**Responses**

- **200** — An alert record
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required) — An object representing a public alert message. Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information. http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://vlab.noaa.gov/web/nws-common-alerting-protocol/cap-documentation
    - `id` (string) — The identifier of the alert message.
    - `areaDesc` (string) — A textual description of the area affected by the alert.
    - `geocode` (object) — Lists of codes for NWS public zones and counties affected by the alert.
      - `UGC` (array of string) — A list of NWS public zone or county identifiers.
      - `SAME` (array of string) — A list of SAME (Specific Area Message Encoding) codes for affected counties.
    - `affectedZones` (array of string (uri)) — An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification.
    - `references` (array of object) — A list of prior alerts that this alert updates or replaces.
      - `@id` (string (uri)) — An API link to the prior alert.
      - `identifier` (string) — The identifier of the alert message.
      - `sender` (string) — The sender of the prior alert.
      - `sent` (string (date-time)) — The time the prior alert was sent.
    - `sent` (string (date-time)) — The time of the origination of the alert message.
    - `effective` (string (date-time)) — The effective time of the information of the alert message.
    - `onset` (string (date-time)) — The expected time of the beginning of the subject event of the alert message. May be null.
    - `expires` (string (date-time)) — The expiry time of the information of the alert message.
    - `ends` (string (date-time)) — The expected end time of the subject event of the alert message. May be null.
    - `status` (string) — Allowed values: `Actual`, `Exercise`, `System`, `Test`, `Draft`.
    - `messageType` (string) — Allowed values: `Alert`, `Update`, `Cancel`, `Ack`, `Error`.
    - `category` (string) — The code denoting the category of the subject event of the alert message. Allowed values: `Met`, `Geo`, `Safety`, `Security`, `Rescue`, `Fire`, `Health`, `Env`, `Transport`, `Infra`, `CBRNE`, `Other`.
    - `severity` (string) — Allowed values: `Extreme`, `Severe`, `Moderate`, `Minor`, `Unknown`.
    - `certainty` (string) — Allowed values: `Observed`, `Likely`, `Possible`, `Unlikely`, `Unknown`.
    - `urgency` (string) — Allowed values: `Immediate`, `Expected`, `Future`, `Past`, `Unknown`.
    - `event` (string) — The text denoting the type of the subject event of the alert message.
    - `sender` (string) — Email address of the NWS webmaster.
    - `senderName` (string) — The text naming the originator of the alert message.
    - `headline` (string) — The text headline of the alert message. May be null.
    - `description` (string) — The text describing the subject event of the alert message.
    - `instruction` (string) — The text describing the recommended action to be taken by recipients of the alert message. May be null.
    - `note` (string) — The text note accompanying the alert message. Per CAP spec, this should accompany alerts with a status of "Test". May be null.
    - `response` (string) — The code denoting the type of action recommended for the target audience. This corresponds to responseType in the CAP specification. Allowed values: `Shelter`, `Evacuate`, `Prepare`, `Execute`, `Avoid`, `Monitor`, `Assess`, `AllClear`, `None`.
    - `parameters` (object) — System-specific additional parameters associated with the alert message. The keys in this object correspond to parameter definitions in the NWS CAP specification.
    - `scope` (string) — The code denoting the intended distribution of the alert message. Allowed values: `Public`, `Restricted`, `Private`.
    - `code` (string) — The code denoting the special handling of the alert message.
    - `language` (string) — The code denoting the language of the info sub-element of the alert message.
    - `web` (string) — The identifier of the hyperlink associating additional information within the alert message.
    - `eventCode` (object) — System-specific code identifiying the event type of the alert message The keys in this object correspond to eventCode definitions in the NWS CAP specification.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /aviation/cwsus/{cwsuId}

Returns metadata about a Center Weather Service Unit

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `cwsuId` | path | string | Yes | NWS CWSU ID. Allowed values: `ZAB`, `ZAN`, `ZAU`, `ZBW`, `ZDC`, `ZDV`, `ZFA`, `ZFW`, `ZHU`, `ZID`, `ZJX`, `ZKC`, `ZLA`, `ZLC`, `ZMA`, `ZME`, `ZMP`, `ZNY`, `ZOA`, `ZOB`, `ZSE`, `ZTL`. |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@type` (string) — Allowed values: `GovernmentOrganization`.
  - `@id` (string (uri))
  - `id` (string)
  - `name` (string)
  - `address` (object)
    - `@type` (string) — Allowed values: `PostalAddress`.
    - `streetAddress` (string)
    - `addressLocality` (string)
    - `addressRegion` (string)
    - `postalCode` (string)
  - `telephone` (string)
  - `faxNumber` (string)
  - `email` (string)
  - `sameAs` (string (uri))
  - `nwsRegion` (string)
  - `parentOrganization` (string (uri))
  - `responsibleCounties` (array of string (uri))
  - `responsibleForecastZones` (array of string (uri))
  - `responsibleFireZones` (array of string (uri))
  - `approvedObservationStations` (array of string (uri))
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /aviation/cwsus/{cwsuId}/cwas

Returns a list of Center Weather Advisories from a CWSU

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `cwsuId` | path | string | Yes | NWS CWSU ID. Allowed values: `ZAB`, `ZAN`, `ZAU`, `ZBW`, `ZDC`, `ZDV`, `ZFA`, `ZFW`, `ZHU`, `ZID`, `ZJX`, `ZKC`, `ZLA`, `ZLC`, `ZMA`, `ZME`, `ZMP`, `ZNY`, `ZOA`, `ZOB`, `ZSE`, `ZTL`. |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object)
      - `id` (string)
      - `issueTime` (string (date-time))
      - `cwsu` (string) — Three-letter identifier for a Center Weather Service Unit (CWSU). Allowed values: `ZAB`, `ZAN`, `ZAU`, `ZBW`, `ZDC`, `ZDV`, `ZFA`, `ZFW`, `ZHU`, `ZID`, `ZJX`, `ZKC`, `ZLA`, `ZLC`, `ZMA`, `ZME`, `ZMP`, `ZNY`, `ZOA`, `ZOB`, `ZSE`, `ZTL`.
      - `sequence` (integer) — Minimum: 101.
      - `start` (string (date-time))
      - `end` (string (date-time))
      - `observedProperty` (string)
      - `text` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /aviation/cwsus/{cwsuId}/cwas/{date}/{sequence}

Returns a list of Center Weather Advisories from a CWSU

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `cwsuId` | path | string | Yes | NWS CWSU ID. Allowed values: `ZAB`, `ZAN`, `ZAU`, `ZBW`, `ZDC`, `ZDV`, `ZFA`, `ZFW`, `ZHU`, `ZID`, `ZJX`, `ZKC`, `ZLA`, `ZLC`, `ZMA`, `ZME`, `ZMP`, `ZNY`, `ZOA`, `ZOB`, `ZSE`, `ZTL`. |
| `date` | path | string (date) | Yes | Date (YYYY-MM-DD format) |
| `sequence` | path | integer | Yes | Sequence number. Minimum: 100. |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required)
    - `id` (string)
    - `issueTime` (string (date-time))
    - `cwsu` (string) — Three-letter identifier for a Center Weather Service Unit (CWSU). Allowed values: `ZAB`, `ZAN`, `ZAU`, `ZBW`, `ZDC`, `ZDV`, `ZFA`, `ZFW`, `ZHU`, `ZID`, `ZJX`, `ZKC`, `ZLA`, `ZLC`, `ZMA`, `ZME`, `ZMP`, `ZNY`, `ZOA`, `ZOB`, `ZSE`, `ZTL`.
    - `sequence` (integer) — Minimum: 101.
    - `start` (string (date-time))
    - `end` (string (date-time))
    - `observedProperty` (string)
    - `text` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /aviation/sigmets

Returns a list of SIGMET/AIRMETs

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `start` | query | string (date-time) | No | Start time |
| `end` | query | string (date-time) | No | End time |
| `date` | query | string (date) | No | Date (YYYY-MM-DD format) |
| `atsu` | query | string | No | ATSU identifier. Pattern: `^[A-Z]{3,4}$`. |
| `sequence` | query | string | No | SIGMET sequence number |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `@context` (one of several types)
    - `id` (string (uri))
    - `type` (string, required) — Allowed values: `Feature`.
    - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
      - `type` (string, required) — Allowed values: `Point`.
      - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `LineString`.
      - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `Polygon`.
      - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiPoint`.
      - `coordinates` (array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiLineString`.
      - `coordinates` (array of array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiPolygon`.
      - `coordinates` (array of array of array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `properties` (object, required)
      - `id` (string (uri))
      - `issueTime` (string (date-time))
      - `fir` (string) — May be null.
      - `atsu` (string) — ATSU Identifier. Pattern: `^[A-Z]{3,4}$`.
      - `sequence` (string) — May be null.
      - `phenomenon` (string (uri)) — May be null.
      - `start` (string (date-time))
      - `end` (string (date-time))
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /aviation/sigmets/{atsu}

Returns a list of SIGMET/AIRMETs for the specified ATSU

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `atsu` | path | string | Yes | ATSU identifier. Pattern: `^[A-Z]{3,4}$`. |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `@context` (one of several types)
    - `id` (string (uri))
    - `type` (string, required) — Allowed values: `Feature`.
    - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
      - `type` (string, required) — Allowed values: `Point`.
      - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `LineString`.
      - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `Polygon`.
      - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiPoint`.
      - `coordinates` (array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiLineString`.
      - `coordinates` (array of array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiPolygon`.
      - `coordinates` (array of array of array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `properties` (object, required)
      - `id` (string (uri))
      - `issueTime` (string (date-time))
      - `fir` (string) — May be null.
      - `atsu` (string) — ATSU Identifier. Pattern: `^[A-Z]{3,4}$`.
      - `sequence` (string) — May be null.
      - `phenomenon` (string (uri)) — May be null.
      - `start` (string (date-time))
      - `end` (string (date-time))
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /aviation/sigmets/{atsu}/{date}

Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `atsu` | path | string | Yes | ATSU identifier. Pattern: `^[A-Z]{3,4}$`. |
| `date` | path | string (date) | Yes | Date (YYYY-MM-DD format) |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `@context` (one of several types)
    - `id` (string (uri))
    - `type` (string, required) — Allowed values: `Feature`.
    - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
      - `type` (string, required) — Allowed values: `Point`.
      - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `LineString`.
      - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `Polygon`.
      - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiPoint`.
      - `coordinates` (array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiLineString`.
      - `coordinates` (array of array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `type` (string, required) — Allowed values: `MultiPolygon`.
      - `coordinates` (array of array of array of array of number, required)
      - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `properties` (object, required)
      - `id` (string (uri))
      - `issueTime` (string (date-time))
      - `fir` (string) — May be null.
      - `atsu` (string) — ATSU Identifier. Pattern: `^[A-Z]{3,4}$`.
      - `sequence` (string) — May be null.
      - `phenomenon` (string (uri)) — May be null.
      - `start` (string (date-time))
      - `end` (string (date-time))
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /aviation/sigmets/{atsu}/{date}/{time}

Returns a specific SIGMET/AIRMET

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `atsu` | path | string | Yes | ATSU identifier. Pattern: `^[A-Z]{3,4}$`. |
| `date` | path | string (date) | Yes | Date (YYYY-MM-DD format) |
| `time` | path | string | Yes | Time (HHMM format). This time is always specified in UTC (Zulu) time. Pattern: `^([01][0-9]|2[0-3])[0-5][0-9]$`. |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required)
    - `id` (string (uri))
    - `issueTime` (string (date-time))
    - `fir` (string) — May be null.
    - `atsu` (string) — ATSU Identifier. Pattern: `^[A-Z]{3,4}$`.
    - `sequence` (string) — May be null.
    - `phenomenon` (string (uri)) — May be null.
    - `start` (string (date-time))
    - `end` (string (date-time))
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /glossary

Returns glossary terms

**Responses**

- **200** — A set of glossary terms
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `glossary` (array of object) — A list of glossary terms
    - `term` (string) — The term being defined
    - `definition` (string) — A definition for the term
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /gridpoints/{wfo}/{x},{y}

Returns raw numerical forecast data for a 2.5km grid area

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `wfo` | path | string | Yes | Forecast office ID. Allowed values: `AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, `BUF`, `CAE`, `CAR`, `CHS`, `CLE`, `CTP`, `GSP`, `GYX`, `ILM`, `ILN`, `LWX`, `MHX`, `OKX`, `PBZ`, `PHI`, `RAH`, `RLX`, `RNK`, `ABQ`, `AMA`, `BMX`, `BRO`, `CRP`, `EPZ`, `EWX`, `FFC`, `FWD`, `HGX`, `HUN`, `JAN`, `JAX`, `KEY`, `LCH`, `LIX`, `LUB`, `LZK`, `MAF`, `MEG`, `MFL`, `MLB`, `MOB`, `MRX`, `OHX`, `OUN`, `SHV`, `SJT`, `SJU`, `TAE`, `TBW`, `TSA`, `ABR`, `APX`, `ARX`, `BIS`, `BOU`, `CYS`, `DDC`, `DLH`, `DMX`, `DTX`, `DVN`, `EAX`, `FGF`, `FSD`, `GID`, `GJT`, `GLD`, `GRB`, `GRR`, `ICT`, `ILX`, `IND`, `IWX`, `JKL`, `LBF`, `LMK`, `LOT`, `LSX`, `MKX`, `MPX`, `MQT`, `OAX`, `PAH`, `PUB`, `RIW`, `SGF`, `TOP`, `UNR`, `BOI`, `BYZ`, `EKA`, `FGZ`, `GGW`, `HNX`, `LKN`, `LOX`, `MFR`, `MSO`, `MTR`, `OTX`, `PDT`, `PIH`, `PQR`, `PSR`, `REV`, `SEW`, `SGX`, `SLC`, `STO`, `TFX`, `TWC`, `VEF`, `AER`, `AFC`, `AFG`, `AJK`, `ALU`, `GUM`, `HPA`, `HFO`, `PPG`, `PQE`, `PQW`, `STU`, `NH1`, `NH2`, `ONA`, `ONP`. |
| `x` | path | integer | Yes | Forecast grid X coordinate. Minimum: 0. |
| `y` | path | integer | Yes | Forecast grid Y coordinate. Minimum: 0. |

**Responses**

- **200** — Gridpoint forecast data
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required) — Raw forecast data for a 2.5km grid square. This is a list of all potential data layers that may appear. Some layers may not be present in all areas. * temperature * dewpoint * maxTemperature * minTemperature * relativeHumidity * apparentTemperature * heatIndex * windChill * wetBulbGlobeTemperature * skyCover * windDirection * windSpeed * windGust * weather * hazards: Watch and advisory products in effect * heatRisk * probabilityOfPrecipitation * quantitativePrecipitation * iceAccumulation * snowfallAmount * snowLevel * ceilingHeight * visibility * transportWindSpeed * transportWindDirection * mixingHeight * hainesIndex * lightningActivityLevel * twentyFootWindSpeed * twentyFootWindDirection * waveHeight * wavePeriod * waveDirection * primarySwellHeight * primarySwellDirection * secondarySwellHeight * secondarySwellDirection * wavePeriod2 * windWaveHeight * dispersionIndex * pressure: Barometric pressure * probabilityOfTropicalStormWinds * probabilityOfHurricaneWinds * potentialOf15mphWinds * potentialOf25mphWinds * potentialOf35mphWinds * potentialOf45mphWinds * potentialOf20mphWindGusts * potentialOf30mphWindGusts * potentialOf40mphWindGusts * potentialOf50mphWindGusts * potentialOf60mphWindGusts * grasslandFireDangerIndex * probabilityOfThunder * davisStabilityIndex * atmosphericDispersionIndex * lowVisibilityOccurrenceRiskIndex * stability * redFlagThreatIndex
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `@id` (string (uri))
    - `@type` (string) — Allowed values: `wx:Gridpoint`.
    - `updateTime` (string (date-time))
    - `validTimes` (one of several types) — A time interval in ISO 8601 format. This can be one of: 1. Start and end time 2. Start time and duration 3. Duration and end time The string "NOW" can also be used in place of a start/end time.
    - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `forecastOffice` (string (uri))
    - `gridId` (string)
    - `gridX` (integer) — Minimum: 0.
    - `gridY` (integer) — Minimum: 0.
    - `weather` (object)
      - `values` (array of object, required)
        - `validTime` (one of several types, required) — A time interval in ISO 8601 format. This can be one of: 1. Start and end time 2. Start time and duration 3. Duration and end time The string "NOW" can also be used in place of a start/end time.
        - `value` (array of object, required)
    - `hazards` (object)
      - `values` (array of object, required)
        - `validTime` (one of several types, required) — A time interval in ISO 8601 format. This can be one of: 1. Start and end time 2. Start time and duration 3. Duration and end time The string "NOW" can also be used in place of a start/end time.
        - `value` (array of object, required)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /gridpoints/{wfo}/{x},{y}/forecast

Returns a textual forecast for a 2.5km grid area

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `wfo` | path | string | Yes | Forecast office ID. Allowed values: `AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, `BUF`, `CAE`, `CAR`, `CHS`, `CLE`, `CTP`, `GSP`, `GYX`, `ILM`, `ILN`, `LWX`, `MHX`, `OKX`, `PBZ`, `PHI`, `RAH`, `RLX`, `RNK`, `ABQ`, `AMA`, `BMX`, `BRO`, `CRP`, `EPZ`, `EWX`, `FFC`, `FWD`, `HGX`, `HUN`, `JAN`, `JAX`, `KEY`, `LCH`, `LIX`, `LUB`, `LZK`, `MAF`, `MEG`, `MFL`, `MLB`, `MOB`, `MRX`, `OHX`, `OUN`, `SHV`, `SJT`, `SJU`, `TAE`, `TBW`, `TSA`, `ABR`, `APX`, `ARX`, `BIS`, `BOU`, `CYS`, `DDC`, `DLH`, `DMX`, `DTX`, `DVN`, `EAX`, `FGF`, `FSD`, `GID`, `GJT`, `GLD`, `GRB`, `GRR`, `ICT`, `ILX`, `IND`, `IWX`, `JKL`, `LBF`, `LMK`, `LOT`, `LSX`, `MKX`, `MPX`, `MQT`, `OAX`, `PAH`, `PUB`, `RIW`, `SGF`, `TOP`, `UNR`, `BOI`, `BYZ`, `EKA`, `FGZ`, `GGW`, `HNX`, `LKN`, `LOX`, `MFR`, `MSO`, `MTR`, `OTX`, `PDT`, `PIH`, `PQR`, `PSR`, `REV`, `SEW`, `SGX`, `SLC`, `STO`, `TFX`, `TWC`, `VEF`, `AER`, `AFC`, `AFG`, `AJK`, `ALU`, `GUM`, `HPA`, `HFO`, `PPG`, `PQE`, `PQW`, `STU`, `NH1`, `NH2`, `ONA`, `ONP`. |
| `x` | path | integer | Yes | Forecast grid X coordinate. Minimum: 0. |
| `y` | path | integer | Yes | Forecast grid Y coordinate. Minimum: 0. |
| `Feature-Flags` | header | array of string | No | Enable future and experimental features (see documentation for more info): * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue |
| `units` | query | string | No | Use US customary or SI (metric) units in textual output. Allowed values: `us`, `si`. Default: `us`. |

**Responses**

- **200** — A forecast for a gridpoint.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required) — A multi-day forecast for a 2.5km grid square.
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `units` (string) — Denotes the units used in the textual portions of the forecast. Allowed values: `us`, `si`. Default: `us`.
    - `forecastGenerator` (string) — The internal generator class used to create the forecast text (used for NWS debugging).
    - `generatedAt` (string (date-time)) — The time this forecast data was generated.
    - `updateTime` (string (date-time)) — The last update time of the data this forecast was generated from.
    - `validTimes` (one of several types) — A time interval in ISO 8601 format. This can be one of: 1. Start and end time 2. Start time and duration 3. Duration and end time The string "NOW" can also be used in place of a start/end time.
    - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `periods` (array of object) — An array of forecast periods.
      - `number` (integer) — Sequential period number. Minimum: 1.
      - `name` (string) — A textual identifier for the period. This value will not be present for hourly forecasts.
      - `startTime` (string (date-time)) — The starting time that this forecast period is valid for.
      - `endTime` (string (date-time)) — The ending time that this forecast period is valid for.
      - `isDaytime` (boolean) — Indicates whether this period is daytime or nighttime.
      - `temperature` (one of several types) — High/low temperature for the period, depending on whether the period is day or night. This property as an integer value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the "forecast_temperature_qv" feature flag on the request.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `temperatureUnit` (string) — The unit of the temperature value (Fahrenheit or Celsius). This property is deprecated. Future versions will indicate the unit within the quantitative value object for the temperature property. To make use of the future standard format now, set the "forecast_temperature_qv" feature flag on the request. Allowed values: `F`, `C`.
      - `temperatureTrend` (string) — If not null, indicates a non-diurnal temperature trend for the period (either rising temperature overnight, or falling temperature during the day). Allowed values: `rising`, `falling`. May be null.
      - `probabilityOfPrecipitation` (object) — Probability of precipitation for the period.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windSpeed` (one of several types) — Wind speed for the period. This property as an string value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the "forecast_wind_speed_qv" feature flag on the request.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windGust` (one of several types) — Peak wind gust for the period. This property as an string value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the "forecast_wind_speed_qv" feature flag on the request. May be null.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windDirection` (string) — The prevailing direction of the wind for the period, using a 16-point compass. Allowed values: `N`, `NNE`, `NE`, `ENE`, `E`, `ESE`, `SE`, `SSE`, `S`, `SSW`, `SW`, `WSW`, `W`, `WNW`, `NW`, `NNW`.
      - `icon` (string (uri)) — A link to an icon representing the forecast summary.
      - `shortForecast` (string) — A brief textual forecast summary for the period.
      - `detailedForecast` (string) — A detailed textual forecast for the period.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /gridpoints/{wfo}/{x},{y}/forecast/hourly

Returns a textual hourly forecast for a 2.5km grid area

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `wfo` | path | string | Yes | Forecast office ID. Allowed values: `AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, `BUF`, `CAE`, `CAR`, `CHS`, `CLE`, `CTP`, `GSP`, `GYX`, `ILM`, `ILN`, `LWX`, `MHX`, `OKX`, `PBZ`, `PHI`, `RAH`, `RLX`, `RNK`, `ABQ`, `AMA`, `BMX`, `BRO`, `CRP`, `EPZ`, `EWX`, `FFC`, `FWD`, `HGX`, `HUN`, `JAN`, `JAX`, `KEY`, `LCH`, `LIX`, `LUB`, `LZK`, `MAF`, `MEG`, `MFL`, `MLB`, `MOB`, `MRX`, `OHX`, `OUN`, `SHV`, `SJT`, `SJU`, `TAE`, `TBW`, `TSA`, `ABR`, `APX`, `ARX`, `BIS`, `BOU`, `CYS`, `DDC`, `DLH`, `DMX`, `DTX`, `DVN`, `EAX`, `FGF`, `FSD`, `GID`, `GJT`, `GLD`, `GRB`, `GRR`, `ICT`, `ILX`, `IND`, `IWX`, `JKL`, `LBF`, `LMK`, `LOT`, `LSX`, `MKX`, `MPX`, `MQT`, `OAX`, `PAH`, `PUB`, `RIW`, `SGF`, `TOP`, `UNR`, `BOI`, `BYZ`, `EKA`, `FGZ`, `GGW`, `HNX`, `LKN`, `LOX`, `MFR`, `MSO`, `MTR`, `OTX`, `PDT`, `PIH`, `PQR`, `PSR`, `REV`, `SEW`, `SGX`, `SLC`, `STO`, `TFX`, `TWC`, `VEF`, `AER`, `AFC`, `AFG`, `AJK`, `ALU`, `GUM`, `HPA`, `HFO`, `PPG`, `PQE`, `PQW`, `STU`, `NH1`, `NH2`, `ONA`, `ONP`. |
| `x` | path | integer | Yes | Forecast grid X coordinate. Minimum: 0. |
| `y` | path | integer | Yes | Forecast grid Y coordinate. Minimum: 0. |
| `Feature-Flags` | header | array of string | No | Enable future and experimental features (see documentation for more info): * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue |
| `units` | query | string | No | Use US customary or SI (metric) units in textual output. Allowed values: `us`, `si`. Default: `us`. |

**Responses**

- **200** — A forecast for a gridpoint.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required) — An hourly forecast for a 2.5km grid square.
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `units` (string) — Denotes the units used in the textual portions of the forecast. Allowed values: `us`, `si`. Default: `us`.
    - `forecastGenerator` (string) — The internal generator class used to create the forecast text (used for NWS debugging).
    - `generatedAt` (string (date-time)) — The time this forecast data was generated.
    - `updateTime` (string (date-time)) — The last update time of the data this forecast was generated from.
    - `validTimes` (one of several types) — A time interval in ISO 8601 format. This can be one of: 1. Start and end time 2. Start time and duration 3. Duration and end time The string "NOW" can also be used in place of a start/end time.
    - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `periods` (array of object) — An array of forecast periods.
      - `number` (integer) — Sequential period number. Minimum: 1.
      - `name` (string) — A textual identifier for the period. This value will not be present for hourly forecasts.
      - `startTime` (string (date-time)) — The starting time that this forecast period is valid for.
      - `endTime` (string (date-time)) — The ending time that this forecast period is valid for.
      - `isDaytime` (boolean) — Indicates whether this period is daytime or nighttime.
      - `temperature` (one of several types) — High/low temperature for the period, depending on whether the period is day or night. This property as an integer value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the "forecast_temperature_qv" feature flag on the request.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `temperatureUnit` (string) — The unit of the temperature value (Fahrenheit or Celsius). This property is deprecated. Future versions will indicate the unit within the quantitative value object for the temperature property. To make use of the future standard format now, set the "forecast_temperature_qv" feature flag on the request. Allowed values: `F`, `C`.
      - `temperatureTrend` (string) — If not null, indicates a non-diurnal temperature trend for the period (either rising temperature overnight, or falling temperature during the day). Allowed values: `rising`, `falling`. May be null.
      - `probabilityOfPrecipitation` (object) — Probability of precipitation for the period.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `dewpoint` (object) — Dewpoint. Only provided in hourly forecasts.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `relativeHumidity` (object) — Relative humidity. Only provided in hourly forecasts.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windSpeed` (one of several types) — Wind speed for the period. This property as an string value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the "forecast_wind_speed_qv" feature flag on the request.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windGust` (one of several types) — Peak wind gust for the period. This property as an string value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the "forecast_wind_speed_qv" feature flag on the request. May be null.
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windDirection` (string) — The prevailing direction of the wind for the period, using a 16-point compass. Allowed values: `N`, `NNE`, `NE`, `ENE`, `E`, `ESE`, `SE`, `SSE`, `S`, `SSW`, `SW`, `WSW`, `W`, `WNW`, `NW`, `NNW`.
      - `icon` (string (uri)) — A link to an icon representing the forecast summary.
      - `shortForecast` (string) — A brief textual forecast summary for the period.
      - `detailedForecast` (string) — A detailed textual forecast for the period.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /gridpoints/{wfo}/{x},{y}/stations

Returns a list of observation stations usable for a given 2.5km grid area

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `wfo` | path | string | Yes | Forecast office ID. Allowed values: `AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, `BUF`, `CAE`, `CAR`, `CHS`, `CLE`, `CTP`, `GSP`, `GYX`, `ILM`, `ILN`, `LWX`, `MHX`, `OKX`, `PBZ`, `PHI`, `RAH`, `RLX`, `RNK`, `ABQ`, `AMA`, `BMX`, `BRO`, `CRP`, `EPZ`, `EWX`, `FFC`, `FWD`, `HGX`, `HUN`, `JAN`, `JAX`, `KEY`, `LCH`, `LIX`, `LUB`, `LZK`, `MAF`, `MEG`, `MFL`, `MLB`, `MOB`, `MRX`, `OHX`, `OUN`, `SHV`, `SJT`, `SJU`, `TAE`, `TBW`, `TSA`, `ABR`, `APX`, `ARX`, `BIS`, `BOU`, `CYS`, `DDC`, `DLH`, `DMX`, `DTX`, `DVN`, `EAX`, `FGF`, `FSD`, `GID`, `GJT`, `GLD`, `GRB`, `GRR`, `ICT`, `ILX`, `IND`, `IWX`, `JKL`, `LBF`, `LMK`, `LOT`, `LSX`, `MKX`, `MPX`, `MQT`, `OAX`, `PAH`, `PUB`, `RIW`, `SGF`, `TOP`, `UNR`, `BOI`, `BYZ`, `EKA`, `FGZ`, `GGW`, `HNX`, `LKN`, `LOX`, `MFR`, `MSO`, `MTR`, `OTX`, `PDT`, `PIH`, `PQR`, `PSR`, `REV`, `SEW`, `SGX`, `SLC`, `STO`, `TFX`, `TWC`, `VEF`, `AER`, `AFC`, `AFG`, `AJK`, `ALU`, `GUM`, `HPA`, `HFO`, `PPG`, `PQE`, `PQW`, `STU`, `NH1`, `NH2`, `ONA`, `ONP`. |
| `x` | path | integer | Yes | Forecast grid X coordinate. Minimum: 0. |
| `y` | path | integer | Yes | Forecast grid Y coordinate. Minimum: 0. |
| `limit` | query | integer | No | Limit. Default: `500`. Minimum: 1. Maximum: 500. |

**Responses**

- **200** — A collection of observation stations.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object)
      - `@context` (one of several types)
      - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
      - `@id` (string (uri))
      - `@type` (string) — Allowed values: `wx:ObservationStation`.
      - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `stationIdentifier` (string)
      - `name` (string)
      - `timeZone` (string (iana-time-zone-identifier))
      - `provider` (string) — The data provider for this station. E.g., "ASOS," "MesoWest," etc.
      - `subProvider` (string) — The sub-provider of for this station. E.g., "FAA," "DOT," etc.
      - `forecast` (string (uri)) — A link to the NWS public forecast zone containing this station.
      - `county` (string (uri)) — A link to the NWS county zone containing this station.
      - `fireWeatherZone` (string (uri)) — A link to the NWS fire weather forecast zone containing this station.
      - `distance` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `bearing` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
  - `observationStations` (array of string (uri))
  - `pagination` (object) — Links for retrieving more data from paged data sets
    - `next` (string (uri), required) — A link to the next page of records
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /icons/{set}/{timeOfDay}/{first}

Returns a forecast icon. Icon services in API are deprecated.

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `set` | path | string | Yes | . |
| `timeOfDay` | path | string | Yes | . |
| `first` | path | string | Yes | . |
| `size` | query | one of several types | No | Font size |
| `fontsize` | query | integer | No | Font size. Minimum: 2. Maximum: 24. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /icons/{set}/{timeOfDay}/{first}/{second}

Returns a forecast icon. Icon services in API are deprecated.

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `set` | path | string | Yes | . |
| `timeOfDay` | path | string | Yes | . |
| `first` | path | string | Yes | . |
| `second` | path | string | Yes | . |
| `size` | query | one of several types | No | Font size |
| `fontsize` | query | integer | No | Font size. Minimum: 2. Maximum: 24. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /icons

Returns a list of icon codes and textual descriptions. Icon services in API are deprecated.

> Deprecated.

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `icons` (object, required)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /thumbnails/satellite/{area}

Returns a thumbnail image for a satellite region. Image services in API are deprecated.

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `area` | path | string | Yes | . Allowed values: `a`, `e`, `g`, `h`, `p`, `s`, `w`. |

**Responses**

- **200** — An image file
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /stations/{stationId}/observations

Returns a list of observations for a given station

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Observation station ID |
| `start` | query | string (date-time) | No | Start time |
| `end` | query | string (date-time) | No | End time |
| `cursor` | query | string | No | Pagination cursor |
| `limit` | query | integer | No | Limit. Minimum: 1. Maximum: 500. |

**Responses**

- **200** — A collection of observation records.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object)
      - `@context` (one of several types)
      - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
      - `@id` (string (uri))
      - `@type` (string) — Allowed values: `wx:ObservationStation`.
      - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `station` (string (uri))
      - `stationId` (string)
      - `stationName` (string)
      - `timestamp` (string (date-time))
      - `rawMessage` (string)
      - `textDescription` (string)
      - `icon` (string (uri)) — May be null.
      - `presentWeather` (array of object)
        - `intensity` (string, required) — Allowed values: `light`, `heavy`. May be null.
        - `modifier` (string, required) — Allowed values: `patches`, `blowing`, `low_drifting`, `freezing`, `shallow`, `partial`, `showers`. May be null.
        - `weather` (string, required) — Allowed values: `fog_mist`, `dust_storm`, `dust`, `drizzle`, `funnel_cloud`, `fog`, `smoke`, `hail`, `snow_pellets`, `haze`, `ice_crystals`, `ice_pellets`, `dust_whirls`, `spray`, `rain`, `sand`, `snow_grains`, `snow`, `squalls`, `sand_storm`, `thunderstorms`, `unknown`, `volcanic_ash`.
        - `rawString` (string, required)
        - `inVicinity` (boolean)
      - `temperature` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `dewpoint` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windDirection` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windSpeed` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windGust` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `barometricPressure` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `seaLevelPressure` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `visibility` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `maxTemperatureLast24Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `minTemperatureLast24Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `precipitationLastHour` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `precipitationLast3Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `precipitationLast6Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `relativeHumidity` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windChill` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `heatIndex` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `cloudLayers` (array of object) — May be null.
        - `base` (object, required) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `amount` (string, required) — Allowed values: `OVC`, `BKN`, `SCT`, `FEW`, `SKC`, `CLR`, `VV`.
  - `pagination` (object) — Links for retrieving more data from paged data sets
    - `next` (string (uri), required) — A link to the next page of records
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /stations/{stationId}/observations/latest

Returns the latest observation for a station

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Observation station ID |
| `require_qc` | query | boolean | No | Require QC |

**Responses**

- **200** — An observation record.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required)
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `@id` (string (uri))
    - `@type` (string) — Allowed values: `wx:ObservationStation`.
    - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `station` (string (uri))
    - `stationId` (string)
    - `stationName` (string)
    - `timestamp` (string (date-time))
    - `rawMessage` (string)
    - `textDescription` (string)
    - `icon` (string (uri)) — May be null.
    - `presentWeather` (array of object)
      - `intensity` (string, required) — Allowed values: `light`, `heavy`. May be null.
      - `modifier` (string, required) — Allowed values: `patches`, `blowing`, `low_drifting`, `freezing`, `shallow`, `partial`, `showers`. May be null.
      - `weather` (string, required) — Allowed values: `fog_mist`, `dust_storm`, `dust`, `drizzle`, `funnel_cloud`, `fog`, `smoke`, `hail`, `snow_pellets`, `haze`, `ice_crystals`, `ice_pellets`, `dust_whirls`, `spray`, `rain`, `sand`, `snow_grains`, `snow`, `squalls`, `sand_storm`, `thunderstorms`, `unknown`, `volcanic_ash`.
      - `rawString` (string, required)
      - `inVicinity` (boolean)
    - `temperature` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `dewpoint` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `windDirection` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `windSpeed` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `windGust` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `barometricPressure` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `seaLevelPressure` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `visibility` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `maxTemperatureLast24Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `minTemperatureLast24Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `precipitationLastHour` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `precipitationLast3Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `precipitationLast6Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `relativeHumidity` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `windChill` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `heatIndex` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `cloudLayers` (array of object) — May be null.
      - `base` (object, required) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `amount` (string, required) — Allowed values: `OVC`, `BKN`, `SCT`, `FEW`, `SKC`, `CLR`, `VV`.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /stations/{stationId}/observations/{time}

Returns a single observation.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Observation station ID |
| `time` | path | string (date-time) | Yes | Timestamp of requested observation |

**Responses**

- **200** — An observation record.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required)
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `@id` (string (uri))
    - `@type` (string) — Allowed values: `wx:ObservationStation`.
    - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `station` (string (uri))
    - `stationId` (string)
    - `stationName` (string)
    - `timestamp` (string (date-time))
    - `rawMessage` (string)
    - `textDescription` (string)
    - `icon` (string (uri)) — May be null.
    - `presentWeather` (array of object)
      - `intensity` (string, required) — Allowed values: `light`, `heavy`. May be null.
      - `modifier` (string, required) — Allowed values: `patches`, `blowing`, `low_drifting`, `freezing`, `shallow`, `partial`, `showers`. May be null.
      - `weather` (string, required) — Allowed values: `fog_mist`, `dust_storm`, `dust`, `drizzle`, `funnel_cloud`, `fog`, `smoke`, `hail`, `snow_pellets`, `haze`, `ice_crystals`, `ice_pellets`, `dust_whirls`, `spray`, `rain`, `sand`, `snow_grains`, `snow`, `squalls`, `sand_storm`, `thunderstorms`, `unknown`, `volcanic_ash`.
      - `rawString` (string, required)
      - `inVicinity` (boolean)
    - `temperature` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `dewpoint` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `windDirection` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `windSpeed` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `windGust` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `barometricPressure` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `seaLevelPressure` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `visibility` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `maxTemperatureLast24Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `minTemperatureLast24Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `precipitationLastHour` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `precipitationLast3Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `precipitationLast6Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `relativeHumidity` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `windChill` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `heatIndex` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `cloudLayers` (array of object) — May be null.
      - `base` (object, required) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `amount` (string, required) — Allowed values: `OVC`, `BKN`, `SCT`, `FEW`, `SKC`, `CLR`, `VV`.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /stations/{stationId}/tafs

Returns Terminal Aerodrome Forecasts for the specified airport station.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Observation station ID |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /stations/{stationId}/tafs/{date}/{time}

Returns a single Terminal Aerodrome Forecast.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Observation station ID |
| `date` | path | string (date) | Yes | Date (YYYY-MM-DD format) |
| `time` | path | string | Yes | Time (HHMM format). This time is always specified in UTC (Zulu) time. Pattern: `^([01][0-9]|2[0-3])[0-5][0-9]$`. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /stations

Returns a list of observation stations.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | query | array of string | No | Filter by observation station ID |
| `state` | query | array of one of several types | No | Filter by state/marine area code |
| `limit` | query | integer | No | Limit. Default: `500`. Minimum: 1. Maximum: 500. |
| `cursor` | query | string | No | Pagination cursor |

**Responses**

- **200** — A collection of observation stations.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object)
      - `@context` (one of several types)
      - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
      - `@id` (string (uri))
      - `@type` (string) — Allowed values: `wx:ObservationStation`.
      - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `stationIdentifier` (string)
      - `name` (string)
      - `timeZone` (string (iana-time-zone-identifier))
      - `provider` (string) — The data provider for this station. E.g., "ASOS," "MesoWest," etc.
      - `subProvider` (string) — The sub-provider of for this station. E.g., "FAA," "DOT," etc.
      - `forecast` (string (uri)) — A link to the NWS public forecast zone containing this station.
      - `county` (string (uri)) — A link to the NWS county zone containing this station.
      - `fireWeatherZone` (string (uri)) — A link to the NWS fire weather forecast zone containing this station.
      - `distance` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `bearing` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
  - `observationStations` (array of string (uri))
  - `pagination` (object) — Links for retrieving more data from paged data sets
    - `next` (string (uri), required) — A link to the next page of records
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /stations/{stationId}

Returns metadata about a given observation station

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Observation station ID |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required)
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `@id` (string (uri))
    - `@type` (string) — Allowed values: `wx:ObservationStation`.
    - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `stationIdentifier` (string)
    - `name` (string)
    - `timeZone` (string (iana-time-zone-identifier))
    - `provider` (string) — The data provider for this station. E.g., "ASOS," "MesoWest," etc.
    - `subProvider` (string) — The sub-provider of for this station. E.g., "FAA," "DOT," etc.
    - `forecast` (string (uri)) — A link to the NWS public forecast zone containing this station.
    - `county` (string (uri)) — A link to the NWS county zone containing this station.
    - `fireWeatherZone` (string (uri)) — A link to the NWS fire weather forecast zone containing this station.
    - `distance` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
    - `bearing` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `value` (number) — A measured value. May be null.
      - `maxValue` (number) — The maximum value of a range of measured values
      - `minValue` (number) — The minimum value of a range of measured values
      - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
      - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /offices/{officeId}

Returns metadata about a NWS forecast office

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `officeId` | path | one of several types | Yes | NWS office ID |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@type` (string) — Allowed values: `GovernmentOrganization`.
  - `@id` (string (uri))
  - `id` (string)
  - `name` (string)
  - `address` (object)
    - `@type` (string) — Allowed values: `PostalAddress`.
    - `streetAddress` (string)
    - `addressLocality` (string)
    - `addressRegion` (string)
    - `postalCode` (string)
  - `telephone` (string)
  - `faxNumber` (string)
  - `email` (string)
  - `sameAs` (string (uri))
  - `nwsRegion` (string)
  - `parentOrganization` (string (uri))
  - `responsibleCounties` (array of string (uri))
  - `responsibleForecastZones` (array of string (uri))
  - `responsibleFireZones` (array of string (uri))
  - `approvedObservationStations` (array of string (uri))
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /offices/{officeId}/briefing

Returns active briefing for an NWS office

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `officeId` | path | one of several types | Yes | NWS office ID |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `id` (string (uuid))
  - `startTime` (string (date-time)) — The time when the document becomes active. ISO8601 datetime.
  - `endTime` (string (date-time)) — The time when the document becomes inactive. ISO8601 datetime.
  - `updateTime` (string (date-time)) — When the document was last updated. ISO8601 datetime.
  - `title` (string) — A short title. Max length: 50.
  - `description` (string) — A longer description and/or caption.
  - `priority` (boolean) — An indicator that a weather story should be emphasized.
  - `download` (string (uri)) — The URL of the media content for the weather story.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /offices/{officeId}/briefing/download/latest

Returns the latest briefing for an office

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `officeId` | path | one of several types | Yes | NWS office ID |

**Responses**

- **302** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /offices/{officeId}/briefing/download/{briefingId}

Returns a briefing for an office

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `officeId` | path | one of several types | Yes | NWS office ID |
| `briefingId` | path | string | Yes | . |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /offices/{officeId}/headlines/{headlineId}

Returns a specific news headline for a given NWS office

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `officeId` | path | one of several types | Yes | NWS office ID |
| `headlineId` | path | string | Yes | Headline record ID |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@id` (string (uri))
  - `id` (string)
  - `office` (string (uri))
  - `important` (boolean)
  - `issuanceTime` (string (date-time))
  - `link` (string (uri))
  - `name` (string)
  - `title` (string)
  - `summary` (string) — May be null.
  - `content` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /offices/{officeId}/headlines

Returns a list of news headlines for a given NWS office

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `officeId` | path | one of several types | Yes | NWS office ID |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types, required)
  - `@graph` (array of object, required)
    - `@context` (one of several types)
    - `@id` (string (uri))
    - `id` (string)
    - `office` (string (uri))
    - `important` (boolean)
    - `issuanceTime` (string (date-time))
    - `link` (string (uri))
    - `name` (string)
    - `title` (string)
    - `summary` (string) — May be null.
    - `content` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /offices/{officeId}/weatherstories

Returns active weather stories for an NWS office

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `officeId` | path | one of several types | Yes | NWS office ID |

**Responses**

- **200** — success
  Body (`application/ld+json`, array of object):
  - `id` (string (uuid))
  - `startTime` (string (date-time), required) — The time when the document becomes active. ISO8601 datetime.
  - `endTime` (string (date-time), required) — The time when the document becomes inactive. ISO8601 datetime.
  - `updateTime` (string (date-time), required) — When the document was last updated. ISO8601 datetime.
  - `title` (string, required) — A short title. Max length: 50.
  - `description` (string, required) — A longer description and/or caption.
  - `priority` (boolean, required) — An indicator that a weather story should be emphasized.
  - `download` (string (uri), required) — The URL of the media content for the weather story.
  - `altText` (string, required) — Alternative text description of the content of the image for assistive technology.
  - `order` (integer, required) — The order in which a weather story should be displayed. Unique for each object. Minimum: 1. Maximum: 7.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /offices/{officeId}/weatherstories/download/{imageId}

Returns the image for a weather story

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `officeId` | path | one of several types | Yes | NWS office ID |
| `imageId` | path | string | Yes | . |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /points/{latitude},{longitude}

Returns metadata about a given latitude/longitude point

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `latitude` | path | number | Yes | Latitude. Minimum: -90. Maximum: 90. Multiple of 0.0001. |
| `longitude` | path | number | Yes | Longitude. Minimum: -180. Maximum: 180. Multiple of 0.0001. |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required)
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `@id` (string (uri))
    - `@type` (string) — Allowed values: `wx:Point`.
    - `cwa` (string) — Three-letter identifier for a NWS office. Allowed values: `AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, `BUF`, `CAE`, `CAR`, `CHS`, `CLE`, `CTP`, `GSP`, `GYX`, `ILM`, `ILN`, `LWX`, `MHX`, `OKX`, `PBZ`, `PHI`, `RAH`, `RLX`, `RNK`, `ABQ`, `AMA`, `BMX`, `BRO`, `CRP`, `EPZ`, `EWX`, `FFC`, `FWD`, `HGX`, `HUN`, `JAN`, `JAX`, `KEY`, `LCH`, `LIX`, `LUB`, `LZK`, `MAF`, `MEG`, `MFL`, `MLB`, `MOB`, `MRX`, `OHX`, `OUN`, `SHV`, `SJT`, `SJU`, `TAE`, `TBW`, `TSA`, `ABR`, `APX`, `ARX`, `BIS`, `BOU`, `CYS`, `DDC`, `DLH`, `DMX`, `DTX`, `DVN`, `EAX`, `FGF`, `FSD`, `GID`, `GJT`, `GLD`, `GRB`, `GRR`, `ICT`, `ILX`, `IND`, `IWX`, `JKL`, `LBF`, `LMK`, `LOT`, `LSX`, `MKX`, `MPX`, `MQT`, `OAX`, `PAH`, `PUB`, `RIW`, `SGF`, `TOP`, `UNR`, `BOI`, `BYZ`, `EKA`, `FGZ`, `GGW`, `HNX`, `LKN`, `LOX`, `MFR`, `MSO`, `MTR`, `OTX`, `PDT`, `PIH`, `PQR`, `PSR`, `REV`, `SEW`, `SGX`, `SLC`, `STO`, `TFX`, `TWC`, `VEF`, `AER`, `AFC`, `AFG`, `AJK`, `ALU`, `GUM`, `HPA`, `HFO`, `PPG`, `PQE`, `PQW`, `STU`, `NH1`, `NH2`, `ONA`, `ONP`.
    - `type` (string) — Whether the specific point is on land or marine. Allowed values: `land`, `marine`.
    - `forecastOffice` (string (uri))
    - `gridId` (string) — Three-letter identifier for a NWS office. Allowed values: `AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, `BUF`, `CAE`, `CAR`, `CHS`, `CLE`, `CTP`, `GSP`, `GYX`, `ILM`, `ILN`, `LWX`, `MHX`, `OKX`, `PBZ`, `PHI`, `RAH`, `RLX`, `RNK`, `ABQ`, `AMA`, `BMX`, `BRO`, `CRP`, `EPZ`, `EWX`, `FFC`, `FWD`, `HGX`, `HUN`, `JAN`, `JAX`, `KEY`, `LCH`, `LIX`, `LUB`, `LZK`, `MAF`, `MEG`, `MFL`, `MLB`, `MOB`, `MRX`, `OHX`, `OUN`, `SHV`, `SJT`, `SJU`, `TAE`, `TBW`, `TSA`, `ABR`, `APX`, `ARX`, `BIS`, `BOU`, `CYS`, `DDC`, `DLH`, `DMX`, `DTX`, `DVN`, `EAX`, `FGF`, `FSD`, `GID`, `GJT`, `GLD`, `GRB`, `GRR`, `ICT`, `ILX`, `IND`, `IWX`, `JKL`, `LBF`, `LMK`, `LOT`, `LSX`, `MKX`, `MPX`, `MQT`, `OAX`, `PAH`, `PUB`, `RIW`, `SGF`, `TOP`, `UNR`, `BOI`, `BYZ`, `EKA`, `FGZ`, `GGW`, `HNX`, `LKN`, `LOX`, `MFR`, `MSO`, `MTR`, `OTX`, `PDT`, `PIH`, `PQR`, `PSR`, `REV`, `SEW`, `SGX`, `SLC`, `STO`, `TFX`, `TWC`, `VEF`, `AER`, `AFC`, `AFG`, `AJK`, `ALU`, `GUM`, `HPA`, `HFO`, `PPG`, `PQE`, `PQW`, `STU`, `NH1`, `NH2`, `ONA`, `ONP`.
    - `gridX` (integer) — Minimum: 0.
    - `gridY` (integer) — Minimum: 0.
    - `forecast` (string (uri))
    - `forecastHourly` (string (uri))
    - `forecastGridData` (string (uri))
    - `observationStations` (string (uri))
    - `relativeLocation` (one of several types)
      - `@context` (one of several types)
      - `id` (string (uri))
      - `type` (string, required) — Allowed values: `Feature`.
      - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
        - `type` (string, required) — Allowed values: `Point`.
        - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
        - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
        - `type` (string, required) — Allowed values: `LineString`.
        - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
        - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
        - `type` (string, required) — Allowed values: `Polygon`.
        - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
        - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
        - `type` (string, required) — Allowed values: `MultiPoint`.
        - `coordinates` (array of array of number, required)
        - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
        - `type` (string, required) — Allowed values: `MultiLineString`.
        - `coordinates` (array of array of array of number, required)
        - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
        - `type` (string, required) — Allowed values: `MultiPolygon`.
        - `coordinates` (array of array of array of array of number, required)
        - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
      - `properties` (object, required)
        - `city` (string)
        - `state` (string)
        - `distance` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `bearing` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
      - `city` (string)
      - `state` (string)
      - `distance` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `bearing` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `geometry` (string (wkt), required) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `forecastZone` (string (uri))
    - `county` (string (uri))
    - `fireWeatherZone` (string (uri))
    - `timeZone` (string)
    - `radarStation` (string)
    - `astronomicalData` (object) — An object representing sunrise, sunset, and twilight information for a location.
      - `sunrise` (string (date-time)) — The timestamp of sunrise, defined as when the sun angle is 90°35' from vertical. May be null.
      - `sunset` (string (date-time)) — The timestamp of sunset, defined as when the sun angle is 90°35' from vertical. May be null.
      - `transit` (string (date-time)) — The timestamp when the sun reaches its zenith. May be null.
      - `civilTwilightBegin` (string (date-time)) — The timestamp of the onset of civil twilight, defined as when the sun angle is 96° from vertical. This is the beginning of civil dawn and lasts until sunrise. May be null.
      - `civilTwilightEnd` (string (date-time)) — The timestamp of the end of civil twilight, defined as when the sun angle is 96° from vertical. This is the end of civil dusk, which begins at sunset. May be null.
      - `nauticalTwilightBegin` (string (date-time)) — The timestamp of the onset of nautical twilight, defined as when the sun angle is 102° from vertical. This is the beginning of nautical dawn and lasts until the civil dawn. May be null.
      - `nauticalTwilightEnd` (string (date-time)) — The timestamp of the end of nautical twilight, defined as when the sun angle is 102° from vertical. This is the end of nautical dusk, which begins at the end of civil twilight. May be null.
      - `astronomicalTwilightBegin` (string (date-time)) — The timestamp of the onset of astronomical twilight, defined as when the sun angle is 108° from vertical. This is the beginning of astronomical dawn and lasts until the nautical dawn. May be null.
      - `astronomicalTwilightEnd` (string (date-time)) — The timestamp of the end of astronomical twilight, defined as when the sun angle is 108° from vertical. This is the end of astronomical dusk, which begins at the end of nautical twilight. May be null.
    - `nwr` (object) — NOAA Weather Radio metadata for this point
      - `transmitter` (string) — Transmitter callsign. May be null.
      - `sameCode` (string) — The SAME code of this point's county
      - `areaBroadcast` (string (uri)) — A link to the area NWR broadcast from this transmitter. May be null.
      - `pointBroadcast` (string (uri)) — A link to the local NWR broadcast for this point. May be null.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /points/{latitude},{longitude}/radio

Returns NOAA Weather Radio broadcast script for a latitude/longitude point

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `latitude` | path | number | Yes | Latitude. Minimum: -90. Maximum: 90. Multiple of 0.0001. |
| `longitude` | path | number | Yes | Longitude. Minimum: -180. Maximum: 180. Multiple of 0.0001. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /points/{latitude},{longitude}/stations

Returns a list of observation stations for a given point

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `latitude` | path | number | Yes | Latitude. Minimum: -90. Maximum: 90. Multiple of 0.0001. |
| `longitude` | path | number | Yes | Longitude. Minimum: -180. Maximum: 180. Multiple of 0.0001. |

**Responses**

- **301** — redirect to gridpoint stations
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radar/servers

Returns a list of radar servers

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `reportingHost` | query | string | No | Show records from specific reporting host |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radar/servers/{id}

Returns metadata about a given radar server

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | Server ID |
| `reportingHost` | query | string | No | Show records from specific reporting host |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radar/spgds

Returns a list of radar spgds

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `published` | query | one of several types | No | Range for publish time |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radar/stations

Returns a list of radar stations

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationType` | query | array of string | No | Limit results to a specific station type or types |
| `reportingHost` | query | string | No | Show RDA and latency info from specific reporting host |
| `host` | query | string | No | Show latency info from specific LDM host |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radar/stations/{stationId}

Returns metadata about a given radar station

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Radar station ID |
| `reportingHost` | query | string | No | Show RDA and latency info from specific reporting host |
| `host` | query | string | No | Show latency info from specific LDM host |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radar/stations/{stationId}/alarms

Returns metadata about a given radar station alarms

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Radar station ID |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radar/queues/{host}

Returns metadata about a given radar queue

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `host` | path | string | Yes | LDM host. Allowed values: `rds`, `tds`. |
| `limit` | query | integer | No | Record limit. Minimum: 1. Maximum: 50000. |
| `arrived` | query | one of several types | No | Range for arrival time |
| `created` | query | one of several types | No | Range for creation time |
| `published` | query | one of several types | No | Range for publish time |
| `station` | query | string | No | Station identifier |
| `type` | query | string | No | Record type |
| `feed` | query | string | No | Originating product feed |
| `resolution` | query | integer | No | Resolution version. Minimum: 1. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radar/profilers/{stationId}

Returns metadata about a given radar wind profiler

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `stationId` | path | string | Yes | Profiler station ID |
| `time` | query | one of several types | No | Time interval |
| `interval` | query | string | No | Averaging interval. Pattern: `^P(\d+Y)?(\d+M)?(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?)?$`. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radio

Returns a collection of transmitters

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `cursor` | query | string | No | Pagination cursor |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radio/{callSign}

Returns a single transmitter

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `callSign` | path | string | Yes | The call sign identifier for a NOAA transmitter station. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /radio/{callSign}/broadcast

Returns NOAA Weather Radio broadcast script for a transmitter

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `callSign` | path | string | Yes | The call sign identifier for a NOAA transmitter station. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products

Returns a list of text products

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `location` | query | array of string | No | Location id |
| `start` | query | string (date-time) | No | Start time |
| `end` | query | string (date-time) | No | End time |
| `office` | query | array of string | No | Issuing office |
| `wmoid` | query | array of string | No | WMO id code |
| `type` | query | array of string | No | Product code |
| `limit` | query | integer | No | Limit. Minimum: 1. Maximum: 500. |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@graph` (array of object)
    - `@context` (one of several types)
    - `@id` (string (uri))
    - `id` (string)
    - `wmoCollectiveId` (string)
    - `issuingOffice` (string)
    - `issuanceTime` (string (date-time))
    - `productCode` (string)
    - `productName` (string)
    - `productText` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products/locations

Returns a list of valid text product issuance locations

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `locations` (object)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products/types

Returns a list of valid text product types and codes

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@graph` (array of object)
    - `productCode` (string, required)
    - `productName` (string, required)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products/{productId}

Returns a specific text product

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `productId` | path | string | Yes | . |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@id` (string (uri))
  - `id` (string)
  - `wmoCollectiveId` (string)
  - `issuingOffice` (string)
  - `issuanceTime` (string (date-time))
  - `productCode` (string)
  - `productName` (string)
  - `productText` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products/types/{typeId}

Returns a list of text products of a given type

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `typeId` | path | string | Yes | . |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@graph` (array of object)
    - `@context` (one of several types)
    - `@id` (string (uri))
    - `id` (string)
    - `wmoCollectiveId` (string)
    - `issuingOffice` (string)
    - `issuanceTime` (string (date-time))
    - `productCode` (string)
    - `productName` (string)
    - `productText` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products/types/{typeId}/locations

Returns a list of valid text product issuance locations for a given product type

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `typeId` | path | string | Yes | . |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `locations` (object)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products/locations/{locationId}/types

Returns a list of valid text product types for a given issuance location

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `locationId` | path | string | Yes | . |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@graph` (array of object)
    - `productCode` (string, required)
    - `productName` (string, required)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products/types/{typeId}/locations/{locationId}

Returns a list of text products of a given type for a given issuance location

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `typeId` | path | string | Yes | . |
| `locationId` | path | string | Yes | . |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@graph` (array of object)
    - `@context` (one of several types)
    - `@id` (string (uri))
    - `id` (string)
    - `wmoCollectiveId` (string)
    - `issuingOffice` (string)
    - `issuanceTime` (string (date-time))
    - `productCode` (string)
    - `productName` (string)
    - `productText` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /products/types/{typeId}/locations/{locationId}/latest

Returns latest text products of a given type for a given issuance location with product text

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `typeId` | path | string | Yes | . |
| `locationId` | path | string | Yes | . |

**Responses**

- **200** — success
  Body (`application/ld+json`, object):
  - `@context` (one of several types)
  - `@id` (string (uri))
  - `id` (string)
  - `wmoCollectiveId` (string)
  - `issuingOffice` (string)
  - `issuanceTime` (string (date-time))
  - `productCode` (string)
  - `productName` (string)
  - `productText` (string)
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /zones

Returns a list of zones

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | query | array of string | No | Zone ID (forecast or county) |
| `area` | query | array of one of several types | No | State/marine area code |
| `region` | query | array of one of several types | No | Region code |
| `type` | query | array of string | No | Zone type |
| `point` | query | string | No | Point (latitude,longitude). Pattern: `^(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)$`. |
| `include_geometry` | query | boolean | No | Include geometry in results (true/false) |
| `limit` | query | integer | No | Limit. Minimum: 1. |
| `effective` | query | string (date-time) | No | Effective date/time |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object)
      - `@context` (one of several types)
      - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
      - `@id` (string (uri))
      - `@type` (string) — Allowed values: `wx:Zone`.
      - `id` (string) — UGC identifier for a NWS forecast zone or county. The first two letters will correspond to either a state code or marine area code (see #/components/schemas/StateTerritoryCode and #/components/schemas/MarineAreaCode for lists of valid letter combinations). The third letter will be Z for public/fire zone or C for county. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`.
      - `type` (string) — Allowed values: `land`, `marine`, `forecast`, `public`, `coastal`, `offshore`, `fire`, `county`.
      - `name` (string)
      - `effectiveDate` (string (date-time))
      - `expirationDate` (string (date-time))
      - `state` (one of several types) — May be null.
      - `forecastOffice` (string (uri))
      - `gridIdentifier` (string)
      - `awipsLocationIdentifier` (string)
      - `cwa` (array of string)
      - `forecastOffices` (array of string (uri))
      - `timeZone` (array of string (iana-time-zone-identifier))
      - `observationStations` (array of string (uri))
      - `radarStation` (string) — May be null.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /zones/{type}

Returns a list of zones of a given type

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | path | string | Yes | Zone type. Allowed values: `land`, `marine`, `forecast`, `public`, `coastal`, `offshore`, `fire`, `county`. |
| `id` | query | array of string | No | Zone ID (forecast or county) |
| `area` | query | array of one of several types | No | State/marine area code |
| `region` | query | array of one of several types | No | Region code |
| `type` | query | array of string | No | Zone type |
| `point` | query | string | No | Point (latitude,longitude). Pattern: `^(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)$`. |
| `include_geometry` | query | boolean | No | Include geometry in results (true/false) |
| `limit` | query | integer | No | Limit. Minimum: 1. |
| `effective` | query | string (date-time) | No | Effective date/time |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object)
      - `@context` (one of several types)
      - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
      - `@id` (string (uri))
      - `@type` (string) — Allowed values: `wx:Zone`.
      - `id` (string) — UGC identifier for a NWS forecast zone or county. The first two letters will correspond to either a state code or marine area code (see #/components/schemas/StateTerritoryCode and #/components/schemas/MarineAreaCode for lists of valid letter combinations). The third letter will be Z for public/fire zone or C for county. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`.
      - `type` (string) — Allowed values: `land`, `marine`, `forecast`, `public`, `coastal`, `offshore`, `fire`, `county`.
      - `name` (string)
      - `effectiveDate` (string (date-time))
      - `expirationDate` (string (date-time))
      - `state` (one of several types) — May be null.
      - `forecastOffice` (string (uri))
      - `gridIdentifier` (string)
      - `awipsLocationIdentifier` (string)
      - `cwa` (array of string)
      - `forecastOffices` (array of string (uri))
      - `timeZone` (array of string (iana-time-zone-identifier))
      - `observationStations` (array of string (uri))
      - `radarStation` (string) — May be null.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /zones/{type}/{zoneId}

Returns metadata about a given zone

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | path | string | Yes | Zone type. Allowed values: `land`, `marine`, `forecast`, `public`, `coastal`, `offshore`, `fire`, `county`. |
| `zoneId` | path | string | Yes | NWS public zone/county identifier. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`. |
| `effective` | query | string (date-time) | No | Effective date/time |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required)
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `@id` (string (uri))
    - `@type` (string) — Allowed values: `wx:Zone`.
    - `id` (string) — UGC identifier for a NWS forecast zone or county. The first two letters will correspond to either a state code or marine area code (see #/components/schemas/StateTerritoryCode and #/components/schemas/MarineAreaCode for lists of valid letter combinations). The third letter will be Z for public/fire zone or C for county. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`.
    - `type` (string) — Allowed values: `land`, `marine`, `forecast`, `public`, `coastal`, `offshore`, `fire`, `county`.
    - `name` (string)
    - `effectiveDate` (string (date-time))
    - `expirationDate` (string (date-time))
    - `state` (one of several types) — May be null.
    - `forecastOffice` (string (uri))
    - `gridIdentifier` (string)
    - `awipsLocationIdentifier` (string)
    - `cwa` (array of string)
    - `forecastOffices` (array of string (uri))
    - `timeZone` (array of string (iana-time-zone-identifier))
    - `observationStations` (array of string (uri))
    - `radarStation` (string) — May be null.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /zones/{type}/{zoneId}/forecast

Returns the current zone forecast for a given zone

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | path | string | Yes | Zone type |
| `zoneId` | path | string | Yes | NWS public zone/county identifier. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`. |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `id` (string (uri))
  - `type` (string, required) — Allowed values: `Feature`.
  - `geometry` (one of several types, required) — A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. May be null.
    - `type` (string, required) — Allowed values: `Point`.
    - `coordinates` (array of number, required) — A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `LineString`.
    - `coordinates` (array of array of number, required) — A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 2.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `Polygon`.
    - `coordinates` (array of array of array of number, required) — A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPoint`.
    - `coordinates` (array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiLineString`.
    - `coordinates` (array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
    - `type` (string, required) — Allowed values: `MultiPolygon`.
    - `coordinates` (array of array of array of array of number, required)
    - `bbox` (array of number) — A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. Min items: 4.
  - `properties` (object, required) — An object representing a zone area forecast.
    - `@context` (one of several types)
    - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
    - `zone` (string (uri)) — An API link to the zone this forecast is for.
    - `updated` (string (date-time)) — The time this zone forecast product was published.
    - `periods` (array of object) — An array of forecast periods.
      - `number` (integer, required) — A sequential identifier number.
      - `name` (string, required) — A textual description of the period.
      - `detailedForecast` (string, required) — A detailed textual forecast for the period.
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /zones/{type}/{zoneId}/radio

Returns transmitter object for a given zone

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | path | string | Yes | Must be value 'county'. Allowed values: `county`. |
| `zoneId` | path | string | Yes | NWS public zone/county identifier. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`. |

**Responses**

- **200** — success
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /zones/forecast/{zoneId}/observations

Returns a list of observations for a given zone

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `zoneId` | path | string | Yes | NWS public zone/county identifier. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`. |
| `start` | query | string (date-time) | No | Start date/time |
| `end` | query | string (date-time) | No | End date/time |
| `limit` | query | integer | No | Limit. Minimum: 1. Maximum: 500. |

**Responses**

- **200** — success
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object)
      - `@context` (one of several types)
      - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
      - `@id` (string (uri))
      - `@type` (string) — Allowed values: `wx:ObservationStation`.
      - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `station` (string (uri))
      - `stationId` (string)
      - `stationName` (string)
      - `timestamp` (string (date-time))
      - `rawMessage` (string)
      - `textDescription` (string)
      - `icon` (string (uri)) — May be null.
      - `presentWeather` (array of object)
        - `intensity` (string, required) — Allowed values: `light`, `heavy`. May be null.
        - `modifier` (string, required) — Allowed values: `patches`, `blowing`, `low_drifting`, `freezing`, `shallow`, `partial`, `showers`. May be null.
        - `weather` (string, required) — Allowed values: `fog_mist`, `dust_storm`, `dust`, `drizzle`, `funnel_cloud`, `fog`, `smoke`, `hail`, `snow_pellets`, `haze`, `ice_crystals`, `ice_pellets`, `dust_whirls`, `spray`, `rain`, `sand`, `snow_grains`, `snow`, `squalls`, `sand_storm`, `thunderstorms`, `unknown`, `volcanic_ash`.
        - `rawString` (string, required)
        - `inVicinity` (boolean)
      - `temperature` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `dewpoint` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windDirection` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windSpeed` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windGust` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `barometricPressure` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `seaLevelPressure` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `visibility` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `maxTemperatureLast24Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `minTemperatureLast24Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `precipitationLastHour` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `precipitationLast3Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `precipitationLast6Hours` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `relativeHumidity` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `windChill` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `heatIndex` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `cloudLayers` (array of object) — May be null.
        - `base` (object, required) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `amount` (string, required) — Allowed values: `OVC`, `BKN`, `SCT`, `FEW`, `SKC`, `CLR`, `VV`.
  - `pagination` (object) — Links for retrieving more data from paged data sets
    - `next` (string (uri), required) — A link to the next page of records
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.

### GET /zones/forecast/{zoneId}/stations

Returns a list of observation stations for a given zone

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `zoneId` | path | string | Yes | NWS public zone/county identifier. Pattern: `^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$`. |
| `limit` | query | integer | No | Limit. Default: `500`. Minimum: 1. Maximum: 500. |
| `cursor` | query | string | No | Pagination cursor |

**Responses**

- **200** — A collection of observation stations.
  Body (`application/geo+json`, object):
  - `@context` (one of several types)
  - `type` (string, required) — Allowed values: `FeatureCollection`.
  - `features` (array of object, required)
    - `properties` (object)
      - `@context` (one of several types)
      - `geometry` (string (wkt)) — A geometry represented in Well-Known Text (WKT) format. May be null.
      - `@id` (string (uri))
      - `@type` (string) — Allowed values: `wx:ObservationStation`.
      - `elevation` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `stationIdentifier` (string)
      - `name` (string)
      - `timeZone` (string (iana-time-zone-identifier))
      - `provider` (string) — The data provider for this station. E.g., "ASOS," "MesoWest," etc.
      - `subProvider` (string) — The sub-provider of for this station. E.g., "FAA," "DOT," etc.
      - `forecast` (string (uri)) — A link to the NWS public forecast zone containing this station.
      - `county` (string (uri)) — A link to the NWS county zone containing this station.
      - `fireWeatherZone` (string (uri)) — A link to the NWS fire weather forecast zone containing this station.
      - `distance` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
      - `bearing` (object) — A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue
        - `value` (number) — A measured value. May be null.
        - `maxValue` (number) — The maximum value of a range of measured values
        - `minValue` (number) — The minimum value of a range of measured values
        - `unitCode` (string) — A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace "nwsUnit" are currently custom and do not align to any standard. Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. Pattern: `^((wmo|uc|wmoUnit|nwsUnit):)?.*$`.
        - `qualityControl` (string) — For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml. Allowed values: `Z`, `C`, `S`, `V`, `X`, `Q`, `G`, `B`, `T`.
  - `observationStations` (array of string (uri))
  - `pagination` (object) — Links for retrieving more data from paged data sets
    - `next` (string (uri), required) — A link to the next page of records
- **default** — An error response.
  Body (`application/problem+json`, object):
  - `type` (string (uri), required) — A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. Default: `about:blank`.
  - `title` (string, required) — A short, human-readable summary of the problem type.
  - `status` (number, required) — The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. Minimum: 100. Maximum: 999.
  - `detail` (string, required) — A human-readable explanation specific to this occurrence of the problem.
  - `instance` (string (uri), required) — A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL.
  - `correlationId` (string, required) — A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue.
