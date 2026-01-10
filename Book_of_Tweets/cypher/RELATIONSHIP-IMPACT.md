---
name: "thought.RELATIONSHIP IMPACT"
alias: "Thought: Relationship Impact"
type: THOUGHT
en_content: "You are either a beneficiary or a casualty of my relationship with God."
parent: "topic.SPIRITUALITY"
tags:
- spirituality
- influence
- relationship
- god
- witness
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Jul-2010)
CREATE (t:THOUGHT {
    name: "thought.RELATIONSHIP IMPACT",
    alias: "Thought: Relationship Impact",
    parent: "topic.SPIRITUALITY",
    tags: ['spirituality', 'influence', 'relationship', 'god', 'witness'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.RELATIONSHIP IMPACT",
    en_title: "Relationship Impact",
    en_content: "You are either a beneficiary or a casualty of my relationship with God.",
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
WHERE t.name = "thought.RELATIONSHIP IMPACT" AND c.name = "content.RELATIONSHIP IMPACT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RELATIONSHIP IMPACT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.RELATIONSHIP IMPACT"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >RELATIONSHIP IMPACT" }]->(child);
```
