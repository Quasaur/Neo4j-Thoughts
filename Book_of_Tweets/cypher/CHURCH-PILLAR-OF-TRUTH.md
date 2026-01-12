---
name: "thought.CHURCH PILLAR OF TRUTH"
alias: "Thought: Church Pillar Of Truth"
type: THOUGHT
en_content: "1 Tim. 3:15: The Church of God is the Pillar and Ground of the Truth on Earth, and to attack and criticize her is perilous."
parent: "topic.RELIGION"
tags:
- church
- truth
- pillar
- bible
- religion
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.CHURCH PILLAR OF TRUTH",
    alias: "Thought: Church Pillar Of Truth",
    parent: "topic.RELIGION",
    tags: ['church', 'truth', 'pillar', 'bible', 'religion'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHURCH PILLAR OF TRUTH",
    en_title: "Church Pillar Of Truth",
    en_content: "1 Tim. 3:15: The Church of God is the Pillar and Ground of the Truth on Earth, and to attack and criticize her is perilous.",
    es_title: "La Iglesia: Columna de la Verdad",
    es_content: "1 Tim. 3:15: La Iglesia de Dios es la Columna y Fundamento de la Verdad en la Tierra, y atacarla y criticarla es peligroso.",
    fr_title: "L'Église : Pilier de la Vérité",
    fr_content: "1 Tim. 3:15 : L'Église de Dieu est le Pilier et le Fondement de la Vérité sur Terre, et l'attaquer et la critiquer est périlleux.",
    hi_title: "चर्च: सत्य का स्तंभ",
    hi_content: "1 तीमुथियुस 3:15: परमेश्वर का चर्च पृथ्वी पर सत्य का स्तंभ और आधार है, और उस पर हमला करना और उसकी आलोचना करना खतरनाक है।",
    zh_title: "Jiàohuì: Zhēnlǐ de zhùzi 教会：真理的柱子",
    zh_content: "Tí mó tài qián shū 3:15: Shàngdì de jiàohuì shì dìshàng zhēnlǐ de zhùzi hé gēnjī, gōngjí hé pīpíng tā shì wéixiǎn de. 提摩太前书3:15：上帝的教会是地上真理的柱子和根基，攻击和批评她是危险的。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CHURCH PILLAR OF TRUTH" AND c.name = "content.CHURCH PILLAR OF TRUTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHURCH PILLAR OF TRUTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.CHURCH PILLAR OF TRUTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHURCH PILLAR OF TRUTH" }]->(child);
```
