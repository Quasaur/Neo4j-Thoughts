---
name: "thought.IDENTITY IN GOD"
alias: "Thought: Identity In God"
type: THOUGHT
en_content: "The only reason anyone would want to be \"normal\" or \"like everyone else\" is that they do not know who they are in God!"
parent: "topic.SPIRITUALITY"
tags:
- identity
- normal
- god
- character
- value
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.IDENTITY IN GOD",
    alias: "Thought: Identity In God",
    parent: "topic.SPIRITUALITY",
    tags: ['identity', 'normal', 'god', 'character', 'value'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IDENTITY IN GOD",
    en_title: "Identity In God",
    en_content: "The only reason anyone would want to be \"normal\" or \"like everyone else\" is that they do not know who they are in God!",
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
WHERE t.name = "thought.IDENTITY IN GOD" AND c.name = "content.IDENTITY IN GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.IDENTITY IN GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.IDENTITY IN GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >IDENTITY IN GOD" }]->(child);
```
