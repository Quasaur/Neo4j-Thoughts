---
type: THOUGHT
name: "thought.CONGRESS HOUSE LORDS"
alias: "Thought: Congress House Lords"
parent: "topic.MORALITY"
en_content: "Both houses of this American Congress have become a House of Lords."
tags: ["congress", "america", "aristocracy", "morality", "society"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2013a)
CREATE (t:THOUGHT {    name: "thought.CONGRESS HOUSE LORDS",
    alias: "Thought: Congress House Lords",
    parent: "topic.MORALITY",
    tags: ['congress', 'america', 'aristocracy', 'morality', 'society'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CONGRESS HOUSE LORDS",
    ctype: "THOUGHT",
    en_title: "Congress House Lords",
    en_content: "Both houses of this American Congress have become a House of Lords.",
    es_title: "Congreso Cámara de Lores",
    es_content: "Ambas cámaras de este Congreso Americano se han convertido en una Cámara de Lores.",
    fr_title: "Congrès Chambre des Lords",
    fr_content: "Les deux chambres de ce Congrès américain sont devenues une Chambre des Lords.",
    hi_title: "कांग्रेस लॉर्ड्स सभा",
    hi_content: "इस अमेरिकी कांग्रेस के दोनों सदन लॉर्ड्स सभा बन गए हैं।",
    zh_title: "Guóhuì Guìzú Yuàn",
    zh_content: "Zhè gè Měiguó Guóhuì de liǎng yuàn dōu biànchéngle Guìzú Yuàn."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CONGRESS HOUSE LORDS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->CONGRESS HOUSE LORDS"
RETURN t, parent;
```
