# Swagger Petstore - OpenAPI 3.0 — API Reference

This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about
Swagger at [https://swagger.io](https://swagger.io). In the third iteration of the pet store, we've switched to the design first approach!
You can now help us improve the API whether it's by making changes to the definition itself or to the code.
That way, with time, we can improve the API in general, and expose some of the new features in OAS3.

Some useful links:
- [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
- [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)

**Version:** 1.0.29-SNAPSHOT  
**Base URL:** `http://localhost:8080/api/v3`

## Authentication

- **petstore_auth**: oauth2.
- **api_key**: API key sent in header parameter `api_key`.

## pet

Everything about your Pets

### PUT /pet

**Update an existing pet.**

Update an existing pet by Id.

**Request body** (`application/json`, required)

Update an existent pet in the store

- `id` (integer (int64))
- `name` (string, required)
- `category` (object)
  - `id` (integer (int64))
  - `name` (string)
- `photoUrls` (array of string, required)
- `tags` (array of object)
  - `id` (integer (int64))
  - `name` (string)
- `status` (string) — pet status in the store. Allowed values: `available`, `pending`, `sold`.

**Responses**

- **200** — Successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `name` (string, required)
  - `category` (object)
    - `id` (integer (int64))
    - `name` (string)
  - `photoUrls` (array of string, required)
  - `tags` (array of object)
    - `id` (integer (int64))
    - `name` (string)
  - `status` (string) — pet status in the store. Allowed values: `available`, `pending`, `sold`.
- **400** — Invalid ID supplied
- **404** — Pet not found
- **422** — Validation exception
- **default** — Unexpected error

### POST /pet

**Add a new pet to the store.**

Add a new pet to the store.

**Request body** (`application/json`, required)

Create a new pet in the store

- `id` (integer (int64))
- `name` (string, required)
- `category` (object)
  - `id` (integer (int64))
  - `name` (string)
- `photoUrls` (array of string, required)
- `tags` (array of object)
  - `id` (integer (int64))
  - `name` (string)
- `status` (string) — pet status in the store. Allowed values: `available`, `pending`, `sold`.

**Responses**

- **200** — Successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `name` (string, required)
  - `category` (object)
    - `id` (integer (int64))
    - `name` (string)
  - `photoUrls` (array of string, required)
  - `tags` (array of object)
    - `id` (integer (int64))
    - `name` (string)
  - `status` (string) — pet status in the store. Allowed values: `available`, `pending`, `sold`.
- **400** — Invalid input
- **422** — Validation exception
- **default** — Unexpected error

### GET /pet/findByStatus

**Finds Pets by status.**

Multiple status values can be provided with comma separated strings.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `status` | query | string | Yes | Status values that need to be considered for filter. Allowed values: `available`, `pending`, `sold`. Default: `available`. |

**Responses**

- **200** — successful operation
  Body (`application/json`, array of object):
  - `id` (integer (int64))
  - `name` (string, required)
  - `category` (object)
    - `id` (integer (int64))
    - `name` (string)
  - `photoUrls` (array of string, required)
  - `tags` (array of object)
    - `id` (integer (int64))
    - `name` (string)
  - `status` (string) — pet status in the store. Allowed values: `available`, `pending`, `sold`.
- **400** — Invalid status value
- **default** — Unexpected error

### GET /pet/findByTags

**Finds Pets by tags.**

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `tags` | query | array of string | Yes | Tags to filter by |

**Responses**

- **200** — successful operation
  Body (`application/json`, array of object):
  - `id` (integer (int64))
  - `name` (string, required)
  - `category` (object)
    - `id` (integer (int64))
    - `name` (string)
  - `photoUrls` (array of string, required)
  - `tags` (array of object)
    - `id` (integer (int64))
    - `name` (string)
  - `status` (string) — pet status in the store. Allowed values: `available`, `pending`, `sold`.
- **400** — Invalid tag value
- **default** — Unexpected error

### GET /pet/{petId}

**Find pet by ID.**

Returns a single pet.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petId` | path | integer (int64) | Yes | ID of pet to return |

**Responses**

- **200** — successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `name` (string, required)
  - `category` (object)
    - `id` (integer (int64))
    - `name` (string)
  - `photoUrls` (array of string, required)
  - `tags` (array of object)
    - `id` (integer (int64))
    - `name` (string)
  - `status` (string) — pet status in the store. Allowed values: `available`, `pending`, `sold`.
- **400** — Invalid ID supplied
- **404** — Pet not found
- **default** — Unexpected error

### POST /pet/{petId}

**Updates a pet in the store with form data.**

Updates a pet resource based on the form data.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petId` | path | integer (int64) | Yes | ID of pet that needs to be updated |
| `name` | query | string | No | Name of pet that needs to be updated |
| `status` | query | string | No | Status of pet that needs to be updated |

**Responses**

- **200** — successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `name` (string, required)
  - `category` (object)
    - `id` (integer (int64))
    - `name` (string)
  - `photoUrls` (array of string, required)
  - `tags` (array of object)
    - `id` (integer (int64))
    - `name` (string)
  - `status` (string) — pet status in the store. Allowed values: `available`, `pending`, `sold`.
- **400** — Invalid input
- **default** — Unexpected error

### DELETE /pet/{petId}

**Deletes a pet.**

Delete a pet.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `api_key` | header | string | No |  |
| `petId` | path | integer (int64) | Yes | Pet id to delete |

**Responses**

- **200** — Pet deleted
- **400** — Invalid pet value
- **default** — Unexpected error

### POST /pet/{petId}/uploadImage

**Uploads an image.**

Upload image of the pet.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petId` | path | integer (int64) | Yes | ID of pet to update |
| `additionalMetadata` | query | string | No | Additional Metadata |

**Request body** (`application/octet-stream`)

- Body type: string (binary)

**Responses**

- **200** — successful operation
  Body (`application/json`, object):
  - `code` (integer (int32))
  - `type` (string)
  - `message` (string)
- **400** — No file uploaded
- **404** — Pet not found
- **default** — Unexpected error

## store

Access to Petstore orders

### GET /store/inventory

**Returns pet inventories by status.**

Returns a map of status codes to quantities.

**Responses**

- **200** — successful operation
- **default** — Unexpected error

### POST /store/order

**Place an order for a pet.**

Place a new order in the store.

**Request body** (`application/json`)

- `id` (integer (int64))
- `petId` (integer (int64))
- `quantity` (integer (int32))
- `shipDate` (string (date-time))
- `status` (string) — Order Status. Allowed values: `placed`, `approved`, `delivered`.
- `complete` (boolean)

**Responses**

- **200** — successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `petId` (integer (int64))
  - `quantity` (integer (int32))
  - `shipDate` (string (date-time))
  - `status` (string) — Order Status. Allowed values: `placed`, `approved`, `delivered`.
  - `complete` (boolean)
- **400** — Invalid input
- **422** — Validation exception
- **default** — Unexpected error

### GET /store/order/{orderId}

**Find purchase order by ID.**

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `orderId` | path | integer (int64) | Yes | ID of order that needs to be fetched |

**Responses**

- **200** — successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `petId` (integer (int64))
  - `quantity` (integer (int32))
  - `shipDate` (string (date-time))
  - `status` (string) — Order Status. Allowed values: `placed`, `approved`, `delivered`.
  - `complete` (boolean)
- **400** — Invalid ID supplied
- **404** — Order not found
- **default** — Unexpected error

### DELETE /store/order/{orderId}

**Delete purchase order by identifier.**

For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `orderId` | path | integer (int64) | Yes | ID of the order that needs to be deleted |

**Responses**

- **200** — order deleted
- **400** — Invalid ID supplied
- **404** — Order not found
- **default** — Unexpected error

## user

Operations about user

### POST /user

**Create user.**

This can only be done by the logged in user.

**Request body** (`application/json`)

Created user object

- `id` (integer (int64))
- `username` (string)
- `firstName` (string)
- `lastName` (string)
- `email` (string)
- `password` (string)
- `phone` (string)
- `userStatus` (integer (int32)) — User Status

**Responses**

- **200** — successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `username` (string)
  - `firstName` (string)
  - `lastName` (string)
  - `email` (string)
  - `password` (string)
  - `phone` (string)
  - `userStatus` (integer (int32)) — User Status
- **default** — Unexpected error

### POST /user/createWithList

**Creates list of users with given input array.**

Creates list of users with given input array.

**Request body** (`application/json`)

- `id` (integer (int64))
- `username` (string)
- `firstName` (string)
- `lastName` (string)
- `email` (string)
- `password` (string)
- `phone` (string)
- `userStatus` (integer (int32)) — User Status

**Responses**

- **200** — Successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `username` (string)
  - `firstName` (string)
  - `lastName` (string)
  - `email` (string)
  - `password` (string)
  - `phone` (string)
  - `userStatus` (integer (int32)) — User Status
- **default** — Unexpected error

### GET /user/login

**Logs user into the system.**

Log into the system.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | query | string | No | The user name for login |
| `password` | query | string | No | The password for login in clear text |

**Responses**

- **200** — successful operation
- **400** — Invalid username/password supplied
- **default** — Unexpected error

### GET /user/logout

**Logs out current logged in user session.**

Log user out of the system.

**Responses**

- **200** — successful operation
- **default** — Unexpected error

### GET /user/{username}

**Get user by user name.**

Get user detail based on username.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes | The name that needs to be fetched. Use user1 for testing |

**Responses**

- **200** — successful operation
  Body (`application/json`, object):
  - `id` (integer (int64))
  - `username` (string)
  - `firstName` (string)
  - `lastName` (string)
  - `email` (string)
  - `password` (string)
  - `phone` (string)
  - `userStatus` (integer (int32)) — User Status
- **400** — Invalid username supplied
- **404** — User not found
- **default** — Unexpected error

### PUT /user/{username}

**Update user resource.**

This can only be done by the logged in user.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes | name that need to be deleted |

**Request body** (`application/json`)

Update an existent user in the store

- `id` (integer (int64))
- `username` (string)
- `firstName` (string)
- `lastName` (string)
- `email` (string)
- `password` (string)
- `phone` (string)
- `userStatus` (integer (int32)) — User Status

**Responses**

- **200** — successful operation
- **400** — bad request
- **404** — user not found
- **default** — Unexpected error

### DELETE /user/{username}

**Delete user resource.**

This can only be done by the logged in user.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | Yes | The name that needs to be deleted |

**Responses**

- **200** — User deleted
- **400** — Invalid username supplied
- **404** — User not found
- **default** — Unexpected error
