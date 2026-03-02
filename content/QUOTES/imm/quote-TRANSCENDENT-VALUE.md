---
type: QUOTE
name: "quote.TRANSCENDENT_VALUE"
alias: "Quote: Quote: TRANSCENDENT VALUE"
parent: "topic.THE-GOSPEL"
en_content: "The promise of the Gospel is that GOD The Father gives us Christ, Who is of TRANSCENDENT VALUE to Him; and in so doing we become as valuable to GOD as Christ is!",
 es_title: "Cita: VALOR TRASCENDENTE",
 es_content: "La promesa del Evangelio es que DIOS El Padre nos da a Cristo, Quien es de VALOR TRASCENDENTE para Él; ¡y al hacerlo nos volvemos tan valiosos para DIOS como lo es Cristo!",
 fr_title: "Citation : VALEUR TRANSCENDANTE",
 fr_content: "La promesse de l'Évangile est que DIEU Le Père nous donne le Christ, qui a pour Lui une VALEUR TRANSCENDANTE ; et ce faisant, nous devenons aussi précieux pour DIEU que Christ !",
 hi_title: "उद्धरण: पारलौकिक मूल्य",
 hi_content: "सुसमाचार का वादा यह है कि परमेश्वर पिता हमें मसीह देता है, जो उसके लिए उत्कृष्ट मूल्य का है; और ऐसा करने से हम परमेश्वर के लिए उतने ही मूल्यवान बन जाते हैं जितने मसीह हैं!",
 zh_title: "yǐn yòng ： chāo yuè jià zhí",
 zh_content: "fú yīn de yīng xǔ shì ， tiān fù shàng dì jiāng jī dū cì gěi wǒ men ， jī dū duì tā lái shuō jù yǒu chāo yuè de jià zhí ； zhè yàng zuò ， wǒ men jiù biàn dé xiàng jī dū yī yàng duì shàng dì yǒu jià zhí ！"
tags: ["gospel", "promise", "jesus_christ", "value", "precious"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.TRANSCENDENT_VALUE",
    alias: "Quote: Quote: TRANSCENDENT VALUE",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "promise", "jesus_christ", "value", "precious"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.TRANSCENDENT_VALUE",
    ctype: "QUOTE",
    en_title: "Quote: TRANSCENDENT VALUE",
    en_content: "The promise of the Gospel is that GOD The Father gives us Christ, Who is of TRANSCENDENT VALUE to Him; and in so doing we become as valuable to GOD as Christ is!",
 es_title: "Cita: VALOR TRASCENDENTE",
 es_content: "La promesa del Evangelio es que DIOS El Padre nos da a Cristo, Quien es de VALOR TRASCENDENTE para Él; ¡y al hacerlo nos volvemos tan valiosos para DIOS como lo es Cristo!",
 fr_title: "Citation : VALEUR TRANSCENDANTE",
 fr_content: "La promesse de l'Évangile est que DIEU Le Père nous donne le Christ, qui a pour Lui une VALEUR TRANSCENDANTE ; et ce faisant, nous devenons aussi précieux pour DIEU que Christ !",
 hi_title: "उद्धरण: पारलौकिक मूल्य",
 hi_content: "सुसमाचार का वादा यह है कि परमेश्वर पिता हमें मसीह देता है, जो उसके लिए उत्कृष्ट मूल्य का है; और ऐसा करने से हम परमेश्वर के लिए उतने ही मूल्यवान बन जाते हैं जितने मसीह हैं!",
 zh_title: "yǐn yòng ： chāo yuè jià zhí",
 zh_content: "fú yīn de yīng xǔ shì ， tiān fù shàng dì jiāng jī dū cì gěi wǒ men ， jī dū duì tā lái shuō jù yǒu chāo yuè de jià zhí ； zhè yàng zuò ， wǒ men jiù biàn dé xiàng jī dū yī yàng duì shàng dì yǒu jià zhí ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.TRANSCENDENT_VALUE"})
MATCH (c:CONTENT {name: "content.TRANSCENDENT_VALUE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.TRANSCENDENT_VALUE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MATCH (child:QUOTE {name: "quote.TRANSCENDENT_VALUE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->TRANSCENDENT_VALUE"}]->(child);

```
