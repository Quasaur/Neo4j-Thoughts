# Naming & YAML Standards Discrepancy Report
Generated: 2026-03-04 17:15

## Executive Summary
An audit of the `content/` folder (491 files) against the standards established in `docs/Naming` revealed several systematic violations across file naming conventions, YAML front matter structure, and property formatting. 112 files were identified with one or more discrepancies.

## Systematic Violations

### 1. File Naming (Rule 1e - Duplicates)
Multiple files use non-standard numbering suffixes (`-2`, `2`, `5`) instead of the required `(n)` format.
- **Example:** `thought-VOLITION5.md` instead of `thought-VOLITION(5).md`
- **Affected files:** `VOLITION(2-5)`, `LOVE2`, `ULTIMATE2`, `CONSEQUENCES-2`, `MIRACLES-2`, `SECURITY-2`.

### 2. YAML Front Matter (Rule 7d - Property Scope)
Extensive presence of secondary node properties (`es_title`, `es_content`, `fr_title`, etc.) within the YAML front matter of primary node files, particularly in the `QUOTES/` and `THOUGHTS/` subfolders.
- **Standard:** These properties belong exclusively in the Cypher block's secondary (CONTENT/DESCRIPTION) node creation query.
- **Affected files:** Nearly all files in `content/QUOTES/to2/`, `content/QUOTES/imm/`, and several in `content/THOUGHTS/`.

### 3. YAML Property Formatting (Rules 4b, 5b, 10b)
- **Rule 4b (Name Formatting):** Several YAML `name` fields use dashes or underscores (e.g., `quote.HEAVENLY-FOOD`) instead of the required spaces (`quote.HEAVENLY FOOD`).
- **Rule 5b (Alias Formatting):** Use of full CAPITAL LETTERS in aliases (e.g., `Topic: The GODHEAD`) where Initial Caps are required.
- **Rule 10b (ptopic Formatting):** Invalid `ptopic` links, such as missing `[[]]` wrappers or using dots (e.g., `topic.BIOLOGY`) instead of dashes (e.g., `topic-BIOLOGY`).

### 4. General Principles (Rule 1d)
While noted as a general principle, several file names exceed the recommended four-word maximum.
- **Example:** `thought-THE-LAKE-OF-FIRE-AND-SULFUR.md` (6 words).

---

## Detailed Violations List (Selected)

| File Path | Discrepancy Description |
| :--- | :--- |
| `content/QUOTES/imm/quote-CONSEQUENCES-2.md` | Violation of Rule 1e: uses dash-number instead of (number). |
| `content/QUOTES/bom/quote-HEAVENLY-FOOD.md` | Rule 4b violation: `name` contains dashes; should use spaces. |
| `content/THOUGHTS/thought-EARTH-SPEED-SPACE.md` | Rule 10b violation: `ptopic` missing `[[]]` wrappers. |
| `content/THOUGHTS/thought-VOLITION5.md` | Violation of Rule 1e: trailing number instead of (number). |
| `content/THOUGHTS/thought-MEEK.md` | Rule 7e violation: Incorrect property order; unapproved `aliases` property. |
| `content/TOPICS/topic-THE-GODHEAD.md` | Rule 5b violation: Alias contains full caps words ("GODHEAD"). |
| `content/THOUGHTS/thought-HUMAN-BREATHS-DAILY.md` | Rule 10b violation: `ptopic` uses dot instead of dash. |
| `content/QUOTES/bom/quote-BEGOTTEN.md` | Invalid `ptopic` link `[[topic-THE]]` (should be `[[topic-THE-GOSPEL]]`). |
| `content/THOUGHTS/thought-692-189.md` | Inconsistent `name` property between YAML and Cypher MATCH queries. |

## Recommendation
A systematic batch refactoring is required to:
1. Rename files violating Rule 1e.
2. Strip forbidden secondary properties from YAML front matter.
3. Standardize `name`, `alias`, and `ptopic` formatting.
4. Correct YAML property order to match the approved list (type, name, alias, parent, en_content, tags, ptopic, level, neo4j).
