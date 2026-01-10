---
name: "thought.INCARCERATION SLAVERY PARALLEL"
alias: "Thought: Incarceration Slavery Parallel"
type: THOUGHT
en_content: "Today in the USA there are more black people incarcerated than there were black slaves in 1850. Thank you, America!"
parent: "topic.MORALITY"
tags:
- incarceration
- slavery
- america
- race
- justice
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.INCARCERATION SLAVERY PARALLEL",
    alias: "Thought: Incarceration Slavery Parallel",
    parent: "topic.MORALITY",
    tags: ['incarceration', 'slavery', 'america', 'race', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INCARCERATION SLAVERY PARALLEL",
    en_title: "Incarceration Slavery Parallel",
    en_content: "Today in the USA there are more black people incarcerated than there were black slaves in 1850. Thank you, America!",
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
WHERE t.name = "thought.INCARCERATION SLAVERY PARALLEL" AND c.name = "content.INCARCERATION SLAVERY PARALLEL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INCARCERATION SLAVERY PARALLEL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.INCARCERATION SLAVERY PARALLEL"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >INCARCERATION SLAVERY PARALLEL" }]->(child);
```
