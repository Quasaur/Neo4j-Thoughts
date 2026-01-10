---
name: "thought.GOOD STRONGER EVIL"
alias: "Thought: Good Stronger Evil"
type: THOUGHT
en_content: "Jesus PROVED that Good is stronger than Evil...that Righteousness is MORE POWERFUL than Sin!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- victory
- evil
- goodness
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.GOOD STRONGER EVIL",
    alias: "Thought: Good Stronger Evil",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'victory', 'evil', 'goodness', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOOD STRONGER EVIL",
    en_title: "Good Stronger Evil",
    en_content: "Jesus PROVED that Good is stronger than Evil...that Righteousness is MORE POWERFUL than Sin!",
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
WHERE t.name = "thought.GOOD STRONGER EVIL" AND c.name = "content.GOOD STRONGER EVIL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOOD STRONGER EVIL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOOD STRONGER EVIL"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOOD STRONGER EVIL" }]->(child);
```
