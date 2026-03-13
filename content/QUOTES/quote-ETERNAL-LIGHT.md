---
type: QUOTE
name: "quote.ETERNAL LIGHT"
alias: "Quote: Eternal Light"
parent: "topic.UNDERSTANDING"
source: "Once Saved, Always Saved: The Assurance of Our Father's LOVE"
en_content: "Eventually, as saved beings, our understanding of God will reach the point where darkness will recede into the past as a faint memory."
tags: ["saved", "understanding", "darkness", "past", "forgotten"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ETERNAL LIGHT",
    alias: "Quote: Eternal Light",
    parent: "topic.UNDERSTANDING",
    tags: ["saved", "understanding", "darkness", "past", "forgotten"],
    source: "Once Saved, Always Saved: The Assurance of Our Father's LOVE",
    booklink: "https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ETERNAL LIGHT",
    ctype: "QUOTE",
    en_title: "Quote: Eternal Light",
    en_content: "Eventually, as saved beings, our understanding of God will reach the point where darkness will recede into the past as a faint memory.",
 es_title: "Cita: Luz eterna",
 es_content: "Con el tiempo, como seres salvos, nuestra comprensión de Dios llegará al punto en que la oscuridad retrocederá hacia el pasado como un débil recuerdo.",
 fr_title: "Citation : Lumière éternelle",
 fr_content: "Finalement, en tant qu’êtres sauvés, notre compréhension de Dieu atteindra le point où les ténèbres disparaîtront dans le passé comme un vague souvenir.",
 hi_title: "उद्धरण: शाश्वत प्रकाश",
 hi_content: "अंततः, बचाए गए प्राणियों के रूप में, ईश्वर के बारे में हमारी समझ उस बिंदु तक पहुंच जाएगी जहां अंधकार एक धुंधली स्मृति के रूप में अतीत में सिमट जाएगा।",
 zh_title: "yǐn yòng ：yǒng héng zhī guāng",
 zh_content: "zuì zhōng ， zuò wéi dé jiù de rén ， wǒ men duì shén de rèn shí jiāng dá dào zhè yàng de chéng dù ： hēi àn jiāng chéng wéi guò qù de wēi ruò jì yì 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.ETERNAL LIGHT"})
MATCH (c:CONTENT {name: "content.ETERNAL LIGHT"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ETERNAL LIGHT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MATCH (child:QUOTE {name: "quote.ETERNAL LIGHT"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.UNDERSTANDING->ETERNAL LIGHT"}]->(child);

```
