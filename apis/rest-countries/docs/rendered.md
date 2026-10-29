# REST countries API — API Reference

REST countries API

**Version:** v2.0.5  
**Base URL:** `http://localhost:9007`

## Endpoints

### GET /v2/all

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/alpha/{alphacode}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `alphacode` | path | string | Yes | Search by ISO 3166-1 2-letter or 3-letter country code |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/alpha

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `codes` | query | string | Yes | Search by list of ISO 3166-1 2-letter or 3-letter country codes |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/currency/{currency}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `currency` | path | string | Yes | Search by ISO 4217 currency code |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/name/{name}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `name` | path | string | Yes | Search by country name. It can be the native name or partial name |
| `fullText` | query | boolean | No |  |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/callingcode/{callingcode}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `callingcode` | path | string | Yes | Search by calling code |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/capital/{capital}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `capital` | path | string | Yes | Search by capital city |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/region/{region}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `region` | path | string | Yes | In version 2 regions are continent and subregions are region Search by continent: Africa, Americas, Asia, Europe, Oceania |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/lang/{lang}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `lang` | path | string | Yes | Search by ISO 639-1 language code |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v2/regionalbloc/{regionalbloc}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `regionalbloc` | path | string | Yes | Search by regional bloc: - EU (European Union) - EFTA (European Free Trade Association) - CARICOM (Caribbean Community) - PA (Pacific Alliance) - AU (African Union) - USAN (Union of South American Nations) - EEU (Eurasian Economic Union) - AL (Arab League) - ASEAN (Association of Southeast Asian Nations) - CAIS (Central American Integration System) - CEFTA (Central European Free Trade Agreement) - NAFTA (North American Free Trade Agreement) - SAARC (South Asian Association for Regional Cooperation) |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/all

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/alpha/{alphacode}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `alphacode` | path | string | Yes | Search by ISO 3166-1 2-letter or 3-letter country code |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/alpha

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `codes` | query | string | Yes | Search by list of ISO 3166-1 2-letter or 3-letter country codes |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/currency/{currency}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `currency` | path | string | Yes | Search by currency code or name |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/name/{name}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `name` | path | string | Yes | Search by country name. It can be the common or official value |
| `fullText` | query | boolean | No |  |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/capital/{capital}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `capital` | path | string | Yes | Search by capital city |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3.1/region/{region}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `region` | path | string | Yes | Search by Region: Africa, Americas, Asia, Europe, Oceania. The search can be using the full region’s name or just part of it |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/subregion/{subregion}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `subregion` | path | string | Yes | Search by Subregion: South America, Southern Europe, Central America, Eastern Asia, etc. The search can be using the full subregion’s name or just part of it |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/lang/{lang}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `lang` | path | string | Yes | Search by language code or name |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/demonym/{demonym}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `demonym` | path | string | Yes | Now you can search by how a citizen is called. |

**Responses**

- **200** — Successful response
- **default** — Other responses

### GET /v3/translation/{translation}

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `fields` | query | string | No | You can filter the output of your request to include only the specified fields. |
| `translation` | path | string | Yes | You can search by any translation name |

**Responses**

- **200** — Successful response
- **default** — Other responses
