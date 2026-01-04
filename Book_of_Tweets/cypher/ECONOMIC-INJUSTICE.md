---
name: "thought.ECONOMIC INJUSTICE"
alias: "Thought: Economic Injustice"
type: THOUGHT
en_content: "This economic downturn is especially difficult for African Americans; we're the last to get hired and the 1st to get fired."
parent: "topic.MORALITY"
tags:
- justice
- economy
- society
- race
- morality
level: 3
neo4j: true
insert: true
---
# Economic Injustice

> [!Thought-en]
> This economic downturn is especially difficult for African Americans; we're the last to get hired and the 1st to get fired.

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Nov-2010a)
CREATE (t:THOUGHT {
    name: "thought.ECONOMIC INJUSTICE",
    alias: "Thought: Economic Injustice",
    parent: "topic.MORALITY",
    tags: ['justice', 'economy', 'society', 'race', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ECONOMIC INJUSTICE",
    en_title: "Economic Injustice",
    en_content: "This economic downturn is especially difficult for African Americans; we're the last to get hired and the 1st to get fired.",
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
WHERE t.name = "thought.ECONOMIC INJUSTICE" AND c.name = "content.ECONOMIC INJUSTICE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ECONOMIC INJUSTICE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.ECONOMIC INJUSTICE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >ECONOMIC INJUSTICE" }]->(child);
```