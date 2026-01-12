---
name: "thought.SACRIFICE IN SERVICE"
alias: "Thought: Sacrifice In Service"
type: THOUGHT
en_content: "You cannot serve God without sacrificing something of great personal value."
parent: "topic.WORSHIP"
tags:
- sacrifice
- service
- worship
- devotion
- commitment
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Aug-2010)
CREATE (t:THOUGHT {
    name: "thought.SACRIFICE IN SERVICE",
    alias: "Thought: Sacrifice In Service",
    parent: "topic.WORSHIP",
    tags: ['sacrifice', 'service', 'worship', 'devotion', 'commitment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SACRIFICE IN SERVICE",
    en_title: "Sacrifice In Service",
    en_content: "You cannot serve God without sacrificing something of great personal value.",
    es_title: "Sacrificio en servicio",
    es_content: "No se puede servir a Dios sin sacrificar algo de gran valor personal.",
    fr_title: "Sacrifice en service",
    fr_content: "Vous ne pouvez pas servir Dieu sans sacrifier quelque chose de grande valeur personnelle.",
    hi_title: "सेवा में बलिदान",
    hi_content: "आप महान व्यक्तिगत मूल्य की किसी चीज़ का त्याग किए बिना भगवान की सेवा नहीं कर सकते।",
    zh_title: "服务牺牲",
    zh_content: "如果不牺牲一些具有重大个人价值的东西，你就无法事奉上帝。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SACRIFICE IN SERVICE" AND c.name = "content.SACRIFICE IN SERVICE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SACRIFICE IN SERVICE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WORSHIP" AND child.name = "thought.SACRIFICE IN SERVICE"
MERGE (parent)-[:HAS_THOUGHT { "name": "WORSHIP >SACRIFICE IN SERVICE" }]->(child);
```
