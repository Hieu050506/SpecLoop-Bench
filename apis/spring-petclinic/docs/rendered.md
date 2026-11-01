# Spring PetClinic — API Reference

Spring PetClinic Sample Application.

**Version:** 1.0  
**Base URL:** `http://localhost:9966/petclinic/api`

## oops

Endpoint which always returns an error.

### GET /oops

**Always fails**

Produces sample error response.

**Responses**

- **200** — Never returned.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## owners

Endpoints related to pet owners.

### GET /owners

**Lists pet owners**

Returns an array of pet owners.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `lastName` | query | string | No | Last name. |

**Responses**

- **200** — Owner details found and returned.
  Body (`application/json`, array of object):
  - `firstName` (string, required) — The first name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `address` (string, required) — The postal address of the pet owner. Min length: 1. Max length: 255.
  - `city` (string, required) — The city of the pet owner. Min length: 1. Max length: 80.
  - `telephone` (string, required) — The telephone number of the pet owner. Min length: 1. Max length: 20. Pattern: `^[0-9]*$`.
  - `id` (integer (int32)) — The ID of the pet owner. Minimum: 0.
  - `pets` (array of object, required) — The pets owned by this individual including any booked vet visits.
    - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
    - `birthDate` (string (date), required) — The date of birth of the pet.
    - `type` (object, required) — A pet type.
      - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
      - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
    - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
    - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
    - `visits` (array of object, required) — Vet visit bookings for this pet.
      - `date` (string (date)) — The date of the visit.
      - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
      - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
      - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### POST /owners

**Adds a pet owner**

Records the details of a new pet owner.

**Request body** (`application/json`, required)

The pet owner

- `firstName` (string, required) — The first name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
- `lastName` (string, required) — The last name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
- `address` (string, required) — The postal address of the pet owner. Min length: 1. Max length: 255.
- `city` (string, required) — The city of the pet owner. Min length: 1. Max length: 80.
- `telephone` (string, required) — The telephone number of the pet owner. Min length: 1. Max length: 20. Pattern: `^[0-9]*$`.

**Responses**

- **201** — The pet owner was successfully added.
  Body (`application/json`, object):
  - `firstName` (string, required) — The first name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `address` (string, required) — The postal address of the pet owner. Min length: 1. Max length: 255.
  - `city` (string, required) — The city of the pet owner. Min length: 1. Max length: 80.
  - `telephone` (string, required) — The telephone number of the pet owner. Min length: 1. Max length: 20. Pattern: `^[0-9]*$`.
  - `id` (integer (int32)) — The ID of the pet owner. Minimum: 0.
  - `pets` (array of object, required) — The pets owned by this individual including any booked vet visits.
    - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
    - `birthDate` (string (date), required) — The date of birth of the pet.
    - `type` (object, required) — A pet type.
      - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
      - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
    - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
    - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
    - `visits` (array of object, required) — Vet visit bookings for this pet.
      - `date` (string (date)) — The date of the visit.
      - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
      - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
      - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### GET /owners/{ownerId}

**Get a pet owner by ID**

Returns the pet owner or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ownerId` | path | integer (int32) | Yes | The ID of the pet owner. Minimum: 0. |

**Responses**

- **200** — Owner details found and returned.
  Body (`application/json`, object):
  - `firstName` (string, required) — The first name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `address` (string, required) — The postal address of the pet owner. Min length: 1. Max length: 255.
  - `city` (string, required) — The city of the pet owner. Min length: 1. Max length: 80.
  - `telephone` (string, required) — The telephone number of the pet owner. Min length: 1. Max length: 20. Pattern: `^[0-9]*$`.
  - `id` (integer (int32)) — The ID of the pet owner. Minimum: 0.
  - `pets` (array of object, required) — The pets owned by this individual including any booked vet visits.
    - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
    - `birthDate` (string (date), required) — The date of birth of the pet.
    - `type` (object, required) — A pet type.
      - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
      - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
    - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
    - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
    - `visits` (array of object, required) — Vet visit bookings for this pet.
      - `date` (string (date)) — The date of the visit.
      - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
      - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
      - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Owner not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### PUT /owners/{ownerId}

**Update a pet owner's details**

Updates the pet owner record with the specified details.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ownerId` | path | integer (int32) | Yes | The ID of the pet owner. Minimum: 0. |

**Request body** (`application/json`, required)

The pet owner details to use for the update.

- `firstName` (string, required) — The first name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
- `lastName` (string, required) — The last name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
- `address` (string, required) — The postal address of the pet owner. Min length: 1. Max length: 255.
- `city` (string, required) — The city of the pet owner. Min length: 1. Max length: 80.
- `telephone` (string, required) — The telephone number of the pet owner. Min length: 1. Max length: 20. Pattern: `^[0-9]*$`.

**Responses**

- **200** — Update successful.
  Body (`application/json`, object):
  - `firstName` (string, required) — The first name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `address` (string, required) — The postal address of the pet owner. Min length: 1. Max length: 255.
  - `city` (string, required) — The city of the pet owner. Min length: 1. Max length: 80.
  - `telephone` (string, required) — The telephone number of the pet owner. Min length: 1. Max length: 20. Pattern: `^[0-9]*$`.
  - `id` (integer (int32)) — The ID of the pet owner. Minimum: 0.
  - `pets` (array of object, required) — The pets owned by this individual including any booked vet visits.
    - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
    - `birthDate` (string (date), required) — The date of birth of the pet.
    - `type` (object, required) — A pet type.
      - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
      - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
    - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
    - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
    - `visits` (array of object, required) — Vet visit bookings for this pet.
      - `date` (string (date)) — The date of the visit.
      - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
      - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
      - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Owner not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### DELETE /owners/{ownerId}

**Delete an owner by ID**

Returns the owner or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ownerId` | path | integer (int32) | Yes | The ID of the owner. Minimum: 0. |

**Responses**

- **200** — Owner details found and returned.
  Body (`application/json`, object):
  - `firstName` (string, required) — The first name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `address` (string, required) — The postal address of the pet owner. Min length: 1. Max length: 255.
  - `city` (string, required) — The city of the pet owner. Min length: 1. Max length: 80.
  - `telephone` (string, required) — The telephone number of the pet owner. Min length: 1. Max length: 20. Pattern: `^[0-9]*$`.
  - `id` (integer (int32)) — The ID of the pet owner. Minimum: 0.
  - `pets` (array of object, required) — The pets owned by this individual including any booked vet visits.
    - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
    - `birthDate` (string (date), required) — The date of birth of the pet.
    - `type` (object, required) — A pet type.
      - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
      - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
    - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
    - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
    - `visits` (array of object, required) — Vet visit bookings for this pet.
      - `date` (string (date)) — The date of the visit.
      - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
      - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
      - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Owner not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### POST /owners/{ownerId}/pets

**Adds a pet to an owner**

Records the details of a new pet.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ownerId` | path | integer (int32) | Yes | The ID of the pet owner. Minimum: 0. |

**Request body** (`application/json`, required)

The details of the new pet.

- `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
- `birthDate` (string (date), required) — The date of birth of the pet.
- `type` (object, required) — A pet type.
  - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.

**Responses**

- **201** — The pet was successfully added.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
  - `birthDate` (string (date), required) — The date of birth of the pet.
  - `type` (object, required) — A pet type.
    - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
    - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
  - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
  - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
  - `visits` (array of object, required) — Vet visit bookings for this pet.
    - `date` (string (date)) — The date of the visit.
    - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
    - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
    - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet or Owner not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### GET /owners/{ownerId}/pets/{petId}

**Get a pet by ID**

Returns the pet or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ownerId` | path | integer (int32) | Yes | The ID of the pet owner. Minimum: 0. |
| `petId` | path | integer (int32) | Yes | The ID of the pet. Minimum: 0. |

**Responses**

- **200** — Pet details found and returned.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
  - `birthDate` (string (date), required) — The date of birth of the pet.
  - `type` (object, required) — A pet type.
    - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
    - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
  - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
  - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
  - `visits` (array of object, required) — Vet visit bookings for this pet.
    - `date` (string (date)) — The date of the visit.
    - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
    - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
    - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Owner or pet not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### PUT /owners/{ownerId}/pets/{petId}

**Update a pet's details**

Updates the pet record with the specified details.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ownerId` | path | integer (int32) | Yes | The ID of the pet owner. Minimum: 0. |
| `petId` | path | integer (int32) | Yes | The ID of the pet. Minimum: 0. |

**Request body** (`application/json`, required)

The pet details to use for the update.

- `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
- `birthDate` (string (date), required) — The date of birth of the pet.
- `type` (object, required) — A pet type.
  - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.

**Responses**

- **204** — Update successful.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet not found for this owner.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### POST /owners/{ownerId}/pets/{petId}/visits

**Adds a vet visit**

Records the details of a new vet visit.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ownerId` | path | integer (int32) | Yes | The ID of the pet owner. Minimum: 0. |
| `petId` | path | integer (int32) | Yes | The ID of the pet. Minimum: 0. |

**Request body** (`application/json`, required)

The details of the new vet visit.

- `date` (string (date)) — The date of the visit.
- `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.

**Responses**

- **201** — The vet visit was successfully added.
  Body (`application/json`, object):
  - `date` (string (date)) — The date of the visit.
  - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
  - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
  - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet not found for this owner.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## owner-v2

Version 2 endpoints related to pet owners.

### GET /v2/owners

**Lists pet owners with pagination**

Returns a page of pet owners.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `lastName` | query | string | No | Last name. |
| `page` | query | integer (int32) | No | Zero-based page index. Default: `0`. Minimum: 0. |
| `size` | query | integer (int32) | No | Number of items per page. Default: `20`. Minimum: 1. Maximum: 100. |

**Responses**

- **200** — Owner page found and returned.
  Body (`application/json`, object):
  - `content` (array of object, required) — Pet owners in the requested page.
    - `firstName` (string, required) — The first name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
    - `lastName` (string, required) — The last name of the pet owner. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
    - `address` (string, required) — The postal address of the pet owner. Min length: 1. Max length: 255.
    - `city` (string, required) — The city of the pet owner. Min length: 1. Max length: 80.
    - `telephone` (string, required) — The telephone number of the pet owner. Min length: 1. Max length: 20. Pattern: `^[0-9]*$`.
    - `id` (integer (int32)) — The ID of the pet owner. Minimum: 0.
    - `pets` (array of object, required) — The pets owned by this individual including any booked vet visits.
      - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
      - `birthDate` (string (date), required) — The date of birth of the pet.
      - `type` (object, required) — A pet type.
        - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
        - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
      - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
      - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
      - `visits` (array of object, required) — Vet visit bookings for this pet.
        - `date` (string (date)) — The date of the visit.
        - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
        - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
        - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
  - `page` (integer (int32), required) — Zero-based page index. Minimum: 0.
  - `size` (integer (int32), required) — Requested page size. Minimum: 1.
  - `totalElements` (integer (int64), required) — Total number of owners matching the request. Minimum: 0.
  - `totalPages` (integer (int32), required) — Total number of pages matching the request. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## pettypes

Endpoints related to pet types.

### GET /pettypes

**Lists pet types**

Returns an array of pet types.

**Responses**

- **200** — Pet types found and returned.
  Body (`application/json`, array of object):
  - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
- **304** — Not modified.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### POST /pettypes

**Create a pet type**

Creates a pet type .

**Request body** (`application/json`, required)

The pet type

- `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.

**Responses**

- **200** — Pet type created successfully.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet Type not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### GET /pettypes/{petTypeId}

**Get a pet type by ID**

Returns the pet type or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petTypeId` | path | integer (int32) | Yes | The ID of the pet type. Minimum: 0. |

**Responses**

- **200** — Pet type details found and returned.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet Type not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### PUT /pettypes/{petTypeId}

**Update a pet type by ID**

Returns the pet type or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petTypeId` | path | integer (int32) | Yes | The ID of the pet type. Minimum: 0. |

**Request body** (`application/json`, required)

The pet type

- `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
- `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.

**Responses**

- **200** — Pet type details found and returned.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet Type not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### DELETE /pettypes/{petTypeId}

**Delete a pet type by ID**

Returns the pet type or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petTypeId` | path | integer (int32) | Yes | The ID of the pet type. Minimum: 0. |

**Responses**

- **200** — Pet type details found and returned.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet type not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## pets

Endpoints related to pets.

### GET /pets

**Lists pet**

Returns an array of pet .

**Responses**

- **200** — Pet types found and returned.
  Body (`application/json`, array of object):
  - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
  - `birthDate` (string (date), required) — The date of birth of the pet.
  - `type` (object, required) — A pet type.
    - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
    - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
  - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
  - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
  - `visits` (array of object, required) — Vet visit bookings for this pet.
    - `date` (string (date)) — The date of the visit.
    - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
    - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
    - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### GET /pets/{petId}

**Get a pet by ID**

Returns the pet  or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petId` | path | integer (int32) | Yes | The ID of the pet. Minimum: 0. |

**Responses**

- **200** — Pet details found and returned.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
  - `birthDate` (string (date), required) — The date of birth of the pet.
  - `type` (object, required) — A pet type.
    - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
    - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
  - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
  - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
  - `visits` (array of object, required) — Vet visit bookings for this pet.
    - `date` (string (date)) — The date of the visit.
    - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
    - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
    - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### PUT /pets/{petId}

**Update a pet by ID**

Returns the pet or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petId` | path | integer (int32) | Yes | The ID of the pet. Minimum: 0. |

**Request body** (`application/json`, required)

The pet

- `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
- `birthDate` (string (date), required) — The date of birth of the pet.
- `type` (object, required) — A pet type.
  - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
- `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
- `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
- `visits` (array of object, required) — Vet visit bookings for this pet.
  - `date` (string (date)) — The date of the visit.
  - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
  - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
  - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.

**Responses**

- **200** — Pet details found and returned.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
  - `birthDate` (string (date), required) — The date of birth of the pet.
  - `type` (object, required) — A pet type.
    - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
    - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
  - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
  - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
  - `visits` (array of object, required) — Vet visit bookings for this pet.
    - `date` (string (date)) — The date of the visit.
    - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
    - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
    - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### DELETE /pets/{petId}

**Delete a pet by ID**

Returns the pet or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `petId` | path | integer (int32) | Yes | The ID of the pet. Minimum: 0. |

**Responses**

- **200** — Pet details found and returned.
  Body (`application/json`, object):
  - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
  - `birthDate` (string (date), required) — The date of birth of the pet.
  - `type` (object, required) — A pet type.
    - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
    - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
  - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
  - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
  - `visits` (array of object, required) — Vet visit bookings for this pet.
    - `date` (string (date)) — The date of the visit.
    - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
    - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
    - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Pet not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## pet-v2

Version 2 endpoints related to pets.

### GET /v2/pets

**Lists pets with pagination.**

Returns a page of pets.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer (int32) | No | Zero-based page index. Default: `0`. Minimum: 0. |
| `size` | query | integer (int32) | No | Number of items per page. Default: `20`. Minimum: 1. Maximum: 100. |

**Responses**

- **200** — Page of pets found and returned.
  Body (`application/json`, object):
  - `content` (array of object, required) — Pets in the requested page.
    - `name` (string, required) — The name of the pet. Min length: 1. Max length: 30.
    - `birthDate` (string (date), required) — The date of birth of the pet.
    - `type` (object, required) — A pet type.
      - `name` (string, required) — The name of the pet type. Min length: 1. Max length: 80.
      - `id` (integer (int32), required) — The ID of the pet type. Minimum: 0.
    - `id` (integer (int32), required) — The ID of the pet. Minimum: 0.
    - `ownerId` (integer (int32)) — The ID of the pet's owner. Minimum: 0.
    - `visits` (array of object, required) — Vet visit bookings for this pet.
      - `date` (string (date)) — The date of the visit.
      - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
      - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
      - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
  - `page` (integer (int32), required) — Zero-based page index. Minimum: 0.
  - `size` (integer (int32), required) — Requested page size. Minimum: 1.
  - `totalElements` (integer (int64), required) — Total number of pets matching the request. Minimum: 0.
  - `totalPages` (integer (int32), required) — Total number of pages matching the request. Minimum: 0.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## visits

Endpoints related to vet visits.

### GET /visits

**Lists visits**

Returns an array of visit .

**Responses**

- **200** — visits found and returned.
  Body (`application/json`, array of object):
  - `date` (string (date)) — The date of the visit.
  - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
  - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
  - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### POST /visits

**Create a visit**

Creates a visit.

**Request body** (`application/json`, required)

The visit

- `date` (string (date)) — The date of the visit.
- `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
- `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
- `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.

**Responses**

- **200** — visit created successfully.
  Body (`application/json`, object):
  - `date` (string (date)) — The date of the visit.
  - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
  - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
  - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Visit not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### GET /visits/{visitId}

**Get a visit by ID**

Returns the visit or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `visitId` | path | integer (int32) | Yes | The ID of the visit. Minimum: 0. |

**Responses**

- **200** — Visit details found and returned.
  Body (`application/json`, object):
  - `date` (string (date)) — The date of the visit.
  - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
  - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
  - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Visit not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### PUT /visits/{visitId}

**Update a visit by ID**

Returns the visit or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `visitId` | path | integer (int32) | Yes | The ID of the visit. Minimum: 0. |

**Request body** (`application/json`, required)

The visit

- `date` (string (date)) — The date of the visit.
- `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.

**Responses**

- **200** — Visit details found and returned.
  Body (`application/json`, object):
  - `date` (string (date)) — The date of the visit.
  - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
  - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
  - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Visit not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### DELETE /visits/{visitId}

**Delete a visit by ID**

Returns the visit or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `visitId` | path | integer (int32) | Yes | The ID of the visit. Minimum: 0. |

**Responses**

- **200** — Visit details found and returned.
  Body (`application/json`, object):
  - `date` (string (date)) — The date of the visit.
  - `description` (string, required) — The description for the visit. Min length: 1. Max length: 255.
  - `id` (integer (int32), required) — The ID of the visit. Minimum: 0.
  - `petId` (integer (int32), required) — The ID of the pet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Visit not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## specialties

Endpoints related to vet specialties.

### GET /specialties

**Lists specialties**

Returns an array of specialty .

**Responses**

- **200** — Specialties found and returned.
  Body (`application/json`, array of object):
  - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
  - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
- **304** — Not modified.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### POST /specialties

**Create a specialty**

Creates a specialty .

**Request body** (`application/json`, required)

The specialty

- `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
- `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.

**Responses**

- **200** — Specialty created successfully.
  Body (`application/json`, object):
  - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
  - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Specialty not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### GET /specialties/{specialtyId}

**Get a specialty by ID**

Returns the specialty or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `specialtyId` | path | integer (int32) | Yes | The ID of the speciality. Minimum: 0. |

**Responses**

- **200** — Specialty details found and returned.
  Body (`application/json`, object):
  - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
  - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Specialty not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### PUT /specialties/{specialtyId}

**Update a specialty by ID**

Returns the specialty or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `specialtyId` | path | integer (int32) | Yes | The ID of the specialty. Minimum: 0. |

**Request body** (`application/json`, required)

The pet

- `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
- `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.

**Responses**

- **200** — Specialty details found and returned.
  Body (`application/json`, object):
  - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
  - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Specialty not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### DELETE /specialties/{specialtyId}

**Delete a specialty by ID**

Returns the specialty or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `specialtyId` | path | integer (int32) | Yes | The ID of the specialty. Minimum: 0. |

**Responses**

- **200** — Specialty details found and returned.
  Body (`application/json`, object):
  - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
  - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Specialty not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## vets

Endpoints related to vets.

### GET /vets

**Lists vets**

Returns an array of vets.

**Responses**

- **200** — Vets found and returned.
  Body (`application/json`, array of object):
  - `firstName` (string, required) — The first name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `specialties` (array of object, required) — The specialties of the vet.
    - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
    - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the vet. Minimum: 0.
- **304** — Not modified.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### POST /vets

**Create a Vet**

Creates a vet .

**Request body** (`application/json`, required)

The vet

- `firstName` (string, required) — The first name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
- `lastName` (string, required) — The last name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
- `specialties` (array of object, required) — The specialties of the vet.
  - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
  - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
- `id` (integer (int32), required) — The ID of the vet. Minimum: 0.

**Responses**

- **200** — Vet created successfully.
  Body (`application/json`, object):
  - `firstName` (string, required) — The first name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `specialties` (array of object, required) — The specialties of the vet.
    - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
    - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the vet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Vet not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### GET /vets/{vetId}

**Get a vet by ID**

Returns the vet or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `vetId` | path | integer (int32) | Yes | The ID of the vet. Minimum: 0. |

**Responses**

- **200** — Vet details found and returned.
  Body (`application/json`, object):
  - `firstName` (string, required) — The first name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `specialties` (array of object, required) — The specialties of the vet.
    - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
    - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the vet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Vet not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### PUT /vets/{vetId}

**Update a vet by ID**

Returns the vet or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `vetId` | path | integer (int32) | Yes | The ID of the vet. Minimum: 0. |

**Request body** (`application/json`, required)

The vet

- `firstName` (string, required) — The first name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
- `lastName` (string, required) — The last name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
- `specialties` (array of object, required) — The specialties of the vet.
  - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
  - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
- `id` (integer (int32), required) — The ID of the vet. Minimum: 0.

**Responses**

- **200** — Pet type details found and returned.
  Body (`application/json`, object):
  - `firstName` (string, required) — The first name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `specialties` (array of object, required) — The specialties of the vet.
    - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
    - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the vet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Vet not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

### DELETE /vets/{vetId}

**Delete a vet by ID**

Returns the vet or a 404 error.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `vetId` | path | integer (int32) | Yes | The ID of the vet. Minimum: 0. |

**Responses**

- **200** — Vet details found and returned.
  Body (`application/json`, object):
  - `firstName` (string, required) — The first name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}$`.
  - `lastName` (string, required) — The last name of the vet. Min length: 1. Max length: 30. Pattern: `^[A-Za-zÀ-ɏ]+([ '-][A-Za-zÀ-ɏ]+){0,2}\.?$`.
  - `specialties` (array of object, required) — The specialties of the vet.
    - `id` (integer (int32), required) — The ID of the specialty. Minimum: 0.
    - `name` (string, required) — The name of the specialty. Min length: 1. Max length: 80.
  - `id` (integer (int32), required) — The ID of the vet. Minimum: 0.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — Vet not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.

## users

Endpoints related to users.

### POST /users

**Create a user**

Creates a user.

**Request body** (`application/json`, required)

The user

- `username` (string, required) — The username. Min length: 1. Max length: 80.
- `password` (string) — The password. Min length: 1. Max length: 80.
- `enabled` (boolean) — Indicates if the user is enabled
- `roles` (array of object) — The roles of an user
  - `name` (string, required) — The role's name. Min length: 1. Max length: 80.

**Responses**

- **200** — User created successfully.
  Body (`application/json`, object):
  - `username` (string, required) — The username. Min length: 1. Max length: 80.
  - `password` (string) — The password. Min length: 1. Max length: 80.
  - `enabled` (boolean) — Indicates if the user is enabled
  - `roles` (array of object) — The roles of an user
    - `name` (string, required) — The role's name. Min length: 1. Max length: 80.
- **304** — Not modified.
- **400** — Bad request.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **404** — User not found.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
- **500** — Server error.
  Body (`application/json`, object):
  - `type` (string (uri), required) — Full URL that originated the error response.
  - `title` (string, required) — The short error title.
  - `status` (integer (int32), required) — HTTP status code. Minimum: 400. Must be less than 600.
  - `detail` (string, required) — The long error message.
  - `timestamp` (string (date-time), required) — The time the error occurred.
  - `schemaValidationErrors` (array of object, required) — Validation errors against the OpenAPI schema.
    - `message` (string, required) — The validation message.
