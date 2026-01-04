---
name: "thought.OBSOLETE HUMAN RACE"
alias: "Thought: Obsolete Human Race"
type: THOUGHT
en_content: "The human race is obsolete...God is creating a new race with Christ as The Adam; familyship is granted by Grace through Faith."
parent: "topic.HUMANITY"
tags:
- humanity
- christ
- grace
- faith
- creation
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.OBSOLETE HUMAN RACE",
    alias: "Thought: Obsolete Human Race",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'christ', 'grace', 'faith', 'creation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OBSOLETE HUMAN RACE",
    en_title: "Obsolete Human Race",
    en_content: "The human race is obsolete...God is creating a new race with Christ as The Adam; familyship is granted by Grace through Faith.",
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
WHERE t.name = "thought.OBSOLETE HUMAN RACE" AND c.name = "content.OBSOLETE HUMAN RACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OBSOLETE HUMAN RACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.OBSOLETE HUMAN RACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >OBSOLETE HUMAN RACE" }]->(child);
```
