---
name: "thought.SPIRITUAL_HEALTH"
alias: "Thought: SPIRITUAL HEALTH"
type: THOUGHT
parent: topic.SPIRITUALITY
tags:
- health
- spiritual
- god
- allpleasing
- character
neo4j: true
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SPIRITUAL_HEALTH",
    alias: "Thought: SPIRITUAL HEALTH",
    parent: "topic.SPIRITUALITY",
    tags: ["health", "spiritual", "god", "allpleasing", "character"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPIRITUAL_HEALTH",
    en_title: "SPIRITUAL HEALTH",
    en_content: "Spiritual Health: Doing what I know pleases God all of the time.",
    es_title: "SALUD ESPIRITUAL",
    es_content: "Salud Espiritual: Hacer lo que sé agrada a Dios todo el tiempo.",
    fr_title: "SANTÉ SPIRITUELLE",
    fr_content: "Santé spirituelle : Faire ce que je sais plaît à Dieu à tout moment.",
    hi_title: "आध्यात्मिक स्वास्थ्य",
    hi_content: "आध्यात्मिक स्वास्थ्य: जो मैं जानता हूं उसे करने से ईश्वर हर समय प्रसन्न होता है।",
    zh_title: "jīng shén jiàn kāng",
    zh_content: "jīng shén jiàn kāng ： zuò wǒ suǒ zhī dào de shì zǒng shì lìng shàng dì gāo xìng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SPIRITUAL_HEALTH" AND c.name = "content.SPIRITUAL_HEALTH"
MERGE (t)-[:HAS_CONTENT {name: "edge.SPIRITUAL_HEALTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SPIRITUAL_HEALTH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITUALITY->SPIRITUAL_HEALTH"}]->(child);
```
