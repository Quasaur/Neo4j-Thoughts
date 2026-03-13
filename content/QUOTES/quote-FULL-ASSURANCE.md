---
type: QUOTE
name: "quote.FULL ASSURANCE"
alias: "Quote: Full Assurance"
parent: "topic.GRACE"
source: "The Narrow Way"
en_content: "I know that KNOWING that you're going to be Saved from the Wrath of GOD is declared heresy by the Roman Catholic Church; if you STUDY A RELIABLE TRANSLATION OF THE BIBLE, however, you will see that GOD wants you to be assured and confident of your eternal destiny (1 John 5:13-15)."
tags: ["knowing", "confidence", "guarantee", "holy_spirit", "divine_witness"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FULL ASSURANCE",
    alias: "Quote: Full Assurance",
    parent: "topic.GRACE",
    tags: ["knowing", "confidence", "guarantee", "holy_spirit", "divine_witness"],
    source: "The Narrow Way",
    booklink: "https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FULL ASSURANCE",
    ctype: "QUOTE",
    en_title: "Quote: Full Assurance",
    en_content: "I know that KNOWING that you're going to be Saved from the Wrath of GOD is declared heresy by the Roman Catholic Church; if you STUDY A RELIABLE TRANSLATION OF THE BIBLE, however, you will see that GOD wants you to be assured and confident of your eternal destiny (1 John 5:13-15).",
 es_title: "Cita: Total Garantía",
 es_content: "Sé que SABER que vas a ser Salvado de la Ira de DIOS es declarado herejía por la Iglesia Católica Romana; Sin embargo, si ESTUDIAS UNA TRADUCCIÓN CONFIABLE DE LA BIBLIA, verás que DIOS quiere que tengas seguridad y confianza en tu destino eterno (1 Juan 5:13-15).",
 fr_title: "Citation : Assurance totale",
 fr_content: "Je sais que SAVOIR que vous allez être sauvé de la colère de DIEU est déclaré hérésie par l'Église catholique romaine ; Cependant, si vous ÉTUDIEZ UNE TRADUCTION FIABLE DE LA BIBLE, vous verrez que DIEU veut que vous soyez assuré et confiant de votre destinée éternelle (1 Jean 5 : 13-15).",
 hi_title: "उद्धरण: पूर्ण आश्वासन",
 hi_content: "मैं जानता हूं कि यह जानना कि आप ईश्वर के क्रोध से बच जायेंगे, रोमन कैथोलिक चर्च द्वारा विधर्म घोषित किया गया है; हालाँकि, यदि आप बाइबल के विश्वसनीय अनुवाद का अध्ययन करते हैं, तो आप देखेंगे कि ईश्वर चाहता है कि आप अपने शाश्वत भाग्य के प्रति आश्वस्त और आश्वस्त रहें (1 यूहन्ना 5:13-15)।",
 zh_title: "bào jià ：chōng fèn bǎo zhèng",
 zh_content: "wǒ zhī dào luó mǎ tiān zhǔ jiào huì xuān bù  zhī dào nǐ jiāng cóng shàng dì de fèn nù zhōng bèi zhěng jiù  wèi yì duān ; rán ér , rú guǒ nǐ yán jiū kě kào de shèng jīng yì běn , nǐ jiù huì fā xiàn shén xī wàng nǐ duì nǐ yǒng héng de mìng yùn yǒu bǎ wò hé xìn xīn （ yuē hàn yī shū 5:13-15）."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.FULL ASSURANCE"})
MATCH (c:CONTENT {name: "content.FULL ASSURANCE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FULL ASSURANCE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.FULL ASSURANCE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->FULL ASSURANCE"}]->(child);

```
