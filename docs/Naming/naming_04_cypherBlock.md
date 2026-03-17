---
type: agent
typeDesc: Instructions for artificial intelligence LLMs, agents and models.
creation: 27-Feb-2026@0942
title: Part 4 - Cypher Block Naming Conventions
version: 2
series: "Neo4j-Thoughts: Naming Conventions"
docStatus: COMPLETE
---
# Part 3 - The Cypher Block

## Introduction

This document defines the standard for what goes into the Cypher block of the markdown file for each node type.

Rule 1: The Cypher block consists of four queries; the first two queries are run together. After a brief pause the next two queries are run separately...one after the other.

Rule 1a: The first query creates the primary node as one of the four types (TOPIC, THOUGHT, QUOTE or PASSAGE).

Rule 1b: The second query creates the secondary node. The secondary node is defined as either the DESCRIPTION node (if the primary node is a TOPIC) or the CONTENT node (if the primary node is a THOUGHT, QUOTE or PASSAGE).

Rule 1c: The third query creates the relationship between the primary and secondary nodes.

Rule 1d: The fourth query creates the relationship between the primary node and its parent TOPIC node. The Developer ensures that the primary node's parent node already exists in the AuraDB instance before the queries in the Cypher block are executed against the AuraDB.

Rule 1e: Thought every primary node isn't a TOPIC node, every primary node has as its parent a TOPIC NODE.

Rule 1f: The Cyper block should have no more than one empty line between itself and the YAML front matter. Likewise each of the four Cypher queries in the Cypher block should be separated by no more than one empty line.

Rule 1g: The properties defined in docs/Naming/naming_03_yaml.md apply to the properties of the same identity that exist in the Cypher block.

The following rules define the values of the primary and secondary nodes as well as the properties of both the relationship between the primary and secondary nodes as well as the relationship between the primary node and its parent node.

  

## Primary Node
Rule 2: The Primary node's properties are replicated in the node markdown file's YAML front matter nearly verbatum (except for the type, en_content, ptopic and neo4j YAML properties.). This is done so that the Developer has an easy view of each file's Cypher block content from the Obsidian Base tables. Where a primary node's property exists in the YAML front matter, the YAML front matter is the source of truth.

Rule 2a: The last property of both the primary node (TOPIC, THOUGHT, QUOTE & PASSAGE) and the secondary node (DESCRIPTION or CONTENT) must not end with a comma, being the last property in the query.
#### Deprecated Properties
Rule 3: For the first CREATE query in the Cyper block the "notes" property has been deprecated from all primary node types (TOPIC, THOUGHT, QUOTE and PASSAGE) and must be removed by the agentic model wherever it is found and the line from which it was deleted in the Cypher CREATE query for the node removed so that there are no empty lines within the query.

### TOPIC Node Type Cypher Query
Rule 4: Every Cypher CREATE query for the TOPIC node type must have the following properties and their values:
	- name
	- alias
	- parent
	- tags
	- level


### THOUGHT Node Type
Rule 5: Like the TOPIC node type, every Cypher CREATE query for the THOUGHT node type must have the following properties and their values:
	- name
	- alias
	- parent
	- tags
	- level


### QUOTE Node Type
Rule 6: Every Cypher CREATE query for the QUOTE node type must have the following properties and their values:
	- name
	- alias
	- parent
	- tags
	- source
	- booklink
	- level

Rule 6a: There must be clear distinction between the QUOTE content and the QUOTE reference properties (source, booklink). That is to say the source and booklink properties of a quote should never be found in the value of any property of the QUOTE's CONTENT node.

Rule 6b: The value of the QUOTE property "source" should be enclosed only with double quotes (i.e., "The Narrow Way"), not double and single quotes (i.e., "'The Narrow Way'"). This rule applies to the YAML property "source" as well.

Rule 6c: The "booklink" property of the QUOTE node should be enclosed only in double quotes; if it is found to be enclosed in parentheses, they should be replaced by double quotes ("[URL]"). If both double quotes and parentheses include the booklink value's URL, the parentheses should be removed, leaving only the double quotes.

### PASSAGE Node Type
Rule 7: Every Cypher CREATE query for the PASSAGE node type must have the following properties and their values:
	- name
	- alias
	- parent
	- tags
	- source
	- sortedsource
	- biblelink
	- level

Rule 7a: There must be clear distinction between the PASSAGE content and the PASSAGE reference properties (source, sortedsource, biblelink). That is to say the source, sortedsource and biblelink properties of a PASSAGE should never be found in the value of any property of the PASSAGE's CONTENT node.

Rule 7b: The values of the source, sortedsource and biblelink properties of the PASSAGE node should each be enclosed in double quotes...not double and single quotes together, and not double quotes and parentheses.

## Secondary Node
Rule 8: The second Cypher CREATE query in the Cypher block creates the node that contains the actual content for the primary node, whether that is the DESCRIPTION of the TOPIC or the COTENT of the THOUGHT, QUERY or PASSAGE node.

Rule 8a: Whether referring to the DESCRIPTION node or CONTENT node, the value of the property "en_title" will be the same as that of the "alias" property of the primary node.

Rule 8b: The values of the properties "es_title", "fr_title", "hi_title" and "zh_title", whether they belong to a DESCRIPTION or CONTENT node, with be faithful translations in their respective languages (Spanish, French, Hini & Chinese Pinyin) of the value for the "en_title" property.
### DESCRIPTION Node Type
Rule 9: Every Cypher CREATE query for the DESCRIPTION node type must have the following properties and their values:
	- name
	- en_title
	- en_content
	- es_title
	- es_content
	- fr_title
	- fr_content
	- hi_title
	- hi_content
	- zh_title
	- zh_content

Rule 9a: the name content matches the name of the TOPIC node in the same Cypher block with one crucial difference: the first part of the name field is always "desc." instead of "topic.".

Rule 9b: The "en_title" property must use Initial Caps; this is true also of the same property in the CONTENT node type.
### CONTENT Node Type
Rule 10: Every Cypher CREATE query for the CONTENT node type must have the following properties and their values:
	- name
	- ctype
	- en_title
	- en_content
	- es_title
	- es_content
	- fr_title
	- fr_content
	- hi_title
	- hi_content
	- zh_title
	- zh_content

#### CONTENT "\*\_title" Properties
Rule 10a: All CONTENT properties whose labels end in "\_title" (en_title, es_title, fr_title, hi_title and zh_title) should have their values begin with the type of primary node they belong to in Initial Caps (i.e., "Quote: Nation of Israel" or "Thought: Act of God"), just as in the primary node's "alias" property.

Rule 10b: All CONTENT properties whose labels end in "_title" (en_title, es_title, fr_title, hi_title and zh_title) should have their values in either Initial Caps or their first word after the colon in Intial Caps and subsequent words in lower case.

#### CONTENT "\*\_content" Properties
Punctuation within the values of the CONTENT properties whose labels end in
"\_content" present a unique set of difficulties. This section seeks to simplify those complications as much as possible.

Rule 10c: the values of all CONTENT node properties that end with "\_content" (en_content, es_content, fr_content, hi_content and zh_content) must be enclosed in double quotes ("").

Rule 10d: If at all possible, only single quotes should be used within the value of CONTENT properties whose labels end with the word "content". 

Rule 10e: Escaped double quotes (a backslash followed by a double quote) and escaped single quotes (a backslash followed by a single quote) are allowed, if deemed necessary by the developer.

Rule 10f: Non-English translations do include their own special characters inside their values for any CONTENT property beginning with "es", "fr", "hi" or "zh"; this is allowed.

#### CONTENT: name Property
Rule 10g: The name content matches the name of the THOUGHT, QUOTE or PASSAGE node in the same Cypher block with one crucial difference: the first part of the name field is always "content." instead of "thought." or "quote." or "passage.".

#### CONTENT: ctype Property

Rule 10h: Because the CONTENT node type is the child of three node types (THOUGHT, QUOTE and PASSAGE) respectively, the property "ctype" was added to the CONTENT node to identify which of the three primary node types the CONTENT node was a child to. Originally the value of the ctype was an integer. The Developer has now decided that the value of the "ctype" will match the value of the YAML property "type". Unfortunately, not every CONTENT node has this field; therefore the agentic model must perform these operations:
	1. In those CONTENT nodes that have the "ctype" property, its value must be changed to match the value of the YAML property "type".
	2. For those CONTENT nodes missing the property "ctype", the property must be added to the CONTENT node on a new line between the "name" and "es_title" properties with a comma added to the end of the line containing the new "ctype" property entry.
Rule 10i: Following is an example of how the new entry should look:
```cypher
ctype: "THOUGHT",
```

#### CONTENT: en_content Property
Rule 10j: As stated in Rule 8b of the document [[docs/Naming/naming_03_yaml.md]], the value of the CONTENT property "en_content" should always ben enclosed with double quotes and end with appropriate punctuation (period, question mark or exclamation mark). If punctuation is missing from the end of the value, placing a period in most cases will resolve the issue.
#### CONTENT: zh_title Property
Rule 10k: For reasons unknown the CONTENT property "zh_title" will often have extra spaces after the colon character; there should only be one space after the colon character.

## Third Query: First Relationship 
### DESCRIPTION Relationship
Rule 11: The third Cypher query makes the DESCRIPTION node the child of the Cypher block's primary TOPIC node using the HAS_DESCRIPTION relationship type.

Rule 11a: The value of the "name" property of the relationship has two parts:
- the prefix "edge."
- the second part of the TOPIC node's name (.i.e., "ANTHROPOLOGY" of "topic.ANTHROPOLOGY").

Rule 11b: Following is an example of the part of the third Cypher query that contains the replationship's "name" field:
```cypher
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ANTHROPOLOGY"}]->(d);
```

### CONTENT Relationship
Rule 12: The third Cypher query makes the CONTENT node the child of the Cypher block's primary THOUGHT, QUOTE or PASSAGE node using the HAS_CONTENT relationship type.

#### THOUGHT to CONTENT
Rule 12a: The value of the "name" property of the THOUGHT to CONTENT relationship has two parts:
- the prefix "t.edge."
- the second part of the THOUGHT node's name (.i.e., "ADDICTION" of "thought.AADDICTION").

Rule 12b: Following is an example of the part of the third Cypher query that contains the replationship's "name" field:
```cypher
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ANTHROPOLOGY"}]->(d);
```

#### QUOTE to CONTENT
Rule 13: The value of the "name" property of the QUOTE to CONTENT relationship has two parts:
- the prefix "q.edge."
- the second part of the QUOTE node's name (.i.e., "BEGOTTEN" of "quote.ANTHROPOLOGY").

Rule 13b: Following is an example of the part of the third Cypher query that contains the replationship's "name" field:
```cypher
MERGE (t)-[:HAS_DESCRIPTION {name: "q.edge.BEGOTTEN"}]->(d);
```

#### PASSAGE to CONTENT
Rule 14: The value of the "name" property of the PASSAGE to CONTENT relationship has two parts:
- the prefix "p.edge."
- the second part of the PASSAGE node's name (.i.e., "FAITHLESSNESS" of "passage.FAITHLESSNESS").
```

## Fourth Query: Second Relationship
Rule 15: the fourth and last Cypher query creates the relationship between the primary node (of type TOPIC, THOUGHT, QUOTE or PASSAGE) and its parent topic (the value of the primary node's "parent" property).

### Primary TOPIC Node to Parent TOPIC Relationship
Rule 16: The fourth Cypher query makes the Cypher block's primary TOPIC node (created in the first query of the Cypher block) the child of the parent TOPIC identified in the primary TOPIC node's "parent" property using the HAS_CHILD relationship type.

#### First (MATCH) Statement
Rule 16a: The value of the first "name" property of the relationship has two parts:
- the prefix "topic."
- the second part of the parent TOPIC's "name" property, which consists of the second part of the parent TOPIC node's name (i.e., "COSMOLOGY" of "topic.COSMOLOGY"). The second part of the first name property must follow the rules of TOPIC names: only spaces are allowed between multiple CAPITAL WORDS...no underscores, spaces or dashes allowed.

Rule 16b: Following is an example of the part of the fourth cypher query that contains the first "name" property:
```cypher
MATCH (parent:TOPIC {name: "topic.COSMOLOGY");
```
#### Second (MATCH) Statement
Rule 16c: The value of the second "name" property of the relationship has two parts:
- the prefix "topic."
- the second part of the child TOPIC's "name" property, which consists of the second part of the child TOPIC node's name (i.e., "ASTROPHYSICS" of "topic.ASTROPHYSICS"). The second part of the second name property must follow the rules of TOPIC names: only spaces are allowed between multiple CAPITAL WORDS...no underscores, spaces or dashes allowed.

Rule 16d: Following is an example of the part of the fourth cypher query that contains the second "name" property:
```cypher
MATCH (child:TOPIC {name: "topic.COSMOLOGY");
```

#### Third (MERGE) Statement
Rule 16e: The value of the third "name" property of the relationship has two parts:
- the prefix "topic."
- the second part of the HAS_CHILD relationship's "name" property, which consists of the second part of the parent TOPIC node's name (i.e., "COSMOLOGY" of "topic.COSMOLOGY") connected to the second part of the primary TOPIC node's "name" property (i.e., "ASTROPHYSICS" of "topic.ASTROPHYISCS") by the characters "->". The second part of both the parent and child name properties must follow the rules of all node names: only spaces are allowed between multiple CAPITAL WORDS...no underscores, spaces or dashes allowed.


Rule 16f: Following is an example of the part of the fourth cypher query that contains the third "name" property:
```cypher
MERGE (p)-[:HAS_CHILD {name: "edge.COSMOLOGY->ASTROPHYSICS"}]->(c);
```

### Primary THOUGHT Node to Parent TOPIC Relationship
Rule 17: The fourth Cypher query makes the Cypher block's primary THOUGHT node (created in the first query of the Cypher block) the child of the parent TOPIC identified in the primary THOUGHT node's "parent" property using the HAS_THOUGHT relationship type.

#### Third (MERGE) Statement
Rule 17a: The value of the third "name" property of the relationship has two parts:
- the prefix "t.edge."
- the second part of the HAS_THOUGHT relationship's "name" property, which consists of the second part of the parent TOPIC node's name (i.e., "HUMANITY" of "topic.HUMANITY") connected to the second part of the primary THOUGHT node's "name" property (i.e., "ACCOUNTABILITY" of "thought.ACCOUNTABILITY") by the characters "->".

Rule 17b: Following is an example of the part of the fourth cypher query that contains the "name" property:
```cypher
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HUMANITY->ACCOUNTABILITY"}]->(child);
```

### Primary QUOTE Node to Parent TOPIC Relationship
Rule 18: The fourth Cypher query makes the Cypher block's primary QUOTE node (created in the first query of the Cypher block) the child of the parent TOPIC identified in the primary QUOTE node's "parent" property using the HAS_QUOTE relationship type.

### Primary PASSAGE Node to Parent TOPIC Relationship
Rule 19: The fourth Cypher query makes the Cypher block's primary PASSAGE node (created in the first query of the Cypher block) the child of the parent TOPIC identified in the primary PASSAGE node's "parent" property using the HAS_PASSAGE relationship type.

