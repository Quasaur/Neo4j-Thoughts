---
name: "thought.NO POOR IN HEAVEN"
alias: "Thought: No Poor In Heaven"
type: THOUGHT
en_content: "There are no poor in Heaven."
parent: "topic.SPIRITUALITY"
tags:
- heaven
- poverty
- abundance
- eternity
- provision
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.NO POOR IN HEAVEN",
    alias: "Thought: No Poor In Heaven",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'poverty', 'abundance', 'eternity', 'provision'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NO POOR IN HEAVEN",
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

MATCH (t:THOUGHT {name: "thought.NO POOR IN HEAVEN"})
MATCH (c:CONTENT {name: "content.NO POOR IN HEAVEN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NO POOR IN HEAVEN" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.NO POOR IN HEAVEN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->NO POOR IN HEAVEN" }]->(child);
```
