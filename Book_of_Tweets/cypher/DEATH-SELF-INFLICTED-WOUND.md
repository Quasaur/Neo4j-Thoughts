---
name: "thought.DEATH SELF INFLICTED WOUND"
alias: "Thought: Death Self Inflicted Wound"
type: THOUGHT
en_content: "Death is not natural; it's a self-inflicted wound we incurred when we separated ourselves from God through disobedience."
parent: "topic.HUMANITY"
tags:
- death
- disobedience
- separation
- humanity
- nature
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.DEATH SELF INFLICTED WOUND",
    alias: "Thought: Death Self Inflicted Wound",
    parent: "topic.HUMANITY",
    tags: ['death', 'disobedience', 'separation', 'humanity', 'nature'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEATH SELF INFLICTED WOUND",
    en_title: "Death Self Inflicted Wound",
    en_content: "Death is not natural; it's a self-inflicted wound we incurred when we separated ourselves from God through disobedience.",
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
WHERE t.name = "thought.DEATH SELF INFLICTED WOUND" AND c.name = "content.DEATH SELF INFLICTED WOUND"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEATH SELF INFLICTED WOUND" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.DEATH SELF INFLICTED WOUND"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >DEATH SELF INFLICTED WOUND" }]->(child);
```
