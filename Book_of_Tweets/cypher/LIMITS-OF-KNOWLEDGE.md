---
name: "thought.LIMITS OF KNOWLEDGE"
alias: "Thought: Limits Of Knowledge"
type: THOUGHT
en_content: "\"If any man thinks he knows anything, he does not yet know as he ought.\" -- The Apostle Paul"
parent: "topic.WISDOM"
tags:
- wisdom
- humility
- knowledge
- truth
- maturity
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.LIMITS OF KNOWLEDGE",
    alias: "Thought: Limits Of Knowledge",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'humility', 'knowledge', 'truth', 'maturity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LIMITS OF KNOWLEDGE",
    en_title: "Limits Of Knowledge",
    en_content: "\"If any man thinks he knows anything, he does not yet know as he ought.\" -- The Apostle Paul",
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
WHERE t.name = "thought.LIMITS OF KNOWLEDGE" AND c.name = "content.LIMITS OF KNOWLEDGE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIMITS OF KNOWLEDGE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.LIMITS OF KNOWLEDGE"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >LIMITS OF KNOWLEDGE" }]->(child);
```
