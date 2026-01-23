---
name: "thought.CHANGING THE HEART"
alias: "Thought: Changing The Heart"
type: THOUGHT
en_content: "Proverbs 21:1; Matthew 19:25, 26. God has--and uses--the ability to change the heart's intent...otherwise no one would be saved."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- salvation
- heart
- transformation
- providence
level: 2
neo4j: false
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2011a)
CREATE (t:THOUGHT {
    name: "thought.CHANGING THE HEART",
    alias: "Thought: Changing The Heart",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'salvation', 'heart', 'transformation', 'providence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.CHANGING THE HEART",
    en_title: "Changing The Heart",
    en_content: "Proverbs 21:1; Matthew 19:25, 26. God has--and uses--the ability to change the heart's intent...otherwise no one would be saved.",
    es_title: "Cambiar el Corazón",
    es_content: "Proverbios 21:1; Mateo 19:25, 26. Dios tiene--y usa--la habilidad de cambiar la intención del corazón... de lo contrario, nadie sería salvo.",
    fr_title: "Changer le Cœur",
    fr_content: "Proverbes 21:1 ; Matthieu 19:25, 26. Dieu a--et utilise--la capacité de changer l'intention du cœur... sinon personne ne serait sauvé.",
    hi_title: "हृदय को बदलना",
    hi_content: "नीतिवचन 21:1; मत्ती 19:25, 26. परमेश्वर के पास हृदय के इरादे को बदलने की क्षमता है--और वह इसका उपयोग करता है... अन्यथा कोई भी बचाया नहीं जाएगा।",
    zh_title: "Gǎibiàn Xīn Yì",
    zh_content: "Zhēnyán 21:1; Mǎtài 19:25, 26. Shàngdì yǒu--bìngqiě shǐyòng--gǎibiàn xīn yì de nénglì... Fǒuzé méiyǒu rén huì dédào zhěngjiù."
});

MATCH (t:THOUGHT {name: "thought.CHANGING THE HEART"})
MATCH (c:CONTENT {name: "content.CHANGING THE HEART"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHANGING THE HEART" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.CHANGING THE HEART"})
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY->CHANGING THE HEART" }]->(child);
```
