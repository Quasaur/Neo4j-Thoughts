---
name: "thought.OVERCOMING FEAR BLAME"
alias: "Thought: Overcoming Fear Blame"
type: THOUGHT
en_content: "If you keep blaming others for your fears, you'll never overcome them."
parent: "topic.ATTITUDE"
tags:
- fear
- blame
- attitude
- courage
- character
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.OVERCOMING FEAR BLAME",
    alias: "Thought: Overcoming Fear Blame",
    parent: "topic.ATTITUDE",
    tags: ['fear', 'blame', 'attitude', 'courage', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.OVERCOMING FEAR BLAME",
    en_title: "Overcoming Fear Blame",
    en_content: "If you keep blaming others for your fears, you'll never overcome them.",
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
WHERE t.name = "thought.OVERCOMING FEAR BLAME" AND c.name = "content.OVERCOMING FEAR BLAME"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OVERCOMING FEAR BLAME" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.OVERCOMING FEAR BLAME"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >OVERCOMING FEAR BLAME" }]->(child);
```
