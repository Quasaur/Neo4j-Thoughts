---
name: "thought.HELL FIRE FOR DEVIL"
alias: "Thought: Hell Fire For Devil"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- hell
- devil
- god
- judgment
- divinity
level: 1
neo4j: true
insert: true
---
# Hell Fire For Devil

> [!Thought-en]
> Hell Fire wasn't made by the Devil...it was made for the Devil by God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.HELL FIRE FOR DEVIL",
    alias: "Thought: Hell Fire For Devil",
    parent: "topic.THE GODHEAD",
    tags: ['hell', 'devil', 'god', 'judgment', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.HELL FIRE FOR DEVIL",
    en_title: "Hell Fire For Devil",
    en_content: "Hell Fire wasn't made by the Devil...it was made for the Devil by God.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HELL FIRE FOR DEVIL" AND c.name = "content.HELL FIRE FOR DEVIL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HELL FIRE FOR DEVIL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.HELL FIRE FOR DEVIL"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >HELL FIRE FOR DEVIL" }]->(child);
```