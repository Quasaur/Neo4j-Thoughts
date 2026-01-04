---
name: "thought.STANDARD MODEL HOLES"
alias: "Thought: Standard Model Holes"
type: THOUGHT
en_content: "The holes in the Standard Model, irreducible and specific complexity, the lack of transitional links in the fossil record...take your pick."
parent: "topic.PHILOSOPHY"
tags:
- science
- philosophy
- creation
- complexity
- truth
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010e)
CREATE (t:THOUGHT {
    name: "thought.STANDARD MODEL HOLES",
    alias: "Thought: Standard Model Holes",
    parent: "topic.PHILOSOPHY",
    tags: ['science', 'philosophy', 'creation', 'complexity', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.STANDARD MODEL HOLES",
    en_title: "Standard Model Holes",
    en_content: "The holes in the Standard Model, irreducible and specific complexity, the lack of transitional links in the fossil record...take your pick.",
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
WHERE t.name = "thought.STANDARD MODEL HOLES" AND c.name = "content.STANDARD MODEL HOLES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.STANDARD MODEL HOLES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.STANDARD MODEL HOLES"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >STANDARD MODEL HOLES" }]->(child);
```
