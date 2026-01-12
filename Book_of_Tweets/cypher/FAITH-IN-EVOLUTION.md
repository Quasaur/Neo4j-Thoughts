---
name: "thought.FAITH IN EVOLUTION"
alias: "Thought: Faith In Evolution"
type: THOUGHT
en_content: "Evolution requires FAR MORE FAITH than Intelligent Design."
parent: "topic.FAITH"
tags:
- faith
- evolution
- design
- creation
- science
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010d)
CREATE (t:THOUGHT {
    name: "thought.FAITH IN EVOLUTION",
    alias: "Thought: Faith In Evolution",
    parent: "topic.FAITH",
    tags: ['faith', 'evolution', 'design', 'creation', 'science'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH IN EVOLUTION",
    en_title: "Faith In Evolution",
    en_content: "Evolution requires FAR MORE FAITH than Intelligent Design.",
    es_title: "Fe en la evolución",
    es_content: "La evolución requiere MUCHA MÁS FE que el Diseño Inteligente.",
    fr_title: "Foi en l'évolution",
    fr_content: "L’évolution nécessite BEAUCOUP PLUS DE FOI que la conception intelligente.",
    hi_title: "विकास में विश्वास",
    hi_content: "विकास के लिए बुद्धिमान डिज़ाइन की तुलना में कहीं अधिक विश्वास की आवश्यकता होती है।",
    zh_title: "相信进化论",
    zh_content: "进化比智能设计需要更多的信念。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FAITH IN EVOLUTION" AND c.name = "content.FAITH IN EVOLUTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAITH IN EVOLUTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.FAITH IN EVOLUTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >FAITH IN EVOLUTION" }]->(child);
```
