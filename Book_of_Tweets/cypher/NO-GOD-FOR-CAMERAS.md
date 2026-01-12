---
name: "thought.NO GOD FOR CAMERAS"
alias: "Thought: No God For Cameras"
type: THOUGHT
en_content: "I am convinced that God doesn't perform for cameras."
parent: "topic.THE GODHEAD"
tags:
- god
- performance
- cameras
- truth
- character
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.NO GOD FOR CAMERAS",
    alias: "Thought: No God For Cameras",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'performance', 'cameras', 'truth', 'character'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NO GOD FOR CAMERAS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NO GOD FOR CAMERAS" AND c.name = "content.NO GOD FOR CAMERAS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NO GOD FOR CAMERAS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NO GOD FOR CAMERAS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NO GOD FOR CAMERAS" }]->(child);
```
