---
name: "thought.THE BRINK OF EXTINCTION"
alias: "Thought: The Brink Of Extinction"
type: THOUGHT
en_content: "Matthew 24:21, 22: It may be that Christ will not return until humanity is on the brink of extinction."
parent: "topic.THE GODHEAD"
tags:
- prophecy
- christ
- return
- humanity
- judgment
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Dec-2010)
CREATE (t:THOUGHT {
    name: "thought.THE BRINK OF EXTINCTION",
    alias: "Thought: The Brink Of Extinction",
    parent: "topic.THE GODHEAD",
    tags: ['prophecy', 'christ', 'return', 'humanity', 'judgment'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE BRINK OF EXTINCTION",
    en_title: "The Brink Of Extinction",
    en_content: "Matthew 24:21, 22: It may be that Christ will not return until humanity is on the brink of extinction.",
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
WHERE t.name = "thought.THE BRINK OF EXTINCTION" AND c.name = "content.THE BRINK OF EXTINCTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE BRINK OF EXTINCTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.THE BRINK OF EXTINCTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >THE BRINK OF EXTINCTION" }]->(child);
```
