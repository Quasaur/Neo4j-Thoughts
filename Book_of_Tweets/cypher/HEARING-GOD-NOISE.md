---
name: "thought.HEARING GOD NOISE"
alias: "Thought: Hearing God Noise"
type: THOUGHT
en_content: "We cannot hear God through the noise of our own desire."
parent: "topic.SPIRITUALITY"
tags:
- spirituality
- desire
- listening
- prayer
- silence
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.HEARING GOD NOISE",
    alias: "Thought: Hearing God Noise",
    parent: "topic.SPIRITUALITY",
    tags: ['spirituality', 'desire', 'listening', 'prayer', 'silence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEARING GOD NOISE",
    en_title: "Hearing God Noise",
    en_content: "We cannot hear God through the noise of our own desire.",
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
WHERE t.name = "thought.HEARING GOD NOISE" AND c.name = "content.HEARING GOD NOISE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEARING GOD NOISE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HEARING GOD NOISE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEARING GOD NOISE" }]->(child);
```
