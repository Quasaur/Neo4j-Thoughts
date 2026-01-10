---
name: "thought.COOKED FOOD HUMANS"
alias: "Thought: Cooked Food Humans"
type: THOUGHT
en_content: "Why are humans the only creatures on planet earth that eat cooked food?"
parent: "topic.CREATION"
tags:
- creation
- humanity
- nature
- food
- mystery
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-May-2012a)
CREATE (t:THOUGHT {
    name: "thought.COOKED FOOD HUMANS",
    alias: "Thought: Cooked Food Humans",
    parent: "topic.CREATION",
    tags: ['creation', 'humanity', 'nature', 'food', 'mystery'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.COOKED FOOD HUMANS",
    en_title: "Cooked Food Humans",
    en_content: "Why are humans the only creatures on planet earth that eat cooked food?",
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
WHERE t.name = "thought.COOKED FOOD HUMANS" AND c.name = "content.COOKED FOOD HUMANS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COOKED FOOD HUMANS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.COOKED FOOD HUMANS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >COOKED FOOD HUMANS" }]->(child);
```
