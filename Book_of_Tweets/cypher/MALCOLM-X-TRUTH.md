---
name: "thought.MALCOLM X TRUTH"
alias: "Thought: Malcolm X Truth"
type: THOUGHT
en_content: "Malcolm X loved his people enough to tell them the Truth about themselves."
parent: "topic.HUMANITY"
tags:
- truth
- leadership
- love
- humanity
- justice
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-May-2011)
CREATE (t:THOUGHT {
    name: "thought.MALCOLM X TRUTH",
    alias: "Thought: Malcolm X Truth",
    parent: "topic.HUMANITY",
    tags: ['truth', 'leadership', 'love', 'humanity', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MALCOLM X TRUTH",
    en_title: "Malcolm X Truth",
    en_content: "Malcolm X loved his people enough to tell them the Truth about themselves.",
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
WHERE t.name = "thought.MALCOLM X TRUTH" AND c.name = "content.MALCOLM X TRUTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MALCOLM X TRUTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.MALCOLM X TRUTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >MALCOLM X TRUTH" }]->(child);
```
