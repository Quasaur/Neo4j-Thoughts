---
type: THOUGHT
name: "thought.GIFT OR GIVER"
alias: "Thought: Gratitude and Priorities"
parent: "topic.WORSHIP"
en_content: "Which is greater: the gift, or the Giver?"
tags: ["gift", "giver", "priorities", "gratitude", "worship"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {    name: "thought.GIFT OR GIVER",
    alias: "Thought: GIFT OR GIVER",
    parent: "topic.WORSHIP",
    tags: ["gift", "giver", "priorities", "gratitude", "worship"],
    level: 3});

CREATE (c:CONTENT {
    name: "content.GIFT OR GIVER",
    ctype: "THOUGHT",
    en_title: "GIFT OR GIVER",
    en_content: "Which is greater: the gift, or the Giver?",
    es_title: "¿REGALO O DONANTE?",
    es_content: "¿Cuál es mayor: el don o el Donante?",
    fr_title: "CADEAU OU DONATEUR",
    fr_content: "Qu'est-ce qui est le plus grand : le cadeau ou le Donateur ?",
    hi_title: "उपहार या दाता",
    hi_content: "कौन बड़ा है: उपहार, या दाता?"
    zh_title: "Lǐwù huò shīzhě",
    zh_content: "ná gè gèng dài ： lǐ wù ， huò shì dào tǐ ？"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GIFT OR GIVER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WORSHIP"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WORSHIP->GIFT OR GIVER"
RETURN t, parent;
```
