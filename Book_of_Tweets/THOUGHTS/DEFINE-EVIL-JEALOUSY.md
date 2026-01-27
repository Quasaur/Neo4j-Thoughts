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
neo4j: false
ptopic: "[[topic-EVIL]]"
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
    es_title: "Definir Celos Malvados",
    es_content: "Celos Malvados: miedo a la pérdida.",
    fr_title: "Définir la Jalousie Maléfique",
    fr_content: "Jalousie Maléfique : peur de la perte.",
    hi_title: "बुराई ईर्ष्या को परिभाषित करें",
    hi_content: "बुराई ईर्ष्या: हानि का डर।",
    zh_title: "Dìngyì è'è de jídù",
    zh_content: "È'è de jídù: Pà shīqù."
});

MATCH (t:THOUGHT {name: "thought.DEFINE EVIL JEALOUSY"})
MATCH (c:CONTENT {name: "content.DEFINE EVIL JEALOUSY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE EVIL JEALOUSY" }]->(c);

MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:THOUGHT {name: "thought.DEFINE EVIL JEALOUSY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.EVIL->DEFINE EVIL JEALOUSY" }]->(child);
```
