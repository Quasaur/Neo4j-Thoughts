---
name: "thought.UNDERSTANDING SIN HELL"
alias: "Thought: Understanding Sin Hell"
type: THOUGHT
en_content: "You will never understand how God feels about sin until you look into Hell."
parent: "topic.EVIL"
tags:
- sin
- hell
- judgment
- god
- character
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Aug-2012)
CREATE (t:THOUGHT {
    name: "thought.UNDERSTANDING SIN HELL",
    alias: "Thought: Understanding Sin Hell",
    parent: "topic.EVIL",
    tags: ['sin', 'hell', 'judgment', 'god', 'character'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.UNDERSTANDING SIN HELL",
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

MATCH (t:THOUGHT {name: "thought.UNDERSTANDING SIN HELL"})
MATCH (c:CONTENT {name: "content.UNDERSTANDING SIN HELL"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNDERSTANDING SIN HELL" }]->(c);

MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:THOUGHT {name: "thought.UNDERSTANDING SIN HELL"})
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >UNDERSTANDING SIN HELL" }]->(child);
```
