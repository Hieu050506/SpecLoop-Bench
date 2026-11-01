# OpenDota API — API Reference

# Introduction
The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.

You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.

You can use the API without a key, but registering for a key allows increased rate limits and usage. Check out the [API page](https://www.opendota.com/api-keys) to learn more.

**Version:** 31.1.1  
**Base URL:** `https://api.opendota.com/api`

## Authentication

- **api_key**: API key sent in query parameter `api_key`.
  Use an API key to remove monthly call limits and to receive higher rate limits. [Learn more and get your API key](https://www.opendota.com/api-keys). Usage example: https://api.opendota.com/api/matches/271145478?api_key=YOUR-API-KEY API key can also be sent using the authorization header "Authorization: Bearer YOUR-API-KEY"

## matches

### GET /matches/{match_id}

**GET /matches/{match_id}**

Match data

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `match_id` | path | integer | Yes |  |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `barracks_status_dire` (integer) — Bitmask. An integer that represents a binary of which barracks are still standing. 63 would mean all barracks still stand at the end of the game.
  - `barracks_status_radiant` (integer) — Bitmask. An integer that represents a binary of which barracks are still standing. 63 would mean all barracks still stand at the end of the game.
  - `chat` (array of object) — Array containing information on the chat of the game
    - `time` (integer) — Time in seconds at which the message was said
    - `unit` (string) — Name of the player who sent the message
    - `key` (string) — The message the player sent
    - `slot` (integer) — slot
    - `player_slot` (integer) — Which slot the player is in. 0-127 are Radiant, 128-255 are Dire. May be null.
  - `cluster` (integer) — cluster
  - `cosmetics` (object) — cosmetics
  - `dire_score` (integer) — Number of kills the Dire team had when the match ended
  - `draft_timings` (array of object) — draft_timings
    - `order` (integer) — order
    - `pick` (boolean) — pick
    - `active_team` (integer) — active_team
    - `hero_id` (integer) — The ID value of the hero played
    - `player_slot` (integer) — Which slot the player is in. 0-127 are Radiant, 128-255 are Dire. May be null.
    - `extra_time` (integer) — extra_time
    - `total_time_taken` (integer) — total_time_taken
  - `duration` (integer) — Duration of the game in seconds
  - `engine` (integer) — engine
  - `first_blood_time` (integer) — Time in seconds at which first blood occurred
  - `game_mode` (integer) — Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json
  - `human_players` (integer) — Number of human players in the game
  - `leagueid` (integer) — leagueid
  - `lobby_type` (integer) — Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json
  - `match_seq_num` (integer) — match_seq_num
  - `negative_votes` (integer) — Number of negative votes the replay received in the in-game client
  - `objectives` (array of object) — objectives
  - `picks_bans` (array of object) — Array containing information on the draft. Each item contains a boolean relating to whether the choice is a pick or a ban, the hero ID, the team the picked or banned it, and the order.
    - `is_pick` (boolean) — Boolean indicating whether the choice is a pick or a ban
    - `hero_id` (integer) — The ID value of the hero played
    - `team` (integer) — The team that picked or banned the hero
    - `order` (integer) — The order of the pick or ban
  - `positive_votes` (integer) — Number of positive votes the replay received in the in-game client
  - `radiant_gold_adv` (array of number) — Array of the Radiant gold advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their gold disadvantage.
  - `radiant_score` (integer) — Number of kills the Radiant team had when the match ended
  - `radiant_win` (boolean) — Boolean indicating whether Radiant won the match. May be null.
  - `radiant_xp_adv` (array of number) — Array of the Radiant experience advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their experience disadvantage.
  - `start_time` (integer) — The Unix timestamp at which the game started
  - `teamfights` (array of object) — teamfights. May be null.
  - `tower_status_dire` (integer) — Bitmask. An integer that represents a binary of which Dire towers are still standing.
  - `tower_status_radiant` (integer) — Bitmask. An integer that represents a binary of which Radiant towers are still standing.
  - `version` (integer) — Parse version, used internally by OpenDota
  - `replay_salt` (integer) — replay_salt
  - `series_id` (integer) — series_id
  - `series_type` (integer) — series_type
  - `radiant_team` (object) — radiant_team
  - `dire_team` (object) — dire_team
  - `league` (object) — league
  - `skill` (integer) — Skill bracket assigned by Valve (Normal, High, Very High). May be null.
  - `players` (array of object) — Array of information on individual players
    - `match_id` (integer) — The ID number of the match assigned by Valve
    - `player_slot` (integer) — Which slot the player is in. 0-127 are Radiant, 128-255 are Dire. May be null.
    - `ability_upgrades_arr` (array of integer) — An array describing how abilities were upgraded
    - `ability_uses` (object) — Object containing information on how many times the played used their abilities
    - `ability_targets` (object) — Object containing information on who the player used their abilities on
    - `damage_targets` (object) — Object containing information on how and how much damage the player dealt to other heroes
    - `account_id` (integer) — The player account ID
    - `actions` (object) — Object containing information on how many and what type of actions the player issued to their hero
    - `additional_units` (array of object) — Object containing information on additional units the player had under their control. May be null.
    - `assists` (integer) — Number of assists the player had
    - `backpack_0` (integer) — Item in backpack slot 0
    - `backpack_1` (integer) — Item in backpack slot 1
    - `backpack_2` (integer) — Item in backpack slot 2
    - `buyback_log` (array of object) — Array containing information about buybacks
      - `time` (integer) — Time in seconds the buyback occurred
      - `slot` (integer) — slot
      - `player_slot` (integer) — Which slot the player is in. 0-127 are Radiant, 128-255 are Dire. May be null.
    - `camps_stacked` (integer) — Number of camps stacked
    - `camps_stacked_t` (array of integer) — Array containing number of camps stacked at different times of the match
    - `connection_log` (array of object) — Array containing information about the player's disconnections and reconnections
      - `time` (integer) — Game time in seconds the event ocurred
      - `event` (string) — Event that occurred
      - `player_slot` (integer) — Which slot the player is in. 0-127 are Radiant, 128-255 are Dire. May be null.
    - `creeps_stacked` (integer) — Number of creeps stacked
    - `damage` (object) — Object containing information about damage dealt by the player to different units
    - `damage_inflictor` (object) — Object containing information about about the sources of this player's damage to heroes
    - `damage_inflictor_received` (object) — Object containing information about the sources of damage received by this player from heroes
    - `damage_taken` (object) — Object containing information about from whom the player took damage
    - `deaths` (integer) — Number of deaths
    - `denies` (integer) — Number of denies
    - `dn_t` (array of integer) — Array containing number of denies at different times of the match
    - `gold` (integer) — Gold at the end of the game
    - `gold_per_min` (integer) — Gold Per Minute obtained by this player
    - `gold_reasons` (object) — Object containing information on how the player gainined gold over the course of the match
    - `gold_spent` (integer) — How much gold the player spent
    - `gold_t` (array of integer) — Array containing total gold at different times of the match
    - `hero_damage` (integer) — Hero Damage Dealt
    - `hero_damage_t` (array of integer) — Array containing cumulative damage dealt to enemy heroes at each minute of the match, taken from the game's own hero damage counter, the one hero_damage comes from, so the final value matches hero_damage up to the last minute boundary. Empty for replays without that counter
    - `hero_healing` (integer) — Hero Healing Done
    - `hero_healing_t` (array of integer) — Array containing cumulative healing done to other heroes at each minute of the match, as computed from the replay combat log. Follows the hero_healing scoreboard definition (self-healing excluded), so the final value matches hero_healing up to the last minute boundary
    - `tower_damage_t` (array of integer) — Array containing cumulative damage dealt to towers at each minute of the match, taken from the game's own tower damage counter, the one tower_damage comes from, so the final value matches tower_damage up to the last minute boundary. Empty for replays without that counter
    - `hero_hits` (object) — Object containing information on how many ticks of damages the hero inflicted with different spells and damage inflictors
    - `hero_id` (integer) — The ID value of the hero played
    - `item_0` (integer) — Item in the player's first slot
    - `item_1` (integer) — Item in the player's second slot
    - `item_2` (integer) — Item in the player's third slot
    - `item_3` (integer) — Item in the player's fourth slot
    - `item_4` (integer) — Item in the player's fifth slot
    - `item_5` (integer) — Item in the player's sixth slot
    - `item_uses` (object) — Object containing information about how many times a player used items
    - `kill_streaks` (object) — Object containing information about the player's killstreaks
    - `killed` (object) — Object containing information about what units the player killed
    - `killed_by` (object) — Object containing information about who killed the player
    - `kills` (integer) — Number of kills
    - `kills_log` (array of object) — Array containing information on which hero the player killed at what time
      - `time` (integer) — Time in seconds the player killed the hero
      - `key` (string) — Hero killed
    - `deaths_log` (array of object) — Array containing information on the player's deaths: when they died, to whom, the gold lost, the gold the enemy collected and the time spent dead. Only present for matches parsed after the field was added
      - `time` (integer) — Time in seconds the player died
      - `key` (string) — Name of the killing unit
      - `gold_lost` (integer) — Gold the player lost to this death. Sums to the negative gold_reasons bucket 1
      - `gold_fed` (integer) — Gold the enemy team collected for this kill, split between the killer and the assisters. Sums to the enemy's gold_reasons bucket 12, and is larger than gold_lost because the bounty is not what the victim drops. 0 for deaths that pay no bounty, such as a suicide or a death with no enemy hero in range
      - `gold_fed_shared` (boolean) — Present and true when another death on the same side claimed the same payout, so one of the two entries carries all of it and the other carries 0. Their sum is still what that side fed, but neither number stands on its own
      - `time_dead` (integer) — Seconds spent dead after this death. Absent if the match ended before the respawn
    - `lane_pos` (object) — Object containing information on lane position
    - `last_hits` (integer) — Number of last hits
    - `leaver_status` (integer) — Integer describing whether or not the player left the game. 0: didn't leave. 1: left safely. 2+: Abandoned
    - `level` (integer) — Level at the end of the game
    - `lh_t` (array of integer) — Array describing last hits at each minute in the game
    - `life_state` (object) — life_state
    - `max_hero_hit` (object) — Object with information on the highest damage instance the player inflicted
    - `multi_kills` (object) — Object with information on the number of the number of multikills the player had
    - `obs` (object) — Object with information on where the player placed observer wards. The location takes the form (outer number, inner number) and are from ~64-192.
    - `obs_left_log` (array of object) — obs_left_log
    - `obs_log` (array of object) — Object containing information on when and where the player placed observer wards
    - `obs_placed` (integer) — Total number of observer wards placed
    - `party_id` (integer) — party_id
    - `permanent_buffs` (array of object) — Array describing permanent buffs the player had at the end of the game. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/permanent_buffs.json
    - `hero_variant` (integer) — 1-indexed facet, see https://github.com/odota/dotaconstants/blob/master/build/hero_abilities.json
    - `pings` (integer) — Total number of pings
    - `purchase` (object) — Object containing information on the items the player purchased
    - `purchase_log` (array of object) — Object containing information on when items were purchased
      - `time` (integer) — Time in seconds the item was bought
      - `key` (string) — String item ID
      - `charges` (integer) — Integer amount of charges
    - `rune_pickups` (integer) — Number of runes picked up
    - `runes` (object) — Object with information about which runes the player picked up
    - `runes_log` (array of object) — Array with information on when runes were picked up
      - `time` (integer) — Time in seconds rune picked up
      - `key` (integer) — key
    - `sen` (object) — Object with information on where sentries were placed. The location takes the form (outer number, inner number) and are from ~64-192.
    - `sen_left_log` (array of object) — Array containing information on when and where the player placed sentries
    - `sen_log` (array of object) — Array with information on when and where sentries were placed by the player
    - `sen_placed` (integer) — How many sentries were placed by the player
    - `stuns` (number) — Total stun duration of all stuns by the player
    - `times` (array of integer) — Time in seconds corresponding to the time of entries of other arrays in the match.
    - `tower_damage` (integer) — Total tower damage done by the player
    - `xp_per_min` (integer) — Experience Per Minute obtained by the player
    - `xp_reasons` (object) — Object containing information on the sources of this player's experience
    - `xp_t` (array of integer) — Experience at each minute of the game
    - `personaname` (string) — Player's Steam name. May be null.
    - `name` (string) — name. May be null.
    - `last_login` (string (date-time)) — Time of player's last login. May be null.
    - `radiant_win` (boolean) — Boolean indicating whether Radiant won the match. May be null.
    - `start_time` (integer) — The Unix timestamp at which the game started
    - `duration` (integer) — Duration of the game in seconds
    - `cluster` (integer) — cluster
    - `lobby_type` (integer) — Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json
    - `game_mode` (integer) — Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json
    - `patch` (integer) — Patch ID, from dotaconstants
    - `region` (integer) — Integer corresponding to the region the game was played on
    - `isRadiant` (boolean) — Boolean for whether or not the player is on Radiant
    - `win` (integer) — Binary integer representing whether or not the player won
    - `lose` (integer) — Binary integer representing whether or not the player lost
    - `total_gold` (integer) — Total gold at the end of the game
    - `total_xp` (integer) — Total experience at the end of the game
    - `kills_per_min` (number) — Number of kills per minute
    - `kda` (number) — kda
    - `abandons` (integer) — abandons
    - `neutral_kills` (integer) — Total number of neutral creeps killed
    - `tower_kills` (integer) — Total number of tower kills the player had
    - `courier_kills` (integer) — Total number of courier kills the player had
    - `lane_kills` (integer) — Total number of lane creeps killed by the player
    - `hero_kills` (integer) — Total number of heroes killed by the player
    - `observer_kills` (integer) — Total number of observer wards killed by the player
    - `sentry_kills` (integer) — Total number of sentry wards killed by the player
    - `roshan_kills` (integer) — Total number of roshan kills (last hit on roshan) the player had
    - `necronomicon_kills` (integer) — Total number of Necronomicon creeps killed by the player
    - `ancient_kills` (integer) — Total number of Ancient creeps killed by the player
    - `buyback_count` (integer) — Total number of buyback the player used
    - `observer_uses` (integer) — Number of observer wards used
    - `sentry_uses` (integer) — Number of sentry wards used
    - `lane_efficiency` (number) — lane_efficiency
    - `lane_efficiency_pct` (number) — lane_efficiency_pct
    - `lane` (integer) — Integer referring to which lane the hero laned in. May be null.
    - `lane_role` (integer) — lane_role. May be null.
    - `is_roaming` (boolean) — Boolean referring to whether or not the player roamed. May be null.
    - `position_est` (integer) — Estimated position (1-5) of the player within their team, from early farm priority and lane data. Only present on parsed matches. May be null.
    - `purchase_time` (object) — Object with information on when the player last purchased an item
    - `first_purchase_time` (object) — Object with information on when the player first puchased an item
    - `item_win` (object) — Object with information on whether or not the item won
    - `item_usage` (object) — Object containing binary integers the tell whether the item was purchased by the player (note: this is always 1)
    - `purchase_tpscroll` (integer) — Total number of TP scrolls purchased by the player
    - `actions_per_min` (integer) — Actions per minute
    - `life_state_dead` (integer) — life_state_dead
    - `rank_tier` (integer) — The rank tier of the player. Tens place indicates rank, ones place indicates stars.
    - `cosmetics` (array of object) — cosmetics
      - `item_id` (integer)
      - `name` (string) — name. May be null.
      - `prefab` (string)
      - `creation_date` (string (date-time)) — May be null.
      - `image_inventory` (string) — May be null.
      - `image_path` (string) — May be null.
      - `item_description` (string) — May be null.
      - `item_name` (string)
      - `item_rarity` (string) — May be null.
      - `item_type_name` (string) — May be null.
      - `used_by_heroes` (string) — May be null.
    - `benchmarks` (object) — Object containing information on certain benchmarks like GPM, XPM, KDA, tower damage, etc
    - `neutral_tokens_log` (array of object) — Object containing information on neutral tokens drops
      - `time` (integer) — Time in seconds at which the token was dropped
      - `key` (string) — Type of token dropped
    - `neutral_item_history` (array of object) — Object containing information on neutral item history
      - `time` (integer) — Time in seconds at which the item was crafted
      - `item_neutral` (string) — Neutral item name
      - `item_neutral_enhancement` (string) — Neutral enhancement name
  - `patch` (integer) — Patch ID, from dotaconstants
  - `region` (integer) — Integer corresponding to the region the game was played on
  - `all_word_counts` (object) — Word counts of the all chat messages in the player's games
  - `my_word_counts` (object) — Word counts of the player's all chat messages
  - `throw` (integer) — Maximum gold advantage of the player's team if they lost the match
  - `comeback` (integer) — Maximum gold disadvantage of the player's team if they won the match
  - `loss` (integer) — Maximum gold disadvantage of the player's team if they lost the match
  - `win` (integer) — Maximum gold advantage of the player's team if they won the match
  - `replay_url` (string) — replay_url
  - `pauses` (array of object) — Array containing information about pauses during the game. Each item contains the time and duration of the pause.
    - `time` (integer) — Time in seconds at which pause started
    - `duration` (integer) — The duration of the pause

## players

### GET /players/{account_id}

**GET /players/{account_id}**

Player data

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `rank_tier` (number) — The player's Dota medal/rank. May be null.
  - `leaderboard_rank` (number) — The player's rank on the Dota leaderboard (if Immortal). May be null.
  - `computed_mmr` (number) — Rating estimate based on ranked matches. May be null.
  - `computed_mmr_turbo` (integer) — Rating estimate based on turbo matches. May be null.
  - `aliases` (array of object) — List of names the player has used on Steam
    - `personaname` (string) — The name used by the player
    - `name_since` (string) — The date the name was used since
  - `profile` (object) — profile
    - `account_id` (integer) — The player account ID
    - `personaname` (string) — Player's Steam name. May be null.
    - `name` (string) — name. May be null.
    - `plus` (boolean) — Boolean indicating status of current Dota Plus subscription
    - `cheese` (integer) — cheese. May be null.
    - `steamid` (string) — steamid. May be null.
    - `avatar` (string) — avatar. May be null.
    - `avatarmedium` (string) — avatarmedium. May be null.
    - `avatarfull` (string) — avatarfull. May be null.
    - `profileurl` (string) — profileurl. May be null.
    - `last_login` (string) — last_login. May be null.
    - `loccountrycode` (string) — loccountrycode. May be null.
    - `is_contributor` (boolean) — Boolean indicating if the user contributed to the development of OpenDota. Default: `false`.
    - `is_subscriber` (boolean) — Boolean indicating if the user subscribed to OpenDota. Default: `false`.

### GET /players/{account_id}/wl

**GET /players/{account_id}/wl**

Win/Loss count

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `win` (integer) — Number of wins
  - `lose` (integer) — Number of loses

### GET /players/{account_id}/recentMatches

**GET /players/{account_id}/recentMatches**

Recent matches played (limited number of results)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |

**Responses**

- **200** — Success

### GET /players/{account_id}/matches

**GET /players/{account_id}/matches**

Matches played (full history, and supports column selection)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |
| `project` | query | string | No | Fields to project (array) |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `player_slot` (integer) — Which slot the player is in. 0-127 are Radiant, 128-255 are Dire. May be null.
  - `radiant_win` (boolean) — Boolean indicating whether Radiant won the match. May be null.
  - `duration` (integer) — Duration of the game in seconds
  - `game_mode` (integer) — Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json
  - `lobby_type` (integer) — Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json
  - `hero_id` (integer) — The ID value of the hero played
  - `start_time` (integer) — The Unix timestamp at which the game started
  - `version` (integer) — version. May be null.
  - `kills` (integer) — Total kills the player had at the end of the game
  - `deaths` (integer) — Total deaths the player had at the end of the game
  - `assists` (integer) — Total assists the player had at the end of the game
  - `skill` (integer) — Skill bracket assigned by Valve (Normal, High, Very High). May be null.
  - `average_rank` (integer) — Average rank of players with public match data. May be null.
  - `leaver_status` (integer) — Integer describing whether or not the player left the game. 0: didn't leave. 1: left safely. 2+: Abandoned
  - `party_size` (integer) — Size of the player's party. May be null.
  - `hero_variant` (integer) — 1-indexed facet, see https://github.com/odota/dotaconstants/blob/master/build/hero_abilities.json

### GET /players/{account_id}/heroes

**GET /players/{account_id}/heroes**

Heroes played

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `hero_id` (integer) — The ID value of the hero played
  - `last_played` (integer) — last_played
  - `games` (integer) — games
  - `win` (integer) — win
  - `with_games` (integer) — with_games
  - `with_win` (integer) — with_win
  - `against_games` (integer) — against_games
  - `against_win` (integer) — against_win

### GET /players/{account_id}/peers

**GET /players/{account_id}/peers**

Players played with

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `account_id` (integer) — The player account ID
  - `last_played` (integer) — last_played
  - `win` (integer) — win
  - `games` (integer) — games
  - `with_win` (integer) — with_win
  - `with_games` (integer) — with_games
  - `against_win` (integer) — against_win
  - `against_games` (integer) — against_games
  - `with_gpm_sum` (integer) — with_gpm_sum
  - `with_xpm_sum` (integer) — with_xpm_sum
  - `personaname` (string) — Player's Steam name. May be null.
  - `name` (string) — name. May be null.
  - `is_contributor` (boolean) — is_contributor
  - `is_subscriber` (boolean) — is_subscriber
  - `last_login` (string) — last_login. May be null.
  - `avatar` (string) — avatar. May be null.
  - `avatarfull` (string) — avatarfull. May be null.

### GET /players/{account_id}/pros

**GET /players/{account_id}/pros**

Pro players played with

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `account_id` (integer) — The player account ID
  - `name` (string) — name. May be null.
  - `country_code` (string) — country_code
  - `fantasy_role` (integer) — fantasy_role
  - `team_id` (integer) — team_id
  - `team_name` (string) — Team name. May be null.
  - `team_tag` (string) — team_tag. May be null.
  - `is_locked` (boolean) — is_locked
  - `is_pro` (boolean) — is_pro
  - `locked_until` (integer) — locked_until. May be null.
  - `steamid` (string) — steamid. May be null.
  - `avatar` (string) — avatar. May be null.
  - `avatarmedium` (string) — avatarmedium. May be null.
  - `avatarfull` (string) — avatarfull. May be null.
  - `profileurl` (string) — profileurl. May be null.
  - `last_login` (string (date-time)) — last_login. May be null.
  - `full_history_time` (string (date-time)) — full_history_time. May be null.
  - `cheese` (integer) — cheese. May be null.
  - `fh_unavailable` (boolean) — fh_unavailable. May be null.
  - `loccountrycode` (string) — loccountrycode. May be null.
  - `last_played` (integer) — last_played. May be null.
  - `win` (integer) — win
  - `games` (integer) — games
  - `with_win` (integer) — with_win
  - `with_games` (integer) — with_games
  - `against_win` (integer) — against_win
  - `against_games` (integer) — against_games
  - `with_gpm_sum` (integer) — with_gpm_sum. May be null.
  - `with_xpm_sum` (integer) — with_xpm_sum. May be null.

### GET /players/{account_id}/totals

**GET /players/{account_id}/totals**

Totals in stats

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `field` (string) — field
  - `n` (integer) — number
  - `sum` (number) — sum

### GET /players/{account_id}/counts

**GET /players/{account_id}/counts**

Counts in categories

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `leaver_status` (object) — Integer describing whether or not the player left the game. 0: didn't leave. 1: left safely. 2+: Abandoned
  - `game_mode` (object) — Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json
  - `lobby_type` (object) — Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json
  - `lane_role` (object) — lane_role
  - `region` (object) — Integer corresponding to the region the game was played on
  - `patch` (object) — Patch ID, from dotaconstants

### GET /players/{account_id}/histograms/{field}

**GET /players/{account_id}/histograms**

Distribution of matches in a single stat

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |
| `field` | path | string | Yes | Field to aggregate on |

**Responses**

- **200** — Success

### GET /players/{account_id}/wardmap

**GET /players/{account_id}/wardmap**

Wards placed in matches played

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `obs` (object) — obs
  - `sen` (object) — sen

### GET /players/{account_id}/wordcloud

**GET /players/{account_id}/wordcloud**

Words said/read in matches played

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |
| `limit` | query | integer | No | Number of matches to limit to |
| `offset` | query | integer | No | Number of matches to offset start by |
| `win` | query | integer | No | Whether the player won |
| `patch` | query | integer | No | Patch ID, from dotaconstants |
| `game_mode` | query | integer | No | Game Mode ID |
| `lobby_type` | query | integer | No | Lobby type ID |
| `region` | query | integer | No | Region ID |
| `date` | query | integer | No | Days previous |
| `lane_role` | query | integer | No | Lane Role ID |
| `hero_id` | query | integer | No | Hero ID |
| `is_radiant` | query | integer | No | Whether the player was radiant |
| `included_account_id` | query | integer | No | Account IDs in the match (array) |
| `excluded_account_id` | query | integer | No | Account IDs not in the match (array) |
| `with_hero_id` | query | integer | No | Hero IDs on the player's team (array) |
| `against_hero_id` | query | integer | No | Hero IDs against the player's team (array) |
| `significant` | query | integer | No | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | query | integer | No | The minimum number of games played, for filtering hero stats |
| `sort` | query | string | No | The field to return matches sorted by in descending order |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `my_word_counts` (object) — my_word_counts
  - `all_word_counts` (object) — all_word_counts

### GET /players/{account_id}/ratings

**GET /players/{account_id}/ratings**

Returns a history of the player rank tier/medal changes (replaces MMR)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `account_id` (integer) — The player account ID
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `rank_tier` (integer) — Rank tier/medal of the player
  - `time` (integer) — time

### GET /players/{account_id}/rankings

**GET /players/{account_id}/rankings**

Player hero rankings

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `hero_id` (integer) — The ID value of the hero played
  - `score` (number) — Hero score
  - `percent_rank` (number) — percent_rank
  - `card` (integer) — numeric_rank

### POST /players/{account_id}/refresh

**POST /players/{account_id}/refresh**

Refresh player match history (up to 500), medal (rank), and profile name

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | integer | Yes | Steam32 account ID |

**Responses**

- **200** — Success

## top players

### GET /topPlayers

**GET /topPlayers**

Get list of highly ranked players

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `turbo` | query | integer | No | Get ratings based on turbo matches |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `account_id` (integer) — The player account ID
  - `steamid` (string) — Player's steam identifier
  - `avatar` (string) — Steam picture URL (small picture)
  - `avatarmedium` (string) — Steam picture URL (medium picture)
  - `avatarfull` (string) — Steam picture URL (full picture)
  - `profileurl` (string) — Steam profile URL
  - `personaname` (string) — Player's Steam name. May be null.
  - `last_login` (string (date-time)) — Date and time of last login to OpenDota
  - `full_history_time` (string (date-time)) — Date and time of last request to refresh player's match history
  - `cheese` (integer) — Amount of dollars the player has donated to OpenDota
  - `fh_unavailable` (boolean) — Whether the refresh of player' match history failed
  - `loccountrycode` (string) — Player's country identifier, e.g. US
  - `name` (string) — Verified player name, e.g. 'Miracle-'
  - `country_code` (string) — Player's country code
  - `fantasy_role` (integer) — Player's ingame role (core: 1 or support: 2)
  - `team_id` (integer) — Player's team identifier
  - `team_name` (string) — Team name. May be null.
  - `team_tag` (string) — Player's team shorthand tag, e.g. 'EG'
  - `is_locked` (boolean) — Whether the roster lock is active
  - `is_pro` (boolean) — Whether the player is professional or not
  - `locked_until` (integer) — When the roster lock will end
  - `computed_mmr` (integer) — Rating estimate based on ranked matches. May be null.

## pro players

### GET /proPlayers

**GET /proPlayers**

Get list of pro players

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `account_id` (integer) — The player account ID
  - `steamid` (string) — Player's steam identifier
  - `avatar` (string) — Steam picture URL (small picture)
  - `avatarmedium` (string) — Steam picture URL (medium picture)
  - `avatarfull` (string) — Steam picture URL (full picture)
  - `profileurl` (string) — Steam profile URL
  - `personaname` (string) — Player's Steam name. May be null.
  - `last_login` (string (date-time)) — Date and time of last login to OpenDota
  - `full_history_time` (string (date-time)) — Date and time of last request to refresh player's match history
  - `cheese` (integer) — Amount of dollars the player has donated to OpenDota
  - `fh_unavailable` (boolean) — Whether the refresh of player' match history failed
  - `loccountrycode` (string) — Player's country identifier, e.g. US
  - `name` (string) — Verified player name, e.g. 'Miracle-'
  - `country_code` (string) — Player's country code
  - `fantasy_role` (integer) — Player's ingame role (core: 1 or support: 2)
  - `team_id` (integer) — Player's team identifier
  - `team_name` (string) — Team name. May be null.
  - `team_tag` (string) — Player's team shorthand tag, e.g. 'EG'
  - `is_locked` (boolean) — Whether the roster lock is active
  - `is_pro` (boolean) — Whether the player is professional or not
  - `locked_until` (integer) — When the roster lock will end
  - `computed_mmr` (integer) — Rating estimate based on ranked matches. May be null.

## pro matches

### GET /proMatches

**GET /proMatches**

Get list of pro matches

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `less_than_match_id` | query | integer | No | Get matches with a match ID lower than this value |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `duration` (integer) — Duration of the game in seconds
  - `start_time` (integer) — The Unix timestamp at which the game started
  - `radiant_team_id` (integer) — The Radiant's team_id
  - `radiant_name` (string) — The Radiant's team name
  - `dire_team_id` (integer) — The Dire's team_id
  - `dire_name` (string) — The Dire's team name
  - `leagueid` (integer) — Identifier for the league the match took place in
  - `league_name` (string) — Name of league the match took place in
  - `series_id` (integer) — Identifier for the series of the match
  - `series_type` (integer) — Type of series the match was
  - `radiant_score` (integer) — Number of kills the Radiant team had when the match ended
  - `dire_score` (integer) — Number of kills the Dire team had when the match ended
  - `radiant_win` (boolean) — Boolean indicating whether Radiant won the match. May be null.
  - `radiant` (boolean) — Whether the team/player/hero was on Radiant

## public matches

### GET /publicMatches

**GET /publicMatches**

Get list of randomly sampled public matches

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `less_than_match_id` | query | integer | No | Get matches with a match ID lower than this value |
| `min_rank` | query | integer | No | Minimum rank for the matches. Ranks are represented by integers (10-15: Herald, 20-25: Guardian, 30-35: Crusader, 40-45: Archon, 50-55: Legend, 60-65: Ancient, 70-75: Divine, 80: Immortal). Each increment represents an additional star. |
| `max_rank` | query | integer | No | Maximum rank for the matches. Ranks are represented by integers (10-15: Herald, 20-25: Guardian, 30-35: Crusader, 40-45: Archon, 50-55: Legend, 60-65: Ancient, 70-75: Divine, 80: Immortal). Each increment represents an additional star. |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `match_seq_num` (integer) — match_seq_num
  - `radiant_win` (boolean) — Boolean indicating whether Radiant won the match. May be null.
  - `start_time` (integer) — The Unix timestamp at which the game started
  - `duration` (integer) — Duration of the game in seconds
  - `lobby_type` (integer)
  - `game_mode` (integer)
  - `avg_rank_tier` (integer)
  - `num_rank_tier` (integer)
  - `cluster` (integer)
  - `radiant_team` (array of integer) — radiant_team
  - `dire_team` (array of integer) — dire_team

## parsed matches

### GET /parsedMatches

**GET /parsedMatches**

Get list of parsed match IDs

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `less_than_match_id` | query | integer | No | Get matches with a match ID lower than this value |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `match_id` (integer) — The ID number of the match assigned by Valve

## explorer

### GET /explorer

**GET /explorer**

Submit arbitrary SQL queries to the database

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `sql` | query | string | No | The PostgreSQL query as percent-encoded string. |

**Responses**

- **200** — Success

## metadata

### GET /metadata

**GET /metadata**

Site metadata

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `banner` (object) — banner. May be null.

## distributions

### GET /distributions

**GET /distributions**

Distributions of MMR data by bracket and country

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `ranks` (object) — ranks
    - `rows` (array of object) — rows
      - `bin` (integer) — bin
      - `bin_name` (integer) — bin_name
      - `count` (integer) — count
      - `cumulative_sum` (integer) — cumulative_sum
    - `sum` (object) — sum
      - `count` (integer) — count

## search

### GET /search

**GET /search**

Search players by personaname.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string | Yes | Search string |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `account_id` (integer) — The player account ID
  - `avatarfull` (string) — avatarfull. May be null.
  - `personaname` (string) — Player's Steam name. May be null.
  - `last_match_time` (string) — last_match_time. May not be present or null.
  - `similarity` (number) — similarity

## rankings

### GET /rankings

**GET /rankings**

Top players by hero

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hero_id` | query | string | Yes | Hero ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `hero_id` (integer) — The ID value of the hero played
  - `rankings` (array of object) — rankings
    - `account_id` (integer) — The player account ID
    - `score` (number) — Score
    - `steamid` (string) — steamid. May be null.
    - `avatar` (string) — avatar. May be null.
    - `avatarmedium` (string) — avatarmedium. May be null.
    - `avatarfull` (string) — avatarfull. May be null.
    - `profileurl` (string) — profileurl. May be null.
    - `personaname` (string) — Player's Steam name. May be null.
    - `last_login` (string (date-time)) — last_login. May be null.
    - `full_history_time` (string (date-time)) — full_history_time
    - `cheese` (integer) — cheese. May be null.
    - `fh_unavailable` (boolean) — fh_unavailable. May be null.
    - `loccountrycode` (string) — loccountrycode. May be null.
    - `rank_tier` (integer) — rank_tier. May be null.

## benchmarks

### GET /benchmarks

**GET /benchmarks**

Benchmarks of average stat values for a hero

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hero_id` | query | string | Yes | Hero ID |
| `bracket` | query | integer | No | Rank bracket from 1 (Herald) to 8 (Immortal) to benchmark against. Omit for matches of all ranks |
| `role` | query | string | No | Benchmark against cores or supports only, estimated from farm within each team. Can be combined with bracket. Omit for all roles. Allowed values: `core`, `support`. |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `hero_id` (integer) — The ID value of the hero played
  - `result` (object) — result
    - `gold_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `xp_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `kills_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `deaths_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `assists_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `last_hits_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `denies_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `hero_damage_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `hero_healing_per_min` (array of object)
      - `percentile` (number) — percentile
      - `value` (number) — value
    - `tower_damage` (array of object)
      - `percentile` (number) — percentile
      - `value` (integer) — value

## health

### GET /health

**GET /health**

Get service health data

**Responses**

- **200** — Success

## request

### GET /request/{jobId}

**GET /request/{jobId}**

Get parse request state

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `jobId` | path | string | Yes | The job ID to query. |

**Responses**

- **200** — Success

### POST /request/{match_id}

**POST /request/{match_id}**

Submit a new parse request. This call counts as 10 calls for rate limit (but not billing) purposes.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `match_id` | path | integer | Yes |  |

**Responses**

- **200** — Success

## findMatches

### GET /findMatches

**GET /**

Finds recent matches by heroes played

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `teamA` | query | array of integer | No | Hero IDs on first team (array) |
| `teamB` | query | array of integer | No | Hero IDs on second team (array) |

**Responses**

- **200** — Success

## heroes

### GET /heroes

**GET /heroes**

Get hero data

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `id` (integer, required) — The ID value of the hero played
  - `name` (string) — Dota hero command name
  - `localized_name` (string) — Hero name
  - `primary_attr` (string) — Hero primary shorthand attribute name, e.g. 'agi'
  - `attack_type` (string) — Hero attack type, either 'Melee' or 'Ranged'
  - `roles` (array of string)

### GET /heroes/{hero_id}/matches

**GET /heroes/{hero_id}/matches**

Get recent matches with a hero

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hero_id` | path | integer | Yes | Hero ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `duration` (integer) — Duration of the game in seconds
  - `start_time` (integer) — The Unix timestamp at which the game started
  - `radiant_team_id` (integer) — The Radiant's team_id
  - `radiant_name` (string) — The Radiant's team name
  - `dire_team_id` (integer) — The Dire's team_id
  - `dire_name` (string) — The Dire's team name
  - `leagueid` (integer) — Identifier for the league the match took place in
  - `league_name` (string) — Name of league the match took place in
  - `series_id` (integer) — Identifier for the series of the match
  - `series_type` (integer) — Type of series the match was
  - `radiant_score` (integer) — Number of kills the Radiant team had when the match ended
  - `dire_score` (integer) — Number of kills the Dire team had when the match ended
  - `radiant_win` (boolean) — Boolean indicating whether Radiant won the match. May be null.
  - `radiant` (boolean) — Whether the team/player/hero was on Radiant

### GET /heroes/{hero_id}/matchups

**GET /heroes/{hero_id}/matchups**

Get results against other heroes for a hero

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hero_id` | path | integer | Yes | Hero ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `hero_id` (integer) — The ID value of the hero played
  - `games_played` (integer) — Number of games played
  - `wins` (integer) — Number of games won

### GET /heroes/{hero_id}/durations

**GET /heroes/{hero_id}/durations**

Get hero performance over a range of match durations

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hero_id` | path | integer | Yes | Hero ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `duration_bin` (string) — Lower bound of number of seconds the match lasted
  - `games_played` (integer) — Number of games played
  - `wins` (integer) — Number of wins

### GET /heroes/{hero_id}/players

**GET /heroes/{hero_id}/players**

Get players who have played this hero

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hero_id` | path | integer | Yes | Hero ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of array of object):
  - `account_id` (integer) — The player account ID
  - `steamid` (string) — Player's steam identifier
  - `avatar` (string) — Steam picture URL (small picture)
  - `avatarmedium` (string) — Steam picture URL (medium picture)
  - `avatarfull` (string) — Steam picture URL (full picture)
  - `profileurl` (string) — Steam profile URL
  - `personaname` (string) — Player's Steam name. May be null.
  - `last_login` (string (date-time)) — Date and time of last login to OpenDota
  - `full_history_time` (string (date-time)) — Date and time of last request to refresh player's match history
  - `cheese` (integer) — Amount of dollars the player has donated to OpenDota
  - `fh_unavailable` (boolean) — Whether the refresh of player' match history failed
  - `loccountrycode` (string) — Player's country identifier, e.g. US
  - `name` (string) — Verified player name, e.g. 'Miracle-'
  - `country_code` (string) — Player's country code
  - `fantasy_role` (integer) — Player's ingame role (core: 1 or support: 2)
  - `team_id` (integer) — Player's team identifier
  - `team_name` (string) — Team name. May be null.
  - `team_tag` (string) — Player's team shorthand tag, e.g. 'EG'
  - `is_locked` (boolean) — Whether the roster lock is active
  - `is_pro` (boolean) — Whether the player is professional or not
  - `locked_until` (integer) — When the roster lock will end
  - `computed_mmr` (integer) — Rating estimate based on ranked matches. May be null.

### GET /heroes/{hero_id}/itemPopularity

**GET /heroes/{hero_id}/itemPopularity**

Get item popularity of hero categoried by start, early, mid and late game, analyzed from professional games

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hero_id` | path | integer | Yes | Hero ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `start_game_items` (object) — Items bought before game started
    - `item` (integer) — Number of item bought
  - `early_game_items` (object) — Items bought in the first 10 min of the game, with cost at least 700
    - `item` (integer) — Number of item bought
  - `mid_game_items` (object) — Items bought between 10 and 25 min of the game, with cost at least 2000
    - `item` (integer) — Number of item bought
  - `late_game_items` (object) — Items bought at least 25 min after game started, with cost at least 4000
    - `item` (integer) — Number of item bought

## hero stats

### GET /heroStats

**GET /heroStats**

Get stats about hero performance in recent matches

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `id` (integer) — The ID value of the hero played
  - `name` (string) — Dota hero command name
  - `localized_name` (string) — Hero name
  - `primary_attr` (string) — primary_attr
  - `attack_type` (string) — attack_type
  - `roles` (array of string) — roles
  - `img` (string) — img
  - `icon` (string) — icon
  - `base_health` (integer) — base_health
  - `base_health_regen` (number) — base_health_regen
  - `base_mana` (integer) — base_mana
  - `base_mana_regen` (integer) — base_mana_regen
  - `base_armor` (integer) — base_armor
  - `base_mr` (integer) — base_mr
  - `base_attack_min` (integer) — base_attack_min
  - `base_attack_max` (integer) — base_attack_max
  - `base_str` (integer) — base_str
  - `base_agi` (integer) — base_agi
  - `base_int` (integer) — base_int
  - `str_gain` (number) — str_gain
  - `agi_gain` (number) — agi_gain
  - `int_gain` (number) — int_gain
  - `attack_range` (integer) — attack_range
  - `projectile_speed` (integer) — projectile_speed
  - `attack_rate` (number) — attack_rate
  - `base_attack_time` (integer) — base_attack_time
  - `attack_point` (number) — attack_point
  - `move_speed` (integer) — move_speed
  - `turn_rate` (number) — turn_rate
  - `cm_enabled` (boolean) — cm_enabled
  - `legs` (integer) — legs
  - `day_vision` (integer) — day_vision
  - `night_vision` (integer) — night_vision
  - `hero_id` (integer) — The ID value of the hero played
  - `turbo_picks` (integer) — Picks in Turbo mode this month
  - `turbo_wins` (integer) — Wins in Turbo mode this month
  - `pro_ban` (integer) — pro_ban
  - `pro_win` (integer) — pro_win
  - `pro_pick` (integer) — pro_pick
  - `1_pick` (integer) — Herald picks
  - `1_win` (integer) — Herald wins
  - `2_pick` (integer) — Guardian picks
  - `2_win` (integer) — Guardian wins
  - `3_pick` (integer) — Crusader picks
  - `3_win` (integer) — Crusader wins
  - `4_pick` (integer) — Archon picks
  - `4_win` (integer) — Archon wins
  - `5_pick` (integer) — Legend picks
  - `5_win` (integer) — Legend wins
  - `6_pick` (integer) — Ancient picks
  - `6_win` (integer) — Ancient wins
  - `7_pick` (integer) — Divine picks
  - `7_win` (integer) — Divine wins
  - `8_pick` (integer) — Immortal picks
  - `8_win` (integer) — Immortal wins

## leagues

### GET /leagues

**GET /leagues**

Get league data

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `leagueid` (integer) — leagueid
  - `ticket` (string) — ticket
  - `banner` (string) — banner
  - `tier` (string) — tier
  - `name` (string) — League name

### GET /leagues/{league_id}

**GET /leagues/{league_id}**

Get data for a league

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `league_id` | path | integer | Yes | League ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `leagueid` (integer) — leagueid
  - `ticket` (string) — ticket
  - `banner` (string) — banner
  - `tier` (string) — tier
  - `name` (string) — League name

### GET /leagues/{league_id}/matches

**GET /leagues/{league_id}/matches**

Get matches for a league (excluding amateur leagues)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `league_id` | path | integer | Yes | League ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `duration` (integer) — Duration of the game in seconds
  - `start_time` (integer) — The Unix timestamp at which the game started
  - `radiant_team_id` (integer) — The Radiant's team_id
  - `radiant_name` (string) — The Radiant's team name
  - `dire_team_id` (integer) — The Dire's team_id
  - `dire_name` (string) — The Dire's team name
  - `leagueid` (integer) — Identifier for the league the match took place in
  - `league_name` (string) — Name of league the match took place in
  - `series_id` (integer) — Identifier for the series of the match
  - `series_type` (integer) — Type of series the match was
  - `radiant_score` (integer) — Number of kills the Radiant team had when the match ended
  - `dire_score` (integer) — Number of kills the Dire team had when the match ended
  - `radiant_win` (boolean) — Boolean indicating whether Radiant won the match. May be null.
  - `radiant` (boolean) — Whether the team/player/hero was on Radiant

### GET /leagues/{league_id}/matchIds

**GET /leagues/{league_id}/matchIds**

Get match IDs for a league (including amateur leagues)

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `league_id` | path | integer | Yes | League ID |

**Responses**

- **200** — Success

### GET /leagues/{league_id}/teams

**GET /leagues/{league_id}/teams**

Get teams for a league

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `league_id` | path | integer | Yes | League ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `team_id` (integer) — Team's identifier
  - `rating` (number) — The Elo rating of the team
  - `wins` (integer) — The number of games won by this team
  - `losses` (integer) — The number of losses by this team
  - `last_match_time` (integer) — The Unix timestamp of the last match played by this team
  - `name` (string) — Team name. May be null.
  - `tag` (string) — The team tag/abbreviation

## teams

### GET /teams

**GET /teams**

Get team data

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | No | Page number, zero indexed. Each page returns up to 1000 entries. |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `team_id` (integer) — Team's identifier
  - `rating` (number) — The Elo rating of the team
  - `wins` (integer) — The number of games won by this team
  - `losses` (integer) — The number of losses by this team
  - `last_match_time` (integer) — The Unix timestamp of the last match played by this team
  - `name` (string) — Team name. May be null.
  - `tag` (string) — The team tag/abbreviation

### GET /teams/{team_id}

**GET /teams/{team_id}**

Get data for a team

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `team_id` | path | integer | Yes | Team ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `team_id` (integer) — Team's identifier
  - `rating` (number) — The Elo rating of the team
  - `wins` (integer) — The number of games won by this team
  - `losses` (integer) — The number of losses by this team
  - `last_match_time` (integer) — The Unix timestamp of the last match played by this team
  - `name` (string) — Team name. May be null.
  - `tag` (string) — The team tag/abbreviation

### GET /teams/{team_id}/matches

**GET /teams/{team_id}/matches**

Get matches for a team

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `team_id` | path | integer | Yes | Team ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `radiant` (boolean) — Whether the team/player/hero was on Radiant
  - `radiant_win` (boolean) — Boolean indicating whether Radiant won the match. May be null.
  - `radiant_score` (integer) — Number of kills the Radiant team had when the match ended
  - `dire_score` (integer) — Number of kills the Dire team had when the match ended
  - `duration` (integer) — Duration of the game in seconds
  - `start_time` (integer) — The Unix timestamp at which the game started
  - `leagueid` (integer) — Identifier for the league the match took place in
  - `league_name` (string) — Name of league the match took place in
  - `cluster` (integer) — cluster
  - `opposing_team_id` (integer) — Opposing team identifier
  - `opposing_team_name` (string) — Opposing team name, e.g. 'Evil Geniuses'. May be null.
  - `opposing_team_logo` (string) — Opposing team logo url

### GET /teams/{team_id}/players

**GET /teams/{team_id}/players**

Get players who have played for a team

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `team_id` | path | integer | Yes | Team ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `account_id` (integer) — The player account ID
  - `name` (string) — name. May be null.
  - `games_played` (integer) — Number of games played
  - `wins` (integer) — Number of wins
  - `is_current_team_member` (boolean) — If this player is on the current roster

### GET /teams/{team_id}/heroes

**GET /teams/{team_id}/heroes**

Get heroes for a team

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `team_id` | path | integer | Yes | Team ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, object):
  - `hero_id` (integer) — The ID value of the hero played
  - `name` (string) — Hero name
  - `games_played` (integer) — Number of games played
  - `wins` (integer) — Number of wins

## records

### GET /records/{field}

**GET /records/{field}**

Get top performances in a stat

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `field` | path | string | Yes | Field name to query |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `match_id` (integer) — The ID number of the match assigned by Valve
  - `start_time` (integer) — The Unix timestamp at which the game started
  - `hero_id` (integer) — The ID value of the hero played
  - `score` (integer) — Record score

## live

### GET /live

**GET /live**

Get top currently ongoing live games

**Responses**

- **200** — Success

## scenarios

### GET /scenarios/itemTimings

**GET /scenarios/itemTimings**

Win rates for certain item timings on a hero for items that cost at least 1400 gold

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `item` | query | string | No | Filter by item name e.g. "spirit_vessel" |
| `hero_id` | query | integer | No | Hero ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `hero_id` (integer) — The ID value of the hero played
  - `item` (string) — Purchased item
  - `time` (integer) — Ingame time in seconds before the item was purchased
  - `games` (string) — The number of games where the hero bought this item before this time
  - `wins` (string) — The number of games won where the hero bought this item before this time

### GET /scenarios/laneRoles

**GET /scenarios/laneRoles**

Win rates for heroes in certain lane roles

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `lane_role` | query | string | No | Filter by lane role 1-4 (Safe, Mid, Off, Jungle) |
| `hero_id` | query | integer | No | Hero ID |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `hero_id` (integer) — The ID value of the hero played
  - `lane_role` (integer) — The hero's lane role
  - `time` (integer) — Maximum game length in seconds
  - `games` (string) — The number of games where the hero played in this lane role
  - `wins` (string) — The number of games won where the hero played in this lane role

### GET /scenarios/misc

**GET /scenarios/misc**

Miscellaneous team scenarios

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `scenario` | query | string | No | Name of the scenario (see teamScenariosQueryParams) |

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `scenario` (string) — The scenario's name or description
  - `is_radiant` (boolean) — Boolean indicating whether Radiant executed this scenario
  - `region` (integer) — Region the game was played in
  - `games` (string) — The number of games where this scenario occurred
  - `wins` (string) — The number of games won where this scenario occured

## schema

### GET /schema

**GET /schema**

Get database schema

**Responses**

- **200** — Success
  Body (`application/json; charset=utf-8`, array of object):
  - `table_name` (string) — table_name
  - `column_name` (string) — column_name
  - `data_type` (string) — data_type

## constants

### GET /constants/{resource}

**GET /constants**

Get static game data mirrored from the dotaconstants repository.

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `resource` | path | string | Yes | Resource name e.g. `heroes`. [List of resources](https://github.com/odota/dotaconstants/tree/master/build) |

**Responses**

- **200** — Success
