---
name: "thought.SPECIFIED COMPLEXITY"
alias: "Thought: Specified Complexity"
type: THOUGHT
en_content: "Evolution can't explain Specified Complexity."
parent: "topic.CREATION"
tags:
- creation
- complexity
- design
- evolution
- intelligence
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010a)
CREATE (t:THOUGHT {
    name: "thought.SPECIFIED COMPLEXITY",
    alias: "Thought: Specified Complexity",
    parent: "topic.CREATION",
    tags: ['creation', 'complexity', 'design', 'evolution', 'intelligence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPECIFIED COMPLEXITY",
    en_title: "Specified Complexity",
    en_content: "Evolution can't explain Specified Complexity.",
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
WHERE t.name = "thought.SPECIFIED COMPLEXITY" AND c.name = "content.SPECIFIED COMPLEXITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPECIFIED COMPLEXITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SPECIFIED COMPLEXITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >SPECIFIED COMPLEXITY" }]->(child);
```
