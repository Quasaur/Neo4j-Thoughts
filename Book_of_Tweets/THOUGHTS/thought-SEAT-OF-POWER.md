---
type: THOUGHT
name: "thought.SEAT OF POWER"
alias: "Thought: Seat Of Power"
parent: "topic.THE GODHEAD"
en_content: "The Seat of True Power is in Heaven, where the Christ patiently waits for His Daddy to turn His Enemies into His footrest."
tags: ["power", "heaven", "christ", "enemies"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Apr-2014)
CREATE (t:THOUGHT {    name: "thought.SEAT OF POWER",
    alias: "Thought: Seat Of Power",
    parent: "topic.THE GODHEAD",
    tags: ['power', 'heaven', 'christ', 'enemies'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.SEAT OF POWER",
    ctype: "THOUGHT",
    en_title: "Seat Of Power",
    en_content: "The Seat of True Power is in Heaven, where the Christ patiently waits for His Daddy to turn His Enemies into His footrest.",
    es_title: "Sede del Poder",
    es_content: "La Sede del Verdadero Poder está en el Cielo, donde Cristo espera pacientemente a que Su Padre convierta a Sus Enemigos en Su estrado.",
    fr_title: "Siège du Pouvoir",
    fr_content: "Le Siège du Vrai Pouvoir est au Ciel, où le Christ attend patiemment que Son Père transforme Ses Ennemis en Son marchepied.",
    hi_title: "शक्ति का सिंहासन",
    hi_content: "सच्ची शक्ति का सिंहासन स्वर्ग में है, जहाँ मसीह धैर्य से प्रतीक्षा करता है कि उसके पिता उसके शत्रुओं को उसकी चरण-पीठिका बना दें।",
    zh_title: "Quánlì zhī Zuò",
    zh_content: "Zhēnzhèng Quánlì zhī Zuò zài Tiāntáng, Jīdū zài nàlǐ nàixīn děngdài Tā de Tiānfù bǎ Tā de Dírén biànchéng Tā de jiǎodèng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SEAT OF POWER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->SEAT OF POWER"
RETURN t, parent;
```
