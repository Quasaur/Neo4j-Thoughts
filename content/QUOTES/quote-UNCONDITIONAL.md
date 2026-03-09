---
type: QUOTE
name: "quote.UNCONDITIONAL"
alias: "Quote: Unconditional"
parent: "topic.GRACE"
en_content: "The Purpose of the Gospel is to bring fallen humanity into The Fellowship of The GODHEAD. And since the Fellowship of The GODHEAD is Itself unconditional, The Gospel of Grace must also be unconditional.",
 es_title: "Cita: INCONDICIONAL",
 es_content: "El Propósito del Evangelio es traer a la humanidad caída a La Comunidad de La Divinidad. Y dado que la Comunidad de La Divinidad es en sí misma incondicional, el Evangelio de la Gracia también debe ser incondicional.",
 fr_title: "Citation : INCONDITIONNEL",
 fr_content: "Le but de l’Évangile est d’amener l’humanité déchue dans la Communauté de la DIVINITÉ. Et puisque la Communauté de la DIVINITÉ est elle-même inconditionnelle, l’Évangile de la Grâce doit également être inconditionnel.",
 hi_title: "उद्धरण: बिना शर्त",
 hi_content: "सुसमाचार का उद्देश्य गिरी हुई मानवता को ईश्वर की संगति में लाना है। और चूँकि ईश्वर की संगति स्वयं बिना शर्त है, अनुग्रह का सुसमाचार भी बिना शर्त होना चाहिए।",
 zh_title: "bào jià ： wú tiáo jiàn",
 zh_content: "fú yīn de mù dì shì jiāng duò luò de rén lèi dài rù shén xìng de tuán qì zhōng 。 jì rán shén xìng de tuán qì běn shēn shì wú tiáo jiàn de ， ēn diǎn de fú yīn yě bì xū shì wú tiáo jiàn de 。"
tags: ["gospel", "purpose", "fellowship", "godhead", "unconditional"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.UNCONDITIONAL",
    alias: "Quote: Unconditional",
    parent: "topic.GRACE",
    tags: ["gospel", "purpose", "fellowship", "godhead", "unconditional"],
    source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'",
    booklink: "(https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL",
    ctype: "QUOTE",
    en_title: "Unconditional",
    en_content: "The Purpose of the Gospel is to bring fallen humanity into The Fellowship of The GODHEAD. And since the Fellowship of The GODHEAD is Itself unconditional, The Gospel of Grace must also be unconditional.",
 es_title: "Cita: INCONDICIONAL",
 es_content: "El Propósito del Evangelio es traer a la humanidad caída a La Comunidad de La Divinidad. Y dado que la Comunidad de La Divinidad es en sí misma incondicional, el Evangelio de la Gracia también debe ser incondicional.",
 fr_title: "Citation : INCONDITIONNEL",
 fr_content: "Le but de l’Évangile est d’amener l’humanité déchue dans la Communauté de la DIVINITÉ. Et puisque la Communauté de la DIVINITÉ est elle-même inconditionnelle, l’Évangile de la Grâce doit également être inconditionnel.",
 hi_title: "उद्धरण: बिना शर्त",
 hi_content: "सुसमाचार का उद्देश्य गिरी हुई मानवता को ईश्वर की संगति में लाना है। और चूँकि ईश्वर की संगति स्वयं बिना शर्त है, अनुग्रह का सुसमाचार भी बिना शर्त होना चाहिए।",
 zh_title: "bào jià ： wú tiáo jiàn",
 zh_content: "fú yīn de mù dì shì jiāng duò luò de rén lèi dài rù shén xìng de tuán qì zhōng 。 jì rán shén xìng de tuán qì běn shēn shì wú tiáo jiàn de ， ēn diǎn de fú yīn yě bì xū shì wú tiáo jiàn de 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.UNCONDITIONAL"})
MATCH (c:CONTENT {name: "content.UNCONDITIONAL"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.UNCONDITIONAL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.UNCONDITIONAL"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->UNCONDITIONAL"}]->(child);

```
