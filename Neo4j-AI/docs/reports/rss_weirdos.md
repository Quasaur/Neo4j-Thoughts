# RSS Feed Non-Compliant Entries

Audit date: 2026-02-13
Script: `backend/scripts/find_rss_weirdos.py`

## Thoughts with Multilingual Markers in `en_content` (13)

| content_id | thought_id | title           | slug            |
| ---------- | ---------- | --------------- | --------------- |
| 223        | 16         | DEATH ROW       | death-row       |
| 225        | 18         | DIVINE WORTH    | divine-worth    |
| 256        | 49         | UNFAIR          | unfair          |
| 285        | 78         | QUIET THE FLESH | quiet-the-flesh |
| 286        | 79         | SELF-DENIAL     | self-denial     |
| 346        | 139        | REACTION        | reaction        |
| 368        | 160        | FIRST RULE      | first-rule      |
| 376        | 168        | THE IRC         | the-irc         |
| 387        | 224        | ANOTHER SINNER  | another-sinner  |
| 392        | 229        | FORBIDDEN       | forbidden       |
| 393        | 230        | INSATIABLE      | insatiable      |
| 396        | 233        | SHOCKED         | shocked         |
| 397        | 234        | THE END OF EVIL | the-end-of-evil |

Markers found: `[!Thought-en]`, `[!Pensamiento-es]`, `[!Pensée-fr]`, `[!सोचा-hi]`, `[!思考-zh]`, etc.

## Quotes — 0 affected

## Passages — 0 affected

## zh_ Fields with Chinese Simplified Characters (1)

| table                | content_id | thought_id | zh_title | zh_content                             |
| -------------------- | ---------- | ---------- | -------- | -------------------------------------- |
| thoughts_app_content | 262        | 55         | 问责制   | 上帝不会让你免受我行为的后果。         |

## Resolution

- **Multilingual markers**: Excluded at the RSS feed queryset level via `_exclude_multilingual()` in `feeds.py`. Database values are preserved.
- **zh_ Chinese Simplified**: Corrected to Pinyin via one-time SQLite update.
