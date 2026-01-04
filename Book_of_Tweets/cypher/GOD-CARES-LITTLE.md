---
name: "thought.GOD CARES LITTLE"
alias: "Thought: God Cares Little"
type: THOUGHT
en_content: "God cares about the little people. He made the big people to care for the little people."
parent: "topic.THE GODHEAD"
tags:
- compassion
- little_people
- care
- god
- divinity
level: 1
neo4j: true
insert: true
---
# God Cares Little

> [!Thought-en]
> God cares about the little people. He made the big people to care for the little people.

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD CARES LITTLE",
    alias: "Thought: God Cares Little",
    parent: "topic.THE GODHEAD",
    tags: ['compassion', 'little_people', 'care', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD CARES LITTLE",
    en_title: "God Cares Little",
    en_content: "God cares about the little people. He made the big people to care for the little people.",
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
WHERE t.name = "thought.GOD CARES LITTLE" AND c.name = "content.GOD CARES LITTLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD CARES LITTLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD CARES LITTLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD CARES LITTLE" }]->(child);
```