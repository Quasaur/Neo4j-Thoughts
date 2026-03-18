---
type: THOUGHT
name: "thought.LOVING THE HATEFUL"
alias: "Thought: Loving The Hateful"
parent: "topic.THE GODHEAD"
en_content: "Loving the hateful... how does God do it? How can I do it?"
tags: ["love", "hate", "character", "god", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2013b)
CREATE (t:THOUGHT {    name: "thought.LOVING THE HATEFUL",
    alias: "Thought: Loving The Hateful",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'hate', 'character', 'god', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.LOVING THE HATEFUL",
    ctype: "THOUGHT",
    en_title: "Loving The Hateful",
    en_content: "Loving the hateful... how does God do it? How can I do it?",
    es_title: "Amar a los Aborrecibles",
    es_content: "Amar a los aborrecibles... ¿cómo lo hace Dios? ¿Cómo puedo hacerlo yo?",
    fr_title: "Aimer Ceux Qui Haïssent",
    fr_content: "Aimer ceux qui haïssent... comment Dieu fait-il cela ? Comment puis-je le faire ?",
    hi_title: "घृणा करने वालों से प्रेम करना",
    hi_content: "घृणा करने वालों से प्रेम करना... परमेश्वर यह कैसे करता है? मैं यह कैसे कर सकता हूँ?",
    zh_title: "Ai Na Xie Ke Wu De Ren",
    zh_content: "Ai na xie ke wu de ren... Shen shi zenme zuo dao de? Wo zenme neng zuo dao?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVING THE HATEFUL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->LOVING THE HATEFUL"
RETURN t, parent;
```
