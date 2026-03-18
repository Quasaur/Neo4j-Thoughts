---
type: THOUGHT
name: "thought.RECONCILING IN CHRIST"
alias: "Thought: Reconciling In Christ"
parent: "topic.THE GODHEAD"
en_content: "1st Corinthians 15:24-28: God is reconciling and consolidating all things into Christ."
tags: ["reconciliation", "christ", "consolidation", "bible", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Nov-2011a)
CREATE (t:THOUGHT {    name: "thought.RECONCILING IN CHRIST",
    alias: "Thought: Reconciling In Christ",
    parent: "topic.THE GODHEAD",
    tags: ['reconciliation', 'christ', 'consolidation', 'bible', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.RECONCILING IN CHRIST",
    ctype: "THOUGHT",
    en_title: "Reconciling In Christ",
    en_content: "1st Corinthians 15:24-28: God is reconciling and consolidating all things into Christ.",
    es_title: "Reconciliando en Cristo",
    es_content: "1 Corintios 15:24-28: Dios está reconciliando y consolidando todas las cosas en Cristo.",
    fr_title: "Réconcilier en Christ",
    fr_content: "1 Corinthiens 15:24-28 : Dieu réconcilie et consolide toutes choses en Christ.",
    hi_title: "मसीह में सुलह करना",
    hi_content: "1 कुरिन्थियों 15:24-28: परमेश्वर सभी चीज़ों को मसीह में सुलह और संघटित कर रहे हैं।",
    zh_title: "Zài Jīdū lǐ héxé  zài jī dū lǐ hé hé",
    zh_content: "Gēlínduō qián shū 15:24-28: Shàngdì zhèng zài Jīdū lǐ héxé bìng zhěnghé wànwù.  gē lín duō qián shū  15:24-28： shàng dì zhèng zài jī dū lǐ hé hé bìng zhěng hé wàn wù 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RECONCILING IN CHRIST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->RECONCILING IN CHRIST"
RETURN t, parent;
```
