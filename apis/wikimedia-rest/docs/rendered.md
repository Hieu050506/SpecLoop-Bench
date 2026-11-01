# Wikimedia REST API — API Reference

This API provides cacheable and straightforward access to Wikimedia content and data, in machine-readable formats.

Caution: The REST Sandbox executes calls against the production database by default. To avoid unintended edits to live content, select the sandbox server (test.wikimedia.org) from the server dropdown before making POST, PUT, PATCH, or DELETE requests.
### Global Rules
- Limit your clients to no more than 200 requests/s to this API.
  Each API endpoint's documentation may detail more specific usage limits.
- Set a unique `User-Agent` or `Api-User-Agent` header that
  allows us to contact you quickly. Email addresses or URLs
  of contact pages work well.

By using this API, you agree to Wikimedia's [Terms of Use](https://wikimediafoundation.org/wiki/Terms_of_Use) and [Privacy Policy](https://wikimediafoundation.org/wiki/Privacy_policy). Unless otherwise specified in the endpoint documentation below, content accessed via this API is licensed under the [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) and [GFDL](https://www.gnu.org/copyleft/fdl.html) licenses, and you irrevocably agree to release modifications or additions made through this API under these licenses. Check the [Wikimedia REST API documentation](https://www.mediawiki.org/wiki/Wikimedia_REST_API) for background and details.
### Endpoint documentation
Please consult each endpoint's documentation for details on:
- Licensing information for the specific type of content
  and data served via the endpoint.
- Stability markers to inform you about development status and
  change policy, according to
  [our API version policy](https://www.mediawiki.org/wiki/API_versioning).
- Endpoint specific usage limits.

**Version:** 1.0.0  
**Base URL:** `https://en.wikipedia.org/api/rest_v1`

## Page content

page content in different formats

### GET /page/

**List page-related API entry points.**

Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)

**Responses**

- **200** — A list of page-related API end points.
  Body (`application/json`, object):
  - `items` (array of string, required)
  - `_links` (object)
    - `next` (object)
      - `href` (string) — Relative link to next result page.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/title/{title}

**Get revision metadata for a title.**

Returns the revision metadata for the given title. If a revision ID is provided,
metadata for that revision is returned, otherwise the latest revision ID is assumed.

Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable).

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |

**Responses**

- **200** — The latest revision metadata for the provided title.
  Body (`application/json`, object):
  - `count` (integer (int32), required)
  - `items` (object, required) — Complete information about the revision
    - `title` (string)
    - `page_id` (integer (int32))
    - `rev` (integer (int32))
    - `tid` (string)
    - `comment` (string)
    - `restrictions` (array of string)
    - `tags` (array of string)
    - `user_id` (integer (int32))
    - `user_text` (string)
    - `timestamp` (string (date-time))
    - `redirect` (boolean)
    - `page_language` (string)
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid these redirects, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title or no revisions found.
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/title/{title}/{revision}

**Get revision metadata for a title.**

Returns the revision metadata for the given title. If a revision ID is provided,
metadata for that revision is returned, otherwise the latest revision ID is assumed.

Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable).

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | The revision id |

**Responses**

- **200** — The latest revision metadata for the provided title.
  Body (`application/json`, object):
  - `count` (integer (int32), required)
  - `items` (object, required) — Complete information about the revision
    - `title` (string)
    - `page_id` (integer (int32))
    - `rev` (integer (int32))
    - `tid` (string)
    - `comment` (string)
    - `restrictions` (array of string)
    - `tags` (array of string)
    - `user_id` (integer (int32))
    - `user_text` (string)
    - `timestamp` (string (date-time))
    - `redirect` (boolean)
    - `page_language` (string)
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid these redirects, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title or no revisions found.
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/html/{title}

**Get latest HTML for a title.**

Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |
| `stash` | query | boolean | No | Whether to temporary stash data-parsoid metadata in order to support transforming the modified content later. If this parameter is set, requests are rate-limited on a per-client basis (max 5 requests per second per client) |
| `Accept-Language` | header | string | No | The desired language variant code for wikis where LanguageConverter is enabled. Example: `sr-el` for Latin transcription of the Serbian language. |

**Responses**

- **200** — The latest HTML for the given page title. See [the MediaWiki DOM spec](https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec) for a description of the MediaWiki-specific semantic markup in this HTML. Note that additional metadata is available in the HTML head.
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target, and the body contains the actual page contents as HTML. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/html/{title}/{revision}

**Get HTML for a specific title/revision & optionally timeuuid.**

Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | The revision |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |
| `stash` | query | boolean | No | Whether to temporary stash data-parsoid metadata in order to support transforming the modified content later. If this parameter is set, requests are rate-limited on a per-client basis (max 5 requests per second per client) |
| `Accept-Language` | header | string | No | The desired language variant code for wikis where LanguageConverter is enabled. Example: `sr-el` for Latin transcription of the Serbian language. |

**Responses**

- **200** — The html for the given page, revision and tid. See [the MediaWiki DOM spec](https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec) for a description of the MediaWiki-specific semantic markup in this HTML. Note that additional metadata is available in the HTML head. This HTML can be edited using arbitrary HTML tools. The modified HTML can be converted back to wikitext using the [/transform/html/to/wikitext{/title}{/revision}](#!/Transforms/transform_html_to_wikitext__title___revision__post) entry point.
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target, and the body contains the actual page revision contents as HTML. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **400** — Invalid revision or tid
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **403** — Access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page, revision or tid
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/lint/{title}

**Get the linter errors for a specific title/revision.**

Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |

**Responses**

- **200** — The lint errors for the given page and optionally revision. See [the Linter extension docs](https://www.mediawiki.org/wiki/Extension:Linter) for more details.
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target, and the body contains the actual page revision contents as HTML. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **400** — Invalid revision or tid
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **403** — Access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page, revision or tid
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/lint/{title}/{revision}

**Get the linter errors for a specific title/revision.**

Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | The revision |

**Responses**

- **200** — The lint errors for the given page and optionally revision. See [the Linter extension docs](https://www.mediawiki.org/wiki/Extension:Linter) for more details.
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target, and the body contains the actual page revision contents as HTML. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **400** — Invalid revision or tid
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **403** — Access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page, revision or tid
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/summary/{title}

**Get basic metadata and simplified article introduction.**

The summary response includes an extract of the first paragraph of the page in plain text
and HTML as well as the type of page. This is useful for page previews (fka. Hovercards,
aka. Popups) on the web and link previews in the apps.

Stability: [stable](https://www.mediawiki.org/wiki/Wikimedia_Product/Wikimedia_Product_Infrastructure_team/API_endpoint_stability_policy#Stable)

Please follow [wikitech-l](https://lists.wikimedia.org/mailman/listinfo/wikitech-l) or [mediawiki-api-announce](https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce) for announcements of breaking changes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |
| `Accept-Language` | header | string | No | The desired language variant code for wikis where LanguageConverter is enabled. Example: `sr-el` for Latin transcription of the Serbian language. |

**Responses**

- **200** — The summary for the given page
  Body (`application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.4.2"`, object):
  - `titles` (object, required) — a good example of the differences can be seen in https://en.wikipedia.org/api/rest_v1/page/summary/IOS_13
    - `canonical` (string, required) — the DB key (non-prefixed), e.g. may have _ instead of spaces, best for making request URIs, still requires Percent-encoding
    - `normalized` (string, required) — the normalized title (https://www.mediawiki.org/wiki/API:Query#Example_2:_Title_normalization), e.g. may have spaces instead of _
    - `display` (string, required) — the title as it should be displayed to the user
  - `title` (string) — The page title. Deprecated: Use `titles.normalized` instead.
  - `displaytitle` (string) — The page title how it should be shown to the user. Deprecated: Use `titles.display` instead.
  - `pageid` (integer) — The page ID
  - `extract` (string, required) — First several sentences of an article in plain text
  - `extract_html` (string) — First several sentences of an article in simple HTML format
  - `thumbnail` (object)
    - `source` (string, required) — Thumbnail image URI
    - `width` (integer, required) — Thumbnail width
    - `height` (integer, required) — Thumnail height
  - `originalimage` (object)
    - `source` (string, required) — Original image URI
    - `width` (integer, required) — Original image width
    - `height` (integer, required) — Original image height
  - `lang` (string, required) — The page language code
  - `dir` (string, required) — The page language direction code
  - `timestamp` (string) — The time when the page was last edited in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
  - `description` (string) — Wikidata description for the page
  - `coordinates` (object) — The coordinates of the item
    - `lat` (number, required) — The latitude
    - `lon` (number, required) — The longitude
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/media-list/{title}

**Get list of media files used on a page.**

Gets the list of media items (images, audio, and video) in the order in which they appear on a
given wiki page.

Stability: [unstable](https://www.mediawiki.org/wiki/Wikimedia_Product/Wikimedia_Product_Infrastructure_team/API_endpoint_stability_policy#Unstable)

Please follow [wikitech-l](https://lists.wikimedia.org/mailman/listinfo/wikitech-l) or [mediawiki-api-announce](https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce) for announcements of breaking changes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |

**Responses**

- **200** — JSON containing metadata of media items appearing on the given page.
  Body (`application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Media/1.3.1"`, object):
  - `revision` (string, required) — the revision ID used to create the list
  - `tid` (string, required) — the time uuid of the page rendering used to create the list
  - `items` (array of object, required) — a list of media items
    - `title` (string) — The file page title
    - `type` (string, required) — Allowed values: `image`, `video`, `audio`.
    - `section_id` (integer, required) — section ID in which the item is found on the page
    - `showInGallery` (boolean, required) — whether the client should show the file in an image gallery presentation
    - `caption` (object)
      - `html` (string) — on-wiki caption for the media item, including all HTML markup
      - `text` (string) — plain text of the on-wiki caption for the media item
    - `original` (object) — reference to a Mathoid-rendered math formula image
      - `source` (string) — Mathoid image render URL
      - `mime` (string) — the Mathoid image mime type
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/media-list/{title}/{revision}

**Get list of media files used on a page.**

Gets the list of media items (images, audio, and video) in the order in which they appear on a
given wiki page.

Stability: [unstable](https://www.mediawiki.org/wiki/Wikimedia_Product/Wikimedia_Product_Infrastructure_team/API_endpoint_stability_policy#Unstable)

Please follow [wikitech-l](https://lists.wikimedia.org/mailman/listinfo/wikitech-l) or [mediawiki-api-announce](https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce) for announcements of breaking changes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | Optional page revision. Note that older revisions are not stored, so request latency with the revision would be higher. |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |

**Responses**

- **200** — JSON containing metadata of media items appearing on the given page.
  Body (`application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Media/1.3.1"`, object):
  - `revision` (string, required) — the revision ID used to create the list
  - `tid` (string, required) — the time uuid of the page rendering used to create the list
  - `items` (array of object, required) — a list of media items
    - `title` (string) — The file page title
    - `type` (string, required) — Allowed values: `image`, `video`, `audio`.
    - `section_id` (integer, required) — section ID in which the item is found on the page
    - `showInGallery` (boolean, required) — whether the client should show the file in an image gallery presentation
    - `caption` (object)
      - `html` (string) — on-wiki caption for the media item, including all HTML markup
      - `text` (string) — plain text of the on-wiki caption for the media item
    - `original` (object) — reference to a Mathoid-rendered math formula image
      - `source` (string) — Mathoid image render URL
      - `mime` (string) — the Mathoid image mime type
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/mobile-html/{title}

**Get page content HTML optimized for mobile consumption.**

Gets the content HTML optimized for mobile consumption for the given page. This content
is derived from Parsoid HTML (see `/page/html/{title}` endpoint).
The difference to Parsoid HTML is roughly:
* Some elements and attributes not needed for the reading case are removed.
* LeadIntroductionTransform: The introductory paragraph is moved before an infobox.
* RedLinks: Red links are flattened (=turned into span elements).
* WidenImage: images that should be displayed in gallery are widened.
* Section headings are slightly changed by wrapping the headings inside a div and adding
  a span element inside the new div for the edit buttons.
* Additional classes are added to img elements to fix issues with non-white backgrounds.
  See Theme support below for instructions on how to enable that.
* Pagelib CSS files needed to display the content are referenced.
* LazyLoadTransform: server-side portion/prep for lazy loading of images.
* CollapseTable: server-side portion/prep for collapsing tables.

What's not included? What parts of the PageLibrary does a client still have to do?
* Theme support: Themes can be turned on by adding a theme class to the root <html> tag.
  Possible class names are:
  * `pagelib_theme_default`
  * `pagelib_theme_dark`
  * `pagelib_theme_black`
  * `pagelib_theme_sepia`

  The pagelib JS has functionality to do that: ThemeTransform.setTheme(document, theme).
* Dim images: DimImagesTransform.dim(window, enable)
* PlatformTransform.classify(window) to trigger Android and iOS app specific CSS rules
* LazyLoadTransformer: client side companion of LazyLoadTransform (note the extra *er*
here)
* FooterTransformer: seems to be more UI than content, requires I18N, too

Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |

**Responses**

- **200** — mobile-optimized HTML of the given page.
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/mobile-html/{title}/{revision}

**Get page content HTML optimized for mobile consumption.**

Gets the content HTML optimized for mobile consumption for the given page. This content
is derived from Parsoid HTML (see `/page/html/{title}` endpoint).
The difference to Parsoid HTML is roughly:
* Some elements and attributes not needed for the reading case are removed.
* LeadIntroductionTransform: The introductory paragraph is moved before an infobox.
* RedLinks: Red links are flattened (=turned into span elements).
* WidenImage: images that should be displayed in gallery are widened.
* Section headings are slightly changed by wrapping the headings inside a div and adding
  a span element inside the new div for the edit buttons.
* Additional classes are added to img elements to fix issues with non-white backgrounds.
  See Theme support below for instructions on how to enable that.
* Pagelib CSS files needed to display the content are referenced.
* LazyLoadTransform: server-side portion/prep for lazy loading of images.
* CollapseTable: server-side portion/prep for collapsing tables.

What's not included? What parts of the PageLibrary does a client still have to do?
* Theme support: Themes can be turned on by adding a theme class to the root <html> tag.
  Possible class names are:
  * `pagelib_theme_default`
  * `pagelib_theme_dark`
  * `pagelib_theme_black`
  * `pagelib_theme_sepia`

  The pagelib JS has functionality to do that: ThemeTransform.setTheme(document, theme).
* Dim images: DimImagesTransform.dim(window, enable)
* PlatformTransform.classify(window) to trigger Android and iOS app specific CSS rules
* LazyLoadTransformer: client side companion of LazyLoadTransform (note the extra *er*
here)
* FooterTransformer: seems to be more UI than content, requires I18N, too

Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | Optional page revision. Note that older revisions are not stored, so request latency with the revision would be higher. |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |

**Responses**

- **200** — mobile-optimized HTML of the given page.
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/mobile-html-offline-resources/{title}

**Get styles and scripts for offline consumption of mobile-html-formatted pages**

Provides links to scripts and styles needed for viewing mobile-html-formatted pages offline.

Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |

**Responses**

- **200** — links to scripts and styles to accompany the mobile-html of the page for offline consumption
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/mobile-html-offline-resources/{title}/{revision}

**Get styles and scripts for offline consumption of mobile-html-formatted pages**

Provides links to scripts and styles needed for viewing mobile-html-formatted pages offline.

Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | Optional page revision. Note that older revisions are not stored, so request latency with the revision would be higher. |

**Responses**

- **200** — links to scripts and styles to accompany the mobile-html of the page for offline consumption
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

## Talk pages

### GET /page/talk/{title}

**Get structured talk page contents**

Gets structured talk page contents for the provided title.

Stability: [experimental](https://www.mediawiki.org/wiki/Wikimedia_Product/Wikimedia_Product_Infrastructure_team/API_endpoint_stability_policy#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |

**Responses**

- **200** — structured talk page JSON.
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /page/talk/{title}/{revision}

**Get structured talk page contents**

Gets structured talk page contents for the provided title.

Stability: [experimental](https://www.mediawiki.org/wiki/Wikimedia_Product/Wikimedia_Product_Infrastructure_team/API_endpoint_stability_policy#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | Optional page revision. Note that older revisions are not stored, so request latency with the revision would be higher. |
| `redirect` | query | boolean | No | Requests for [redirect pages](https://www.mediawiki.org/wiki/Help:Redirects) return HTTP 302 with a redirect target in `Location` header and content in the body. To get a 200 response instead, supply `false` to the `redirect` parameter. |

**Responses**

- **200** — structured talk page JSON.
- **301** — A permanent redirect is returned if the supplied article title was not in the normalized form. To avoid this kind of redirect, you can use the [mediawiki-title](https://github.com/wikimedia/mediawiki-title) library to perform title normalization client-side. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **302** — The page is a [redirect page](https://www.mediawiki.org/wiki/Help:Redirects). The `location` header points to the redirect target. If you would like to avoid automatically following redirect pages, set the `redirect=false` query parameter. Beware that redirected pre-flighted cross-origin requests (such as those sending custom request headers like `Api-User-Agent`) will fail in most current browsers [due to a spec bug](https://github.com/whatwg/fetch/issues/204).
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

## Transforms

convert content between HTML and Wikitext

### POST /transform/html/to/wikitext

**Transform HTML to Wikitext**

Transform [Parsoid HTML](https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec)
to Wikitext.

When converting pre-existing (possibly modified) content, you should
pass in the `title`, `revision`, and `If-Match` header. This lets
[Parsoid](https://www.mediawiki.org/wiki/Parsoid) preserve small
syntactic variations in wikitext, which ensures that diffs are
readable.

- Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)
- Rate limit: 25 req/s

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `if-match` | header | string | No | The `ETag` header of the original render indicating it's revision and timeuuid. Required if both `title` and `revision` parameters are present. |

**Request body** (`multipart/form-data`, required)

- `html` (string, required) — The HTML to transform
- `scrub_wikitext` (boolean) — Normalise the DOM to yield cleaner wikitext?

**Responses**

- **200** — MediaWiki Wikitext.
- **403** — Access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page title or revision
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/html/to/wikitext/{title}

**Transform HTML to Wikitext**

Transform [Parsoid HTML](https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec)
to Wikitext.

When converting pre-existing (possibly modified) content, you should
pass in the `title`, `revision`, and `If-Match` header. This lets
[Parsoid](https://www.mediawiki.org/wiki/Parsoid) preserve small
syntactic variations in wikitext, which ensures that diffs are
readable.

- Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)
- Rate limit: 25 req/s

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `if-match` | header | string | No | The `ETag` header of the original render indicating it's revision and timeuuid. Required if both `title` and `revision` parameters are present. |

**Request body** (`multipart/form-data`, required)

- `html` (string, required) — The HTML to transform
- `scrub_wikitext` (boolean) — Normalise the DOM to yield cleaner wikitext?

**Responses**

- **200** — MediaWiki Wikitext.
- **403** — Access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page title or revision
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/html/to/wikitext/{title}/{revision}

**Transform HTML to Wikitext**

Transform [Parsoid HTML](https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec)
to Wikitext.

When converting pre-existing (possibly modified) content, you should
pass in the `title`, `revision`, and `If-Match` header. This lets
[Parsoid](https://www.mediawiki.org/wiki/Parsoid) preserve small
syntactic variations in wikitext, which ensures that diffs are
readable.

- Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)
- Rate limit: 25 req/s

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | The page revision |
| `if-match` | header | string | No | The `ETag` header of the original render indicating it's revision and timeuuid. Required if both `title` and `revision` parameters are present. |

**Request body** (`multipart/form-data`, required)

- `html` (string, required) — The HTML to transform
- `scrub_wikitext` (boolean) — Normalise the DOM to yield cleaner wikitext?

**Responses**

- **200** — MediaWiki Wikitext.
- **403** — Access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page title or revision
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/wikitext/to/html

**Transform Wikitext to HTML**

Transform wikitext to HTML. Note that if you set `stash: true`, you
also need to supply the title.

- Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)
- Rate limit: 25 req/s (5 req/s when `stash: true`)

**Request body** (`multipart/form-data`, required)

- `wikitext` (string, required) — The Wikitext to transform to HTML
- `body_only` (boolean) — Return only `body.innerHTML`
- `stash` (boolean) — Whether to temporarily stash the result of the transformation

**Responses**

- **200** — See wikipage https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec
- **403** — access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page title or revision
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/wikitext/to/html/{title}

**Transform Wikitext to HTML**

Transform wikitext to HTML. Note that if you set `stash: true`, you
also need to supply the title.

- Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)
- Rate limit: 25 req/s (5 req/s when `stash: true`)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |

**Request body** (`multipart/form-data`, required)

- `wikitext` (string, required) — The Wikitext to transform to HTML
- `body_only` (boolean) — Return only `body.innerHTML`
- `stash` (boolean) — Whether to temporarily stash the result of the transformation

**Responses**

- **200** — See wikipage https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec
- **403** — access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page title or revision
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/wikitext/to/html/{title}/{revision}

**Transform Wikitext to HTML**

Transform wikitext to HTML. Note that if you set `stash: true`, you
also need to supply the title.

- Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable)
- Rate limit: 25 req/s (5 req/s when `stash: true`)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | The page revision |

**Request body** (`multipart/form-data`, required)

- `wikitext` (string, required) — The Wikitext to transform to HTML
- `body_only` (boolean) — Return only `body.innerHTML`
- `stash` (boolean) — Whether to temporarily stash the result of the transformation

**Responses**

- **200** — See wikipage https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec
- **403** — access to the specific revision is restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **404** — Unknown page title or revision
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/wikitext/to/lint

**Check Wikitext for lint errors**

Parse the supplied wikitext and check it for lint errors.

- Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)
- Rate limit: 25 req/s

**Request body** (`multipart/form-data`, required)

- `wikitext` (string, required) — The Wikitext to check

**Responses**

- **200** — Linter errors, if any, as a JSON blob
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Latest revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/wikitext/to/lint/{title}

**Check Wikitext for lint errors**

Parse the supplied wikitext and check it for lint errors.

- Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)
- Rate limit: 25 req/s

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |

**Request body** (`multipart/form-data`, required)

- `wikitext` (string, required) — The Wikitext to check

**Responses**

- **200** — Linter errors, if any, as a JSON blob
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Latest revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/wikitext/to/lint/{title}/{revision}

**Check Wikitext for lint errors**

Parse the supplied wikitext and check it for lint errors.

- Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)
- Rate limit: 25 req/s

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `revision` | path | integer | Yes | The page revision |

**Request body** (`multipart/form-data`, required)

- `wikitext` (string, required) — The Wikitext to check

**Responses**

- **200** — Linter errors, if any, as a JSON blob
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **409** — Latest revision was restricted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **410** — Page was deleted
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /transform/wikitext/to/mobile-html/{title}

**Transform Wikitext to Mobile HTML**

Transform wikitext to Mobile HTML.

- Stability: [stable](https://www.mediawiki.org/wiki/Wikimedia_Product/Wikimedia_Product_Infrastructure_team/API_endpoint_stability_policy#Stable)
- Rate limit: 25 req/s (5 req/s when `stash: true`)

Please follow [wikitech-l](https://lists.wikimedia.org/mailman/listinfo/wikitech-l) or [mediawiki-api-announce](https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce) for announcements of breaking changes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `title` | path | string | Yes | Page title. Use underscores instead of spaces. Use percent-encoding. Example: `Main_Page`. |
| `Accept-Language` | header | string | No | The desired language variant code for wikis where LanguageConverter is enabled. Example: `sr-el` for Latin transcription of the Serbian language. |
| `output-mode` | header | string | No | Output mode for mobile-html. Default is `editPreview`. Allowed values: `editPreview`, `contentAndReferences`, `content`, `references`. |

**Request body** (`multipart/form-data`, required)

- `wikitext` (string, required) — The Wikitext to transform to HTML

**Responses**

- **200** — See wikipage https://www.mediawiki.org/wiki/Parsoid/MediaWiki_DOM_spec
- **404** — Unknown page title
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

## Math

formula rendering

### POST /media/math/check/{type}

**Check and normalize a TeX formula.**

Checks the supplied TeX formula for correctness and returns the
normalised formula representation as well as information about
identifiers. Available types are tex and inline-tex. The response
contains the `x-resource-location` header which can be used to retrieve
the render of the checked formula in one of the supported rendering
formats. Just append the value of the header to `/media/math/{format}/`
and perform a GET request against that URL.

**NOTE**: the use of this endpoint is *strongly discouraged*. Instead, use the identical endpoint of the (canonical) Math API on the `wikimedia.org` domain.

Stability: [deprecated](https://www.mediawiki.org/wiki/API_versioning#Deprecated).

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | path | string | Yes | The input type of the given formula; can be tex or inline-tex. Allowed values: `tex`, `inline-tex`, `chem`. |

**Request body** (`multipart/form-data`, required)

- `q` (string, required) — The formula to check

**Responses**

- **200** — Information about the checked formula
- **400** — Invalid type
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /media/math/formula/{hash}

**Get a previously-stored formula**

Returns the previously-stored formula via `/media/math/check/{type}` for
the given hash.

**NOTE**: the use of this endpoint is *strongly discouraged*. Instead, use the identical endpoint of the (canonical) Math API on the `wikimedia.org` domain.

Stability: [deprecated](https://www.mediawiki.org/wiki/API_versioning#Deprecated).

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hash` | path | string | Yes | The hash string of the previous POST data. Min length: 1. |

**Responses**

- **200** — Information about the checked formula
- **404** — Data for the given hash cannot be found
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /media/math/render/{format}/{hash}

**Get rendered formula in the given format.**

Given a request hash, renders a TeX formula into its mathematic
representation in the given format. When a request is issued to the
`/media/math/check/{format}` POST endpoint, the response contains the
`x-resource-location` header denoting the hash ID of the POST data. Once
obtained, this endpoint has to be used to obtain the actual render.

**NOTE**: the use of this endpoint is *strongly discouraged*. Instead, use the identical endpoint of the (canonical) Math API on the `wikimedia.org` domain.

Stability: [deprecated](https://www.mediawiki.org/wiki/API_versioning#Deprecated).

> Deprecated.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `format` | path | string | Yes | The output format; can be svg or mml. Allowed values: `svg`, `mml`, `png`. |
| `hash` | path | string | Yes | The hash string of the previous POST data. Min length: 1. |

**Responses**

- **200** — The rendered formula
- **404** — Unknown format or hash ID
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

## Citation

generation of citation data

### GET /data/citation/{format}/{query}

**Get citation data given an article identifier.**

Generates citation data given a URL, DOI, PMID, or PMCID.

Automated requests can be made at a rate of 1 request per second (rps).

See more at [Citoid service documentation](https://www.mediawiki.org/wiki/Citoid)

The citation data can be requested in one of the following formats:
  - `mediawiki`: format designed for MediaWiki to be used with `templateData`.
    Uses [Zotero field names](https://aurimasv.github.io/z2csl/typeMap.xml).
  - `mediawiki-basefields`: `mediawiki` format with Zotero `basefield` field names.
  - `zotero`: format used by [Zotero](https://www.zotero.org/).
  - `bibtex`: format used in conjunction with LaTeX documents.
    See [bibtex.org](http://www.bibtex.org/).
  - `wikibase`: format designed for [Wikibase](https://www.mediawiki.org/wiki/Extension:Wikibase_Repository).

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `format` | path | string | Yes | The format to use for the resulting citation data. Allowed values: `mediawiki`, `mediawiki-basefields`, `zotero`, `bibtex`, `wikibase`. |
| `query` | path | string | Yes | URL of an article, DOI, PMCID or PMID in the URL-encoded format. Note that on the Swagger-UI doc page you don't need to URI-encode the parameter manually, it will be done by the docs engine. |
| `Accept-Language` | header | string | No | For some articles the result depends on the `Accept-Language` header, so provide it if localized content is required. |

**Responses**

- **200** — The citation data in the requested format
  Body (`application/json; charset=utf-8;`, object):
  - `itemType` (string, required)
  - `title` (string, required)
  - `url` (string, required)
- **404** — Citation data was not found.
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

## Reading lists

Private lists of selected pages

### POST /data/lists/setup

**Opt in to use reading lists.**

Must precede other list operations.

Request must be authenticated with a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `csrf_token` | query | string | Yes | The CRSF edit token provided by the MediaWiki API |

**Responses**

- **200** — Success.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /data/lists/teardown

**Opt out from using reading lists.**

Deletes all data. User needs to opt in again before being able to do anything.

Request must be authenticated with a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `csrf_token` | query | string | Yes | The CRSF edit token provided by the MediaWiki API |

**Responses**

- **200** — Success.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /data/lists/

**Get all lists of the current user.**

Returns metadata describing the lists of the current user. Might be truncated and include
a continuation token.

Request must be authenticated with a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `next` | query | string | No | Continuation parameter from previous request |
| `sort` | query | string | No | Sort order - `name`: by name, ascending; - `updated`: by last modification date, descending. Allowed values: `name`, `updated`. Default: `updated`. |

**Responses**

- **200** — An array of list metadata.
  Body (`application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Lists/0.1"`, object):
  - `lists` (array of object)
    - `id` (integer, required)
    - `name` (string, required)
    - `description` (string)
    - `created` (string (date-time), required) — Creation date (in ISO 8601)
    - `updated` (string (date-time), required) — Last modification date (in ISO 8601)
  - `next` (string) — Continuation token.
  - `continue-from` (string (date-time)) — Timestamp to sync from, to be used with the `GET /lists/changes/since/{date}` endpoint.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /data/lists/

**Create a new list for the current user.**

Creates a new empty list. On name conflict, does nothing and returns the data of an
existing list.

Request must be authenticated with a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

This endpoint is deprecated and might be removed without warning. Use the batch version
instead.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `csrf_token` | query | string | Yes | The CRSF edit token provided by the MediaWiki API |

**Request body** (`*/*`, required)

- `name` (string, required)
- `description` (string)

**Responses**

- **200** — The data for the new list.
  Body (`application/json; charset=utf-8`, object):
  - `id` (integer, required) — List ID. Deprecated, will be removed. Use the full list object.
  - `list` (object, required)
    - `id` (integer, required)
    - `name` (string, required)
    - `description` (string)
    - `created` (string (date-time), required) — Creation date (in ISO 8601)
    - `updated` (string (date-time), required) — Last modification date (in ISO 8601)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### PUT /data/lists/{id}

**Update a list.**

List must belong to current user and request must be authenticated with
a MediaWiki session cookie. If the name is changed, the new name must not be in use.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `csrf_token` | query | string | Yes | The CRSF edit token provided by the MediaWiki API |

**Request body** (`*/*`)

- `name` (string, required)
- `description` (string)

**Responses**

- **200** — The updated data for the list.
  Body (`application/json; charset=utf-8`, object):
  - `id` (integer, required) — List ID. Deprecated, will be removed. Use the full list object.
  - `list` (object, required)
    - `id` (integer, required)
    - `name` (string, required)
    - `description` (string)
    - `created` (string (date-time), required) — Creation date (in ISO 8601)
    - `updated` (string (date-time), required) — Last modification date (in ISO 8601)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### DELETE /data/lists/{id}

**Delete a list.**

List must belong to current user and request must be authenticated with
a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |

**Responses**

- **200** — Success.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /data/lists/batch

**Create multiple new lists for the current user.**

See `POST /lists/`.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `csrf_token` | query | string | Yes | The CRSF edit token provided by the MediaWiki API |

**Request body** (`*/*`, required)

- `batch` (array of object, required) — Max items: 500.
  - `name` (string, required)
  - `description` (string)

**Responses**

- **200** — The data for the new lists (in the same order as the inputs).
  Body (`application/json; charset=utf-8`, object):
  - `batch` (array of object, required) — Deprecated, will be removed. Use the full list objects instead.
    - `id` (integer, required) — List ID
  - `lists` (array of object, required)
    - `id` (integer, required)
    - `name` (string, required)
    - `description` (string)
    - `created` (string (date-time), required) — Creation date (in ISO 8601)
    - `updated` (string (date-time), required) — Last modification date (in ISO 8601)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /data/lists/{id}/entries/

**Get all entries of a given list.**

Returns pages contained by the given list. Might be truncated and include
a continuation token.

List must belong to current user and request must be authenticated with
a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `next` | query | string | No | Continuation parameter from previous request |
| `sort` | query | string | No | Sort order - `name`: by page title, ascending; - `updated`: by last modification date, descending. Allowed values: `name`, `updated`. Default: `updated`. |

**Responses**

- **200** — An array of list entries.
  Body (`application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Lists/0.1"`, object):
  - `entries` (array of object)
    - `id` (integer)
    - `project` (string) — Domain of the wiki containing the page.
    - `title` (string) — Title of the page containing the page, in database format.
    - `created` (string (date-time)) — Creation date (in ISO 8601)
    - `updated` (string (date-time)) — Last modification date (in ISO 8601)
  - `next` (string) — Continuation token.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /data/lists/{id}/entries/

**Create a new list entry.**

Creates a new list entry in the given list. On conflict, does nothing and returns the
data of an existing list.

The list must belong to the current user and the request must be
authenticated with a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

This endpoint is deprecated and might be removed without warning. Use the batch version
instead.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `csrf_token` | query | string | Yes | The CRSF edit token provided by the MediaWiki API |

**Request body** (`*/*`, required)

- `project` (string, required) — Domain of the wiki containing the page.
- `title` (string, required) — Title of the page containing the page, in database format.

**Responses**

- **200** — The data for the new list entry.
  Body (`application/json; charset=utf-8`, object):
  - `id` (integer, required) — List entry ID Deprecated, will be removed. Use the full entry object instead.
  - `entry` (object, required)
    - `id` (integer)
    - `project` (string) — Domain of the wiki containing the page.
    - `title` (string) — Title of the page containing the page, in database format.
    - `created` (string (date-time)) — Creation date (in ISO 8601)
    - `updated` (string (date-time)) — Last modification date (in ISO 8601)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### DELETE /data/lists/{id}/entries/{entry_id}

**Delete a list entry.**

Deletes a given list entry.

The list must belong to the current user and the request must be
authenticated with a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `entry_id` | path | integer | Yes |  |

**Responses**

- **200** — Success.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### POST /data/lists/{id}/entries/batch

**Create multiple new list entries.**

See `POST /lists/{id}/entries/`.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes |  |
| `csrf_token` | query | string | Yes | The CRSF edit token provided by the MediaWiki API |

**Request body** (`*/*`, required)

- `batch` (array of object, required) — Max items: 500.
  - `project` (string, required) — Domain of the wiki containing the page.
  - `title` (string, required) — Title of the page containing the page, in database format.

**Responses**

- **200** — The data for the new list entries (in the same order as the inputs).
  Body (`application/json; charset=utf-8`, object):
  - `batch` (array of object, required)
    - `id` (integer) — List entry ID
  - `entries` (array of object, required)
    - `id` (integer)
    - `project` (string) — Domain of the wiki containing the page.
    - `title` (string) — Title of the page containing the page, in database format.
    - `created` (string (date-time)) — Creation date (in ISO 8601)
    - `updated` (string (date-time)) — Last modification date (in ISO 8601)
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /data/lists/pages/{project}/{title}

**Get lists of the current user which contain a given page.**

Request must be authenticated with a MediaWiki session cookie.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `project` | path | string | Yes |  |
| `title` | path | string | Yes |  |
| `next` | query | string | No | Continuation parameter from previous request |

**Responses**

- **200** — An array of list metadata.
  Body (`application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Lists/0.1"`, object):
  - `lists` (array of object)
    - `id` (integer, required)
    - `name` (string, required)
    - `description` (string)
    - `created` (string (date-time), required) — Creation date (in ISO 8601)
    - `updated` (string (date-time), required) — Last modification date (in ISO 8601)
  - `next` (string) — Continuation token.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /data/lists/changes/since/{date}

**Get recent changes to the lists**

Returns metadata describing lists and entries which have changed. Might be truncated
and include a continuation token.

Request must be authenticated with a MediaWiki session cookie.

For safe synchronization, the date parameter should be taken from the `continue-from`
field of a previous `GET /lists/` or `GET /lists/changes/since/{date}` request. This will
ensure that no changes are skipped, at the cost of sometimes receiving the same change
multitple times. Clients should handle changes in an idempotent way.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `date` | path | string (date-time) | Yes | Cutoff date (in ISO 8601). To ensure reliable synchronization, the API might return changes which are slightly older than the cutoff date. |
| `next` | query | string | No | Continuation parameter from previous request |

**Responses**

- **200** — An array of list and entry metadata.
  Body (`application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Lists/0.1"`, object):
  - `lists` (array of object)
    - `id` (integer, required)
    - `name` (string, required)
    - `description` (string)
    - `created` (string (date-time), required) — Creation date (in ISO 8601)
    - `updated` (string (date-time), required) — Last modification date (in ISO 8601)
  - `next` (string) — Continuation token.
  - `continue-from` (string (date-time)) — Timestamp to sync from, to be used with the `GET /lists/changes/since/{date}` endpoint.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

## Recommendation

contribution recommendations

### GET /data/recommendation/article/creation/translation/{from_lang}

**Recommend articles for translation.**

Recommends articles to be translated from the source
to the domain language.

See more at [Recommendation API documentation](https://meta.wikimedia.org/wiki/Recommendation_API)

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `from_lang` | path | string | Yes | The source language code |
| `count` | query | integer | No | The max number of articles to return. Default: `24`. |

**Responses**

- **200** — the list of articles recommended for translation
  Body (`application/json`, object):
  - `count` (integer) — the number of recommendations returned
  - `items` (array of object) — the list of articles recommended for translation
    - `wikidata_id` (string) — wikidata id for the item
    - `title` (string) — title of the article in the source language
    - `sitelink_count` (integer) — count of sites the wikidata item is linked to
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /data/recommendation/article/creation/translation/{from_lang}/{seed_article}

**Recommend articles for translation.**

Recommends articles to be translated from the source
to the domain language.

See more at [Recommendation API documentation](https://meta.wikimedia.org/wiki/Recommendation_API)

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `from_lang` | path | string | Yes | The source language code |
| `seed_article` | path | string | Yes | The article to use as a search seed |
| `count` | query | integer | No | The max number of articles to return. Default: `24`. |

**Responses**

- **200** — the list of articles recommended for translation
  Body (`application/json`, object):
  - `count` (integer) — the number of recommendations returned
  - `items` (array of object) — the list of articles recommended for translation
    - `wikidata_id` (string) — wikidata id for the item
    - `title` (string) — title of the article in the source language
    - `sitelink_count` (integer) — count of sites the wikidata item is linked to
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /data/recommendation/article/creation/morelike/{seed_article}

**Recommend missing articles**

Recommends articles similar to the seed article but are missing
from the domain language Wikipedia.

Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `seed_article` | path | string | Yes | The article title used to search similar but missing articles |

**Responses**

- **200** — the prioritized list of Wikidata IDs recommended for creation as Wikipedia articles
  Body (`application/json`, array of object):
  - `wikidata_id` (string) — Wikidata ID for the item
  - `score` (number) — Score of the recommendation. The higher the score, the more important the recommendation is.
  - `source_language` (string) — Source of the recommendation -- which wiki is recommending the current article.
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

## Mobile

### GET /data/css/mobile/{type}

**Get CSS for mobile apps.**

Gets common CSS mobile apps need to properly display pages using Page Content Service.
In most cases all of the types are needed (preferably in this order):
* base (Common mobile CSS from ResourceLoader)
* site (Site-specific, mobile CSS from ResourceLoader, as defined in MediaWiki\:Mobile.css)
* pcs (CSS for the Page Content Service)

The `base` and `pcs` responses are the same regardless of what domain is used.
For these we suggest meta.wikimedia.org.

You can still pass pagelib for type, but this is a legacy version of the CSS for
existing app clients.

Stability: [unstable](https://www.mediawiki.org/wiki/Wikimedia_Product/Wikimedia_Product_Infrastructure_team/API_endpoint_stability_policy#Unstable)

Please follow [wikitech-l](https://lists.wikimedia.org/mailman/listinfo/wikitech-l) or [mediawiki-api-announce](https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce) for announcements of breaking changes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | path | string | Yes | The desired CSS bundle. Allowed values: `base`, `pagelib`, `pcs`, `site`. |

**Responses**

- **200** — Success
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /data/javascript/mobile/{type}

**Get JavaScript for mobileapps**

Gets the JavaScript bundle so that clients can have
convenient access to that for consuming the page HTML.
Amongst other things,
* it allows to detect the platform and through that enable platform specific CSS rules,
* has code to lazy load images on the page,
* code for collapsing and expanding tables.

Valid types are pagelib or pcs. Passing pcs will return the JavaScript for the
Page Content Service. Passing pagelib will return a deprecated legacy version
of the wikimedia-page-library JavaScript to support existing app clients.

Stability: [unstable](https://www.mediawiki.org/wiki/Wikimedia_Product/Wikimedia_Product_Infrastructure_team/API_endpoint_stability_policy#Unstable)

Please follow [wikitech-l](https://lists.wikimedia.org/mailman/listinfo/wikitech-l) or [mediawiki-api-announce](https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce) for announcements of breaking changes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | path | string | Yes | The desired JavaScript bundle. Allowed values: `pagelib`, `pcs`. |

**Responses**

- **200** — Success
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)

### GET /data/i18n/{type}

**Get internationalization info**

Gets internationalization information for the given site. Currently the only
supported type is pcs for the Page Content Service.

Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | path | string | Yes | The desired internationalization bundle. Allowed values: `pcs`. |

**Responses**

- **200** — Success
- **default** — Error
  Body (`application/problem+json`, object):
  - `type` (string, required)
  - `title` (string)
  - `detail` (string)
  - `instance` (string)
