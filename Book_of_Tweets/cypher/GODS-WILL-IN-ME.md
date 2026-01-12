---
name: "thought.GODS WILL IN ME"
alias: "Thought: Gods Will In Me"
type: THOUGHT
en_content: "I can't make God do anything; yet He effortlessly executes His Will in me without my awareness of the act."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- providence
- grace
- willpower
- surrender
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011a)
CREATE (t:THOUGHT {
    name: "thought.GODS WILL IN ME",
    alias: "Thought: Gods Will In Me",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'providence', 'grace', 'willpower', 'surrender'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GODS WILL IN ME",
    en_title: "Gods Will In Me",
    en_content: "I can't make God do anything; yet He effortlessly executes His Will in me without my awareness of the act.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS WILL IN ME" AND c.name = "content.GODS WILL IN ME"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS WILL IN ME" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.GODS WILL IN ME"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >GODS WILL IN ME" }]->(child);
```
