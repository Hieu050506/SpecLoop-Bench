# Bookstore-Lab API documentation

Welcome to the Bookstore-Lab API. It lets you browse the catalogue of a small online bookstore,
look up authors, add new books and place orders. All endpoints exchange JSON.

**Base URL:** `http://localhost:8000/v1`

No authentication is required for this lab environment.

## Conventions

### Errors

When a request cannot be processed, the API responds with an HTTP error status and a JSON body:

```json
{ "error": "human readable message", "field": "name of the offending field or null" }
```

`field` is `null` when the error is not tied to a specific input field.

### Pagination

List endpoints are paginated with a `page` query parameter. Pages are numbered starting from 1.
Each list response contains the items of the requested page and a `total` count of all matching items.

## Books

A **book** object has the following fields:

| Field | Type | Notes |
|---|---|---|
| `id` | integer | Unique identifier assigned by the server. |
| `title` | string | Title of the book. |
| `isbn` | string | 13-digit ISBN, digits only (for example `9780306406157`). |
| `price` | number | Price in USD. |
| `genre` | string | One of `fiction`, `science` or `history`. |
| `published_at` | string | Publication date, formatted as `YYYY-MM-DD`. Optional. |
| `tags` | array of strings | Free-form labels such as `bestseller`. |
| `author_id` | integer | Identifier of the book's author. |

### List books

`GET /books`

Returns a page of books from the catalogue.

Query parameters:

- `limit` *(integer)* – number of books per page. Defaults to 20.
- `page` *(integer)* – page number, starting from 1. Defaults to 1.
- `sort` *(string, required)* – field used to sort the results: `title` or `published_at`.
- `order` *(string)* – sort direction, `asc` or `desc`. Only used together with `sort`.

Response `200 OK`:

```json
{
  "items": [
    { "id": 1, "title": "Atlas of Clouds", "isbn": "9780000000001", "price": 8.7,
      "genre": "science", "published_at": "1991-02-02", "tags": [], "author_id": 2 }
  ],
  "total": 40
}
```

If a query parameter is invalid the API answers `400 Bad Request` with an error body.

### Get a book

`GET /books/{book_id}`

Returns a single book. `book_id` is the positive integer identifier of the book.

Response `200 OK`: the book object.

### Create a book

`POST /books`

Adds a book to the catalogue. Send a JSON object with these fields:

- `title` *(string, required)* – title of the book.
- `isbn` *(string, required)* – 13-digit ISBN, digits only.
- `price` *(number, required)* – price in USD. The price must be greater than 0.
- `genre` *(string, required)* – one of `fiction`, `science`, `history`.
- `author_id` *(integer, required)* – identifier of an existing author.
- `published_at` *(string, optional)* – publication date in `YYYY-MM-DD` format.
- `tags` *(array of strings, optional)* – labels for the book.

Example request:

```json
{
  "title": "The Little Compiler",
  "isbn": "9780306406157",
  "price": 12.5,
  "genre": "science",
  "author_id": 3,
  "published_at": "2024-05-01",
  "tags": ["programming"]
}
```

Response `201 Created`: the created book object, including its new `id`.
Response `400 Bad Request`: one of the fields is missing or invalid.

## Authors

An **author** has an `id` (integer), a `name` (string) and a `country` (string).

### List authors

`GET /authors`

Returns authors, 10 per page.

Query parameters:

- `q` *(string)* – search text matched against author names. It must contain at least 2 characters.
- `page` *(integer)* – page number, starting from 1. Defaults to 1.

Response `200 OK`: `{ "items": [ author, ... ], "total": <integer> }`.
Response `400 Bad Request`: invalid query parameter.

### Get an author

`GET /authors/{author_id}`

Response `200 OK`: the author object.
Response `404 Not Found`: no author has this identifier.

## Orders

An **order** object contains:

- `id` *(integer)* – order identifier.
- `book_id` *(integer)* – the ordered book.
- `quantity` *(integer)* – number of copies.
- `total_price` *(number)* – price after discounts.
- `status` *(string)* – `pending`, `paid` or `cancelled`.
- `coupon_code` *(string or null)* – the coupon used, if any.

### Place an order

`POST /orders`

Request body:

- `book_id` *(integer, required)* – the book to buy.
- `quantity` *(integer, required)* – number of copies, from 1 up to a maximum of 10.
- `coupon_code` *(string, optional)* – a discount coupon.
- `voucher_type` *(string, optional)* – how the coupon is applied: `percent` or `fixed`.

Response `200 OK`: the new order object.
Response `400 Bad Request`: validation error.

### Get an order

`GET /orders/{order_id}`

Response `200 OK`: the order object. Response `404 Not Found`: unknown order.

### Cancel an order

`DELETE /orders/{order_id}`

Response `204 No Content`: the order was cancelled. Response `404 Not Found`: unknown order.
