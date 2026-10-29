# OMDb API — API Reference

This API requires authorization, you can get a free key here: [http://omdbapi.com/apikey.aspx](http://omdbapi.com/apikey.aspx)

**Version:** 1.0  
**Base URL:** `https://www.omdbapi.com`

## Authentication

- **APIKeyQueryParam**: API key sent in query parameter `apikey`.

## Search

### GET /

**Search**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `t` | query | string | No | Title of movie or series |
| `i` | query | string | No | A valid IMDb ID (e.g. tt0000001) |
| `s` | query | string | No | Title of movie or series |
| `page` | query | integer | No | Page number to return |
| `y` | query | integer | No | Year of release |
| `type` | query | string | No | Return movie or series. Allowed values: `movie`, `series`, `episode`. |
| `plot` | query | string | No | Return short or full plot. Allowed values: `short`, `full`. |
| `r` | query | string | No | The response type to return. Allowed values: `json`, `xml`. |
| `callback` | query | string | No | JSONP callback name |

**Parameter dependencies:** `OnlyOne(i OR t, s);`

**Responses**

- **200** — Successful operation
  Body (`*/*`, object):
  - `Response` (string, required) — Allowed values: `true`, `false`.
  - `Error` (string)
  - `Search` (array of object)
    - `Title` (string)
    - `Year` (string)
    - `imdbID` (string)
    - `Type` (string)
    - `Poster` (string)
  - `totalResults` (integer)
  - `Title` (string)
  - `Year` (string)
  - `Rated` (string)
  - `Released` (string)
  - `Runtime` (string)
  - `Genre` (string)
  - `Director` (string)
  - `Writer` (string)
  - `Actors` (string)
  - `Plot` (string)
  - `Language` (string)
  - `Country` (string)
  - `Awards` (string)
  - `Poster` (string)
  - `Ratings` (array of object)
    - `Source` (string)
    - `Value` (string)
  - `Metascore` (string)
  - `imdbRating` (string)
  - `imdbVotes` (string)
  - `imdbID` (string)
  - `Type` (string)
  - `DVD` (string)
  - `BoxOffice` (string)
  - `Production` (string)
  - `Website` (string)
  - `Episode` (string)
  - `Season` (string)
  - `seriesID` (string)
  - `totalSeasons` (string)
- **401** — Not authenticated
  Body (`*/*`, object):
  - `Response` (string, required) — Allowed values: `false`.
  - `Error` (string, required)
