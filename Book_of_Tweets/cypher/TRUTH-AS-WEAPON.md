---
name: "thought.TRUTH AS WEAPON"
alias: "Thought: Truth As Weapon"
type: THOUGHT
en_content: "Truth is a weapon far more dangerous than the hydrogen bomb."
parent: "topic.TRUTH"
tags:
- truth
- power
- weapon
- danger
- reality
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.TRUTH AS WEAPON",
    alias: "Thought: Truth As Weapon",
    parent: "topic.TRUTH",
    tags: ['truth', 'power', 'weapon', 'danger', 'reality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TRUTH AS WEAPON",
    en_title: "Truth As Weapon",
    en_content: "Truth is a weapon far more dangerous than the hydrogen bomb.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRUTH AS WEAPON" AND c.name = "content.TRUTH AS WEAPON"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRUTH AS WEAPON" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.TRUTH AS WEAPON"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >TRUTH AS WEAPON" }]->(child);
```
