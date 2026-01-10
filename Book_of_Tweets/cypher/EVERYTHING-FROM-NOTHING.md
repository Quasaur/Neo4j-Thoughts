---
name: "thought.EVERYTHING FROM NOTHING"
alias: "Thought: Everything From Nothing"
type: THOUGHT
en_content: "Saying that everything came from nothing makes no sense."
parent: "topic.TRUTH"
tags:
- truth
- origin
- science
- creation
- logic
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.EVERYTHING FROM NOTHING",
    alias: "Thought: Everything From Nothing",
    parent: "topic.TRUTH",
    tags: ['truth', 'origin', 'science', 'creation', 'logic'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EVERYTHING FROM NOTHING",
    en_title: "Everything From Nothing",
    en_content: "Saying that everything came from nothing makes no sense.",
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
WHERE t.name = "thought.EVERYTHING FROM NOTHING" AND c.name = "content.EVERYTHING FROM NOTHING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EVERYTHING FROM NOTHING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.EVERYTHING FROM NOTHING"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >EVERYTHING FROM NOTHING" }]->(child);
```
