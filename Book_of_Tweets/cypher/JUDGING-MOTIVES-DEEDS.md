---
name: "thought.JUDGING MOTIVES DEEDS"
alias: "Thought: Judging Motives Deeds"
type: THOUGHT
en_content: "While your neighbor is looking at your deeds to judge your motives, God is looking at your motives to judge your deeds!"
parent: "topic.THE GODHEAD"
tags:
- motives
- deeds
- judgment
- god
- perspective
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jul-2012)
CREATE (t:THOUGHT {
    name: "thought.JUDGING MOTIVES DEEDS",
    alias: "Thought: Judging Motives Deeds",
    parent: "topic.THE GODHEAD",
    tags: ['motives', 'deeds', 'judgment', 'god', 'perspective'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.JUDGING MOTIVES DEEDS",
    en_title: "Judging Motives Deeds",
    en_content: "While your neighbor is looking at your deeds to judge your motives, God is looking at your motives to judge your deeds!",
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
WHERE t.name = "thought.JUDGING MOTIVES DEEDS" AND c.name = "content.JUDGING MOTIVES DEEDS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JUDGING MOTIVES DEEDS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.JUDGING MOTIVES DEEDS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >JUDGING MOTIVES DEEDS" }]->(child);
```
