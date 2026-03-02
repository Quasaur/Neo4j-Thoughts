---
type: agent
typeDesc: Instructions for aritificial intelligence LLMs, agents and models.
creation: 27-Feb-2026@0942
title: "Part 3 - Cypher Block Naming Conventions"
series: "Neo4j-Thoughts: Naming Conventions"
docStatus: COMPLETE
---
**# Part 3 - The Cypher Block**

**## Introduction**

This document defines the standard for what goes into the Cypher block of the markdown file for each node type.

Rule 1: The Cypher block consists of four queries; the first two queries are run together. After a brief pause the next two queries are run separately...one after the other.

Rule 2: The first query creates the primary node as one of the four types (TOPIC, THOUGHT, QUOTE or PASSAGE).

Rule 3: The second query creates the secondary node. The secondary node is defined as either the DESCRIPTION node (if the primary node is a TOPIC) or the CONTENT node (if the primary node is a THOUGHT, QUOTE or PASSAGE).

Rule 4: The third query creates the relationship between the primary and secondary nodes.

Rule 5: The fourth query creates the relationship between the primary node and its parent TOPIC node. The Developer ensures that the primary node's parent node already exists in the AuraDB instance before the queries in the Cypher block are executed against the AuraDB.

Rule 6: Thought every primary node isn't a TOPIC node, every primary node has as its parent a TOPIC NODE.

Rule 7: The Cyper block should have no more than one empty line between itself and the YAML front matter. Likewise each of the four Cypher queries in the Cypher block should be separated by no more than one empty line.

The following rules define the values of the primary and secondary nodes as well as the properties of both the relationship between the primary and secondary nodes as well as the relationship between the primary node and its parent node.

  

## Primary Node
Rule 8: The Primary node's properties are replicated in the node markdown file's YAML front matter nearly verbatum (except for the type, en_content, ptopic and neo4j YAML properties.). This is done so that the Developer has an easy view of each file's content from the Obsidian Base tables. Where a primary node's property exists in the YAML front matter, the YAML front matter is the source of truth.

#### Deprecated Properties
Rule 9: For the first CREATE query in the Cyper block the "notes" property has been deprecated from all primary node types (TOPIC, THOUGHT, QUOTE and PASSAGE) and must be removed by the agentic model wherever it is found and the line from which it was deleted in the Cypher CREATE query for the node removed so that there are no empty lines within the query.

### TOPIC Node Type Cypher Query
Rule 10: Every Cypher CREATE query for the TOPIC node type must have the following properties and their values:
	- name
	- alias
	- parent
	- tags
	- level

### THOUGHT Node Type
Rule 11: Like the TOPIC node type, every Cypher CREATE query for the THOUGHT node type must have the following properties and their values:
	- name
	- alias
	- parent
	- tags
	- level

### QUOTE Node Type
Rule 12: Every Cypher CREATE query for the QUOTE node type must have the following properties and their values:
	- name
	- alias
	- parent
	- tags
	- source
	- booklink
	- level

### PASSAGE Node Type
Rule 13: Every Cypher CREATE query for the PASSAGE node type must have the following properties and their values:
	- name
	- alias
	- parent
	- tags
	- source
	- sortedsource
	- biblelink
	- level


## Secondary Node
The second Cypher CREATE query in the Cypher block creates the node that contains the actual content for the primary node, whether that is the DESCRIPTION of the TOPIC or the COTENT of the THOUGHT, QUERY or PASSAGE node.

### DESCRIPTION Node Type
Rule 14: Every Cypher CREATE query for the DESCRIPTION node type must have the following properties and their values:
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

Rule 15: the name content matches the name of the TOPIC node in the same Cypher block with one crucial difference: the first part of the name field is always "desc." instead of "topic.".

### CONTENT Node Type
Rule 16: Every Cypher CREATE query for the CONTENT node type must have the following properties and their values:
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

Rule 17: the name content matches the name of the THOUGHT, QUOTE or PASSAGE node in the same Cypher block with one crucial difference: the first part of the name field is always "content." instead of "thought." or "quote." or "passage.".

Rule 18: Because the CONTENT node type is the child of three node types (THOUGHT, QUOTE and PASSAGE) respectively, the property "ctype" was added to the CONTENT node to identify which of the three primary node types the CONTENT node was a child to. Originally the value of the ctype was an integer. The Developer has now decided that the value of the "ctype" will match the value of the YAML property "type". Unfortunately, not every CONTENT node has this field; therefore the agentic model must perform these operations:
	1. In those CONTENT nodes that have the "ctype" property, its value must be changed to match the value of the YAML property "type".
	2. For those CONTENT nodes missing the property "ctype", the property must be added to the CONTENT node on a new line between the "name" and "es_title" properties with a comma added to the end of the line containing the new "ctype" property entry.
RULE 18a: Following is an example of how the new entry should look:
```cypher
ctype: "THOUGHT",
```

## First Relationship 
Rule 19: The fourth Cypher query makes the DESCRIPTION or CONTENT node the child of the Cypher blocks
  

## Second Relationship