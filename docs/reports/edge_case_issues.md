---
type: agent
typeDesc: Instructions for aritificial intelligence LLMs, agents and models.
creation: 02-Mar-2026@1421
title: Part 4 - Edge Cases
series: "Neo4j-Thoughts: Naming Conventions"
docStatus: Editing
---
# Part 4 - Edge Cases
This document addresses the edge cases identified in the docs/reports/unaddressed_isues_02-Mar-2026@1415.

## Special Characters in Names
The standards say node names are CAPITAL LETTERS with words separated by spaces," but there's no rule specifying what an agent should do if it encounters commas, colons, or question marks in existing node names (e.g., `thought.692,189` or `thought.INVITE_OR_COMMAND?`). 

### Q:
Should they be stripped out, or are they allowed?

## A:
These issues are addressed in documents 03 & 04 in the docs/Naming folder.

## Duplicate Concept Resolution Strategy
While Rule 5 covers file numbering (`(2)`, `(3)`) for non-unique names, there is still no rule telling an agent how to merge or handle logically identical variants currently sitting in AuraDB.

### Q:
If both `THE ULTIMATE` and `THE_ULTIMATE` exist, which one survives and how do we resolve the relationships of the one being deleted?).

### A:
The node with the younger creation date is removed; the remaining node is tested against the documents in the docs/Naming folder and refactored to be compliant with the aforementioned documents.


    
## Orphaned AuraDB Nodes & Sync Integrity (`neo4j: true`)
There's no protocol outlined for handling nodes that exist in AuraDB but have no markdown file at all, nor any instructions for reconciling files that have `neo4j: true` but are actually missing from the database.

## A:
Any nodes in the AuraDB that have no corresponding definition in the Cypher block of any markdown file in the Neo4j-Thoughts Obsidian folder and repo should have its contents copied to a markdown file in the AuraDB folder of the Neo4j-Thoughts Obsidian vault. The Developer will examine these file and determine a course of action.

