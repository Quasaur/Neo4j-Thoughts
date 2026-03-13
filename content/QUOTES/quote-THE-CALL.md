---
type: QUOTE
name: "quote.THE CALL"
alias: "Quote: The Call"
parent: "topic.THE GOSPEL"
source: "The Narrow Way"
en_content: "That being said, for the last two thousand years GOD has put out a call to every nation, tribe, tongue and people on the face of the planet to turn to His Only-Begotten Son Jesus Christ for the forgiveness of ALL SIN--past, present and future--and to receive The Gift of The Holy Spirit of GOD and embark on the transcendent experience of That Priceless Treasure: a Sinless, Endless Life!"
tags: ["preaching", "good_news", "glad_tidings", "command", "repentance"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE CALL",
    alias: "Quote: The Call",
    parent: "topic.THE GOSPEL",
    tags: ["preaching", "good_news", "glad_tidings", "command", "repentance"],
    source: "The Narrow Way",
    booklink: "https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE CALL",
    ctype: "QUOTE",
    en_title: "Quote: The Call",
    en_content: "That being said, for the last two thousand years GOD has put out a call to every nation, tribe, tongue and people on the face of the planet to turn to His Only-Begotten Son Jesus Christ for the forgiveness of ALL SIN--past, present and future--and to receive The Gift of The Holy Spirit of GOD and embark on the transcendent experience of That Priceless Treasure: a Sinless, Endless Life!",
 es_title: "Cita: La llamada",
 es_content: "Dicho esto, durante los últimos dos mil años, DIOS ha hecho un llamado a cada nación, tribu, lengua y pueblo sobre la faz del planeta para que recurran a Su Hijo Unigénito Jesucristo para el perdón de TODO PECADO (pasado, presente y futuro) y para recibir el Don del Espíritu Santo de DIOS y embarcarse en la experiencia trascendente de Ese Tesoro Invaluable: ¡una Vida sin pecado y sin fin!",
 fr_title: "Citation : L'appel",
 fr_content: "Cela étant dit, au cours des deux mille dernières années, DIEU a lancé un appel à chaque nation, tribu, langue et peuple de la planète à se tourner vers Son Fils unique Jésus-Christ pour le pardon de TOUS LES PÉCHÉS - passés, présents et futurs - et à recevoir le don du Saint-Esprit de DIEU et à se lancer dans l'expérience transcendante de ce trésor inestimable : une vie sans péché et sans fin !",
 hi_title: "उद्धरण: कॉल",
 hi_content: "जैसा कि कहा जा रहा है, पिछले दो हजार वर्षों से भगवान ने ग्रह के हर राष्ट्र, जनजाति, भाषा और लोगों को सभी पापों की क्षमा के लिए अपने एकमात्र पुत्र यीशु मसीह की ओर मुड़ने और भगवान की पवित्र आत्मा का उपहार प्राप्त करने और उस अमूल्य खजाने के उत्कृष्ट अनुभव को अपनाने का आह्वान किया है: एक पाप रहित, अंतहीन जीवन!",
 zh_title: "yǐn yòng ：hū huàn",
 zh_content: "huà suī zhè me shuō ， zài guò qù de liǎng qiān duō nián lǐ ， shàng dì yǐ jīng xiàng dì qiú shàng de měi yí gè guó jiā 、 bù luò 、 yǔ yán hé rén mín fā chū le hū yù ， yāo qiú tā de dú shēng zi yē sū jī dū kuān shù suǒ yǒu de zuì niè —— guò qù de 、 xiàn zài de hé wèi lái de —— bìng jiē shòu shàng dì shèng líng de ēn cì ， kāi shǐ chāo rán de tǐ yàn nà wú jià de bǎo zàng ： wú zuì 、 wú jìn de shēng mìng ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE CALL"})
MATCH (c:CONTENT {name: "content.THE CALL"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE CALL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE GOSPEL"})
MATCH (child:QUOTE {name: "quote.THE CALL"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GOSPEL->THE CALL"}]->(child);

```
