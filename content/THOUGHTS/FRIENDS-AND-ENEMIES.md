---
name: "thought.FRIENDS AND ENEMIES"
alias: "Thought: Divine Design"
parent: topic.CREATION
type: THOUGHT
en_content: "Something to think about: God created His friends AND His enemies!"
tags:
  - creation
  - purpose
  - sovereignty
  - relations
  - divine_will
level: 2
ptopic: "[[topic-CREATION]]"
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FRIENDS AND ENEMIES",
    alias: "Thought: Divine Design",
    parent: "topic.CREATION",
    tags: ["creation", "purpose", "sovereignty", "relations", "divine_will"],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FRIENDS AND ENEMIES",
    en_title: "Friends and Enemies",
    en_content: "Something to think about: God created His friends AND His enemies!",
    es_title: "Amigos y enemigos",
    es_content: "¡Dios creó a Sus amigos Y a Sus enemigos!",
    fr_title: "Amis et ennemis",
    fr_content: "Dieu a créé Ses amis ET Ses ennemis !",
    hi_title: "dost aur dushman",
    hi_content: "सोचने वाली बात: भगवान ने अपने दोस्तों और अपने दुश्मनों को बनाया!",
    zh_title: "péng yǒu hé dírén",
    zh_content: "zhí dé sī kǎo de shì : shàng dì chuàng zào le tā de péng yǒu, yě chuàng zào le tā de dírén!"
});

MATCH (t:THOUGHT {name: "thought.FRIENDS AND ENEMIES"})
MATCH (c:CONTENT {name: "content.FRIENDS AND ENEMIES"})
MERGE (t)-[:HAS_CONTENT {name: "edge.FRIENDS AND ENEMIES"}]->(c);

MATCH (parent:TOPIC {name: "topic.CREATION"})
MATCH (child:THOUGHT {name: "thought.FRIENDS AND ENEMIES"})
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->FRIENDS AND ENEMIES"}]->(child);
```
