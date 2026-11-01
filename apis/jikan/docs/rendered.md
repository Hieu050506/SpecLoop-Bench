# Jikan API — API Reference

[Jikan](https://jikan.moe) is an **Unofficial** MyAnimeList API.
It scrapes the website to satisfy the need for a complete API - which MyAnimeList lacks.

# Information

⚡ Jikan is powered by its awesome backers - 🙏 [Become a backer](https://www.patreon.com/jikan)

## Rate Limiting

| Duration | Requests |
|----|----|
| Daily | **Unlimited** |
| Per Minute | 60 requests |
| Per Second | 3 requests |

Note: It's still possible to get rate limited from MyAnimeList.net instead.


## JSON Notes
- Any property (except arrays or objects) whose value does not exist or is undetermined, will be `null`.
- Any array or object property whose value does not exist or is undetermined, will be empty.
- Any `score` property whose value does not exist or is undetermined, will be `0`.
- All dates and timestamps are returned in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format and in UTC timezone

## Caching
By **CACHING**, we refer to the data parsed from MyAnimeList which is stored temporarily on our servers to provide better API performance.

All requests are cached for **24 hours**.

The following response headers will detail cache information.

| Header | Remarks |
| ---- | ---- |
| `Expires` | Cache expiry date |
| `Last-Modified` | Cache set date |
| `X-Request-Fingerprint` | Unique request fingerprint (only for cachable requests, not queries) |


Note: `X-Request-Fingerprint` will only be available on single resource requests and their child endpoints. e.g `/anime/1`, `/anime/1/relations`.
They won't be available on pages which perform queries, like /anime, or /top/anime, etc.

## Allowed HTTP(s) requests

**Jikan REST API does not provide authenticated requests for MyAnimeList.** This means you can not use it to update your anime/manga list.
Only GET requests are supported which return READ-ONLY data.

## HTTP Responses

All error responses are accompanied by a JSON Error response.

| Exception | HTTP Status | Remarks |
| ---- | ---- | ---- |
| N/A | `200 - OK` | The request was successful |
| N/A | `304 - Not Modified` | You have the latest data (Cache Validation response) |
| `BadRequestException`,`ValidationException` | `400 - Bad Request` | You've made an invalid request. Recheck documentation |
| `BadResponseException` | `404 - Not Found` | The resource was not found or MyAnimeList responded with a `404` |
| `BadRequestException` | `405 - Method Not Allowed` | Requested Method is not supported for resource. Only `GET` requests are allowed |
| `RateLimitException` | `429 - Too Many Request` | You are being rate limited by Jikan or MyAnimeList is rate-limiting our servers (specified in the error response) |
| `UpstreamException`,`ParserException`,etc. | `500 - Internal Server Error` | Something didn't work. Try again later. If you see an error response with a `report_url` URL, please click on it to open an auto-generated GitHub issue |
| `ServiceUnavailableException` | `503 - Service Unavailable` | In most cases this is intentionally done if the service is down for maintenance. |

## JSON Error Response

```json
 {
     "status": 500,
     "type": "InternalException",
     "message": "Exception Message",
     "error": "Exception Trace",
     "report_url": "https://github.com..."
  }
```

| Property | Remarks |
| ---- | ---- |
| `status` | Returned HTTP Status Code |
| `type` | Thrown Exception |
| `message` | Human-readable error message |
| `error` | Error response and trace from the API |
| `report_url` | Clicking this would redirect you to a generated GitHub issue |


## Cache Validation

- All requests return a `ETag` header which is an MD5 hash of the response
- You can use this hash to verify if there's new or updated content by suppliying it as the value for the `If-None-Match` in your next request header
- You will get a HTTP `304 - Not Modified` response if the content has not changed
- If the content has changed, you'll get a HTTP `200 - OK` response with the updated JSON response

![Cache Validation](https://i.imgur.com/925ozVn.png 'Cache Validation')

## Disclaimer

- Jikan is not affiliated with MyAnimeList.net.
- Jikan is a free, open-source API. Please use it responsibly.

----

By using the API, you are agreeing to Jikan's [terms of use](https://jikan.moe/terms) policy.

[v3 Documentation](https://jikan.docs.apiary.io/) - [Wrappers/SDKs](https://github.com/jikan-me/jikan#wrappers) - [Report an issue](https://github.com/jikan-me/jikan-rest/issues/new) - [Host your own server](https://github.com/jikan-me/jikan-rest)

**Version:** 4.0.0  
**Base URL:** `https://api.jikan.moe/v4`

## anime

### GET /anime/{id}/full

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns complete anime resource data
  Body (`application/json`, object):
  - `data` (object) — Full anime Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `relations` (array of object)
      - `relation` (string) — Relation type
      - `entry` (array of object)
        - `mal_id` (integer) — MyAnimeList ID
        - `type` (string) — Type of resource
        - `name` (string) — Resource Name/Title
        - `url` (string) — MyAnimeList URL
    - `theme` (object)
      - `openings` (array of string)
      - `endings` (array of string)
    - `external` (array of object)
      - `name` (string)
      - `url` (string)
    - `streaming` (array of object)
      - `name` (string)
      - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime resource
  Body (`application/json`, object):
  - `data` (object) — Anime Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/characters

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime characters resource
  Body (`application/json`, object):
  - `data` (array of object)
    - `character` (object) — Character details
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `name` (string) — Character Name
    - `role` (string) — Character's Role
    - `voice_actors` (array of object)
      - `person` (object)
        - `mal_id` (integer)
        - `url` (string)
        - `images` (object)
        - `name` (string)
      - `language` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/staff

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime staff resource
  Body (`application/json`, object):
  - `data` (array of object)
    - `person` (object) — Person details
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
      - `name` (string) — Name
    - `positions` (array of string) — Staff Positions
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/episodes

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns a list of anime episodes
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL. This is the URL of the episode's video. If there is no video url, this will be null. May be null.
    - `title` (string) — Title
    - `title_japanese` (string) — Title Japanese. May be null.
    - `title_romanji` (string) — title_romanji. May be null.
    - `aired` (string) — Aired Date ISO8601. May be null.
    - `score` (number) — Aggregated episode score (1.00 - 5.00) based on MyAnimeList user voting. Minimum: 1. Maximum: 5. May be null.
    - `filler` (boolean) — Filler episode
    - `recap` (boolean) — Recap episode
    - `forum_url` (string) — Episode discussion forum URL. May be null.
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/episodes/{episode}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `episode` | path | integer | Yes |  |

**Responses**

- **200** — Returns a single anime episode resource
  Body (`application/json`, object):
  - `data` (object) — Anime Episode Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `title` (string) — Title
    - `title_japanese` (string) — Title Japanese. May be null.
    - `title_romanji` (string) — title_romanji. May be null.
    - `duration` (integer) — Episode duration in seconds. May be null.
    - `aired` (string) — Aired Date ISO8601. May be null.
    - `filler` (boolean) — Filler episode
    - `recap` (boolean) — Recap episode
    - `synopsis` (string) — Episode Synopsis. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/news

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns a list of news articles related to the entry
  Body (`application/json`, object):
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `title` (string) — Title
    - `date` (string) — Post Date ISO8601
    - `author_username` (string) — Author MyAnimeList Username
    - `author_url` (string) — Author Profile URL
    - `forum_url` (string) — Forum topic URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `comments` (integer) — Comment count
    - `excerpt` (string) — Excerpt
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/forum

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `filter` | query | string | No | Filter topics. Allowed values: `all`, `episode`, `other`. |

**Responses**

- **200** — Returns a list of forum topics related to the entry
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `title` (string) — Title
    - `date` (string) — Post Date ISO8601
    - `author_username` (string) — Author MyAnimeList Username
    - `author_url` (string) — Author Profile URL
    - `comments` (integer) — Comment count
    - `last_comment` (object) — Last comment details
      - `url` (string) — Last comment URL
      - `author_username` (string) — Author MyAnimeList Username
      - `author_url` (string) — Author Profile URL
      - `date` (string) — Last comment date posted ISO8601. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/videos

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns videos related to the entry
  Body (`application/json`, object):
  - `data` (object)
    - `promo` (array of object)
      - `title` (string) — Title
      - `trailer` (object) — Youtube Details
        - `youtube_id` (string) — YouTube ID. May be null.
        - `url` (string) — YouTube URL. May be null.
        - `embed_url` (string) — Parsed Embed URL. May be null.
        - `images` (object)
    - `episodes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `title` (string) — Title
      - `episode` (string) — Episode
      - `images` (object)
        - `jpg` (object) — Available images in JPG
    - `music_videos` (array of object)
      - `title` (string) — Title
      - `video` (object) — Youtube Details
        - `youtube_id` (string) — YouTube ID. May be null.
        - `url` (string) — YouTube URL. May be null.
        - `embed_url` (string) — Parsed Embed URL. May be null.
        - `images` (object)
      - `meta` (object)
        - `title` (string) — May be null.
        - `author` (string) — May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/videos/episodes

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns episode videos related to the entry
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID or Episode Number
    - `title` (string) — Episode Title
    - `episode` (string) — Episode Subtitle
    - `url` (string) — Episode Page URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/pictures

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns pictures related to the entry
  Body (`application/json`, object):
  - `data` (array of object)
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/statistics

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime statistics
  Body (`application/json`, object):
  - `data` (object)
    - `watching` (integer) — Number of users watching the resource
    - `completed` (integer) — Number of users who have completed the resource
    - `on_hold` (integer) — Number of users who have put the resource on hold
    - `dropped` (integer) — Number of users who have dropped the resource
    - `plan_to_watch` (integer) — Number of users who have planned to watch the resource
    - `total` (integer) — Total number of users who have the resource added to their lists
    - `scores` (array of object)
      - `score` (integer) — Scoring value
      - `votes` (integer) — Number of votes for this score
      - `percentage` (number (float)) — Percentage of votes for this score
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/moreinfo

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime statistics
  Body (`application/json`, object):
  - `data` (object)
    - `moreinfo` (string) — Additional information on the entry. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/recommendations

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime recommendations
  Body (`application/json`, object):
  - `data` (array of object)
    - `entry` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/userupdates

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns a list of users who have added/updated/removed the entry on their list
  Body (`application/json`, object):
  - `data` (array of object)
    - `user` (object)
      - `username` (string) — MyAnimeList Username
      - `url` (string) — MyAnimeList Profile URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
    - `score` (integer) — User Score. May be null.
    - `status` (string) — User list status
    - `episodes_seen` (integer) — Number of episodes seen. May be null.
    - `episodes_total` (integer) — Total number of episodes. May be null.
    - `date` (string) — Last updated date ISO8601
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/reviews

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |
| `preliminary` | query | boolean | No | Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: `?preliminary=true` |
| `spoilers` | query | boolean | No | Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: `?spoiler=true` |

**Responses**

- **200** — Returns anime reviews
  Body (`application/json`, object):
  - `data` (array of object)
    - `user` (object)
      - `username` (string) — MyAnimeList Username
      - `url` (string) — MyAnimeList Profile URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList review URL
    - `type` (string) — Entry type
    - `reactions` (object) — User reaction count on the review
      - `overall` (integer) — Overall reaction count
      - `nice` (integer) — Nice reaction count
      - `love_it` (integer) — Love it reaction count
      - `funny` (integer) — Funny reaction count
      - `confusing` (integer) — Confusing reaction count
      - `informative` (integer) — Informative reaction count
      - `well_written` (integer) — Well written reaction count
      - `creative` (integer) — Creative reaction count
    - `date` (string) — Review created date ISO8601
    - `review` (string) — Review content
    - `score` (integer) — Number of user votes on the Review
    - `tags` (array of string) — Review tags
    - `is_spoiler` (boolean) — The review contains spoiler
    - `is_preliminary` (boolean) — The review was made before the entry was completed
    - `episodes_watched` (integer) — Number of episodes watched
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/relations

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime relations
  Body (`application/json`, object):
  - `data` (array of object)
    - `relation` (string) — Relation type
    - `entry` (array of object) — Related entries
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL

### GET /anime/{id}/themes

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime themes
  Body (`application/json`, object):
  - `data` (object)
    - `openings` (array of string)
    - `endings` (array of string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/external

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime external links
  Body (`application/json`, object):
  - `data` (array of object)
    - `name` (string)
    - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime/{id}/streaming

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime streaming links
  Body (`application/json`, object):
  - `data` (array of object)
    - `name` (string)
    - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /anime

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `unapproved` | query | boolean | No | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` |
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |
| `q` | query | string | No |  |
| `type` | query | string | No | Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. |
| `score` | query | number | No |  |
| `min_score` | query | number | No | Set a minimum score for results. |
| `max_score` | query | number | No | Set a maximum score for results |
| `status` | query | string | No | Allowed values: `airing`, `complete`, `upcoming`. |
| `rating` | query | string | No | Allowed values: `g`, `pg`, `pg13`, `r17`, `r`, `rx`. |
| `sfw` | query | boolean | No | Filter out Adult entries |
| `genres` | query | string | No | Filter by genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 |
| `genres_exclude` | query | string | No | Exclude genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 |
| `order_by` | query | string | No | Allowed values: `mal_id`, `title`, `start_date`, `end_date`, `episodes`, `score`, `scored_by`, `rank`, `popularity`, `members`, `favorites`. |
| `sort` | query | string | No | Allowed values: `desc`, `asc`. |
| `letter` | query | string | No | Return entries starting with the given letter |
| `producers` | query | string | No | Filter by producer(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 |
| `start_date` | query | string | No | Filter by starting date. Format: YYYY-MM-DD. e.g `2022`, `2005-05`, `2005-01-01` |
| `end_date` | query | string | No | Filter by ending date. Format: YYYY-MM-DD. e.g `2022`, `2005-05`, `2005-01-01` |

**Responses**

- **200** — Returns search results for anime
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

## characters

### GET /characters/{id}/full

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns complete character resource data
  Body (`application/json`, object):
  - `data` (object) — Character Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
    - `name` (string) — Name
    - `name_kanji` (string) — Name. May be null.
    - `nicknames` (array of string) — Other Names
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
    - `anime` (array of object)
      - `role` (string) — Character's Role
      - `anime` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
    - `manga` (array of object)
      - `role` (string) — Character's Role
      - `manga` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
    - `voices` (array of object)
      - `language` (string) — Character's Role
      - `person` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `name` (string) — Entry name
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /characters/{id}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns character resource
  Body (`application/json`, object):
  - `data` (object) — Character Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
    - `name` (string) — Name
    - `name_kanji` (string) — Name. May be null.
    - `nicknames` (array of string) — Other Names
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /characters/{id}/anime

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime that character is in
  Body (`application/json`, object):
  - `data` (array of object)
    - `role` (string) — Character's Role
    - `anime` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /characters/{id}/manga

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns manga that character is in
  Body (`application/json`, object):
  - `data` (array of object)
    - `role` (string) — Character's Role
    - `manga` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /characters/{id}/voices

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns the character's voice actors
  Body (`application/json`, object):
  - `data` (array of object)
    - `language` (string) — Character's Role
    - `person` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
      - `name` (string) — Entry name
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /characters/{id}/pictures

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns pictures related to the entry
  Body (`application/json`, object):
  - `data` (array of object)
    - `image_url` (string) — Default JPG Image Size URL. May be null.
    - `large_image_url` (string) — Large JPG Image Size URL. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /characters

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |
| `q` | query | string | No |  |
| `order_by` | query | string | No | Allowed values: `mal_id`, `name`, `favorites`. |
| `sort` | query | string | No | Allowed values: `desc`, `asc`. |
| `letter` | query | string | No | Return entries starting with the given letter |

**Responses**

- **200** — Returns search results for characters
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
    - `name` (string) — Name
    - `name_kanji` (string) — Name. May be null.
    - `nicknames` (array of string) — Other Names
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

## clubs

### GET /clubs/{id}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns Club Resource
  Body (`application/json`, object):
  - `data` (object) — Club Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `name` (string) — Club name
    - `url` (string) — Club URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `members` (integer) — Number of club members
    - `category` (string) — Club Category. Allowed values: `actors & artists`, `anime`, `characters`, `cities & neighborhoods`, `companies`, `conventions`, `games`, `japan`, `manga`, `music`, `others`, `schools`.
    - `created` (string) — Date Created ISO8601
    - `access` (string) — Club access. Allowed values: `public`, `private`, `secret`.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /clubs/{id}/members

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns Club Members Resource
  Body (`application/json`, object):
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
  - `data` (array of object)
    - `username` (string) — User's username
    - `url` (string) — User URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /clubs/{id}/staff

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns Club Staff
  Body (`application/json`, object):
  - `data` (array of object)
    - `url` (string) — User URL
    - `username` (string) — User's username
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /clubs/{id}/relations

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns Club Relations
  Body (`application/json`, object):
  - `data` (object)
    - `anime` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `manga` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `characters` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /clubs

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |
| `q` | query | string | No |  |
| `type` | query | string | No | Allowed values: `public`, `private`, `secret`. |
| `category` | query | string | No | Allowed values: `anime`, `manga`, `actors_and_artists`, `characters`, `cities_and_neighborhoods`, `companies`, `conventions`, `games`, `japan`, `music`, `other`, `schools`. |
| `order_by` | query | string | No | Allowed values: `mal_id`, `name`, `members_count`, `created`. |
| `sort` | query | string | No | Allowed values: `desc`, `asc`. |
| `letter` | query | string | No | Return entries starting with the given letter |

**Responses**

- **200** — Returns search results for clubs
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `name` (string) — Club name
    - `url` (string) — Club URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `members` (integer) — Number of club members
    - `category` (string) — Club Category. Allowed values: `actors & artists`, `anime`, `characters`, `cities & neighborhoods`, `companies`, `conventions`, `games`, `japan`, `manga`, `music`, `others`, `schools`.
    - `created` (string) — Date Created ISO8601
    - `access` (string) — Club access. Allowed values: `public`, `private`, `secret`.
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

## genres

### GET /genres/anime

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `filter` | query | string | No | Allowed values: `genres`, `explicit_genres`, `themes`, `demographics`. |

**Responses**

- **200** — Returns entry genres, explicit_genres, themes and demographics
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `name` (string) — Genre Name
    - `url` (string) — MyAnimeList URL
    - `count` (integer) — Genre's entry count
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /genres/manga

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `filter` | query | string | No | Allowed values: `genres`, `explicit_genres`, `themes`, `demographics`. |

**Responses**

- **200** — Returns entry genres, explicit_genres, themes and demographics
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `name` (string) — Genre Name
    - `url` (string) — MyAnimeList URL
    - `count` (integer) — Genre's entry count
- **400** — Error: Bad request. When required parameters were not supplied.

## magazines

### GET /magazines

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |
| `q` | query | string | No |  |
| `order_by` | query | string | No | Allowed values: `mal_id`, `name`, `count`. |
| `sort` | query | string | No | Allowed values: `desc`, `asc`. |
| `letter` | query | string | No | Return entries starting with the given letter |

**Responses**

- **200** — Returns magazines collection
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `name` (string) — Magazine Name
    - `url` (string) — MyAnimeList URL
    - `count` (integer) — Magazine's manga count
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

## manga

### GET /manga/{id}/full

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns complete manga resource data
  Body (`application/json`, object):
  - `data` (object) — Manga Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All Titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Manga Type. Allowed values: `Manga`, `Novel`, `Light Novel`, `One-shot`, `Doujinshi`, `Manhua`, `Manhwa`, `OEL`. May be null.
    - `chapters` (integer) — Chapter count. May be null.
    - `volumes` (integer) — Volume count. May be null.
    - `status` (string) — Publishing status. Allowed values: `Finished`, `Publishing`, `On Hiatus`, `Discontinued`, `Not yet published`.
    - `publishing` (boolean) — Publishing boolean
    - `published` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `authors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `serializations` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `relations` (array of object)
      - `relation` (string) — Relation type
      - `entry` (array of object)
        - `mal_id` (integer) — MyAnimeList ID
        - `type` (string) — Type of resource
        - `name` (string) — Resource Name/Title
        - `url` (string) — MyAnimeList URL
    - `external` (array of object)
      - `name` (string)
      - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns pictures related to the entry
  Body (`application/json`, object):
  - `data` (object) — Manga Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All Titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `type` (string) — Manga Type. Allowed values: `Manga`, `Novel`, `Light Novel`, `One-shot`, `Doujinshi`, `Manhua`, `Manhwa`, `OEL`. May be null.
    - `chapters` (integer) — Chapter count. May be null.
    - `volumes` (integer) — Volume count. May be null.
    - `status` (string) — Publishing status. Allowed values: `Finished`, `Publishing`, `On Hiatus`, `Discontinued`, `Not yet published`.
    - `publishing` (boolean) — Publishing boolean
    - `published` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `authors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `serializations` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/characters

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns manga characters resource
  Body (`application/json`, object):
  - `data` (array of object)
    - `character` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `name` (string) — Entry name
    - `role` (string) — Character's Role
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/news

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns a list of manga news topics
  Body (`application/json`, object):
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `title` (string) — Title
    - `date` (string) — Post Date ISO8601
    - `author_username` (string) — Author MyAnimeList Username
    - `author_url` (string) — Author Profile URL
    - `forum_url` (string) — Forum topic URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `comments` (integer) — Comment count
    - `excerpt` (string) — Excerpt
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/forum

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `filter` | query | string | No | Filter topics. Allowed values: `all`, `episode`, `other`. |

**Responses**

- **200** — Returns a list of manga forum topics
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `title` (string) — Title
    - `date` (string) — Post Date ISO8601
    - `author_username` (string) — Author MyAnimeList Username
    - `author_url` (string) — Author Profile URL
    - `comments` (integer) — Comment count
    - `last_comment` (object) — Last comment details
      - `url` (string) — Last comment URL
      - `author_username` (string) — Author MyAnimeList Username
      - `author_url` (string) — Author Profile URL
      - `date` (string) — Last comment date posted ISO8601. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/pictures

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns a list of manga pictures
  Body (`application/json`, object):
  - `data` (array of object)
    - `jpg` (object) — Available images in JPG
      - `image_url` (string) — Image URL JPG. May be null.
      - `small_image_url` (string) — Small Image URL JPG. May be null.
      - `large_image_url` (string) — Image URL JPG. May be null.
    - `webp` (object) — Available images in WEBP
      - `image_url` (string) — Image URL WEBP. May be null.
      - `small_image_url` (string) — Small Image URL WEBP. May be null.
      - `large_image_url` (string) — Image URL WEBP. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/statistics

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns anime statistics
  Body (`application/json`, object):
  - `data` (object)
    - `reading` (integer) — Number of users reading the resource
    - `completed` (integer) — Number of users who have completed the resource
    - `on_hold` (integer) — Number of users who have put the resource on hold
    - `dropped` (integer) — Number of users who have dropped the resource
    - `plan_to_read` (integer) — Number of users who have planned to read the resource
    - `total` (integer) — Total number of users who have the resource added to their lists
    - `scores` (array of object)
      - `score` (integer) — Scoring value
      - `votes` (integer) — Number of votes for this score
      - `percentage` (number (float)) — Percentage of votes for this score
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/moreinfo

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns manga moreinfo
  Body (`application/json`, object):
  - `data` (object)
    - `moreinfo` (string) — Additional information on the entry. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/recommendations

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns manga recommendations
  Body (`application/json`, object):
  - `data` (array of object)
    - `entry` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/userupdates

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns manga user updates
  Body (`application/json`, object):
  - `data` (array of object)
    - `user` (object)
      - `username` (string) — MyAnimeList Username
      - `url` (string) — MyAnimeList Profile URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
    - `score` (integer) — User Score. May be null.
    - `status` (string) — User list status
    - `volumes_read` (integer) — Number of volumes read
    - `volumes_total` (integer) — Total number of volumes
    - `chapters_read` (integer) — Number of chapters read
    - `chapters_total` (integer) — Total number of chapters
    - `date` (string) — Last updated date ISO8601
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/reviews

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `page` | query | integer | No |  |
| `preliminary` | query | boolean | No | Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: `?preliminary=true` |
| `spoilers` | query | boolean | No | Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: `?spoiler=true` |

**Responses**

- **200** — Returns manga reviews
  Body (`application/json`, object):
  - `data` (array of object)
    - `user` (object)
      - `username` (string) — MyAnimeList Username
      - `url` (string) — MyAnimeList Profile URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList review URL
    - `type` (string) — Entry type
    - `reactions` (object) — User reaction count on the review
      - `overall` (integer) — Overall reaction count
      - `nice` (integer) — Nice reaction count
      - `love_it` (integer) — Love it reaction count
      - `funny` (integer) — Funny reaction count
      - `confusing` (integer) — Confusing reaction count
      - `informative` (integer) — Informative reaction count
      - `well_written` (integer) — Well written reaction count
      - `creative` (integer) — Creative reaction count
    - `date` (string) — Review created date ISO8601
    - `review` (string) — Review content
    - `score` (integer) — Number of user votes on the Review
    - `tags` (array of string) — Review tags
    - `is_spoiler` (boolean) — The review contains spoiler
    - `is_preliminary` (boolean) — The review was made before the entry was completed
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/relations

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns manga relations
  Body (`application/json`, object):
  - `data` (array of object)
    - `relation` (string) — Relation type
    - `entry` (array of object) — Related entries
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga/{id}/external

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns manga external links
  Body (`application/json`, object):
  - `data` (array of object)
    - `name` (string)
    - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /manga

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `unapproved` | query | boolean | No | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` |
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |
| `q` | query | string | No |  |
| `type` | query | string | No | Allowed values: `manga`, `novel`, `lightnovel`, `oneshot`, `doujin`, `manhwa`, `manhua`. |
| `score` | query | number | No |  |
| `min_score` | query | number | No | Set a minimum score for results. |
| `max_score` | query | number | No | Set a maximum score for results |
| `status` | query | string | No | Allowed values: `publishing`, `complete`, `hiatus`, `discontinued`, `upcoming`. |
| `sfw` | query | boolean | No | Filter out Adult entries |
| `genres` | query | string | No | Filter by genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 |
| `genres_exclude` | query | string | No | Exclude genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 |
| `order_by` | query | string | No | Allowed values: `mal_id`, `title`, `start_date`, `end_date`, `chapters`, `volumes`, `score`, `scored_by`, `rank`, `popularity`, `members`, `favorites`. |
| `sort` | query | string | No | Allowed values: `desc`, `asc`. |
| `letter` | query | string | No | Return entries starting with the given letter |
| `magazines` | query | string | No | Filter by magazine(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 |
| `start_date` | query | string | No | Filter by starting date. Format: YYYY-MM-DD. e.g `2022`, `2005-05`, `2005-01-01` |
| `end_date` | query | string | No | Filter by ending date. Format: YYYY-MM-DD. e.g `2022`, `2005-05`, `2005-01-01` |

**Responses**

- **200** — Returns search results for manga
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All Titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `type` (string) — Manga Type. Allowed values: `Manga`, `Novel`, `Light Novel`, `One-shot`, `Doujinshi`, `Manhua`, `Manhwa`, `OEL`. May be null.
    - `chapters` (integer) — Chapter count. May be null.
    - `volumes` (integer) — Volume count. May be null.
    - `status` (string) — Publishing status. Allowed values: `Finished`, `Publishing`, `On Hiatus`, `Discontinued`, `Not yet published`.
    - `publishing` (boolean) — Publishing boolean
    - `published` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `authors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `serializations` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

## people

### GET /people/{id}/full

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns complete character resource data
  Body (`application/json`, object):
  - `data` (object) — Person Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `website_url` (string) — Person's website URL. May be null.
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `name` (string) — Name
    - `given_name` (string) — Given Name. May be null.
    - `family_name` (string) — Family Name. May be null.
    - `alternate_names` (array of string) — Other Names
    - `birthday` (string) — Birthday Date ISO8601. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
    - `anime` (array of object)
      - `position` (string) — Person's position
      - `anime` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
    - `manga` (array of object)
      - `position` (string) — Person's position
      - `manga` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
    - `voices` (array of object)
      - `role` (string) — Person's Character's role in the anime
      - `anime` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
      - `character` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `name` (string) — Entry name
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /people/{id}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns pictures related to the entry
  Body (`application/json`, object):
  - `data` (object) — Person Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `website_url` (string) — Person's website URL. May be null.
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `name` (string) — Name
    - `given_name` (string) — Given Name. May be null.
    - `family_name` (string) — Family Name. May be null.
    - `alternate_names` (array of string) — Other Names
    - `birthday` (string) — Birthday Date ISO8601. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /people/{id}/anime

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns person's anime staff positions
  Body (`application/json`, object):
  - `data` (array of object)
    - `position` (string) — Person's position
    - `anime` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /people/{id}/voices

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns person's voice acting roles
  Body (`application/json`, object):
  - `data` (array of object)
    - `role` (string) — Person's Character's role in the anime
    - `anime` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `character` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `name` (string) — Entry name
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /people/{id}/manga

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns person's published manga works
  Body (`application/json`, object):
  - `data` (array of object)
    - `position` (string) — Person's position
    - `manga` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /people/{id}/pictures

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns a list of pictures of the person
  Body (`application/json`, object):
  - `data` (array of object)
    - `jpg` (object) — Available images in JPG
      - `image_url` (string) — Image URL JPG. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /people

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |
| `q` | query | string | No |  |
| `order_by` | query | string | No | Allowed values: `mal_id`, `name`, `birthday`, `favorites`. |
| `sort` | query | string | No | Allowed values: `desc`, `asc`. |
| `letter` | query | string | No | Return entries starting with the given letter |

**Responses**

- **200** — Returns search results for people
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `website_url` (string) — Person's website URL. May be null.
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `name` (string) — Name
    - `given_name` (string) — Given Name. May be null.
    - `family_name` (string) — Family Name. May be null.
    - `alternate_names` (array of string) — Other Names
    - `birthday` (string) — Birthday Date ISO8601. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

## producers

### GET /producers/{id}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns producer resource
  Body (`application/json`, object):
  - `data` (object) — Producers Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `favorites` (integer) — Producers's member favorites count
    - `count` (integer) — Producers's anime count
    - `established` (string) — Established Date ISO8601. May be null.
    - `about` (string) — About the Producer. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /producers/{id}/full

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns producer resource
  Body (`application/json`, object):
  - `data` (object) — Producers Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `favorites` (integer) — Producers's member favorites count
    - `count` (integer) — Producers's anime count
    - `established` (string) — Established Date ISO8601. May be null.
    - `about` (string) — About the Producer. May be null.
    - `external` (array of object)
      - `name` (string)
      - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /producers/{id}/external

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns producer's external links
  Body (`application/json`, object):
  - `data` (array of object)
    - `name` (string)
    - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /producers

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |
| `q` | query | string | No |  |
| `order_by` | query | string | No | Allowed values: `mal_id`, `count`, `favorites`, `established`. |
| `sort` | query | string | No | Allowed values: `desc`, `asc`. |
| `letter` | query | string | No | Return entries starting with the given letter |

**Responses**

- **200** — Returns producers collection
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `favorites` (integer) — Producers's member favorites count
    - `count` (integer) — Producers's anime count
    - `established` (string) — Established Date ISO8601. May be null.
    - `about` (string) — About the Producer. May be null.
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

## random

### GET /random/anime

**Responses**

- **200** — Returns a random anime resource
  Body (`application/json`, object):
  - `data` (object) — Anime Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /random/manga

**Responses**

- **200** — Returns a random manga resource
  Body (`application/json`, object):
  - `data` (object) — Manga Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All Titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `type` (string) — Manga Type. Allowed values: `Manga`, `Novel`, `Light Novel`, `One-shot`, `Doujinshi`, `Manhua`, `Manhwa`, `OEL`. May be null.
    - `chapters` (integer) — Chapter count. May be null.
    - `volumes` (integer) — Volume count. May be null.
    - `status` (string) — Publishing status. Allowed values: `Finished`, `Publishing`, `On Hiatus`, `Discontinued`, `Not yet published`.
    - `publishing` (boolean) — Publishing boolean
    - `published` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `authors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `serializations` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /random/characters

**Responses**

- **200** — Returns a random character resource
  Body (`application/json`, object):
  - `data` (object) — Character Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
    - `name` (string) — Name
    - `name_kanji` (string) — Name. May be null.
    - `nicknames` (array of string) — Other Names
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /random/people

**Responses**

- **200** — Returns a random person resource
  Body (`application/json`, object):
  - `data` (object) — Person Resource
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `website_url` (string) — Person's website URL. May be null.
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `name` (string) — Name
    - `given_name` (string) — Given Name. May be null.
    - `family_name` (string) — Family Name. May be null.
    - `alternate_names` (array of string) — Other Names
    - `birthday` (string) — Birthday Date ISO8601. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /random/users

**Responses**

- **200** — Returns a random user profile resource
  Body (`application/json`, object):
  - `data` (object)
    - `mal_id` (integer) — MyAnimeList ID. May be null.
    - `username` (string) — MyAnimeList Username
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
    - `last_online` (string) — Last Online Date ISO8601. May be null.
    - `gender` (string) — User Gender. May be null.
    - `birthday` (string) — Birthday Date ISO8601. May be null.
    - `location` (string) — Location. May be null.
    - `joined` (string) — Joined Date ISO8601. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

## recommendations

### GET /recommendations/anime

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns recent anime recommendations
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (string) — MAL IDs of recommendations is both of the MAL ID's with a `-` delimiter
    - `entry` (array of object) — Array of 2 entries that are being recommended to each other
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `content` (string) — Recommendation context provided by the user
    - `user` (object) — User Meta By ID
      - `url` (string) — MyAnimeList URL
      - `username` (string) — MyAnimeList Username
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /recommendations/manga

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns recent manga recommendations
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (string) — MAL IDs of recommendations is both of the MAL ID's with a `-` delimiter
    - `entry` (array of object) — Array of 2 entries that are being recommended to each other
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `content` (string) — Recommendation context provided by the user
    - `user` (object) — User Meta By ID
      - `url` (string) — MyAnimeList URL
      - `username` (string) — MyAnimeList Username
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

## reviews

### GET /reviews/anime

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `preliminary` | query | boolean | No | Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: `?preliminary=true` |
| `spoilers` | query | boolean | No | Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: `?spoiler=true` |

**Responses**

- **200** — Returns recent anime reviews
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /reviews/manga

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `preliminary` | query | boolean | No | Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: `?preliminary=true` |
| `spoilers` | query | boolean | No | Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: `?spoiler=true` |

**Responses**

- **200** — Returns recent manga reviews
- **400** — Error: Bad request. When required parameters were not supplied.

## schedules

### GET /schedules

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `filter` | query | string | No | Filter by day. Allowed values: `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`, `unknown`, `other`. |
| `kids` | query | string | No | When supplied, it will filter entries with the `Kids` Genre Demographic. When supplied as `kids=true`, it will return only Kid entries and when supplied as `kids=false`, it will filter out any Kid entries. Defaults to `false`. Allowed values: `true`, `false`. |
| `sfw` | query | string | No | 'Safe For Work'. When supplied, it will filter entries with the `Hentai` Genre. When supplied as `sfw=true`, it will return only SFW entries and when supplied as `sfw=false`, it will filter out any Hentai entries. Defaults to `false`. Allowed values: `true`, `false`. |
| `unapproved` | query | boolean | No | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` |
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |

**Responses**

- **200** — Returns weekly schedule
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

## users

### GET /users

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |
| `q` | query | string | No |  |
| `gender` | query | string | No | Allowed values: `any`, `male`, `female`, `nonbinary`. |
| `location` | query | string | No |  |
| `maxAge` | query | integer | No |  |
| `minAge` | query | integer | No |  |

**Responses**

- **200** — Returns search results for users
  Body (`application/json`, object):
  - `data` (array of object)
    - `url` (string) — MyAnimeList URL
    - `username` (string) — MyAnimeList Username
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
    - `last_online` (string) — Last Online Date ISO8601
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/userbyid/{id}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Returns username by ID search
  Body (`application/json`, object):
  - `data` (object) — User Meta By ID
    - `url` (string) — MyAnimeList URL
    - `username` (string) — MyAnimeList Username
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/full

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |

**Responses**

- **200** — Returns complete user resource data
  Body (`application/json`, object):
  - `data` (object) — Transform the resource into an array.
    - `mal_id` (integer) — MyAnimeList ID. May be null.
    - `username` (string) — MyAnimeList Username
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
    - `last_online` (string) — Last Online Date ISO8601. May be null.
    - `gender` (string) — User Gender. May be null.
    - `birthday` (string) — Birthday Date ISO8601. May be null.
    - `location` (string) — Location. May be null.
    - `joined` (string) — Joined Date ISO8601. May be null.
    - `statistics` (object)
      - `anime` (object) — Anime Statistics
        - `days_watched` (number (float)) — Number of days spent watching Anime
        - `mean_score` (number (float)) — Mean Score
        - `watching` (integer) — Anime Watching
        - `completed` (integer) — Anime Completed
        - `on_hold` (integer) — Anime On-Hold
        - `dropped` (integer) — Anime Dropped
        - `plan_to_watch` (integer) — Anime Planned to Watch
        - `total_entries` (integer) — Total Anime entries on User list
        - `rewatched` (integer) — Anime re-watched
        - `episodes_watched` (integer) — Number of Anime Episodes Watched
      - `manga` (object) — Manga Statistics
        - `days_read` (number (float)) — Number of days spent reading Manga
        - `mean_score` (number (float)) — Mean Score
        - `reading` (integer) — Manga Reading
        - `completed` (integer) — Manga Completed
        - `on_hold` (integer) — Manga On-Hold
        - `dropped` (integer) — Manga Dropped
        - `plan_to_read` (integer) — Manga Planned to Read
        - `total_entries` (integer) — Total Manga entries on User list
        - `reread` (integer) — Manga re-read
        - `chapters_read` (integer) — Number of Manga Chapters Read
        - `volumes_read` (integer) — Number of Manga Volumes Read
    - `external` (array of object)
      - `name` (string)
      - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |

**Responses**

- **200** — Returns user profile
  Body (`application/json`, object):
  - `data` (object)
    - `mal_id` (integer) — MyAnimeList ID. May be null.
    - `username` (string) — MyAnimeList Username
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
    - `last_online` (string) — Last Online Date ISO8601. May be null.
    - `gender` (string) — User Gender. May be null.
    - `birthday` (string) — Birthday Date ISO8601. May be null.
    - `location` (string) — Location. May be null.
    - `joined` (string) — Joined Date ISO8601. May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/statistics

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |

**Responses**

- **200** — Returns user statistics
  Body (`application/json`, object):
  - `data` (object)
    - `anime` (object) — Anime Statistics
      - `days_watched` (number (float)) — Number of days spent watching Anime
      - `mean_score` (number (float)) — Mean Score
      - `watching` (integer) — Anime Watching
      - `completed` (integer) — Anime Completed
      - `on_hold` (integer) — Anime On-Hold
      - `dropped` (integer) — Anime Dropped
      - `plan_to_watch` (integer) — Anime Planned to Watch
      - `total_entries` (integer) — Total Anime entries on User list
      - `rewatched` (integer) — Anime re-watched
      - `episodes_watched` (integer) — Number of Anime Episodes Watched
    - `manga` (object) — Manga Statistics
      - `days_read` (number (float)) — Number of days spent reading Manga
      - `mean_score` (number (float)) — Mean Score
      - `reading` (integer) — Manga Reading
      - `completed` (integer) — Manga Completed
      - `on_hold` (integer) — Manga On-Hold
      - `dropped` (integer) — Manga Dropped
      - `plan_to_read` (integer) — Manga Planned to Read
      - `total_entries` (integer) — Total Manga entries on User list
      - `reread` (integer) — Manga re-read
      - `chapters_read` (integer) — Number of Manga Chapters Read
      - `volumes_read` (integer) — Number of Manga Volumes Read
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/favorites

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |

**Responses**

- **200** — Returns user favorites
  Body (`application/json`, object):
  - `data` (object)
    - `anime` (array of object) — Favorite Anime
      - `type` (string)
      - `start_year` (integer)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `manga` (array of object) — Favorite Manga
      - `type` (string)
      - `start_year` (integer)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `characters` (array of object) — Favorite Characters
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `name` (string) — Entry name
      - `type` (string) — Type of resource
      - `title` (string) — Resource Name/Title
    - `people` (array of object) — Favorite People
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `name` (string) — Entry name
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/userupdates

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |

**Responses**

- **200** — Returns user updates
  Body (`application/json`, object):
  - `data` (object)
    - `anime` (array of object) — Last updated Anime
      - `entry` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
      - `score` (integer) — May be null.
      - `status` (string)
      - `episodes_seen` (integer) — May be null.
      - `episodes_total` (integer) — May be null.
      - `date` (string) — ISO8601 format
    - `manga` (array of object) — Last updated Manga
      - `entry` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
      - `score` (integer) — May be null.
      - `status` (string)
      - `chapters_read` (integer) — May be null.
      - `chapters_total` (integer) — May be null.
      - `volumes_read` (integer) — May be null.
      - `volumes_total` (integer) — May be null.
      - `date` (string) — ISO8601 format
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/about

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |

**Responses**

- **200** — Returns user about in raw HTML
  Body (`application/json`, object):
  - `data` (array of object)
    - `about` (string) — User About. NOTE: About information is customizable by users through BBCode on MyAnimeList. This means users can add multimedia content, different text sizes, etc. Due to this freeform, Jikan returns parsed HTML. Validate on your end! May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/history

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |
| `type` | query | string | No | Allowed values: `anime`, `manga`. |

**Responses**

- **200** — Returns user history (past 30 days)
  Body (`application/json`, object):
  - `data` (array of object)
    - `entry` (object) — Parsed URL Data
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `increment` (integer) — Number of episodes/chapters watched/read
    - `date` (string) — Date ISO8601
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/friends

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns user friends
  Body (`application/json`, object):
  - `data` (array of object)
    - `user` (object)
      - `username` (string) — MyAnimeList Username
      - `url` (string) — MyAnimeList Profile URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
    - `last_online` (string) — Last Online Date ISO8601 format
    - `friends_since` (string) — Friends Since Date ISO8601 format
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/animelist

User Anime lists have been discontinued since May 1st, 2022. <a href='https://docs.google.com/document/d/1-6H-agSnqa8Mfmw802UYfGQrceIEnAaEh4uCXAPiX5A'>Read more</a>

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |
| `status` | query | string | No | Allowed values: `all`, `watching`, `completed`, `onhold`, `dropped`, `plantowatch`. |

**Responses**

- **200** — Returns user anime list
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/mangalist

User Manga lists have been discontinued since May 1st, 2022. <a href='https://docs.google.com/document/d/1-6H-agSnqa8Mfmw802UYfGQrceIEnAaEh4uCXAPiX5A'>Read more</a>

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |
| `status` | query | string | No | Allowed values: `all`, `reading`, `completed`, `onhold`, `dropped`, `plantoread`. |

**Responses**

- **200** — Returns user manga list
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/reviews

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns user reviews
  Body (`application/json`, object):
  - `data` (object)
    - `data` (array of one of several types)
      - `user` (object)
        - `username` (string) — MyAnimeList Username
        - `url` (string) — MyAnimeList Profile URL
        - `images` (object)
      - `anime` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList review URL
      - `type` (string) — Entry type
      - `reactions` (object) — User reaction count on the review
        - `overall` (integer) — Overall reaction count
        - `nice` (integer) — Nice reaction count
        - `love_it` (integer) — Love it reaction count
        - `funny` (integer) — Funny reaction count
        - `confusing` (integer) — Confusing reaction count
        - `informative` (integer) — Informative reaction count
        - `well_written` (integer) — Well written reaction count
        - `creative` (integer) — Creative reaction count
      - `date` (string) — Review created date ISO8601
      - `review` (string) — Review content
      - `score` (integer) — Number of user votes on the Review
      - `tags` (array of string) — Review tags
      - `is_spoiler` (boolean) — The review contains spoiler
      - `is_preliminary` (boolean) — The review was made before the entry was completed
      - `episodes_watched` (integer) — Number of episodes watched
      - `user` (object)
        - `username` (string) — MyAnimeList Username
        - `url` (string) — MyAnimeList Profile URL
        - `images` (object)
      - `manga` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList review URL
      - `type` (string) — Entry type
      - `reactions` (object) — User reaction count on the review
        - `overall` (integer) — Overall reaction count
        - `nice` (integer) — Nice reaction count
        - `love_it` (integer) — Love it reaction count
        - `funny` (integer) — Funny reaction count
        - `confusing` (integer) — Confusing reaction count
        - `informative` (integer) — Informative reaction count
        - `well_written` (integer) — Well written reaction count
        - `creative` (integer) — Creative reaction count
      - `date` (string) — Review created date ISO8601
      - `review` (string) — Review content
      - `score` (integer) — Number of user votes on the Review
      - `tags` (array of string) — Review tags
      - `is_spoiler` (boolean) — The review contains spoiler
      - `is_preliminary` (boolean) — The review was made before the entry was completed
    - `pagination` (object)
      - `last_visible_page` (integer)
      - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/recommendations

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns Recent Anime Recommendations
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (string) — MAL IDs of recommendations is both of the MAL ID's with a `-` delimiter
    - `entry` (array of object) — Array of 2 entries that are being recommended to each other
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `content` (string) — Recommendation context provided by the user
    - `user` (object) — User Meta By ID
      - `url` (string) — MyAnimeList URL
      - `username` (string) — MyAnimeList Username
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/clubs

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns user clubs
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `name` (string) — Club Name
    - `url` (string) — Club URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /users/{username}/external

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes |  |

**Responses**

- **200** — Returns user's external links
  Body (`application/json`, object):
  - `data` (array of object)
    - `name` (string)
    - `url` (string)
- **400** — Error: Bad request. When required parameters were not supplied.

## seasons

### GET /seasons/now

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `filter` | query | string | No | Entry types. Allowed values: `tv`, `movie`, `ova`, `special`, `ona`, `music`. |
| `sfw` | query | boolean | No | 'Safe For Work'. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: `?sfw` |
| `unapproved` | query | boolean | No | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` |
| `continuing` | query | boolean | No | This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &#8243;TV (continuing)&#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) <br />Example usage: `?continuing` |
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |

**Responses**

- **200** — Returns current seasonal anime
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /seasons/{year}/{season}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `year` | path | integer | Yes |  |
| `season` | path | string | Yes |  |
| `filter` | query | string | No | Entry types. Allowed values: `tv`, `movie`, `ova`, `special`, `ona`, `music`. |
| `sfw` | query | boolean | No | 'Safe For Work'. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: `?sfw` |
| `unapproved` | query | boolean | No | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` |
| `continuing` | query | boolean | No | This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &#8243;TV (continuing)&#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) <br />Example usage: `?continuing` |
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |

**Responses**

- **200** — Returns seasonal anime
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /seasons

**Responses**

- **200** — Returns available list of seasons
  Body (`application/json`, object):
  - `data` (array of object)
    - `year` (integer) — Year
    - `seasons` (array of string) — List of available seasons
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /seasons/upcoming

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `filter` | query | string | No | Entry types. Allowed values: `tv`, `movie`, `ova`, `special`, `ona`, `music`. |
| `sfw` | query | boolean | No | 'Safe For Work'. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: `?sfw` |
| `unapproved` | query | boolean | No | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` |
| `continuing` | query | boolean | No | This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &#8243;TV (continuing)&#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) <br />Example usage: `?continuing` |
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |

**Responses**

- **200** — Returns upcoming season's anime
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

## top

### GET /top/anime

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | query | string | No | Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. |
| `filter` | query | string | No | Allowed values: `airing`, `upcoming`, `bypopularity`, `favorite`. |
| `rating` | query | string | No | Allowed values: `g`, `pg`, `pg13`, `r17`, `r`, `rx`. |
| `sfw` | query | boolean | No | Filter out Adult entries |
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |

**Responses**

- **200** — Returns top anime
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `title_synonyms` (array of string) — Other Titles
    - `type` (string) — Anime Type. Allowed values: `TV`, `OVA`, `Movie`, `Special`, `ONA`, `Music`, `CM`, `PV`, `TV Special`. May be null.
    - `source` (string) — Original Material/Source adapted from. May be null.
    - `episodes` (integer) — Episode count. May be null.
    - `status` (string) — Airing status. Allowed values: `Finished Airing`, `Currently Airing`, `Not yet aired`. May be null.
    - `airing` (boolean) — Airing boolean
    - `aired` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `duration` (string) — Parsed raw duration. May be null.
    - `rating` (string) — Anime audience rating. Allowed values: `G - All Ages`, `PG - Children`, `PG-13 - Teens 13 or older`, `R - 17+ (violence & profanity)`, `R+ - Mild Nudity`, `Rx - Hentai`. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `season` (string) — Season. Allowed values: `summer`, `winter`, `spring`, `fall`. May be null.
    - `year` (integer) — Year. May be null.
    - `broadcast` (object) — Broadcast Details
      - `day` (string) — Day of the week. May be null.
      - `time` (string) — Time in 24 hour format. May be null.
      - `timezone` (string) — Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). May be null.
      - `string` (string) — Raw parsed broadcast string. May be null.
    - `producers` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `licensors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `studios` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /top/manga

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | query | string | No | Allowed values: `manga`, `novel`, `lightnovel`, `oneshot`, `doujin`, `manhwa`, `manhua`. |
| `filter` | query | string | No | Allowed values: `publishing`, `upcoming`, `bypopularity`, `favorite`. |
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |

**Responses**

- **200** — Returns top manga
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
        - `large_image_url` (string) — Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
        - `large_image_url` (string) — Image URL WEBP. May be null.
    - `approved` (boolean) — Whether the entry is pending approval on MAL or not
    - `titles` (array of object) — All Titles
      - `type` (string) — Title type
      - `title` (string) — Title value
    - `title` (string) — Title
    - `title_english` (string) — English Title. May be null.
    - `title_japanese` (string) — Japanese Title. May be null.
    - `type` (string) — Manga Type. Allowed values: `Manga`, `Novel`, `Light Novel`, `One-shot`, `Doujinshi`, `Manhua`, `Manhwa`, `OEL`. May be null.
    - `chapters` (integer) — Chapter count. May be null.
    - `volumes` (integer) — Volume count. May be null.
    - `status` (string) — Publishing status. Allowed values: `Finished`, `Publishing`, `On Hiatus`, `Discontinued`, `Not yet published`.
    - `publishing` (boolean) — Publishing boolean
    - `published` (object) — Date range
      - `from` (string) — Date ISO8601. May be null.
      - `to` (string) — Date ISO8601. May be null.
      - `prop` (object) — Date Prop
        - `from` (object) — Date Prop From
        - `to` (object) — Date Prop To
        - `string` (string) — Raw parsed string. May be null.
    - `score` (number (float)) — Score. May be null.
    - `scored_by` (integer) — Number of users. May be null.
    - `rank` (integer) — Ranking. May be null.
    - `popularity` (integer) — Popularity. May be null.
    - `members` (integer) — Number of users who have added this entry to their list. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry. May be null.
    - `synopsis` (string) — Synopsis. May be null.
    - `background` (string) — Background. May be null.
    - `authors` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `serializations` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `explicit_genres` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `themes` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
    - `demographics` (array of object)
      - `mal_id` (integer) — MyAnimeList ID
      - `type` (string) — Type of resource
      - `name` (string) — Resource Name/Title
      - `url` (string) — MyAnimeList URL
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /top/people

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |

**Responses**

- **200** — Returns top people
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `website_url` (string) — Person's website URL. May be null.
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
    - `name` (string) — Name
    - `given_name` (string) — Given Name. May be null.
    - `family_name` (string) — Family Name. May be null.
    - `alternate_names` (array of string) — Other Names
    - `birthday` (string) — Birthday Date ISO8601. May be null.
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /top/characters

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `limit` | query | integer | No |  |

**Responses**

- **200** — Returns top characters
  Body (`application/json`, object):
  - `data` (array of object)
    - `mal_id` (integer) — MyAnimeList ID
    - `url` (string) — MyAnimeList URL
    - `images` (object)
      - `jpg` (object) — Available images in JPG
        - `image_url` (string) — Image URL JPG. May be null.
        - `small_image_url` (string) — Small Image URL JPG. May be null.
      - `webp` (object) — Available images in WEBP
        - `image_url` (string) — Image URL WEBP. May be null.
        - `small_image_url` (string) — Small Image URL WEBP. May be null.
    - `name` (string) — Name
    - `name_kanji` (string) — Name. May be null.
    - `nicknames` (array of string) — Other Names
    - `favorites` (integer) — Number of users who have favorited this entry
    - `about` (string) — Biography. May be null.
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
    - `current_page` (integer)
    - `items` (object)
      - `count` (integer)
      - `total` (integer)
      - `per_page` (integer)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /top/reviews

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |
| `type` | query | string | No | Allowed values: `anime`, `manga`. |
| `preliminary` | query | boolean | No | Whether the results include preliminary reviews or not. Defaults to true. |
| `spoilers` | query | boolean | No | Whether the results include reviews with spoilers or not. Defaults to true. |

**Responses**

- **200** — Returns top reviews
  Body (`application/json`, object):
  - `data` (object)
    - `data` (array of one of several types)
      - `user` (object)
        - `username` (string) — MyAnimeList Username
        - `url` (string) — MyAnimeList Profile URL
        - `images` (object)
      - `anime` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList review URL
      - `type` (string) — Entry type
      - `reactions` (object) — User reaction count on the review
        - `overall` (integer) — Overall reaction count
        - `nice` (integer) — Nice reaction count
        - `love_it` (integer) — Love it reaction count
        - `funny` (integer) — Funny reaction count
        - `confusing` (integer) — Confusing reaction count
        - `informative` (integer) — Informative reaction count
        - `well_written` (integer) — Well written reaction count
        - `creative` (integer) — Creative reaction count
      - `date` (string) — Review created date ISO8601
      - `review` (string) — Review content
      - `score` (integer) — Number of user votes on the Review
      - `tags` (array of string) — Review tags
      - `is_spoiler` (boolean) — The review contains spoiler
      - `is_preliminary` (boolean) — The review was made before the entry was completed
      - `episodes_watched` (integer) — Number of episodes watched
      - `user` (object)
        - `username` (string) — MyAnimeList Username
        - `url` (string) — MyAnimeList Profile URL
        - `images` (object)
      - `manga` (object)
        - `mal_id` (integer) — MyAnimeList ID
        - `url` (string) — MyAnimeList URL
        - `images` (object)
        - `title` (string) — Entry title
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList review URL
      - `type` (string) — Entry type
      - `reactions` (object) — User reaction count on the review
        - `overall` (integer) — Overall reaction count
        - `nice` (integer) — Nice reaction count
        - `love_it` (integer) — Love it reaction count
        - `funny` (integer) — Funny reaction count
        - `confusing` (integer) — Confusing reaction count
        - `informative` (integer) — Informative reaction count
        - `well_written` (integer) — Well written reaction count
        - `creative` (integer) — Creative reaction count
      - `date` (string) — Review created date ISO8601
      - `review` (string) — Review content
      - `score` (integer) — Number of user votes on the Review
      - `tags` (array of string) — Review tags
      - `is_spoiler` (boolean) — The review contains spoiler
      - `is_preliminary` (boolean) — The review was made before the entry was completed
    - `pagination` (object)
      - `last_visible_page` (integer)
      - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

## watch

### GET /watch/episodes

**Responses**

- **200** — Returns Recently Added Episodes
  Body (`application/json`, object):
  - `data` (array of object)
    - `entry` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `episodes` (array of object) — Recent Episodes (max 2 listed)
      - `mal_id` (string) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `title` (string) — Episode Title
      - `premium` (boolean) — For MyAnimeList Premium Users
    - `region_locked` (boolean) — Region Locked Episode
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /watch/episodes/popular

**Responses**

- **200** — Returns Popular Episodes
  Body (`application/json`, object):
  - `data` (array of object)
    - `entry` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `episodes` (array of object) — Recent Episodes (max 2 listed)
      - `mal_id` (string) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `title` (string) — Episode Title
      - `premium` (boolean) — For MyAnimeList Premium Users
    - `region_locked` (boolean) — Region Locked Episode
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /watch/promos

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No |  |

**Responses**

- **200** — Returns Recently Added Promotional Videos
  Body (`application/json`, object):
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
  - `data` (array of object)
    - `title` (string) — Promo Title
    - `entry` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
      - `images` (object)
        - `image_url` (string) — Default Image Size URL (120x90). May be null.
        - `small_image_url` (string) — Small Image Size URL (640x480). May be null.
        - `medium_image_url` (string) — Medium Image Size URL (320x180). May be null.
        - `large_image_url` (string) — Large Image Size URL (480x360). May be null.
        - `maximum_image_url` (string) — Maximum Image Size URL (1280x720). May be null.
- **400** — Error: Bad request. When required parameters were not supplied.

### GET /watch/promos/popular

**Responses**

- **200** — Returns Popular Promotional Videos
  Body (`application/json`, object):
  - `pagination` (object)
    - `last_visible_page` (integer)
    - `has_next_page` (boolean)
  - `data` (array of object)
    - `title` (string) — Promo Title
    - `entry` (object)
      - `mal_id` (integer) — MyAnimeList ID
      - `url` (string) — MyAnimeList URL
      - `images` (object)
        - `jpg` (object) — Available images in JPG
        - `webp` (object) — Available images in WEBP
      - `title` (string) — Entry title
    - `trailer` (object) — Youtube Details
      - `youtube_id` (string) — YouTube ID. May be null.
      - `url` (string) — YouTube URL. May be null.
      - `embed_url` (string) — Parsed Embed URL. May be null.
      - `images` (object)
        - `image_url` (string) — Default Image Size URL (120x90). May be null.
        - `small_image_url` (string) — Small Image Size URL (640x480). May be null.
        - `medium_image_url` (string) — Medium Image Size URL (320x180). May be null.
        - `large_image_url` (string) — Large Image Size URL (480x360). May be null.
        - `maximum_image_url` (string) — Maximum Image Size URL (1280x720). May be null.
- **400** — Error: Bad request. When required parameters were not supplied.
