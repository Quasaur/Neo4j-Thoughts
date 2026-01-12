---
name: "thought.RECONCILING IN CHRIST"
alias: "Thought: Reconciling In Christ"
type: THOUGHT
en_content: "1st Corinthians 15:24-28: God is reconciling and consolidating all things into Christ."
parent: "topic.THE GODHEAD"
tags:
- reconciliation
- christ
- consolidation
- bible
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Nov-2011a)
CREATE (t:THOUGHT {
    name: "thought.RECONCILING IN CHRIST",
    alias: "Thought: Reconciling In Christ",
    parent: "topic.THE GODHEAD",
    tags: ['reconciliation', 'christ', 'consolidation', 'bible', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.RECONCILING IN CHRIST",
    en_title: "Reconciling In Christ",
    en_content: "1st Corinthians 15:24-28: God is reconciling and consolidating all things into Christ.",
    es_title: "Reconciliando en Cristo",
    es_content: "1 Corintios 15:24-28: Dios está reconciliando y consolidando todas las cosas en Cristo.",
    fr_title: "Réconcilier en Christ",
    fr_content: "1 Corinthiens 15:24-28 : Dieu réconcilie et consolide toutes choses en Christ.",
    hi_title: "मसीह में सुलह करना",
    hi_content: "1 कुरिन्थियों 15:24-28: परमेश्वर सभी चीज़ों को मसीह में सुलह और संघटित कर रहे हैं।",
    zh_title: "Zài Jīdū lǐ héxé 在基督里和合",
    zh_content: "Gēlínduō qián shū 15:24-28: Shàngdì zhèng zài Jīdū lǐ héxé bìng zhěnghé wànwù. 哥林多前书 15:24-28：上帝正在基督里和合并整合万物。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.RECONCILING IN CHRIST" AND c.name = "content.RECONCILING IN CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RECONCILING IN CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.RECONCILING IN CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >RECONCILING IN CHRIST" }]->(child);
```
