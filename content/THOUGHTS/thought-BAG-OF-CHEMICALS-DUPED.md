---
type: THOUGHT
name: "thought.BAG OF CHEMICALS DUPED"
alias: "Thought: Bag Of Chemicals Duped"
parent: "topic.HUMANITY"
en_content: "It's hard to fathom that people can be duped into thinking they're nothing more than a bag of chemicals and electricity."
tags: ["humanity", "chemistry", "deception", "spirit", "science"]
ptopic: "[[topic-HUMANITY]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.BAG OF CHEMICALS DUPED",
    alias: "Thought: Bag Of Chemicals Duped",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'chemistry', 'deception', 'spirit', 'science'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BAG OF CHEMICALS DUPED",
    ctype: "THOUGHT",
    en_title: "Bag Of Chemicals Duped",
    en_content: "It's hard to fathom that people can be duped into thinking they're nothing more than a bag of chemicals and electricity.",
    es_title: "Engañados como Bolsa de Químicos",
    es_content: "Es difícil comprender que las personas puedan ser engañadas para pensar que no son más que una bolsa de químicos y electricidad.",
    fr_title: "Dupés en Sac de Produits Chimiques",
    fr_content: "Il est difficile de comprendre que les gens puissent être dupés en pensant qu'ils ne sont rien de plus qu'un sac de produits chimiques et d'électricité.",
    hi_title: "रसायनों के थैले के रूप में धोखा",
    hi_content: "यह समझना मुश्किल है कि लोगों को यह सोचने के लिए धोखा दिया जा सकता है कि वे रसायनों और बिजली के एक थैले से अधिक कुछ नहीं हैं।",
    zh_title: "Bèi piàn wéi huàxué dàizi  bèi piàn wèi huà xué dài zi",
    zh_content: "Hěn nán xiǎngxiàng rénmen huì bèi piàn qù rènwéi tāmen zhǐshì yīgè zhuāng mǎn huàxué wùzhì hé diànlì de dàizi.  hěn nán xiǎng xiàng rén men huì bèi piàn qù rèn wéi tā men zhǐ shì yí gè zhuāng mǎn huà xué wù zhì hé diàn lì de dài zi 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BAG OF CHEMICALS DUPED"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->BAG OF CHEMICALS DUPED"
RETURN t, parent;
```
