---
name: "thought.HIDING IN PRAYER"
alias: "Thought: Hiding In Prayer"
type: THOUGHT
en_content: "Prayer is where I hide from the world."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- world
- hiding
- spirituality
- presence
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013e)
CREATE (t:THOUGHT {
    name: "thought.HIDING IN PRAYER",
    alias: "Thought: Hiding In Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'world', 'hiding', 'spirituality', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HIDING IN PRAYER",
    en_title: "Hiding In Prayer",
    en_content: "Prayer is where I hide from the world.",
    es_title: "Refugiándose en la Oración",
    es_content: "La oración es donde me refugio del mundo.",
    fr_title: "Se Cacher dans la Prière",
    fr_content: "La prière est l'endroit où je me cache du monde.",
    hi_title: "प्रार्थना में छुपना",
    hi_content: "प्रार्थना वह स्थान है जहाँ मैं संसार से छुपता हूँ।",
    zh_title: "Zài Qídǎo Zhōng Yǐncáng",
    zh_content: "Qídǎo shì wǒ cóng shìjiè zhōng yǐncáng de dìfāng."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HIDING IN PRAYER" AND c.name = "content.HIDING IN PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HIDING IN PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HIDING IN PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HIDING IN PRAYER" }]->(child);
```
