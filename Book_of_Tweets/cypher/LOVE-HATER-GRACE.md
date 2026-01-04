---
name: "thought.LOVE HATER GRACE"
alias: "Thought: Love Hater Grace"
type: THOUGHT
en_content: "To love the one who loves you is pleasure. To love the one who ignores you is compassion. To love the one who hates you is Grace."
parent: "topic.GRACE"
tags:
- love
- hater
- grace
- character
- compassion
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013e)
CREATE (t:THOUGHT {
    name: "thought.LOVE HATER GRACE",
    alias: "Thought: Love Hater Grace",
    parent: "topic.GRACE",
    tags: ['love', 'hater', 'grace', 'character', 'compassion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LOVE HATER GRACE",
    en_title: "Love Hater Grace",
    en_content: "To love the one who loves you is pleasure. To love the one who ignores you is compassion. To love the one who hates you is Grace.",
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
WHERE t.name = "thought.LOVE HATER GRACE" AND c.name = "content.LOVE HATER GRACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVE HATER GRACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LOVE HATER GRACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LOVE HATER GRACE" }]->(child);
```
