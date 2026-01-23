---
name: "thought.RECONCILING ALL THINGS"
alias: "Thought: Reconciling All Things"
type: THOUGHT
en_content: "1st Corinthians 15:24-28: God is #reconciling and consolidating all things into Christ."
parent: "topic.THE GODHEAD"
tags:
- reconciliation
- christ
- sovereignty
- consolidation
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Nov-2011b)
CREATE (t:THOUGHT {
    name: "thought.RECONCILING ALL THINGS",
    alias: "Thought: Reconciling All Things",
    parent: "topic.THE GODHEAD",
    tags: ["reconciliation", "christ", "sovereignty", "consolidation", "divinity"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.RECONCILING ALL THINGS",
    en_title: "Reconciling All Things",
    en_content: "1st Corinthians 15:24-28: God is #reconciling and consolidating all things into Christ.",
    es_title: "Reconciliando Todas las Cosas",
    es_content: "1 Corintios 15:24-28: Dios está #reconciliando y consolidando todas las cosas en Cristo.",
    fr_title: "Réconcilier Toutes Choses",
    fr_content: "1 Corinthiens 15:24-28: Dieu #réconcilie et consolide toutes choses en Christ.",
    hi_title: "सभी वस्तुओं का मेल-मिलाप",
    hi_content: "1 कुरिन्थियों 15:24-28: परमेश्वर सभी वस्तुओं को मसीह में #मेल-मिलाप करा रहा है और एकीकृत कर रहा है।",
    zh_title: "Hé Xié Wàn Wù",
    zh_content: "Gē Lín Duō Qián Shū 15:24-28: Shàng Dì zhèng zài #hé xié bìng jiāng wàn wù guī yī yú Jī Dū."
});

MATCH (t:THOUGHT {name: "thought.RECONCILING ALL THINGS"})
MATCH (c:CONTENT {name: "content.RECONCILING ALL THINGS"})
MERGE (t)-[:HAS_CONTENT {name: "edge.RECONCILING ALL THINGS"}]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.RECONCILING ALL THINGS"})
MERGE (parent)-[:HAS_THOUGHT {name: "THE GODHEAD >RECONCILING ALL THINGS"}]->(child);
```
