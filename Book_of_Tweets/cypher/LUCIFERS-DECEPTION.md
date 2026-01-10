---
name: "thought.LUCIFERS DECEPTION"
alias: "Thought: Lucifers Deception"
type: THOUGHT
en_content: "God knew what Lucifer was doing...and allowed him to tempt, deceive and lead astray one third of Heaven."
parent: "topic.EVIL"
tags:
- lucifer
- deception
- temptation
- evil
- sovereignty
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Jan-2011)
CREATE (t:THOUGHT {
    name: "thought.LUCIFERS DECEPTION",
    alias: "Thought: Lucifers Deception",
    parent: "topic.EVIL",
    tags: ['lucifer', 'deception', 'temptation', 'evil', 'sovereignty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LUCIFERS DECEPTION",
    en_title: "Lucifers Deception",
    en_content: "God knew what Lucifer was doing...and allowed him to tempt, deceive and lead astray one third of Heaven.",
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
WHERE t.name = "thought.LUCIFERS DECEPTION" AND c.name = "content.LUCIFERS DECEPTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LUCIFERS DECEPTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.LUCIFERS DECEPTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >LUCIFERS DECEPTION" }]->(child);
```
