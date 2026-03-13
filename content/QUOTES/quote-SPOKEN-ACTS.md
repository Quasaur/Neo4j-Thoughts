---
type: QUOTE
name: "quote.SPOKEN ACTS"
alias: "Quote: Spoken Acts"
parent: "topic.LINGUISTICS"
source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide"
en_content: "Spoken words are human acts which are meticulously recorded in Heaven."
tags: ["spoken", "words", "idle", "acts", "accountable"]
ptopic: "[[topic-LINGUISTICS]]"
level: 5
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SPOKEN ACTS",
    alias: "Quote: Spoken Acts",
    parent: "topic.LINGUISTICS",
    tags: ["spoken", "words", "idle", "acts", "accountable"],
    source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SPOKEN ACTS",
    ctype: "QUOTE",
    en_title: "Quote: Spoken Acts",
    en_content: "Spoken words are human acts which are meticulously recorded in Heaven.",
 es_title: "Cita: Actos hablados",
 es_content: "Las palabras habladas son actos humanos que quedan meticulosamente registrados en el Cielo.",
 fr_title: "Citation : Actes parlés",
 fr_content: "Les paroles prononcées sont des actes humains méticuleusement enregistrés au Ciel.",
 hi_title: "उद्धरण: मौखिक कृत्य",
 hi_content: "बोले गए शब्द मानवीय कृत्य हैं जिन्हें स्वर्ग में सावधानीपूर्वक दर्ज किया जाता है।",
 zh_title: "yǐn yòng ：kǒu tóu xíng wéi",
 zh_content: "yán yǔ shì rén lèi de xíng wéi , zài tiān shàng bèi jīng xīn jì lù ."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.SPOKEN ACTS"})
MATCH (c:CONTENT {name: "content.SPOKEN ACTS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SPOKEN ACTS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.LINGUISTICS"})
MATCH (child:QUOTE {name: "quote.SPOKEN ACTS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.LINGUISTICS->SPOKEN ACTS"}]->(child);

```
