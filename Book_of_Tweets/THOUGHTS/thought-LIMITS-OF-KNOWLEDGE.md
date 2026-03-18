---
type: THOUGHT
name: "thought.LIMITS OF KNOWLEDGE"
alias: "Thought: Limits Of Knowledge"
parent: "topic.WISDOM"
en_content: "\"If any man thinks he knows anything, he does not yet know as he ought.\" -- The Apostle Paul"
tags: ["wisdom", "humility", "knowledge", "truth", "maturity"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Nov-2011)
CREATE (t:THOUGHT {    name: "thought.LIMITS OF KNOWLEDGE",
    alias: "Thought: Limits Of Knowledge",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'humility', 'knowledge', 'truth', 'maturity'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.LIMITS OF KNOWLEDGE",
    ctype: "THOUGHT",
    en_title: "Limits Of Knowledge",
    en_content: "\"If any man thinks he knows anything, he does not yet know as he ought.\" -- The Apostle Paul",
    es_title: "Límites del conocimiento",
    es_content: "\",
    fr_title: "Limites de la connaissance",
    fr_content: "\",
    hi_title: "ज्ञान की सीमा",
    hi_content: "\",
    zh_title: "zhī shí de jú xiàn xìng",
    zh_content: "\"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIMITS OF KNOWLEDGE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->LIMITS OF KNOWLEDGE"
RETURN t, parent;
```
