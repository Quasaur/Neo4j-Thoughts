---
name: "thought.WORK TO BE SAVED"
alias: "Thought: Work To Be Saved"
type: THOUGHT
en_content: "Getting saved is hard work; but hard work alone won't get you saved."
parent: "topic.GRACE"
tags:
- salvation
- work
- grace
- effort
- power
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.WORK TO BE SAVED",
    alias: "Thought: Work To Be Saved",
    parent: "topic.GRACE",
    tags: ['salvation', 'work', 'grace', 'effort', 'power'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WORK TO BE SAVED",
    en_title: "Work To Be Saved",
    en_content: "Getting saved is hard work; but hard work alone won't get you saved.",
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
WHERE t.name = "thought.WORK TO BE SAVED" AND c.name = "content.WORK TO BE SAVED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WORK TO BE SAVED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.WORK TO BE SAVED"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >WORK TO BE SAVED" }]->(child);
```
