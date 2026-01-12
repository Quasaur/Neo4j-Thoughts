---
name: "thought.BORN FOR SERMON"
alias: "Thought: Born For Sermon"
type: THOUGHT
en_content: "Christmas sermon at the Pittsburgh prison was well-received...this is what I was born to do!"
parent: "topic.SPIRITUALITY"
tags:
- calling
- ministry
- prison
- sermon
- purpose
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Dec-2010)
CREATE (t:THOUGHT {
    name: "thought.BORN FOR SERMON",
    alias: "Thought: Born For Sermon",
    parent: "topic.SPIRITUALITY",
    tags: ['calling', 'ministry', 'prison', 'sermon', 'purpose'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BORN FOR SERMON",
    en_title: "Born For Sermon",
    en_content: "Christmas sermon at the Pittsburgh prison was well-received...this is what I was born to do!",
    es_title: "Nacido para Predicar",
    es_content: "El sermón de Navidad en la prisión de Pittsburgh fue bien recibido... ¡esto es para lo que nací!",
    fr_title: "Né pour Prêcher",
    fr_content: "Le sermon de Noël à la prison de Pittsburgh a été bien reçu... c'est pour cela que je suis né !",
    hi_title: "उपदेश के लिए जन्मा",
    hi_content: "पिट्सबर्ग जेल में क्रिसमस उपदेश को अच्छी तरह से सराहा गया... मैं इसी के लिए पैदा हुआ था!",
    zh_title: "Wèi bùdào ér shēng 为布道而生",
    zh_content: "Zài Pǐcíbǎo jiānyù de Shèngdànjié bùdào hěn shòu huānyíng... zhè jiùshì wǒ chūshēng de mùdì! 在匹兹堡监狱的圣诞节布道很受欢迎...这就是我出生的目的！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BORN FOR SERMON" AND c.name = "content.BORN FOR SERMON"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BORN FOR SERMON" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.BORN FOR SERMON"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >BORN FOR SERMON" }]->(child);
```
