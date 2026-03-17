---
type: PASSAGE
name: "passage.FAMILIAR SPIRITS WARNING"
alias: "Passage: Familiar Spirits Warning"
parent: "topic.EVIL"
sortedsource: "Leviticus 19:31"
en_content: "Do not turn to mediums or spiritists; do not seek them out to be defiled by them. I am the Lord your God."
tags: ["occult", "spirits", "evil", "law", "bible"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 't' and 'c' as variables to keep them in memory
CREATE (t:PASSAGE {
    name: "passage.FAMILIAR SPIRITS WARNING",
    parent: "topic.EVIL",
    alias: "Passage: Familiar Spirits Warning",
    tags: ["occult", "spirits", "evil", "law", "bible"],
	source: "Leviticus 19:31",
    sortedsource: "Leviticus 19:31",
    biblelink: "[https://www.biblegateway.com/passage/?search=Proverbs+3%3A3-4&version=NASB](https://www.biblegateway.com/passage/?search=Leviticus%2019%3A31&version=NASB)",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.FAMILIAR SPIRITS WARNING",
    ctype: "PASSAGE",
    en_title: "Passage: Familiar Spirits Warning",
    en_content: "Do not turn to mediums or spiritists; do not seek them out to be defiled by them. I am the Lord your God.",
    es_title: "Pasaje: Advertencia de espíritus familiares",
    es_content: "Advertencia sobre los espíritus familiares: No recurran a médiums ni a espiritistas; no los busquen para no contaminarse con ellos. Yo soy el Señor su Dios.",
    fr_title: "Passage : Avertissement des esprits familiers",
    fr_content: "Avertissement concernant les esprits familiers ; Ne vous tournez pas vers les médiums ni les spirites ; ne les consultez pas, de peur d'être souillés par eux. Je suis l'Éternel, votre Dieu.",
    hi_title: "परिच्छेद: परिचित आत्माओं की चेतावनी",
    hi_content: "माध्यमों या आत्माओं से बात करने वालों के पास न जाएं; उनसे अपवित्र होने के लिए उन्हें न ढूंढें। मैं तुम्हारा परमेश्वर यहोवा हूँ।",
    zh_title: "duàn luò : shú xī de líng hún jǐng gào",
    zh_content: "bù yāo qiúzhù yú líng méi huò zhāohún shùshì; bùyào xúnqiú tāmen de bāngzhù, yǐmiǎn bèi tāmen diànwū. Wǒ shì yēhéhuá nǐ de shén."
})

// 2. Link Content to Passage using the variables 't' and 'c'
MERGE (t)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.FAMILIAR SPIRITS WARNING"

// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_PASSAGE]->(t)
ON CREATE SET r2.name = "p.edge.EVIL->FAMILIAR SPIRITS WARNING"
RETURN t, parent;
```
