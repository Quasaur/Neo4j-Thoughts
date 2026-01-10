---
name: "thought.DEFINE EXQUISITAGIOUS"
alias: "Thought: Define Exquisitagious"
type: THOUGHT
en_content: "New Word: exquisitagious Meaning: something so exquisite that the feeling's contagious!"
parent: "topic.BEAUTY"
tags:
- beauty
- language
- humor
- contagious
- aesthetics
level: 6
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012d)
CREATE (t:THOUGHT {
    name: "thought.DEFINE EXQUISITAGIOUS",
    alias: "Thought: Define Exquisitagious",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'language', 'humor', 'contagious', 'aesthetics'],
    notes: "",
    level: 6
});

CREATE (c:CONTENT {
    name: "content.DEFINE EXQUISITAGIOUS",
    en_title: "Define Exquisitagious",
    en_content: "New Word: exquisitagious Meaning: something so exquisite that the feeling's contagious!",
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
WHERE t.name = "thought.DEFINE EXQUISITAGIOUS" AND c.name = "content.DEFINE EXQUISITAGIOUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE EXQUISITAGIOUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.DEFINE EXQUISITAGIOUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY >DEFINE EXQUISITAGIOUS" }]->(child);
```
