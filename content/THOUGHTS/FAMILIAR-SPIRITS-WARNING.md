---
name: "passage.FAMILIAR SPIRITS WARNING"
alias: "Passage: Familiar Spirits Warning"
type: PASSAGE
en_content: "Do not turn to mediums or spiritists; do not seek them out to be defiled by them. I am the Lord your God."
parent: "topic.EVIL"
tags:
- occult
- spirits
- evil
- law
- bible
level: 4
neo4j: true
ptopic: "[[topic-EVIL]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Sep-2011)
CREATE (t:PASSAGE {
    name: "passage.FAMILIAR SPIRITS WARNING",
    alias: "Passages: Familiar Spirits Warning",
    parent: "topic.EVIL",
    tags: ['occult', 'spirits', 'evil', 'law', 'bible'],
    source: "Leviticus 19:31",
    sortedsource: "Leviticus 19:31",
    biblelink: "(https://www.biblegateway.com/passage/?search=Leviticus+19%3A31&version=NASB)",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAMILIAR SPIRITS WARNING",
    en_title: "Familiar Spirits Warning",
    en_content: "Do not turn to mediums or spiritists; do not seek them out to be defiled by them. I am the Lord your God.",
    es_title: "Advertencia sobre los espíritus familiares",
    es_content: "Advertencia sobre los espíritus familiares:
No recurran a médiums ni a espiritistas; no los busquen para no contaminarse con ellos. Yo soy el Señor su Dios.",
    fr_title: "Avertissement concernant les esprits familiers",
    fr_content: "Avertissement concernant les esprits familiers
Ne vous tournez pas vers les médiums ni les spirites ; ne les consultez pas, de peur d'être souillés par eux. Je suis l'Éternel, votre Dieu.",
    hi_title: "परिचित आत्माओं से चेतावनी",
    hi_content: "माध्यमों या आत्माओं से बात करने वालों के पास न जाएं; उनसे अपवित्र होने के लिए उन्हें न ढूंढें। मैं तुम्हारा परमेश्वर यहोवा हूँ।",
    zh_title: "Jǐngtì xié líng",
    zh_content: "bù yāo qiúzhù yú líng méi huò zhāohún shùshì; bùyào xúnqiú tāmen de bāngzhù, yǐmiǎn bèi tāmen diànwū. Wǒ shì yēhéhuá nǐ de shén."
});

MATCH (t:PASSAGE {name: "passage.FAMILIAR SPIRITS WARNING"})
MATCH (c:CONTENT {name: "content.FAMILIAR SPIRITS WARNING"})
MERGE (t)-[:HAS_CONTENT { "name": "p.edge.FAMILIAR SPIRITS WARNING" }]->(c);

MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.FAMILIAR SPIRITS WARNING"})
MERGE (parent)-[:HAS_PASSAGE { "name": "p.edge.EVIL->FAMILIAR SPIRITS WARNING" }]->(child);
```
