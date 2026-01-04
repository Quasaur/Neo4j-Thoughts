---
name: "thought.SPIRIT OF CHRIST ENCOUNTER"
alias: "Thought: Spirit Of Christ Encounter"
type: THOUGHT
en_content: "The greatest moment of my existence was being swallowed up by the Spirit of Christ...all I want is to go back (or forward) to that moment."
parent: "topic.SPIRITUALITY"
tags:
- spirit
- encounter
- christ
- joy
- presence
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Nov-2011b)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT OF CHRIST ENCOUNTER",
    alias: "Thought: Spirit Of Christ Encounter",
    parent: "topic.SPIRITUALITY",
    tags: ['spirit', 'encounter', 'christ', 'joy', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPIRIT OF CHRIST ENCOUNTER",
    en_title: "Spirit Of Christ Encounter",
    en_content: "The greatest moment of my existence was being swallowed up by the Spirit of Christ...all I want is to go back (or forward) to that moment.",
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
WHERE t.name = "thought.SPIRIT OF CHRIST ENCOUNTER" AND c.name = "content.SPIRIT OF CHRIST ENCOUNTER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPIRIT OF CHRIST ENCOUNTER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SPIRIT OF CHRIST ENCOUNTER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SPIRIT OF CHRIST ENCOUNTER" }]->(child);
```
