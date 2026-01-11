---
name: "thought.DEATH_VS_DEATH"
alias: "Thought: DEATH VS DEATH"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- death
- destroy
- idea
- god
- eternallife
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DEATH_VS_DEATH",
    alias: "Thought: DEATH VS DEATH",
    parent: "topic.THE-GOSPEL",
    tags: ["death", "destroy", "idea", "god", "eternallife"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEATH_VS_DEATH",
    en_title: "DEATH VS DEATH",
    en_content: "Only GOD could come up with the idea of using death to destroy death!!!",
    es_title: "MUERTE CONTRA MUERTE",
    es_content: "¡¡¡Sólo a DIOS se le ocurrió la idea de usar la muerte para destruir la muerte!!!",
    fr_title: "MORT CONTRE MORT",
    fr_content: "Seul DIEU pouvait avoir l'idée d'utiliser la mort pour détruire la mort !!!",
    hi_title: "मृत्यु बनाम मृत्यु",
    hi_content: "केवल भगवान ही मृत्यु को नष्ट करने के लिए मृत्यु का उपयोग करने का विचार लेकर आ सकते हैं!!!",
    zh_title: "sǐ wáng yǔ sǐ wáng",
    zh_content: "zhǐ yǒu shàng dì cái néng xiǎng chū yòng sǐ wáng lái huǐ miè sǐ wáng de zhǔ yì ！！！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEATH_VS_DEATH" AND c.name = "content.DEATH_VS_DEATH"
MERGE (t)-[:HAS_CONTENT {name: "edge.DEATH_VS_DEATH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.DEATH_VS_DEATH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->DEATH_VS_DEATH"}]->(child);
```
