---
type: agent
typeDesc: Instructions for aritificial intelligence LLMs, agents and models.
creation: 27-Feb-2026@0946
title: "Part 3 - YAML Properties"
version: 2.0
series: "Neo4j-Thoughts: Naming Conventions"
docStatus: COMPLETE
---
# **Part 2 - YAML Properties**

Every compliant node file must contain certain YAML front matter based upon the node type as defined in the rules that follow.

Rule 1: The YAML front matter of every compliant node markdown file is identified by three dashes ('---') followed by a group of properties in the 'key: data' format and closed by a second set of three dashes ('---').

## Deprecated YAML Properties

Rule 2: Deprecated YAML properties include:

- "mling" (multilingual description or content exists)
- "draft" (node should be displayed on static site)
- "inserted" (this node has been uploaded to the AuraDB).

Rule 2a: These properties, if found in the YAML front matter of any markdown file, should be removed from the markdown file along with their values.

## Approved YAML Properties

Following are the approved YAML properties in the order they should appear. When this document is completed, it can be used to guide LLM / agentic models to execute compliance on local node markdown files in this Obsidian vault.

```yaml
type:
name:
alias:
parent:
en_content:
tags:
ptopic:
level:
neo4j:
```

### 1st YAML Property: "type"

Rule 3: The first YAML property listed in the front matter should be "type" and should have one of the following values:

- TOPIC
- THOUGHT
- QUOTE
- PASSAGE
Rule 3a: The purpose of the YAML property "type" is to identify which node type the Cypher block of the markdown file is designed to create. The "type" property exists only in the YAML section of the file and not in the file's Cypher block.

Rule 3b: the value of the YAML property "type" doesn't require enclosing double quotes.

### 2nd YAML Property: "name"

Rule 4: The second YAML property listed in the front matter should be "name" and conforms to the field of the same name in the markdown file's Cypher block as well as the Neo4j AuraDB instance. This property exists in TOPIC, THOUGHT, QUOTE and PASSAGE node types. DESCRIPTION & CONTENT node types also have the "name" field and follow the same naming convention rules:

- Rule 4a: The first part of the "name" field describes the node type:
 a. "topic."
 b. "thought."
 c. "quote."
 d. "passage."
 e. "desc." - (the DESCRIPTION node type's "name" field does not appear in the YAML front matter).
 f. "content." - (the CONTENT node type's "name" field does not appear in the YAML front matter).
 
- Rule 4b: The second part of the "name" field contains the name of the node in CAPITAL LETTERS (Initial Caps are not allowed) with words separated by spaces (this rule applies to both the YAML properies and the properties of the Cypher block). For this reason the YAML property "name" value must always be encased in double quotation marks:
 a. "topic.THE GODHEAD"
 b. "thought.EMPTINESS"
 c. "quote.THE DESIRE OF NATIONS"
 d. "passage.THE LORD GIVES"
 e. "desc.THE GODHEAD"
 f. "content.EMPTINESS"

Rule 4c: While most punctuation is allowed in the second part of the YAML property "name", underscores and dashes are not; this rule applies to both the YAML front matter and the Cypher block.

### 3rd YAML Property: "alias"

Rule 5: The third YAML property listed in the front matter should be "alias" and exists also in the Cypher block for the following node types:

- TOPIC
- THOUGHT
- QUOTE
- PASSAGE

Rule 5a: The "alias" field is used by The Book of Wisdom website in the Title View of all node detail pages.

Rule 5b: The format of the "alias" field is as follows:

- The first part of the "alias" field identifies the node type:
 a. "Topic: "
 b. "Thought: "
 c. "Quote: "
 d. "Passage: "
 
- The second part of the "alias" field identifies the title of the node in Initial Caps (words in full capitals are forbidden in the values of the "alias" property in both the YAML front matter and the Cypher block). Together with the node type, these two components form the "alias":
 a. "Topic: The Godhead"
 b. "Thought: Emptiness"
 c. "Quote: The Desire of Nations"
 d. "Passage: The Lord Gives"

Rule 5c: If the YAML properties "alias" and "title" both exist in the same markdown file, the "title" key and its value should be deleted and the "alias" property's value audited and, if necessary, refactored to conform to the rules set forth in Rule 5, 5a and 5b. At this point the "alias" key and value should be placed third in the YAML section of the markdown file.

Rule 5d: If the YAML property "title" exists without the "alias" property being present, the "title" key should be changed to "alias" and its value refactored to conform to the rules set forth in Rule 5, 5a and 5b. At this point the "alias" key and value should be placed third in the YAML section of the markdown file.

### 4th YAML Property: "parent"

Rule 6: The fourth YAML property listed in the front matter should be "parent" and exists in the following node types found in the Cypher block of the markdown file:

- TOPIC
- THOUGHT
- QUOTE
- PASSAGE

Rule 6a: the YAML property "parent" identifies the "name" field of the parent TOPIC, and therefore must follow the same naming convention as the "name" field of any node that contains that property.

### 5th YAML Property: "en_content"

Rule 7: The fifth YAML property listed in the front matter should be "en_content", which is added to enable the Developer to browse the English content of any DESCRIPTION or CONTENT node from the Obsidian.md app's Base tables. The "en_content" property exists only in the following node types:

- DESCRIPTION (for node type TOPIC)
- CONTENT (for node types THOUGHT, QUOTE & PASSAGE)

Rule 7a: The format of the value is demonstrated in the following YAML block:

```yaml
en_content: "This is example English content."
```

Rule 7b: The entire value for the YAML property "en_content" must be enclosed in double quotes.

Rule 7c: In the case of multi-line values for the YAML property "en_content", lines 2 and beyond must be tab-indented to be recognized by the Obsidian.md app as parts of the same value:

```yaml
en_content: "It’s why we eat when we’re not hungry.
 It’s why we watch hours of mindless television and play with ouija boards and horoscopes.
 It’s why we pursue one addiction after another, and there’s only One Cure that will fill that black hole in
 the core of our being: The Lord Jesus Christ.
 How insane it is, then, to attend Church for years and NEVER meet Jesus!!!"
```

Rule 7d: The following properties belong exclusively to the secondary node (DESCRIPTION or CONTENT) in the Cypher block and must NOT appear in the YAML front matter:

- es_title
- es_content
- fr_title
- fr_content
- hi_title
- hi_content
- zh_title
- zh_content
- en_title
- ctype
If any of these properties are found in the YAML front matter, the agentic model must remove them along with their values from the YAML section. Their values remain in the Cypher block's secondary node CREATE query where they belong.

Rule 7e: As a general principle, the YAML front matter must contain ONLY the nine approved properties listed in Rule 2's "Approved YAML Properties" block (type, name, alias, parent, en_content, tags, ptopic, level, neo4j) in the order specified. Any property not in this approved list — including trailing commas, leading spaces, or other formatting artifacts carried over from Cypher syntax — must be removed from the YAML section.

### 6th YAML Property: "tags"

Rule 8: The sixth YAML property listed in the front matter should be "tags" and exists in the following node types found in the Cypher Block section of the markdown file:

- TOPIC
- THOUGHT
- QUOTE
- PASSAGE

Rule 9: The YAML property "tags" is unique in that, unlike other YAML properties, its value consists of an array of five values which are keywords associated with the name and content of the containing node. Originally, the YAML property "tags" displays its array in the following format:

```yaml
tags:
- occult
- spirits
- evil
- law
- bible
```

However, in the Cypher query for the primary node, the format is:

```cypher
tags: ["occult", "spirits", "evil", "law", "bible"]
```

...followed by a comma to comply with Cypher language syntax.
To eliminate confusion and to ensure that all YAML front matter properties in node markdown files are in single-line format (except for the YAML property "en_content"), from this point forward, the YAML syntax for the "tags" property will be the following (displayed on its own line):

```yaml
tags: ["occult", "spirits", "evil", "law", "bible"]
```

Rule 9a: Whenever the agent find the YAML property "tags" in the original format, it must be changed to the new format.

Rule 9b: Every "tags" array entry that in both the YAML front matter and primary node CREATE query in the Cypher block (which is the first CREATE query in the Cypher block) that contains two or more English words set together without underscores, spaces or dashes should be formatted so that the words are separated by underscores:

```yaml
tags: ["mass_shootings", "gun_violence", "holy_spirit", "jesus_christ", "holy_bible"]
```

..and the same goes for the "tags" array in the Cypher block.

### 7th YAML Property: "ptopic"

Rule 10: The seventh YAML property listed in the front matter should be "ptopic" and exists only in the Obsidian app's YAML front matter for the markdown files of the following node types:

- TOPIC
- THOUGHT
- QUOTE
- PASSAGE

Rule 10a: The YAML property "ptopic" has no corresponding entry in the Neo4j AuraDB instance; its function is Obsidian-centric: it links to the Obsidian node markdown file containing the info for the current node's parent TOPIC. This enables the Developer to track and browse the relationships between the nodes in the Neo4j-Thoughts Obsidian vault, which has it's own graph view function similar to that of Neo4j. In the Book_of_Tweets folder in the Neo4j-Thoughts Obsidian vault, the YAML property "ptopic" was also used as a means to track which files in the Book_of_Tweets folder were ready to be uploaded to the Neo4j AuraDB instance and then moved to the corresponding subfolder in the content folder: if the YAML "ptopic" property's value had a valid link to a parent TOPIC's file, that meant its Cypher block was approved to be added to the AuraDB instance.

Rule 10b: Up till now the value of the YAML property "ptopic" has been manually added by the Developer in the course of auditing the contents of the Book_of_Tweets folder in the current Obsidian vault. Now, however, using the naming convention documentation in this series of files ("Neo4j-Thoughts: Naming Conventions"), the YAML "ptopic" property's value can now be added simbly by altering the punctuation of the YAML property "parent":

- parent: "topic.THE GODHEAD"
  would become
  ptopic: "[[topic-THE-GODHEAD]]"
- parent: "topic.FAITH"
  would become
  ptopic: "[[topic-FAITH]]"
...and so on.

### 8th YAML Property: "level"

Rule 11: The eighth YAML property listed in the front matter should be "level" and exists only in the Obsidian app's YAML front matter and as a property of the following node types in the Cypher block of each markdown file:

- TOPIC
- THOUGHT
- QUOTE
- PASSAGE

Rule 11a: The YAML property "level" contains an integer that represents the distance that exists in TOPIC nodes between the current node (TOPIC, THOUGHT, QUOTE OR PASSAGE) and the top-most node "topic.NULL TOPIC", which is level 0 (zero).

Rule 11b: The value of the YAML property "level" doesn't require enclosing double quotes.

### 9th YAML Property: "neo4j"

Rule 12: the ninth and last YAML property is "neo4j"...the value of which is boolean (either true or false). If the value of "neo4j" is true, the Cypher block of the markdown file is assumed to have already been uploaded to the Neo4j AuraDB instance; a value false means the file's Cypher block has not yet been executed against the AuraDB instance.

Rule 12a: The value of the YAML property "level" doesn't require enclosing double quotes.
