---
type: QUOTE
name: "quote.UNCONDITIONAL GRACE"
alias: "Quote: Unconditional Grace"
parent: "topic.GRACE"
source: "Once Saved, Always Saved: The Assurance of Our Father's LOVE"
en_content: "The Purpose of the Gospel is to bring fallen humanity into The Fellowship of The Godhead. And since the Fellowship of The Godhead is Itself unconditional, The Gospel of Grace must also be unconditional."
tags: ["saved", "understanding", "darkness", "past", "forgotten"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.UNCONDITIONAL GRACE",
    alias: "Quote: Unconditional Grace",
    parent: "topic.GRACE",
    tags: ["saved", "understanding", "darkness", "past", "forgotten"],
    source: "Once Saved, Always Saved: The Assurance of Our Father's LOVE",
    booklink: "https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL GRACE",
    ctype: "QUOTE",
    en_title: "Quote: Unconditional Grace",
    en_content: "The Purpose of the Gospel is to bring fallen humanity into The Fellowship of The Godhead. And since the Fellowship of The Godhead is Itself unconditional, The Gospel of Grace must also be unconditional.",
 es_title: "Cita: Gracia incondicional",
 es_content: "El propósito del Evangelio es traer a la humanidad caída a la Comunidad de la Divinidad. Y dado que la comunión de la Deidad es en sí misma incondicional, el Evangelio de la Gracia también debe ser incondicional.",
 fr_title: "Citation : Grâce inconditionnelle",
 fr_content: "Le but de l’Évangile est d’amener l’humanité déchue dans la communion de la Divinité. Et puisque la communion avec la Divinité est elle-même inconditionnelle, l’Évangile de la Grâce doit également être inconditionnel.",
 hi_title: "उद्धरण: बिना शर्त अनुग्रह",
 hi_content: "सुसमाचार का उद्देश्य पतित मानवता को ईश्वरत्व की संगति में लाना है। और चूँकि ईश्वर की संगति स्वयं बिना शर्त है, अनुग्रह का सुसमाचार भी बिना शर्त होना चाहिए।",
 zh_title: "yǐn yòng ：wú tiáo jiàn de ēn diǎn",
 zh_content: "fú yīn de mù dì shì jiāng duò luò de rén lèi dài rù shén xìng de tuán qì zhōng . jì rán shén xìng de tuán qì běn shēn shì wú tiáo jiàn de , ēn diǎn de fú yīn yě bì xū shì wú tiáo jiàn de ."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.UNCONDITIONAL GRACE"})
MATCH (c:CONTENT {name: "content.UNCONDITIONAL GRACE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.UNCONDITIONAL GRACE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.UNCONDITIONAL GRACE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->UNCONDITIONAL GRACE"}]->(child);

```
