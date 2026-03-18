---
type: THOUGHT
name: "thought.CHURCH PILLAR OF TRUTH"
alias: "Thought: Church Pillar Of Truth"
parent: "topic.RELIGION"
en_content: "1 Tim. 3:15: The Church of God is the Pillar and Ground of the Truth on Earth, and to attack and criticize her is perilous."
tags: ["church", "truth", "pillar", "bible", "religion"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Feb-2012a)
CREATE (t:THOUGHT {    name: "thought.CHURCH PILLAR OF TRUTH",
    alias: "Thought: Church Pillar Of Truth",
    parent: "topic.RELIGION",
    tags: ['church', 'truth', 'pillar', 'bible', 'religion'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.CHURCH PILLAR OF TRUTH",
    ctype: "THOUGHT",
    en_title: "Church Pillar Of Truth",
    en_content: "1 Tim. 3:15: The Church of God is the Pillar and Ground of the Truth on Earth, and to attack and criticize her is perilous.",
    es_title: "La Iglesia: Columna de la Verdad",
    es_content: "1 Tim. 3:15: La Iglesia de Dios es la Columna y Fundamento de la Verdad en la Tierra, y atacarla y criticarla es peligroso.",
    fr_title: "L'Église : Pilier de la Vérité",
    fr_content: "1 Tim. 3:15 : L'Église de Dieu est le Pilier et le Fondement de la Vérité sur Terre, et l'attaquer et la critiquer est périlleux.",
    hi_title: "चर्च: सत्य का स्तंभ",
    hi_content: "1 तीमुथियुस 3:15: परमेश्वर का चर्च पृथ्वी पर सत्य का स्तंभ और आधार है, और उस पर हमला करना और उसकी आलोचना करना खतरनाक है।",
    zh_title: "Jiàohuì: Zhēnlǐ de zhùzi  jiào huì ： zhēn lǐ de zhù zi",
    zh_content: "Tí mó tài qián shū 3:15: Shàngdì de jiàohuì shì dìshàng zhēnlǐ de zhùzi hé gēnjī, gōngjí hé pīpíng tā shì wéixiǎn de.  tí mó tài qián shū 3:15： shàng dì de jiào huì shì dì shàng zhēn lǐ de zhù zi hé gēn jī ， gōng jī hé pī píng tā shì wēi xiǎn de 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CHURCH PILLAR OF TRUTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->CHURCH PILLAR OF TRUTH"
RETURN t, parent;
```
