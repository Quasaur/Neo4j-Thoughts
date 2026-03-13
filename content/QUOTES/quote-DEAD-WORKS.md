---
type: QUOTE
name: "quote.DEAD WORKS"
alias: "Quote: Dead Works"
parent: "topic.RELIGION"
source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide"
en_content: "The obedience of the sinner CANNOT BE ACCEPTED by GOD because since the sinner is spiritually dead THEIR OBEDIENCE IS DEAD AS WELL."
tags: ["sinner", "obedience", "dead_spirit", "works", "filthy_rags"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.DEAD WORKS",
    alias: "Quote: Dead Works",
    parent: "topic.RELIGION",
    tags: ["sinner", "obedience", "dead_spirit", "works", "filthy_rags"],
    source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide",
    booklink: "https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.DEAD WORKS",
    ctype: "QUOTE",
    en_title: "Quote: Dead Works",
    en_content: "The obedience of the sinner CANNOT BE ACCEPTED by GOD because since the sinner is spiritually dead THEIR OBEDIENCE IS DEAD AS WELL.",
 es_title: "Cita: Obras muertas",
 es_content: "La obediencia del pecador NO PUEDE SER ACEPTADA por DIOS porque como el pecador está espiritualmente muerto, SU OBEDIENCIA TAMBIÉN ESTÁ MUERTA.",
 fr_title: "Citation : Œuvres mortes",
 fr_content: "L'obéissance du pécheur NE PEUT PAS ÊTRE ACCEPTÉE PAR DIEU car puisque le pécheur est spirituellement mort, LEUR OBÉISSANCE EST MORTE AUSSI.",
 hi_title: "उद्धरण: मृत कार्य",
 hi_content: "पापी की आज्ञाकारिता को ईश्वर द्वारा स्वीकार नहीं किया जा सकता क्योंकि चूँकि पापी आध्यात्मिक रूप से मर चुका है इसलिए उसकी आज्ञाकारिता भी मृत है।",
 zh_title: "yǐn yòng ：sǐ wáng zuò pǐn",
 zh_content: "zuì rén de shùn fú bù néng bèi shén suǒ jiē shòu ， yīn wèi zuì rén zài líng xìng shàng shì sǐ de ， tā men de shùn fú yě sǐ le 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.DEAD WORKS"})
MATCH (c:CONTENT {name: "content.DEAD WORKS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.DEAD WORKS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.DEAD WORKS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->DEAD WORKS"}]->(child);

```
