# Spaceflight News API — API Reference

The Spaceflight News API (SNAPI) is a product by [The Space Devs](https://thespacedevs.com) (TSD). It's the most complete and up-to-date spaceflight news API currently available.

While this API is **free to use**, we do encourage developers to support us through [Patreon](https://www.patreon.com/TheSpaceDevs) to keep the API up and running.

 ### GraphQL

 The Spaceflight News API also has GraphQL support available! You can find the GraphiQl IDE [here](https://api.spaceflightnewsapi.net/v4/graphql/).

 ### FAQs & Tutorials

 - [GitHub repository](https://github.com/TheSpaceDevs/Tutorials/): contains FAQs and tutorials for TSD APIs

 - [TSD FAQ](https://github.com/TheSpaceDevs/Tutorials/blob/main/faqs/faq_TSD.md): TSD-specific FAQ (e.g. history, network, funding, etc.)

 - [SNAPI FAQ](https://github.com/TheSpaceDevs/Tutorials/blob/main/faqs/faq_SNAPI.md): SNAPI-specific FAQ

 ### Feedback & Support

 If you need any help with SNAPI, you can ask in the [`💬feedback-and-help`](https://discord.com/channels/676725644444565514/1019976345884827750) forum of the TSD [Discord server](https://discord.gg/p7ntkNA) or email [derk@spaceflightnewsapi.net](mailto:derk@spaceflightnewsapi.net).

**Version:** 4.37.1 (v4)  
**Base URL:** `https://api.spaceflightnewsapi.net/v4`

## articles

### GET /v4/articles/

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `event` | query | array of integer | No | Search for all documents related to a specific event using its Launch Library 2 ID. |
| `has_event` | query | boolean | No | Get all documents that have a related event. |
| `has_launch` | query | boolean | No | Get all documents that have a related launch. |
| `is_featured` | query | boolean | No | Get all documents that are featured. |
| `launch` | query | array of string (uuid) | No | Search for all documents related to a specific launch using its Launch Library 2 ID. |
| `limit` | query | integer | No | Number of results to return per page. |
| `news_site` | query | string | No | Search for documents with a news_site__name present in a list of comma-separated values. Case insensitive. |
| `news_site_exclude` | query | string | No | Search for documents with a news_site__name not present in a list of comma-separated values. Case insensitive. |
| `offset` | query | integer | No | The initial index from which to return the results, at most 10,000. To go further back, filter on `published_at_lt` with the `published_at` of the last result instead. |
| `ordering` | query | array of string | No | Order the result on `published_at, -published_at, updated_at, -updated_at`. * `published_at` - Published at * `-published_at` - Published at (descending) * `updated_at` - Updated at * `-updated_at` - Updated at (descending) |
| `published_at_gt` | query | string (date-time) | No | Get all documents published after a given ISO8601 timestamp (excluded). |
| `published_at_gte` | query | string (date-time) | No | Get all documents published after a given ISO8601 timestamp (included). |
| `published_at_lt` | query | string (date-time) | No | Get all documents published before a given ISO8601 timestamp (excluded). |
| `published_at_lte` | query | string (date-time) | No | Get all documents published before a given ISO8601 timestamp (included). |
| `search` | query | string | No | Search for documents with a specific phrase in the title or summary. |
| `summary_contains` | query | string | No | Search for all documents with a specific phrase in the summary. |
| `summary_contains_all` | query | string | No | Search for documents with a summary containing all keywords from comma-separated values. |
| `summary_contains_one` | query | string | No | Search for documents with a summary containing at least one keyword from comma-separated values. |
| `title_contains` | query | string | No | Search for all documents with a specific phrase in the title. |
| `title_contains_all` | query | string | No | Search for documents with a title containing all keywords from comma-separated values. |
| `title_contains_one` | query | string | No | Search for documents with a title containing at least one keyword from comma-separated values. |
| `updated_at_gt` | query | string (date-time) | No | Get all documents updated after a given ISO8601 timestamp (excluded). |
| `updated_at_gte` | query | string (date-time) | No | Get all documents updated after a given ISO8601 timestamp (included). |
| `updated_at_lt` | query | string (date-time) | No | Get all documents updated before a given ISO8601 timestamp (excluded). |
| `updated_at_lte` | query | string (date-time) | No | Get all documents updated before a given ISO8601 timestamp (included). |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `id` (integer, required)
    - `title` (string, required) — Max length: 500.
    - `authors` (array of object, required)
      - `name` (string, required) — Max length: 250.
      - `socials` (object)
        - `x` (one of several types)
        - `youtube` (one of several types)
        - `instagram` (one of several types)
        - `linkedin` (one of several types)
        - `mastodon` (one of several types)
        - `bluesky` (one of several types)
    - `url` (string (uri), required) — Max length: 500.
    - `image_url` (string (uri), required) — Max length: 500.
    - `news_site` (string, required)
    - `summary` (string, required)
    - `published_at` (string (date-time), required)
    - `updated_at` (string (date-time), required)
    - `featured` (boolean)
    - `launches` (array of object, required)
      - `launch_id` (string (uuid), required)
      - `provider` (string, required)
    - `events` (array of object, required)
      - `event_id` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `provider` (string, required)

### GET /v4/articles/{id}/

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes | A unique integer value identifying this article. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `title` (string, required) — Max length: 500.
  - `authors` (array of object, required)
    - `name` (string, required) — Max length: 250.
    - `socials` (object)
      - `x` (one of several types)
      - `youtube` (one of several types)
      - `instagram` (one of several types)
      - `linkedin` (one of several types)
      - `mastodon` (one of several types)
      - `bluesky` (one of several types)
  - `url` (string (uri), required) — Max length: 500.
  - `image_url` (string (uri), required) — Max length: 500.
  - `news_site` (string, required)
  - `summary` (string, required)
  - `published_at` (string (date-time), required)
  - `updated_at` (string (date-time), required)
  - `featured` (boolean)
  - `launches` (array of object, required)
    - `launch_id` (string (uuid), required)
    - `provider` (string, required)
  - `events` (array of object, required)
    - `event_id` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `provider` (string, required)

## blogs

### GET /v4/blogs/

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `event` | query | array of integer | No | Search for all documents related to a specific event using its Launch Library 2 ID. |
| `has_event` | query | boolean | No | Get all documents that have a related event. |
| `has_launch` | query | boolean | No | Get all documents that have a related launch. |
| `is_featured` | query | boolean | No | Get all documents that are featured. |
| `launch` | query | array of string (uuid) | No | Search for all documents related to a specific launch using its Launch Library 2 ID. |
| `limit` | query | integer | No | Number of results to return per page. |
| `news_site` | query | string | No | Search for documents with a news_site__name present in a list of comma-separated values. Case insensitive. |
| `news_site_exclude` | query | string | No | Search for documents with a news_site__name not present in a list of comma-separated values. Case insensitive. |
| `offset` | query | integer | No | The initial index from which to return the results, at most 10,000. To go further back, filter on `published_at_lt` with the `published_at` of the last result instead. |
| `ordering` | query | array of string | No | Order the result on `published_at, -published_at, updated_at, -updated_at`. * `published_at` - Published at * `-published_at` - Published at (descending) * `updated_at` - Updated at * `-updated_at` - Updated at (descending) |
| `published_at_gt` | query | string (date-time) | No | Get all documents published after a given ISO8601 timestamp (excluded). |
| `published_at_gte` | query | string (date-time) | No | Get all documents published after a given ISO8601 timestamp (included). |
| `published_at_lt` | query | string (date-time) | No | Get all documents published before a given ISO8601 timestamp (excluded). |
| `published_at_lte` | query | string (date-time) | No | Get all documents published before a given ISO8601 timestamp (included). |
| `search` | query | string | No | Search for documents with a specific phrase in the title or summary. |
| `summary_contains` | query | string | No | Search for all documents with a specific phrase in the summary. |
| `summary_contains_all` | query | string | No | Search for documents with a summary containing all keywords from comma-separated values. |
| `summary_contains_one` | query | string | No | Search for documents with a summary containing at least one keyword from comma-separated values. |
| `title_contains` | query | string | No | Search for all documents with a specific phrase in the title. |
| `title_contains_all` | query | string | No | Search for documents with a title containing all keywords from comma-separated values. |
| `title_contains_one` | query | string | No | Search for documents with a title containing at least one keyword from comma-separated values. |
| `updated_at_gt` | query | string (date-time) | No | Get all documents updated after a given ISO8601 timestamp (excluded). |
| `updated_at_gte` | query | string (date-time) | No | Get all documents updated after a given ISO8601 timestamp (included). |
| `updated_at_lt` | query | string (date-time) | No | Get all documents updated before a given ISO8601 timestamp (excluded). |
| `updated_at_lte` | query | string (date-time) | No | Get all documents updated before a given ISO8601 timestamp (included). |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `id` (integer, required)
    - `title` (string, required) — Max length: 500.
    - `authors` (array of object, required)
      - `name` (string, required) — Max length: 250.
      - `socials` (object)
        - `x` (one of several types)
        - `youtube` (one of several types)
        - `instagram` (one of several types)
        - `linkedin` (one of several types)
        - `mastodon` (one of several types)
        - `bluesky` (one of several types)
    - `url` (string (uri), required) — Max length: 500.
    - `image_url` (string (uri), required) — Max length: 500.
    - `news_site` (string, required)
    - `summary` (string, required)
    - `published_at` (string (date-time), required)
    - `updated_at` (string (date-time), required)
    - `featured` (boolean)
    - `launches` (array of object, required)
      - `launch_id` (string (uuid), required)
      - `provider` (string, required)
    - `events` (array of object, required)
      - `event_id` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `provider` (string, required)

### GET /v4/blogs/{id}/

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes | A unique integer value identifying this blog. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `title` (string, required) — Max length: 500.
  - `authors` (array of object, required)
    - `name` (string, required) — Max length: 250.
    - `socials` (object)
      - `x` (one of several types)
      - `youtube` (one of several types)
      - `instagram` (one of several types)
      - `linkedin` (one of several types)
      - `mastodon` (one of several types)
      - `bluesky` (one of several types)
  - `url` (string (uri), required) — Max length: 500.
  - `image_url` (string (uri), required) — Max length: 500.
  - `news_site` (string, required)
  - `summary` (string, required)
  - `published_at` (string (date-time), required)
  - `updated_at` (string (date-time), required)
  - `featured` (boolean)
  - `launches` (array of object, required)
    - `launch_id` (string (uuid), required)
    - `provider` (string, required)
  - `events` (array of object, required)
    - `event_id` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `provider` (string, required)

## info

### GET /v4/info/

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `version` (string, required)
  - `news_sites` (array of string, required)

## reports

### GET /v4/reports/

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `news_site` | query | string | No | Search for documents with a news_site__name present in a list of comma-separated values. Case insensitive. |
| `news_site_exclude` | query | string | No | Search for documents with a news_site__name not present in a list of comma-separated values. Case insensitive. |
| `offset` | query | integer | No | The initial index from which to return the results, at most 10,000. To go further back, filter on `published_at_lt` with the `published_at` of the last result instead. |
| `ordering` | query | array of string | No | Order the result on `published_at, -published_at, updated_at, -updated_at`. * `published_at` - Published at * `-published_at` - Published at (descending) * `updated_at` - Updated at * `-updated_at` - Updated at (descending) |
| `published_at_gt` | query | string (date-time) | No | Get all documents published after a given ISO8601 timestamp (excluded). |
| `published_at_gte` | query | string (date-time) | No | Get all documents published after a given ISO8601 timestamp (included). |
| `published_at_lt` | query | string (date-time) | No | Get all documents published before a given ISO8601 timestamp (excluded). |
| `published_at_lte` | query | string (date-time) | No | Get all documents published before a given ISO8601 timestamp (included). |
| `search` | query | string | No | Search for documents with a specific phrase in the title or summary. |
| `summary_contains` | query | string | No | Search for all documents with a specific phrase in the summary. |
| `summary_contains_all` | query | string | No | Search for documents with a summary containing all keywords from comma-separated values. |
| `summary_contains_one` | query | string | No | Search for documents with a summary containing at least one keyword from comma-separated values. |
| `title_contains` | query | string | No | Search for all documents with a specific phrase in the title. |
| `title_contains_all` | query | string | No | Search for documents with a title containing all keywords from comma-separated values. |
| `title_contains_one` | query | string | No | Search for documents with a title containing at least one keyword from comma-separated values. |
| `updated_at_gt` | query | string (date-time) | No | Get all documents updated after a given ISO8601 timestamp (excluded). |
| `updated_at_gte` | query | string (date-time) | No | Get all documents updated after a given ISO8601 timestamp (included). |
| `updated_at_lt` | query | string (date-time) | No | Get all documents updated before a given ISO8601 timestamp (excluded). |
| `updated_at_lte` | query | string (date-time) | No | Get all documents updated before a given ISO8601 timestamp (included). |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `id` (integer, required)
    - `title` (string, required) — Max length: 500.
    - `authors` (array of object, required)
      - `name` (string, required) — Max length: 250.
      - `socials` (object)
        - `x` (one of several types)
        - `youtube` (one of several types)
        - `instagram` (one of several types)
        - `linkedin` (one of several types)
        - `mastodon` (one of several types)
        - `bluesky` (one of several types)
    - `url` (string (uri), required) — Max length: 500.
    - `image_url` (string (uri), required) — Max length: 500.
    - `news_site` (string, required)
    - `summary` (string)
    - `published_at` (string (date-time), required)
    - `updated_at` (string (date-time), required)

### GET /v4/reports/{id}/

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes | A unique integer value identifying this report. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `title` (string, required) — Max length: 500.
  - `authors` (array of object, required)
    - `name` (string, required) — Max length: 250.
    - `socials` (object)
      - `x` (one of several types)
      - `youtube` (one of several types)
      - `instagram` (one of several types)
      - `linkedin` (one of several types)
      - `mastodon` (one of several types)
      - `bluesky` (one of several types)
  - `url` (string (uri), required) — Max length: 500.
  - `image_url` (string (uri), required) — Max length: 500.
  - `news_site` (string, required)
  - `summary` (string)
  - `published_at` (string (date-time), required)
  - `updated_at` (string (date-time), required)
