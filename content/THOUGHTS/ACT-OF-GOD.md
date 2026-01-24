---
name: "thought.ACT_OF_GOD"
alias: "Thought: Act of God"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- person
- people
- wife
- husband
- imageofgod
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ACT_OF_GOD",
    alias: "Thought: Act of God",
    parent: "topic.PSYCHOLOGY",
    tags: ["person", "people", "wife", "husband", "imageofgod"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ACT_OF_GOD",
    en_title: "Act of God",
    en_content: "If every person is an Act of God, what can my wife teach me about God?",
    es_title: "Caso de fuerza mayor",
    es_content: "Si cada persona es un acto de Dios, ¿qué puede enseñarme mi esposa sobre Dios?",
    fr_title: "Acte de Dieu",
    fr_content: "Si chaque personne est un acte de Dieu, que peut m’apprendre ma femme sur Dieu ?",
    hi_title: "दैवीय घटना",
    hi_content: "यदि प्रत्येक व्यक्ति ईश्वर का कार्य है, तो मेरी पत्नी मुझे ईश्वर के बारे में क्या सिखा सकती है?",
    zh_title: "tiān zāi",
    zh_content: "rú guǒ měi gè rén dōu shì shàng dì de zuò wéi ， wǒ de qī zǐ néng jiào wǒ shén me guān yú shàng dì de shì ？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACT_OF_GOD" AND c.name = "content.ACT_OF_GOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.ACT_OF_GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.ACT_OF_GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->ACT_OF_GOD"}]->(child);
```
