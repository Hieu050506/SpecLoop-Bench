# PokéAPI — API Reference

All the Pokémon data you'll ever need in one place, easily accessible through a modern free open-source RESTful API.

## What is this?

This is a full RESTful API linked to an extensive database detailing everything about the Pokémon main game series.

We've covered everything from Pokémon to Berry Flavors.

## Where do I start?

We have awesome [documentation](https://pokeapi.co/docs/v2) on how to use this API. It takes minutes to get started.

This API will always be publicly available and will never require any extensive setup process to consume.

Created by [**Paul Hallett**](https://github.com/phalt) and other [**PokéAPI contributors**](https://github.com/PokeAPI/pokeapi#contributing) around the world. Pokémon and Pokémon character names are trademarks of Nintendo.

**Version:** 2.10.0  
**Base URL:** `https://pokeapi.co`

## utility

### GET /api/v2/meta/

**Get API metadata**

Returns metadata about the current deployed version of the API, including the git commit hash, deploy date, and tag (if any).

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `deploy_date` (string, required) — May be null.
  - `hash` (string, required) — May be null.
  - `tag` (string, required) — May be null.

### GET /api/v2/language/

**List languages**

Languages for translations of API resource information.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/language/{id}/

**Get language**

Languages for translations of API resource information.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `official` (boolean)
  - `iso639` (string, required) — Max length: 10.
  - `iso3166` (string, required) — Max length: 2.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

## pokemon

Pokémon are the creatures that inhabit the world of the Pokémon games. They can be caught using Pokéballs and trained by battling with other Pokémon. Each Pokémon belongs to a specific species but may take on a variant which makes it differ from other Pokémon of the same species, such as base stats, available abilities and typings. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_(species)) for greater detail.

### GET /api/v2/ability/

**List abilities**

Abilities provide passive effects for Pokémon in battle or in the overworld. Pokémon have multiple possible abilities but can have only one ability at a time. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Ability) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/ability/{id}/

**Get ability**

Abilities provide passive effects for Pokémon in battle or in the overworld. Pokémon have multiple possible abilities but can have only one ability at a time. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Ability) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `is_main_series` (boolean)
  - `generation` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `effect_entries` (array of object, required)
    - `effect` (string, required) — Max length: 6000.
    - `short_effect` (string, required) — Max length: 300.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `effect_changes` (array of object, required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `effect_entries` (array of object, required)
      - `effect` (string, required) — Max length: 6000.
      - `language` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `flavor_text_entries` (array of object, required)
    - `flavor_text` (string, required)
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon` (array of object, required)
    - `is_hidden` (boolean)
    - `slot` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `pokemon` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/characteristic/

**List characteristics**

Characteristics indicate which stat contains a Pokémon's highest IV. A Pokémon's Characteristic is determined by the remainder of its highest IV divided by 5 (gene_modulo). Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Characteristic) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `url` (string (uri), required)

### GET /api/v2/characteristic/{id}/

**Get characteristic**

Characteristics indicate which stat contains a Pokémon's highest IV. A Pokémon's Characteristic is determined by the remainder of its highest IV divided by 5 (gene_modulo). Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Characteristic) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `gene_modulo` (integer, required)
  - `possible_values` (array of integer, required)
  - `highest_stat` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/egg-group/

**List egg groups**

Egg Groups are categories which determine which Pokémon are able to interbreed. Pokémon may belong to either one or two Egg Groups. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Egg_Group) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/egg-group/{id}/

**Get egg group**

Egg Groups are categories which determine which Pokémon are able to interbreed. Pokémon may belong to either one or two Egg Groups. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Egg_Group) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_species` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/gender/

**List genders**

Genders were introduced in Generation II for the purposes of breeding Pokémon but can also result in visual differences or even different evolutionary lines. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Gender) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/gender/{id}/

**Get gender**

Genders were introduced in Generation II for the purposes of breeding Pokémon but can also result in visual differences or even different evolutionary lines. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Gender) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `pokemon_species_details` (array of object, required)
    - `rate` (integer, required)
    - `pokemon_species` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `required_for_evolution` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/growth-rate/

**List growth rates**

Growth rates are the speed with which Pokémon gain levels through experience. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Experience) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/growth-rate/{id}/

**Get growth rate**

Growth rates are the speed with which Pokémon gain levels through experience. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Experience) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `formula` (string, required) — Max length: 500.
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `levels` (array of object, required)
    - `level` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `experience` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
  - `pokemon_species` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-damage-class/

**List move damage classes**

Damage classes moves can have, e.g. physical, special, or non-damaging.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-damage-class/{id}/

**Get move damage class**

Damage classes moves can have, e.g. physical, special, or non-damaging.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `moves` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/nature/

**List natures**

Natures influence how a Pokémon's stats grow. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Nature) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/nature/{id}/

**Get nature**

Natures influence how a Pokémon's stats grow. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Nature) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `decreased_stat` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `increased_stat` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `likes_flavor` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `hates_flavor` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `berries` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `pokeathlon_stat_changes` (array of object, required)
    - `max_change` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `pokeathlon_stat` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `move_battle_style_preferences` (array of object, required)
    - `low_hp_preference` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `high_hp_preference` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `move_battle_style` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/pokemon/

**List pokemon**

Pokémon are the creatures that inhabit the world of the Pokémon games. They can be caught using Pokéballs and trained by battling with other Pokémon. Each Pokémon belongs to a specific species but may take on a variant which makes it differ from other Pokémon of the same species, such as base stats, available abilities and typings. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_(species)) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon/{id}/

**Get pokemon**

Pokémon are the creatures that inhabit the world of the Pokémon games. They can be caught using Pokéballs and trained by battling with other Pokémon. Each Pokémon belongs to a specific species but may take on a variant which makes it differ from other Pokémon of the same species, such as base stats, available abilities and typings. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_(species)) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `base_experience` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `height` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `is_default` (boolean)
  - `order` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `weight` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `abilities` (array of object, required)
    - `is_hidden` (boolean)
    - `slot` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `ability` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `past_abilities` (array of object, required)
    - `abilities` (array of object, required)
      - `is_hidden` (boolean)
      - `slot` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `ability` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
    - `generation` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `forms` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `game_indices` (array of object, required)
    - `game_index` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `version` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `held_items` (array of object, required)
    - `pokemon` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_details` (array of object, required)
      - `rarity` (integer, required)
      - `version` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `location_area_encounters` (string, required)
  - `moves` (array of object, required)
    - `move` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_group_details` (array of object, required)
      - `level_learned_at` (integer, required)
      - `move_learn_method` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `version_group` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `order` (integer)
  - `species` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `sprites` (object, required)
    - `front_default` (string, required) — May be null.
  - `cries` (object, required)
    - `latest` (string, required) — May be null.
    - `legacy` (string, required) — May be null.
  - `stats` (array of object, required)
    - `base_stat` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `effort` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `stat` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `past_stats` (array of object, required)
    - `generation` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `stats` (array of object, required)
      - `base_stat` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `effort` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `stat` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `types` (array of object, required)
    - `slot` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `type` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `past_types` (array of object, required)
    - `generation` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `types` (array of object, required)
      - `slot` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `pokemon` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)

### GET /api/v2/pokemon-color/

**List pokemon colors**

Colors used for sorting Pokémon in a Pokédex. The color listed in the Pokédex is usually the color most apparent or covering each Pokémon's body. No orange category exists; Pokémon that are primarily orange are listed as red or brown.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon-color/{id}/

**Get pokemon color**

Colors used for sorting Pokémon in a Pokédex. The color listed in the Pokédex is usually the color most apparent or covering each Pokémon's body. No orange category exists; Pokémon that are primarily orange are listed as red or brown.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_species` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon-form/

**List pokemon forms**

Some Pokémon may appear in one of multiple, visually different forms. These differences are purely cosmetic. For variations within a Pokémon species, which do differ in more than just visuals, the 'Pokémon' entity is used to represent such a variety.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon-form/{id}/

**Get pokemon form**

Some Pokémon may appear in one of multiple, visually different forms. These differences are purely cosmetic. For variations within a Pokémon species, which do differ in more than just visuals, the 'Pokémon' entity is used to represent such a variety.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `order` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `form_order` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `is_default` (boolean)
  - `is_battle_only` (boolean)
  - `is_mega` (boolean)
  - `form_name` (string, required) — Max length: 30.
  - `pokemon` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `sprites` (object, required)
    - `sprites` (any, required)
  - `version_group` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `form_names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `types` (array of object, required)
    - `slot` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `type` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `trigger_conditions` (array of object, required)
    - `trigger` (string, required)
    - `base_form` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `flavor_text_entries` (array of object, required)
    - `flavor_text` (string, required)
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/pokemon-habitat/

**List pokemom habitas**

Habitats are generally different terrain Pokémon can be found in but can also be areas designated for rare or legendary Pokémon.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon-habitat/{id}/

**Get pokemom habita**

Habitats are generally different terrain Pokémon can be found in but can also be areas designated for rare or legendary Pokémon.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_species` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon-shape/

**List pokemon shapes**

Shapes used for sorting Pokémon in a Pokédex.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon-shape/{id}/

**Get pokemon shape**

Shapes used for sorting Pokémon in a Pokédex.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `awesome_names` (array of object, required)
    - `awesome_name` (string, required) — Max length: 30.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_species` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon-species/

**List pokemon species**

A Pokémon Species forms the basis for at least one Pokémon. Attributes of a Pokémon species are shared across all varieties of Pokémon within the species. A good example is Wormadam; Wormadam is the species which can be found in three different varieties, Wormadam-Trash, Wormadam-Sandy and Wormadam-Plant.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokemon-species/{id}/

**Get pokemon species**

A Pokémon Species forms the basis for at least one Pokémon. Attributes of a Pokémon species are shared across all varieties of Pokémon within the species. A good example is Wormadam; Wormadam is the species which can be found in three different varieties, Wormadam-Trash, Wormadam-Sandy and Wormadam-Plant.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `order` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `gender_rate` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `capture_rate` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `base_happiness` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `is_baby` (boolean)
  - `is_legendary` (boolean)
  - `is_mythical` (boolean)
  - `hatch_counter` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `has_gender_differences` (boolean)
  - `forms_switchable` (boolean)
  - `growth_rate` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `pokedex_numbers` (array of object, required)
    - `entry_number` (integer, required)
    - `pokedex` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `egg_groups` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `color` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `shape` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `evolves_from_species` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `evolution_chain` (object, required)
    - `url` (string (uri), required)
  - `habitat` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `generation` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pal_park_encounters` (array of object, required)
    - `base_score` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `rate` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `area` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `form_descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `flavor_text_entries` (array of object, required)
    - `flavor_text` (string, required)
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `genera` (array of object, required)
    - `genus` (string, required) — Max length: 30.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `varieties` (array of object, required)
    - `is_default` (boolean, required)
    - `pokemon` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/pokeathlon-stat/

**List pokeathlon stats**

Pokeathlon Stats are different attributes of a Pokémon's performance in Pokéathlons. In Pokéathlons, competitions happen on different courses; one for each of the different Pokéathlon stats. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9athlon) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokeathlon-stat/{id}/

**Get pokeathlon stat**

Pokeathlon Stats are different attributes of a Pokémon's performance in Pokéathlons. In Pokéathlons, competitions happen on different courses; one for each of the different Pokéathlon stats. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9athlon) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `affecting_natures` (object, required)
    - `increase` (array of object, required)
      - `max_change` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `nature` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
    - `decrease` (array of object, required)
      - `max_change` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `nature` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/stat/

**List stats**

Stats determine certain aspects of battles. Each Pokémon has a value for each stat which grows as they gain levels and can be altered momentarily by effects in battles.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/stat/{id}/

**Get stat**

Stats determine certain aspects of battles. Each Pokémon has a value for each stat which grows as they gain levels and can be altered momentarily by effects in battles.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `game_index` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
  - `is_battle_only` (boolean)
  - `affecting_moves` (object, required)
    - `increase` (array of object, required)
      - `change` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `move` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
    - `decrease` (array of object, required)
      - `change` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
      - `move` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `affecting_natures` (object, required)
    - `increase` (array of object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `decrease` (array of object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `affecting_items` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `characteristics` (array of object, required)
    - `url` (string (uri), required)
  - `move_damage_class` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/type/

**List types**

Types are properties for Pokémon and their moves. Each type has three properties: which types of Pokémon it is super effective against, which types of Pokémon it is not very effective against, and which types of Pokémon it is completely ineffective against.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/type/{id}/

**Get types**

Types are properties for Pokémon and their moves. Each type has three properties: which types of Pokémon it is super effective against, which types of Pokémon it is not very effective against, and which types of Pokémon it is completely ineffective against.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `damage_relations` (object, required)
    - `no_damage_to` (array of object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `half_damage_to` (array of object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `double_damage_to` (array of object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `no_damage_from` (array of object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `half_damage_from` (array of object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `double_damage_from` (array of object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `past_damage_relations` (array of object, required)
    - `generation` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `damage_relations` (object, required)
      - `no_damage_to` (array of object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `half_damage_to` (array of object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `double_damage_to` (array of object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `no_damage_from` (array of object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `half_damage_from` (array of object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `double_damage_from` (array of object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `game_indices` (array of object, required)
    - `game_index` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `generation` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `generation` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `move_damage_class` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon` (array of object, required)
    - `slot` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `pokemon` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `moves` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `sprites` (object, required)
    - `sprites` (any, required)

## berries

Berries can be soft or hard. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Category:Berries_by_firmness) for greater detail.

### GET /api/v2/berry/

**List berries**

Berries are small fruits that can provide HP and status condition restoration, stat enhancement, and even damage negation when eaten by Pokémon. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Berry) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/berry/{id}/

**Get a berry**

Berries are small fruits that can provide HP and status condition restoration, stat enhancement, and even damage negation when eaten by Pokémon. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Berry) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `growth_time` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `max_harvest` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `natural_gift_power` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `size` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `smoothness` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `soil_dryness` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `firmness` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `flavors` (array of object, required)
    - `potency` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `flavor` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `item` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `natural_gift_type` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/berry-firmness/

**List berry firmness**

Berries can be soft or hard. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Category:Berries_by_firmness) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/berry-firmness/{id}/

**Get berry by firmness**

Berries can be soft or hard. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Category:Berries_by_firmness) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `berries` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/berry-flavor/

**List berry flavors**

Flavors determine whether a Pokémon will benefit or suffer from eating a berry based on their **nature**. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Flavor) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/berry-flavor/{id}/

**Get berries by flavor**

Flavors determine whether a Pokémon will benefit or suffer from eating a berry based on their **nature**. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Flavor) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `berries` (array of object, required)
    - `potency` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `berry` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `contest_type` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

## contests

### GET /api/v2/contest-type/

**List contest types**

Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Contest_condition) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/contest-type/{id}/

**Get contest type**

Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Contest_condition) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `berry_flavor` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `color` (string, required) — Max length: 10.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/contest-effect/

**List contest effects**

Contest effects refer to the effects of moves when used in contests.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `url` (string (uri), required)

### GET /api/v2/contest-effect/{id}/

**Get contest effect**

Contest effects refer to the effects of moves when used in contests.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `appeal` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
  - `jam` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
  - `effect_entries` (array of object, required)
    - `effect` (string, required) — Max length: 6000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `flavor_text_entries` (array of object, required)
    - `flavor_text` (string, required) — Max length: 500.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/super-contest-effect/

**List super contest effects**

Super contest effects refer to the effects of moves when used in super contests.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `url` (string (uri), required)

### GET /api/v2/super-contest-effect/{id}/

**Get super contest effect**

Super contest effects refer to the effects of moves when used in super contests.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `appeal` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
  - `flavor_text_entries` (array of object, required)
    - `flavor_text` (string, required) — Max length: 500.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `moves` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

## encounters

### GET /api/v2/encounter-method/

**List encounter methods**

Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall grass. Check out Bulbapedia for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/encounter-method/{id}/

**Get encounter method**

Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall grass. Check out Bulbapedia for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `order` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/encounter-condition/

**List encounter conditions**

Conditions which affect what pokemon might appear in the wild, e.g., day or night.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/encounter-condition/{id}/

**Get encounter condition**

Conditions which affect what pokemon might appear in the wild, e.g., day or night.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `values` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/encounter-condition-value/

**List encounter condition values**

Encounter condition values are the various states that an encounter condition can have, i.e., time of day can be either day or night.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/encounter-condition-value/{id}/

**Get encounter condition value**

Encounter condition values are the various states that an encounter condition can have, i.e., time of day can be either day or night.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `condition` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/pokemon/{pokemon_id}/encounters

**Get pokemon encounter**

Handles Pokemon Encounters as a sub-resource.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `pokemon_id` | path | string | Yes | Pattern: `^\d+$`. |

**Responses**

- **200** — Response
  Body (`application/json`, array of object):
  - `location_area` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `version_details` (array of object, required)
    - `version` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `max_chance` (integer, required)
    - `encounter_details` (array of object, required)
      - `chance` (integer, required)
      - `condition_values` (array of object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `max_level` (integer, required)
      - `method` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `min_level` (integer, required)

## evolution

Evolution is a process in which a Pokémon changes into a different species of Pokémon.

### GET /api/v2/evolution-chain/

**List evolution chains**

Evolution chains are essentially family trees. They start with the lowest stage within a family and detail evolution conditions for each as well as Pokémon they can evolve into up through the hierarchy.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `url` (string (uri), required)

### GET /api/v2/evolution-chain/{id}/

**Get evolution chain**

Evolution chains are essentially family trees. They start with the lowest stage within a family and detail evolution conditions for each as well as Pokémon they can evolve into up through the hierarchy.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `baby_trigger_item` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `chain` (object, required)
    - `is_baby` (boolean, required)
    - `species` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `evolution_details` (array of object, required)
      - `version_group` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `is_default` (boolean)
      - `item` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `trigger` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `gender` (integer) — May be null.
      - `held_item` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `known_move` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `known_move_type` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `location` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `min_level` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
      - `min_happiness` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
      - `min_beauty` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
      - `min_affection` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
      - `near_special_rock` (boolean)
      - `needs_multiplayer` (boolean)
      - `needs_overworld_rain` (boolean)
      - `party_species` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `party_type` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `relative_physical_stats` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
      - `time_of_day` (string) — Max length: 10.
      - `trade_species` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `turn_upside_down` (boolean)
      - `region` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `required_pokemon_form` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `evolved_pokemon_form` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `used_move` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `min_move_count` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
      - `min_steps` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
      - `min_damage_taken` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
      - `allowed_natures` (array of object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `condition_expression` (object, required) — May be null.
        - `expression` (string, required) — Evaluatable RPN condition expression using evolution variables (e.g. 'EC 100 % 0 ==')
        - `percentage_chance` (number (double), required) — Percentage chance of evolution under this condition (0-100). May be null.
        - `variables` (array of object, required) — Evolution variables referenced in the expression
    - `evolves_to` (array of object, required)

### GET /api/v2/evolution-trigger/

**List evolution triggers**

Evolution triggers are the events and conditions that cause a Pokémon to evolve. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Methods_of_evolution) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/evolution-trigger/{id}/

**Get evolution trigger**

Evolution triggers are the events and conditions that cause a Pokémon to evolve. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Methods_of_evolution) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_species` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/evolution-variable/

**List evolution variables**

Evolution variables represent parameters (such as Encryption Constant and Personality Value) used in boolean expressions for form-branching evolutions. Check out [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Personality_value) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/evolution-variable/{id}/

**Get evolution variable**

Evolution variables represent parameters (such as Encryption Constant and Personality Value) used in boolean expressions for form-branching evolutions. Check out [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Personality_value) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `symbol` (string, required) — Max length: 10.
  - `data_type` (string) — Max length: 20.
  - `source` (string) — Where the value comes from: 'pokemon' for data stored on the Pokemon (e.g. EC, PID), 'player-input' for an action taken by the player while evolving (e.g. SPIN_DIR, SPIN_SEC). Max length: 20.
  - `version_group` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

## games

The Pokémon games are all video games in the Pokémon franchise.

### GET /api/v2/generation/

**List genrations**

A generation is a grouping of the Pokémon games that separates them based on the Pokémon they include. In each generation, a new set of Pokémon, Moves, Abilities and Types that did not exist in the previous generation are released.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/generation/{id}/

**Get genration**

A generation is a grouping of the Pokémon games that separates them based on the Pokémon they include. In each generation, a new set of Pokémon, Moves, Abilities and Types that did not exist in the previous generation are released.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `abilities` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `main_region` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `moves` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_species` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `types` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `version_groups` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokedex/

**List pokedex**

A Pokédex is a handheld electronic encyclopedia device; one which is capable of recording and retaining information of the various Pokémon in a given region with the exception of the national dex and some smaller dexes related to portions of a region. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pokedex) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pokedex/{id}/

**Get pokedex**

A Pokédex is a handheld electronic encyclopedia device; one which is capable of recording and retaining information of the various Pokémon in a given region with the exception of the national dex and some smaller dexes related to portions of a region. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pokedex) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `is_main_series` (boolean)
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_entries` (array of object, required)
    - `entry_number` (integer, required)
    - `pokemon_species` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `region` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `version_groups` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/version/

**List versions**

Versions of the games, e.g., Red, Blue or Yellow.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/version/{id}/

**Get version**

Versions of the games, e.g., Red, Blue or Yellow.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `version_group` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/version-group/

**List version groups**

Version groups categorize highly similar versions of the games.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/version-group/{id}/

**Get version group**

Version groups categorize highly similar versions of the games.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `order` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `generation` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `move_learn_methods` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `pokedexes` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `regions` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `versions` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

## items

An item is an object in the games which the player can pick up, keep in their bag, and use in some manner. They have various uses, including healing, powering up, helping catch Pokémon, or to access a new area.

### GET /api/v2/item/

**List items**

An item is an object in the games which the player can pick up, keep in their bag, and use in some manner. They have various uses, including healing, powering up, helping catch Pokémon, or to access a new area.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/item/{id}/

**Get item**

An item is an object in the games which the player can pick up, keep in their bag, and use in some manner. They have various uses, including healing, powering up, helping catch Pokémon, or to access a new area.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `fling_power` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `fling_effect` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `attributes` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `category` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `effect_entries` (array of object, required)
    - `effect` (string, required) — Max length: 6000.
    - `short_effect` (string, required) — Max length: 300.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `flavor_text_entries` (array of object, required)
    - `text` (string, required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `game_indices` (array of object, required)
    - `game_index` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `generation` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `prices` (array of object, required)
    - `purchase_price` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `sell_price` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `currency` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `held_by_pokemon` (array of object, required)
    - `pokemon` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_details` (array of object, required)
      - `rarity` (integer, required)
      - `version` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `sprites` (object, required)
    - `default` (string, required) — May be null.
  - `baby_trigger_for` (object, required) — May be null.
    - `url` (string (uri), required)
  - `machines` (array of object, required)
    - `machine` (object, required)
      - `url` (string (uri), required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/item-category/

**List item categories**

Item categories determine where items will be placed in the players bag.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/item-category/{id}/

**Get item category**

Item categories determine where items will be placed in the players bag.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `items` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pocket` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/item-attribute/

**List item attributes**

Item attributes define particular aspects of items, e.g."usable in battle" or "consumable".

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/item-attribute/{id}/

**Get item attribute**

Item attributes define particular aspects of items, e.g."usable in battle" or "consumable".

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `items` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/item-fling-effect/

**List item fling effects**

The various effects of the move"Fling" when used with different items.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/item-fling-effect/{id}/

**Get item fling effect**

The various effects of the move"Fling" when used with different items.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `effect_entries` (array of object, required)
    - `effect` (string, required) — Max length: 6000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `items` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/item-pocket/

**List item pockets**

Pockets within the players bag used for storing items by category.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/item-pocket/{id}/

**Get item pocket**

Pockets within the players bag used for storing items by category.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `categories` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/currency/

**List currencies**

Currencies used to buy items.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/currency/{id}/

**Get currency**

Currencies used to buy items.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

## location

Locations that can be visited within the games. Locations make up sizable portions of regions, like cities or routes.

### GET /api/v2/location/

**List locations**

Locations that can be visited within the games. Locations make up sizable portions of regions, like cities or routes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/location/{id}/

**Get location**

Locations that can be visited within the games. Locations make up sizable portions of regions, like cities or routes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `region` (object, required) — May be null.
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `game_indices` (array of object, required)
    - `game_index` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `generation` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `areas` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/location-area/

**List location areas**

Location areas are sections of areas, such as floors in a building or cave. Each area has its own set of possible Pokémon encounters.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/location-area/{id}/

**Get location area**

Location areas are sections of areas, such as floors in a building or cave. Each area has its own set of possible Pokémon encounters.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | Yes | A unique integer value identifying this location area. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `game_index` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
  - `encounter_method_rates` (array of object, required)
    - `encounter_method` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_details` (array of object, required)
      - `rate` (integer, required)
      - `version` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `location` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_encounters` (array of object, required)
    - `pokemon` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_details` (array of object, required)
      - `version` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `max_chance` (integer, required)
      - `encounter_details` (array of object, required)
        - `min_level` (integer, required)
        - `max_level` (integer, required)
        - `chance` (integer) — Default: `0`.
        - `method` (object)
        - `condition_values` (array of object, required)
        - `pokemon_details` (object, required) — May be null.

### GET /api/v2/pal-park-area/

**List pal park areas**

Areas used for grouping Pokémon encounters in Pal Park. They're like habitats that are specific to Pal Park.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/pal-park-area/{id}/

**Get pal park area**

Areas used for grouping Pokémon encounters in Pal Park. They're like habitats that are specific to Pal Park.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokemon_encounters` (array of object, required)
    - `base_score` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `rate` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `pokemon_species` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/region/

**List regions**

A region is an organized area of the Pokémon world. Most often, the main difference between regions is the species of Pokémon that can be encountered within them.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/region/{id}/

**Get region**

A region is an organized area of the Pokémon world. Most often, the main difference between regions is the species of Pokémon that can be encountered within them.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `locations` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `main_generation` (object, required) — May be null.
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `pokedexes` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `version_groups` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

## machines

Machines are the representation of items that teach moves to Pokémon. They vary from version to version, so it is not certain that one specific TM or HM corresponds to a single Machine.

### GET /api/v2/machine/

**List machines**

Machines are the representation of items that teach moves to Pokémon. They vary from version to version, so it is not certain that one specific TM or HM corresponds to a single Machine.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `url` (string (uri), required)

### GET /api/v2/machine/{id}/

**Get machine**

Machines are the representation of items that teach moves to Pokémon. They vary from version to version, so it is not certain that one specific TM or HM corresponds to a single Machine.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `item` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `version_group` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `move` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

## moves

Moves are the skills of Pokémon in battle. In battle, a Pokémon uses one move each turn. Some moves (including those learned by Hidden Machine) can be used outside of battle as well, usually for the purpose of removing obstacles or exploring new areas.

### GET /api/v2/move/

**List moves**

Moves are the skills of Pokémon in battle. In battle, a Pokémon uses one move each turn. Some moves (including those learned by Hidden Machine) can be used outside of battle as well, usually for the purpose of removing obstacles or exploring new areas.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move/{id}/

**Get move**

Moves are the skills of Pokémon in battle. In battle, a Pokémon uses one move each turn. Some moves (including those learned by Hidden Machine) can be used outside of battle as well, usually for the purpose of removing obstacles or exploring new areas.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `accuracy` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `effect_chance` (integer, required)
  - `pp` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `priority` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `power` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `contest_combos` (object, required) — May be null.
    - `normal` (object, required)
      - `use_before` (array of object, required) — May be null.
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `use_after` (array of object, required) — May be null.
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
    - `super` (object, required)
      - `use_before` (array of object, required) — May be null.
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
      - `use_after` (array of object, required) — May be null.
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `contest_type` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `contest_effect` (object, required)
    - `url` (string (uri), required)
  - `damage_class` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `effect_entries` (array of object, required)
    - `effect` (string, required) — Max length: 6000.
    - `short_effect` (string, required) — Max length: 300.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `effect_changes` (array of object, required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `effect_entries` (array of object, required)
      - `effect` (string, required) — Max length: 6000.
      - `language` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
  - `generation` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `meta` (object, required)
    - `ailment` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `category` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `min_hits` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `max_hits` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `min_turns` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `max_turns` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `drain` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `healing` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `crit_rate` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `ailment_chance` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `flinch_chance` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `stat_chance` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `past_values` (array of object, required)
    - `accuracy` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `power` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `pp` (integer) — Minimum: -2147483648. Maximum: 2147483647. May be null.
    - `effect_chance` (integer, required)
    - `effect_entries` (array of object, required)
      - `effect` (string, required) — Max length: 6000.
      - `short_effect` (string, required) — Max length: 300.
      - `language` (object, required)
        - `name` (string, required) — Max length: 200.
        - `url` (string (uri), required)
    - `type` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `stat_changes` (array of object, required)
    - `change` (integer, required) — Minimum: -2147483648. Maximum: 2147483647.
    - `stat` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `super_contest_effect` (object, required)
    - `url` (string (uri), required)
  - `target` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `type` (object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `machines` (array of object, required)
    - `machine` (object, required)
      - `url` (string (uri), required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `flavor_text_entries` (array of object, required)
    - `flavor_text` (string, required)
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
    - `version_group` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `learned_by_pokemon` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-ailment/

**List move meta ailments**

Move Ailments are status conditions caused by moves used during battle. See [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Status_condition) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-ailment/{id}/

**Get move meta ailment**

Move Ailments are status conditions caused by moves used during battle. See [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Status_condition) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `moves` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/move-battle-style/

**List move battle styles**

Styles of moves when used in the Battle Palace. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Battle_Frontier_(Generation_III)) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-battle-style/{id}/

**Get move battle style**

Styles of moves when used in the Battle Palace. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Battle_Frontier_(Generation_III)) for greater detail.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)

### GET /api/v2/move-category/

**List move meta categories**

Very general categories that loosely group move effects.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-category/{id}/

**Get move meta category**

Very general categories that loosely group move effects.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `moves` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-learn-method/

**List move learn methods**

Methods by which Pokémon can learn moves.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-learn-method/{id}/

**Get move learn method**

Methods by which Pokémon can learn moves.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `version_groups` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-target/

**List move targets**

Targets moves can be directed at during battle. Targets can be Pokémon, environments or even other moves.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `limit` | query | integer | No | Number of results to return per page. |
| `offset` | query | integer | No | The initial index from which to return the results. |
| `q` | query | string | No | > Only available locally and not at [pokeapi.co](https://pokeapi.co/docs/v2) Case-insensitive query applied on the `name` property. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `count` (integer, required)
  - `next` (string (uri)) — May be null.
  - `previous` (string (uri)) — May be null.
  - `results` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)

### GET /api/v2/move-target/{id}/

**Get move target**

Targets moves can be directed at during battle. Targets can be Pokémon, environments or even other moves.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | Yes | This parameter can be a string or an integer. |

**Responses**

- **200** — Response
  Body (`application/json`, object):
  - `id` (integer, required)
  - `name` (string, required) — Max length: 200.
  - `descriptions` (array of object, required)
    - `description` (string) — Max length: 2000.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
  - `moves` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `url` (string (uri), required)
  - `names` (array of object, required)
    - `name` (string, required) — Max length: 200.
    - `language` (object, required)
      - `name` (string, required) — Max length: 200.
      - `url` (string (uri), required)
