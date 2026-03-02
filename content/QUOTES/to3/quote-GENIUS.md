---
type: QUOTE
name: "quote.GENIUS"
alias: "Quote: Quote: GENIUS"
parent: "topic.UNDERSTANDING"
en_content: "Genius, like patience or temperance, is a SPIRITUAL attribute that can be acquired at any point in the life by either the Sovereignty of God or by simply asking God for it.",
 es_title: "Cita: GENIO",
 es_content: "El genio, como la paciencia o la templanza, es un atributo ESPIRITUAL que se puede adquirir en cualquier momento de la vida ya sea por la Soberanía de Dios o simplemente pidiéndola a Dios.",
 fr_title: "Citation : GÉNIE",
 fr_content: "Le génie, comme la patience ou la tempérance, est un attribut SPIRITUEL qui peut être acquis à tout moment de la vie soit par la souveraineté de Dieu, soit en le demandant simplement à Dieu.",
 hi_title: "उद्धरण: प्रतिभा",
 hi_content: "प्रतिभा, धैर्य या संयम की तरह, एक आध्यात्मिक गुण है जिसे जीवन के किसी भी बिंदु पर या तो ईश्वर की संप्रभुता से या केवल ईश्वर से इसके लिए पूछकर प्राप्त किया जा सकता है।",
 zh_title: "yǐn yòng ： tiān cái",
 zh_content: "tiān cái ， jiù xiàng nài xīn huò jié zhì yī yàng ， shì yī zhǒng jīng shén shǔ xìng ， kě yǐ zài shēng mìng zhòng de rèn hé shí kè tōng guò shàng dì de zhǔ quán huò jiǎn dān dì xiàng shàng dì qí qiú lái huò dé 。"
tags: ["gift", "grace", "accomplish", "effort", "duplicate"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.GENIUS",
    alias: "Quote: Quote: GENIUS",
    parent: "topic.UNDERSTANDING",
    tags: ["gift", "grace", "accomplish", "effort", "duplicate"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.GENIUS",
    ctype: "QUOTE",
    en_title: "Quote: GENIUS",
    en_content: "Genius, like patience or temperance, is a SPIRITUAL attribute that can be acquired at any point in the life by either the Sovereignty of God or by simply asking God for it.",
 es_title: "Cita: GENIO",
 es_content: "El genio, como la paciencia o la templanza, es un atributo ESPIRITUAL que se puede adquirir en cualquier momento de la vida ya sea por la Soberanía de Dios o simplemente pidiéndola a Dios.",
 fr_title: "Citation : GÉNIE",
 fr_content: "Le génie, comme la patience ou la tempérance, est un attribut SPIRITUEL qui peut être acquis à tout moment de la vie soit par la souveraineté de Dieu, soit en le demandant simplement à Dieu.",
 hi_title: "उद्धरण: प्रतिभा",
 hi_content: "प्रतिभा, धैर्य या संयम की तरह, एक आध्यात्मिक गुण है जिसे जीवन के किसी भी बिंदु पर या तो ईश्वर की संप्रभुता से या केवल ईश्वर से इसके लिए पूछकर प्राप्त किया जा सकता है।",
 zh_title: "yǐn yòng ： tiān cái",
 zh_content: "tiān cái ， jiù xiàng nài xīn huò jié zhì yī yàng ， shì yī zhǒng jīng shén shǔ xìng ， kě yǐ zài shēng mìng zhòng de rèn hé shí kè tōng guò shàng dì de zhǔ quán huò jiǎn dān dì xiàng shàng dì qí qiú lái huò dé 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.GENIUS"})
MATCH (c:CONTENT {name: "content.GENIUS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.GENIUS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MATCH (child:QUOTE {name: "quote.GENIUS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.UNDERSTANDING->GENIUS"}]->(child);

```
