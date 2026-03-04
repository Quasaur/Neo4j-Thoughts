---
type: THOUGHT
name: "thought.SPIRITUAL HEALTH"
alias: "Thought: Spiritual Health"
parent: "topic.SPIRITUALITY"
en_content: "Spiritual Health: Doing what I know pleases God all of the time."
tags: ["health", "spiritual", "god", "allpleasing", "character"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SPIRITUAL HEALTH",
    alias: "Thought: Spiritual Health",
    parent: "topic.SPIRITUALITY",
    tags: ["health", "spiritual", "god", "allpleasing", "character"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPIRITUAL HEALTH",
    ctype: "THOUGHT",
    en_title: "Spiritual Health",
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
WHERE t.name = "thought.SPIRITUAL HEALTH" AND c.name = "content.SPIRITUAL HEALTH"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.SPIRITUAL HEALTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SPIRITUAL HEALTH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITUALITY->SPIRITUAL HEALTH"}]->(child);
```
