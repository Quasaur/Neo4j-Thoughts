---
type: agent
typeDesc: Instructions for aritificial intelligence LLMs, agents and models.
creation: 27-Feb-2026@0942
title: "Part 2 - File Names"
version: 2.0
series: "Neo4j-Thoughts: Naming Conventions"
docStatus: COMPLETE
---
# **Part 1 - File Names**
The documents in this folder (~\Developer\Neo4j-Thoughts\docs) take precedence over all other markdown files in this repo that are of an earlier creation date.

This document has been revised according to the principles set forth in the document docs/Naming/naming_01_neo4j_specs.md

Here are the rules set in stone for how markdown files designed for the Neo4j AuraDB instance created for The Book of Wisdom website (their file names, YAML front matter and Cypher block contents) in the Obsidian app Vault named Neo4j-Thoughts should be named for the four primary node types (TOPIC, THOUGHT, QUOTE & PASSAGE) and the two secondary node types (DESCRIPTION & CONTENT).

Node type DESCRIPTION is defined inside TOPIC markdown files and node type CONTENT is defined inside of THOUGHT, QUOTE & PASSAGE markdown files.

It is important to understand the structure of the Neo4j-Thoughts Obsidian.md Vault. At this time there are only two folders in the Neo4j-Thoughts vault  that contain  nodes that A.I. agents and models should manage:

1. the content folder: every node markdown file in the content folder has at some point in the past been uploaded to the Neo4j AuraDB instance which is located in the Internet cloud.
2. the Book_of_Tweets folder: this folder contains node entries from the original book published on Amazon Kindle which have yet to be uploaded to the Neo4j AuraDB instance. These node files are being audited and edited to ensure their compliance with the rules established in this set of documents before they're uploaded to the Neo4j AuraDB instance.

Rule 1: The 1st part of each file name defines the node type:
- TOPIC files: "topic-"
- THOUGHT files: "thought-"
- QUOTE files: "quote-"
- PASSAGE files: "passage-"

Rule 1a: The 2nd part of each file name defines the node name (always with CAPITAL LETTERS):
- TOPIC: "topic-NAME"
- THOUGHT: "thought-NAME"
- QUOTE: "quote-NAME"
- PASSAGE: "passage-NAME"

Rule 1b: the 3rd part of the file name contains the extension (i.e., ".md"); complete file names would be saved thus:
- TOPIC: "topic-NAME.md"
- THOUGHT: "thought-NAME.md"
- QUOTE: "quote-NAME.md"
- PASSAGE: "passage-NAME.md"

Rule 1c: If a node name consists of two or more words, the words of the node name (as displayed in the file name) will be in CAPITAL LETTERS separated by dashes:
- TOPIC: "topic-NODE-NAME.md"
- THOUGHT: "thought-MY-NODE-NAME.md"
- QUOTE: "quote-I-YOU-HIM-HER.md"
- PASSAGE: "passage-THAT-NAME.md"

Rule 1d: As a general principle, no node name should consist of more than four words in capitals.

Rule 1e: Two files of the same node type (TOPIC, THOUGHT, QUOTE or PASSAGE) may have the same node name; however the 2nd, 3rd, etc. nodes with the same name must include after their name a sequential integer in parentheses:

- TOPIC: "topic-NAME"
- TOPIC: "topic-NAME(2)"
- TOPIC: "topic-NAME(3)"
