---
name: "thought.HUMAN_LIFE"
alias: "Thought: HUMAN LIFE"
type: THOUGHT
parent: topic.WORSHIP
tags:
- humanity
- godhead
- intelligent
- life
- purpose
neo4j: true
ptopic: "[[topic-WORSHIP]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMAN_LIFE",
    alias: "Thought: HUMAN LIFE",
    parent: "topic.WORSHIP",
    tags: ["humanity", "godhead", "intelligent", "life", "purpose"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMAN_LIFE",
    en_title: "HUMAN LIFE",
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
WHERE t.name = "thought.HUMAN_LIFE" AND c.name = "content.HUMAN_LIFE"
MERGE (t)-[:HAS_CONTENT {name: "edge.HUMAN_LIFE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WORSHIP" AND child.name = "thought.HUMAN_LIFE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.WORSHIP->HUMAN_LIFE"}]->(child);
```
