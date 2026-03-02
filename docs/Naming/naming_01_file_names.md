---
type: agent
typeDesc: Instructions for aritificial intelligence LLMs, agents and models.
creation: 27-Feb-2026@0942
title: Part 1 - File Names
series: "Neo4j-Thoughts: Naming Conventions"
docStatus: COMPLETE
---
# **Part 1 - File Names**
The documents in this folder (~\Developer\Neo4j-Thoughts\docs) take precedence over all other markdown files in this repo that are of an earlier creation date.

Here are the rules set in stone for how markdown files in the Obsidian.md Vault named Neo4j-Thoughts should be named for the four primary node types (TOPIC, THOUGHT, QUOTE & PASSAGE).

Node type DESCRIPTION is defined inside TOPIC markdown files and node type CONTENT is defined inside of THOUGHT, QUOTE & PASSAGE markdown files.

It is important to understand the structure of the Neo4j-Thoughts Obsidian.md Vault. At this time there are only two folders in the Neo4j-Thoughts vault  that contain  nodes that A.I. agents and models should manage:

1. the content folder: every node markdown file in the content folder has at some point in the past been uploaded to the Neo4j AuraDB instance which is located in the Internet cloud.
2. the Book_of_Tweets folder: this folder contains node entries from the original book published on Amazon Kindle which have yet to be uploaded to the Neo4j AuraDB instance. These node files are being audited and edited to ensure their compliance with the rules established in this set of documents before they're uploaded to the Neo4j AuraDB instance.

Rule 1: The 1st part of each file name defines the node type:

- TOPIC: "topic-"
- THOUGHT: "thought-"
- QUOTE: "quote-"
- PASSAGE: "passage-"

Rule 2: The 2nd part of each file name defines the node name (always with CAPITAL LETTERS):

- TOPIC: "topic-NAME"
- THOUGHT: "thought-NAME"
- QUOTE: "quote-NAME"
- PASSAGE: "passage-NAME"

Rule 3: If a node name consists of two or more words, the words of the node name will be in CAPITAL LETTERS separated by dashes:

- TOPIC: "topic-NODE-NAME"
- THOUGHT: "thought-MY-NODE-NAME"
- QUOTE: "quote-I-YOU-HIM-HER"
- PASSAGE: "passage-THAT-NAME"

Rule 4: As a general principle, no node name should consist of more than four words in capitals.

Rule 5: Two files of the same node type (TOPIC, THOUGHT, QUOTE or PASSAGE) may have the same node name; however the 2nd, 3rd, etc. nodes with the same name must include after their name a sequential integer in parentheses:

- TOPIC: "topic-NAME"
- TOPIC: "topic-NAME(2)"
- TOPIC: "topic-NAME(3)"

Rule 6: All node files must have the .md extension:

- TOPIC: "topic-NAME.md"
- TOPIC: "topic-NODE-NAME.md"
- THOUGHT: "thought-MY-NODE-NAME.md"
- QUOTE: "quote-I-YOU-HIM-HER(5).md"