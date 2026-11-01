# Qdrant API — API Reference

API description for Qdrant vector search engine.

This document describes CRUD and search operations on collections of points (vectors with payload).

Qdrant supports any combinations of `should`, `min_should`, `must` and `must_not` conditions, which makes it possible to use in applications when object could not be described solely by vector. It could be location features, availability flags, and other custom properties businesses should take into account.
## Examples
This examples cover the most basic use-cases - collection creation and basic vector search.
### Create collection
First - let's create a collection with dot-production metric.
```
curl -X PUT 'http://localhost:6333/collections/test_collection' \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "vectors": {
      "size": 4,
      "distance": "Dot"
    }
  }'

```
Expected response:
```
{
    "result": true,
    "status": "ok",
    "time": 0.031095451
}
```
We can ensure that collection was created:
```
curl 'http://localhost:6333/collections/test_collection'
```
Expected response:
```
{
  "result": {
    "status": "green",
    "segments_count": 5,
    "disk_data_size": 0,
    "ram_data_size": 0,
    "config": {
      "params": {
        "vectors": {
          "size": 4,
          "distance": "Dot"
        }
      },
      "hnsw_config": {
        "m": 16,
        "ef_construct": 100,
        "full_scan_threshold": 10000
      },
      "optimizer_config": {
        "deleted_threshold": 0.2,
        "vacuum_min_vector_number": 1000,
        "default_segment_number": 2,
        "max_segment_size": null,
        "memmap_threshold": null,
        "indexing_threshold": 20000,
        "flush_interval_sec": 5,
        "max_optimization_threads": null
      },
      "wal_config": {
        "wal_capacity_mb": 32,
        "wal_segments_ahead": 0
      }
    }
  },
  "status": "ok",
  "time": 2.1199e-05
}
```

### Add points
Let's now add vectors with some payload:
```
curl -L -X PUT 'http://localhost:6333/collections/test_collection/points?wait=true' \ -H 'Content-Type: application/json' \ --data-raw '{
  "points": [
    {"id": 1, "vector": [0.05, 0.61, 0.76, 0.74], "payload": {"city": "Berlin"}},
    {"id": 2, "vector": [0.19, 0.81, 0.75, 0.11], "payload": {"city": ["Berlin", "London"] }},
    {"id": 3, "vector": [0.36, 0.55, 0.47, 0.94], "payload": {"city": ["Berlin", "Moscow"] }},
    {"id": 4, "vector": [0.18, 0.01, 0.85, 0.80], "payload": {"city": ["London", "Moscow"] }},
    {"id": 5, "vector": [0.24, 0.18, 0.22, 0.44], "payload": {"count": [0]}},
    {"id": 6, "vector": [0.35, 0.08, 0.11, 0.44]}
  ]
}'
```
Expected response:
```
{
    "result": {
        "operation_id": 0,
        "status": "completed"
    },
    "status": "ok",
    "time": 0.000206061
}
```
### Search with filtering
Let's start with a basic request:
```
curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \ -H 'Content-Type: application/json' \ --data-raw '{
    "vector": [0.2,0.1,0.9,0.7],
    "top": 3
}'
```
Expected response:
```
{
    "result": [
        { "id": 4, "score": 1.362, "payload": null, "version": 0 },
        { "id": 1, "score": 1.273, "payload": null, "version": 0 },
        { "id": 3, "score": 1.208, "payload": null, "version": 0 }
    ],
    "status": "ok",
    "time": 0.000055785
}
```
But result is different if we add a filter:
```
curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \ -H 'Content-Type: application/json' \ --data-raw '{
    "filter": {
        "should": [
            {
                "key": "city",
                "match": {
                    "value": "London"
                }
            }
        ]
    },
    "vector": [0.2, 0.1, 0.9, 0.7],
    "top": 3
}'
```
Expected response:
```
{
    "result": [
        { "id": 4, "score": 1.362, "payload": null, "version": 0 },
        { "id": 2, "score": 0.871, "payload": null, "version": 0 }
    ],
    "status": "ok",
    "time": 0.000093972
}
```

**Version:** master  
**Base URL:** `http://localhost:6343`

## Authentication

- **api-key**: API key sent in header parameter `api-key`.
  Authorization key, either read-write or read-only
- **bearerAuth**: HTTP bearer authentication.

## Distributed

Service distributed setup.

### GET /collections/{collection_name}/shards

**List shard keys**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to list shard keys for |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `shard_keys` (array of object) — The existing shard keys. Only available when sharding method is `custom`. May be null.
      - `key` (one of several types, required)

### PUT /collections/{collection_name}/shards

**Create shard key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to create shards for |
| `timeout` | query | integer | No | Wait for operation commit timeout in seconds. If timeout is reached - request will return with service error. Minimum: 1. |

**Request body** (`application/json`)

Shard key configuration

- `shard_key` (one of several types, required)
- `shards_number` (integer (uint32)) — How many shards to create for this key If not specified, will use the default value from config. Minimum: 1. May be null.
- `replication_factor` (integer (uint32)) — How many replicas to create for each shard If not specified, will use the default value from config. Minimum: 1. May be null.
- `placement` (array of integer (uint64)) — Placement of shards for this key List of peer ids, that can be used to place shards for this key If not specified, will be randomly placed among all peers. May be null.
- `initial_state` (one of several types) — Initial state of the shards for this key If not specified, will be `Initializing` first and then `Active` Warning: do not change this unless you know what you are doing

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

### POST /collections/{collection_name}/shards/delete

**Delete shard key**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to create shards for |
| `timeout` | query | integer | No | Wait for operation commit timeout in seconds. If timeout is reached - request will return with service error. Minimum: 1. |

**Request body** (`application/json`)

Select shard key to delete

- `shard_key` (one of several types, required)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

### GET /cluster

**Get cluster status info**

Get information about the current state and composition of the cluster

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (one of several types) — Information about current cluster status and structure
    - `status` (string, required) — Allowed values: `disabled`.
    - `status` (string, required) — Allowed values: `enabled`.
    - `peer_id` (integer (uint64), required) — ID of this peer. Minimum: 0.
    - `peers` (object, required) — Peers composition of the cluster with main information
    - `raft_info` (object, required) — Summary information about the current raft state
      - `term` (integer (uint64), required) — Raft divides time into terms of arbitrary length, each beginning with an election. If a candidate wins the election, it remains the leader for the rest of the term. The term number increases monotonically. Each server stores the current term number which is also exchanged in every communication. Minimum: 0.
      - `commit` (integer (uint64), required) — The index of the latest committed (finalized) operation that this peer is aware of. Minimum: 0.
      - `pending_operations` (integer (uint), required) — Number of consensus operations pending to be applied on this peer. Minimum: 0.
      - `leader` (integer (uint64)) — Leader of the current term. Minimum: 0. May be null.
      - `role` (one of several types) — Role of this peer in the current term
      - `is_voter` (boolean, required) — Is this peer a voter or a learner
    - `consensus_thread_status` (one of several types, required) — Information about current consensus thread status
      - `consensus_thread_status` (string, required) — Allowed values: `working`.
      - `last_update` (string (date-time), required)
      - `consensus_thread_status` (string, required) — Allowed values: `stopped`.
      - `consensus_thread_status` (string, required) — Allowed values: `stopped_with_err`.
      - `err` (string, required)
    - `message_send_failures` (object, required) — Consequent failures of message send operations in consensus by peer address. On the first success to send to that peer - entry is removed from this hashmap.

### GET /cluster/telemetry

**Collect cluster telemetry data**

Get telemetry data, from the point of view of the cluster. This includes peers info, collections info, shard transfers, and resharding status

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `details_level` | query | integer | No | The level of detail to include in the response |
| `timeout` | query | integer | No | Timeout for this request. Default: `60`. Minimum: 1. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `collections` (object, required)
    - `cluster` (one of several types)
      - `enabled` (boolean, required)
      - `number_of_peers` (integer (uint64)) — Minimum: 0. May be null.
      - `peers` (object, required)

### POST /cluster/recover

**Tries to recover current peer Raft state.**

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

### DELETE /cluster/peer/{peer_id}

**Remove peer from the cluster**

Tries to remove peer from the cluster. Will return an error if peer has shards on it.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `peer_id` | path | integer | Yes | Id of the peer |
| `timeout` | query | integer | No | Wait for operation commit timeout in seconds. If timeout is reached - request will return with service error. Minimum: 1. |
| `force` | query | boolean | No | If true - removes peer even if it has shards/replicas on it. Default: `false`. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

### GET /collections/{collection_name}/cluster

**Collection cluster info**

Get cluster information for a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to retrieve the cluster info for |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object) — Current clustering distribution for the collection
    - `peer_id` (integer (uint64), required) — ID of this peer. Minimum: 0.
    - `shard_count` (integer (uint), required) — Total number of shards. Minimum: 0.
    - `local_shards` (array of object, required) — Local shards
      - `shard_id` (integer (uint32), required) — Local shard id. Minimum: 0.
      - `shard_key` (one of several types) — User-defined sharding key
      - `points_count` (integer (uint), required) — Number of points in the shard. Minimum: 0.
      - `state` (string, required) — State of the single shard within a replica set. Allowed values: `Active`, `Dead`, `Partial`, `Initializing`, `Listener`, `PartialSnapshot`, `Recovery`, `Resharding`, `ReshardingScaleDown`, `ActiveRead`, `ManualRecovery`.
    - `remote_shards` (array of object, required) — Remote shards
      - `shard_id` (integer (uint32), required) — Remote shard id. Minimum: 0.
      - `shard_key` (one of several types) — User-defined sharding key
      - `peer_id` (integer (uint64), required) — Remote peer id. Minimum: 0.
      - `state` (string, required) — State of the single shard within a replica set. Allowed values: `Active`, `Dead`, `Partial`, `Initializing`, `Listener`, `PartialSnapshot`, `Recovery`, `Resharding`, `ReshardingScaleDown`, `ActiveRead`, `ManualRecovery`.
    - `shard_transfers` (array of object, required) — Shard transfers
      - `shard_id` (integer (uint32), required) — Minimum: 0.
      - `to_shard_id` (integer (uint32)) — Target shard ID if different than source shard ID Used exclusively with `ReshardingStreamRecords` transfer method. Minimum: 0. May be null.
      - `from` (integer (uint64), required) — Source peer id. Minimum: 0.
      - `to` (integer (uint64), required) — Destination peer id. Minimum: 0.
      - `sync` (boolean, required) — If `true` transfer is a synchronization of a replicas If `false` transfer is a moving of a shard from one peer to another
      - `method` (one of several types)
      - `comment` (string) — A human-readable report of the transfer progress. Available only on the source peer, and on the target peer during snapshot recovery. May be null.
    - `resharding_operations` (array of object) — Resharding operations. May be null.
      - `direction` (string, required) — Resharding direction, scale up or down in number of shards - `up` - Scale up, add a new shard - `down` - Scale down, remove a shard. Allowed values: `up`, `down`.
      - `shard_id` (integer (uint32), required) — Minimum: 0.
      - `peer_id` (integer (uint64), required) — Minimum: 0.
      - `shard_key` (one of several types)

### POST /collections/{collection_name}/cluster

**Update collection cluster setup**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection on which to to apply the cluster update operation |
| `timeout` | query | integer | No | Wait for operation commit timeout in seconds. If timeout is reached - request will return with service error. Minimum: 1. |

**Request body** (`application/json`)

Collection cluster update operations

- `move_shard` (object, required)
  - `shard_id` (integer (uint32), required) — Minimum: 0.
  - `to_peer_id` (integer (uint64), required) — Minimum: 0.
  - `from_peer_id` (integer (uint64), required) — Minimum: 0.
  - `method` (one of several types) — Method for transferring the shard from one node to another
- `replicate_shard` (object, required)
  - `shard_id` (integer (uint32), required) — Minimum: 0.
  - `to_peer_id` (integer (uint64), required) — Minimum: 0.
  - `from_peer_id` (integer (uint64), required) — Minimum: 0.
  - `method` (one of several types) — Method for transferring the shard from one node to another
- `abort_transfer` (object, required)
  - `shard_id` (integer (uint32), required) — Minimum: 0.
  - `to_peer_id` (integer (uint64), required) — Minimum: 0.
  - `from_peer_id` (integer (uint64), required) — Minimum: 0.
- `drop_replica` (object, required)
  - `shard_id` (integer (uint32), required) — Minimum: 0.
  - `peer_id` (integer (uint64), required) — Minimum: 0.
- `create_sharding_key` (object, required)
  - `shard_key` (one of several types, required)
  - `shards_number` (integer (uint32)) — How many shards to create for this key If not specified, will use the default value from config. Minimum: 1. May be null.
  - `replication_factor` (integer (uint32)) — How many replicas to create for each shard If not specified, will use the default value from config. Minimum: 1. May be null.
  - `placement` (array of integer (uint64)) — Placement of shards for this key List of peer ids, that can be used to place shards for this key If not specified, will be randomly placed among all peers. May be null.
  - `initial_state` (one of several types) — Initial state of the shards for this key If not specified, will be `Initializing` first and then `Active` Warning: do not change this unless you know what you are doing
- `drop_sharding_key` (object, required)
  - `shard_key` (one of several types, required)
- `restart_transfer` (object, required)
  - `shard_id` (integer (uint32), required) — Minimum: 0.
  - `from_peer_id` (integer (uint64), required) — Minimum: 0.
  - `to_peer_id` (integer (uint64), required) — Minimum: 0.
  - `method` (string, required) — Methods for transferring a shard from one node to another. - `stream_records` - Stream all shard records in batches until the whole shard is transferred. - `snapshot` - Snapshot the shard, transfer and restore it on the receiver. - `wal_delta` - Attempt to transfer shard difference by WAL delta. - `resharding_stream_records` - Shard transfer for resharding: stream all records in batches until all points are transferred. Allowed values: `stream_records`, `snapshot`, `wal_delta`, `resharding_stream_records`.
- `start_resharding` (object, required)
  - `direction` (string, required) — Resharding direction, scale up or down in number of shards - `up` - Scale up, add a new shard - `down` - Scale down, remove a shard. Allowed values: `up`, `down`.
  - `peer_id` (integer (uint64)) — Peer to create the new shard on, or to migrate points away from when scaling down. If not specified, the least loaded peer is picked when scaling up, a peer holding the removed shard when scaling down. Minimum: 0. May be null.
  - `shard_key` (one of several types) — Custom shard key to reshard, must already exist. If not specified, shards without a shard key are resharded.
- `abort_resharding` (object, required)
- `replicate_points` (object, required)
  - `filter` (one of several types)
    - `should` (one of several types) — At least one of those conditions should match
    - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `conditions` (array of one of several types, required)
      - `min_count` (integer (uint), required) — Minimum: 1.
    - `must` (one of several types) — All conditions must match
    - `must_not` (one of several types) — All conditions must NOT match
  - `from_shard_key` (one of several types, required)
  - `to_shard_key` (one of several types, required)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

## Service

Qdrant service utilities.

### GET /

**Returns information about the running Qdrant instance**

Returns information about the running Qdrant instance like version and commit id

**Responses**

- **200** — Qdrant server version information
  Body (`application/json`, object):
  - `title` (string, required)
  - `version` (string, required)
  - `commit` (string) — May be null.
- **4XX** — error

### GET /telemetry

**Collect telemetry data**

Collect telemetry data including app info, system info, collections info, cluster info, configs and statistics

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `anonymize` | query | boolean | No | If true, anonymize result |
| `details_level` | query | integer | No | Level of details in telemetry data. Minimal level is 0, maximal is infinity. Minimum: 0. |
| `per_collection` | query | boolean | No | If true, include per-collection request statistics in the response |
| `timeout` | query | integer | No | Timeout for this request. Default: `60`. Minimum: 1. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `id` (string, required)
    - `app` (one of several types)
      - `name` (string, required)
      - `version` (string, required)
      - `features` (one of several types)
        - `debug` (boolean, required)
        - `service_debug_feature` (boolean, required)
        - `recovery_mode` (boolean, required)
        - `gpu` (boolean, required)
        - `rocksdb` (boolean, required)
        - `staging` (boolean, required)
      - `runtime_features` (one of several types)
        - `all` (boolean) — Magic feature flag that enables all features. Note that this will only be applied to all flags when passed into [`init_feature_flags`]. Default: `false`.
        - `incremental_hnsw_building` (boolean) — Use incremental HNSW building. Enabled by default in Qdrant 1.14.1. Default: `true`.
        - `appendable_quantization` (boolean) — Use appendable quantization in appendable plain segments. Enabled by default in Qdrant 1.16.0. Default: `true`.
        - `single_file_mmap_vector_storage` (boolean) — Use single-file mmap in-ram vector storage (InRamMmap) Enabled by default in Qdrant 1.18.3+. Default: `true`.
        - `async_payload_storage` (boolean) — Allow the io_uring-based payload storage implementation. When disabled, io_uring payload storage is *never* used. When enabled, payload storage backend is decided based on `storage.performance.io_uring` option and payload storage type. Default: `true`.
        - `async_hnsw_graph` (boolean) — Allow the batched io_uring-based HNSW graph search. When disabled, the HNSW graph is *never* opened on io_uring. When enabled, the graph backend is decided based on `storage.performance.io_uring` option and links placement. Default: `false`.
        - `write_segment_manifest` (boolean) — Write a segment manifest (`segments_manifest.json`, next to the `segments/` directory) listing the shard's segments and their state, so out-of-process readers can discover segments without scanning the filesystem. Default: `false`.
        - `append_only_mutations` (boolean) — Build new segments in append-only mode: in-place point mutations become clone-and-tombstone appends instead. Intended for testing the append-only storage path. Default: `false`.
        - `compact_bitmask` (boolean) — Persist write-once bitmasks in the compact `StoredBitmask` format instead of raw dense bitslices. Only gates writing: both formats are always readable. Default: `false`.
        - `append_only_storages` (boolean) — Create Blobstore-backed storages (payload storage, appendable field indexes, sparse vectors) in the append-only Logstore mode. Gates creation only: an existing storage keeps its persisted mode, and both modes are always readable. Implies [`Self::append_only_mutations`], enforced by [`init_feature_flags`]. Default: `false`.
        - `compact_logstore_tracker` (boolean) — In non-appendable segments built by the optimizer, store the tracker of an append-only payload storage in the compacted format: read into RAM whole on open instead of one lookup per value. Only has an effect together with [`Self::append_only_storages`]. Gates creation only: both formats are always readable. Default: `false`.
        - `transfer_raw_points` (boolean) — Transfer points as storage-native bytes (raw points), for every collection rather than only those whose vector storage would lose precision in a decode-encode round-trip (TurboQuant). Read on the sending side only, where the transfer batch is prepared: nodes accept raw points regardless. Default: `true`.
        - `transfer_raw_payloads` (boolean) — Send the payload of a raw point as the byte blob it is stored as, so the sending node does not parse it and neither node builds a protobuf value tree for it. The receiving node still parses the blob, once, when the operation is applied. Only has an effect on points transferred raw, see [`Self::transfer_raw_points`]. Read on the sending side only: nodes accept raw payloads regardless. Default: `true`.
        - `persist_proxy_segments` (boolean) — Persist proxy segment changes on disk. Prevents pinning the WAL while proxy segments are open. Replays the persisted changes on startup to guarantee data consistency. Required for serverless deployments where storage and compute is separated. Default: `false`.
        - `combined_vector_storage` (boolean) — When `hnsw_config.inline_storage` enabled, use the `GraphInline` vector storage (aka inline-storage without standalone vector storage) for new segments. Existing `GraphInline` segments are always readable, regardless of this flag. Default: `true`.
        - `serverless_compatible` (boolean) — Serverless-compatible deployment mode. Implies [`Self::write_segment_manifest`], [`Self::append_only_mutations`], [`Self::compact_bitmask`], [`Self::append_only_storages`], [`Self::compact_logstore_tracker`] and [`Self::persist_proxy_segments`]. Note that this will only be applied when passed into [`init_feature_flags`]. Default: `false`.
      - `low_memory_mode` (one of several types)
      - `hnsw_global_config` (one of several types)
        - `healing_threshold` (number (double)) — Enable HNSW healing if the ratio of missing points is no more than this value. To disable healing completely, set this value to `0.0`. Default: `0.3`. Minimum: 0. Maximum: 1.
      - `system` (one of several types)
        - `distribution` (string) — May be null.
        - `distribution_version` (string) — May be null.
        - `is_docker` (boolean, required)
        - `container_runtime` (string, required) — Container runtime Qdrant is running under (`none` if bare metal). Allowed values: `none`, `docker`, `kubernetes`, `other`.
        - `cores` (integer (uint)) — Minimum: 0. May be null.
        - `cpu_cores_used` (number (float)) — Average number of CPU cores used by this process over roughly the last two seconds. `None` on unsupported platforms, before two samples are collected, or on transient failures reading process CPU time. May be null.
        - `ram_size` (integer (uint)) — Effective total memory for this process in KiB (cgroup limit or host RAM). Minimum: 0. May be null.
        - `disk_size` (integer (uint)) — Size in KiB of the filesystem hosting Qdrant's /storage path (if not available, fallback to host disk size). Minimum: 0. May be null.
        - `cpu_flags` (string, required)
        - `cpu_endian` (one of several types)
        - `gpu_devices` (array of object) — May be null.
      - `jwt_rbac` (boolean) — May be null.
      - `hide_jwt_dashboard` (boolean) — May be null.
      - `audit` (one of several types)
        - `dir` (string, required)
        - `rotation` (string, required)
        - `max_log_files` (integer (uint), required) — Minimum: 0.
        - `trust_forwarded_headers` (boolean, required)
        - `log_api` (boolean, required)
        - `output` (string, required)
        - `dir_size_bytes` (integer (uint)) — Minimum: 0. May be null.
      - `startup` (string (date-time), required)
    - `collections` (object, required)
      - `number_of_collections` (integer (uint), required) — Minimum: 0.
      - `max_collections` (integer (uint)) — Minimum: 0. May be null.
      - `collections` (array of one of several types) — May be null.
        - `id` (string, required)
        - `init_time_ms` (integer (uint64)) — Minimum: 0. May be null.
        - `config` (one of several types)
        - `shards` (array of object) — May be null.
        - `transfers` (array of object) — May be null.
        - `resharding` (array of object) — May be null.
        - `shard_clean_tasks` (object) — May be null.
        - `vectors` (integer (uint), required) — Minimum: 0.
        - `optimizers_status` (one of several types, required) — Current state of the collection
        - `params` (object, required)
      - `snapshots` (array of object) — May be null.
        - `id` (string, required)
        - `running_snapshots` (integer (uint)) — Minimum: 0. May be null.
        - `running_snapshot_recovery` (integer (uint)) — Minimum: 0. May be null.
        - `total_snapshot_creations` (integer (uint)) — Minimum: 0. May be null.
    - `cluster` (one of several types)
      - `enabled` (boolean, required)
      - `status` (one of several types)
        - `number_of_peers` (integer (uint), required) — Minimum: 0.
        - `term` (integer (uint64), required) — Minimum: 0.
        - `commit` (integer (uint64), required) — Minimum: 0.
        - `pending_operations` (integer (uint), required) — Minimum: 0.
        - `role` (one of several types)
        - `is_voter` (boolean, required)
        - `peer_id` (integer (uint64)) — Minimum: 0. May be null.
        - `consensus_thread_status` (one of several types, required) — Information about current consensus thread status
      - `config` (one of several types)
        - `grpc_timeout_ms` (integer (uint64), required) — Minimum: 0.
        - `p2p` (object, required)
        - `consensus` (object, required)
      - `peers` (object) — May be null.
      - `peer_metadata` (object) — May be null.
      - `metadata` (object) — May be null.
      - `resharding_enabled` (boolean) — May be null.
    - `requests` (one of several types)
      - `rest` (object, required)
        - `responses` (object, required)
        - `per_collection_responses` (object)
      - `grpc` (object, required)
        - `responses` (object, required)
        - `per_collection_responses` (object)
    - `memory` (one of several types)
      - `active_bytes` (integer (uint), required) — Total number of bytes in active pages allocated by the application. Minimum: 0.
      - `allocated_bytes` (integer (uint), required) — Total number of bytes allocated by the application. Minimum: 0.
      - `metadata_bytes` (integer (uint), required) — Total number of bytes dedicated to metadata. Minimum: 0.
      - `resident_bytes` (integer (uint), required) — Maximum number of bytes in physically resident data pages mapped. Minimum: 0.
      - `retained_bytes` (integer (uint), required) — Total number of bytes in virtual memory mappings. Minimum: 0.
    - `hardware` (one of several types)
      - `collection_data` (object, required)
    - `search_pool` (one of several types)
      - `mode` (string, required) — Currently active mode (`high_cpu` or `high_io`).
      - `high_cpu_threads` (integer (uint), required) — Blocking-thread count of the high-CPU runtime. Minimum: 0.
      - `high_io_threads` (integer (uint), required) — Blocking-thread count of the high-IO runtime. Minimum: 0.
    - `quota` (one of several types) — Resource quota this node is enforcing, and whether it is currently over it. The config is whatever this node last persisted, so a peer that missed a consensus update reports what it is actually applying rather than what the cluster agreed on. Absent for a token without global access, which `GET /quotas` requires as well.
      - `config` (object, required) — Cluster-wide limits on node resources. An unset limit means the corresponding resource is not capped. Limits are only enforced while `enabled` is true.
        - `enabled` (boolean) — Whether the limits below are enforced. Default: `false`.
        - `max_resident_memory_percent` (integer (uint8)) — Reject memory-consuming updates once process resident memory reaches this percentage of total system memory (or of the cgroup limit, if one applies). Minimum: 1. Maximum: 100. May be null.
        - `max_disk_usage_percent` (integer (uint8)) — Reject disk-consuming updates once the filesystem hosting the storage directory is filled to this percentage of its capacity. Minimum: 1. Maximum: 100. May be null.
        - `release_margin_percent` (integer (uint8)) — How many percentage points below its limit a resource has to fall before this node starts accepting work again. Without a margin, a resource resting on its limit crosses it in both directions on the noise between two readings, putting the node in and out of service each time — and restarting a shard recovery with it. Raise it where usage is volatile; `0` disables the margin and releases as soon as usage is back under the limit. Unset leaves the built-in default in force, so a config written today does not pin a number that a later release may want to revise. Minimum: 0. Maximum: 100. May be null.
      - `exceeded` (object, required) — Which of the enforced limits a node is currently refusing work over. Reported per resource because they are freed by different actions: disk by deleting or optimizing, memory by unloading. A single flag would not say which one to go and fix. `true` outlasts the reading that caused it: a resource that reaches its limit stays flagged until it has fallen a margin below, so that one resting near the limit does not flip the node in and out of service. Expect to see it set while the reported utilization is already back under the configured limit. A field is `null` when the node is not enforcing that resource — the quota is disabled, no limit is set for it, or it cannot be measured here. That is deliberately distinct from `false`: a resource that can never trip must not be reported as one that is within its limits, or it invites an alert that can never fire.
        - `resident_memory` (boolean) — May be null.
        - `disk_usage` (boolean) — May be null.

### GET /metrics

**Collect Prometheus metrics data**

Collect metrics data including app info, collections info, cluster info and statistics

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `anonymize` | query | boolean | No | If true, anonymize result |
| `per_collection` | query | boolean | No | If true, include per-collection request metrics with a collection label instead of global request metrics |
| `timeout` | query | integer | No | Timeout for this request. Default: `60`. Minimum: 1. |

**Responses**

- **200** — Metrics data in Prometheus format
- **4XX** — error

### GET /healthz

**Kubernetes healthz endpoint**

Liveness-style health check. Returns 200 as soon as the HTTP API is serving requests. It does not inspect collections, shards or consensus state, and is identical to `/livez`. Use it only to detect whether the process is up and responsive.

**Responses**

- **200** — Healthz response
- **4XX** — error

### GET /livez

**Kubernetes livez endpoint**

Kubernetes liveness probe. Returns 200 as soon as the HTTP API is serving requests. It does not inspect collections, shards or consensus state, and is identical to `/healthz`. A failure indicates the process is unresponsive and should be restarted.

**Responses**

- **200** — Healthz response
- **4XX** — error

### GET /readyz

**Kubernetes readyz endpoint**

Kubernetes readiness probe. Checks the instance and waits out pending data operations to see when it can start accepting traffic. In a distributed deployment it returns 200 only once the node has caught up with the cluster consensus commit and its local shards are healthy; otherwise it returns 503. In a single-node deployment it always returns 200 once the API is up. Use it to decide when to route traffic to the instance.

**Responses**

- **200** — The instance is ready to accept traffic
- **503** — The instance is not ready to accept traffic yet
- **4XX** — error

## Beta

Beta features, do not depend on these yet.

### GET /issues

**Get issues**

Get a report of performance issues and configuration suggestions

**Responses**

- **200** — Successful response
- **4XX** — error

### DELETE /issues

**Clear issues**

Removes all issues reported so far

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

## Quotas

Cluster-wide resource quotas.

### GET /quotas

**Get global quotas**

Get the cluster-wide resource quota configuration, together with the current utilization it is measured against.
The configuration is the same on every peer, but the reported utilization is for the node serving this request only -
memory and disk are node-local, so query each peer to see where the whole cluster stands.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object) — Quota configuration in effect, and how close each peer is to it. The configuration is cluster-wide; the utilization is not. `usage` is the node that served the request, and `peers` is what every peer that answered reports about itself — memory and disk are node-local, so one peer being under its limit says nothing about the others.
    - `config` (object, required) — Cluster-wide limits on node resources. An unset limit means the corresponding resource is not capped. Limits are only enforced while `enabled` is true.
      - `enabled` (boolean) — Whether the limits below are enforced. Default: `false`.
      - `max_resident_memory_percent` (integer (uint8)) — Reject memory-consuming updates once process resident memory reaches this percentage of total system memory (or of the cgroup limit, if one applies). Minimum: 1. Maximum: 100. May be null.
      - `max_disk_usage_percent` (integer (uint8)) — Reject disk-consuming updates once the filesystem hosting the storage directory is filled to this percentage of its capacity. Minimum: 1. Maximum: 100. May be null.
      - `release_margin_percent` (integer (uint8)) — How many percentage points below its limit a resource has to fall before this node starts accepting work again. Without a margin, a resource resting on its limit crosses it in both directions on the noise between two readings, putting the node in and out of service each time — and restarting a shard recovery with it. Raise it where usage is volatile; `0` disables the margin and releases as soon as usage is back under the limit. Unset leaves the built-in default in force, so a config written today does not pin a number that a later release may want to revise. Minimum: 0. Maximum: 100. May be null.
    - `usage` (object, required) — Utilization of the quota-managed resources **on this node alone** — memory and disk are node-local, so a peer under its limit says nothing about the rest of the cluster. A field is `null` when the platform does not expose the underlying stat.
      - `resident_memory_percent` (integer (uint8)) — Resident memory of this node's process, as a percentage of the memory available to it (cgroup limit if one applies, else total system memory). Minimum: 0. May be null.
      - `disk_usage_percent` (integer (uint8)) — Used space of this node's storage filesystem, as a percentage of its capacity. Minimum: 0. May be null.
    - `peers` (object) — Utilization reported by each peer, keyed by peer ID, including the one that served the request. Only peers that answered are listed: a peer missing from the map could not be reached, which is itself worth seeing. Absent entirely outside distributed mode, where there are no peers to ask. May be null.

### PUT /quotas

**Set global quotas**

Replace the cluster-wide resource quota configuration. The new configuration is propagated to every peer through consensus and persisted, so it survives restarts

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `wait` | query | boolean | No | If true, wait until the new configuration is confirmed by consensus on this peer. If false - the request returns as soon as the change is proposed. Default: `false`. |

**Request body** (`application/json`)

Quota configuration to apply

- `enabled` (boolean) — Whether the limits below are enforced. Default: `false`.
- `max_resident_memory_percent` (integer (uint8)) — Reject memory-consuming updates once process resident memory reaches this percentage of total system memory (or of the cgroup limit, if one applies). Minimum: 1. Maximum: 100. May be null.
- `max_disk_usage_percent` (integer (uint8)) — Reject disk-consuming updates once the filesystem hosting the storage directory is filled to this percentage of its capacity. Minimum: 1. Maximum: 100. May be null.
- `release_margin_percent` (integer (uint8)) — How many percentage points below its limit a resource has to fall before this node starts accepting work again. Without a margin, a resource resting on its limit crosses it in both directions on the noise between two readings, putting the node in and out of service each time — and restarting a shard recovery with it. Raise it where usage is volatile; `0` disables the margin and releases as soon as usage is back under the limit. Unset leaves the built-in default in force, so a config written today does not pin a number that a later release may want to revise. Minimum: 0. Maximum: 100. May be null.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

## Collections

Searchable collections of points.

### GET /collections

**List collections**

Get list name of all existing collections

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `collections` (array of object, required)
      - `name` (string, required)

### GET /collections/{collection_name}

**Collection info**

Get detailed information about specified existing collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to retrieve |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object) — Current statistics and configuration of the collection
    - `status` (string, required) — Current state of the collection. `Green` - all good. `Yellow` - optimization is running, 'Grey' - optimizations are possible but not triggered, `Red` - some operations failed and was not recovered. Allowed values: `green`, `yellow`, `grey`, `red`.
    - `optimizer_status` (one of several types, required) — Current state of the collection
      - `error` (string, required)
    - `warnings` (array of object) — Warnings related to the collection
      - `message` (string, required) — Warning message
    - `indexed_vectors_count` (integer (uint)) — Approximate number of indexed vectors in the collection. Indexed vectors in large segments are faster to query, as it is stored in a specialized vector index. Minimum: 0. May be null.
    - `points_count` (integer (uint)) — Approximate number of points (vectors + payloads) in collection. Each point could be accessed by unique id. Minimum: 0. May be null.
    - `segments_count` (integer (uint), required) — Number of segments in collection. Each segment has independent vector as payload indexes. Minimum: 0.
    - `config` (object, required) — Information about the collection configuration
      - `params` (object, required)
        - `vectors` (one of several types) — Vector params separator for single and multiple vector modes Single mode: { "size": 128, "distance": "Cosine" } or multiple mode: { "default": { "size": 128, "distance": "Cosine" } }
        - `shard_number` (integer (uint32)) — Number of shards the collection has. Default: `1`. Minimum: 1.
        - `sharding_method` (one of several types) — Sharding method Default is Auto - points are distributed across all available shards Custom - points are distributed across shards according to shard key
        - `replication_factor` (integer (uint32)) — Number of replicas for each shard. Default: `1`. Minimum: 1.
        - `write_consistency_factor` (integer (uint32)) — Defines how many replicas should apply the operation for us to consider it successful. Increasing this number will make the collection more resilient to inconsistencies, but will also make it fail if not enough replicas are available. Does not have any performance impact. Default: `1`. Minimum: 1.
        - `read_fan_out_factor` (integer (uint32)) — Defines how many additional replicas should be processing read request at the same time. Default value is Auto, which means that fan-out will be determined automatically based on the busyness of the local replica. Having more than 0 might be useful to smooth latency spikes of individual nodes. Minimum: 0. May be null.
        - `read_fan_out_delay_ms` (integer (uint64)) — Define number of milliseconds to wait before attempting to read from another replica. This setting can help to reduce latency spikes in case of occasional slow replicas. Default is 0, which means delayed fan out request is disabled. Minimum: 0. May be null.
        - `on_disk_payload` (boolean) — Deprecated: use `payload.memory` instead. If true - point's payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by (slightly) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM. Default: true. Default: `true`. May be null.
        - `payload` (one of several types) — Configuration of the payload storage
        - `id_tracker` (one of several types) — Configuration of the point id tracker
        - `sparse_vectors` (object) — Configuration of the sparse vector storage. May be null.
      - `hnsw_config` (object, required) — Config of HNSW index
        - `m` (integer (uint), required) — Number of edges per node in the index graph. Larger the value - more accurate the search, more space required. Set to 0 to disable the main HNSW graph. Additional payload-aware links may still be built when the effective payload M is positive (see payload_m). This setting alone does not guarantee exact search. Minimum: 0.
        - `ef_construct` (integer (uint), required) — Number of neighbours to consider during the index building. Larger the value - more accurate the search, more time required to build index. Minimum: 4.
        - `full_scan_threshold` (integer (uint), required) — Minimal size threshold (in KiloBytes) below which full-scan is preferred over HNSW search. This measures the total size of vectors being queried against. When the maximum estimated amount of points that a condition satisfies is smaller than `full_scan_threshold_kb`, the query planner will use full-scan search instead of HNSW index traversal for better performance. Note: 1Kb = 1 vector of size 256. Minimum: 0.
        - `max_indexing_threads` (integer (uint)) — Number of parallel threads used for background index building. If 0 - automatically select from 8 to 16. Best to keep between 8 and 16 to prevent likelihood of slow building or broken/inefficient HNSW graphs. On small CPUs, less threads are used. Default: `0`. Minimum: 0.
        - `on_disk` (boolean) — Deprecated: use `memory` instead. Store HNSW index on disk. If set to false, index will be stored in RAM. Default: false. May be null.
        - `memory` (one of several types) — Memory placement of the HNSW graph. Overrides the deprecated `on_disk` flag if both are set. Default: `cached` (`cold` if `on_disk` is set to true).
        - `payload_m` (integer (uint)) — Number of additional payload-aware links per node. If unset, the value of m is used. An effective value of 0 disables these additional links. A positive value allows them for indexed payload fields with HNSW enabled, even when m is 0. Minimum: 0. May be null.
        - `inline_storage` (boolean) — Store copies of original and quantized vectors within the HNSW index file. Default: false. Enabling this option will trade the search speed for disk usage by reducing amount of random seeks during the search. Requires quantized vectors to be enabled. Multi-vectors are not supported. May be null.
      - `optimizer_config` (object, required)
        - `deleted_threshold` (number (double)) — The minimal fraction of deleted vectors in a segment, required to perform segment optimization. Default: `0.2`. Minimum: 0. Maximum: 1.
        - `vacuum_min_vector_number` (integer (uint)) — The minimal number of vectors in a segment, required to perform segment optimization. Default: `1000`. Minimum: 100.
        - `default_segment_number` (integer (uint), required) — Target amount of segments optimizer will try to keep. Real amount of segments may vary depending on multiple parameters: - Amount of stored points - Current write RPS It is recommended to select default number of segments as a factor of the number of search threads, so that each segment would be handled evenly by one of the threads. If `default_segment_number = 0`, will be automatically selected by the number of available CPUs. Minimum: 0.
        - `max_segment_size` (integer (uint)) — Do not create segments larger than this size (in kilobytes). Large segments might require disproportionately long indexation times, therefore it makes sense to limit the size of segments. If indexing speed is more important - make this parameter lower. If search speed is more important - make this parameter higher. Note: 1Kb = 1 vector of size 256 If not set, will be automatically selected considering the number of available CPUs. Default: `None`. Minimum: 1. May be null.
        - `memmap_threshold` (integer (uint)) — Maximum size (in kilobytes) of vectors to store in-memory per segment. Segments larger than this threshold will be stored as read-only memmapped file. Memmap storage is disabled by default, to enable it, set this threshold to a reasonable value. To disable memmap storage, set this to `0`. Internally it will use the largest threshold possible. Note: 1Kb = 1 vector of size 256. Default: `None`. Minimum: 0. May be null.
        - `indexing_threshold` (integer (uint)) — Maximum size (in kilobytes) of vectors allowed for plain index, exceeding this threshold will enable vector indexing Default value is 10,000, based on experiments and observations. To disable vector indexing, set to `0`. Note: 1kB = 1 vector of size 256. Default: `None`. Minimum: 0. May be null.
        - `flush_interval_sec` (integer (uint64), required) — Minimum interval between forced flushes. Minimum: 0.
        - `max_optimization_threads` (integer (uint)) — Max number of threads (jobs) for running optimizations per shard. Note: each optimization job will also use `max_indexing_threads` threads by itself for index building. If null - have no limit and choose dynamically to saturate CPU. If 0 - no optimization threads, optimizations will be disabled. Default: `None`. Minimum: 0. May be null.
        - `prevent_unoptimized` (boolean) — If enabled, the service will try to prevent the creation of large unoptimized segments. When enabled, new points written to segments larger than the indexing threshold are stored as "deferred points": they are persisted in the WAL and segments, but excluded from read/search results until the corresponding segments are optimized (e.g. indexed, quantized, or moved to mmap storage). Update requests with `wait=true` will only return after the deferred points become visible, which may significantly increase the perceived latency between submitting an update and its completion. Update requests with `wait=false` are not affected. Default is disabled. Default: `None`. May be null.
      - `wal_config` (one of several types)
        - `wal_capacity_mb` (integer (uint), required) — Size of a single WAL segment in MB. Minimum: 1.
        - `wal_segments_ahead` (integer (uint), required) — Number of WAL segments to create ahead of actually used ones. Minimum: 0.
        - `wal_retain_closed` (integer (uint)) — Number of closed WAL segments to keep. Default: `1`. Minimum: 1.
      - `quantization_config` (one of several types) — Default: `None`.
      - `strict_mode_config` (one of several types)
        - `enabled` (boolean) — Whether strict mode is enabled for a collection or not. May be null.
        - `max_query_limit` (integer (uint)) — Max allowed `limit` parameter for all APIs that don't have their own max limit. Minimum: 0. May be null.
        - `max_timeout` (integer (uint)) — Max allowed `timeout` parameter. Minimum: 0. May be null.
        - `unindexed_filtering_retrieve` (boolean) — Allow usage of unindexed fields in retrieval based (e.g. search) filters. May be null.
        - `unindexed_filtering_update` (boolean) — Allow usage of unindexed fields in filtered updates (e.g. delete by payload). May be null.
        - `search_max_hnsw_ef` (integer (uint)) — Max HNSW value allowed in search parameters. Minimum: 0. May be null.
        - `search_allow_exact` (boolean) — Whether exact search is allowed or not. May be null.
        - `search_max_oversampling` (number (double)) — Max oversampling value allowed in search. May be null.
        - `upsert_max_batchsize` (integer (uint)) — Max batchsize when upserting. Minimum: 0. May be null.
        - `search_max_batchsize` (integer (uint)) — Max batchsize when searching. Minimum: 0. May be null.
        - `max_collection_vector_size_bytes` (integer (uint)) — Max size of a collections vector storage in bytes, ignoring replicas. Minimum: 0. May be null.
        - `read_rate_limit` (integer (uint)) — Max number of read operations per minute per replica. Minimum: 0. May be null.
        - `write_rate_limit` (integer (uint)) — Max number of write operations per minute per replica. Minimum: 0. May be null.
        - `max_collection_payload_size_bytes` (integer (uint)) — Max size of a collections payload storage in bytes. Minimum: 0. May be null.
        - `max_points_count` (integer (uint)) — Max number of points estimated in a collection. Minimum: 0. May be null.
        - `filter_max_conditions` (integer (uint)) — Max conditions a filter can have. Minimum: 0. May be null.
        - `condition_max_size` (integer (uint)) — Max size of a condition, eg. items in `MatchAny`. Minimum: 0. May be null.
        - `multivector_config` (one of several types) — Multivector configuration
        - `sparse_config` (one of several types) — Sparse vector configuration
        - `max_payload_index_count` (integer (uint)) — Max number of payload indexes in a collection. Minimum: 0. May be null.
        - `max_resident_memory_percent` (integer (uint8)) — Deprecated: use the node-wide quota config instead. Reject memory-consuming update operations when resident memory exceeds this percentage of total RAM (1-100). Minimum: 0. May be null.
      - `metadata` (one of several types) — Arbitrary JSON metadata for the collection This can be used to store application-specific information such as creation time, migration data, inference model info, etc.
    - `payload_schema` (object, required) — Types of stored payload
    - `update_queue` (one of several types) — Update queue info
      - `length` (integer (uint), required) — Number of elements in the queue. Minimum: 0.
      - `deferred_points` (integer (uint)) — Number of points that are deferred (i.e hidden from search as they're not yet optimized). Minimum: 0. May be null.
    - `created_at` (string (date-time)) — Time of the collection creation. Absent for collections created before Qdrant started recording it. May be null.

### PUT /collections/{collection_name}

**Create collection**

Create new collection with given parameters

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the new collection |
| `timeout` | query | integer | No | Wait for operation commit timeout in seconds. If timeout is reached - request will return with service error. Minimum: 1. |

**Request body** (`application/json`)

Parameters of a new collection

- `vectors` (one of several types) — Vector params separator for single and multiple vector modes Single mode: { "size": 128, "distance": "Cosine" } or multiple mode: { "default": { "size": 128, "distance": "Cosine" } }
  - `size` (integer (uint64), required) — Size of a vectors used. Minimum: 1. Maximum: 65536.
  - `distance` (string, required) — Type of internal tags, build from payload Distance function types used to compare vectors. Allowed values: `Cosine`, `Euclid`, `Dot`, `Manhattan`.
  - `hnsw_config` (one of several types) — Custom params for HNSW index. If none - values from collection configuration are used.
    - `m` (integer (uint)) — Number of edges per node in the index graph. Larger the value - more accurate the search, more space required. Set to 0 to disable the main HNSW graph. Additional payload-aware links may still be built when the effective payload M is positive (see payload_m). This setting alone does not guarantee exact search. Minimum: 0. May be null.
    - `ef_construct` (integer (uint)) — Number of neighbours to consider during the index building. Larger the value - more accurate the search, more time required to build the index. Minimum: 4. May be null.
    - `full_scan_threshold` (integer (uint)) — Minimal size threshold (in KiloBytes) below which full-scan is preferred over HNSW search. This measures the total size of vectors being queried against. When the maximum estimated amount of points that a condition satisfies is smaller than `full_scan_threshold_kb`, the query planner will use full-scan search instead of HNSW index traversal for better performance. Note: 1Kb = 1 vector of size 256. Minimum: 10. May be null.
    - `max_indexing_threads` (integer (uint)) — Number of parallel threads used for background index building. If 0 - automatically select from 8 to 16. Best to keep between 8 and 16 to prevent likelihood of building broken/inefficient HNSW graphs. On small CPUs, less threads are used. Minimum: 0. May be null.
    - `on_disk` (boolean) — Deprecated: use `memory` instead. Store HNSW index on disk. If set to false, the index will be stored in RAM. Default: false. May be null.
    - `memory` (one of several types) — Memory placement of the HNSW graph. Overrides the deprecated `on_disk` flag if both are set. Default: `cached` (`cold` if `on_disk` is set to true).
    - `payload_m` (integer (uint)) — Number of additional payload-aware links per node. If unset, the value of m is used. An effective value of 0 disables these additional links. A positive value allows them for indexed payload fields with HNSW enabled, even when m is 0. Minimum: 0. May be null.
    - `inline_storage` (boolean) — Store copies of original and quantized vectors within the HNSW index file. Default: false. Enabling this option will trade the search speed for disk usage by reducing amount of random seeks during the search. Requires quantized vectors to be enabled. Multi-vectors are not supported. May be null.
  - `quantization_config` (one of several types) — Custom params for quantization. If none - values from collection configuration are used.
  - `on_disk` (boolean) — Deprecated: use `memory` instead. If true, vectors are served from disk, improving RAM usage at the cost of latency Default: false. May be null.
  - `memory` (one of several types) — Memory placement of the original vector storage. Overrides the deprecated `on_disk` flag if both are set. `pinned` is not supported for dense vector storage. Default: `cached` (`cold` if `on_disk` is set to true).
  - `datatype` (one of several types) — Defines which datatype should be used to represent vectors in the storage. Choosing different datatypes allows to optimize memory usage and performance vs accuracy. - For `float32` datatype - vectors are stored as single-precision floating point numbers, 4 bytes. - For `float16` datatype - vectors are stored as half-precision floating point numbers, 2 bytes. - For `uint8` datatype - vectors are stored as unsigned 8-bit integers, 1 byte. It expects vector elements to be in range `[0, 255]`. - For `turbo4` datatype - vectors are quantized to 4 bits per element using the TurboQuant algorithm. - For `turbo8` datatype - vectors are quantized to 8 bits per element using the TurboQuant algorithm. - For `turbo16` datatype - vectors are quantized to 16 bits per element using the TurboQuant algorithm.
  - `multivector_config` (one of several types)
    - `comparator` (string, required) — Allowed values: `max_sim`.
- `shard_number` (integer (uint32)) — For auto sharding: Number of shards in collection. - If not specified, selected automatically - Minimum is 1 For custom sharding: Number of shards in collection per shard group. - Default is 1, meaning that each shard key will be mapped to a single shard - Minimum is 1. Default: `None`. Minimum: 1. May be null.
- `sharding_method` (one of several types) — Sharding method Default is Auto - points are distributed across all available shards Custom - points are distributed across shards according to shard key. Default: `None`.
- `replication_factor` (integer (uint32)) — Number of shards replicas. Default is 1 Minimum is 1. Default: `None`. Minimum: 1. May be null.
- `write_consistency_factor` (integer (uint32)) — Defines how many replicas should apply the operation for us to consider it successful. Increasing this number will make the collection more resilient to inconsistencies, but will also make it fail if not enough replicas are available. Does not have any performance impact. Default: `None`. Minimum: 1. May be null.
- `on_disk_payload` (boolean) — Deprecated: use `payload.memory` instead. If true - point's payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by (slightly) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM. Default: true. Default: `None`. May be null.
- `payload` (one of several types) — Configuration of the payload storage. Default: `None`.
  - `memory` (one of several types) — Memory placement of the payload storage. Overrides the deprecated `on_disk_payload` flag if both are set. `pinned` is not supported for payload storage. Default: `cold` (`cached` if `on_disk_payload` is set to false).
- `id_tracker` (one of several types) — Configuration of the point id tracker. Default: `None`.
  - `memory` (one of several types) — Memory placement of the point id mapping in indexed segments: `cold` keeps it on disk and reads it on demand, `cached` keeps it on disk but primes the page cache with it on load, `pinned` keeps it in RAM. Default: `pinned`.
- `hnsw_config` (one of several types) — Custom params for HNSW index. If none - values from service configuration file are used.
  - `m` (integer (uint)) — Number of edges per node in the index graph. Larger the value - more accurate the search, more space required. Set to 0 to disable the main HNSW graph. Additional payload-aware links may still be built when the effective payload M is positive (see payload_m). This setting alone does not guarantee exact search. Minimum: 0. May be null.
  - `ef_construct` (integer (uint)) — Number of neighbours to consider during the index building. Larger the value - more accurate the search, more time required to build the index. Minimum: 4. May be null.
  - `full_scan_threshold` (integer (uint)) — Minimal size threshold (in KiloBytes) below which full-scan is preferred over HNSW search. This measures the total size of vectors being queried against. When the maximum estimated amount of points that a condition satisfies is smaller than `full_scan_threshold_kb`, the query planner will use full-scan search instead of HNSW index traversal for better performance. Note: 1Kb = 1 vector of size 256. Minimum: 10. May be null.
  - `max_indexing_threads` (integer (uint)) — Number of parallel threads used for background index building. If 0 - automatically select from 8 to 16. Best to keep between 8 and 16 to prevent likelihood of building broken/inefficient HNSW graphs. On small CPUs, less threads are used. Minimum: 0. May be null.
  - `on_disk` (boolean) — Deprecated: use `memory` instead. Store HNSW index on disk. If set to false, the index will be stored in RAM. Default: false. May be null.
  - `memory` (one of several types) — Memory placement of the HNSW graph. Overrides the deprecated `on_disk` flag if both are set. Default: `cached` (`cold` if `on_disk` is set to true).
  - `payload_m` (integer (uint)) — Number of additional payload-aware links per node. If unset, the value of m is used. An effective value of 0 disables these additional links. A positive value allows them for indexed payload fields with HNSW enabled, even when m is 0. Minimum: 0. May be null.
  - `inline_storage` (boolean) — Store copies of original and quantized vectors within the HNSW index file. Default: false. Enabling this option will trade the search speed for disk usage by reducing amount of random seeks during the search. Requires quantized vectors to be enabled. Multi-vectors are not supported. May be null.
- `wal_config` (one of several types) — Custom params for WAL. If none - values from service configuration file are used.
  - `wal_capacity_mb` (integer (uint)) — Size of a single WAL segment in MB. Minimum: 1. May be null.
  - `wal_segments_ahead` (integer (uint)) — Number of WAL segments to create ahead of actually used ones. Minimum: 0. May be null.
  - `wal_retain_closed` (integer (uint)) — Number of closed WAL segments to retain. Minimum: 0. May be null.
- `optimizers_config` (one of several types) — Custom params for Optimizers. If none - values from service configuration file are used.
  - `deleted_threshold` (number (double)) — The minimal fraction of deleted vectors in a segment, required to perform segment optimization. Minimum: 0. Maximum: 1. May be null.
  - `vacuum_min_vector_number` (integer (uint)) — The minimal number of vectors in a segment, required to perform segment optimization. Minimum: 100. May be null.
  - `default_segment_number` (integer (uint)) — Target amount of segments optimizer will try to keep. Real amount of segments may vary depending on multiple parameters: - Amount of stored points - Current write RPS It is recommended to select default number of segments as a factor of the number of search threads, so that each segment would be handled evenly by one of the threads If `default_segment_number = 0`, will be automatically selected by the number of available CPUs. Minimum: 0. May be null.
  - `max_segment_size` (integer (uint)) — Do not create segments larger than this size (in kilobytes). Large segments might require disproportionately long indexation times, therefore it makes sense to limit the size of segments. If indexation speed have more priority for your - make this parameter lower. If search speed is more important - make this parameter higher. Note: 1Kb = 1 vector of size 256. Minimum: 1. May be null.
  - `memmap_threshold` (integer (uint)) — Maximum size (in kilobytes) of vectors to store in-memory per segment. Segments larger than this threshold will be stored as read-only memmapped file. Memmap storage is disabled by default, to enable it, set this threshold to a reasonable value. To disable memmap storage, set this to `0`. Note: 1Kb = 1 vector of size 256 Deprecated since Qdrant 1.15.0. Minimum: 0. May be null.
  - `indexing_threshold` (integer (uint)) — Maximum size (in kilobytes) of vectors allowed for plain index, exceeding this threshold will enable vector indexing Default value is 20,000, based on <https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md>. To disable vector indexing, set to `0`. Note: 1kB = 1 vector of size 256. Minimum: 0. May be null.
  - `flush_interval_sec` (integer (uint64)) — Minimum interval between forced flushes. Minimum: 0. May be null.
  - `max_optimization_threads` (one of several types) — Max number of threads (jobs) for running optimizations per shard. Note: each optimization job will also use `max_indexing_threads` threads by itself for index building. If "auto" - have no limit and choose dynamically to saturate CPU. If 0 - no optimization threads, optimizations will be disabled.
  - `prevent_unoptimized` (boolean) — If enabled, the service will try to prevent the creation of large unoptimized segments. When enabled, new points written to segments larger than the indexing threshold are stored as "deferred points": they are persisted in the WAL and segments, but excluded from read/search results until the corresponding segments are optimized (e.g. indexed, quantized, or moved to mmap storage). Update requests with `wait=true` will only return after the deferred points become visible, which may significantly increase the perceived latency between submitting an update and its completion. Update requests with `wait=false` are not affected. Default is disabled. Default: `None`. May be null.
- `quantization_config` (one of several types) — Quantization parameters. If none - quantization is disabled. Default: `None`.
- `sparse_vectors` (object) — Sparse vector data config. May be null.
- `strict_mode_config` (one of several types) — Strict-mode config.
  - `enabled` (boolean) — Whether strict mode is enabled for a collection or not. May be null.
  - `max_query_limit` (integer (uint)) — Max allowed `limit` parameter for all APIs that don't have their own max limit. Minimum: 1. May be null.
  - `max_timeout` (integer (uint)) — Max allowed `timeout` parameter. Minimum: 1. May be null.
  - `unindexed_filtering_retrieve` (boolean) — Allow usage of unindexed fields in retrieval based (e.g. search) filters. May be null.
  - `unindexed_filtering_update` (boolean) — Allow usage of unindexed fields in filtered updates (e.g. delete by payload). May be null.
  - `search_max_hnsw_ef` (integer (uint)) — Max HNSW ef value allowed in search parameters. Minimum: 0. May be null.
  - `search_allow_exact` (boolean) — Whether exact search is allowed. May be null.
  - `search_max_oversampling` (number (double)) — Max oversampling value allowed in search. May be null.
  - `upsert_max_batchsize` (integer (uint)) — Max batchsize when upserting. Minimum: 0. May be null.
  - `search_max_batchsize` (integer (uint)) — Max batchsize when searching. Minimum: 0. May be null.
  - `max_collection_vector_size_bytes` (integer (uint)) — Max size of a collections vector storage in bytes, ignoring replicas. Minimum: 0. May be null.
  - `read_rate_limit` (integer (uint)) — Max number of read operations per minute per replica. Minimum: 1. May be null.
  - `write_rate_limit` (integer (uint)) — Max number of write operations per minute per replica. Minimum: 1. May be null.
  - `max_collection_payload_size_bytes` (integer (uint)) — Max size of a collections payload storage in bytes. Minimum: 0. May be null.
  - `max_points_count` (integer (uint)) — Max number of points estimated in a collection. Minimum: 1. May be null.
  - `filter_max_conditions` (integer (uint)) — Max conditions a filter can have. Minimum: 0. May be null.
  - `condition_max_size` (integer (uint)) — Max size of a condition, eg. items in `MatchAny`. Minimum: 0. May be null.
  - `multivector_config` (one of several types) — Multivector strict mode configuration
  - `sparse_config` (one of several types) — Sparse vector strict mode configuration
  - `max_payload_index_count` (integer (uint)) — Max number of payload indexes in a collection. Minimum: 0. May be null.
  - `max_resident_memory_percent` (integer (uint8)) — Deprecated: use the node-wide quota config (`PUT /quotas`) instead, which caps the same resource for every collection. Scheduled for removal in 1.21. Reject memory-consuming update operations (e.g. upsert, set payload) when the process resident memory exceeds this percentage of total system memory (or cgroup limit). Value in [1, 100]. Memory is a node-wide resource, so this only tightens the quota for one collection; it cannot lift it. Delete operations are not affected, so callers can still free memory. Minimum: 1. Maximum: 100. May be null.
- `metadata` (one of several types) — Arbitrary JSON metadata for the collection This can be used to store application-specific information such as creation time, migration data, inference model info, etc.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

### DELETE /collections/{collection_name}

**Delete collection**

Drop collection and all associated data

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to delete |
| `timeout` | query | integer | No | Wait for operation commit timeout in seconds. If timeout is reached - request will return with service error. Minimum: 1. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

### PATCH /collections/{collection_name}

**Update collection parameters**

Update parameters of the existing collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to update |
| `timeout` | query | integer | No | Wait for operation commit timeout in seconds. If timeout is reached - request will return with service error. Minimum: 1. |

**Request body** (`application/json`)

New parameters

- `vectors` (one of several types) — Map of vector data parameters to update for each named vector. To update parameters in a collection having a single unnamed vector, use an empty string as name.
- `optimizers_config` (one of several types) — Custom params for Optimizers. If none - it is left unchanged. This operation is blocking, it will only proceed once all current optimizations are complete
  - `deleted_threshold` (number (double)) — The minimal fraction of deleted vectors in a segment, required to perform segment optimization. Minimum: 0. Maximum: 1. May be null.
  - `vacuum_min_vector_number` (integer (uint)) — The minimal number of vectors in a segment, required to perform segment optimization. Minimum: 100. May be null.
  - `default_segment_number` (integer (uint)) — Target amount of segments optimizer will try to keep. Real amount of segments may vary depending on multiple parameters: - Amount of stored points - Current write RPS It is recommended to select default number of segments as a factor of the number of search threads, so that each segment would be handled evenly by one of the threads If `default_segment_number = 0`, will be automatically selected by the number of available CPUs. Minimum: 0. May be null.
  - `max_segment_size` (integer (uint)) — Do not create segments larger than this size (in kilobytes). Large segments might require disproportionately long indexation times, therefore it makes sense to limit the size of segments. If indexation speed have more priority for your - make this parameter lower. If search speed is more important - make this parameter higher. Note: 1Kb = 1 vector of size 256. Minimum: 1. May be null.
  - `memmap_threshold` (integer (uint)) — Maximum size (in kilobytes) of vectors to store in-memory per segment. Segments larger than this threshold will be stored as read-only memmapped file. Memmap storage is disabled by default, to enable it, set this threshold to a reasonable value. To disable memmap storage, set this to `0`. Note: 1Kb = 1 vector of size 256 Deprecated since Qdrant 1.15.0. Minimum: 0. May be null.
  - `indexing_threshold` (integer (uint)) — Maximum size (in kilobytes) of vectors allowed for plain index, exceeding this threshold will enable vector indexing Default value is 20,000, based on <https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md>. To disable vector indexing, set to `0`. Note: 1kB = 1 vector of size 256. Minimum: 0. May be null.
  - `flush_interval_sec` (integer (uint64)) — Minimum interval between forced flushes. Minimum: 0. May be null.
  - `max_optimization_threads` (one of several types) — Max number of threads (jobs) for running optimizations per shard. Note: each optimization job will also use `max_indexing_threads` threads by itself for index building. If "auto" - have no limit and choose dynamically to saturate CPU. If 0 - no optimization threads, optimizations will be disabled.
  - `prevent_unoptimized` (boolean) — If enabled, the service will try to prevent the creation of large unoptimized segments. When enabled, new points written to segments larger than the indexing threshold are stored as "deferred points": they are persisted in the WAL and segments, but excluded from read/search results until the corresponding segments are optimized (e.g. indexed, quantized, or moved to mmap storage). Update requests with `wait=true` will only return after the deferred points become visible, which may significantly increase the perceived latency between submitting an update and its completion. Update requests with `wait=false` are not affected. Default is disabled. Default: `None`. May be null.
- `params` (one of several types) — Collection base params. If none - it is left unchanged.
  - `replication_factor` (integer (uint32)) — Number of replicas for each shard. Minimum: 1. May be null.
  - `write_consistency_factor` (integer (uint32)) — Minimal number successful responses from replicas to consider operation successful. Minimum: 1. May be null.
  - `read_fan_out_factor` (integer (uint32)) — Fan-out every read request to these many additional remote nodes (and return first available response). Minimum: 0. May be null.
  - `read_fan_out_delay_ms` (integer (uint64)) — Delay in milliseconds before sending read requests to remote nodes. Minimum: 0. May be null.
  - `on_disk_payload` (boolean) — Deprecated: use `payload.memory` instead. If true - point's payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by (slightly) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM. Default: `None`. May be null.
  - `payload` (one of several types) — Update params of the payload storage. If none - it is left unchanged.
    - `memory` (one of several types) — Memory placement of the payload storage. Overrides the deprecated `on_disk_payload` flag if both are set. `pinned` is not supported for payload storage. Default: `cold` (`cached` if `on_disk_payload` is set to false).
  - `id_tracker` (one of several types) — Update params of the point id tracker. If none - it is left unchanged.
    - `memory` (one of several types) — Memory placement of the point id mapping in indexed segments: `cold` keeps it on disk and reads it on demand, `cached` keeps it on disk but primes the page cache with it on load, `pinned` keeps it in RAM. Default: `pinned`.
- `hnsw_config` (one of several types) — HNSW parameters to update for the collection index. If none - it is left unchanged.
  - `m` (integer (uint)) — Number of edges per node in the index graph. Larger the value - more accurate the search, more space required. Set to 0 to disable the main HNSW graph. Additional payload-aware links may still be built when the effective payload M is positive (see payload_m). This setting alone does not guarantee exact search. Minimum: 0. May be null.
  - `ef_construct` (integer (uint)) — Number of neighbours to consider during the index building. Larger the value - more accurate the search, more time required to build the index. Minimum: 4. May be null.
  - `full_scan_threshold` (integer (uint)) — Minimal size threshold (in KiloBytes) below which full-scan is preferred over HNSW search. This measures the total size of vectors being queried against. When the maximum estimated amount of points that a condition satisfies is smaller than `full_scan_threshold_kb`, the query planner will use full-scan search instead of HNSW index traversal for better performance. Note: 1Kb = 1 vector of size 256. Minimum: 10. May be null.
  - `max_indexing_threads` (integer (uint)) — Number of parallel threads used for background index building. If 0 - automatically select from 8 to 16. Best to keep between 8 and 16 to prevent likelihood of building broken/inefficient HNSW graphs. On small CPUs, less threads are used. Minimum: 0. May be null.
  - `on_disk` (boolean) — Deprecated: use `memory` instead. Store HNSW index on disk. If set to false, the index will be stored in RAM. Default: false. May be null.
  - `memory` (one of several types) — Memory placement of the HNSW graph. Overrides the deprecated `on_disk` flag if both are set. Default: `cached` (`cold` if `on_disk` is set to true).
  - `payload_m` (integer (uint)) — Number of additional payload-aware links per node. If unset, the value of m is used. An effective value of 0 disables these additional links. A positive value allows them for indexed payload fields with HNSW enabled, even when m is 0. Minimum: 0. May be null.
  - `inline_storage` (boolean) — Store copies of original and quantized vectors within the HNSW index file. Default: false. Enabling this option will trade the search speed for disk usage by reducing amount of random seeks during the search. Requires quantized vectors to be enabled. Multi-vectors are not supported. May be null.
- `quantization_config` (one of several types) — Quantization parameters to update. If none - it is left unchanged. Default: `None`.
- `sparse_vectors` (one of several types) — Map of sparse vector data parameters to update for each sparse vector.
- `strict_mode_config` (one of several types)
  - `enabled` (boolean) — Whether strict mode is enabled for a collection or not. May be null.
  - `max_query_limit` (integer (uint)) — Max allowed `limit` parameter for all APIs that don't have their own max limit. Minimum: 1. May be null.
  - `max_timeout` (integer (uint)) — Max allowed `timeout` parameter. Minimum: 1. May be null.
  - `unindexed_filtering_retrieve` (boolean) — Allow usage of unindexed fields in retrieval based (e.g. search) filters. May be null.
  - `unindexed_filtering_update` (boolean) — Allow usage of unindexed fields in filtered updates (e.g. delete by payload). May be null.
  - `search_max_hnsw_ef` (integer (uint)) — Max HNSW ef value allowed in search parameters. Minimum: 0. May be null.
  - `search_allow_exact` (boolean) — Whether exact search is allowed. May be null.
  - `search_max_oversampling` (number (double)) — Max oversampling value allowed in search. May be null.
  - `upsert_max_batchsize` (integer (uint)) — Max batchsize when upserting. Minimum: 0. May be null.
  - `search_max_batchsize` (integer (uint)) — Max batchsize when searching. Minimum: 0. May be null.
  - `max_collection_vector_size_bytes` (integer (uint)) — Max size of a collections vector storage in bytes, ignoring replicas. Minimum: 0. May be null.
  - `read_rate_limit` (integer (uint)) — Max number of read operations per minute per replica. Minimum: 1. May be null.
  - `write_rate_limit` (integer (uint)) — Max number of write operations per minute per replica. Minimum: 1. May be null.
  - `max_collection_payload_size_bytes` (integer (uint)) — Max size of a collections payload storage in bytes. Minimum: 0. May be null.
  - `max_points_count` (integer (uint)) — Max number of points estimated in a collection. Minimum: 1. May be null.
  - `filter_max_conditions` (integer (uint)) — Max conditions a filter can have. Minimum: 0. May be null.
  - `condition_max_size` (integer (uint)) — Max size of a condition, eg. items in `MatchAny`. Minimum: 0. May be null.
  - `multivector_config` (one of several types) — Multivector strict mode configuration
  - `sparse_config` (one of several types) — Sparse vector strict mode configuration
  - `max_payload_index_count` (integer (uint)) — Max number of payload indexes in a collection. Minimum: 0. May be null.
  - `max_resident_memory_percent` (integer (uint8)) — Deprecated: use the node-wide quota config (`PUT /quotas`) instead, which caps the same resource for every collection. Scheduled for removal in 1.21. Reject memory-consuming update operations (e.g. upsert, set payload) when the process resident memory exceeds this percentage of total system memory (or cgroup limit). Value in [1, 100]. Memory is a node-wide resource, so this only tightens the quota for one collection; it cannot lift it. Delete operations are not affected, so callers can still free memory. Minimum: 1. Maximum: 100. May be null.
- `metadata` (one of several types) — Metadata to update for the collection. If provided, this will merge with existing metadata. Individual keys can be removed by setting their value to `null`.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

### GET /collections/{collection_name}/exists

**Check the existence of a collection**

Returns "true" if the given collection name exists, and "false" otherwise

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object) — State of existence of a collection, true = exists, false = does not exist
    - `exists` (boolean, required)

### PUT /collections/{collection_name}/vectors/{vector_name}

**Create named vector**

Create a new named vector on an existing collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `vector_name` | path | string | Yes | Name of the vector to create |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

Vector configuration - dense or sparse

- `dense` (object, required) — Configuration for creating a new dense named vector. Only includes properties that define the vector space and cannot be changed after creation. Storage type, index type, and quantization are inferred.
  - `size` (integer (uint), required) — Dimensionality of the vectors. Minimum: 1. Maximum: 65536.
  - `distance` (string, required) — Type of internal tags, build from payload Distance function types used to compare vectors. Allowed values: `Cosine`, `Euclid`, `Dot`, `Manhattan`.
  - `multivector_config` (one of several types) — Configuration for multi-vector points (e.g., ColBERT)
    - `comparator` (string, required) — Allowed values: `max_sim`.
  - `datatype` (one of several types) — Element storage type (Float32, Float16, Uint8, Turbo4, Turbo8, Turbo16)
- `sparse` (object, required) — Configuration for creating a new sparse named vector. Only includes properties that define the vector space and cannot be changed after creation.
  - `modifier` (one of several types) — Value modifier for sparse vectors (e.g., IDF)
  - `datatype` (one of several types) — Datatype used to store weights in the index

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### DELETE /collections/{collection_name}/vectors/{vector_name}

**Delete named vector**

Delete a named vector from a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `vector_name` | path | string | Yes | Name of the vector to delete |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### GET /collections/{collection_name}/optimizations

**Get optimization progress**

Get progress of ongoing and completed optimizations for a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `with` | query | string | No | Comma-separated list of optional fields to include in the response. Possible values: queued, completed, idle_segments. |
| `completed_limit` | query | integer | No | Maximum number of completed optimizations to return. Ignored if `completed` is not in the `with` parameter. Default: `16`. Minimum: 0. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object) — Optimizations progress for the collection
    - `summary` (object, required)
      - `queued_optimizations` (integer (uint), required) — Number of pending optimizations in the queue. Each optimization will take one or more unoptimized segments and produce one optimized segment. Minimum: 0.
      - `queued_segments` (integer (uint), required) — Number of unoptimized segments in the queue. Minimum: 0.
      - `queued_points` (integer (uint), required) — Number of points in unoptimized segments in the queue. Minimum: 0.
      - `idle_segments` (integer (uint), required) — Number of segments that don't require optimization. Minimum: 0.
    - `running` (array of object, required) — Currently running optimizations.
      - `uuid` (string (uuid), required) — Unique identifier of the optimization process. After the optimization is complete, a new segment will be created with this UUID.
      - `optimizer` (string, required) — Name of the optimizer that performed this optimization.
      - `status` (one of several types, required) — Represents the current state of the optimizer being tracked
        - `cancelled` (string, required)
        - `error` (string, required)
      - `segments` (array of object, required) — Segments being optimized. After the optimization is complete, these segments will be replaced by the new optimized segment.
        - `uuid` (string (uuid), required) — Unique identifier of the segment.
        - `points_count` (integer (uint), required) — Number of non-deleted points in the segment. Minimum: 0.
      - `progress` (object, required)
        - `name` (string, required) — Name of the operation.
        - `started_at` (string (date-time)) — When the operation started. May be null.
        - `finished_at` (string (date-time)) — When the operation finished. May be null.
        - `duration_sec` (number (double)) — For finished operations, how long they took, in seconds. May be null.
        - `done` (integer (uint64)) — Number of completed units of work, if applicable. Minimum: 0. May be null.
        - `total` (integer (uint64)) — Total number of units of work, if applicable and known. Minimum: 0. May be null.
        - `children` (array of any) — Child operations.
    - `queued` (array of object) — An estimated queue of pending optimizations. Requires `?with=queued`. May be null.
      - `optimizer` (string, required) — Name of the optimizer that scheduled this optimization.
      - `segments` (array of object, required) — Segments that will be optimized.
        - `uuid` (string (uuid), required) — Unique identifier of the segment.
        - `points_count` (integer (uint), required) — Number of non-deleted points in the segment. Minimum: 0.
    - `completed` (array of object) — Completed optimizations. Requires `?with=completed`. Limited by `?completed_limit=N`. May be null.
      - `uuid` (string (uuid), required) — Unique identifier of the optimization process. After the optimization is complete, a new segment will be created with this UUID.
      - `optimizer` (string, required) — Name of the optimizer that performed this optimization.
      - `status` (one of several types, required) — Represents the current state of the optimizer being tracked
        - `cancelled` (string, required)
        - `error` (string, required)
      - `segments` (array of object, required) — Segments being optimized. After the optimization is complete, these segments will be replaced by the new optimized segment.
        - `uuid` (string (uuid), required) — Unique identifier of the segment.
        - `points_count` (integer (uint), required) — Number of non-deleted points in the segment. Minimum: 0.
      - `progress` (object, required)
        - `name` (string, required) — Name of the operation.
        - `started_at` (string (date-time)) — When the operation started. May be null.
        - `finished_at` (string (date-time)) — When the operation finished. May be null.
        - `duration_sec` (number (double)) — For finished operations, how long they took, in seconds. May be null.
        - `done` (integer (uint64)) — Number of completed units of work, if applicable. Minimum: 0. May be null.
        - `total` (integer (uint64)) — Total number of units of work, if applicable and known. Minimum: 0. May be null.
        - `children` (array of any) — Child operations.
    - `idle_segments` (array of object) — Segments that don't require optimization. Requires `?with=idle_segments`. May be null.
      - `uuid` (string (uuid), required) — Unique identifier of the segment.
      - `points_count` (integer (uint), required) — Number of non-deleted points in the segment. Minimum: 0.

## Aliases

Additional names for existing collections.

### POST /collections/aliases

**Update aliases of the collections**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `timeout` | query | integer | No | Wait for operation commit timeout in seconds. If timeout is reached - request will return with service error. Minimum: 1. |

**Request body** (`application/json`)

Alias update operations

- `actions` (array of one of several types, required)
  - `create_alias` (object, required) — Create alternative name for a collection. Collection will be available under both names for search, retrieve,
    - `collection_name` (string, required)
    - `alias_name` (string, required)
  - `delete_alias` (object, required) — Delete alias if exists
    - `alias_name` (string, required)
  - `rename_alias` (object, required) — Change alias to a new one
    - `old_alias_name` (string, required)
    - `new_alias_name` (string, required)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)

### GET /collections/{collection_name}/aliases

**List aliases for collection**

Get list of all aliases for a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `aliases` (array of object, required)
      - `alias_name` (string, required)
      - `collection_name` (string, required)

### GET /aliases

**List collections aliases**

Get list of all existing collections aliases

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `aliases` (array of object, required)
      - `alias_name` (string, required)
      - `collection_name` (string, required)

## Indexes

Indexes for payloads associated with points.

### PUT /collections/{collection_name}/index

**Create index for field in collection**

Create index for field in collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

Field name

- `field_name` (string, required)
- `field_schema` (one of several types)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### DELETE /collections/{collection_name}/index/{field_name}

**Delete index for field in collection**

Delete field index for collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `field_name` | path | string | Yes | Name of the field where to delete the index |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

## Snapshots

Storage and collections snapshots.

### POST /collections/{collection_name}/snapshots/upload

**Recover from an uploaded snapshot**

Recover local collection data from an uploaded snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |
| `priority` | query | string | No | Defines source of truth for snapshot recovery. Allowed values: `no_sync`, `snapshot`, `replica`. |
| `checksum` | query | string | No | Optional SHA256 checksum to verify snapshot integrity before recovery. |

**Request body** (`multipart/form-data`)

Snapshot to recover from

- `snapshot` (string (binary))

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### PUT /collections/{collection_name}/snapshots/recover

**Recover from a snapshot**

Recover local collection data from a snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |

**Request body** (`application/json`)

Snapshot to recover from

- `location` (string (uri), required) — Examples: - URL `http://localhost:8080/collections/my_collection/snapshots/my_snapshot` - Local path `file:///qdrant/snapshots/test_collection-2022-08-04-10-49-10.snapshot`
- `priority` (one of several types) — Defines which data should be used as a source of truth if there are other replicas in the cluster. If set to `Snapshot`, the snapshot will be used as a source of truth, and the current state will be overwritten. If set to `Replica`, the current state will be used as a source of truth, and after recovery it will be synchronized from other replicas. Default: `None`.
- `checksum` (string) — Optional SHA256 checksum to verify snapshot integrity before recovery. Default: `None`. May be null.
- `api_key` (string) — Optional API key used when fetching the snapshot from a remote URL. Default: `None`. May be null.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### GET /collections/{collection_name}/snapshots

**List collection snapshots**

Get list of snapshots for a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (array of object)
    - `name` (string, required)
    - `creation_time` (string (partial-date-time)) — May be null.
    - `size` (integer (uint64), required) — Minimum: 0.
    - `checksum` (string) — May be null.

### POST /collections/{collection_name}/snapshots

**Create collection snapshot**

Create new snapshot for a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection for which to create a snapshot |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `name` (string, required)
    - `creation_time` (string (partial-date-time)) — May be null.
    - `size` (integer (uint64), required) — Minimum: 0.
    - `checksum` (string) — May be null.
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### GET /collections/{collection_name}/snapshots/{snapshot_name}

**Download collection snapshot**

Download specified snapshot from a collection as a file

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `snapshot_name` | path | string | Yes | Name of the snapshot to download |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — Snapshot file

### DELETE /collections/{collection_name}/snapshots/{snapshot_name}

**Delete collection snapshot**

Delete snapshot for a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection for which to delete a snapshot |
| `snapshot_name` | path | string | Yes | Name of the snapshot to delete |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### GET /snapshots

**List of storage snapshots**

Get list of snapshots of the whole storage

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (array of object)
    - `name` (string, required)
    - `creation_time` (string (partial-date-time)) — May be null.
    - `size` (integer (uint64), required) — Minimum: 0.
    - `checksum` (string) — May be null.

### POST /snapshots

**Create storage snapshot**

Create new snapshot of the whole storage

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `name` (string, required)
    - `creation_time` (string (partial-date-time)) — May be null.
    - `size` (integer (uint64), required) — Minimum: 0.
    - `checksum` (string) — May be null.
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### GET /snapshots/{snapshot_name}

**Download storage snapshot**

Download specified snapshot of the whole storage as a file

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `snapshot_name` | path | string | Yes | Name of the snapshot to download |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — Snapshot file

### DELETE /snapshots/{snapshot_name}

**Delete storage snapshot**

Delete snapshot of the whole storage

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `snapshot_name` | path | string | Yes | Name of the full snapshot to delete |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### GET /collections/{collection_name}/shards/{shard_id}/snapshot

**Download shard snapshot**

Stream the current state of a shard as a snapshot file

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `shard_id` | path | integer | Yes | Id of the shard |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — Snapshot file

### POST /collections/{collection_name}/shards/{shard_id}/snapshots/upload

**Recover shard from an uploaded snapshot**

Recover shard of a local collection from an uploaded snapshot. This will overwrite any data, stored on this node, for the collection shard.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `shard_id` | path | integer | Yes | Id of the shard to recover |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |
| `priority` | query | string | No | Defines source of truth for snapshot recovery. Allowed values: `no_sync`, `snapshot`, `replica`. |
| `checksum` | query | string | No | Optional SHA256 checksum to verify snapshot integrity before recovery. |

**Request body** (`multipart/form-data`)

Snapshot to recover from

- `snapshot` (string (binary))

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### PUT /collections/{collection_name}/shards/{shard_id}/snapshots/recover

**Recover from a snapshot**

Recover shard of a local collection data from a snapshot. This will overwrite any data, stored in this shard, for the collection.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `shard_id` | path | integer | Yes | Id of the shard to recover |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |

**Request body** (`application/json`)

Snapshot to recover from

- `location` (one of several types, required)
- `priority` (one of several types) — Default: `None`.
- `checksum` (string) — Optional SHA256 checksum to verify snapshot integrity before recovery. Default: `None`. May be null.
- `api_key` (string) — Optional API key used when fetching the snapshot from a remote URL. Default: `None`. May be null.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### GET /collections/{collection_name}/shards/{shard_id}/snapshots

**List shards snapshots for a collection**

Get list of snapshots for a shard of a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `shard_id` | path | integer | Yes | Id of the shard |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (array of object)
    - `name` (string, required)
    - `creation_time` (string (partial-date-time)) — May be null.
    - `size` (integer (uint64), required) — Minimum: 0.
    - `checksum` (string) — May be null.

### POST /collections/{collection_name}/shards/{shard_id}/snapshots

**Create shard snapshot**

Create new snapshot of a shard for a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection for which to create a snapshot |
| `shard_id` | path | integer | Yes | Id of the shard |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `name` (string, required)
    - `creation_time` (string (partial-date-time)) — May be null.
    - `size` (integer (uint64), required) — Minimum: 0.
    - `checksum` (string) — May be null.
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

### GET /collections/{collection_name}/shards/{shard_id}/snapshots/{snapshot_name}

**Download collection snapshot**

Download specified snapshot of a shard from a collection as a file

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection |
| `shard_id` | path | integer | Yes | Id of the shard |
| `snapshot_name` | path | string | Yes | Name of the snapshot to download |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — Snapshot file

### DELETE /collections/{collection_name}/shards/{shard_id}/snapshots/{snapshot_name}

**Delete shard snapshot**

Delete snapshot of a shard for a collection

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection for which to delete a snapshot |
| `shard_id` | path | integer | Yes | Id of the shard |
| `snapshot_name` | path | string | Yes | Name of the snapshot to delete |
| `wait` | query | boolean | No | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (boolean)
- **202** — operation is accepted
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)

## Points

Float-point vectors with payload.

### GET /collections/{collection_name}/points/{id}

**Get point**

Retrieve full information of single point by id

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to retrieve from |
| `id` | path | one of several types | Yes | Id of the point |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object) — Point data
    - `id` (one of several types, required) — Type, used for specifying point ID in user interface
    - `payload` (one of several types) — Payload - values assigned to the point
    - `vector` (one of several types) — Vector of the point
    - `shard_key` (one of several types) — Shard Key
    - `order_value` (one of several types)

### PUT /collections/{collection_name}/points

**Upsert points**

Perform insert + updates on points. If point with given ID already exists - it will be overwritten.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to update from |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

Operation to perform on points

- `batch` (object, required)
  - `ids` (array of one of several types, required)
  - `vectors` (one of several types, required)
  - `payloads` (array of one of several types) — May be null.
- `shard_key` (one of several types)
- `update_filter` (one of several types) — Filter to apply when updating existing points. Only points matching this filter will be updated. Points that don't match will keep their current state. New points will be inserted regardless of the filter.
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `update_mode` (one of several types) — Mode of the upsert operation: insert_only, upsert (default), update_only
- `points` (array of object, required)
  - `id` (one of several types, required) — Type, used for specifying point ID in user interface
  - `vector` (one of several types, required) — Full vector data per point separator with single and multiple vector modes
    - `text` (string, required) — Text of the document. This field will be used as input for the embedding model.
    - `model` (string, required) — Name of the model used to generate the vector. List of available models depends on a provider. Min length: 1.
    - `options` (one of several types) — Additional options for the model, will be passed to the inference service as-is. See model cards for available options.
    - `image` (any, required) — Image data: base64 encoded image or an URL
    - `model` (string, required) — Name of the model used to generate the vector. List of available models depends on a provider. Min length: 1.
    - `options` (object) — Parameters for the model Values of the parameters are model-specific. May be null.
    - `object` (any, required) — Arbitrary data, used as input for the embedding model. Used if the model requires more than one input or a custom input.
    - `model` (string, required) — Name of the model used to generate the vector. List of available models depends on a provider. Min length: 1.
    - `options` (object) — Parameters for the model Values of the parameters are model-specific. May be null.
  - `payload` (one of several types) — Payload values (optional)
- `shard_key` (one of several types)
- `update_filter` (one of several types) — Filter to apply when updating existing points. Only points matching this filter will be updated. Points that don't match will keep their current state. New points will be inserted regardless of the filter.
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `update_mode` (one of several types) — Mode of the upsert operation: insert_only, upsert (default), update_only

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### POST /collections/{collection_name}/points

**Get points**

Retrieve multiple points by specified IDs

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to retrieve from |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

List of points to retrieve

- `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
- `ids` (array of one of several types, required) — Look for points with ids
- `with_payload` (one of several types) — Select which payload to return with the response. Default is true.
- `with_vector` (one of several types) — Options for specifying which vector to include

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (array of object)
    - `id` (one of several types, required) — Type, used for specifying point ID in user interface
    - `payload` (one of several types) — Payload - values assigned to the point
    - `vector` (one of several types) — Vector of the point
    - `shard_key` (one of several types) — Shard Key
    - `order_value` (one of several types)

### POST /collections/{collection_name}/points/delete

**Delete points**

Delete points

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to delete from |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

Operation to perform on points

- `points` (array of one of several types, required)
- `shard_key` (one of several types)
- `filter` (object, required)
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `shard_key` (one of several types)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### PUT /collections/{collection_name}/points/vectors

**Update vectors**

Update specified named vectors on points, keep unspecified vectors intact.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to update from |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

Update named vectors on points

- `points` (array of object, required) — Points with named vectors. Min items: 1.
  - `id` (one of several types, required) — Type, used for specifying point ID in user interface
  - `vector` (one of several types, required) — Full vector data per point separator with single and multiple vector modes
    - `text` (string, required) — Text of the document. This field will be used as input for the embedding model.
    - `model` (string, required) — Name of the model used to generate the vector. List of available models depends on a provider. Min length: 1.
    - `options` (one of several types) — Additional options for the model, will be passed to the inference service as-is. See model cards for available options.
    - `image` (any, required) — Image data: base64 encoded image or an URL
    - `model` (string, required) — Name of the model used to generate the vector. List of available models depends on a provider. Min length: 1.
    - `options` (object) — Parameters for the model Values of the parameters are model-specific. May be null.
    - `object` (any, required) — Arbitrary data, used as input for the embedding model. Used if the model requires more than one input or a custom input.
    - `model` (string, required) — Name of the model used to generate the vector. List of available models depends on a provider. Min length: 1.
    - `options` (object) — Parameters for the model Values of the parameters are model-specific. May be null.
- `shard_key` (one of several types)
- `update_filter` (one of several types)
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### POST /collections/{collection_name}/points/vectors/delete

**Delete vectors**

Delete named vectors from the given points.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to delete from |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

Delete named vectors from points

- `points` (array of one of several types) — Deletes values from each point in this list. May be null.
- `filter` (one of several types) — Deletes values from points that satisfy this filter condition
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `vector` (array of string, required) — Vector names. Min items: 1. Items must be unique.
- `shard_key` (one of several types)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### PUT /collections/{collection_name}/points/payload

**Overwrite payload**

Replace full payload of points with new one

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to set from |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

Payload and points selector

- `payload` (object, required)
- `points` (array of one of several types) — Assigns payload to each point in this list. May be null.
- `filter` (one of several types) — Assigns payload to each point that satisfy this filter condition
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `shard_key` (one of several types)
- `key` (string) — Assigns payload to each point that satisfy this path of property. May be null.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### POST /collections/{collection_name}/points/payload

**Set payload**

Set payload values for points

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to set from |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

Set payload on points

- `payload` (object, required)
- `points` (array of one of several types) — Assigns payload to each point in this list. May be null.
- `filter` (one of several types) — Assigns payload to each point that satisfy this filter condition
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `shard_key` (one of several types)
- `key` (string) — Assigns payload to each point that satisfy this path of property. May be null.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### POST /collections/{collection_name}/points/payload/delete

**Delete payload**

Delete specified key payload for points

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to delete from |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

delete payload on points

- `keys` (array of string, required) — List of payload keys to remove from payload
- `points` (array of one of several types) — Deletes values from each point in this list. May be null.
- `filter` (one of several types) — Deletes values from points that satisfy this filter condition
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `shard_key` (one of several types)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### POST /collections/{collection_name}/points/payload/clear

**Clear payload**

Remove all payload for specified points

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to clear payload from |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

clear payload on points

- `points` (array of one of several types, required)
- `shard_key` (one of several types)
- `filter` (object, required)
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `shard_key` (one of several types)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### POST /collections/{collection_name}/points/batch

**Batch update points**

Apply a series of update operations for points, vectors and payloads

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to apply operations on |
| `wait` | query | boolean | No | If true, wait for changes to actually happen |
| `ordering` | query | string | No | define ordering guarantees for the operation. Allowed values: `weak`, `medium`, `strong`. |
| `timeout` | query | integer | No | Timeout for the operation. Minimum: 1. |

**Request body** (`application/json`)

update operations

- `operations` (array of one of several types, required)
  - `upsert` (one of several types, required)
    - `batch` (object, required)
      - `ids` (array of one of several types, required)
      - `vectors` (one of several types, required)
      - `payloads` (array of one of several types) — May be null.
    - `shard_key` (one of several types)
    - `update_filter` (one of several types) — Filter to apply when updating existing points. Only points matching this filter will be updated. Points that don't match will keep their current state. New points will be inserted regardless of the filter.
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `update_mode` (one of several types) — Mode of the upsert operation: insert_only, upsert (default), update_only
    - `points` (array of object, required)
      - `id` (one of several types, required) — Type, used for specifying point ID in user interface
      - `vector` (one of several types, required) — Full vector data per point separator with single and multiple vector modes
      - `payload` (one of several types) — Payload values (optional)
    - `shard_key` (one of several types)
    - `update_filter` (one of several types) — Filter to apply when updating existing points. Only points matching this filter will be updated. Points that don't match will keep their current state. New points will be inserted regardless of the filter.
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `update_mode` (one of several types) — Mode of the upsert operation: insert_only, upsert (default), update_only
  - `delete` (one of several types, required)
    - `points` (array of one of several types, required)
    - `shard_key` (one of several types)
    - `filter` (object, required)
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `shard_key` (one of several types)
  - `set_payload` (object, required) — This data structure is used in API interface and applied across multiple shards
    - `payload` (object, required)
    - `points` (array of one of several types) — Assigns payload to each point in this list. May be null.
    - `filter` (one of several types) — Assigns payload to each point that satisfy this filter condition
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `shard_key` (one of several types)
    - `key` (string) — Assigns payload to each point that satisfy this path of property. May be null.
  - `overwrite_payload` (object, required) — This data structure is used in API interface and applied across multiple shards
    - `payload` (object, required)
    - `points` (array of one of several types) — Assigns payload to each point in this list. May be null.
    - `filter` (one of several types) — Assigns payload to each point that satisfy this filter condition
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `shard_key` (one of several types)
    - `key` (string) — Assigns payload to each point that satisfy this path of property. May be null.
  - `delete_payload` (object, required) — This data structure is used in API interface and applied across multiple shards
    - `keys` (array of string, required) — List of payload keys to remove from payload
    - `points` (array of one of several types) — Deletes values from each point in this list. May be null.
    - `filter` (one of several types) — Deletes values from points that satisfy this filter condition
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `shard_key` (one of several types)
  - `clear_payload` (one of several types, required)
    - `points` (array of one of several types, required)
    - `shard_key` (one of several types)
    - `filter` (object, required)
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `shard_key` (one of several types)
  - `update_vectors` (object, required)
    - `points` (array of object, required) — Points with named vectors. Min items: 1.
      - `id` (one of several types, required) — Type, used for specifying point ID in user interface
      - `vector` (one of several types, required) — Full vector data per point separator with single and multiple vector modes
    - `shard_key` (one of several types)
    - `update_filter` (one of several types)
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
  - `delete_vectors` (object, required)
    - `points` (array of one of several types) — Deletes values from each point in this list. May be null.
    - `filter` (one of several types) — Deletes values from points that satisfy this filter condition
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `vector` (array of string, required) — Vector names. Min items: 1. Items must be unique.
    - `shard_key` (one of several types)

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (array of object)
    - `operation_id` (integer (uint64)) — Sequential number of the operation. Minimum: 0. May be null.
    - `status` (string, required) — `Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual. `WaitTimeout` - Request is waiting for timeout. Allowed values: `acknowledged`, `completed`, `wait_timeout`.

### POST /collections/{collection_name}/points/scroll

**Scroll points**

Scroll request - paginate over all points which matches given filtering condition

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to retrieve from |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

Pagination and filter parameters

- `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
- `offset` (one of several types) — Start ID to read points from.
- `limit` (integer (uint)) — Page size. Default: 10. Minimum: 1. May be null.
- `filter` (one of several types) — Look only for points which satisfies this conditions. If not provided - all points.
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `with_payload` (one of several types) — Select which payload to return with the response. Default is true.
- `with_vector` (one of several types) — Options for specifying which vector to include
- `order_by` (one of several types) — Order the records by a payload field.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object) — Result of the points read request
    - `points` (array of object, required) — List of retrieved points
      - `id` (one of several types, required) — Type, used for specifying point ID in user interface
      - `payload` (one of several types) — Payload - values assigned to the point
      - `vector` (one of several types) — Vector of the point
      - `shard_key` (one of several types) — Shard Key
      - `order_value` (one of several types)
    - `next_page_offset` (one of several types) — Offset which should be used to retrieve a next page result

### POST /collections/{collection_name}/points/count

**Count points**

Count points which matches given filtering condition

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to count in |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

Request counts of points which matches given filtering condition

- `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
- `filter` (one of several types) — Look only for points which satisfies this conditions
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `exact` (boolean) — If true, count exact number of points. If false, count approximate number of points faster. Approximate count might be unreliable during the indexing process. Default: true. Default: `true`.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `count` (integer (uint), required) — Number of points which satisfy the conditions. Minimum: 0.

### POST /collections/{collection_name}/facet

**Facet a payload key with a given filter.**

Count points that satisfy the given filter for each unique value of a payload key.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to facet in |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

Request counts of points for each unique value of a payload key

- `shard_key` (one of several types)
- `key` (string, required) — Payload key to use for faceting.
- `limit` (integer (uint)) — Max number of hits to return. Default is 10. Minimum: 1. May be null.
- `filter` (one of several types) — Filter conditions - only consider points that satisfy these conditions.
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `exact` (boolean) — Whether to do a more expensive exact count for each of the values in the facet. Default is false. May be null.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `hits` (array of object, required)
      - `value` (one of several types, required)
      - `count` (integer (uint), required) — Minimum: 0.

## Search

Find points in a collection.

### POST /collections/{collection_name}/points/query

**Query points**

Universally query points. This endpoint covers all capabilities of search, recommend, discover, filters. But also enables hybrid and multi-stage queries.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to query |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

Describes the query to make to the collection

- `shard_key` (one of several types)
- `prefetch` (one of several types) — Sub-requests to perform first. If present, the query will be performed on the results of the prefetch(es). Default: `None`.
  - `prefetch` (one of several types) — Sub-requests to perform first. If present, the query will be performed on the results of the prefetches. Default: `None`.
  - `query` (one of several types) — Query to perform. If missing without prefetches, returns points ordered by their IDs.
  - `using` (string) — Define which vector name to use for querying. If missing, the default vector is used. For a `text` query, the payload field whose text index to search. May be null.
  - `filter` (one of several types) — Filter conditions - return only those points that satisfy the specified conditions.
    - `should` (one of several types) — At least one of those conditions should match
    - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `conditions` (array of one of several types, required)
      - `min_count` (integer (uint), required) — Minimum: 1.
    - `must` (one of several types) — All conditions must match
    - `must_not` (one of several types) — All conditions must NOT match
  - `params` (one of several types) — Search params for when there is no prefetch
    - `hnsw_ef` (integer (uint)) — Params relevant to HNSW index Size of the beam in a beam-search. Larger the value - more accurate the result, more time required for search. Minimum: 1. May be null.
    - `exact` (boolean) — Search without approximation. If set to true, search may run long but with exact results. Default: `false`.
    - `quantization` (one of several types) — Quantization params
      - `ignore` (boolean) — If true, quantized vectors are ignored. Default is false. Default: `false`.
      - `rescore` (boolean) — If true, use original vectors to re-score top-k results. Might require more time in case if original vectors are stored on disk. If not set, qdrant decides automatically apply rescoring or not. May be null.
      - `oversampling` (number (double)) — Oversampling factor for quantization. Default is 1.0. Defines how many extra vectors should be preselected using quantized index, and then re-scored using original vectors. For example, if `oversampling` is 2.4 and `limit` is 100, then 240 vectors will be preselected using quantized index, and then top-100 will be returned after re-scoring. Minimum: 1. May be null.
    - `indexed_only` (boolean) — If enabled, the engine will only perform search among indexed or small segments. Using this option prevents slow searches in case of delayed index, but does not guarantee that all uploaded vectors will be included in search results. Default: `false`.
    - `acorn` (one of several types) — ACORN search params
      - `enable` (boolean) — If true, then ACORN may be used for the HNSW search based on filters selectivity. Improves search recall for searches with multiple low-selectivity payload filters, at cost of performance. Default: `false`.
      - `max_selectivity` (number (double)) — Maximum selectivity of filters to enable ACORN. If estimated filters selectivity is higher than this value, ACORN will not be used. Selectivity is estimated as: `estimated number of points satisfying the filters / total number of points`. 0.0 for never, 1.0 for always. Default is 0.4. Minimum: 0. Maximum: 1. May be null.
    - `idf` (one of several types) — Which population IDF statistics are computed over. By default (or with explicit `"global"`) statistics are collection-wide. Only applicable to sparse vectors with the IDF modifier enabled, and to BM25 over a text index.
  - `score_threshold` (number (float)) — Return points with scores better than this threshold. May be null.
  - `limit` (integer (uint)) — Max number of points to return. Default is 10. Minimum: 1. May be null.
  - `lookup_from` (one of several types) — The location to use for IDs lookup, if not specified - use the current collection and the 'using' vector Note: the other collection vectors should have the same vector size as the 'using' vector in the current collection. Default: `None`.
    - `collection` (string, required) — Name of the collection used for lookup
    - `vector` (string) — Optional name of the vector field within the collection. If not provided, the default vector field will be used. Default: `None`. May be null.
    - `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
- `query` (one of several types) — Query to perform. If missing without prefetches, returns points ordered by their IDs.
- `using` (string) — Define which vector name to use for querying. If missing, the default vector is used. For a `text` query, the payload field whose text index to search. May be null.
- `filter` (one of several types) — Filter conditions - return only those points that satisfy the specified conditions.
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `params` (one of several types) — Search params for when there is no prefetch
  - `hnsw_ef` (integer (uint)) — Params relevant to HNSW index Size of the beam in a beam-search. Larger the value - more accurate the result, more time required for search. Minimum: 1. May be null.
  - `exact` (boolean) — Search without approximation. If set to true, search may run long but with exact results. Default: `false`.
  - `quantization` (one of several types) — Quantization params
    - `ignore` (boolean) — If true, quantized vectors are ignored. Default is false. Default: `false`.
    - `rescore` (boolean) — If true, use original vectors to re-score top-k results. Might require more time in case if original vectors are stored on disk. If not set, qdrant decides automatically apply rescoring or not. May be null.
    - `oversampling` (number (double)) — Oversampling factor for quantization. Default is 1.0. Defines how many extra vectors should be preselected using quantized index, and then re-scored using original vectors. For example, if `oversampling` is 2.4 and `limit` is 100, then 240 vectors will be preselected using quantized index, and then top-100 will be returned after re-scoring. Minimum: 1. May be null.
  - `indexed_only` (boolean) — If enabled, the engine will only perform search among indexed or small segments. Using this option prevents slow searches in case of delayed index, but does not guarantee that all uploaded vectors will be included in search results. Default: `false`.
  - `acorn` (one of several types) — ACORN search params
    - `enable` (boolean) — If true, then ACORN may be used for the HNSW search based on filters selectivity. Improves search recall for searches with multiple low-selectivity payload filters, at cost of performance. Default: `false`.
    - `max_selectivity` (number (double)) — Maximum selectivity of filters to enable ACORN. If estimated filters selectivity is higher than this value, ACORN will not be used. Selectivity is estimated as: `estimated number of points satisfying the filters / total number of points`. 0.0 for never, 1.0 for always. Default is 0.4. Minimum: 0. Maximum: 1. May be null.
  - `idf` (one of several types) — Which population IDF statistics are computed over. By default (or with explicit `"global"`) statistics are collection-wide. Only applicable to sparse vectors with the IDF modifier enabled, and to BM25 over a text index.
- `score_threshold` (number (float)) — Return points with scores better than this threshold. May be null.
- `limit` (integer (uint)) — Max number of points to return. Default is 10. Minimum: 1. May be null.
- `offset` (integer (uint)) — Offset of the result. Skip this many points. Default is 0. Minimum: 0. May be null.
- `with_vector` (one of several types) — Options for specifying which vectors to include into the response. Default is false.
- `with_payload` (one of several types) — Options for specifying which payload to include or not. Default is false.
- `lookup_from` (one of several types) — The location to use for IDs lookup, if not specified - use the current collection and the 'using' vector Note: the other collection vectors should have the same vector size as the 'using' vector in the current collection. Default: `None`.
  - `collection` (string, required) — Name of the collection used for lookup
  - `vector` (string) — Optional name of the vector field within the collection. If not provided, the default vector field will be used. Default: `None`. May be null.
  - `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `points` (array of object, required)
      - `id` (one of several types, required) — Type, used for specifying point ID in user interface
      - `version` (integer (uint64), required) — Point version. Minimum: 0.
      - `score` (number (float), required) — Points vector distance to the query vector
      - `payload` (one of several types) — Payload - values assigned to the point
      - `vector` (one of several types) — Vector of the point
      - `shard_key` (one of several types) — Shard Key
      - `order_value` (one of several types) — Order-by value

### POST /collections/{collection_name}/points/query/batch

**Query points in batch**

Universally query points in batch. This endpoint covers all capabilities of search, recommend, discover, filters. But also enables hybrid and multi-stage queries.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to query |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

Describes the queries to make to the collection

- `searches` (array of object, required)
  - `shard_key` (one of several types)
  - `prefetch` (one of several types) — Sub-requests to perform first. If present, the query will be performed on the results of the prefetch(es). Default: `None`.
    - `prefetch` (one of several types) — Sub-requests to perform first. If present, the query will be performed on the results of the prefetches. Default: `None`.
    - `query` (one of several types) — Query to perform. If missing without prefetches, returns points ordered by their IDs.
    - `using` (string) — Define which vector name to use for querying. If missing, the default vector is used. For a `text` query, the payload field whose text index to search. May be null.
    - `filter` (one of several types) — Filter conditions - return only those points that satisfy the specified conditions.
      - `should` (one of several types) — At least one of those conditions should match
      - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `must` (one of several types) — All conditions must match
      - `must_not` (one of several types) — All conditions must NOT match
    - `params` (one of several types) — Search params for when there is no prefetch
      - `hnsw_ef` (integer (uint)) — Params relevant to HNSW index Size of the beam in a beam-search. Larger the value - more accurate the result, more time required for search. Minimum: 1. May be null.
      - `exact` (boolean) — Search without approximation. If set to true, search may run long but with exact results. Default: `false`.
      - `quantization` (one of several types) — Quantization params
      - `indexed_only` (boolean) — If enabled, the engine will only perform search among indexed or small segments. Using this option prevents slow searches in case of delayed index, but does not guarantee that all uploaded vectors will be included in search results. Default: `false`.
      - `acorn` (one of several types) — ACORN search params
      - `idf` (one of several types) — Which population IDF statistics are computed over. By default (or with explicit `"global"`) statistics are collection-wide. Only applicable to sparse vectors with the IDF modifier enabled, and to BM25 over a text index.
    - `score_threshold` (number (float)) — Return points with scores better than this threshold. May be null.
    - `limit` (integer (uint)) — Max number of points to return. Default is 10. Minimum: 1. May be null.
    - `lookup_from` (one of several types) — The location to use for IDs lookup, if not specified - use the current collection and the 'using' vector Note: the other collection vectors should have the same vector size as the 'using' vector in the current collection. Default: `None`.
      - `collection` (string, required) — Name of the collection used for lookup
      - `vector` (string) — Optional name of the vector field within the collection. If not provided, the default vector field will be used. Default: `None`. May be null.
      - `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
  - `query` (one of several types) — Query to perform. If missing without prefetches, returns points ordered by their IDs.
  - `using` (string) — Define which vector name to use for querying. If missing, the default vector is used. For a `text` query, the payload field whose text index to search. May be null.
  - `filter` (one of several types) — Filter conditions - return only those points that satisfy the specified conditions.
    - `should` (one of several types) — At least one of those conditions should match
    - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `conditions` (array of one of several types, required)
      - `min_count` (integer (uint), required) — Minimum: 1.
    - `must` (one of several types) — All conditions must match
    - `must_not` (one of several types) — All conditions must NOT match
  - `params` (one of several types) — Search params for when there is no prefetch
    - `hnsw_ef` (integer (uint)) — Params relevant to HNSW index Size of the beam in a beam-search. Larger the value - more accurate the result, more time required for search. Minimum: 1. May be null.
    - `exact` (boolean) — Search without approximation. If set to true, search may run long but with exact results. Default: `false`.
    - `quantization` (one of several types) — Quantization params
      - `ignore` (boolean) — If true, quantized vectors are ignored. Default is false. Default: `false`.
      - `rescore` (boolean) — If true, use original vectors to re-score top-k results. Might require more time in case if original vectors are stored on disk. If not set, qdrant decides automatically apply rescoring or not. May be null.
      - `oversampling` (number (double)) — Oversampling factor for quantization. Default is 1.0. Defines how many extra vectors should be preselected using quantized index, and then re-scored using original vectors. For example, if `oversampling` is 2.4 and `limit` is 100, then 240 vectors will be preselected using quantized index, and then top-100 will be returned after re-scoring. Minimum: 1. May be null.
    - `indexed_only` (boolean) — If enabled, the engine will only perform search among indexed or small segments. Using this option prevents slow searches in case of delayed index, but does not guarantee that all uploaded vectors will be included in search results. Default: `false`.
    - `acorn` (one of several types) — ACORN search params
      - `enable` (boolean) — If true, then ACORN may be used for the HNSW search based on filters selectivity. Improves search recall for searches with multiple low-selectivity payload filters, at cost of performance. Default: `false`.
      - `max_selectivity` (number (double)) — Maximum selectivity of filters to enable ACORN. If estimated filters selectivity is higher than this value, ACORN will not be used. Selectivity is estimated as: `estimated number of points satisfying the filters / total number of points`. 0.0 for never, 1.0 for always. Default is 0.4. Minimum: 0. Maximum: 1. May be null.
    - `idf` (one of several types) — Which population IDF statistics are computed over. By default (or with explicit `"global"`) statistics are collection-wide. Only applicable to sparse vectors with the IDF modifier enabled, and to BM25 over a text index.
  - `score_threshold` (number (float)) — Return points with scores better than this threshold. May be null.
  - `limit` (integer (uint)) — Max number of points to return. Default is 10. Minimum: 1. May be null.
  - `offset` (integer (uint)) — Offset of the result. Skip this many points. Default is 0. Minimum: 0. May be null.
  - `with_vector` (one of several types) — Options for specifying which vectors to include into the response. Default is false.
  - `with_payload` (one of several types) — Options for specifying which payload to include or not. Default is false.
  - `lookup_from` (one of several types) — The location to use for IDs lookup, if not specified - use the current collection and the 'using' vector Note: the other collection vectors should have the same vector size as the 'using' vector in the current collection. Default: `None`.
    - `collection` (string, required) — Name of the collection used for lookup
    - `vector` (string) — Optional name of the vector field within the collection. If not provided, the default vector field will be used. Default: `None`. May be null.
    - `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (array of object)
    - `points` (array of object, required)
      - `id` (one of several types, required) — Type, used for specifying point ID in user interface
      - `version` (integer (uint64), required) — Point version. Minimum: 0.
      - `score` (number (float), required) — Points vector distance to the query vector
      - `payload` (one of several types) — Payload - values assigned to the point
      - `vector` (one of several types) — Vector of the point
      - `shard_key` (one of several types) — Shard Key
      - `order_value` (one of several types) — Order-by value

### POST /collections/{collection_name}/points/query/groups

**Query points, grouped by a given payload field**

Universally query points, grouped by a given payload field

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to query |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

Describes the query to make to the collection

- `shard_key` (one of several types)
- `prefetch` (one of several types) — Sub-requests to perform first. If present, the query will be performed on the results of the prefetch(es). Default: `None`.
  - `prefetch` (one of several types) — Sub-requests to perform first. If present, the query will be performed on the results of the prefetches. Default: `None`.
  - `query` (one of several types) — Query to perform. If missing without prefetches, returns points ordered by their IDs.
  - `using` (string) — Define which vector name to use for querying. If missing, the default vector is used. For a `text` query, the payload field whose text index to search. May be null.
  - `filter` (one of several types) — Filter conditions - return only those points that satisfy the specified conditions.
    - `should` (one of several types) — At least one of those conditions should match
    - `min_should` (one of several types) — At least minimum amount of given conditions should match
      - `conditions` (array of one of several types, required)
      - `min_count` (integer (uint), required) — Minimum: 1.
    - `must` (one of several types) — All conditions must match
    - `must_not` (one of several types) — All conditions must NOT match
  - `params` (one of several types) — Search params for when there is no prefetch
    - `hnsw_ef` (integer (uint)) — Params relevant to HNSW index Size of the beam in a beam-search. Larger the value - more accurate the result, more time required for search. Minimum: 1. May be null.
    - `exact` (boolean) — Search without approximation. If set to true, search may run long but with exact results. Default: `false`.
    - `quantization` (one of several types) — Quantization params
      - `ignore` (boolean) — If true, quantized vectors are ignored. Default is false. Default: `false`.
      - `rescore` (boolean) — If true, use original vectors to re-score top-k results. Might require more time in case if original vectors are stored on disk. If not set, qdrant decides automatically apply rescoring or not. May be null.
      - `oversampling` (number (double)) — Oversampling factor for quantization. Default is 1.0. Defines how many extra vectors should be preselected using quantized index, and then re-scored using original vectors. For example, if `oversampling` is 2.4 and `limit` is 100, then 240 vectors will be preselected using quantized index, and then top-100 will be returned after re-scoring. Minimum: 1. May be null.
    - `indexed_only` (boolean) — If enabled, the engine will only perform search among indexed or small segments. Using this option prevents slow searches in case of delayed index, but does not guarantee that all uploaded vectors will be included in search results. Default: `false`.
    - `acorn` (one of several types) — ACORN search params
      - `enable` (boolean) — If true, then ACORN may be used for the HNSW search based on filters selectivity. Improves search recall for searches with multiple low-selectivity payload filters, at cost of performance. Default: `false`.
      - `max_selectivity` (number (double)) — Maximum selectivity of filters to enable ACORN. If estimated filters selectivity is higher than this value, ACORN will not be used. Selectivity is estimated as: `estimated number of points satisfying the filters / total number of points`. 0.0 for never, 1.0 for always. Default is 0.4. Minimum: 0. Maximum: 1. May be null.
    - `idf` (one of several types) — Which population IDF statistics are computed over. By default (or with explicit `"global"`) statistics are collection-wide. Only applicable to sparse vectors with the IDF modifier enabled, and to BM25 over a text index.
  - `score_threshold` (number (float)) — Return points with scores better than this threshold. May be null.
  - `limit` (integer (uint)) — Max number of points to return. Default is 10. Minimum: 1. May be null.
  - `lookup_from` (one of several types) — The location to use for IDs lookup, if not specified - use the current collection and the 'using' vector Note: the other collection vectors should have the same vector size as the 'using' vector in the current collection. Default: `None`.
    - `collection` (string, required) — Name of the collection used for lookup
    - `vector` (string) — Optional name of the vector field within the collection. If not provided, the default vector field will be used. Default: `None`. May be null.
    - `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
- `query` (one of several types) — Query to perform. If missing without prefetches, returns points ordered by their IDs.
- `using` (string) — Define which vector name to use for querying. If missing, the default vector is used. For a `text` query, the payload field whose text index to search. May be null.
- `filter` (one of several types) — Filter conditions - return only those points that satisfy the specified conditions.
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `params` (one of several types) — Search params for when there is no prefetch
  - `hnsw_ef` (integer (uint)) — Params relevant to HNSW index Size of the beam in a beam-search. Larger the value - more accurate the result, more time required for search. Minimum: 1. May be null.
  - `exact` (boolean) — Search without approximation. If set to true, search may run long but with exact results. Default: `false`.
  - `quantization` (one of several types) — Quantization params
    - `ignore` (boolean) — If true, quantized vectors are ignored. Default is false. Default: `false`.
    - `rescore` (boolean) — If true, use original vectors to re-score top-k results. Might require more time in case if original vectors are stored on disk. If not set, qdrant decides automatically apply rescoring or not. May be null.
    - `oversampling` (number (double)) — Oversampling factor for quantization. Default is 1.0. Defines how many extra vectors should be preselected using quantized index, and then re-scored using original vectors. For example, if `oversampling` is 2.4 and `limit` is 100, then 240 vectors will be preselected using quantized index, and then top-100 will be returned after re-scoring. Minimum: 1. May be null.
  - `indexed_only` (boolean) — If enabled, the engine will only perform search among indexed or small segments. Using this option prevents slow searches in case of delayed index, but does not guarantee that all uploaded vectors will be included in search results. Default: `false`.
  - `acorn` (one of several types) — ACORN search params
    - `enable` (boolean) — If true, then ACORN may be used for the HNSW search based on filters selectivity. Improves search recall for searches with multiple low-selectivity payload filters, at cost of performance. Default: `false`.
    - `max_selectivity` (number (double)) — Maximum selectivity of filters to enable ACORN. If estimated filters selectivity is higher than this value, ACORN will not be used. Selectivity is estimated as: `estimated number of points satisfying the filters / total number of points`. 0.0 for never, 1.0 for always. Default is 0.4. Minimum: 0. Maximum: 1. May be null.
  - `idf` (one of several types) — Which population IDF statistics are computed over. By default (or with explicit `"global"`) statistics are collection-wide. Only applicable to sparse vectors with the IDF modifier enabled, and to BM25 over a text index.
- `score_threshold` (number (float)) — Return points with scores better than this threshold. May be null.
- `with_vector` (one of several types) — Options for specifying which vectors to include into the response. Default is false.
- `with_payload` (one of several types) — Options for specifying which payload to include or not. Default is false.
- `lookup_from` (one of several types) — The location to use for IDs lookup, if not specified - use the current collection and the 'using' vector Note: the other collection vectors should have the same vector size as the 'using' vector in the current collection. Default: `None`.
  - `collection` (string, required) — Name of the collection used for lookup
  - `vector` (string) — Optional name of the vector field within the collection. If not provided, the default vector field will be used. Default: `None`. May be null.
  - `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
- `group_by` (string, required) — Payload field to group by, must be a string or number field. If the field contains more than 1 value, all values will be used for grouping. One point can be in multiple groups. Min length: 1.
- `group_size` (integer (uint)) — Maximum amount of points to return per group. Default is 3. Minimum: 1. May be null.
- `limit` (integer (uint)) — Maximum amount of groups to return. Default is 10. Minimum: 1. May be null.
- `with_lookup` (one of several types) — Look for points in another collection using the group ids

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `groups` (array of object, required)
      - `hits` (array of object, required) — Scored points that have the same value of the group_by key
        - `id` (one of several types, required) — Type, used for specifying point ID in user interface
        - `version` (integer (uint64), required) — Point version. Minimum: 0.
        - `score` (number (float), required) — Points vector distance to the query vector
        - `payload` (one of several types) — Payload - values assigned to the point
        - `vector` (one of several types) — Vector of the point
        - `shard_key` (one of several types) — Shard Key
        - `order_value` (one of several types) — Order-by value
      - `id` (one of several types, required) — Value of the group_by key, shared across all the hits in the group
      - `lookup` (one of several types) — Record that has been looked up using the group id
        - `id` (one of several types, required) — Type, used for specifying point ID in user interface
        - `payload` (one of several types) — Payload - values assigned to the point
        - `vector` (one of several types) — Vector of the point
        - `shard_key` (one of several types) — Shard Key
        - `order_value` (one of several types)

### POST /collections/{collection_name}/points/search/matrix/pairs

**Search points matrix distance pairs**

Compute distance matrix for sampled points with a pair based output format

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to search in |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

Search matrix request with optional filtering

- `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
- `filter` (one of several types) — Look only for points which satisfies this conditions
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `sample` (integer (uint)) — How many points to select and search within. Default is 10. Minimum: 2. May be null.
- `limit` (integer (uint)) — How many neighbours per sample to find. Default is 3. Minimum: 1. May be null.
- `using` (string) — Define which vector name to use for querying. If missing, the default vector is used. May be null.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `pairs` (array of object, required) — List of pairs of points with scores
      - `a` (one of several types, required) — Type, used for specifying point ID in user interface
      - `b` (one of several types, required) — Type, used for specifying point ID in user interface
      - `score` (number (float), required)

### POST /collections/{collection_name}/points/search/matrix/offsets

**Search points matrix distance offsets**

Compute distance matrix for sampled points with an offset based output format

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `collection_name` | path | string | Yes | Name of the collection to search in |
| `consistency` | query | one of several types | No | Define read consistency guarantees for the operation |
| `timeout` | query | integer | No | If set, overrides global timeout for this request. Unit is seconds. Minimum: 1. |

**Request body** (`application/json`)

Search matrix request with optional filtering

- `shard_key` (one of several types) — Specify in which shards to look for the points, if not specified - look in all shards
- `filter` (one of several types) — Look only for points which satisfies this conditions
  - `should` (one of several types) — At least one of those conditions should match
  - `min_should` (one of several types) — At least minimum amount of given conditions should match
    - `conditions` (array of one of several types, required)
      - `key` (string, required) — Payload key
      - `match` (one of several types) — Check if point has field with a given value
      - `range` (one of several types) — Check if points value lies in a given range
      - `geo_bounding_box` (one of several types) — Check if points geolocation lies in a given area
      - `geo_radius` (one of several types) — Check if geo point is within a given radius
      - `geo_polygon` (one of several types) — Check if geo point is within a given polygon
      - `values_count` (one of several types) — Check number of values of the field
      - `is_empty` (boolean) — Check that the field is empty, alternative syntax for `is_empty: "field_name"`. May be null.
      - `is_null` (boolean) — Check that the field is null, alternative syntax for `is_null: "field_name"`. May be null.
      - `is_empty` (object, required) — Payload field
      - `is_null` (object, required) — Payload field
      - `has_id` (array of one of several types, required) — Items must be unique.
      - `has_vector` (string, required)
      - `slice` (object, required) — One of `total` disjoint deterministic slices of the id space. A point belongs to the slice iff `hash(id) % total == index`, where `hash` is SipHash-2-4 with a zero key over the canonical id bytes: 8 little-endian bytes for numeric ids, the 16 RFC 4122 bytes for UUIDs. For a fixed `total`, slices `0..total` are disjoint and together cover all points; membership is uniform regardless of the id scheme and stable across queries, segments, platforms and Qdrant versions. Slices with different `total` values are correlated (same hash, no salt): e.g. slice `0` of `total: 4` is a strict subset of slice `0` of `total: 2`. This keeps a smaller sample contained in a larger one.
      - `nested` (object, required) — Select points with payload for a specified nested field
    - `min_count` (integer (uint), required) — Minimum: 1.
  - `must` (one of several types) — All conditions must match
  - `must_not` (one of several types) — All conditions must NOT match
- `sample` (integer (uint)) — How many points to select and search within. Default is 10. Minimum: 2. May be null.
- `limit` (integer (uint)) — How many neighbours per sample to find. Default is 3. Minimum: 1. May be null.
- `using` (string) — Define which vector name to use for querying. If missing, the default vector is used. May be null.

**Responses**

- **default** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **4XX** — error
  Body (`application/json`, object):
  - `time` (number (float)) — Time spent to process this request
  - `status` (object)
    - `error` (string) — Description of the occurred error.
  - `result` (object) — May be null.
- **200** — successful operation
  Body (`application/json`, object):
  - `usage` (one of several types) — Default: `None`.
    - `hardware` (one of several types)
      - `cpu` (integer (uint), required) — Minimum: 0.
      - `payload_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_io_write` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_read` (integer (uint), required) — Minimum: 0.
      - `payload_index_io_write` (integer (uint), required) — Minimum: 0.
      - `vector_io_read` (integer (uint), required) — Minimum: 0.
      - `vector_io_write` (integer (uint), required) — Minimum: 0.
    - `inference` (one of several types)
      - `models` (object, required)
  - `time` (number (float)) — Time spent to process this request
  - `status` (string)
  - `result` (object)
    - `offsets_row` (array of integer (uint64), required) — Row indices of the matrix
    - `offsets_col` (array of integer (uint64), required) — Column indices of the matrix
    - `scores` (array of number (float), required) — Scores associated with matrix coordinates
    - `ids` (array of one of several types, required) — Ids of the points in order
