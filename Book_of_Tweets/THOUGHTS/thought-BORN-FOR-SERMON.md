---
type: THOUGHT
name: "thought.BORN FOR SERMON"
alias: "Thought: Born For Sermon"
parent: "topic.SPIRITUALITY"
en_content: "Christmas sermon at the Pittsburgh prison was well-received...this is what I was born to do!"
tags: ["calling", "ministry", "prison", "sermon", "purpose"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Dec-2010)
CREATE (t:THOUGHT {    name: "thought.BORN FOR SERMON",
    alias: "Thought: Born For Sermon",
    parent: "topic.SPIRITUALITY",
    tags: ['calling', 'ministry', 'prison', 'sermon', 'purpose'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.BORN FOR SERMON",
    ctype: "THOUGHT",
    en_title: "Born For Sermon",
    en_content: "Christmas sermon at the Pittsburgh prison was well-received...this is what I was born to do!",
    es_title: "Nacido para Predicar",
    es_content: "El sermón de Navidad en la prisión de Pittsburgh fue bien recibido... ¡esto es para lo que nací!",
    fr_title: "Né pour Prêcher",
    fr_content: "Le sermon de Noël à la prison de Pittsburgh a été bien reçu... c'est pour cela que je suis né !",
    hi_title: "उपदेश के लिए जन्मा",
    hi_content: "पिट्सबर्ग जेल में क्रिसमस उपदेश को अच्छी तरह से सराहा गया... मैं इसी के लिए पैदा हुआ था!",
    zh_title: "Wèi bùdào ér shēng  wèi bù dào ér shēng",
    zh_content: "Zài Pǐcíbǎo jiānyù de Shèngdànjié bùdào hěn shòu huānyíng... zhè jiùshì wǒ chūshēng de mùdì!  zài pǐ zī bǎo jiān yù de shèng dàn jié bù dào hěn shòu huān yíng ... zhè jiù shì wǒ chū shēng de mù dì ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BORN FOR SERMON"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->BORN FOR SERMON"
RETURN t, parent;
```
