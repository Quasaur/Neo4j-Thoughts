---
name: "thought.MLK MURDERED GOOD DEEDS"
alias: "Thought: Mlk Murdered Good Deeds"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- mlk
- justice
- murder
- deeds
- morality
level: 3
neo4j: true
insert: true
---
# Mlk Murdered Good Deeds

> [!Thought-en]
> Remember: Martin Luther King Jr. was murdered -- not for his crimes, but for his good deeds.

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.MLK MURDERED GOOD DEEDS",
    alias: "Thought: Mlk Murdered Good Deeds",
    parent: "topic.MORALITY",
    tags: ['mlk', 'justice', 'murder', 'deeds', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MLK MURDERED GOOD DEEDS",
    en_title: "Mlk Murdered Good Deeds",
    en_content: "Remember: Martin Luther King Jr. was murdered -- not for his crimes, but for his good deeds.",
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
WHERE t.name = "thought.MLK MURDERED GOOD DEEDS" AND c.name = "content.MLK MURDERED GOOD DEEDS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MLK MURDERED GOOD DEEDS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.MLK MURDERED GOOD DEEDS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >MLK MURDERED GOOD DEEDS" }]->(child);
```