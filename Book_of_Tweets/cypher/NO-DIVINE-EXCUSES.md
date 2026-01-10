---
name: "thought.NO DIVINE EXCUSES"
alias: "Thought: No Divine Excuses"
type: THOUGHT
en_content: "God can and will forgive anything...but He will not excuse anything."
parent: "topic.THE GODHEAD"
tags:
- forgiveness
- excuse
- character
- god
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Nov-2012)
CREATE (t:THOUGHT {
    name: "thought.NO DIVINE EXCUSES",
    alias: "Thought: No Divine Excuses",
    parent: "topic.THE GODHEAD",
    tags: ['forgiveness', 'excuse', 'character', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NO DIVINE EXCUSES",
    en_title: "No Divine Excuses",
    en_content: "God can and will forgive anything...but He will not excuse anything.",
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
WHERE t.name = "thought.NO DIVINE EXCUSES" AND c.name = "content.NO DIVINE EXCUSES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NO DIVINE EXCUSES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NO DIVINE EXCUSES"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NO DIVINE EXCUSES" }]->(child);
```
