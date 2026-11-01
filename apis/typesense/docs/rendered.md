# Typesense API — API Reference

An open source search engine for building delightful search experiences.

**Version:** 30.0  
**Base URL:** `http://localhost:8108`

## Authentication

- **api_key_header**: API key sent in header parameter `X-TYPESENSE-API-KEY`.

## collections

A collection is defined by a schema

### GET /collections

**List all collections**

Returns a summary of all your collections. The collections are returned sorted by creation date, with the most recent collections appearing first.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `getCollectionsParameters` | query | object | No |  |

**Responses**

- **200** — List of all collections
  Body (`application/json`, array of object):
  - `name` (string, required) — Name of the collection
  - `fields` (array of object, required) — A list of fields for querying, filtering and faceting
    - `name` (string, required)
    - `type` (string, required)
    - `optional` (boolean)
    - `facet` (boolean)
    - `index` (boolean) — Default: `true`.
    - `locale` (string)
    - `sort` (boolean)
    - `infix` (boolean) — Default: `false`.
    - `reference` (string) — Name of a field in another collection that should be linked to this collection so that it can be joined during query.
    - `async_reference` (boolean) — Allow documents to be indexed successfully even when the referenced document doesn't exist yet.
    - `num_dim` (integer)
    - `drop` (boolean)
    - `store` (boolean) — When set to false, the field value will not be stored on disk. Default: true.
    - `vec_dist` (string) — The distance metric to be used for vector search. Default: `cosine`. You can also use `ip` for inner product.
    - `range_index` (boolean) — Enables an index optimized for range filtering on numerical fields (e.g. rating:>3.5). Default: false.
    - `stem` (boolean) — Values are stemmed before indexing in-memory. Default: false.
    - `stem_dictionary` (string) — Name of the stemming dictionary to use for this field
    - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
    - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
    - `embed` (object)
      - `from` (array of string, required)
      - `model_config` (object, required)
        - `model_name` (string, required)
        - `api_key` (string)
        - `url` (string)
        - `access_token` (string)
        - `refresh_token` (string)
        - `client_id` (string)
        - `client_secret` (string)
        - `project_id` (string)
        - `indexing_prefix` (string)
        - `query_prefix` (string)
  - `default_sorting_field` (string) — The name of an int32 / float field that determines the order in which the search results are ranked when a sort_by clause is not provided during searching. This field must indicate some kind of popularity. Default: ``.
  - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
  - `synonym_sets` (array of string) — List of synonym set names to associate with this collection
  - `enable_nested_fields` (boolean) — Enables experimental support at a collection level for nested object or object array fields. This field is only available if the Typesense server is version `0.24.0.rcn34` or later. Default: `false`.
  - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
  - `voice_query_model` (object) — Configuration for the voice query model
    - `model_name` (string)
  - `metadata` (object) — Optional details about the collection, e.g., when it was created, who created it etc.
  - `num_documents` (integer (int64), required) — Number of documents in the collection
  - `created_at` (integer (int64), required) — Timestamp of when the collection was created (Unix epoch in seconds)

### POST /collections

**Create a new collection**

When a collection is created, we give it a name and describe the fields that will be indexed from the documents added to the collection.

**Request body** (`application/json`, required)

The collection object to be created

- `name` (string, required) — Name of the collection
- `fields` (array of object, required) — A list of fields for querying, filtering and faceting
  - `name` (string, required)
  - `type` (string, required)
  - `optional` (boolean)
  - `facet` (boolean)
  - `index` (boolean) — Default: `true`.
  - `locale` (string)
  - `sort` (boolean)
  - `infix` (boolean) — Default: `false`.
  - `reference` (string) — Name of a field in another collection that should be linked to this collection so that it can be joined during query.
  - `async_reference` (boolean) — Allow documents to be indexed successfully even when the referenced document doesn't exist yet.
  - `num_dim` (integer)
  - `drop` (boolean)
  - `store` (boolean) — When set to false, the field value will not be stored on disk. Default: true.
  - `vec_dist` (string) — The distance metric to be used for vector search. Default: `cosine`. You can also use `ip` for inner product.
  - `range_index` (boolean) — Enables an index optimized for range filtering on numerical fields (e.g. rating:>3.5). Default: false.
  - `stem` (boolean) — Values are stemmed before indexing in-memory. Default: false.
  - `stem_dictionary` (string) — Name of the stemming dictionary to use for this field
  - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
  - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
  - `embed` (object)
    - `from` (array of string, required)
    - `model_config` (object, required)
      - `model_name` (string, required)
      - `api_key` (string)
      - `url` (string)
      - `access_token` (string)
      - `refresh_token` (string)
      - `client_id` (string)
      - `client_secret` (string)
      - `project_id` (string)
      - `indexing_prefix` (string)
      - `query_prefix` (string)
- `default_sorting_field` (string) — The name of an int32 / float field that determines the order in which the search results are ranked when a sort_by clause is not provided during searching. This field must indicate some kind of popularity. Default: ``.
- `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
- `synonym_sets` (array of string) — List of synonym set names to associate with this collection
- `enable_nested_fields` (boolean) — Enables experimental support at a collection level for nested object or object array fields. This field is only available if the Typesense server is version `0.24.0.rcn34` or later. Default: `false`.
- `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
- `voice_query_model` (object) — Configuration for the voice query model
  - `model_name` (string)
- `metadata` (object) — Optional details about the collection, e.g., when it was created, who created it etc.

**Responses**

- **201** — Collection successfully created
  Body (`application/json`, object):
  - `name` (string, required) — Name of the collection
  - `fields` (array of object, required) — A list of fields for querying, filtering and faceting
    - `name` (string, required)
    - `type` (string, required)
    - `optional` (boolean)
    - `facet` (boolean)
    - `index` (boolean) — Default: `true`.
    - `locale` (string)
    - `sort` (boolean)
    - `infix` (boolean) — Default: `false`.
    - `reference` (string) — Name of a field in another collection that should be linked to this collection so that it can be joined during query.
    - `async_reference` (boolean) — Allow documents to be indexed successfully even when the referenced document doesn't exist yet.
    - `num_dim` (integer)
    - `drop` (boolean)
    - `store` (boolean) — When set to false, the field value will not be stored on disk. Default: true.
    - `vec_dist` (string) — The distance metric to be used for vector search. Default: `cosine`. You can also use `ip` for inner product.
    - `range_index` (boolean) — Enables an index optimized for range filtering on numerical fields (e.g. rating:>3.5). Default: false.
    - `stem` (boolean) — Values are stemmed before indexing in-memory. Default: false.
    - `stem_dictionary` (string) — Name of the stemming dictionary to use for this field
    - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
    - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
    - `embed` (object)
      - `from` (array of string, required)
      - `model_config` (object, required)
        - `model_name` (string, required)
        - `api_key` (string)
        - `url` (string)
        - `access_token` (string)
        - `refresh_token` (string)
        - `client_id` (string)
        - `client_secret` (string)
        - `project_id` (string)
        - `indexing_prefix` (string)
        - `query_prefix` (string)
  - `default_sorting_field` (string) — The name of an int32 / float field that determines the order in which the search results are ranked when a sort_by clause is not provided during searching. This field must indicate some kind of popularity. Default: ``.
  - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
  - `synonym_sets` (array of string) — List of synonym set names to associate with this collection
  - `enable_nested_fields` (boolean) — Enables experimental support at a collection level for nested object or object array fields. This field is only available if the Typesense server is version `0.24.0.rcn34` or later. Default: `false`.
  - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
  - `voice_query_model` (object) — Configuration for the voice query model
    - `model_name` (string)
  - `metadata` (object) — Optional details about the collection, e.g., when it was created, who created it etc.
  - `num_documents` (integer (int64), required) — Number of documents in the collection
  - `created_at` (integer (int64), required) — Timestamp of when the collection was created (Unix epoch in seconds)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **409** — Collection already exists
  Body (`application/json`, object):
  - `message` (string, required)

### GET /collections/{collectionName}

**Retrieve a single collection**

Retrieve the details of a collection, given its name.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to retrieve |

**Responses**

- **200** — Collection fetched
  Body (`application/json`, object):
  - `name` (string, required) — Name of the collection
  - `fields` (array of object, required) — A list of fields for querying, filtering and faceting
    - `name` (string, required)
    - `type` (string, required)
    - `optional` (boolean)
    - `facet` (boolean)
    - `index` (boolean) — Default: `true`.
    - `locale` (string)
    - `sort` (boolean)
    - `infix` (boolean) — Default: `false`.
    - `reference` (string) — Name of a field in another collection that should be linked to this collection so that it can be joined during query.
    - `async_reference` (boolean) — Allow documents to be indexed successfully even when the referenced document doesn't exist yet.
    - `num_dim` (integer)
    - `drop` (boolean)
    - `store` (boolean) — When set to false, the field value will not be stored on disk. Default: true.
    - `vec_dist` (string) — The distance metric to be used for vector search. Default: `cosine`. You can also use `ip` for inner product.
    - `range_index` (boolean) — Enables an index optimized for range filtering on numerical fields (e.g. rating:>3.5). Default: false.
    - `stem` (boolean) — Values are stemmed before indexing in-memory. Default: false.
    - `stem_dictionary` (string) — Name of the stemming dictionary to use for this field
    - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
    - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
    - `embed` (object)
      - `from` (array of string, required)
      - `model_config` (object, required)
        - `model_name` (string, required)
        - `api_key` (string)
        - `url` (string)
        - `access_token` (string)
        - `refresh_token` (string)
        - `client_id` (string)
        - `client_secret` (string)
        - `project_id` (string)
        - `indexing_prefix` (string)
        - `query_prefix` (string)
  - `default_sorting_field` (string) — The name of an int32 / float field that determines the order in which the search results are ranked when a sort_by clause is not provided during searching. This field must indicate some kind of popularity. Default: ``.
  - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
  - `synonym_sets` (array of string) — List of synonym set names to associate with this collection
  - `enable_nested_fields` (boolean) — Enables experimental support at a collection level for nested object or object array fields. This field is only available if the Typesense server is version `0.24.0.rcn34` or later. Default: `false`.
  - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
  - `voice_query_model` (object) — Configuration for the voice query model
    - `model_name` (string)
  - `metadata` (object) — Optional details about the collection, e.g., when it was created, who created it etc.
  - `num_documents` (integer (int64), required) — Number of documents in the collection
  - `created_at` (integer (int64), required) — Timestamp of when the collection was created (Unix epoch in seconds)
- **404** — Collection not found
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /collections/{collectionName}

**Delete a collection**

Permanently drops a collection. This action cannot be undone. For large collections, this might have an impact on read latencies.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to delete |

**Responses**

- **200** — Collection deleted
  Body (`application/json`, object):
  - `name` (string, required) — Name of the collection
  - `fields` (array of object, required) — A list of fields for querying, filtering and faceting
    - `name` (string, required)
    - `type` (string, required)
    - `optional` (boolean)
    - `facet` (boolean)
    - `index` (boolean) — Default: `true`.
    - `locale` (string)
    - `sort` (boolean)
    - `infix` (boolean) — Default: `false`.
    - `reference` (string) — Name of a field in another collection that should be linked to this collection so that it can be joined during query.
    - `async_reference` (boolean) — Allow documents to be indexed successfully even when the referenced document doesn't exist yet.
    - `num_dim` (integer)
    - `drop` (boolean)
    - `store` (boolean) — When set to false, the field value will not be stored on disk. Default: true.
    - `vec_dist` (string) — The distance metric to be used for vector search. Default: `cosine`. You can also use `ip` for inner product.
    - `range_index` (boolean) — Enables an index optimized for range filtering on numerical fields (e.g. rating:>3.5). Default: false.
    - `stem` (boolean) — Values are stemmed before indexing in-memory. Default: false.
    - `stem_dictionary` (string) — Name of the stemming dictionary to use for this field
    - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
    - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
    - `embed` (object)
      - `from` (array of string, required)
      - `model_config` (object, required)
        - `model_name` (string, required)
        - `api_key` (string)
        - `url` (string)
        - `access_token` (string)
        - `refresh_token` (string)
        - `client_id` (string)
        - `client_secret` (string)
        - `project_id` (string)
        - `indexing_prefix` (string)
        - `query_prefix` (string)
  - `default_sorting_field` (string) — The name of an int32 / float field that determines the order in which the search results are ranked when a sort_by clause is not provided during searching. This field must indicate some kind of popularity. Default: ``.
  - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
  - `synonym_sets` (array of string) — List of synonym set names to associate with this collection
  - `enable_nested_fields` (boolean) — Enables experimental support at a collection level for nested object or object array fields. This field is only available if the Typesense server is version `0.24.0.rcn34` or later. Default: `false`.
  - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
  - `voice_query_model` (object) — Configuration for the voice query model
    - `model_name` (string)
  - `metadata` (object) — Optional details about the collection, e.g., when it was created, who created it etc.
  - `num_documents` (integer (int64), required) — Number of documents in the collection
  - `created_at` (integer (int64), required) — Timestamp of when the collection was created (Unix epoch in seconds)
- **404** — Collection not found
  Body (`application/json`, object):
  - `message` (string, required)

### PATCH /collections/{collectionName}

**Update a collection**

Update a collection's schema to modify the fields and their types.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to update |

**Request body** (`application/json`, required)

The document object with fields to be updated

- `fields` (array of object) — A list of fields for querying, filtering and faceting
  - `name` (string, required)
  - `type` (string, required)
  - `optional` (boolean)
  - `facet` (boolean)
  - `index` (boolean) — Default: `true`.
  - `locale` (string)
  - `sort` (boolean)
  - `infix` (boolean) — Default: `false`.
  - `reference` (string) — Name of a field in another collection that should be linked to this collection so that it can be joined during query.
  - `async_reference` (boolean) — Allow documents to be indexed successfully even when the referenced document doesn't exist yet.
  - `num_dim` (integer)
  - `drop` (boolean)
  - `store` (boolean) — When set to false, the field value will not be stored on disk. Default: true.
  - `vec_dist` (string) — The distance metric to be used for vector search. Default: `cosine`. You can also use `ip` for inner product.
  - `range_index` (boolean) — Enables an index optimized for range filtering on numerical fields (e.g. rating:>3.5). Default: false.
  - `stem` (boolean) — Values are stemmed before indexing in-memory. Default: false.
  - `stem_dictionary` (string) — Name of the stemming dictionary to use for this field
  - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
  - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
  - `embed` (object)
    - `from` (array of string, required)
    - `model_config` (object, required)
      - `model_name` (string, required)
      - `api_key` (string)
      - `url` (string)
      - `access_token` (string)
      - `refresh_token` (string)
      - `client_id` (string)
      - `client_secret` (string)
      - `project_id` (string)
      - `indexing_prefix` (string)
      - `query_prefix` (string)
- `synonym_sets` (array of string) — List of synonym set names to associate with this collection
- `metadata` (object) — Optional details about the collection, e.g., when it was created, who created it etc.

**Responses**

- **200** — The updated partial collection schema
  Body (`application/json`, object):
  - `fields` (array of object) — A list of fields for querying, filtering and faceting
    - `name` (string, required)
    - `type` (string, required)
    - `optional` (boolean)
    - `facet` (boolean)
    - `index` (boolean) — Default: `true`.
    - `locale` (string)
    - `sort` (boolean)
    - `infix` (boolean) — Default: `false`.
    - `reference` (string) — Name of a field in another collection that should be linked to this collection so that it can be joined during query.
    - `async_reference` (boolean) — Allow documents to be indexed successfully even when the referenced document doesn't exist yet.
    - `num_dim` (integer)
    - `drop` (boolean)
    - `store` (boolean) — When set to false, the field value will not be stored on disk. Default: true.
    - `vec_dist` (string) — The distance metric to be used for vector search. Default: `cosine`. You can also use `ip` for inner product.
    - `range_index` (boolean) — Enables an index optimized for range filtering on numerical fields (e.g. rating:>3.5). Default: false.
    - `stem` (boolean) — Values are stemmed before indexing in-memory. Default: false.
    - `stem_dictionary` (string) — Name of the stemming dictionary to use for this field
    - `token_separators` (array of string) — List of symbols or special characters to be used for splitting the text into individual words in addition to space and new-line characters. Default: `[]`.
    - `symbols_to_index` (array of string) — List of symbols or special characters to be indexed. Default: `[]`.
    - `embed` (object)
      - `from` (array of string, required)
      - `model_config` (object, required)
        - `model_name` (string, required)
        - `api_key` (string)
        - `url` (string)
        - `access_token` (string)
        - `refresh_token` (string)
        - `client_id` (string)
        - `client_secret` (string)
        - `project_id` (string)
        - `indexing_prefix` (string)
        - `query_prefix` (string)
  - `synonym_sets` (array of string) — List of synonym set names to associate with this collection
  - `metadata` (object) — Optional details about the collection, e.g., when it was created, who created it etc.
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **404** — The collection was not found
  Body (`application/json`, object):
  - `message` (string, required)

### GET /aliases

**List all aliases**

List all aliases and the corresponding collections that they map to.

**Responses**

- **200** — List of all collection aliases
  Body (`application/json`, object):
  - `aliases` (array of object, required)
    - `name` (string, required) — Name of the collection alias
    - `collection_name` (string, required) — Name of the collection the alias mapped to

### GET /aliases/{aliasName}

**Retrieve an alias**

Find out which collection an alias points to by fetching it

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `aliasName` | path | string | Yes | The name of the alias to retrieve |

**Responses**

- **200** — Collection alias fetched
  Body (`application/json`, object):
  - `name` (string, required) — Name of the collection alias
  - `collection_name` (string, required) — Name of the collection the alias mapped to
- **404** — The alias was not found
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /aliases/{aliasName}

**Create or update a collection alias**

Create or update a collection alias. An alias is a virtual collection name that points to a real collection. If you're familiar with symbolic links on Linux, it's very similar to that. Aliases are useful when you want to reindex your data in the background on a new collection and switch your application to it without any changes to your code.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `aliasName` | path | string | Yes | The name of the alias to create/update |

**Request body** (`application/json`)

Collection alias to be created/updated

- `collection_name` (string, required) — Name of the collection you wish to map the alias to

**Responses**

- **200** — The collection alias was created/updated
  Body (`application/json`, object):
  - `name` (string, required) — Name of the collection alias
  - `collection_name` (string, required) — Name of the collection the alias mapped to
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **404** — Alias not found
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /aliases/{aliasName}

**Delete an alias**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `aliasName` | path | string | Yes | The name of the alias to delete |

**Responses**

- **200** — Collection alias was deleted
  Body (`application/json`, object):
  - `name` (string, required) — Name of the collection alias
  - `collection_name` (string, required) — Name of the collection the alias mapped to
- **404** — Alias not found
  Body (`application/json`, object):
  - `message` (string, required)

## documents

A document is an individual record to be indexed and belongs to a collection

### POST /collections/{collectionName}/documents

**Index a document**

A document to be indexed in a given collection must conform to the schema of the collection.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to add the document to |
| `action` | query | string | No | Additional action to perform. Allowed values: `create`, `update`, `upsert`, `emplace`. |
| `dirty_values` | query | string | No | Dealing with Dirty Data. Allowed values: `coerce_or_reject`, `coerce_or_drop`, `drop`, `reject`. |

**Request body** (`application/json`, required)

The document object to be indexed

- Body type: object

**Responses**

- **201** — Document successfully created/indexed
- **404** — Collection not found
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /collections/{collectionName}/documents

**Delete a bunch of documents**

Delete a bunch of documents that match a specific filter condition. Use the `batch_size` parameter to control the number of documents that should deleted at a time. A larger value will speed up deletions, but will impact performance of other operations running on the server.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to delete documents from |
| `deleteDocumentsParameters` | query | object | No |  |

**Responses**

- **200** — Documents successfully deleted
  Body (`application/json`, object):
  - `num_deleted` (integer, required)
- **404** — Collection not found
  Body (`application/json`, object):
  - `message` (string, required)

### PATCH /collections/{collectionName}/documents

**Update documents with conditional query**

The filter_by query parameter is used to filter to specify a condition against which the documents are matched. The request body contains the fields that should be updated for any documents that match the filter condition. This endpoint is only available if the Typesense server is version `0.25.0.rc12` or later.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to update documents in |
| `updateDocumentsParameters` | query | object | No |  |

**Request body** (`application/json`, required)

The document fields to be updated

- Body type: object

**Responses**

- **200** — The response contains a single field, `num_updated`, indicating the number of documents affected.
  Body (`application/json`, object):
  - `num_updated` (integer, required) — The number of documents that have been updated
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **404** — The collection was not found
  Body (`application/json`, object):
  - `message` (string, required)

### GET /collections/{collectionName}/documents/search

**Search for documents in a collection**

Search for documents in a collection that match the search criteria.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to search for the document under |
| `searchParameters` | query | object | Yes |  |

**Responses**

- **200** — Search results
  Body (`application/json`, object):
  - `facet_counts` (array of object)
    - `counts` (array of object)
      - `count` (integer)
      - `highlighted` (string)
      - `value` (string)
      - `parent` (object)
    - `field_name` (string)
    - `sampled` (boolean)
    - `stats` (object)
      - `max` (number (double))
      - `min` (number (double))
      - `sum` (number (double))
      - `total_values` (integer)
      - `avg` (number (double))
  - `found` (integer) — The number of documents found
  - `found_docs` (integer)
  - `search_time_ms` (integer) — The number of milliseconds the search took
  - `out_of` (integer) — The total number of documents in the collection
  - `search_cutoff` (boolean) — Whether the search was cut off
  - `page` (integer) — The search result page number
  - `grouped_hits` (array of object)
    - `found` (integer)
    - `group_key` (array of any, required)
    - `hits` (array of object, required) — The documents that matched the search query
      - `highlights` (array of object) — (Deprecated) Contains highlighted portions of the search fields
        - `field` (string)
        - `snippet` (string) — Present only for (non-array) string fields
        - `snippets` (array of string) — Present only for (array) string[] fields
        - `value` (string) — Full field value with highlighting, present only for (non-array) string fields
        - `values` (array of string) — Full field value with highlighting, present only for (array) string[] fields
        - `indices` (array of integer) — The indices property will be present only for string[] fields and will contain the corresponding indices of the snippets in the search field
        - `matched_tokens` (array of object)
      - `highlight` (object) — Highlighted version of the matching document
      - `document` (object) — Can be any key-value pair
      - `text_match` (integer (int64))
      - `text_match_info` (object)
        - `best_field_score` (string)
        - `best_field_weight` (integer)
        - `fields_matched` (integer)
        - `num_tokens_dropped` (integer (int64))
        - `score` (string)
        - `tokens_matched` (integer)
        - `typo_prefix_score` (integer)
      - `geo_distance_meters` (object) — Can be any key-value pair
      - `vector_distance` (number (float)) — Distance between the query vector and matching document's vector value
      - `hybrid_search_info` (object) — Information about hybrid search scoring
        - `rank_fusion_score` (number (float)) — Combined score from rank fusion of text and vector search
      - `search_index` (integer) — Returned only for union query response. Indicates the index of the query which this document matched to.
  - `hits` (array of object) — The documents that matched the search query
    - `highlights` (array of object) — (Deprecated) Contains highlighted portions of the search fields
      - `field` (string)
      - `snippet` (string) — Present only for (non-array) string fields
      - `snippets` (array of string) — Present only for (array) string[] fields
      - `value` (string) — Full field value with highlighting, present only for (non-array) string fields
      - `values` (array of string) — Full field value with highlighting, present only for (array) string[] fields
      - `indices` (array of integer) — The indices property will be present only for string[] fields and will contain the corresponding indices of the snippets in the search field
      - `matched_tokens` (array of object)
    - `highlight` (object) — Highlighted version of the matching document
    - `document` (object) — Can be any key-value pair
    - `text_match` (integer (int64))
    - `text_match_info` (object)
      - `best_field_score` (string)
      - `best_field_weight` (integer)
      - `fields_matched` (integer)
      - `num_tokens_dropped` (integer (int64))
      - `score` (string)
      - `tokens_matched` (integer)
      - `typo_prefix_score` (integer)
    - `geo_distance_meters` (object) — Can be any key-value pair
    - `vector_distance` (number (float)) — Distance between the query vector and matching document's vector value
    - `hybrid_search_info` (object) — Information about hybrid search scoring
      - `rank_fusion_score` (number (float)) — Combined score from rank fusion of text and vector search
    - `search_index` (integer) — Returned only for union query response. Indicates the index of the query which this document matched to.
  - `request_params` (object)
    - `collection_name` (string, required)
    - `first_q` (string)
    - `q` (string, required)
    - `per_page` (integer, required)
    - `voice_query` (object)
      - `transcribed_query` (string)
  - `conversation` (object)
    - `answer` (string, required)
    - `conversation_history` (array of object, required)
    - `conversation_id` (string, required)
    - `query` (string, required)
  - `union_request_params` (array of object) — Returned only for union query response.
    - `collection_name` (string, required)
    - `first_q` (string)
    - `q` (string, required)
    - `per_page` (integer, required)
    - `voice_query` (object)
      - `transcribed_query` (string)
  - `metadata` (object) — Custom JSON object that can be returned in the search response
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **404** — The collection or field was not found
  Body (`application/json`, object):
  - `message` (string, required)

### GET /collections/{collectionName}/documents/export

**Export all documents in a collection**

Export all documents in a collection in JSON lines format.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection |
| `exportDocumentsParameters` | query | object | No |  |

**Responses**

- **200** — Exports all the documents in a given collection.
- **404** — The collection was not found
  Body (`application/json`, object):
  - `message` (string, required)

### POST /collections/{collectionName}/documents/import

**Import documents into a collection**

The documents to be imported must be formatted in a newline delimited JSON structure. You can feed the output file from a Typesense export operation directly as import.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection |
| `importDocumentsParameters` | query | object | No |  |

**Request body** (`application/octet-stream`, required)

The json array of documents or the JSONL file to import

- Body type: string

**Responses**

- **200** — Result of the import operation. Each line of the response indicates the result of each document present in the request body (in the same order). If the import of a single document fails, it does not affect the other documents. If there is a failure, the response line will include a corresponding error message and as well as the actual document content.
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **404** — The collection was not found
  Body (`application/json`, object):
  - `message` (string, required)

### GET /collections/{collectionName}/documents/{documentId}

**Retrieve a document**

Fetch an individual document from a collection by using its ID.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to search for the document under |
| `documentId` | path | string | Yes | The Document ID |

**Responses**

- **200** — The document referenced by the ID
- **404** — The document or collection was not found
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /collections/{collectionName}/documents/{documentId}

**Delete a document**

Delete an individual document from a collection by using its ID.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to search for the document under |
| `documentId` | path | string | Yes | The Document ID |

**Responses**

- **200** — The document referenced by the ID was deleted
- **404** — The document or collection was not found
  Body (`application/json`, object):
  - `message` (string, required)

### PATCH /collections/{collectionName}/documents/{documentId}

**Update a document**

Update an individual document from a collection by using its ID. The update can be partial.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collectionName` | path | string | Yes | The name of the collection to search for the document under |
| `documentId` | path | string | Yes | The Document ID |
| `dirty_values` | query | string | No | Dealing with Dirty Data. Allowed values: `coerce_or_reject`, `coerce_or_drop`, `drop`, `reject`. |

**Request body** (`application/json`, required)

The document object with fields to be updated

- Body type: object

**Responses**

- **200** — The document referenced by the ID was updated
- **404** — The document or collection was not found
  Body (`application/json`, object):
  - `message` (string, required)

### POST /multi_search

**send multiple search requests in a single HTTP request**

This is especially useful to avoid round-trip network latencies incurred otherwise if each of these requests are sent in separate HTTP requests. You can also use this feature to do a federated search across multiple collections in a single HTTP request.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `multiSearchParameters` | query | object | Yes |  |

**Request body** (`application/json`)

- `union` (boolean) — When true, merges the search results from each search query into a single ordered set of hits. Default: `false`.
- `searches` (array of object, required)
  - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
  - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
  - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
  - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
  - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
  - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
  - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
  - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
  - `filter_by` (string) — Filter conditions for refining youropen api validator search results. Separate multiple conditions with &&.
  - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
  - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
  - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
  - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
  - `max_facet_values` (integer) — Maximum number of facet values to be returned.
  - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
  - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
  - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
  - `page` (integer) — Results from this specific page number would be fetched.
  - `per_page` (integer) — Number of results to fetch per page. Default: 10
  - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
  - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
  - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
  - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
  - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
  - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
  - `include_fields` (string) — List of fields from the document to include in the search result
  - `exclude_fields` (string) — List of fields from the document to exclude in the search result
  - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
  - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
  - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
  - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
  - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
  - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
  - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
  - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
  - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
  - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
  - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
  - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
  - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
  - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
  - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
  - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
  - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
  - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
  - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
  - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
  - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same. Default: `false`.
  - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
  - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
  - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
  - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
  - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
  - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
  - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
  - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
  - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
  - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
  - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
  - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
  - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
  - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
  - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
  - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
  - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
  - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
  - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
  - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
  - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
  - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
  - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
  - `conversation` (boolean) — Enable conversational search.
  - `conversation_model_id` (string) — The Id of Conversation Model to be used.
  - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
  - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
  - `collection` (string) — The collection to search in.
  - `x-typesense-api-key` (string) — A separate search API key for each search within a multi_search request

**Responses**

- **200** — Search results
  Body (`application/json`, object):
  - `results` (array of object, required)
    - `facet_counts` (array of object)
      - `counts` (array of object)
        - `count` (integer)
        - `highlighted` (string)
        - `value` (string)
        - `parent` (object)
      - `field_name` (string)
      - `sampled` (boolean)
      - `stats` (object)
        - `max` (number (double))
        - `min` (number (double))
        - `sum` (number (double))
        - `total_values` (integer)
        - `avg` (number (double))
    - `found` (integer) — The number of documents found
    - `found_docs` (integer)
    - `search_time_ms` (integer) — The number of milliseconds the search took
    - `out_of` (integer) — The total number of documents in the collection
    - `search_cutoff` (boolean) — Whether the search was cut off
    - `page` (integer) — The search result page number
    - `grouped_hits` (array of object)
      - `found` (integer)
      - `group_key` (array of any, required)
      - `hits` (array of object, required) — The documents that matched the search query
        - `highlights` (array of object) — (Deprecated) Contains highlighted portions of the search fields
        - `highlight` (object) — Highlighted version of the matching document
        - `document` (object) — Can be any key-value pair
        - `text_match` (integer (int64))
        - `text_match_info` (object)
        - `geo_distance_meters` (object) — Can be any key-value pair
        - `vector_distance` (number (float)) — Distance between the query vector and matching document's vector value
        - `hybrid_search_info` (object) — Information about hybrid search scoring
        - `search_index` (integer) — Returned only for union query response. Indicates the index of the query which this document matched to.
    - `hits` (array of object) — The documents that matched the search query
      - `highlights` (array of object) — (Deprecated) Contains highlighted portions of the search fields
        - `field` (string)
        - `snippet` (string) — Present only for (non-array) string fields
        - `snippets` (array of string) — Present only for (array) string[] fields
        - `value` (string) — Full field value with highlighting, present only for (non-array) string fields
        - `values` (array of string) — Full field value with highlighting, present only for (array) string[] fields
        - `indices` (array of integer) — The indices property will be present only for string[] fields and will contain the corresponding indices of the snippets in the search field
        - `matched_tokens` (array of object)
      - `highlight` (object) — Highlighted version of the matching document
      - `document` (object) — Can be any key-value pair
      - `text_match` (integer (int64))
      - `text_match_info` (object)
        - `best_field_score` (string)
        - `best_field_weight` (integer)
        - `fields_matched` (integer)
        - `num_tokens_dropped` (integer (int64))
        - `score` (string)
        - `tokens_matched` (integer)
        - `typo_prefix_score` (integer)
      - `geo_distance_meters` (object) — Can be any key-value pair
      - `vector_distance` (number (float)) — Distance between the query vector and matching document's vector value
      - `hybrid_search_info` (object) — Information about hybrid search scoring
        - `rank_fusion_score` (number (float)) — Combined score from rank fusion of text and vector search
      - `search_index` (integer) — Returned only for union query response. Indicates the index of the query which this document matched to.
    - `request_params` (object)
      - `collection_name` (string, required)
      - `first_q` (string)
      - `q` (string, required)
      - `per_page` (integer, required)
      - `voice_query` (object)
        - `transcribed_query` (string)
    - `conversation` (object)
      - `answer` (string, required)
      - `conversation_history` (array of object, required)
      - `conversation_id` (string, required)
      - `query` (string, required)
    - `union_request_params` (array of object) — Returned only for union query response.
      - `collection_name` (string, required)
      - `first_q` (string)
      - `q` (string, required)
      - `per_page` (integer, required)
      - `voice_query` (object)
        - `transcribed_query` (string)
    - `metadata` (object) — Custom JSON object that can be returned in the search response
    - `code` (integer (int64)) — HTTP error code
    - `error` (string) — Error description
  - `conversation` (object)
    - `answer` (string, required)
    - `conversation_history` (array of object, required)
    - `conversation_id` (string, required)
    - `query` (string, required)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

## synonyms

Manage synonyms

### GET /synonym_sets

**List all synonym sets**

Retrieve all synonym sets

**Responses**

- **200** — List of all synonym sets
  Body (`application/json`, array of object):
  - `items` (array of object, required) — Array of synonym items
    - `id` (string, required) — Unique identifier for the synonym item
    - `synonyms` (array of string, required) — Array of words that should be considered as synonyms
    - `root` (string) — For 1-way synonyms, indicates the root word that words in the synonyms parameter map to
    - `locale` (string) — Locale for the synonym, leave blank to use the standard tokenizer
    - `symbols_to_index` (array of string) — By default, special characters are dropped from synonyms. Use this attribute to specify which special characters should be indexed as is
  - `name` (string, required) — Name of the synonym set

### GET /synonym_sets/{synonymSetName}

**Retrieve a synonym set**

Retrieve a specific synonym set by its name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `synonymSetName` | path | string | Yes | The name of the synonym set to retrieve |

**Responses**

- **200** — Synonym set fetched
  Body (`application/json`, object):
  - `items` (array of object, required) — Array of synonym items
    - `id` (string, required) — Unique identifier for the synonym item
    - `synonyms` (array of string, required) — Array of words that should be considered as synonyms
    - `root` (string) — For 1-way synonyms, indicates the root word that words in the synonyms parameter map to
    - `locale` (string) — Locale for the synonym, leave blank to use the standard tokenizer
    - `symbols_to_index` (array of string) — By default, special characters are dropped from synonyms. Use this attribute to specify which special characters should be indexed as is
  - `name` (string, required) — Name of the synonym set
- **404** — Synonym set not found
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /synonym_sets/{synonymSetName}

**Create or update a synonym set**

Create or update a synonym set with the given name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `synonymSetName` | path | string | Yes | The name of the synonym set to create/update |

**Request body** (`application/json`, required)

The synonym set to be created/updated

- `items` (array of object, required) — Array of synonym items
  - `id` (string, required) — Unique identifier for the synonym item
  - `synonyms` (array of string, required) — Array of words that should be considered as synonyms
  - `root` (string) — For 1-way synonyms, indicates the root word that words in the synonyms parameter map to
  - `locale` (string) — Locale for the synonym, leave blank to use the standard tokenizer
  - `symbols_to_index` (array of string) — By default, special characters are dropped from synonyms. Use this attribute to specify which special characters should be indexed as is

**Responses**

- **200** — Synonym set successfully created/updated
  Body (`application/json`, object):
  - `items` (array of object, required) — Array of synonym items
    - `id` (string, required) — Unique identifier for the synonym item
    - `synonyms` (array of string, required) — Array of words that should be considered as synonyms
    - `root` (string) — For 1-way synonyms, indicates the root word that words in the synonyms parameter map to
    - `locale` (string) — Locale for the synonym, leave blank to use the standard tokenizer
    - `symbols_to_index` (array of string) — By default, special characters are dropped from synonyms. Use this attribute to specify which special characters should be indexed as is
  - `name` (string, required) — Name of the synonym set
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /synonym_sets/{synonymSetName}

**Delete a synonym set**

Delete a specific synonym set by its name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `synonymSetName` | path | string | Yes | The name of the synonym set to delete |

**Responses**

- **200** — Synonym set successfully deleted
  Body (`application/json`, object):
  - `name` (string, required) — Name of the deleted synonym set
- **404** — Synonym set not found
  Body (`application/json`, object):
  - `message` (string, required)

### GET /synonym_sets/{synonymSetName}/items

**List items in a synonym set**

Retrieve all synonym items in a set

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `synonymSetName` | path | string | Yes | The name of the synonym set to retrieve items for |

**Responses**

- **200** — List of synonym items
  Body (`application/json`, array of object):
  - `id` (string, required) — Unique identifier for the synonym item
  - `synonyms` (array of string, required) — Array of words that should be considered as synonyms
  - `root` (string) — For 1-way synonyms, indicates the root word that words in the synonyms parameter map to
  - `locale` (string) — Locale for the synonym, leave blank to use the standard tokenizer
  - `symbols_to_index` (array of string) — By default, special characters are dropped from synonyms. Use this attribute to specify which special characters should be indexed as is
- **404** — Synonym set not found
  Body (`application/json`, object):
  - `message` (string, required)

### GET /synonym_sets/{synonymSetName}/items/{itemId}

**Retrieve a synonym set item**

Retrieve a specific synonym item by its id

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `synonymSetName` | path | string | Yes | The name of the synonym set |
| `itemId` | path | string | Yes | The id of the synonym item to retrieve |

**Responses**

- **200** — Synonym item fetched
  Body (`application/json`, object):
  - `id` (string, required) — Unique identifier for the synonym item
  - `synonyms` (array of string, required) — Array of words that should be considered as synonyms
  - `root` (string) — For 1-way synonyms, indicates the root word that words in the synonyms parameter map to
  - `locale` (string) — Locale for the synonym, leave blank to use the standard tokenizer
  - `symbols_to_index` (array of string) — By default, special characters are dropped from synonyms. Use this attribute to specify which special characters should be indexed as is
- **404** — Synonym item not found
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /synonym_sets/{synonymSetName}/items/{itemId}

**Create or update a synonym set item**

Create or update a synonym set item with the given id

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `synonymSetName` | path | string | Yes | The name of the synonym set |
| `itemId` | path | string | Yes | The id of the synonym item to upsert |

**Request body** (`application/json`, required)

The synonym item to be created/updated

- `synonyms` (array of string, required) — Array of words that should be considered as synonyms
- `root` (string) — For 1-way synonyms, indicates the root word that words in the synonyms parameter map to
- `locale` (string) — Locale for the synonym, leave blank to use the standard tokenizer
- `symbols_to_index` (array of string) — By default, special characters are dropped from synonyms. Use this attribute to specify which special characters should be indexed as is

**Responses**

- **200** — Synonym item successfully created/updated
  Body (`application/json`, object):
  - `id` (string, required) — Unique identifier for the synonym item
  - `synonyms` (array of string, required) — Array of words that should be considered as synonyms
  - `root` (string) — For 1-way synonyms, indicates the root word that words in the synonyms parameter map to
  - `locale` (string) — Locale for the synonym, leave blank to use the standard tokenizer
  - `symbols_to_index` (array of string) — By default, special characters are dropped from synonyms. Use this attribute to specify which special characters should be indexed as is
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /synonym_sets/{synonymSetName}/items/{itemId}

**Delete a synonym set item**

Delete a specific synonym item by its id

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `synonymSetName` | path | string | Yes | The name of the synonym set |
| `itemId` | path | string | Yes | The id of the synonym item to delete |

**Responses**

- **200** — Synonym item successfully deleted
  Body (`application/json`, object):
  - `id` (string, required) — ID of the deleted synonym item
- **404** — Synonym item not found
  Body (`application/json`, object):
  - `message` (string, required)

## curation_sets

Manage curation sets

### GET /curation_sets

**List all curation sets**

Retrieve all curation sets

**Responses**

- **200** — List of all curation sets
  Body (`application/json`, array of object):
  - `items` (array of object, required) — Array of curation items
    - `rule` (object, required)
      - `tags` (array of string) — List of tag values to associate with this curation rule.
      - `query` (string) — Indicates what search queries should be curated
      - `match` (string) — Indicates whether the match on the query term should be `exact` or `contains`. If we want to match all queries that contained the word `apple`, we will use the `contains` match instead. Allowed values: `exact`, `contains`.
      - `filter_by` (string) — Indicates that the curation should apply when the filter_by parameter in a search query exactly matches the string specified here (including backticks, spaces, brackets, etc).
    - `includes` (array of object) — List of document `id`s that should be included in the search results with their corresponding `position`s.
      - `id` (string, required) — document id that should be included
      - `position` (integer, required) — position number where document should be included in the search results
    - `excludes` (array of object) — List of document `id`s that should be excluded from the search results.
      - `id` (string, required) — document id that should be excluded from the search results.
    - `filter_by` (string) — A filter by clause that is applied to any search query that matches the curation rule.
    - `remove_matched_tokens` (boolean) — Indicates whether search query tokens that exist in the curation's rule should be removed from the search query.
    - `metadata` (object) — Return a custom JSON object in the Search API response, when this rule is triggered. This can can be used to display a pre-defined message (eg: a promotion banner) on the front-end when a particular rule is triggered.
    - `sort_by` (string) — A sort by clause that is applied to any search query that matches the curation rule.
    - `replace_query` (string) — Replaces the current search query with this value, when the search query matches the curation rule.
    - `filter_curated_hits` (boolean) — When set to true, the filter conditions of the query is applied to the curated records as well. Default: false.
    - `effective_from_ts` (integer) — A Unix timestamp that indicates the date/time from which the curation will be active. You can use this to create rules that start applying from a future point in time.
    - `effective_to_ts` (integer) — A Unix timestamp that indicates the date/time until which the curation will be active. You can use this to create rules that stop applying after a period of time.
    - `stop_processing` (boolean) — When set to true, curation processing will stop at the first matching rule. When set to false curation processing will continue and multiple curation actions will be triggered in sequence. Curations are processed in the lexical sort order of their id field.
    - `id` (string) — ID of the curation item
  - `description` (string) — Optional description for the curation set
  - `name` (string, required)

### GET /curation_sets/{curationSetName}

**Retrieve a curation set**

Retrieve a specific curation set by its name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `curationSetName` | path | string | Yes | The name of the curation set to retrieve |

**Responses**

- **200** — Curation set fetched
  Body (`application/json`, object):
  - `items` (array of object, required) — Array of curation items
    - `rule` (object, required)
      - `tags` (array of string) — List of tag values to associate with this curation rule.
      - `query` (string) — Indicates what search queries should be curated
      - `match` (string) — Indicates whether the match on the query term should be `exact` or `contains`. If we want to match all queries that contained the word `apple`, we will use the `contains` match instead. Allowed values: `exact`, `contains`.
      - `filter_by` (string) — Indicates that the curation should apply when the filter_by parameter in a search query exactly matches the string specified here (including backticks, spaces, brackets, etc).
    - `includes` (array of object) — List of document `id`s that should be included in the search results with their corresponding `position`s.
      - `id` (string, required) — document id that should be included
      - `position` (integer, required) — position number where document should be included in the search results
    - `excludes` (array of object) — List of document `id`s that should be excluded from the search results.
      - `id` (string, required) — document id that should be excluded from the search results.
    - `filter_by` (string) — A filter by clause that is applied to any search query that matches the curation rule.
    - `remove_matched_tokens` (boolean) — Indicates whether search query tokens that exist in the curation's rule should be removed from the search query.
    - `metadata` (object) — Return a custom JSON object in the Search API response, when this rule is triggered. This can can be used to display a pre-defined message (eg: a promotion banner) on the front-end when a particular rule is triggered.
    - `sort_by` (string) — A sort by clause that is applied to any search query that matches the curation rule.
    - `replace_query` (string) — Replaces the current search query with this value, when the search query matches the curation rule.
    - `filter_curated_hits` (boolean) — When set to true, the filter conditions of the query is applied to the curated records as well. Default: false.
    - `effective_from_ts` (integer) — A Unix timestamp that indicates the date/time from which the curation will be active. You can use this to create rules that start applying from a future point in time.
    - `effective_to_ts` (integer) — A Unix timestamp that indicates the date/time until which the curation will be active. You can use this to create rules that stop applying after a period of time.
    - `stop_processing` (boolean) — When set to true, curation processing will stop at the first matching rule. When set to false curation processing will continue and multiple curation actions will be triggered in sequence. Curations are processed in the lexical sort order of their id field.
    - `id` (string) — ID of the curation item
  - `description` (string) — Optional description for the curation set
  - `name` (string, required)
- **404** — Curation set not found
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /curation_sets/{curationSetName}

**Create or update a curation set**

Create or update a curation set with the given name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `curationSetName` | path | string | Yes | The name of the curation set to create/update |

**Request body** (`application/json`, required)

The curation set to be created/updated

- `items` (array of object, required) — Array of curation items
  - `rule` (object, required)
    - `tags` (array of string) — List of tag values to associate with this curation rule.
    - `query` (string) — Indicates what search queries should be curated
    - `match` (string) — Indicates whether the match on the query term should be `exact` or `contains`. If we want to match all queries that contained the word `apple`, we will use the `contains` match instead. Allowed values: `exact`, `contains`.
    - `filter_by` (string) — Indicates that the curation should apply when the filter_by parameter in a search query exactly matches the string specified here (including backticks, spaces, brackets, etc).
  - `includes` (array of object) — List of document `id`s that should be included in the search results with their corresponding `position`s.
    - `id` (string, required) — document id that should be included
    - `position` (integer, required) — position number where document should be included in the search results
  - `excludes` (array of object) — List of document `id`s that should be excluded from the search results.
    - `id` (string, required) — document id that should be excluded from the search results.
  - `filter_by` (string) — A filter by clause that is applied to any search query that matches the curation rule.
  - `remove_matched_tokens` (boolean) — Indicates whether search query tokens that exist in the curation's rule should be removed from the search query.
  - `metadata` (object) — Return a custom JSON object in the Search API response, when this rule is triggered. This can can be used to display a pre-defined message (eg: a promotion banner) on the front-end when a particular rule is triggered.
  - `sort_by` (string) — A sort by clause that is applied to any search query that matches the curation rule.
  - `replace_query` (string) — Replaces the current search query with this value, when the search query matches the curation rule.
  - `filter_curated_hits` (boolean) — When set to true, the filter conditions of the query is applied to the curated records as well. Default: false.
  - `effective_from_ts` (integer) — A Unix timestamp that indicates the date/time from which the curation will be active. You can use this to create rules that start applying from a future point in time.
  - `effective_to_ts` (integer) — A Unix timestamp that indicates the date/time until which the curation will be active. You can use this to create rules that stop applying after a period of time.
  - `stop_processing` (boolean) — When set to true, curation processing will stop at the first matching rule. When set to false curation processing will continue and multiple curation actions will be triggered in sequence. Curations are processed in the lexical sort order of their id field.
  - `id` (string) — ID of the curation item
- `description` (string) — Optional description for the curation set

**Responses**

- **200** — Curation set successfully created/updated
  Body (`application/json`, object):
  - `items` (array of object, required) — Array of curation items
    - `rule` (object, required)
      - `tags` (array of string) — List of tag values to associate with this curation rule.
      - `query` (string) — Indicates what search queries should be curated
      - `match` (string) — Indicates whether the match on the query term should be `exact` or `contains`. If we want to match all queries that contained the word `apple`, we will use the `contains` match instead. Allowed values: `exact`, `contains`.
      - `filter_by` (string) — Indicates that the curation should apply when the filter_by parameter in a search query exactly matches the string specified here (including backticks, spaces, brackets, etc).
    - `includes` (array of object) — List of document `id`s that should be included in the search results with their corresponding `position`s.
      - `id` (string, required) — document id that should be included
      - `position` (integer, required) — position number where document should be included in the search results
    - `excludes` (array of object) — List of document `id`s that should be excluded from the search results.
      - `id` (string, required) — document id that should be excluded from the search results.
    - `filter_by` (string) — A filter by clause that is applied to any search query that matches the curation rule.
    - `remove_matched_tokens` (boolean) — Indicates whether search query tokens that exist in the curation's rule should be removed from the search query.
    - `metadata` (object) — Return a custom JSON object in the Search API response, when this rule is triggered. This can can be used to display a pre-defined message (eg: a promotion banner) on the front-end when a particular rule is triggered.
    - `sort_by` (string) — A sort by clause that is applied to any search query that matches the curation rule.
    - `replace_query` (string) — Replaces the current search query with this value, when the search query matches the curation rule.
    - `filter_curated_hits` (boolean) — When set to true, the filter conditions of the query is applied to the curated records as well. Default: false.
    - `effective_from_ts` (integer) — A Unix timestamp that indicates the date/time from which the curation will be active. You can use this to create rules that start applying from a future point in time.
    - `effective_to_ts` (integer) — A Unix timestamp that indicates the date/time until which the curation will be active. You can use this to create rules that stop applying after a period of time.
    - `stop_processing` (boolean) — When set to true, curation processing will stop at the first matching rule. When set to false curation processing will continue and multiple curation actions will be triggered in sequence. Curations are processed in the lexical sort order of their id field.
    - `id` (string) — ID of the curation item
  - `description` (string) — Optional description for the curation set
  - `name` (string, required)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /curation_sets/{curationSetName}

**Delete a curation set**

Delete a specific curation set by its name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `curationSetName` | path | string | Yes | The name of the curation set to delete |

**Responses**

- **200** — Curation set successfully deleted
  Body (`application/json`, object):
  - `name` (string, required) — Name of the deleted curation set
- **404** — Curation set not found
  Body (`application/json`, object):
  - `message` (string, required)

### GET /curation_sets/{curationSetName}/items

**List items in a curation set**

Retrieve all curation items in a set

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `curationSetName` | path | string | Yes | The name of the curation set to retrieve items for |

**Responses**

- **200** — List of curation items
  Body (`application/json`, array of object):
  - `rule` (object, required)
    - `tags` (array of string) — List of tag values to associate with this curation rule.
    - `query` (string) — Indicates what search queries should be curated
    - `match` (string) — Indicates whether the match on the query term should be `exact` or `contains`. If we want to match all queries that contained the word `apple`, we will use the `contains` match instead. Allowed values: `exact`, `contains`.
    - `filter_by` (string) — Indicates that the curation should apply when the filter_by parameter in a search query exactly matches the string specified here (including backticks, spaces, brackets, etc).
  - `includes` (array of object) — List of document `id`s that should be included in the search results with their corresponding `position`s.
    - `id` (string, required) — document id that should be included
    - `position` (integer, required) — position number where document should be included in the search results
  - `excludes` (array of object) — List of document `id`s that should be excluded from the search results.
    - `id` (string, required) — document id that should be excluded from the search results.
  - `filter_by` (string) — A filter by clause that is applied to any search query that matches the curation rule.
  - `remove_matched_tokens` (boolean) — Indicates whether search query tokens that exist in the curation's rule should be removed from the search query.
  - `metadata` (object) — Return a custom JSON object in the Search API response, when this rule is triggered. This can can be used to display a pre-defined message (eg: a promotion banner) on the front-end when a particular rule is triggered.
  - `sort_by` (string) — A sort by clause that is applied to any search query that matches the curation rule.
  - `replace_query` (string) — Replaces the current search query with this value, when the search query matches the curation rule.
  - `filter_curated_hits` (boolean) — When set to true, the filter conditions of the query is applied to the curated records as well. Default: false.
  - `effective_from_ts` (integer) — A Unix timestamp that indicates the date/time from which the curation will be active. You can use this to create rules that start applying from a future point in time.
  - `effective_to_ts` (integer) — A Unix timestamp that indicates the date/time until which the curation will be active. You can use this to create rules that stop applying after a period of time.
  - `stop_processing` (boolean) — When set to true, curation processing will stop at the first matching rule. When set to false curation processing will continue and multiple curation actions will be triggered in sequence. Curations are processed in the lexical sort order of their id field.
  - `id` (string, required)
- **404** — Curation set not found
  Body (`application/json`, object):
  - `message` (string, required)

### GET /curation_sets/{curationSetName}/items/{itemId}

**Retrieve a curation set item**

Retrieve a specific curation item by its id

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `curationSetName` | path | string | Yes | The name of the curation set |
| `itemId` | path | string | Yes | The id of the curation item to retrieve |

**Responses**

- **200** — Curation item fetched
  Body (`application/json`, object):
  - `rule` (object, required)
    - `tags` (array of string) — List of tag values to associate with this curation rule.
    - `query` (string) — Indicates what search queries should be curated
    - `match` (string) — Indicates whether the match on the query term should be `exact` or `contains`. If we want to match all queries that contained the word `apple`, we will use the `contains` match instead. Allowed values: `exact`, `contains`.
    - `filter_by` (string) — Indicates that the curation should apply when the filter_by parameter in a search query exactly matches the string specified here (including backticks, spaces, brackets, etc).
  - `includes` (array of object) — List of document `id`s that should be included in the search results with their corresponding `position`s.
    - `id` (string, required) — document id that should be included
    - `position` (integer, required) — position number where document should be included in the search results
  - `excludes` (array of object) — List of document `id`s that should be excluded from the search results.
    - `id` (string, required) — document id that should be excluded from the search results.
  - `filter_by` (string) — A filter by clause that is applied to any search query that matches the curation rule.
  - `remove_matched_tokens` (boolean) — Indicates whether search query tokens that exist in the curation's rule should be removed from the search query.
  - `metadata` (object) — Return a custom JSON object in the Search API response, when this rule is triggered. This can can be used to display a pre-defined message (eg: a promotion banner) on the front-end when a particular rule is triggered.
  - `sort_by` (string) — A sort by clause that is applied to any search query that matches the curation rule.
  - `replace_query` (string) — Replaces the current search query with this value, when the search query matches the curation rule.
  - `filter_curated_hits` (boolean) — When set to true, the filter conditions of the query is applied to the curated records as well. Default: false.
  - `effective_from_ts` (integer) — A Unix timestamp that indicates the date/time from which the curation will be active. You can use this to create rules that start applying from a future point in time.
  - `effective_to_ts` (integer) — A Unix timestamp that indicates the date/time until which the curation will be active. You can use this to create rules that stop applying after a period of time.
  - `stop_processing` (boolean) — When set to true, curation processing will stop at the first matching rule. When set to false curation processing will continue and multiple curation actions will be triggered in sequence. Curations are processed in the lexical sort order of their id field.
  - `id` (string, required)
- **404** — Curation item not found
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /curation_sets/{curationSetName}/items/{itemId}

**Create or update a curation set item**

Create or update a curation set item with the given id

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `curationSetName` | path | string | Yes | The name of the curation set |
| `itemId` | path | string | Yes | The id of the curation item to upsert |

**Request body** (`application/json`, required)

The curation item to be created/updated

- `rule` (object, required)
  - `tags` (array of string) — List of tag values to associate with this curation rule.
  - `query` (string) — Indicates what search queries should be curated
  - `match` (string) — Indicates whether the match on the query term should be `exact` or `contains`. If we want to match all queries that contained the word `apple`, we will use the `contains` match instead. Allowed values: `exact`, `contains`.
  - `filter_by` (string) — Indicates that the curation should apply when the filter_by parameter in a search query exactly matches the string specified here (including backticks, spaces, brackets, etc).
- `includes` (array of object) — List of document `id`s that should be included in the search results with their corresponding `position`s.
  - `id` (string, required) — document id that should be included
  - `position` (integer, required) — position number where document should be included in the search results
- `excludes` (array of object) — List of document `id`s that should be excluded from the search results.
  - `id` (string, required) — document id that should be excluded from the search results.
- `filter_by` (string) — A filter by clause that is applied to any search query that matches the curation rule.
- `remove_matched_tokens` (boolean) — Indicates whether search query tokens that exist in the curation's rule should be removed from the search query.
- `metadata` (object) — Return a custom JSON object in the Search API response, when this rule is triggered. This can can be used to display a pre-defined message (eg: a promotion banner) on the front-end when a particular rule is triggered.
- `sort_by` (string) — A sort by clause that is applied to any search query that matches the curation rule.
- `replace_query` (string) — Replaces the current search query with this value, when the search query matches the curation rule.
- `filter_curated_hits` (boolean) — When set to true, the filter conditions of the query is applied to the curated records as well. Default: false.
- `effective_from_ts` (integer) — A Unix timestamp that indicates the date/time from which the curation will be active. You can use this to create rules that start applying from a future point in time.
- `effective_to_ts` (integer) — A Unix timestamp that indicates the date/time until which the curation will be active. You can use this to create rules that stop applying after a period of time.
- `stop_processing` (boolean) — When set to true, curation processing will stop at the first matching rule. When set to false curation processing will continue and multiple curation actions will be triggered in sequence. Curations are processed in the lexical sort order of their id field.
- `id` (string) — ID of the curation item

**Responses**

- **200** — Curation item successfully created/updated
  Body (`application/json`, object):
  - `rule` (object, required)
    - `tags` (array of string) — List of tag values to associate with this curation rule.
    - `query` (string) — Indicates what search queries should be curated
    - `match` (string) — Indicates whether the match on the query term should be `exact` or `contains`. If we want to match all queries that contained the word `apple`, we will use the `contains` match instead. Allowed values: `exact`, `contains`.
    - `filter_by` (string) — Indicates that the curation should apply when the filter_by parameter in a search query exactly matches the string specified here (including backticks, spaces, brackets, etc).
  - `includes` (array of object) — List of document `id`s that should be included in the search results with their corresponding `position`s.
    - `id` (string, required) — document id that should be included
    - `position` (integer, required) — position number where document should be included in the search results
  - `excludes` (array of object) — List of document `id`s that should be excluded from the search results.
    - `id` (string, required) — document id that should be excluded from the search results.
  - `filter_by` (string) — A filter by clause that is applied to any search query that matches the curation rule.
  - `remove_matched_tokens` (boolean) — Indicates whether search query tokens that exist in the curation's rule should be removed from the search query.
  - `metadata` (object) — Return a custom JSON object in the Search API response, when this rule is triggered. This can can be used to display a pre-defined message (eg: a promotion banner) on the front-end when a particular rule is triggered.
  - `sort_by` (string) — A sort by clause that is applied to any search query that matches the curation rule.
  - `replace_query` (string) — Replaces the current search query with this value, when the search query matches the curation rule.
  - `filter_curated_hits` (boolean) — When set to true, the filter conditions of the query is applied to the curated records as well. Default: false.
  - `effective_from_ts` (integer) — A Unix timestamp that indicates the date/time from which the curation will be active. You can use this to create rules that start applying from a future point in time.
  - `effective_to_ts` (integer) — A Unix timestamp that indicates the date/time until which the curation will be active. You can use this to create rules that stop applying after a period of time.
  - `stop_processing` (boolean) — When set to true, curation processing will stop at the first matching rule. When set to false curation processing will continue and multiple curation actions will be triggered in sequence. Curations are processed in the lexical sort order of their id field.
  - `id` (string, required)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /curation_sets/{curationSetName}/items/{itemId}

**Delete a curation set item**

Delete a specific curation item by its id

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `curationSetName` | path | string | Yes | The name of the curation set |
| `itemId` | path | string | Yes | The id of the curation item to delete |

**Responses**

- **200** — Curation item successfully deleted
  Body (`application/json`, object):
  - `id` (string, required) — ID of the deleted curation item
- **404** — Curation item not found
  Body (`application/json`, object):
  - `message` (string, required)

## conversations

Conversational Search (RAG)

### GET /conversations/models

**List all conversation models**

Retrieve all conversation models

**Responses**

- **200** — List of all conversation models
  Body (`application/json`, array of object):
  - `id` (string, required) — An explicit id for the model, otherwise the API will return a response with an auto-generated conversation model id.
  - `model_name` (string, required) — Name of the LLM model offered by OpenAI, Cloudflare or vLLM
  - `api_key` (string) — The LLM service's API Key
  - `history_collection` (string, required) — Typesense collection that stores the historical conversations
  - `account_id` (string) — LLM service's account ID (only applicable for Cloudflare)
  - `system_prompt` (string) — The system prompt that contains special instructions to the LLM
  - `ttl` (integer) — Time interval in seconds after which the messages would be deleted. Default: 86400 (24 hours)
  - `max_bytes` (integer, required) — The maximum number of bytes to send to the LLM in every API call. Consult the LLM's documentation on the number of bytes supported in the context window.
  - `vllm_url` (string) — URL of vLLM service

### POST /conversations/models

**Create a conversation model**

Create a Conversation Model

**Request body** (`application/json`, required)

- `id` (string) — An explicit id for the model, otherwise the API will return a response with an auto-generated conversation model id.
- `model_name` (string, required) — Name of the LLM model offered by OpenAI, Cloudflare or vLLM
- `api_key` (string) — The LLM service's API Key
- `history_collection` (string, required) — Typesense collection that stores the historical conversations
- `account_id` (string) — LLM service's account ID (only applicable for Cloudflare)
- `system_prompt` (string) — The system prompt that contains special instructions to the LLM
- `ttl` (integer) — Time interval in seconds after which the messages would be deleted. Default: 86400 (24 hours)
- `max_bytes` (integer, required) — The maximum number of bytes to send to the LLM in every API call. Consult the LLM's documentation on the number of bytes supported in the context window.
- `vllm_url` (string) — URL of vLLM service

**Responses**

- **201** — Created Conversation Model
  Body (`application/json`, object):
  - `id` (string, required) — An explicit id for the model, otherwise the API will return a response with an auto-generated conversation model id.
  - `model_name` (string, required) — Name of the LLM model offered by OpenAI, Cloudflare or vLLM
  - `api_key` (string) — The LLM service's API Key
  - `history_collection` (string, required) — Typesense collection that stores the historical conversations
  - `account_id` (string) — LLM service's account ID (only applicable for Cloudflare)
  - `system_prompt` (string) — The system prompt that contains special instructions to the LLM
  - `ttl` (integer) — Time interval in seconds after which the messages would be deleted. Default: 86400 (24 hours)
  - `max_bytes` (integer, required) — The maximum number of bytes to send to the LLM in every API call. Consult the LLM's documentation on the number of bytes supported in the context window.
  - `vllm_url` (string) — URL of vLLM service
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### GET /conversations/models/{modelId}

**Retrieve a conversation model**

Retrieve a conversation model

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `modelId` | path | string | Yes | The id of the conversation model to retrieve |

**Responses**

- **200** — A conversation model
  Body (`application/json`, object):
  - `id` (string, required) — An explicit id for the model, otherwise the API will return a response with an auto-generated conversation model id.
  - `model_name` (string, required) — Name of the LLM model offered by OpenAI, Cloudflare or vLLM
  - `api_key` (string) — The LLM service's API Key
  - `history_collection` (string, required) — Typesense collection that stores the historical conversations
  - `account_id` (string) — LLM service's account ID (only applicable for Cloudflare)
  - `system_prompt` (string) — The system prompt that contains special instructions to the LLM
  - `ttl` (integer) — Time interval in seconds after which the messages would be deleted. Default: 86400 (24 hours)
  - `max_bytes` (integer, required) — The maximum number of bytes to send to the LLM in every API call. Consult the LLM's documentation on the number of bytes supported in the context window.
  - `vllm_url` (string) — URL of vLLM service

### PUT /conversations/models/{modelId}

**Update a conversation model**

Update a conversation model

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `modelId` | path | string | Yes | The id of the conversation model to update |

**Request body** (`application/json`, required)

- `id` (string) — An explicit id for the model, otherwise the API will return a response with an auto-generated conversation model id.
- `model_name` (string) — Name of the LLM model offered by OpenAI, Cloudflare or vLLM
- `api_key` (string) — The LLM service's API Key
- `history_collection` (string) — Typesense collection that stores the historical conversations
- `account_id` (string) — LLM service's account ID (only applicable for Cloudflare)
- `system_prompt` (string) — The system prompt that contains special instructions to the LLM
- `ttl` (integer) — Time interval in seconds after which the messages would be deleted. Default: 86400 (24 hours)
- `max_bytes` (integer) — The maximum number of bytes to send to the LLM in every API call. Consult the LLM's documentation on the number of bytes supported in the context window.
- `vllm_url` (string) — URL of vLLM service

**Responses**

- **200** — The conversation model was successfully updated
  Body (`application/json`, object):
  - `id` (string, required) — An explicit id for the model, otherwise the API will return a response with an auto-generated conversation model id.
  - `model_name` (string, required) — Name of the LLM model offered by OpenAI, Cloudflare or vLLM
  - `api_key` (string) — The LLM service's API Key
  - `history_collection` (string, required) — Typesense collection that stores the historical conversations
  - `account_id` (string) — LLM service's account ID (only applicable for Cloudflare)
  - `system_prompt` (string) — The system prompt that contains special instructions to the LLM
  - `ttl` (integer) — Time interval in seconds after which the messages would be deleted. Default: 86400 (24 hours)
  - `max_bytes` (integer, required) — The maximum number of bytes to send to the LLM in every API call. Consult the LLM's documentation on the number of bytes supported in the context window.
  - `vllm_url` (string) — URL of vLLM service

### DELETE /conversations/models/{modelId}

**Delete a conversation model**

Delete a conversation model

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `modelId` | path | string | Yes | The id of the conversation model to delete |

**Responses**

- **200** — The conversation model was successfully deleted
  Body (`application/json`, object):
  - `id` (string, required) — An explicit id for the model, otherwise the API will return a response with an auto-generated conversation model id.
  - `model_name` (string, required) — Name of the LLM model offered by OpenAI, Cloudflare or vLLM
  - `api_key` (string) — The LLM service's API Key
  - `history_collection` (string, required) — Typesense collection that stores the historical conversations
  - `account_id` (string) — LLM service's account ID (only applicable for Cloudflare)
  - `system_prompt` (string) — The system prompt that contains special instructions to the LLM
  - `ttl` (integer) — Time interval in seconds after which the messages would be deleted. Default: 86400 (24 hours)
  - `max_bytes` (integer, required) — The maximum number of bytes to send to the LLM in every API call. Consult the LLM's documentation on the number of bytes supported in the context window.
  - `vllm_url` (string) — URL of vLLM service

## keys

Manage API Keys with fine-grain access control

### GET /keys

**Retrieve (metadata about) all keys.**

**Responses**

- **200** — List of all keys
  Body (`application/json`, object):
  - `keys` (array of object, required)
    - `value` (string)
    - `description` (string, required)
    - `actions` (array of string, required)
    - `collections` (array of string, required)
    - `expires_at` (integer (int64))
    - `id` (integer (int64))
    - `value_prefix` (string)

### POST /keys

**Create an API Key**

Create an API Key with fine-grain access control. You can restrict access on both a per-collection and per-action level. The generated key is returned only during creation. You want to store this key carefully in a secure place.

**Request body** (`application/json`)

The object that describes API key scope

- `value` (string)
- `description` (string, required)
- `actions` (array of string, required)
- `collections` (array of string, required)
- `expires_at` (integer (int64))

**Responses**

- **201** — Created API key
  Body (`application/json`, object):
  - `value` (string)
  - `description` (string, required)
  - `actions` (array of string, required)
  - `collections` (array of string, required)
  - `expires_at` (integer (int64))
  - `id` (integer (int64))
  - `value_prefix` (string)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **409** — API key generation conflict
  Body (`application/json`, object):
  - `message` (string, required)

### GET /keys/{keyId}

**Retrieve (metadata about) a key**

Retrieve (metadata about) a key. Only the key prefix is returned when you retrieve a key. Due to security reasons, only the create endpoint returns the full API key.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `keyId` | path | integer (int64) | Yes | The ID of the key to retrieve |

**Responses**

- **200** — The key referenced by the ID
  Body (`application/json`, object):
  - `value` (string)
  - `description` (string, required)
  - `actions` (array of string, required)
  - `collections` (array of string, required)
  - `expires_at` (integer (int64))
  - `id` (integer (int64))
  - `value_prefix` (string)
- **404** — The key was not found
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /keys/{keyId}

**Delete an API key given its ID.**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `keyId` | path | integer (int64) | Yes | The ID of the key to delete |

**Responses**

- **200** — The key referenced by the ID
  Body (`application/json`, object):
  - `id` (integer (int64), required) — The id of the API key that was deleted
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **404** — Key not found
  Body (`application/json`, object):
  - `message` (string, required)

## debug

Debugging information

### GET /debug

**Print debugging information**

Print debugging information

**Responses**

- **200** — Debugging information
  Body (`application/json`, object):
  - `version` (string)

## health

### GET /health

**Checks if Typesense server is ready to accept requests.**

Checks if Typesense server is ready to accept requests.

**Responses**

- **200** — Search service is ready for requests.
  Body (`application/json`, object):
  - `ok` (boolean, required)

## operations

Manage Typesense cluster

### GET /operations/schema_changes

**Get the status of in-progress schema change operations**

Returns the status of any ongoing schema change operations. If no schema changes are in progress, returns an empty response.

**Responses**

- **200** — List of schema changes in progress
  Body (`application/json`, array of object):
  - `collection` (string) — Name of the collection being modified
  - `validated_docs` (integer) — Number of documents that have been validated
  - `altered_docs` (integer) — Number of documents that have been altered

### POST /operations/snapshot

**Creates a point-in-time snapshot of a Typesense node's state and data in the specified directory.**

Creates a point-in-time snapshot of a Typesense node's state and data in the specified directory. You can then backup the snapshot directory that gets created and later restore it as a data directory, as needed.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `snapshot_path` | query | string | Yes | The directory on the server where the snapshot should be saved. |

**Responses**

- **201** — Snapshot is created.
  Body (`application/json`, object):
  - `success` (boolean, required)

### POST /operations/vote

**Triggers a follower node to initiate the raft voting process, which triggers leader re-election.**

Triggers a follower node to initiate the raft voting process, which triggers leader re-election. The follower node that you run this operation against will become the new leader, once this command succeeds.

**Responses**

- **200** — Re-election is performed.
  Body (`application/json`, object):
  - `success` (boolean, required)

### POST /operations/cache/clear

**Clear the cached responses of search requests in the LRU cache.**

Clear the cached responses of search requests that are sent with `use_cache` parameter in the LRU cache.

**Responses**

- **200** — Clear cache succeeded.
  Body (`application/json`, object):
  - `success` (boolean, required)

### POST /operations/db/compact

**Compacting the on-disk database**

Typesense uses RocksDB to store your documents on the disk. If you do frequent writes or updates, you could benefit from running a compaction of the underlying RocksDB database. This could reduce the size of the database and decrease read latency. While the database will not block during this operation, we recommend running it during off-peak hours.

**Responses**

- **200** — Compacting the on-disk database succeeded.
  Body (`application/json`, object):
  - `success` (boolean, required)

### POST /config

**Toggle Slow Request Log**

Enable logging of requests that take over a defined threshold of time. Default is `-1` which disables slow request logging. Slow requests are logged to the primary log file, with the prefix SLOW REQUEST.

**Request body** (`application/json`)

- `log-slow-requests-time-ms` (integer, required)

Example:

```json
"{\"log-slow-requests-time-ms\": 2000}\n"
```

**Responses**

- **200** — Toggle Slow Request Log database succeeded.
  Body (`application/json`, object):
  - `success` (boolean, required)

### GET /metrics.json

**Get current RAM, CPU, Disk & Network usage metrics.**

Retrieve the metrics.

**Responses**

- **200** — Metrics fetched.

### GET /stats.json

**Get stats about API endpoints.**

Retrieve the stats about API endpoints.

**Responses**

- **200** — Stats fetched.
  Body (`application/json`, object):
  - `delete_latency_ms` (number (double))
  - `delete_requests_per_second` (number (double))
  - `import_latency_ms` (number (double))
  - `import_requests_per_second` (number (double))
  - `latency_ms` (object)
  - `overloaded_requests_per_second` (number (double))
  - `pending_write_batches` (number (double))
  - `requests_per_second` (object)
  - `search_latency_ms` (number (double))
  - `search_requests_per_second` (number (double))
  - `total_requests_per_second` (number (double))
  - `write_latency_ms` (number (double))
  - `write_requests_per_second` (number (double))

## analytics

Typesense can aggregate search queries for both analytics purposes and for query suggestions.

### GET /analytics/events

**Retrieve analytics events**

Retrieve the most recent events for a user and rule.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `user_id` | query | string | Yes |  |
| `name` | query | string | Yes | Analytics rule name |
| `n` | query | integer | Yes | Number of events to return (max 1000) |

**Responses**

- **200** — Events fetched
  Body (`application/json`, object):
  - `events` (array of object, required)
    - `name` (string)
    - `event_type` (string)
    - `collection` (string)
    - `timestamp` (integer (int64))
    - `user_id` (string)
    - `doc_id` (string)
    - `doc_ids` (array of string)
    - `query` (string)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### POST /analytics/events

**Create an analytics event**

Submit a single analytics event. The event must correspond to an existing analytics rule by name.

**Request body** (`application/json`, required)

The analytics event to be created

- `name` (string, required) — Name of the analytics rule this event corresponds to
- `event_type` (string, required) — Type of event (e.g., click, conversion, query, visit)
- `data` (object, required) — Event payload
  - `user_id` (string)
  - `doc_id` (string)
  - `doc_ids` (array of string)
  - `q` (string)
  - `analytics_tag` (string)

**Responses**

- **200** — Analytics event successfully created
  Body (`application/json`, object):
  - `ok` (boolean, required)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### POST /analytics/flush

**Flush in-memory analytics to disk**

Triggers a flush of analytics data to persistent storage.

**Responses**

- **200** — Flush triggered
  Body (`application/json`, object):
  - `ok` (boolean, required)

### GET /analytics/status

**Get analytics subsystem status**

Returns sizes of internal analytics buffers and queues.

**Responses**

- **200** — Status fetched
  Body (`application/json`, object):
  - `popular_prefix_queries` (integer)
  - `nohits_prefix_queries` (integer)
  - `log_prefix_queries` (integer)
  - `query_log_events` (integer)
  - `query_counter_events` (integer)
  - `doc_log_events` (integer)
  - `doc_counter_events` (integer)

### GET /analytics/rules

**Retrieve analytics rules**

Retrieve all analytics rules. Use the optional rule_tag filter to narrow down results.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `rule_tag` | query | string | No | Filter rules by rule_tag |

**Responses**

- **200** — Analytics rules fetched
  Body (`application/json`, array of object):
  - `name` (string, required)
  - `type` (string, required) — Allowed values: `popular_queries`, `nohits_queries`, `counter`, `log`.
  - `collection` (string, required)
  - `event_type` (string, required)
  - `rule_tag` (string)
  - `params` (object)
    - `destination_collection` (string)
    - `limit` (integer)
    - `capture_search_requests` (boolean)
    - `meta_fields` (array of string)
    - `expand_query` (boolean)
    - `counter_field` (string)
    - `weight` (integer)

### POST /analytics/rules

**Create analytics rule(s)**

Create one or more analytics rules. You can send a single rule object or an array of rule objects.

**Request body** (`application/json`, required)

The analytics rule(s) to be created

- `name` (string, required)
- `type` (string, required) — Allowed values: `popular_queries`, `nohits_queries`, `counter`, `log`.
- `collection` (string, required)
- `event_type` (string, required)
- `rule_tag` (string)
- `params` (object)
  - `destination_collection` (string)
  - `limit` (integer)
  - `capture_search_requests` (boolean)
  - `meta_fields` (array of string)
  - `expand_query` (boolean)
  - `counter_field` (string)
  - `weight` (integer)

**Responses**

- **200** — Analytics rule(s) successfully created
  Body (`application/json`, one of several types):
  - `name` (string, required)
  - `type` (string, required) — Allowed values: `popular_queries`, `nohits_queries`, `counter`, `log`.
  - `collection` (string, required)
  - `event_type` (string, required)
  - `rule_tag` (string)
  - `params` (object)
    - `destination_collection` (string)
    - `limit` (integer)
    - `capture_search_requests` (boolean)
    - `meta_fields` (array of string)
    - `expand_query` (boolean)
    - `counter_field` (string)
    - `weight` (integer)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### GET /analytics/rules/{ruleName}

**Retrieves an analytics rule**

Retrieve the details of an analytics rule, given it's name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ruleName` | path | string | Yes | The name of the analytics rule to retrieve |

**Responses**

- **200** — Analytics rule fetched
  Body (`application/json`, object):
  - `name` (string, required)
  - `type` (string, required) — Allowed values: `popular_queries`, `nohits_queries`, `counter`, `log`.
  - `collection` (string, required)
  - `event_type` (string, required)
  - `rule_tag` (string)
  - `params` (object)
    - `destination_collection` (string)
    - `limit` (integer)
    - `capture_search_requests` (boolean)
    - `meta_fields` (array of string)
    - `expand_query` (boolean)
    - `counter_field` (string)
    - `weight` (integer)
- **404** — Analytics rule not found
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /analytics/rules/{ruleName}

**Upserts an analytics rule**

Upserts an analytics rule with the given name.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ruleName` | path | string | Yes | The name of the analytics rule to upsert |

**Request body** (`application/json`, required)

The Analytics rule to be upserted

- `name` (string)
- `rule_tag` (string)
- `params` (object)
  - `destination_collection` (string)
  - `limit` (integer)
  - `capture_search_requests` (boolean)
  - `meta_fields` (array of string)
  - `expand_query` (boolean)
  - `counter_field` (string)
  - `weight` (integer)

**Responses**

- **200** — Analytics rule successfully upserted
  Body (`application/json`, object):
  - `name` (string, required)
  - `type` (string, required) — Allowed values: `popular_queries`, `nohits_queries`, `counter`, `log`.
  - `collection` (string, required)
  - `event_type` (string, required)
  - `rule_tag` (string)
  - `params` (object)
    - `destination_collection` (string)
    - `limit` (integer)
    - `capture_search_requests` (boolean)
    - `meta_fields` (array of string)
    - `expand_query` (boolean)
    - `counter_field` (string)
    - `weight` (integer)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /analytics/rules/{ruleName}

**Delete an analytics rule**

Permanently deletes an analytics rule, given it's name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ruleName` | path | string | Yes | The name of the analytics rule to delete |

**Responses**

- **200** — Analytics rule deleted
  Body (`application/json`, object):
  - `name` (string, required)
  - `type` (string, required) — Allowed values: `popular_queries`, `nohits_queries`, `counter`, `log`.
  - `collection` (string, required)
  - `event_type` (string, required)
  - `rule_tag` (string)
  - `params` (object)
    - `destination_collection` (string)
    - `limit` (integer)
    - `capture_search_requests` (boolean)
    - `meta_fields` (array of string)
    - `expand_query` (boolean)
    - `counter_field` (string)
    - `weight` (integer)
- **404** — Analytics rule not found
  Body (`application/json`, object):
  - `message` (string, required)

## stopwords

Manage stopwords sets

### GET /stopwords

**Retrieves all stopwords sets.**

Retrieve the details of all stopwords sets

**Responses**

- **200** — Stopwords sets fetched.
  Body (`application/json`, object):
  - `stopwords` (array of object, required)
    - `id` (string, required)
    - `stopwords` (array of string, required)
    - `locale` (string)

### GET /stopwords/{setId}

**Retrieves a stopwords set.**

Retrieve the details of a stopwords set, given it's name.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `setId` | path | string | Yes | The ID of the stopwords set to retrieve. |

**Responses**

- **200** — Stopwords set fetched.
  Body (`application/json`, object):
  - `stopwords` (object, required)
    - `id` (string, required)
    - `stopwords` (array of string, required)
    - `locale` (string)
- **404** — Stopwords set not found.
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /stopwords/{setId}

**Upserts a stopwords set.**

When an analytics rule is created, we give it a name and describe the type, the source collections and the destination collection.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `setId` | path | string | Yes | The ID of the stopwords set to upsert. |

**Request body** (`application/json`, required)

The stopwords set to upsert.

- `stopwords` (array of string, required)
- `locale` (string)

Example:

```json
"{\"stopwords\": [\"Germany\", \"France\", \"Italy\"], \"locale\": \"en\"}\n"
```

**Responses**

- **200** — Stopwords set successfully upserted.
  Body (`application/json`, object):
  - `id` (string, required)
  - `stopwords` (array of string, required)
  - `locale` (string)
- **400** — Bad request, see error message for details.
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /stopwords/{setId}

**Delete a stopwords set.**

Permanently deletes a stopwords set, given it's name.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `setId` | path | string | Yes | The ID of the stopwords set to delete. |

**Responses**

- **200** — Stopwords set rule deleted.
  Body (`application/json`, object):
  - `id` (string, required)
- **404** — Stopwords set not found.
  Body (`application/json`, object):
  - `message` (string, required)

## presets

Store and reference search parameters

### GET /presets

**Retrieves all presets.**

Retrieve the details of all presets

**Responses**

- **200** — Presets fetched.
  Body (`application/json`, object):
  - `presets` (array of object, required)
    - `value` (one of several types, required)
      - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
      - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
      - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
      - `nl_query` (boolean) — Whether to use natural language processing to parse the query.
      - `nl_model_id` (string) — The ID of the natural language model to use.
      - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
      - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
      - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
      - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
      - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
      - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
      - `filter_by` (string) — Filter conditions for refining your open api validator search results. Separate multiple conditions with &&.
      - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
      - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
      - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
      - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
      - `max_facet_values` (integer) — Maximum number of facet values to be returned.
      - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
      - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
      - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
      - `page` (integer) — Results from this specific page number would be fetched.
      - `per_page` (integer) — Number of results to fetch per page. Default: 10
      - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
      - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
      - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
      - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
      - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
      - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
      - `include_fields` (string) — List of fields from the document to include in the search result
      - `exclude_fields` (string) — List of fields from the document to exclude in the search result
      - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
      - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
      - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
      - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
      - `enable_highlight_v1` (boolean) — Flag for enabling/disabling the deprecated, old highlight structure in the response. Default: true. Default: `true`.
      - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
      - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
      - `synonym_sets` (string) — List of synonym set names to associate with this search query
      - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
      - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
      - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
      - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
      - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
      - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
      - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
      - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
      - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
      - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
      - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
      - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
      - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
      - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
      - `split_join_tokens` (string) — Treat space as typo: search for q=basket ball if q=basketball is not found or vice-versa. Splitting/joining of tokens will only be attempted if the original query produces no results. To always trigger this behavior, set value to `always``. To disable, set value to `off`. Default is `fallback`.
      - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same
      - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
      - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
      - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
      - `max_candidates` (integer) — Control the number of words that Typesense considers for typo and prefix searching.
      - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
      - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
      - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
      - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
      - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
      - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
      - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
      - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
      - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
      - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
      - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
      - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
      - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
      - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
      - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
      - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
      - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
      - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
      - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
      - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
      - `conversation` (boolean) — Enable conversational search.
      - `conversation_model_id` (string) — The Id of Conversation Model to be used.
      - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
      - `union` (boolean) — When true, merges the search results from each search query into a single ordered set of hits. Default: `false`.
      - `searches` (array of object, required)
        - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
        - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
        - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
        - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
        - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
        - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
        - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
        - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
        - `filter_by` (string) — Filter conditions for refining youropen api validator search results. Separate multiple conditions with &&.
        - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
        - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
        - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
        - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
        - `max_facet_values` (integer) — Maximum number of facet values to be returned.
        - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
        - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
        - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
        - `page` (integer) — Results from this specific page number would be fetched.
        - `per_page` (integer) — Number of results to fetch per page. Default: 10
        - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
        - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
        - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
        - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
        - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
        - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
        - `include_fields` (string) — List of fields from the document to include in the search result
        - `exclude_fields` (string) — List of fields from the document to exclude in the search result
        - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
        - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
        - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
        - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
        - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
        - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
        - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
        - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
        - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
        - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
        - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
        - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
        - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
        - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
        - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
        - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
        - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
        - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
        - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
        - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
        - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same. Default: `false`.
        - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
        - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
        - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
        - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
        - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
        - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
        - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
        - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
        - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
        - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
        - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
        - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
        - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
        - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
        - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
        - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
        - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
        - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
        - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
        - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
        - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
        - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
        - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
        - `conversation` (boolean) — Enable conversational search.
        - `conversation_model_id` (string) — The Id of Conversation Model to be used.
        - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
        - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
        - `collection` (string) — The collection to search in.
        - `x-typesense-api-key` (string) — A separate search API key for each search within a multi_search request
    - `name` (string, required)

### GET /presets/{presetId}

**Retrieves a preset.**

Retrieve the details of a preset, given it's name.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `presetId` | path | string | Yes | The ID of the preset to retrieve. |

**Responses**

- **200** — Preset fetched.
  Body (`application/json`, object):
  - `value` (one of several types, required)
    - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
    - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
    - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
    - `nl_query` (boolean) — Whether to use natural language processing to parse the query.
    - `nl_model_id` (string) — The ID of the natural language model to use.
    - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
    - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
    - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
    - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
    - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
    - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
    - `filter_by` (string) — Filter conditions for refining your open api validator search results. Separate multiple conditions with &&.
    - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
    - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
    - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
    - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
    - `max_facet_values` (integer) — Maximum number of facet values to be returned.
    - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
    - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
    - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
    - `page` (integer) — Results from this specific page number would be fetched.
    - `per_page` (integer) — Number of results to fetch per page. Default: 10
    - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
    - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
    - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
    - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
    - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
    - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
    - `include_fields` (string) — List of fields from the document to include in the search result
    - `exclude_fields` (string) — List of fields from the document to exclude in the search result
    - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
    - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
    - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
    - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
    - `enable_highlight_v1` (boolean) — Flag for enabling/disabling the deprecated, old highlight structure in the response. Default: true. Default: `true`.
    - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
    - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
    - `synonym_sets` (string) — List of synonym set names to associate with this search query
    - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
    - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
    - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
    - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
    - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
    - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
    - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
    - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
    - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
    - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
    - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
    - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
    - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
    - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
    - `split_join_tokens` (string) — Treat space as typo: search for q=basket ball if q=basketball is not found or vice-versa. Splitting/joining of tokens will only be attempted if the original query produces no results. To always trigger this behavior, set value to `always``. To disable, set value to `off`. Default is `fallback`.
    - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same
    - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
    - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
    - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
    - `max_candidates` (integer) — Control the number of words that Typesense considers for typo and prefix searching.
    - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
    - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
    - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
    - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
    - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
    - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
    - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
    - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
    - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
    - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
    - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
    - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
    - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
    - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
    - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
    - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
    - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
    - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
    - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
    - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
    - `conversation` (boolean) — Enable conversational search.
    - `conversation_model_id` (string) — The Id of Conversation Model to be used.
    - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
    - `union` (boolean) — When true, merges the search results from each search query into a single ordered set of hits. Default: `false`.
    - `searches` (array of object, required)
      - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
      - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
      - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
      - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
      - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
      - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
      - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
      - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
      - `filter_by` (string) — Filter conditions for refining youropen api validator search results. Separate multiple conditions with &&.
      - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
      - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
      - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
      - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
      - `max_facet_values` (integer) — Maximum number of facet values to be returned.
      - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
      - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
      - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
      - `page` (integer) — Results from this specific page number would be fetched.
      - `per_page` (integer) — Number of results to fetch per page. Default: 10
      - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
      - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
      - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
      - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
      - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
      - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
      - `include_fields` (string) — List of fields from the document to include in the search result
      - `exclude_fields` (string) — List of fields from the document to exclude in the search result
      - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
      - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
      - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
      - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
      - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
      - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
      - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
      - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
      - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
      - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
      - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
      - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
      - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
      - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
      - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
      - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
      - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
      - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
      - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
      - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
      - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same. Default: `false`.
      - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
      - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
      - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
      - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
      - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
      - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
      - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
      - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
      - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
      - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
      - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
      - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
      - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
      - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
      - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
      - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
      - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
      - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
      - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
      - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
      - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
      - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
      - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
      - `conversation` (boolean) — Enable conversational search.
      - `conversation_model_id` (string) — The Id of Conversation Model to be used.
      - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
      - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
      - `collection` (string) — The collection to search in.
      - `x-typesense-api-key` (string) — A separate search API key for each search within a multi_search request
  - `name` (string, required)
- **404** — Preset not found.
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /presets/{presetId}

**Upserts a preset.**

Create or update an existing preset.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `presetId` | path | string | Yes | The name of the preset set to upsert. |

**Request body** (`application/json`, required)

The stopwords set to upsert.

- `value` (one of several types, required)
  - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
  - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
  - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
  - `nl_query` (boolean) — Whether to use natural language processing to parse the query.
  - `nl_model_id` (string) — The ID of the natural language model to use.
  - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
  - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
  - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
  - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
  - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
  - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
  - `filter_by` (string) — Filter conditions for refining your open api validator search results. Separate multiple conditions with &&.
  - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
  - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
  - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
  - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
  - `max_facet_values` (integer) — Maximum number of facet values to be returned.
  - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
  - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
  - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
  - `page` (integer) — Results from this specific page number would be fetched.
  - `per_page` (integer) — Number of results to fetch per page. Default: 10
  - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
  - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
  - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
  - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
  - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
  - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
  - `include_fields` (string) — List of fields from the document to include in the search result
  - `exclude_fields` (string) — List of fields from the document to exclude in the search result
  - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
  - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
  - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
  - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
  - `enable_highlight_v1` (boolean) — Flag for enabling/disabling the deprecated, old highlight structure in the response. Default: true. Default: `true`.
  - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
  - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
  - `synonym_sets` (string) — List of synonym set names to associate with this search query
  - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
  - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
  - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
  - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
  - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
  - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
  - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
  - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
  - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
  - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
  - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
  - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
  - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
  - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
  - `split_join_tokens` (string) — Treat space as typo: search for q=basket ball if q=basketball is not found or vice-versa. Splitting/joining of tokens will only be attempted if the original query produces no results. To always trigger this behavior, set value to `always``. To disable, set value to `off`. Default is `fallback`.
  - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same
  - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
  - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
  - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
  - `max_candidates` (integer) — Control the number of words that Typesense considers for typo and prefix searching.
  - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
  - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
  - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
  - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
  - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
  - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
  - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
  - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
  - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
  - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
  - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
  - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
  - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
  - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
  - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
  - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
  - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
  - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
  - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
  - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
  - `conversation` (boolean) — Enable conversational search.
  - `conversation_model_id` (string) — The Id of Conversation Model to be used.
  - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
  - `union` (boolean) — When true, merges the search results from each search query into a single ordered set of hits. Default: `false`.
  - `searches` (array of object, required)
    - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
    - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
    - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
    - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
    - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
    - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
    - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
    - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
    - `filter_by` (string) — Filter conditions for refining youropen api validator search results. Separate multiple conditions with &&.
    - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
    - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
    - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
    - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
    - `max_facet_values` (integer) — Maximum number of facet values to be returned.
    - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
    - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
    - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
    - `page` (integer) — Results from this specific page number would be fetched.
    - `per_page` (integer) — Number of results to fetch per page. Default: 10
    - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
    - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
    - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
    - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
    - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
    - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
    - `include_fields` (string) — List of fields from the document to include in the search result
    - `exclude_fields` (string) — List of fields from the document to exclude in the search result
    - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
    - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
    - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
    - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
    - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
    - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
    - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
    - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
    - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
    - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
    - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
    - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
    - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
    - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
    - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
    - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
    - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
    - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
    - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
    - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
    - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same. Default: `false`.
    - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
    - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
    - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
    - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
    - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
    - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
    - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
    - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
    - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
    - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
    - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
    - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
    - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
    - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
    - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
    - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
    - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
    - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
    - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
    - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
    - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
    - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
    - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
    - `conversation` (boolean) — Enable conversational search.
    - `conversation_model_id` (string) — The Id of Conversation Model to be used.
    - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
    - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
    - `collection` (string) — The collection to search in.
    - `x-typesense-api-key` (string) — A separate search API key for each search within a multi_search request

**Responses**

- **200** — Preset successfully upserted.
  Body (`application/json`, object):
  - `value` (one of several types, required)
    - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
    - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
    - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
    - `nl_query` (boolean) — Whether to use natural language processing to parse the query.
    - `nl_model_id` (string) — The ID of the natural language model to use.
    - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
    - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
    - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
    - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
    - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
    - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
    - `filter_by` (string) — Filter conditions for refining your open api validator search results. Separate multiple conditions with &&.
    - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
    - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
    - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
    - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
    - `max_facet_values` (integer) — Maximum number of facet values to be returned.
    - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
    - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
    - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
    - `page` (integer) — Results from this specific page number would be fetched.
    - `per_page` (integer) — Number of results to fetch per page. Default: 10
    - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
    - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
    - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
    - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
    - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
    - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
    - `include_fields` (string) — List of fields from the document to include in the search result
    - `exclude_fields` (string) — List of fields from the document to exclude in the search result
    - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
    - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
    - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
    - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
    - `enable_highlight_v1` (boolean) — Flag for enabling/disabling the deprecated, old highlight structure in the response. Default: true. Default: `true`.
    - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
    - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
    - `synonym_sets` (string) — List of synonym set names to associate with this search query
    - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
    - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
    - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
    - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
    - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
    - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
    - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
    - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
    - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
    - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
    - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
    - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
    - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
    - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
    - `split_join_tokens` (string) — Treat space as typo: search for q=basket ball if q=basketball is not found or vice-versa. Splitting/joining of tokens will only be attempted if the original query produces no results. To always trigger this behavior, set value to `always``. To disable, set value to `off`. Default is `fallback`.
    - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same
    - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
    - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
    - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
    - `max_candidates` (integer) — Control the number of words that Typesense considers for typo and prefix searching.
    - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
    - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
    - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
    - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
    - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
    - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
    - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
    - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
    - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
    - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
    - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
    - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
    - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
    - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
    - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
    - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
    - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
    - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
    - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
    - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
    - `conversation` (boolean) — Enable conversational search.
    - `conversation_model_id` (string) — The Id of Conversation Model to be used.
    - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
    - `union` (boolean) — When true, merges the search results from each search query into a single ordered set of hits. Default: `false`.
    - `searches` (array of object, required)
      - `q` (string) — The query text to search for in the collection. Use * as the search string to return all documents. This is typically useful when used in conjunction with filter_by.
      - `query_by` (string) — A list of `string` fields that should be queried against. Multiple fields are separated with a comma.
      - `query_by_weights` (string) — The relative weight to give each `query_by` field when ranking results. This can be used to boost fields in priority, when looking for matches. Multiple fields are separated with a comma.
      - `text_match_type` (string) — In a multi-field matching context, this parameter determines how the representative text match score of a record is calculated. Possible values are max_score (default) or max_weight.
      - `prefix` (string) — Boolean field to indicate that the last word in the query should be treated as a prefix, and not as a whole word. This is used for building autocomplete and instant search interfaces. Defaults to true.
      - `infix` (string) — If infix index is enabled for this field, infix searching can be done on a per-field basis by sending a comma separated string parameter called infix to the search query. This parameter can have 3 values; `off` infix search is disabled, which is default `always` infix search is performed along with regular search `fallback` infix search is performed if regular search does not produce results
      - `max_extra_prefix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
      - `max_extra_suffix` (integer) — There are also 2 parameters that allow you to control the extent of infix searching max_extra_prefix and max_extra_suffix which specify the maximum number of symbols before or after the query that can be present in the token. For example query "K2100" has 2 extra symbols in "6PK2100". By default, any number of prefixes/suffixes can be present for a match.
      - `filter_by` (string) — Filter conditions for refining youropen api validator search results. Separate multiple conditions with &&.
      - `enable_lazy_filter` (boolean) — Applies the filtering operation incrementally / lazily. Set this to true when you are potentially filtering on large values but the tokens in the query are expected to match very few documents. Default: false
      - `max_filter_by_candidates` (integer) — Controls the number of similar words that Typesense considers during fuzzy search on filter_by values. Useful for controlling prefix matches like company_name:Acm*.
      - `sort_by` (string) — A list of numerical fields and their corresponding sort orders that will be used for ordering your results. Up to 3 sort fields can be specified. The text similarity score is exposed as a special `_text_match` field that you can use in the list of sorting fields. If no `sort_by` parameter is specified, results are sorted by `_text_match:desc,default_sorting_field:desc`
      - `facet_by` (string) — A list of fields that will be used for faceting your results on. Separate multiple fields with a comma.
      - `max_facet_values` (integer) — Maximum number of facet values to be returned.
      - `facet_query` (string) — Facet values that are returned can now be filtered via this parameter. The matching facet text is also highlighted. For example, when faceting by `category`, you can set `facet_query=category:shoe` to return only facet values that contain the prefix "shoe".
      - `facet_query_num_typos` (integer) — Controls the fuzziness of the facet query filter. Default: 2.
      - `num_typos` (string) — The number of typographical errors (1 or 2) that would be tolerated. Default: 2
      - `page` (integer) — Results from this specific page number would be fetched.
      - `per_page` (integer) — Number of results to fetch per page. Default: 10
      - `limit` (integer) — Number of hits to fetch. Can be used as an alternative to the per_page parameter. Default: 10.
      - `offset` (integer) — Identifies the starting point to return hits from a result set. Can be used as an alternative to the page parameter.
      - `group_by` (string) — You can aggregate search results into groups or buckets by specify one or more `group_by` fields. Separate multiple fields with a comma. To group on a particular field, it must be a faceted field.
      - `group_limit` (integer) — Maximum number of hits to be returned for every group. If the `group_limit` is set as `K` then only the top K hits in each group are returned in the response. Default: 3
      - `group_missing_values` (boolean) — Setting this parameter to true will place all documents that have a null value in the group_by field, into a single group. Setting this parameter to false, will cause each document with a null value in the group_by field to not be grouped with other documents. Default: true
      - `group_max_candidates` (integer) — Overrides the behavior of group_by queries where found value is an approximation. When group_max_candidates is passed, found will be accurate up until its value.
      - `include_fields` (string) — List of fields from the document to include in the search result
      - `exclude_fields` (string) — List of fields from the document to exclude in the search result
      - `highlight_full_fields` (string) — List of fields which should be highlighted fully without snippeting
      - `highlight_affix_num_tokens` (integer) — The number of tokens that should surround the highlighted text on each side. Default: 4
      - `highlight_start_tag` (string) — The start tag used for the highlighted snippets. Default: `<mark>`
      - `highlight_end_tag` (string) — The end tag used for the highlighted snippets. Default: `</mark>`
      - `snippet_threshold` (integer) — Field values under this length will be fully highlighted, instead of showing a snippet of relevant portion. Default: 30
      - `drop_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to drop the tokens in the query until enough results are found. Tokens that have the least individual hits are dropped first. Set to 0 to disable. Default: 10
      - `drop_tokens_mode` (string) — Dictates the direction in which the words in the query must be dropped when the original words in the query do not appear in any document. Values: right_to_left (default), left_to_right, both_sides:3 A note on both_sides:3 - for queries up to 3 tokens (words) in length, this mode will drop tokens from both sides and exhaustively rank all matching results. If query length is greater than 3 words, Typesense will just fallback to default behavior of right_to_left. Allowed values: `right_to_left`, `left_to_right`, `both_sides:3`.
      - `typo_tokens_threshold` (integer) — If the number of results found for a specific query is less than this number, Typesense will attempt to look for tokens with more typos until enough results are found. Default: 100
      - `enable_typos_for_alpha_numerical_tokens` (boolean) — Set this parameter to false to disable typos on alphanumerical query tokens. Default: true.
      - `filter_curated_hits` (boolean) — Whether the filter_by condition of the search query should be applicable to curated results (curation definitions, pinned hits, hidden hits, etc.). Default: false
      - `enable_synonyms` (boolean) — If you have some synonyms defined but want to disable all of them for a particular search query, set enable_synonyms to false. Default: true
      - `enable_analytics` (boolean) — Flag for enabling/disabling analytics aggregation for specific search queries (for e.g. those originating from a test script). Default: `true`.
      - `synonym_prefix` (boolean) — Allow synonym resolution on word prefixes in the query. Default: false
      - `demote_synonym_match` (boolean) — When set to true, search results that matched via synonyms will be demoted in ranking, appearing below results that have a direct match. Default: false
      - `synonym_num_typos` (integer) — Allow synonym resolution on typo-corrected words in the query. Default: 0
      - `pinned_hits` (string) — A list of records to unconditionally include in the search results at specific positions. An example use case would be to feature or promote certain items on the top of search results. A list of `record_id:hit_position`. Eg: to include a record with ID 123 at Position 1 and another record with ID 456 at Position 5, you'd specify `123:1,456:5`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
      - `hidden_hits` (string) — A list of records to unconditionally hide from search results. A list of `record_id`s to hide. Eg: to hide records with IDs 123 and 456, you'd specify `123,456`. You could also use the Curation feature to override search results based on rules. Curations are applied first, followed by `pinned_hits` and finally `hidden_hits`.
      - `curation_tags` (string) — Comma separated list of tags to trigger the curations rules that match the tags.
      - `highlight_fields` (string) — A list of custom fields that must be highlighted even if you don't query for them
      - `rerank_hybrid_matches` (boolean) — When true, computes both text match and vector distance scores for all matches in hybrid search. Documents found only through keyword search will get a vector distance score, and documents found only through vector search will get a text match score. Default: `false`.
      - `pre_segmented_query` (boolean) — You can index content from any logographic language into Typesense if you are able to segment / split the text into space-separated words yourself before indexing and querying. Set this parameter to true to do the same. Default: `false`.
      - `preset` (string) — Search using a bunch of search parameters by setting this parameter to the name of the existing Preset.
      - `enable_curations` (boolean) — If you have some curation sets defined but want to disable all of them during query time, you can do that by setting this parameter to false. Default: `false`.
      - `prioritize_exact_match` (boolean) — Set this parameter to true to ensure that an exact match is ranked above the others. Default: `true`.
      - `prioritize_token_position` (boolean) — Make Typesense prioritize documents where the query words appear earlier in the text. Default: `false`.
      - `prioritize_num_matching_fields` (boolean) — Make Typesense prioritize documents where the query words appear in more number of fields. Default: `true`.
      - `enable_typos_for_numerical_tokens` (boolean) — Make Typesense disable typos for numerical tokens. Default: `true`.
      - `exhaustive_search` (boolean) — Setting this to true will make Typesense consider all prefixes and typo corrections of the words in the query without stopping early when enough results are found (drop_tokens_threshold and typo_tokens_threshold configurations are ignored).
      - `search_cutoff_ms` (integer) — Typesense will attempt to return results early if the cutoff time has elapsed. This is not a strict guarantee and facet computation is not bound by this parameter.
      - `limit_hits` (integer) — Maximum number of hits that can be fetched from the collection. page * per_page should be less than this number for the search request to return results.
      - `use_cache` (boolean) — Enable server side caching of search query results. By default, caching is disabled.
      - `cache_ttl` (integer) — The duration (in seconds) that determines how long the search query is cached. This value can be set on a per-query basis. Default: 60.
      - `min_len_1typo` (integer) — Minimum word length for 1-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
      - `min_len_2typo` (integer) — Minimum word length for 2-typo correction to be applied. The value of num_typos is still treated as the maximum allowed typos.
      - `vector_query` (string) — Vector query expression for fetching documents "closest" to a given query/document vector.
      - `remote_embedding_timeout_ms` (integer) — Timeout (in milliseconds) for fetching remote embeddings.
      - `remote_embedding_num_tries` (integer) — Number of times to retry fetching remote embeddings.
      - `facet_strategy` (string) — Choose the underlying faceting strategy used. Comma separated string of allows values: exhaustive, top_values or automatic (default).
      - `stopwords` (string) — Name of the stopwords set to apply for this search, the keywords present in the set will be removed from the search query.
      - `facet_return_parent` (string) — Comma separated string of nested facet fields whose parent object should be returned in facet response.
      - `facet_sample_percent` (integer) — Percentage of hits that will be used to estimate facet counts. Default: 100.
      - `facet_sample_threshold` (integer) — Minimum number of hits above which the facet counts are sampled. Default: 0.
      - `facet_sample_slope` (number) — Controls how steeply facet_sample_percent falls as the collection grows. facet_sample_threshold should be non-zero for facet_sample_slope to be effective. Default: 0.
      - `voice_query` (string) — The base64 encoded audio file in 16 khz 16-bit WAV format.
      - `conversation` (boolean) — Enable conversational search.
      - `conversation_model_id` (string) — The Id of Conversation Model to be used.
      - `conversation_id` (string) — The Id of a previous conversation to continue, this tells Typesense to include prior context when communicating with the LLM.
      - `validate_field_names` (boolean) — Controls whether Typesense should validate if the fields exist in the schema. When set to false, Typesense will not throw an error if a field is missing. This is useful for programmatic grouping where not all fields may exist.
      - `collection` (string) — The collection to search in.
      - `x-typesense-api-key` (string) — A separate search API key for each search within a multi_search request
  - `name` (string, required)
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /presets/{presetId}

**Delete a preset.**

Permanently deletes a preset, given it's name.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `presetId` | path | string | Yes | The ID of the preset to delete. |

**Responses**

- **200** — Preset deleted.
  Body (`application/json`, object):
  - `name` (string, required)
- **404** — Preset not found.
  Body (`application/json`, object):
  - `message` (string, required)

## stemming

Manage stemming dictionaries

### GET /stemming/dictionaries

**List all stemming dictionaries**

Retrieve a list of all available stemming dictionaries.

**Responses**

- **200** — List of all dictionaries
  Body (`application/json`, object):
  - `dictionaries` (array of string)

### GET /stemming/dictionaries/{dictionaryId}

**Retrieve a stemming dictionary**

Fetch details of a specific stemming dictionary.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `dictionaryId` | path | string | Yes | The ID of the dictionary to retrieve |

**Responses**

- **200** — Stemming dictionary details
  Body (`application/json`, object):
  - `id` (string, required) — Unique identifier for the dictionary
  - `words` (array of object, required) — List of word mappings in the dictionary
    - `word` (string, required) — The word form to be stemmed
    - `root` (string, required) — The root form of the word
- **404** — Dictionary not found
  Body (`application/json`, object):
  - `message` (string, required)

### POST /stemming/dictionaries/import

**Import a stemming dictionary**

Upload a JSONL file containing word mappings to create or update a stemming dictionary.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | query | string | Yes | The ID to assign to the dictionary |

**Request body** (`application/json`, required)

The JSONL file containing word mappings

- Body type: string

Example:

```json
"{\"word\": \"people\", \"root\": \"person\"}\n{\"word\": \"children\", \"root\": \"child\"}\n"
```

**Responses**

- **200** — Dictionary successfully imported
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

## nl_search_models

Manage NL search models

### GET /nl_search_models

**List all NL search models**

Retrieve all NL search models.

**Responses**

- **200** — List of all NL search models
  Body (`application/json`, array of object):
  - `model_name` (string) — Name of the NL model to use
  - `api_key` (string) — API key for the NL model service
  - `api_url` (string) — Custom API URL for the NL model service
  - `max_bytes` (integer) — Maximum number of bytes to process
  - `temperature` (number) — Temperature parameter for the NL model
  - `system_prompt` (string) — System prompt for the NL model
  - `top_p` (number) — Top-p parameter for the NL model (Google-specific)
  - `top_k` (integer) — Top-k parameter for the NL model (Google-specific)
  - `stop_sequences` (array of string) — Stop sequences for the NL model (Google-specific)
  - `api_version` (string) — API version for the NL model service
  - `project_id` (string) — Project ID for GCP Vertex AI
  - `access_token` (string) — Access token for GCP Vertex AI
  - `refresh_token` (string) — Refresh token for GCP Vertex AI
  - `client_id` (string) — Client ID for GCP Vertex AI
  - `client_secret` (string) — Client secret for GCP Vertex AI
  - `region` (string) — Region for GCP Vertex AI
  - `max_output_tokens` (integer) — Maximum output tokens for GCP Vertex AI
  - `account_id` (string) — Account ID for Cloudflare-specific models
  - `id` (string, required) — ID of the NL search model

### POST /nl_search_models

**Create a NL search model**

Create a new NL search model.

**Request body** (`application/json`, required)

The NL search model to be created

- `model_name` (string) — Name of the NL model to use
- `api_key` (string) — API key for the NL model service
- `api_url` (string) — Custom API URL for the NL model service
- `max_bytes` (integer) — Maximum number of bytes to process
- `temperature` (number) — Temperature parameter for the NL model
- `system_prompt` (string) — System prompt for the NL model
- `top_p` (number) — Top-p parameter for the NL model (Google-specific)
- `top_k` (integer) — Top-k parameter for the NL model (Google-specific)
- `stop_sequences` (array of string) — Stop sequences for the NL model (Google-specific)
- `api_version` (string) — API version for the NL model service
- `project_id` (string) — Project ID for GCP Vertex AI
- `access_token` (string) — Access token for GCP Vertex AI
- `refresh_token` (string) — Refresh token for GCP Vertex AI
- `client_id` (string) — Client ID for GCP Vertex AI
- `client_secret` (string) — Client secret for GCP Vertex AI
- `region` (string) — Region for GCP Vertex AI
- `max_output_tokens` (integer) — Maximum output tokens for GCP Vertex AI
- `account_id` (string) — Account ID for Cloudflare-specific models
- `id` (string) — Optional ID for the NL search model

**Responses**

- **201** — NL search model successfully created
  Body (`application/json`, object):
  - `model_name` (string) — Name of the NL model to use
  - `api_key` (string) — API key for the NL model service
  - `api_url` (string) — Custom API URL for the NL model service
  - `max_bytes` (integer) — Maximum number of bytes to process
  - `temperature` (number) — Temperature parameter for the NL model
  - `system_prompt` (string) — System prompt for the NL model
  - `top_p` (number) — Top-p parameter for the NL model (Google-specific)
  - `top_k` (integer) — Top-k parameter for the NL model (Google-specific)
  - `stop_sequences` (array of string) — Stop sequences for the NL model (Google-specific)
  - `api_version` (string) — API version for the NL model service
  - `project_id` (string) — Project ID for GCP Vertex AI
  - `access_token` (string) — Access token for GCP Vertex AI
  - `refresh_token` (string) — Refresh token for GCP Vertex AI
  - `client_id` (string) — Client ID for GCP Vertex AI
  - `client_secret` (string) — Client secret for GCP Vertex AI
  - `region` (string) — Region for GCP Vertex AI
  - `max_output_tokens` (integer) — Maximum output tokens for GCP Vertex AI
  - `account_id` (string) — Account ID for Cloudflare-specific models
  - `id` (string, required) — ID of the NL search model
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)

### GET /nl_search_models/{modelId}

**Retrieve a NL search model**

Retrieve a specific NL search model by its ID.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `modelId` | path | string | Yes | The ID of the NL search model to retrieve |

**Responses**

- **200** — NL search model fetched
  Body (`application/json`, object):
  - `model_name` (string) — Name of the NL model to use
  - `api_key` (string) — API key for the NL model service
  - `api_url` (string) — Custom API URL for the NL model service
  - `max_bytes` (integer) — Maximum number of bytes to process
  - `temperature` (number) — Temperature parameter for the NL model
  - `system_prompt` (string) — System prompt for the NL model
  - `top_p` (number) — Top-p parameter for the NL model (Google-specific)
  - `top_k` (integer) — Top-k parameter for the NL model (Google-specific)
  - `stop_sequences` (array of string) — Stop sequences for the NL model (Google-specific)
  - `api_version` (string) — API version for the NL model service
  - `project_id` (string) — Project ID for GCP Vertex AI
  - `access_token` (string) — Access token for GCP Vertex AI
  - `refresh_token` (string) — Refresh token for GCP Vertex AI
  - `client_id` (string) — Client ID for GCP Vertex AI
  - `client_secret` (string) — Client secret for GCP Vertex AI
  - `region` (string) — Region for GCP Vertex AI
  - `max_output_tokens` (integer) — Maximum output tokens for GCP Vertex AI
  - `account_id` (string) — Account ID for Cloudflare-specific models
  - `id` (string, required) — ID of the NL search model
- **404** — NL search model not found
  Body (`application/json`, object):
  - `message` (string, required)

### PUT /nl_search_models/{modelId}

**Update a NL search model**

Update an existing NL search model.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `modelId` | path | string | Yes | The ID of the NL search model to update |

**Request body** (`application/json`, required)

The NL search model fields to update

- `model_name` (string) — Name of the NL model to use
- `api_key` (string) — API key for the NL model service
- `api_url` (string) — Custom API URL for the NL model service
- `max_bytes` (integer) — Maximum number of bytes to process
- `temperature` (number) — Temperature parameter for the NL model
- `system_prompt` (string) — System prompt for the NL model
- `top_p` (number) — Top-p parameter for the NL model (Google-specific)
- `top_k` (integer) — Top-k parameter for the NL model (Google-specific)
- `stop_sequences` (array of string) — Stop sequences for the NL model (Google-specific)
- `api_version` (string) — API version for the NL model service
- `project_id` (string) — Project ID for GCP Vertex AI
- `access_token` (string) — Access token for GCP Vertex AI
- `refresh_token` (string) — Refresh token for GCP Vertex AI
- `client_id` (string) — Client ID for GCP Vertex AI
- `client_secret` (string) — Client secret for GCP Vertex AI
- `region` (string) — Region for GCP Vertex AI
- `max_output_tokens` (integer) — Maximum output tokens for GCP Vertex AI
- `account_id` (string) — Account ID for Cloudflare-specific models
- `id` (string) — Optional ID for the NL search model

**Responses**

- **200** — NL search model successfully updated
  Body (`application/json`, object):
  - `model_name` (string) — Name of the NL model to use
  - `api_key` (string) — API key for the NL model service
  - `api_url` (string) — Custom API URL for the NL model service
  - `max_bytes` (integer) — Maximum number of bytes to process
  - `temperature` (number) — Temperature parameter for the NL model
  - `system_prompt` (string) — System prompt for the NL model
  - `top_p` (number) — Top-p parameter for the NL model (Google-specific)
  - `top_k` (integer) — Top-k parameter for the NL model (Google-specific)
  - `stop_sequences` (array of string) — Stop sequences for the NL model (Google-specific)
  - `api_version` (string) — API version for the NL model service
  - `project_id` (string) — Project ID for GCP Vertex AI
  - `access_token` (string) — Access token for GCP Vertex AI
  - `refresh_token` (string) — Refresh token for GCP Vertex AI
  - `client_id` (string) — Client ID for GCP Vertex AI
  - `client_secret` (string) — Client secret for GCP Vertex AI
  - `region` (string) — Region for GCP Vertex AI
  - `max_output_tokens` (integer) — Maximum output tokens for GCP Vertex AI
  - `account_id` (string) — Account ID for Cloudflare-specific models
  - `id` (string, required) — ID of the NL search model
- **400** — Bad request, see error message for details
  Body (`application/json`, object):
  - `message` (string, required)
- **404** — NL search model not found
  Body (`application/json`, object):
  - `message` (string, required)

### DELETE /nl_search_models/{modelId}

**Delete a NL search model**

Delete a specific NL search model by its ID.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `modelId` | path | string | Yes | The ID of the NL search model to delete |

**Responses**

- **200** — NL search model successfully deleted
  Body (`application/json`, object):
  - `id` (string, required) — ID of the deleted NL search model
- **404** — NL search model not found
  Body (`application/json`, object):
  - `message` (string, required)
