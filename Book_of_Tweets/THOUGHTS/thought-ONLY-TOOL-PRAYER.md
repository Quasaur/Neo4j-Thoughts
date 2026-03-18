---
type: THOUGHT
name: "thought.ONLY TOOL PRAYER"
alias: "Thought: Only Tool Prayer"
parent: "topic.SPIRITUALITY"
en_content: "Prayer is not our best tool; it's our ONLY tool."
tags: ["prayer", "spirituality", "dependence", "faith", "connection"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-May-2011a)
CREATE (t:THOUGHT {    name: "thought.ONLY TOOL PRAYER",
    alias: "Thought: Only Tool Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'spirituality', 'dependence', 'faith', 'connection'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.ONLY TOOL PRAYER",
    ctype: "THOUGHT",
    en_title: "Only Tool Prayer",
    en_content: "Prayer is not our best tool; it's our ONLY tool.",
    es_title: "La Oración Como Única Herramienta",
    es_content: "La oración no es nuestra mejor herramienta; es nuestra ÚNICA herramienta.",
    fr_title: "La Prière Seul Outil",
    fr_content: "La prière n'est pas notre meilleur outil ; c'est notre SEUL outil.",
    hi_title: "केवल साधन प्रार्थना",
    hi_content: "प्रार्थना हमारा सबसे अच्छा साधन नहीं है; यह हमारा एकमात्र साधन है।",
    zh_title: "Wei Yi Gong Ju Qi Dao",
    zh_content: "Qi dao bu shi wo men zui hao de gong ju; ta shi wo men WEI YI de gong ju."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ONLY TOOL PRAYER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->ONLY TOOL PRAYER"
RETURN t, parent;
```
