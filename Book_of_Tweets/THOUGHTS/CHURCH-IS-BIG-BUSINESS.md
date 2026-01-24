---
name: "thought.CHURCH IS BIG BUSINESS"
alias: "Thought: Church Is Big Business"
type: THOUGHT
en_content: "In America church is big business...that's a problem."
parent: "topic.RELIGION"
tags:
- church
- business
- money
- religion
- america
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.CHURCH IS BIG BUSINESS",
    alias: "Thought: Church Is Big Business",
    parent: "topic.RELIGION",
    tags: ['church', 'business', 'money', 'religion', 'america'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHURCH IS BIG BUSINESS",
    en_title: "Church Is Big Business",
    en_content: "In America church is big business...that's a problem.",
    es_title: "La Iglesia es un Gran Negocio",
    es_content: "En América la iglesia es un gran negocio... eso es un problema.",
    fr_title: "L'Église est une Grande Affaire",
    fr_content: "En Amérique, l'église est une grande affaire... c'est un problème.",
    hi_title: "चर्च एक बड़ा व्यवसाय है",
    hi_content: "अमेरिका में चर्च एक बड़ा व्यवसाय है... यह एक समस्या है।",
    zh_title: "Jiàotáng Shì Dà Shēngyì",
    zh_content: "Zài Měiguó, Jiàotáng shì dà shēngyì... Zhè shì yīgè wèntí."
});

MATCH (t:THOUGHT {name: "thought.CHURCH IS BIG BUSINESS"})
MATCH (c:CONTENT {name: "content.CHURCH IS BIG BUSINESS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHURCH IS BIG BUSINESS" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.CHURCH IS BIG BUSINESS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION->CHURCH IS BIG BUSINESS" }]->(child);
```
