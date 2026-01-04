---
name: "thought.LIVING FAITH"
alias: "Thought: Active Belief"
type: THOUGHT
en_content: "Faith is when Divine Truth is caught by your imagination and you begin to live it."
parent: "topic.FAITH"
tags:
- faith
- truth
- imagination
- lifestyle
- action
level: 4
neo4j: true
insert: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LIVING FAITH",
    alias: "Thought: Active Belief",
    parent: "topic.FAITH",
    tags: ["faith", "truth", "imagination", "lifestyle", "action"],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LIVING FAITH",
    en_title: "Living Faith",
    en_content: "Faith is when Divine Truth is caught by your imagination and you begin to live it.",
    es_title: "Fe viva",
    es_content: "La fe es cuando la Verdad Divina es captada por tu imaginación y comienzas a vivirla.",
    fr_title: "Foi vivante",
    fr_content: "La foi, c'est quand la Vérité Divine est saisie par votre imagination et que vous commencez à la vivre.",
    hi_title: "jeevant vishvaas",
    hi_content: "विश्वास तब होता है जब दिव्य सत्य आपकी कल्पना में पकड़ लिया जाता है और आप उसे जीना शुरू कर देते हैं।",
    zh_title: "huó de xìn xīn",
    zh_content: "xìn xīn shì dāng shén shèng de zhēn lǐ bèi nǐ de xiǎng xiàng lì bǎo zhuō bìng qiě nǐ kāi shǐ shí jiàn tā dì shí hòu."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIVING FAITH" AND c.name = "content.LIVING FAITH"
MERGE (t)-[:HAS_CONTENT {name: "edge.LIVING FAITH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.LIVING FAITH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITH >LIVING FAITH"}]->(child);
```
