---
name: "thought.COMMUNICATION SYSTEMS"
alias: "Thought: Communication Systems"
type: THOUGHT
en_content: "Every communication system must have a language, a medium, an organ that reads, and an intelligence that writes/interprets...God is Great!"
parent: "topic.COMMUNICATION THEORY"
tags:
  - design
  - language
  - intelligence
  - communication
  - creation
level: 4
neo4j: true
ptopic: "[[topic-COMMUNICATION-THEORY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011d)
CREATE (t:THOUGHT {
    name: "thought.COMMUNICATION SYSTEMS",
    alias: "Thought: Communication Systems",
    parent: "topic.COMMUNICATION THEORY",
    tags: ['design', 'language', 'intelligence', 'communication', 'creation'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.COMMUNICATION SYSTEMS",
    en_title: "Communication Systems",
    en_content: "Every communication system must have a language, a medium, a device that reads, and an intelligence that writes/interprets...God is Great!",
    es_title: "Sistemas de Comunicación",
    es_content: "Todo sistema de comunicación debe tener un lenguaje, un medio, un dispositivo que lee, y una inteligencia que escribe/interpreta... ¡Dios es Grande!",
    fr_title: "Systèmes de Communication",
    fr_content: "Chaque système de communication doit avoir un langage, un médium, un dispositif qui lit, et une intelligence qui écrit/interprète... Dieu est Grand !",
    hi_title: "संचार प्रणाली",
    hi_content: "हर संचार प्रणाली में एक भाषा, एक माध्यम, एक उपकरण जो पढ़ता है, और एक बुद्धि होनी चाहिए जो लिखती/व्याख्या करती है... भगवान महान हैं!",
    zh_title: "Tōngxìn Xìtǒng",
    zh_content: "Měi gè tōngxìn xìtǒng dōu bìxū yǒu yī zhǒng yǔyán, yī zhǒng méijì, yī zhǒng yuèdú shèbèi, yǐjí yī zhǒng biānxiě/jiěshì de zhìhuì... Shàngdì shì wěidà de!"
});

MATCH (t:THOUGHT {name: "thought.COMMUNICATION SYSTEMS"})
MATCH (c:CONTENT {name: "content.COMMUNICATION SYSTEMS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.COMMUNICATION SYSTEMS" }]->(c);

MATCH (parent:TOPIC {name: "topic.COMMUNICATION THEORY"})
MATCH (child:THOUGHT {name: "thought.COMMUNICATION SYSTEMS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "COMMUNICATION THEORY->COMMUNICATION SYSTEMS" }]->(child);
```
