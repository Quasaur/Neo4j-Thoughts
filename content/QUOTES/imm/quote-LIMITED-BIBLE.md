---
type: QUOTE
name: "quote.LIMITED BIBLE"
alias: "Quote: Limited Bible"
parent: "topic.THE-BIBLE"
en_content: "The Holy Bible does NOT tell us all there is to know about GOD! The Bible was inspired by GOD for a very specific purpose: to give the saint everything needful to be saved from the Lake of Fire—and therefore from the power of sin.",
 es_title: "Cita: BIBLIA LIMITADA",
 es_content: "¡La Santa Biblia NO nos dice todo lo que hay que saber acerca de DIOS! La Biblia fue inspirada por DIOS con un propósito muy específico: darle al santo todo lo necesario para ser salvo del Lago de Fuego y, por lo tanto, del poder del pecado.",
 fr_title: "Citation : BIBLE LIMITÉE",
 fr_content: "La Sainte Bible ne nous dit PAS tout ce qu’il y a à savoir sur DIEU ! La Bible a été inspirée par DIEU dans un but très précis : donner au saint tout ce dont il a besoin pour être sauvé de l’étang de feu – et donc de la puissance du péché.",
 hi_title: "उद्धरण: सीमित बाइबिल",
 hi_content: "पवित्र बाइबल हमें परमेश्वर के बारे में जानने लायक सब कुछ नहीं बताती! बाइबल एक बहुत ही विशिष्ट उद्देश्य के लिए भगवान द्वारा प्रेरित की गई थी: संत को आग की झील से बचाने के लिए आवश्यक हर चीज देना - और इसलिए पाप की शक्ति से।",
 zh_title: "yǐn yòng ： yǒu xiàn shèng jīng",
 zh_content: "shèng jīng bìng méi yǒu gào sù wǒ men guān yú shàng dì de yī qiè ！ shèng jīng shì shàng dì wèi le yí gè fēi cháng jù tǐ de mù dì suǒ mò shì de ： jǐ yǔ shèng tú cóng huǒ hú zhōng zhěng jiù chū lái suǒ xū de yī qiè ， cóng ér cóng zuì de quán shì zhōng dé jiù 。"
tags: ["scriptures", "bible", "uncomprehensive", "purpose", "objective"]
ptopic: "[[topic-THE-BIBLE]]"
level: 5
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.LIMITED BIBLE",
    alias: "Quote: Limited Bible",
    parent: "topic.THE-BIBLE",
    tags: ["scriptures", "bible", "uncomprehensive", "purpose", "objective"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.LIMITED BIBLE",
    ctype: "QUOTE",
    en_title: "Limited Bible",
    en_content: "The Holy Bible does NOT tell us all there is to know about GOD! The Bible was inspired by GOD for a very specific purpose: to give the saint everything needful to be saved from the Lake of Fire—and therefore from the power of sin.",
 es_title: "Cita: BIBLIA LIMITADA",
 es_content: "¡La Santa Biblia NO nos dice todo lo que hay que saber acerca de DIOS! La Biblia fue inspirada por DIOS con un propósito muy específico: darle al santo todo lo necesario para ser salvo del Lago de Fuego y, por lo tanto, del poder del pecado.",
 fr_title: "Citation : BIBLE LIMITÉE",
 fr_content: "La Sainte Bible ne nous dit PAS tout ce qu’il y a à savoir sur DIEU ! La Bible a été inspirée par DIEU dans un but très précis : donner au saint tout ce dont il a besoin pour être sauvé de l’étang de feu – et donc de la puissance du péché.",
 hi_title: "उद्धरण: सीमित बाइबिल",
 hi_content: "पवित्र बाइबल हमें परमेश्वर के बारे में जानने लायक सब कुछ नहीं बताती! बाइबल एक बहुत ही विशिष्ट उद्देश्य के लिए भगवान द्वारा प्रेरित की गई थी: संत को आग की झील से बचाने के लिए आवश्यक हर चीज देना - और इसलिए पाप की शक्ति से।",
 zh_title: "yǐn yòng ： yǒu xiàn shèng jīng",
 zh_content: "shèng jīng bìng méi yǒu gào sù wǒ men guān yú shàng dì de yī qiè ！ shèng jīng shì shàng dì wèi le yí gè fēi cháng jù tǐ de mù dì suǒ mò shì de ： jǐ yǔ shèng tú cóng huǒ hú zhōng zhěng jiù chū lái suǒ xū de yī qiè ， cóng ér cóng zuì de quán shì zhōng dé jiù 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.LIMITED BIBLE"})
MATCH (c:CONTENT {name: "content.LIMITED BIBLE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.LIMITED BIBLE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-BIBLE"})
MATCH (child:QUOTE {name: "quote.LIMITED BIBLE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-BIBLE->LIMITED BIBLE"}]->(child);

```
