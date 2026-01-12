---
name: "thought.POWER AND WILL"
alias: "Thought: Power And Will"
type: THOUGHT
en_content: "We don't tap into God's Strength because we are not committed to executing God's Will."
parent: "topic.SPIRITUALITY"
tags:
- strength
- will
- commitment
- spirituality
- power
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2010)
CREATE (t:THOUGHT {
    name: "thought.POWER AND WILL",
    alias: "Thought: Power And Will",
    parent: "topic.SPIRITUALITY",
    tags: ['strength', 'will', 'commitment', 'spirituality', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.POWER AND WILL",
    en_title: "Power And Will",
    en_content: "We don't tap into God's Strength because we are not committed to executing God's Will.",
    es_title: "Poder y voluntad",
    es_content: "No aprovechamos la Fuerza de Dios porque no estamos comprometidos a ejecutar la Voluntad de Dios.",
    fr_title: "Pouvoir et volonté",
    fr_content: "Nous ne puisons pas dans la Force de Dieu parce que nous ne sommes pas déterminés à exécuter la Volonté de Dieu.",
    hi_title: "शक्ति और इच्छा",
    hi_content: "हम ईश्वर की शक्ति का लाभ नहीं उठाते क्योंकि हम ईश्वर की इच्छा को क्रियान्वित करने के लिए प्रतिबद्ध नहीं हैं।",
    zh_title: "力量与意志",
    zh_content: "我们没有利用神的力量，因为我们没有致力于执行神的旨意。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.POWER AND WILL" AND c.name = "content.POWER AND WILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.POWER AND WILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.POWER AND WILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >POWER AND WILL" }]->(child);
```
