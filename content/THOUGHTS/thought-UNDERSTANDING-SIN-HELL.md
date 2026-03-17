---
type: THOUGHT
name: "thought.UNDERSTANDING SIN HELL"
alias: "Thought: Understanding Sin Hell"
parent: "topic.EVIL"
en_content: "You will never understand how God feels about sin until you look into Hell."
tags: ["sin", "hell", "judgment", "god", "character"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.UNDERSTANDING SIN HELL",
    alias: "Thought: Understanding Sin Hell",
    parent: "topic.EVIL",
    tags: ['sin', 'hell', 'judgment', 'god', 'character'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.UNDERSTANDING SIN HELL",
    ctype: "THOUGHT",
    en_title: "Understanding Sin Hell",
    en_content: "You will never understand how God feels about sin until you look into Hell.",
    es_title: "Entendiendo el Pecado y el Infierno",
    es_content: "Nunca entenderás cómo se siente Dios acerca del pecado hasta que mires hacia el Infierno.",
    fr_title: "Comprendre le Péché et l'Enfer",
    fr_content: "Tu ne comprendras jamais ce que Dieu ressent à propos du péché jusqu'à ce que tu regardes dans l'Enfer.",
    hi_title: "पाप और नरक को समझना",
    hi_content: "जब तक आप नरक में नहीं देखते, तब तक आप कभी नहीं समझ पाएंगे कि परमेश्वर पाप के बारे में कैसा महसूस करता है।",
    zh_title: "Li Jie Zui Yu Di Yu",
    zh_content: "Zhi you dang ni kan xiang di yu shi, ni cai neng li jie Shang Di dui zui de gan shou."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNDERSTANDING SIN HELL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->UNDERSTANDING SIN HELL"
RETURN t, parent;
```
