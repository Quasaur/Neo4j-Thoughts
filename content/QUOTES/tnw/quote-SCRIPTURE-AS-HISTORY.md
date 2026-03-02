---
type: QUOTE
name: "quote.SCRIPTURE_AS_HISTORY"
alias: "Quote: Quote: SCRIPTURE AS HISTORY"
parent: "topic.THE-BIBLE"
en_content: "The Bible is the most accurate ancient library of its kind, and 1,500 years of so-called 'higher criticism' has not proven otherwise. Rather, the reliability and reputation of the Holy Scriptures has only increased with the continuous examination of Their contents."
 es_title: "Cita: LA ESCRITURA COMO HISTORIA"
 es_content: "La Biblia es la biblioteca antigua más precisa de su tipo, y 1.500 años de la llamada \"alta crítica\" no han demostrado lo contrario. Más bien, la confiabilidad y reputación de las Sagradas Escrituras solo ha aumentado con el examen continuo de Su contenido."
 fr_title: "Citation : L'ÉCRITURE COMME HISTOIRE"
 fr_content: "La Bible est la bibliothèque ancienne la plus précise de son genre, et 1 500 ans de soi-disant « haute critique » n’ont pas prouvé le contraire. Au contraire, la fiabilité et la réputation des Saintes Écritures n’ont fait qu’augmenter grâce à l’examen continu de leur contenu."
 hi_title: "उद्धरण: इतिहास के रूप में धर्मग्रंथ"
 hi_content: "बाइबिल अपनी तरह का सबसे सटीक प्राचीन पुस्तकालय है, और 1,500 वर्षों की तथाकथित 'उच्च आलोचना' अन्यथा साबित नहीं हुई है। बल्कि, पवित्र ग्रंथों की विश्वसनीयता और प्रतिष्ठा उनकी सामग्री की निरंतर जांच से ही बढ़ी है।"
 zh_title: "yǐn yòng ： shèng jīng zuò wéi lì shǐ"
 zh_content: "《 shèng jīng 》 shì tóng lèi zhōng zuì zhǔn què de gǔ dài tú shū guǎn ，1500  nián de suǒ wèi “ gāo děng pī píng ” bìng méi yǒu zhèng míng shì shí bìng fēi rú cǐ 。 xiāng fǎn ， shèng jīng de kě kào xìng hé shēng yù zhǐ huì suí zhe duì qí nèi róng de bù duàn jiǎn yàn ér zēng jiā 。"
tags: ["bible", "research", "reliability", "holyscripture", "accuracy"]
ptopic: "[[topic-THE-BIBLE]]"
level: 5
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SCRIPTURE_AS_HISTORY",
    alias: "Quote: Quote: SCRIPTURE AS HISTORY",
    parent: "topic.THE-BIBLE",
    tags: ["bible", "research", "reliability", "holyscripture", "accuracy"],
    source: "'The Narrow Way'",
    booklink: "()",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SCRIPTURE_AS_HISTORY",
    ctype: "QUOTE",
    en_title: "Quote: SCRIPTURE AS HISTORY",
    en_content: "The Bible is the most accurate ancient library of its kind, and 1,500 years of so-called 'higher criticism' has not proven otherwise. Rather, the reliability and reputation of the Holy Scriptures has only increased with the continuous examination of Their contents.",
 es_title: "Cita: LA ESCRITURA COMO HISTORIA",
 es_content: "La Biblia es la biblioteca antigua más precisa de su tipo, y 1.500 años de la llamada \"alta crítica\" no han demostrado lo contrario. Más bien, la confiabilidad y reputación de las Sagradas Escrituras solo ha aumentado con el examen continuo de Su contenido.",
 fr_title: "Citation : L'ÉCRITURE COMME HISTOIRE",
 fr_content: "La Bible est la bibliothèque ancienne la plus précise de son genre, et 1 500 ans de soi-disant « haute critique » n’ont pas prouvé le contraire. Au contraire, la fiabilité et la réputation des Saintes Écritures n’ont fait qu’augmenter grâce à l’examen continu de leur contenu.",
 hi_title: "उद्धरण: इतिहास के रूप में धर्मग्रंथ",
 hi_content: "बाइबिल अपनी तरह का सबसे सटीक प्राचीन पुस्तकालय है, और 1,500 वर्षों की तथाकथित 'उच्च आलोचना' अन्यथा साबित नहीं हुई है। बल्कि, पवित्र ग्रंथों की विश्वसनीयता और प्रतिष्ठा उनकी सामग्री की निरंतर जांच से ही बढ़ी है।",
 zh_title: "yǐn yòng ： shèng jīng zuò wéi lì shǐ",
 zh_content: "《 shèng jīng 》 shì tóng lèi zhōng zuì zhǔn què de gǔ dài tú shū guǎn ，1500  nián de suǒ wèi “ gāo děng pī píng ” bìng méi yǒu zhèng míng shì shí bìng fēi rú cǐ 。 xiāng fǎn ， shèng jīng de kě kào xìng hé shēng yù zhǐ huì suí zhe duì qí nèi róng de bù duàn jiǎn yàn ér zēng jiā 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.SCRIPTURE_AS_HISTORY"})
MATCH (c:CONTENT {name: "content.SCRIPTURE_AS_HISTORY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SCRIPTURE_AS_HISTORY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-BIBLE"})
MATCH (child:QUOTE {name: "quote.SCRIPTURE_AS_HISTORY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-BIBLE->SCRIPTURE_AS_HISTORY"}]->(child);
```