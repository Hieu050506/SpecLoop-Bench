# LanguageTool API — API Reference

Check texts for style and grammar issues with LanguageTool. See <a href='http://wiki.languagetool.org/public-http-api'>our wiki</a> for access limitations.

**Version:** 1.0.2  
**Base URL:** `https://api.languagetool.org/v2`

## Endpoints

### POST /check

**Check a text**

The main feature - check a text with LanguageTool for possible style and grammar issues.

**Request body** (`application/x-www-form-urlencoded`, required)

- `text` (string) — The text to be checked. This or 'data' is required.
- `data` (string) — The text to be checked, given as a JSON document that specifies what's text and what's markup. This or 'text' is required. Markup will be ignored when looking for errors. Example text: <pre>A &lt;b>test&lt;/b></pre>JSON for the example text: <pre>{"annotation":[ {"text": "A "}, {"markup": "&lt;b>"}, {"text": "test"}, {"markup": "&lt;/b>"} ]}</pre> <p>If you have markup that should be interpreted as whitespace, like <tt>&lt;p&gt;</tt> in HTML, you can have it interpreted like this: <pre>{"markup": "&lt;p&gt;", "interpretAs": "\n\n"}</pre><p>The 'data' feature is not limited to HTML or XML, it can be used for any kind of markup.
- `language` (string, required) — A language code like `en-US`, `de-DE`, `fr`, or `auto` to guess the language automatically (see `preferredVariants` below). For languages with variants (English, German, Portuguese) spell checking will only be activated when you specify the variant, e.g. `en-GB` instead of just `en`.
- `altLanguages` (string) — EXPERIMENTAL: Comma-separated list of language codes to check if a word is not similar to one of the main language (parameter `language`). Unknown words that are similar to a word from the main language will still be considered errors but with type `Hint`. For languages with variants (English, German, Portuguese) you need to specify the variant, e.g. `en-GB` instead of just `en`.
- `motherTongue` (string) — A language code of the user's native language, enabling false friends checks for some language pairs.
- `preferredVariants` (string) — Comma-separated list of preferred language variants. The language detector used with `language=auto` can detect e.g. English, but it cannot decide whether British English or American English is used. Thus this parameter can be used to specify the preferred variants like `en-GB` and `de-AT`. Only available with `language=auto`.
- `enabledRules` (string) — IDs of rules to be enabled, comma-separated
- `disabledRules` (string) — IDs of rules to be disabled, comma-separated
- `enabledCategories` (string) — IDs of categories to be enabled, comma-separated
- `disabledCategories` (string) — IDs of categories to be disabled, comma-separated
- `enabledOnly` (boolean) — If true, only the rules and categories whose IDs are specified with `enabledRules` or `enabledCategories` are enabled. Default: `false`.

**Responses**

- **200** — the result of checking the text

### GET /languages

**Get a list of supported languages.**

**Responses**

- **200** — An array of language objects.
  Body (`application/json`, array of object):
  - `name` (string, required) — a language name like 'French' or 'English (Australia)'
  - `code` (string, required) — a language code like 'en'
  - `longCode` (string, required) — a language code like 'en-US' or 'ca-ES-valencia'
