---
type: QUOTE
name: "quote.LOGICAL_COURSE"
alias: "Quote: Quote: LOGICAL COURSE"
parent: "topic.FAITH"
en_content: "The logical course of action for an ignorant creature (and all creatures are ignorant to varying degrees) is to place its total faith in its Creator Who knows and understands all.",
 es_title: "Cita: CURSO LÓGICO",
 es_content: "El curso de acción lógico para una criatura ignorante (y todas las criaturas son ignorantes en diversos grados) es depositar su fe total en su Creador, Quien lo sabe y lo comprende todo.",
 fr_title: "Citation : COURS LOGIQUE",
 fr_content: "La ligne de conduite logique pour une créature ignorante (et toutes les créatures sont ignorantes à des degrés divers) est de placer sa confiance totale en son Créateur qui sait et comprend tout.",
 hi_title: "उद्धरण: तार्किक पाठ्यक्रम",
 hi_content: "एक अज्ञानी प्राणी (और सभी प्राणी अलग-अलग डिग्री तक अज्ञानी हैं) के लिए कार्रवाई का तार्किक तरीका अपने निर्माता पर अपना पूरा विश्वास रखना है जो सब कुछ जानता और समझता है।",
 zh_title: "yǐn yòng ： luó jí kè chéng",
 zh_content: "duì yú yí gè wú zhī de shēng wù （ suǒ yǒu de shēng wù dōu bù tóng chéng dù dì wú zhī ） lái shuō ， hé hū luó jí de xíng dòng fāng zhēn shì wán quán xiāng xìn zhī dào bìng lǐ jiě yī qiè de zào wù zhǔ 。"
tags: ["logic", "action", "faith", "creator", "understanding"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.LOGICAL_COURSE",
    alias: "Quote: Quote: LOGICAL COURSE",
    parent: "topic.FAITH",
    tags: ["logic", "action", "faith", "creator", "understanding"],
    source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'",
    booklink: "(https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.LOGICAL_COURSE",
    ctype: "QUOTE",
    en_title: "Quote: LOGICAL COURSE",
    en_content: "The logical course of action for an ignorant creature (and all creatures are ignorant to varying degrees) is to place its total faith in its Creator Who knows and understands all.",
 es_title: "Cita: CURSO LÓGICO",
 es_content: "El curso de acción lógico para una criatura ignorante (y todas las criaturas son ignorantes en diversos grados) es depositar su fe total en su Creador, Quien lo sabe y lo comprende todo.",
 fr_title: "Citation : COURS LOGIQUE",
 fr_content: "La ligne de conduite logique pour une créature ignorante (et toutes les créatures sont ignorantes à des degrés divers) est de placer sa confiance totale en son Créateur qui sait et comprend tout.",
 hi_title: "उद्धरण: तार्किक पाठ्यक्रम",
 hi_content: "एक अज्ञानी प्राणी (और सभी प्राणी अलग-अलग डिग्री तक अज्ञानी हैं) के लिए कार्रवाई का तार्किक तरीका अपने निर्माता पर अपना पूरा विश्वास रखना है जो सब कुछ जानता और समझता है।",
 zh_title: "yǐn yòng ： luó jí kè chéng",
 zh_content: "duì yú yí gè wú zhī de shēng wù （ suǒ yǒu de shēng wù dōu bù tóng chéng dù dì wú zhī ） lái shuō ， hé hū luó jí de xíng dòng fāng zhēn shì wán quán xiāng xìn zhī dào bìng lǐ jiě yī qiè de zào wù zhǔ 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.LOGICAL_COURSE"})
MATCH (c:CONTENT {name: "content.LOGICAL_COURSE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.LOGICAL_COURSE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:QUOTE {name: "quote.LOGICAL_COURSE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.FAITH->LOGICAL_COURSE"}]->(child);

```
