---
type: THOUGHT
name: "thought.NO POOR IN HEAVEN"
alias: "Thought: No Poor In Heaven"
parent: "topic.SPIRITUALITY"
en_content: "There are no poor in Heaven."
tags: ["heaven", "poverty", "abundance", "eternity", "provision"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jan-2012)
CREATE (t:THOUGHT {    name: "thought.NO POOR IN HEAVEN",
    alias: "Thought: No Poor In Heaven",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'poverty', 'abundance', 'eternity', 'provision'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.NO POOR IN HEAVEN",
    ctype: "THOUGHT",
    en_title: "No Poor In Heaven",
    en_content: "There are no poor in Heaven.",
    es_title: "No Hay Pobres en el Cielo",
    es_content: "No hay pobres en el Cielo.",
    fr_title: "Pas de Pauvres au Paradis",
    fr_content: "Il n'y a pas de pauvres au Paradis.",
    hi_title: "स्वर्ग में कोई गरीब नहीं",
    hi_content: "स्वर्ग में कोई गरीब नहीं हैं।",
    zh_title: "Tiān táng lǐ méi yǒu qióng rén",
    zh_content: "Tiān táng lǐ méi yǒu qióng rén."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NO POOR IN HEAVEN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->NO POOR IN HEAVEN"
RETURN t, parent;
```
