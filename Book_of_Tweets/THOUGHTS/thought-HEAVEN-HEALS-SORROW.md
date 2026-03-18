---
type: THOUGHT
name: "thought.HEAVEN HEALS SORROW"
alias: "Thought: Heaven Heals Sorrow"
parent: "topic.SPIRITUALITY"
en_content: "Earth has no sorrow that Heaven cannot heal. -- Hymn"
tags: ["healing", "heaven", "sorrow", "comfort", "grace"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011c)
CREATE (t:THOUGHT {    name: "thought.HEAVEN HEALS SORROW",
    alias: "Thought: Heaven Heals Sorrow",
    parent: "topic.SPIRITUALITY",
    tags: ['healing', 'heaven', 'sorrow', 'comfort', 'grace'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.HEAVEN HEALS SORROW",
    ctype: "THOUGHT",
    en_title: "Heaven Heals Sorrow",
    en_content: "Earth has no sorrow that Heaven cannot heal. -- Hymn",
    es_title: "El Cielo Sana la Tristeza",
    es_content: "No hay tristeza en la Tierra que el Cielo no pueda sanar. -- Himno",
    fr_title: "Le Ciel Guérit la Douleur",
    fr_content: "La Terre n'a aucune douleur que le Ciel ne puisse guérir. -- Cantique",
    hi_title: "स्वर्ग दुःख को चंगा करता है",
    hi_content: "पृथ्वी पर कोई दुःख नहीं है जिसे स्वर्ग चंगा नहीं कर सकता। -- भजन",
    zh_title: "Tiāntáng Zhìyù Bēishāng",
    zh_content: "Shìjiān méiyǒu tiāntáng bùnéng zhìyù de bēishāng. -- Shèngshī"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HEAVEN HEALS SORROW"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->HEAVEN HEALS SORROW"
RETURN t, parent;
```
