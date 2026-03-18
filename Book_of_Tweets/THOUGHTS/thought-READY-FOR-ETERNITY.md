---
type: THOUGHT
name: "thought.READY FOR ETERNITY"
alias: "Thought: Ready For Eternity"
parent: "topic.SPIRITUALITY"
en_content: "We are all going to die; are you ready for Eternity?"
tags: ["eternity", "death", "readiness", "spirituality", "judgment"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jun-2012)
CREATE (t:THOUGHT {    name: "thought.READY FOR ETERNITY",
    alias: "Thought: Ready For Eternity",
    parent: "topic.SPIRITUALITY",
    tags: ['eternity', 'death', 'readiness', 'spirituality', 'judgment'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.READY FOR ETERNITY",
    ctype: "THOUGHT",
    en_title: "Ready For Eternity",
    en_content: "We are all going to die; are you ready for Eternity?",
    es_title: "Preparados Para la Eternidad",
    es_content: "Todos vamos a morir; ¿estás preparado para la Eternidad?",
    fr_title: "Prêt Pour l'Éternité",
    fr_content: "Nous allons tous mourir ; êtes-vous prêt pour l'Éternité ?",
    hi_title: "अनंत काल के लिए तैयार",
    hi_content: "हम सब मरने वाले हैं; क्या आप अनंत काल के लिए तैयार हैं?",
    zh_title: "Wei Yongsheng Zuohao Zhunbei",
    zh_content: "Women dou jiang yao siwang; ni wei yongsheng zhunbei hao le ma?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.READY FOR ETERNITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->READY FOR ETERNITY"
RETURN t, parent;
```
