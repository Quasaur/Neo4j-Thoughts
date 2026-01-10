---
name: "thought.SPITTING IN GODS FACE"
alias: "Thought: Spitting In Gods Face"
type: THOUGHT
en_content: "America can spit in God's Face over this gay thing if it wants to, but this is NOT going to end well for any of us."
parent: "topic.MORALITY"
tags:
- america
- morality
- judgment
- truth
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.SPITTING IN GODS FACE",
    alias: "Thought: Spitting In Gods Face",
    parent: "topic.MORALITY",
    tags: ['america', 'morality', 'judgment', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SPITTING IN GODS FACE",
    en_title: "Spitting In Gods Face",
    en_content: "America can spit in God's Face over this gay thing if it wants to, but this is NOT going to end well for any of us.",
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
WHERE t.name = "thought.SPITTING IN GODS FACE" AND c.name = "content.SPITTING IN GODS FACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPITTING IN GODS FACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SPITTING IN GODS FACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SPITTING IN GODS FACE" }]->(child);
```
