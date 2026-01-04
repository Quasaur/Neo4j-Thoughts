---
name: "thought.DANGEROUS AND SAFE"
alias: "Thought: Dangerous And Safe"
type: THOUGHT
en_content: "Who is more dangerous than God? Who is more safe than The Almighty?"
parent: "topic.THE GODHEAD"
tags:
- god
- majesty
- safety
- danger
- power
level: 1
neo4j: true
insert: true
---
# Dangerous And Safe

> [!Thought-en]
> Who is more dangerous than God? Who is more safe than The Almighty?

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jan-2012c)
CREATE (t:THOUGHT {
    name: "thought.DANGEROUS AND SAFE",
    alias: "Thought: Dangerous And Safe",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'majesty', 'safety', 'danger', 'power'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.DANGEROUS AND SAFE",
    en_title: "Dangerous And Safe",
    en_content: "Who is more dangerous than God? Who is more safe than The Almighty?",
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
WHERE t.name = "thought.DANGEROUS AND SAFE" AND c.name = "content.DANGEROUS AND SAFE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DANGEROUS AND SAFE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.DANGEROUS AND SAFE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >DANGEROUS AND SAFE" }]->(child);
```