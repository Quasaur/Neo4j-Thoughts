---
name: "thought.CONGRESS HOUSE LORDS"
alias: "Thought: Congress House Lords"
type: THOUGHT
en_content: "Both houses of this American Congress have become a House of Lords."
parent: "topic.MORALITY"
tags:
- congress
- america
- aristocracy
- morality
- society
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.CONGRESS HOUSE LORDS",
    alias: "Thought: Congress House Lords",
    parent: "topic.MORALITY",
    tags: ['congress', 'america', 'aristocracy', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONGRESS HOUSE LORDS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONGRESS HOUSE LORDS" AND c.name = "content.CONGRESS HOUSE LORDS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONGRESS HOUSE LORDS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CONGRESS HOUSE LORDS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CONGRESS HOUSE LORDS" }]->(child);
```
