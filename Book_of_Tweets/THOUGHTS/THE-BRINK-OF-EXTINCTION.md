---
name: "thought.THE BRINK OF EXTINCTION"
alias: "Thought: The Brink Of Extinction"
type: THOUGHT
en_content: "Matthew 24:21, 22: It may be that Christ will not return until humanity is on the brink of extinction."
parent: "topic.THE GODHEAD"
tags:
- prophecy
- christ
- return
- humanity
- judgment
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Dec-2010)
CREATE (t:THOUGHT {
    name: "thought.THE BRINK OF EXTINCTION",
    alias: "Thought: The Brink Of Extinction",
    parent: "topic.THE GODHEAD",
    tags: ['prophecy', 'christ', 'return', 'humanity', 'judgment'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE BRINK OF EXTINCTION",
    en_title: "The Brink Of Extinction",
    en_content: "Matthew 24:21, 22: It may be that Christ will not return until humanity is on the brink of extinction.",
    es_title: "Al Borde de la Extinción",
    es_content: "Mateo 24:21, 22: Puede ser que Cristo no regrese hasta que la humanidad esté al borde de la extinción.",
    fr_title: "Au Bord de l'Extinction",
    fr_content: "Matthieu 24:21, 22: Il se peut que le Christ ne revienne pas avant que l'humanité ne soit au bord de l'extinction.",
    hi_title: "विलुप्ति के कगार पर",
    hi_content: "मत्ती 24:21, 22: यह हो सकता है कि मसीह तब तक वापस न आएं जब तक मानवता विलुप्ति के कगार पर न पहुंच जाए।",
    zh_title: "Miè jué de biān yuán",
    zh_content: "Mǎ tài fú yīn 24:21, 22: Yě xǔ Jī dū bù huì zài rén lèi miàn lín miè jué zhī qián guī lái."
});

MATCH (t:THOUGHT {name: "thought.THE BRINK OF EXTINCTION"})
MATCH (c:CONTENT {name: "content.THE BRINK OF EXTINCTION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE BRINK OF EXTINCTION" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.THE BRINK OF EXTINCTION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->THE BRINK OF EXTINCTION" }]->(child);
```
