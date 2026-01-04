---
name: "thought.POWER AND WILL"
alias: "Thought: Power And Will"
type: THOUGHT
en_content: "We don't tap into God's Strength because we are not committed to executing God's Will."
parent: "topic.SPIRITUALITY"
tags:
- strength
- will
- commitment
- spirituality
- power
level: 2
neo4j: true
insert: true
---
# Power And Will

> [!Thought-en]
> We don't tap into God's Strength because we are not committed to executing God's Will.

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2010)
CREATE (t:THOUGHT {
    name: "thought.POWER AND WILL",
    alias: "Thought: Power And Will",
    parent: "topic.SPIRITUALITY",
    tags: ['strength', 'will', 'commitment', 'spirituality', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.POWER AND WILL",
    en_title: "Power And Will",
    en_content: "We don't tap into God's Strength because we are not committed to executing God's Will.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.POWER AND WILL" AND c.name = "content.POWER AND WILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.POWER AND WILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.POWER AND WILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >POWER AND WILL" }]->(child);
```