# httpbin.org — API Reference

A simple HTTP Request & Response Service.

**Base URL:** `http://localhost:8800`

## Redirects

Returns different redirect responses

### GET /absolute-redirect/{n}

**Absolutely 302 Redirects n times.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `n` | path | integer | Yes |  |

**Responses**

- **302** — A redirection.

### GET /redirect-to

**302/3XX Redirects to the given URL.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `url` | query | string | Yes |  |
| `status_code` | query | integer | No |  |

**Responses**

- **302** — A redirection.

### PUT /redirect-to

**302/3XX Redirects to the given URL.**

**Request body** (`application/x-www-form-urlencoded`)

- `url` (string, required)
- `status_code` (integer)

**Responses**

- **302** — A redirection.

### POST /redirect-to

**302/3XX Redirects to the given URL.**

**Request body** (`application/x-www-form-urlencoded`)

- `url` (string, required)
- `status_code` (integer)

**Responses**

- **302** — A redirection.

### DELETE /redirect-to

**302/3XX Redirects to the given URL.**

**Responses**

- **302** — A redirection.

### PATCH /redirect-to

**302/3XX Redirects to the given URL.**

**Responses**

- **302** — A redirection.

### TRACE /redirect-to

**302/3XX Redirects to the given URL.**

**Responses**

- **302** — A redirection.

### GET /redirect/{n}

**302 Redirects n times.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `n` | path | integer | Yes |  |

**Responses**

- **302** — A redirection.

### GET /relative-redirect/{n}

**Relatively 302 Redirects n times.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `n` | path | integer | Yes |  |

**Responses**

- **302** — A redirection.

## Anything

Returns anything that is passed to request

### GET /anything

**Returns anything passed in request data.**

**Responses**

- **200** — Anything passed in request

### PUT /anything

**Returns anything passed in request data.**

**Responses**

- **200** — Anything passed in request

### POST /anything

**Returns anything passed in request data.**

**Responses**

- **200** — Anything passed in request

### DELETE /anything

**Returns anything passed in request data.**

**Responses**

- **200** — Anything passed in request

### PATCH /anything

**Returns anything passed in request data.**

**Responses**

- **200** — Anything passed in request

### TRACE /anything

**Returns anything passed in request data.**

**Responses**

- **200** — Anything passed in request

### GET /anything/{anything}

**Returns anything passed in request data.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `anything` | path | string | Yes |  |

**Responses**

- **200** — Anything passed in request

### PUT /anything/{anything}

**Returns anything passed in request data.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `anything` | path | string | Yes |  |

**Responses**

- **200** — Anything passed in request

### POST /anything/{anything}

**Returns anything passed in request data.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `anything` | path | string | Yes |  |

**Responses**

- **200** — Anything passed in request

### DELETE /anything/{anything}

**Returns anything passed in request data.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `anything` | path | string | Yes |  |

**Responses**

- **200** — Anything passed in request

### PATCH /anything/{anything}

**Returns anything passed in request data.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `anything` | path | string | Yes |  |

**Responses**

- **200** — Anything passed in request

### TRACE /anything/{anything}

**Returns anything passed in request data.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `anything` | path | string | Yes |  |

**Responses**

- **200** — Anything passed in request

## Dynamic data

Generates random and dynamic data

### GET /base64/{value}

**Decodes base64url-encoded string.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `value` | path | string | Yes | Default: `SFRUUEJJTiBpcyBhd2Vzb21l`. |

**Responses**

- **200** — Decoded base64 content.

### GET /bytes/{n}

**Returns n random bytes generated with given seed**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `n` | path | integer | Yes |  |

**Responses**

- **200** — Bytes.

### GET /delay/{delay}

**Returns a delayed response (max of 10 seconds).**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `delay` | path | integer | Yes |  |

**Responses**

- **200** — A delayed response.

### PUT /delay/{delay}

**Returns a delayed response (max of 10 seconds).**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `delay` | path | integer | Yes |  |

**Responses**

- **200** — A delayed response.

### POST /delay/{delay}

**Returns a delayed response (max of 10 seconds).**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `delay` | path | integer | Yes |  |

**Responses**

- **200** — A delayed response.

### DELETE /delay/{delay}

**Returns a delayed response (max of 10 seconds).**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `delay` | path | integer | Yes |  |

**Responses**

- **200** — A delayed response.

### PATCH /delay/{delay}

**Returns a delayed response (max of 10 seconds).**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `delay` | path | integer | Yes |  |

**Responses**

- **200** — A delayed response.

### TRACE /delay/{delay}

**Returns a delayed response (max of 10 seconds).**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `delay` | path | integer | Yes |  |

**Responses**

- **200** — A delayed response.

### GET /drip

**Drips data over a duration after an optional initial delay.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `duration` | query | number | No | The amount of time (in seconds) over which to drip each byte. Default: `2`. |
| `numbytes` | query | integer | No | The number of bytes to respond with. Default: `10`. |
| `code` | query | integer | No | The response code that will be returned. Default: `200`. |
| `delay` | query | number | No | The amount of time (in seconds) to delay before responding. Default: `2`. |

**Responses**

- **200** — A dripped response.

### GET /links/{n}/{offset}

**Generate a page containing n links to other pages which do the same.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `n` | path | integer | Yes |  |
| `offset` | path | integer | Yes |  |

**Responses**

- **200** — HTML links.

### GET /range/{numbytes}

**Streams n random bytes generated with given seed, at given chunk size per packet.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `numbytes` | path | integer | Yes |  |

**Responses**

- **200** — Bytes.

### GET /stream-bytes/{n}

**Streams n random bytes generated with given seed, at given chunk size per packet.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `n` | path | integer | Yes |  |

**Responses**

- **200** — Bytes.

### GET /stream/{n}

**Stream n JSON responses**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `n` | path | integer | Yes |  |

**Responses**

- **200** — Streamed JSON responses.

### GET /uuid

**Return a UUID4.**

**Responses**

- **200** — A UUID4.

## Auth

Auth methods

### GET /basic-auth/{user}/{passwd}

**Prompts the user for authorization using HTTP Basic Auth.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `user` | path | string | Yes |  |
| `passwd` | path | string | Yes |  |

**Responses**

- **200** — Sucessful authentication.
- **401** — Unsuccessful authentication.

### GET /bearer

**Prompts the user for authorization using bearer authentication.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `Authorization` | header | string | No |  |

**Responses**

- **200** — Sucessful authentication.
- **401** — Unsuccessful authentication.

### GET /digest-auth/{qop}/{user}/{passwd}

**Prompts the user for authorization using Digest Auth.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `qop` | path | string | Yes | auth or auth-int |
| `user` | path | string | Yes |  |
| `passwd` | path | string | Yes |  |

**Responses**

- **200** — Sucessful authentication.
- **401** — Unsuccessful authentication.

### GET /digest-auth/{qop}/{user}/{passwd}/{algorithm}

**Prompts the user for authorization using Digest Auth + Algorithm.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `qop` | path | string | Yes | auth or auth-int |
| `user` | path | string | Yes |  |
| `passwd` | path | string | Yes |  |
| `algorithm` | path | string | Yes | MD5, SHA-256, SHA-512. Default: `MD5`. |

**Responses**

- **200** — Sucessful authentication.
- **401** — Unsuccessful authentication.

### GET /digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}

**Prompts the user for authorization using Digest Auth + Algorithm.**

allow settings the stale_after argument.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `qop` | path | string | Yes | auth or auth-int |
| `user` | path | string | Yes |  |
| `passwd` | path | string | Yes |  |
| `algorithm` | path | string | Yes | MD5, SHA-256, SHA-512. Default: `MD5`. |
| `stale_after` | path | string | Yes | Default: `never`. |

**Responses**

- **200** — Sucessful authentication.
- **401** — Unsuccessful authentication.

### GET /hidden-basic-auth/{user}/{passwd}

**Prompts the user for authorization using HTTP Basic Auth.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `user` | path | string | Yes |  |
| `passwd` | path | string | Yes |  |

**Responses**

- **200** — Sucessful authentication.
- **404** — Unsuccessful authentication.

## Response formats

Returns responses in different data formats

### GET /brotli

**Returns Brotli-encoded data.**

**Responses**

- **200** — Brotli-encoded data.

### GET /deflate

**Returns Deflate-encoded data.**

**Responses**

- **200** — Defalte-encoded data.

### GET /deny

**Returns page denied by robots.txt rules.**

**Responses**

- **200** — Denied message

### GET /encoding/utf8

**Returns a UTF-8 encoded body.**

**Responses**

- **200** — Encoded UTF-8 content.

### GET /gzip

**Returns GZip-encoded data.**

**Responses**

- **200** — GZip-encoded data.

### GET /html

**Returns a simple HTML document.**

**Responses**

- **200** — An HTML page.

### GET /json

**Returns a simple JSON document.**

**Responses**

- **200** — An JSON document.

### GET /robots.txt

**Returns some robots.txt rules.**

**Responses**

- **200** — Robots file

### GET /xml

**Returns a simple XML document.**

**Responses**

- **200** — An XML document.

## Response inspection

Inspect the response data like caching and headers

### GET /cache

**Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `If-Modified-Since` | header | any | No |  |
| `If-None-Match` | header | any | No |  |

**Responses**

- **200** — Cached response
- **304** — Modified

### GET /cache/{value}

**Sets a Cache-Control header for n seconds.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `value` | path | integer | Yes |  |

**Responses**

- **200** — Cache control set

### GET /etag/{etag}

**Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `If-None-Match` | header | any | No |  |
| `If-Match` | header | any | No |  |
| `etag` | path | string | Yes |  |

**Responses**

- **200** — Normal response
- **412** — match

### GET /response-headers

**Returns a set of response headers from the query string.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `freeform` | query | object | No |  |

**Responses**

- **200** — Response headers

### POST /response-headers

**Returns a set of response headers from the query string.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `freeform` | query | object | No |  |

**Responses**

- **200** — Response headers

## Cookies

Creates, reads and deletes Cookies

### GET /cookies

**Returns cookie data.**

**Responses**

- **200** — Set cookies.

### GET /cookies/delete

**Deletes cookie(s) as provided by the query string and redirects to cookie list.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `freeform` | query | object | No |  |

**Responses**

- **200** — Redirect to cookie list

### GET /cookies/set

**Sets cookie(s) as provided by the query string and redirects to cookie list.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `freeform` | query | object | No |  |

**Responses**

- **200** — Redirect to cookie list

### GET /cookies/set/{name}/{value}

**Sets a cookie and redirects to cookie list.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | Yes |  |
| `value` | path | string | Yes |  |

**Responses**

- **200** — Set cookies and redirects to cookie list.

## HTTP Methods

Testing different HTTP verbs

### DELETE /delete

**The request's DELETE parameters.**

**Responses**

- **200** — The request's DELETE parameters.

### GET /get

**The request's query parameters.**

**Responses**

- **200** — The request's query parameters.

### PATCH /patch

**The request's PATCH parameters.**

**Responses**

- **200** — The request's PATCH parameters.

### POST /post

**The request's POST parameters.**

**Responses**

- **200** — The request's POST parameters.

### PUT /put

**The request's PUT parameters.**

**Responses**

- **200** — The request's PUT parameters.

## Request inspection

Inspect the request data

### GET /headers

**Return the incoming request's HTTP headers.**

**Responses**

- **200** — The request's headers.

### GET /ip

**Returns the requester's IP Address.**

**Responses**

- **200** — The Requester's IP Address.

### GET /user-agent

**Return the incoming requests's User-Agent header.**

**Responses**

- **200** — The request's User-Agent header.

## Images

Returns different image formats

### GET /image

**Returns a simple image of the type suggest by the Accept header.**

**Responses**

- **200** — An image.

### GET /image/jpeg

**Returns a simple JPEG image.**

**Responses**

- **200** — A JPEG image.

### GET /image/png

**Returns a simple PNG image.**

**Responses**

- **200** — A PNG image.

### GET /image/svg

**Returns a simple SVG image.**

**Responses**

- **200** — An SVG image.

### GET /image/webp

**Returns a simple WEBP image.**

**Responses**

- **200** — A WEBP image.

## Status codes

Generates responses with given status code

### GET /status/{codes}

**Return status code or random status code if more than one are given**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `codes` | path | any | Yes |  |

**Responses**

- **100** — Informational responses
- **200** — Success
- **300** — Redirection
- **400** — Client Errors
- **500** — Server Errors

### PUT /status/{codes}

**Return status code or random status code if more than one are given**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `codes` | path | any | Yes |  |

**Responses**

- **100** — Informational responses
- **200** — Success
- **300** — Redirection
- **400** — Client Errors
- **500** — Server Errors

### POST /status/{codes}

**Return status code or random status code if more than one are given**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `codes` | path | any | Yes |  |

**Responses**

- **100** — Informational responses
- **200** — Success
- **300** — Redirection
- **400** — Client Errors
- **500** — Server Errors

### DELETE /status/{codes}

**Return status code or random status code if more than one are given**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `codes` | path | any | Yes |  |

**Responses**

- **100** — Informational responses
- **200** — Success
- **300** — Redirection
- **400** — Client Errors
- **500** — Server Errors

### PATCH /status/{codes}

**Return status code or random status code if more than one are given**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `codes` | path | any | Yes |  |

**Responses**

- **100** — Informational responses
- **200** — Success
- **300** — Redirection
- **400** — Client Errors
- **500** — Server Errors

### TRACE /status/{codes}

**Return status code or random status code if more than one are given**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `codes` | path | any | Yes |  |

**Responses**

- **100** — Informational responses
- **200** — Success
- **300** — Redirection
- **400** — Client Errors
- **500** — Server Errors
