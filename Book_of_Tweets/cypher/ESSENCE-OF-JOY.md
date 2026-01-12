---
name: "thought.ESSENCE OF JOY"
alias: "Thought: Essence Of Joy"
type: THOUGHT
en_content: "The essence of Joy is to discover that God is more wonderful, more great and more important than I."
parent: "topic.ATTITUDE"
tags:
- joy
- god
- majesty
- discovery
- attitude
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.ESSENCE OF JOY",
    alias: "Thought: Essence Of Joy",
    parent: "topic.ATTITUDE",
    tags: ['joy', 'god', 'majesty', 'discovery', 'attitude'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ESSENCE OF JOY",
    en_title: "Essence Of Joy",
    en_content: "The essence of Joy is to discover that God is more wonderful, more great and more important than I.",
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
WHERE t.name = "thought.ESSENCE OF JOY" AND c.name = "content.ESSENCE OF JOY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ESSENCE OF JOY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ESSENCE OF JOY"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >ESSENCE OF JOY" }]->(child);
```
