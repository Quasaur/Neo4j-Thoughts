---
type: QUOTE
name: "quote.NO NEED"
alias: "Quote: No Need"
parent: "topic.WEALTH"
en_content: "You do not need money to either survive or thrive in this life or the next.",
 es_title: "Cita: NO ES NECESARIO",
 es_content: "No necesitas dinero para sobrevivir o prosperar en esta vida o en la siguiente.",
 fr_title: "Citation : PAS BESOIN",
 fr_content: "Vous n’avez pas besoin d’argent pour survivre ou prospérer dans cette vie ou dans la suivante.",
 hi_title: "उद्धरण: कोई ज़रूरत नहीं",
 hi_content: "आपको इस जीवन या अगले जीवन में जीवित रहने या आगे बढ़ने के लिए धन की आवश्यकता नहीं है।",
 zh_title: "yǐn yòng ：  bù xū yào",
 zh_content: "nǐ bù xū yào jīn qián lái zài jīn shēng huò lái shì shēng cún huò fā zhǎn 。"
tags: ["survive", "thrive", "needless", "money", "wisdom"]
ptopic: "[[topic-WEALTH]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NO NEED",
    alias: "Quote: No Need",
    parent: "topic.WEALTH",
    tags: ["survive", "thrive", "needless", "money", "wisdom"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NO NEED",
    ctype: "QUOTE",
    en_title: "No Need",
    en_content: "You do not need money to either survive or thrive in this life or the next.",
 es_title: "Cita: NO ES NECESARIO",
 es_content: "No necesitas dinero para sobrevivir o prosperar en esta vida o en la siguiente.",
 fr_title: "Citation : PAS BESOIN",
 fr_content: "Vous n’avez pas besoin d’argent pour survivre ou prospérer dans cette vie ou dans la suivante.",
 hi_title: "उद्धरण: कोई ज़रूरत नहीं",
 hi_content: "आपको इस जीवन या अगले जीवन में जीवित रहने या आगे बढ़ने के लिए धन की आवश्यकता नहीं है।",
 zh_title: "yǐn yòng ：  bù xū yào",
 zh_content: "nǐ bù xū yào jīn qián lái zài jīn shēng huò lái shì shēng cún huò fā zhǎn 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.NO NEED"})
MATCH (c:CONTENT {name: "content.NO NEED"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NO NEED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.WEALTH"})
MATCH (child:QUOTE {name: "quote.NO NEED"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.WEALTH->NO NEED"}]->(child);

```
