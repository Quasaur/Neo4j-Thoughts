---
name: "thought.BAG OF CHEMICALS DUPED"
alias: "Thought: Bag Of Chemicals Duped"
type: THOUGHT
en_content: "It's hard to fathom that people can be duped into thinking they're nothing more than a bag of chemicals and electricity."
parent: "topic.HUMANITY"
tags:
- humanity
- chemistry
- deception
- spirit
- science
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013c)
CREATE (t:THOUGHT {
    name: "thought.BAG OF CHEMICALS DUPED",
    alias: "Thought: Bag Of Chemicals Duped",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'chemistry', 'deception', 'spirit', 'science'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BAG OF CHEMICALS DUPED",
    en_title: "Bag Of Chemicals Duped",
    en_content: "It's hard to fathom that people can be duped into thinking they're nothing more than a bag of chemicals and electricity.",
    es_title: "Engañados como Bolsa de Químicos",
    es_content: "Es difícil comprender que las personas puedan ser engañadas para pensar que no son más que una bolsa de químicos y electricidad.",
    fr_title: "Dupés en Sac de Produits Chimiques",
    fr_content: "Il est difficile de comprendre que les gens puissent être dupés en pensant qu'ils ne sont rien de plus qu'un sac de produits chimiques et d'électricité.",
    hi_title: "रसायनों के थैले के रूप में धोखा",
    hi_content: "यह समझना मुश्किल है कि लोगों को यह सोचने के लिए धोखा दिया जा सकता है कि वे रसायनों और बिजली के एक थैले से अधिक कुछ नहीं हैं।",
    zh_title: "Bèi piàn wéi huàxué dàizi 被骗为化学袋子",
    zh_content: "Hěn nán xiǎngxiàng rénmen huì bèi piàn qù rènwéi tāmen zhǐshì yīgè zhuāng mǎn huàxué wùzhì hé diànlì de dàizi. 很难想象人们会被骗去认为他们只是一个装满化学物质和电力的袋子。"
});

MATCH (t:THOUGHT {name: "thought.BAG OF CHEMICALS DUPED"})
MATCH (c:CONTENT {name: "content.BAG OF CHEMICALS DUPED"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BAG OF CHEMICALS DUPED" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.BAG OF CHEMICALS DUPED"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->BAG OF CHEMICALS DUPED" }]->(child);
```
