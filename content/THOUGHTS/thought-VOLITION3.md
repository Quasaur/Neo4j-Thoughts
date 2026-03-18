---
type: THOUGHT
name: "thought.VOLITION3"
alias: "Thought: Third Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["freedom", "volition", "free_will", "accountability", "judgment"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.VOLITION3",
    alias: "Thought: Third Volition",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "free_will", "accountability", "judgment"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION3",
    ctype: "THOUGHT",
    en_title: "Third Volition",
    en_content: "",
    es_title: "TERCERA VOLICIÓN",
    es_content: "El libre albedrío es genial... siempre y cuando tomes las decisiones que Dios aprueba.",
    fr_title: "TROISIÈME VOLITION",
    fr_content: "Le libre arbitre est formidable… tant que vous faites les choix que Dieu approuve.",
    hi_title: "तीसरी इच्छा",
    hi_content: "स्वतंत्र इच्छा महान है...जब तक आप वही विकल्प चुन रहे हैं जो ईश्वर को मंजूर है।",
    zh_title: "dì sān cì yì yuàn",
    zh_content: "zì yóu yì zhì shì wěi dà de …… zhǐ yào nǐ zuò chū shàng dì rèn kě de xuǎn zé 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.VOLITION3"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->VOLITION3"
RETURN t, parent;
```
