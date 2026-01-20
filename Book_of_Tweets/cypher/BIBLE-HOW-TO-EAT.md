---
name: "thought.BIBLE HOW TO EAT"
alias: "Thought: Bible How To Eat"
type: THOUGHT
en_content: "The Bible not only tells us how to live, but also HOW TO EAT!"
parent: "topic.TRUTH"
tags:
- bible
- food
- health
- truth
- life
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013f)
CREATE (t:THOUGHT {
    name: "thought.BIBLE HOW TO EAT",
    alias: "Thought: Bible How To Eat",
    parent: "topic.TRUTH",
    tags: ['bible', 'food', 'health', 'truth', 'life'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BIBLE HOW TO EAT",
    en_title: "Bible How To Eat",
    en_content: "The Bible not only tells us how to live, but also HOW TO EAT!",
    es_title: "La Biblia y Cómo Comer",
    es_content: "¡La Biblia no solo nos dice cómo vivir, sino también CÓMO COMER!",
    fr_title: "La Bible et Comment Manger",
    fr_content: "La Bible ne nous dit pas seulement comment vivre, mais aussi COMMENT MANGER !",
    hi_title: "बाइबिल कैसे खाएं",
    hi_content: "बाइबिल हमें न केवल यह बताती है कि कैसे जीना है, बल्कि यह भी कि कैसे खाना है!",
    zh_title: "Shèngjīng jiàodǎo rúhé chī 圣经教导如何吃",
    zh_content: "Shèngjīng bùjǐn gàosu wǒmen rúhé shēnghuó, yě gàosu wǒmen rúhé yǐnshí! 圣经不仅告诉我们如何生活，也告诉我们如何饮食！"
});

MATCH (t:THOUGHT {name: "thought.BIBLE HOW TO EAT"})
MATCH (c:CONTENT {name: "content.BIBLE HOW TO EAT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BIBLE HOW TO EAT" }]->(c);

MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:THOUGHT {name: "thought.BIBLE HOW TO EAT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >BIBLE HOW TO EAT" }]->(child);
```
