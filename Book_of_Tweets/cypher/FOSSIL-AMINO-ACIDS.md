---
name: "thought.FOSSIL AMINO ACIDS"
alias: "Thought: Fossil Amino Acids"
type: THOUGHT
en_content: "Why is it that amino acids are still found in fossils and are not broken down after hundreds of millions of years?"
parent: "topic.CREATION"
tags:
- science
- biology
- fossils
- creation
- time
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Jul-2011)
CREATE (t:THOUGHT {
    name: "thought.FOSSIL AMINO ACIDS",
    alias: "Thought: Fossil Amino Acids",
    parent: "topic.CREATION",
    tags: ['science', 'biology', 'fossils', 'creation', 'time'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FOSSIL AMINO ACIDS",
    en_title: "Fossil Amino Acids",
    en_content: "Why is it that amino acids are still found in fossils and are not broken down after hundreds of millions of years?",
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
WHERE t.name = "thought.FOSSIL AMINO ACIDS" AND c.name = "content.FOSSIL AMINO ACIDS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FOSSIL AMINO ACIDS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.FOSSIL AMINO ACIDS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >FOSSIL AMINO ACIDS" }]->(child);
```
