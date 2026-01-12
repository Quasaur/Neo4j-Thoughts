---
name: "thought.READY FOR ETERNITY"
alias: "Thought: Ready For Eternity"
type: THOUGHT
en_content: "We are all going to die; are you ready for Eternity?"
parent: "topic.SPIRITUALITY"
tags:
- eternity
- death
- readiness
- spirituality
- judgment
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jun-2012)
CREATE (t:THOUGHT {
    name: "thought.READY FOR ETERNITY",
    alias: "Thought: Ready For Eternity",
    parent: "topic.SPIRITUALITY",
    tags: ['eternity', 'death', 'readiness', 'spirituality', 'judgment'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.READY FOR ETERNITY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.READY FOR ETERNITY" AND c.name = "content.READY FOR ETERNITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.READY FOR ETERNITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.READY FOR ETERNITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >READY FOR ETERNITY" }]->(child);
```
