---
name: "thought.PLANETARY STARVATION"
alias: "Thought: Planetary Starvation"
type: THOUGHT
en_content: "There's enough resources on Planet Earth for EVERYONE...so why are people starving?!?"
parent: "topic.MORALITY"
tags:
- poverty
- hunger
- resources
- justice
- morality
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jun-2012b)
CREATE (t:THOUGHT {
    name: "thought.PLANETARY STARVATION",
    alias: "Thought: Planetary Starvation",
    parent: "topic.MORALITY",
    tags: ['poverty', 'hunger', 'resources', 'justice', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PLANETARY STARVATION",
    en_title: "Planetary Starvation",
    en_content: "There's enough resources on Planet Earth for EVERYONE...so why are people starving?!?",
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
WHERE t.name = "thought.PLANETARY STARVATION" AND c.name = "content.PLANETARY STARVATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PLANETARY STARVATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PLANETARY STARVATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PLANETARY STARVATION" }]->(child);
```
