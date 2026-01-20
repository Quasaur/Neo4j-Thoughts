---
name: "thought.GORGEOUS DIVINITY"
alias: "Thought: Gorgeous Divinity"
type: THOUGHT
en_content: "God is overwhelmingly gorgeous...both inside and out!"
parent: topic.BEAUTY
tags:
  - beauty
  - aesthetics
  - holiness
  - character
  - divinity
level: 5
neo4j: false
ptopic: "[[topic-BEAUTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Aug-2012)
CREATE (t:THOUGHT {
    name: "thought.GORGEOUS DIVINITY",
    alias: "Thought: Gorgeous Divinity",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'aesthetics', 'holiness', 'character', 'divinity'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.GORGEOUS DIVINITY",
    en_title: "Gorgeous Divinity",
    en_content: "God is overwhelmingly gorgeous...both inside and out!",
    es_title: "Divinidad Hermosa",
    es_content: "¡Dios es abrumadoramente hermoso...tanto por dentro como por fuera!",
    fr_title: "Divinité Magnifique",
    fr_content: "Dieu est d'une beauté écrasante...à l'intérieur comme à l'extérieur !",
    hi_title: "भव्य दिव्यता",
    hi_content: "परमेश्वर अत्यंत सुंदर है...अंदर और बाहर दोनों तरफ से!",
    zh_title: "huáměi de shénxìng",
    zh_content: "Shàngdì shì yāo rén de měilì...nèizài hé wàizài dōu shì!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GORGEOUS DIVINITY" AND c.name = "content.GORGEOUS DIVINITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GORGEOUS DIVINITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.GORGEOUS DIVINITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY->GORGEOUS DIVINITY" }]->(child);
```
