---
type: QUOTE
name: "quote.THE CROSS"
alias: "Quote: The Cross"
parent: "topic.THE GOSPEL"
source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide"
en_content: "The Power of the Gospel is The Cross of Jesus Christ. The 'magic' of The Cross is that GOD loved us so unconditionally and so deeply that He spared neither Himself nor us the pain and agony necessary to provide us a complete delivery from the power, penalty and—most important—the love of and need for sin."
tags: ["gospel", "power", "jesus_christ", "redemption", "sanctification"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE CROSS",
    alias: "Quote: The Cross",
    parent: "topic.THE GOSPEL",
    tags: ["gospel", "power", "jesus_christ", "redemption", "sanctification"],
    source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide",
    booklink: "https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE CROSS",
    ctype: "QUOTE",
    en_title: "Quote: The Cross",
    en_content: "The Power of the Gospel is The Cross of Jesus Christ. The “magic” of The Cross is that GOD loved us so unconditionally and so deeply that He spared neither Himself nor us the pain and agony necessary to provide us a complete delivery from the power, penalty and—most important—the love of and need for sin.",
 es_title: "Cita: La Cruz",
 es_content: "El Poder del Evangelio es La Cruz de Jesucristo. La “magia” de La Cruz es que DIOS nos amó tan incondicional y tan profundamente que no se ahorró ni a Sí mismo ni a nosotros el dolor y la agonía necesarios para brindarnos una liberación completa del poder, la pena y, lo más importante, el amor y la necesidad del pecado.",
 fr_title: "Citation : La Croix",
 fr_content: "La puissance de l'Évangile est la Croix de Jésus-Christ. La « magie » de la Croix est que DIEU nous a aimés si inconditionnellement et si profondément qu’il ne s’est épargné ni lui-même ni nous-mêmes la douleur et l’agonie nécessaires pour nous délivrer complètement du pouvoir, du châtiment et, plus important encore, de l’amour et du besoin du péché.",
 hi_title: "उद्धरण: क्रॉस",
 hi_content: "सुसमाचार की शक्ति यीशु मसीह का क्रूस है। क्रॉस का \"जादू\" यह है कि भगवान ने हमें इतनी बिना शर्त और इतनी गहराई से प्यार किया कि उन्होंने न तो खुद को और न ही हमें शक्ति, दंड और - सबसे महत्वपूर्ण - प्यार और पाप की आवश्यकता से पूर्ण मुक्ति प्रदान करने के लिए आवश्यक दर्द और पीड़ा से बचाया।",
 zh_title: "yǐn yòng ：shí zì jià",
 zh_content: "fú yīn de lì liàng jiù shì yē sū jī dū de shí zì jià 。 shí zì jià de “ mó lì ” zài yú ， shén rú cǐ wú tiáo jiàn 、 rú cǐ shēn qiè dì ài wǒ men ， yǐ zhì yú tā zì jǐ hé wǒ men dōu méi yǒu miǎn zāo bì yào de tòng kǔ hé tòng kǔ ， shǐ wǒ men néng gòu wán quán bǎi tuō zuì de quán shì 、 xíng fá ， yǐ jí zuì zhòng yào de —— duì zuì de xǐ ài hé xū yào 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE CROSS"})
MATCH (c:CONTENT {name: "content.THE CROSS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE CROSS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE GOSPEL"})
MATCH (child:QUOTE {name: "quote.THE CROSS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GOSPEL->THE CROSS"}]->(child);
```