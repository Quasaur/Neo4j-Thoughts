---
type: THOUGHT
name: "thought.VOLITION3"
alias: "Thought: Third Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["freedom", "volition", "free_will", "accountability", "judgment"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
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
 es_title: "TERCERA VOLICIÓN",
 fr_title: "TROISIÈME VOLITION",
 hi_title: "तीसरी इच्छा",
 zh_title: "dì sān cì yì yuàn",
    en_content: "",
 es_content: "El libre albedrío es genial... siempre y cuando tomes las decisiones que Dios aprueba.",
 fr_content: "Le libre arbitre est formidable… tant que vous faites les choix que Dieu approuve.",
 hi_content: "स्वतंत्र इच्छा महान है...जब तक आप वही विकल्प चुन रहे हैं जो ईश्वर को मंजूर है।",
 zh_content: "zì yóu yì zhì shì wěi dà de …… zhǐ yào nǐ zuò chū shàng dì rèn kě de xuǎn zé 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION3" AND c.name = "content.VOLITION3"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.VOLITION3"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION3"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->VOLITION3"}]->(child);
```