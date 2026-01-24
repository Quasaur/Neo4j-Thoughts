---
name: "thought.PEOPLE MORE UNFORGIVING"
alias: "Thought: People More Unforgiving"
type: THOUGHT
en_content: "People are FAR MORE unforgiving than God."
parent: "topic.THE GODHEAD"
tags:
- forgiveness
- god
- people
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.PEOPLE MORE UNFORGIVING",
    alias: "Thought: People More Unforgiving",
    parent: "topic.THE GODHEAD",
    tags: ['forgiveness', 'god', 'people', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.PEOPLE MORE UNFORGIVING",
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

MATCH (t:THOUGHT {name: "thought.PEOPLE MORE UNFORGIVING"})
MATCH (c:CONTENT {name: "content.PEOPLE MORE UNFORGIVING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PEOPLE MORE UNFORGIVING" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.PEOPLE MORE UNFORGIVING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->PEOPLE MORE UNFORGIVING" }]->(child);
```
