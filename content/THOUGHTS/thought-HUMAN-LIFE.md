---
type: THOUGHT
name: "thought.HUMAN LIFE"
alias: "Thought: Human Life"
parent: "topic.WORSHIP"
en_content: "The purpose of intelligent human life is to Worship, Obey and Serve The Godhead."
tags: ["humanity", "godhead", "intelligent", "life", "purpose"]
ptopic: "[[topic-WORSHIP]]"
level: 3
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMAN LIFE",
    alias: "Thought: Human Life",
    parent: "topic.WORSHIP",
    tags: ["humanity", "godhead", "intelligent", "life", "purpose"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMAN LIFE",
    ctype: "THOUGHT",
    en_title: "Human Life",
    en_content: "The purpose of intelligent human life is to Worship, Obey and Serve The Godhead.",
    es_title: "VIDA HUMANA",
    es_content: "El propósito de la vida humana inteligente es Adorar, Obedecer y Servir a la Divinidad.",
    fr_title: "VIE HUMAINE",
    fr_content: "Le but de la vie humaine intelligente est d’adorer, d’obéir et de servir la Divinité.",
    hi_title: "मानव जीवन",
    hi_content: "बुद्धिमान मानव जीवन का उद्देश्य भगवान की पूजा, आज्ञापालन और सेवा करना है।",
    zh_title: "rén lèi shēng huó",
    zh_content: "zhì huì rén lèi shēng huó de mù dì shì chóng bài 、 fú cóng hé fú wù shén 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN LIFE" AND c.name = "content.HUMAN LIFE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.HUMAN LIFE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WORSHIP" AND child.name = "thought.HUMAN LIFE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.WORSHIP->HUMAN LIFE"}]->(child);
```
