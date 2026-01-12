---
name: thought.UNREASONABLE PRIDE
alias: "Thought: Unreasonable Pride"
type: THOUGHT
en_content: Self Pride is always unreasonable.
parent: topic.EVIL
tags:
  - pride
  - attitude
  - reason
  - character
  - arrogance
level: 3
neo4j: true
ptopic: "[[topic-EVIL]]"
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Dec-2011c)
CREATE (t:THOUGHT {
    name: "thought.UNREASONABLE PRIDE",
    alias: "Thought: Unreasonable Pride",
    parent: "topic.ATTITUDE",
    tags: ['pride', 'attitude', 'reason', 'character', 'arrogance'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNREASONABLE PRIDE",
    en_title: "Unreasonable Pride",
    en_content: "Self Pride is always unreasonable.",
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
WHERE t.name = "thought.UNREASONABLE PRIDE" AND c.name = "content.UNREASONABLE PRIDE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNREASONABLE PRIDE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.UNREASONABLE PRIDE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >UNREASONABLE PRIDE" }]->(child);
```
