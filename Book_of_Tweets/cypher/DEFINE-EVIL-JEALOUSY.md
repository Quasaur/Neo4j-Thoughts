---
name: "thought.DEFINE EVIL JEALOUSY"
alias: "Thought: Define Evil Jealousy"
type: THOUGHT
en_content: "Evil Jealousy: fear of loss."
parent: "topic.EVIL"
tags:
- jealousy
- fear
- evil
- character
- philosophy
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Feb-2012c)
CREATE (t:THOUGHT {
    name: "thought.DEFINE EVIL JEALOUSY",
    alias: "Thought: Define Evil Jealousy",
    parent: "topic.EVIL",
    tags: ['jealousy', 'fear', 'evil', 'character', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE EVIL JEALOUSY",
    en_title: "Define Evil Jealousy",
    en_content: "Evil Jealousy: fear of loss.",
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
WHERE t.name = "thought.DEFINE EVIL JEALOUSY" AND c.name = "content.DEFINE EVIL JEALOUSY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE EVIL JEALOUSY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.DEFINE EVIL JEALOUSY"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >DEFINE EVIL JEALOUSY" }]->(child);
```
