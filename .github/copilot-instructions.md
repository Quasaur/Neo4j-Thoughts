# Agent Instructions for Neo4j-Thoughts Project

This file contains guidelines and rules for AI agents and models working in this repository.

---

## Python Script Organization Rules

All Python scripts in this project MUST be organized according to the following rules. When creating new Python scripts, place them in the appropriate folder based on their functionality.

### Folder Structure

```
python/
├── AuraDB/          # Scripts connecting to Neo4j AuraDB online instance
├── content/         # Scripts exclusive to content/ folder
├── Book_of_Tweets/  # Scripts exclusive to Book_of_Tweets/ folder
├── other/           # Scripts addressing BOTH content AND Book_of_Tweets
└── repo/            # Scripts addressing NEITHER content NOR Book_of_Tweets
```

### Classification Rules

Use this decision tree to determine where a script belongs:

1. **Does the script connect to Neo4j AuraDB online instance?**
   - Uses `GraphDatabase` from `neo4j` module
   - Connects to `neo4j+s://` URI
   - **→ Place in: `python/AuraDB/`**

2. **Does the script reference BOTH content/ AND Book_of_Tweets/ folders?**
   - Contains paths or references to both folders
   - **→ Place in: `python/other/`**

3. **Does the script reference ONLY the content/ folder?**
   - Works with `content/THOUGHTS/`, `content/TOPICS/`, `content/QUOTES/`, `content/PASSAGES/`
   - **→ Place in: `python/content/`**

4. **Does the script reference ONLY the Book_of_Tweets/ folder?**
   - Works exclusively with Book_of_Tweets content
   - **→ Place in: `python/Book_of_Tweets/`**

5. **Does the script reference NEITHER content/ NOR Book_of_Tweets/?**
   - General utility scripts, repo-wide analysis, etc.
   - **→ Place in: `python/repo/`**

### Before Creating Any Python Script

Before creating a new Python script, **always search the `python/` folder recursively** to check if an existing script will either:
1. Complete the planned operation as-is, or
2. Can be modified to complete the operation.

Only create a new script if no suitable existing script is found.

---

### Priority Order

When a script could fit multiple categories, use this priority:
1. **AuraDB connection** (highest priority)
2. BOTH folders (content + Book_of_Tweets)
3. content/ folder only
4. Book_of_Tweets/ folder only
5. NEITHER (lowest priority)

### Examples

| Script | References | Destination |
|--------|------------|-------------|
| `sync_thoughts.py` | Neo4j AuraDB + content/THOUGHTS | `python/AuraDB/` |
| `check_filenames.py` | content/ + Book_of_Tweets/ | `python/other/` |
| `add_verified_property.py` | content/ only | `python/content/` |
| `fix_book_of_tweets_pinyin.py` | Book_of_Tweets/ only | `python/Book_of_Tweets/` |
| `audit_naming.py` | Neither | `python/repo/` |

---

## Current Script Inventory

### python/AuraDB/ (16 scripts)
Scripts connecting to Neo4j AuraDB online instance:
- check_db.py
- cleanup_duplicates.py
- complete_auradb_export.py
- create_missing.py
- create_quotes.py
- final_report.py
- find_missing.py
- fix_naming.py
- fix_orphans.py
- investigate_orphans.py
- query_quotes_auradb.py
- sync_auradb_topics.py
- sync_neo4j.py
- sync_verified_thoughts.py
- verify_sync.py

### python/content/ (44 scripts)
Scripts exclusive to content/ folder:
- add_ptopic.py
- add_source_to_quotes.py
- add_verified_property.py
- apply_translations.py
- check_and_move_inserted_thoughts.py
- check_auradb_passages.py
- cleanup_thoughts.py
- consolidate_passages.py
- consolidate_quotes.py
- consolidate_topics.py
- convert_chinese_to_pinyin.py
- convert_to_obsidian_cypher.py
- convert_uninserted_to_obsidian_cypher.py
- create_missing_relationships.py
- debug_passage.py
- direct_translate.py
- execute_passage_neo4j_updates.py
- find_auradb_placeholders.py
- fix_broken_yaml.py
- fix_musicology_duplicates.py
- generate_complete_translations.py
- generate_passage_cypher_updates.py
- generate_translation_workbook.py
- get_next_batch.py
- investigate_musicology_duplicates.py
- query_auradb_status.py
- query_passage_neo4j.py
- query_thought_692_189.py
- scan_passage_translations.py
- standardize_aliases.py
- standardize_frontmatter.py
- standardize_level_order.py
- sync_corrected_thoughts.py
- sync_passages_final.py
- sync_passages_to_auradb.py
- translate_passages_free.py
- translate_placeholders.py
- translate_with_ai.py
- translation_controller.py
- update_auradb_translations.py
- verify_consolidation.py
- verify_passages.py
- verify_quotes.py
- verify_topic_levels.py

### python/Book_of_Tweets/ (29 scripts)
Scripts exclusive to Book_of_Tweets/ folder:
- add_ptopic_book_of_tweets.py
- apply_chinese_corrections.py
- batch_translate_helper.py
- batch_translate.py
- bulk_insert_all.py
- bulk_insert_thoughts.py
- check_yaml_frontmatter.py
- complete_translations.py
- execute_topic_music.py
- execute_topic_musicology.py
- extract_tweets.py
- find_chinese_simplified.py
- find_ptopic_files.py
- fix_book_of_tweets_levels.py
- fix_book_of_tweets_pinyin.py
- fix_edge_errors.py
- free_translate.py
- get_untranslated_files.py
- insert_ptopic_thoughts.py
- process_batch.py
- process_insert.py
- quote_frontmatter_fields.py
- scan_edge_errors.py
- translate_batch.py
- translate_direct.py
- translate_files.py
- update_natural_sciences_desc.py
- update_topic_music.py

### python/other/ (1 script)
Scripts addressing BOTH content/ AND Book_of_Tweets/:
- check_filenames.py

### python/repo/ (17 scripts)
Scripts addressing NEITHER content/ NOR Book_of_Tweets/:
- analyze_properties.py
- audit_naming.py
- check_auradb_duplicates.py
- check_missing_topics.py
- check_social_science_topics.py
- create_final_relationships.py
- delete_duplicate_cosmology.py
- delete_notes_property.py
- execute_neo4j_corrections.py
- final_verification.py
- generate_auradb_report.py
- generate_neo4j_corrections.py
- move_sociology_parent.py
- sync_local_content.py
- verify_relationships.py
- verify_sociology_description.py
- verify_synced_thoughts.py

---

*Last updated: 2026-03-17*
