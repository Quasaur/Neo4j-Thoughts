---
type: THOUGHT
name: "thought.PEOPLE MORE UNFORGIVING"
alias: "Thought: People More Unforgiving"
parent: "topic.THE GODHEAD"
en_content: "People are FAR MORE unforgiving than God."
tags: ["forgiveness", "god", "people", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Nov-2013)
CREATE (t:THOUGHT {    name: "thought.PEOPLE MORE UNFORGIVING",
    alias: "Thought: People More Unforgiving",
    parent: "topic.THE GODHEAD",
    tags: ['forgiveness', 'god', 'people', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.PEOPLE MORE UNFORGIVING",
    ctype: "THOUGHT",
    en_title: "People More Unforgiving",
    en_content: "People are FAR MORE unforgiving than God.",
    es_title: "Las Personas Más Implacables",
    es_content: "Las personas son MUCHO MÁS implacables que Dios.",
    fr_title: "Les Gens Plus Impitoyables",
    fr_content: "Les gens sont BEAUCOUP PLUS impitoyables que Dieu.",
    hi_title: "लोग अधिक निर्दयी",
    hi_content: "लोग परमेश्वर से कहीं अधिक निर्दयी हैं।",
    zh_title: "Rén Gèng Jiā Bù Kuān Shù",
    zh_content: "Rén bǐ Shàng Dì yuǎn yuǎn gèng jiā bù kuān shù."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PEOPLE MORE UNFORGIVING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->PEOPLE MORE UNFORGIVING"
RETURN t, parent;
```
