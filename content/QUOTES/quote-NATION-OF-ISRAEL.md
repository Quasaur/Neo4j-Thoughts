---
type: QUOTE
name: "quote.NATION OF ISRAEL"
alias: "Quote: Nation of Israel"
parent: "topic.POLITICAL SCIENCE"
source: "The Traveler's Oasis, Book Three"
en_content: "The Bible makes a crucial distinction between the Earthly, physical Nation of Israel, which is temporary and the SPIRITUAL Nation of Israel, which is Infinite; nothing about the Gospel or Biblical prophecy makes sense without this truth."
tags: ["nation", "israel", "earthly", "spiritual", "prophecy"]
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NATION OF ISRAEL",
    alias: "Quote: Nation of Israel",
    parent: "topic.POLITICAL SCIENCE",
    tags: ["nation", "israel", "earthly", "spiritual", "prophecy"],
    source: "The Traveler's Oasis, Book Three",
    booklink: "https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NATION OF ISRAEL",
    ctype: "QUOTE",
    en_title: "Quote: Nation of Israel",
    en_content: "The Bible makes a crucial distinction between the Earthly, physical Nation of Israel, which is temporary and the SPIRITUAL Nation of Israel, which is Infinite; nothing about the Gospel or Biblical prophecy makes sense without this truth.",
 es_title: "Cita: Nación de Israel",
 es_content: "La Biblia hace una distinción crucial entre la Nación física y terrenal de Israel, que es temporal, y la Nación ESPIRITUAL de Israel, que es Infinita; nada sobre el Evangelio o la profecía bíblica tiene sentido sin esta verdad.",
 fr_title: "Citation : Nation d'Israël",
 fr_content: "La Bible fait une distinction cruciale entre la nation terrestre et physique d'Israël, qui est temporaire, et la nation spirituelle d'Israël, qui est infinie ; rien dans l’Évangile ou dans la prophétie biblique n’a de sens sans cette vérité.",
 hi_title: "उद्धरण: इज़राइल राष्ट्र",
 hi_content: "बाइबल इज़राइल के सांसारिक, भौतिक राष्ट्र, जो अस्थायी है और इज़राइल के आध्यात्मिक राष्ट्र, जो अनंत है, के बीच एक महत्वपूर्ण अंतर बनाती है; इस सत्य के बिना सुसमाचार या बाइबिल की भविष्यवाणी के बारे में कुछ भी समझ में नहीं आता है।",
 zh_title: "yǐn yòng ：yǐ sè liè mín zú bào",
 zh_content: "shèng jīng duì dì qiú shàng de yǐ sè liè guó （ zàn shí de ） hé jīng shén shàng de yǐ sè liè guó （ wú xiàn de ） zuò chū le zhì guān zhòng yào de qū fēn . rú guǒ méi yǒu zhè ge zhēn lǐ , fú yīn huò shèng jīng de yù yán jiù háo wú yì yì ."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.NATION OF ISRAEL"})
MATCH (c:CONTENT {name: "content.NATION OF ISRAEL"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NATION OF ISRAEL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.POLITICAL SCIENCE"})
MATCH (child:QUOTE {name: "quote.NATION OF ISRAEL"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.POLITICAL SCIENCE->NATION OF ISRAEL"}]->(child);

```
