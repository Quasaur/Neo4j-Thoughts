---
type: THOUGHT
name: "thought.LIFE IN PRAYER"
alias: "Thought: Life In Prayer"
parent: "topic.SPIRITUALITY"
en_content: "There is no life outside of Prayer."
tags: ["prayer", "life", "spirituality", "essence"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Feb-2014)
CREATE (t:THOUGHT {    name: "thought.LIFE IN PRAYER",
    alias: "Thought: Life In Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'life', 'spirituality', 'essence'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.LIFE IN PRAYER",
    ctype: "THOUGHT",
    en_title: "Life In Prayer",
    en_content: "There is no life outside of Prayer.",
    es_title: "Vida en Oración",
    es_content: "No hay vida fuera de la Oración.",
    fr_title: "Vie dans la Prière",
    fr_content: "Il n'y a pas de vie en dehors de la Prière.",
    hi_title: "प्रार्थना में जीवन",
    hi_content: "प्रार्थना के बाहर कोई जीवन नहीं है।",
    zh_title: "Qídǎo zhōng de Shēngmìng",
    zh_content: "Méiyǒu qídǎo jiù méiyǒu shēngmìng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIFE IN PRAYER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->LIFE IN PRAYER"
RETURN t, parent;
```
