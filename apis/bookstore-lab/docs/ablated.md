# Bookstore-Lab API — API Reference (ablated)

Lab REST API of a small online bookstore – browse books and authors, add books and place orders.

**Version:** 1.0.0  
**Base URL:** `http://localhost:8000/v1`

## Books

### GET /books

**List books**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of books per page. Default: `20`. |
| `page` | query | integer | No | Default: `1`. |
| `sort` | query | string | Yes | Sort field. |
| `order` | query | string | No | Sort direction. Only used together with sort. Allowed values: `asc`, `desc`. |

**Parameter dependencies:** `IF order THEN sort;`

**Responses**

- **200** — A page of books.
  Body (`application/json`, object):
  - `items` (array of object, required)
    - `id` (integer, required)
    - `title` (string, required)
    - `isbn` (string, required) — Pattern: `^[0-9]{13}$`.
    - `price` (number, required)
    - `genre` (string, required) — Allowed values: `fiction`, `science`, `history`.
    - `published_at` (string (date))
    - `tags` (array of string)
    - `author_id` (integer, required)
  - `total` (integer, required)
- **400** — Invalid query parameter.
  Body (`application/json`, object):
  - `error` (string, required)
  - `field` (string) — May be null.

### POST /books

**Create a book**

**Request body** (`application/json`, required)

- `title` (string, required)
- `isbn` (string, required)
- `price` (number) — Must be greater than 0.
- `genre` (string, required)
- `published_at` (string (date))
- `tags` (array of string)
- `author_id` (integer, required)

**Responses**

- **201** — The created book.
  Body (`application/json`, object):
  - `id` (integer, required)
  - `title` (string, required)
  - `isbn` (string, required) — Pattern: `^[0-9]{13}$`.
  - `price` (number, required)
  - `genre` (string, required) — Allowed values: `fiction`, `science`, `history`.
  - `published_at` (string (date))
  - `tags` (array of string)
  - `author_id` (integer, required)
- **400** — Validation error.
  Body (`application/json`, object):
  - `error` (string, required)
  - `field` (string) — May be null.

### GET /books/{book_id}

**Get a book**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `book_id` | path | integer | Yes | Minimum: 1. |

**Responses**

- **200** — The book.
  Body (`application/json`, object):
  - `id` (integer, required)
  - `title` (string, required)
  - `isbn` (string, required) — Pattern: `^[0-9]{13}$`.
  - `price` (number, required)
  - `genre` (string, required) — Allowed values: `fiction`, `science`, `history`.
  - `published_at` (string (date))
  - `tags` (array of string)
  - `author_id` (integer, required)

## Authors

### GET /authors

**List authors**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string | No | Search text matched against author names. At least 2 characters. Min length: 2. |
| `page` | query | integer | No | Page number, starting from 1. Default: `1`. Minimum: 1. |

**Responses**

- **200** — A page of authors (10 per page).
  Body (`application/json`, object):
  - `items` (array of object, required)
    - `id` (integer, required)
    - `name` (string, required)
    - `country` (string)
  - `total` (integer, required)
- **400** — Invalid query parameter.
  Body (`application/json`, object):
  - `error` (string, required)
  - `field` (string) — May be null.

### GET /authors/{author_id}

**Get an author**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `author_id` | path | integer | Yes |  |

**Responses**

- **200** — The author.
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required)
  - `country` (string)
- **404** — Author not found.
  Body (`application/json`, object):
  - `error` (string, required)
  - `field` (string) — May be null.

## Orders

### POST /orders

**Place an order**

**Request body** (`application/json`, required)

- `book_id` (integer, required)
- `quantity` (integer, required)
- `coupon_code` (string)
- `voucher_type` (string) — Allowed values: `percent`, `fixed`.

**Responses**

- **200** — The created order.
  Body (`application/json`, object):
  - `id` (integer, required)
  - `book_id` (integer, required)
  - `quantity` (integer, required)
  - `total_price` (number, required)
  - `status` (string, required) — Allowed values: `pending`, `paid`, `cancelled`.
  - `coupon_code` (string) — May be null.
- **400** — Validation error.
  Body (`application/json`, object):
  - `error` (string, required)
  - `field` (string) — May be null.

### GET /orders/{order_id}

**Get an order**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | Yes |  |

**Responses**

- **200** — The order.
  Body (`application/json`, object):
  - `id` (integer, required)
  - `book_id` (integer, required)
  - `quantity` (integer, required)
  - `total_price` (number, required)
  - `status` (string, required) — Allowed values: `pending`, `paid`, `cancelled`.
  - `coupon_code` (string) — May be null.
- **404** — Order not found.
  Body (`application/json`, object):
  - `error` (string, required)
  - `field` (string) — May be null.

### DELETE /orders/{order_id}

**Cancel an order**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | Yes |  |

**Responses**

- **204** — Order cancelled.
- **404** — Order not found.
  Body (`application/json`, object):
  - `error` (string, required)
  - `field` (string) — May be null.
