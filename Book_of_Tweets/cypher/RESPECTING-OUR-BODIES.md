---
name: "thought.RESPECTING OUR BODIES"
alias: "Thought: Respecting Our Bodies"
type: THOUGHT
en_content: "We don't respect our own bodies yet we want others to respect us!"
parent: "topic.ATTITUDE"
tags:
- respect
- body
- attitude
- character
- integrity
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013d)
CREATE (t:THOUGHT {
    name: "thought.RESPECTING OUR BODIES",
    alias: "Thought: Respecting Our Bodies",
    parent: "topic.ATTITUDE",
    tags: ['respect', 'body', 'attitude', 'character', 'integrity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.RESPECTING OUR BODIES",
    en_title: "Respecting Our Bodies",
    en_content: "We don't respect our own bodies yet we want others to respect us!",
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
WHERE t.name = "thought.RESPECTING OUR BODIES" AND c.name = "content.RESPECTING OUR BODIES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RESPECTING OUR BODIES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.RESPECTING OUR BODIES"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >RESPECTING OUR BODIES" }]->(child);
```
