---
name: "thought.GOD SIRED CHRIST"
alias: "Thought: God Sired Christ"
type: THOUGHT
en_content: "God did not create Christ, He SIRED Him! That's why Jesus is called THE ONLY BEGOTTEN of the Father."
parent: "topic.THE GODHEAD"
tags:
- christ
- begotten
- sired
- god
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD SIRED CHRIST",
    alias: "Thought: God Sired Christ",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'begotten', 'sired', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD SIRED CHRIST",
    en_title: "God Sired Christ",
    en_content: "God did not create Christ, He SIRED Him! That's why Jesus is called THE ONLY BEGOTTEN of the Father.",
    es_title: "Dios Engendró a Cristo",
    es_content: "¡Dios no creó a Cristo, Él lo ENGENDRÓ! Por eso Jesús es llamado EL UNIGÉNITO del Padre.",
    fr_title: "Dieu a Engendré le Christ",
    fr_content: "Dieu n'a pas créé le Christ, Il l'a ENGENDRÉ ! C'est pourquoi Jésus est appelé LE FILS UNIQUE du Père.",
    hi_title: "परमेश्वर ने मसीह को जन्म दिया",
    hi_content: "परमेश्वर ने मसीह को सृजित नहीं किया, उसने उसे जन्म दिया! इसीलिए यीशु को पिता का एकलौता पुत्र कहा जाता है।",
    zh_title: "Shén shēng le Jīdū",
    zh_content: "Shén méiyǒu chuàngzào Jīdū, Tā shēng le Tā! Zhè jiùshì wèishénme Yēsū bèi chēngwéi Fùqīn de dúshēng ér."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD SIRED CHRIST" AND c.name = "content.GOD SIRED CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD SIRED CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD SIRED CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD SIRED CHRIST" }]->(child);
```
