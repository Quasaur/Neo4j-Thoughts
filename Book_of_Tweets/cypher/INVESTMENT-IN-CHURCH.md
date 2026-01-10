---
name: "thought.INVESTMENT IN CHURCH"
alias: "Thought: Investment In Church"
type: THOUGHT
en_content: "If you put something into your church, you'll ALWAYS get something out!"
parent: "topic.RELIGION"
tags:
- church
- investment
- return
- religion
- community
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013e)
CREATE (t:THOUGHT {
    name: "thought.INVESTMENT IN CHURCH",
    alias: "Thought: Investment In Church",
    parent: "topic.RELIGION",
    tags: ['church', 'investment', 'return', 'religion', 'community'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INVESTMENT IN CHURCH",
    en_title: "Investment In Church",
    en_content: "If you put something into your church, you'll ALWAYS get something out!",
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
WHERE t.name = "thought.INVESTMENT IN CHURCH" AND c.name = "content.INVESTMENT IN CHURCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INVESTMENT IN CHURCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.INVESTMENT IN CHURCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >INVESTMENT IN CHURCH" }]->(child);
```
