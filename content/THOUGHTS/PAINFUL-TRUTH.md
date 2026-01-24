---
name: "thought.PAINFUL_TRUTH"
alias: "Thought: PAINFUL TRUTH"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- tedx
- russellellis
- whitesupremacy
- change
- faith
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PAINFUL_TRUTH",
    alias: "Thought: PAINFUL TRUTH",
    parent: "topic.PSYCHOLOGY",
    tags: ["tedx", "russellellis", "whitesupremacy", "change", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PAINFUL_TRUTH",
    en_title: "PAINFUL TRUTH",
    en_content: "Perhaps the Truth only hurts when we refuse to submit to It.",
    es_title: "VERDAD DOLOROSA",
    es_content: "Quizás la Verdad sólo duele cuando nos negamos a someternos a Ella.",
    fr_title: "VÉRITÉ DOULOUREUSE",
    fr_content: "Peut-être que la Vérité ne fait mal que lorsque nous refusons de nous y soumettre.",
    hi_title: "दर्दनाक सच",
    hi_content: "शायद सत्य केवल तभी दुख पहुंचाता है जब हम उसके प्रति समर्पित होने से इनकार करते हैं।",
    zh_title: "tòng kǔ de zhēn xiàng",
    zh_content: "yě xǔ zhǐ yǒu dāng wǒ men jù jué fú cóng zhēn lǐ shí ， tā cái huì dài lái shāng hài 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PAINFUL_TRUTH" AND c.name = "content.PAINFUL_TRUTH"
MERGE (t)-[:HAS_CONTENT {name: "edge.PAINFUL_TRUTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.PAINFUL_TRUTH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->PAINFUL_TRUTH"}]->(child);
```
