---
name: "thought.WAY OF EMPIRES"
alias: "Thought: Way Of Empires"
type: THOUGHT
en_content: "We are going the way of the Roman Empire and the Soviet Union."
parent: "topic.HUMANITY"
tags:
- history
- humanity
- fall
- society
- judgment
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.WAY OF EMPIRES",
    alias: "Thought: Way Of Empires",
    parent: "topic.HUMANITY",
    tags: ['history', 'humanity', 'fall', 'society', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WAY OF EMPIRES",
    en_title: "Way Of Empires",
    en_content: "We are going the way of the Roman Empire and the Soviet Union.",
    es_title: "Camino de los Imperios",
    es_content: "Vamos por el camino del Imperio Romano y la Unión Soviética.",
    fr_title: "Voie des Empires",
    fr_content: "Nous suivons la voie de l'Empire romain et de l'Union soviétique.",
    hi_title: "साम्राज्यों का मार्ग",
    hi_content: "हम रोमन साम्राज्य और सोवियत संघ के मार्ग पर चल रहे हैं।",
    zh_title: "Diguo zhi Lu",
    zh_content: "Women zhengzai zou Luoma Diguo he Sulian de daolu."
});

MATCH (t:THOUGHT {name: "thought.WAY OF EMPIRES"})
MATCH (c:CONTENT {name: "content.WAY OF EMPIRES"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.WAY OF EMPIRES" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.WAY OF EMPIRES"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >WAY OF EMPIRES" }]->(child);
```
