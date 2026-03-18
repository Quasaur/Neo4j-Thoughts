---
type: THOUGHT
name: "thought.NO GOD FOR CAMERAS"
alias: "Thought: No God For Cameras"
parent: "topic.THE GODHEAD"
en_content: "I am convinced that God doesn't perform for cameras."
tags: ["god", "performance", "cameras", "truth", "character"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2012)
CREATE (t:THOUGHT {    name: "thought.NO GOD FOR CAMERAS",
    alias: "Thought: No God For Cameras",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'performance', 'cameras', 'truth', 'character'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.NO GOD FOR CAMERAS",
    ctype: "THOUGHT",
    en_title: "No God For Cameras",
    en_content: "I am convinced that God doesn't perform for cameras.",
    es_title: "Ningún Dios Para Cámaras",
    es_content: "Estoy convencido de que Dios no actúa para las cámaras.",
    fr_title: "Pas de Dieu Pour les Caméras",
    fr_content: "Je suis convaincu que Dieu ne joue pas pour les caméras.",
    hi_title: "कैमरों के लिए कोई भगवान नहीं",
    hi_content: "मैं आश्वस्त हूं कि भगवान कैमरों के लिए प्रदर्शन नहीं करते।",
    zh_title: "Méi yǒu wèi shèxiàngtóu biǎoyǎn de Shàngdì",
    zh_content: "Wǒ xiāngxìn Shàngdì bù wèi shèxiàngtóu biǎoyǎn."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NO GOD FOR CAMERAS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->NO GOD FOR CAMERAS"
RETURN t, parent;
```
