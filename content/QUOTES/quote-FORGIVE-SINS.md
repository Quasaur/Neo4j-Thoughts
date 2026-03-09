---
type: QUOTE
name: "quote.FORGIVE SINS"
alias: "Quote: Forgive Sins"
parent: "topic.MERCY"
source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'"
en_content: "Only GOD The Word (in the Person of The Lord Jesus Christ) has authority on Earth to forgive sins and apply His own Blood to the soul of the sinner!",
 es_title: "Cita: PERDONA LOS PECADOS",
 es_content: "¡Sólo DIOS La Palabra (en la Persona del Señor Jesucristo) tiene autoridad en la Tierra para perdonar pecados y aplicar Su propia Sangre al alma del pecador!",
 fr_title: "Citation : PARDONNER LES PÉCHÉS",
 fr_content: "Seul DIEU La Parole (dans la personne du Seigneur Jésus-Christ) a l'autorité sur Terre pour pardonner les péchés et appliquer Son propre Sang à l'âme du pécheur !",
 hi_title: "उद्धरण: पापों को क्षमा करें",
 hi_content: "पृथ्वी पर केवल वचन परमेश्वर (प्रभु यीशु मसीह के रूप में) के पास ही पापों को क्षमा करने और पापी की आत्मा पर अपना रक्त लगाने का अधिकार है!",
 zh_title: "yǐn yòng ： kuān shù zuì è",
 zh_content: "zhǐ yǒu shén dào （ yǐ zhǔ yē sū jī dū de shēn fèn ） zài dì qiú shàng yǒu quán bǐng shè miǎn zuì bìng jiāng tā zì jǐ de bǎo xuè yìng yòng dào zuì rén de líng hún shàng ！"
tags: ["jesus_christ", "authority", "earth", "remission", "sins"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FORGIVE SINS",
    alias: "Quote: Forgive Sins",
    parent: "topic.MERCY",
    tags: ["jesus_christ", "authority", "earth", "remission", "sins"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FORGIVE SINS",
    ctype: "QUOTE",
    en_title: "Forgive Sins",
    en_content: "Only GOD The Word (in the Person of The Lord Jesus Christ) has authority on Earth to forgive sins and apply His own Blood to the soul of the sinner!",
 es_title: "Cita: PERDONA LOS PECADOS",
 es_content: "¡Sólo DIOS La Palabra (en la Persona del Señor Jesucristo) tiene autoridad en la Tierra para perdonar pecados y aplicar Su propia Sangre al alma del pecador!",
 fr_title: "Citation : PARDONNER LES PÉCHÉS",
 fr_content: "Seul DIEU La Parole (dans la personne du Seigneur Jésus-Christ) a l'autorité sur Terre pour pardonner les péchés et appliquer Son propre Sang à l'âme du pécheur !",
 hi_title: "उद्धरण: पापों को क्षमा करें",
 hi_content: "पृथ्वी पर केवल वचन परमेश्वर (प्रभु यीशु मसीह के रूप में) के पास ही पापों को क्षमा करने और पापी की आत्मा पर अपना रक्त लगाने का अधिकार है!",
 zh_title: "yǐn yòng ： kuān shù zuì è",
 zh_content: "zhǐ yǒu shén dào （ yǐ zhǔ yē sū jī dū de shēn fèn ） zài dì qiú shàng yǒu quán bǐng shè miǎn zuì bìng jiāng tā zì jǐ de bǎo xuè yìng yòng dào zuì rén de líng hún shàng ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.FORGIVE SINS"})
MATCH (c:CONTENT {name: "content.FORGIVE SINS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FORGIVE SINS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.MERCY"})
MATCH (child:QUOTE {name: "quote.FORGIVE SINS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.MERCY->FORGIVE SINS"}]->(child);

```
