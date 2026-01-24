---
name: "thought.YOUR_KINGDOM"
alias: "Thought: YOUR KINGDOM"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- kingdom
- heaven
- earth
- destruction
- jesuschrist
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.YOUR_KINGDOM",
    alias: "Thought: YOUR KINGDOM",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["kingdom", "heaven", "earth", "destruction", "jesuschrist"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.YOUR_KINGDOM",
    en_title: "YOUR KINGDOM",
    en_content: "To establish the Kingdom of the Heavens on this Earth, Christ must destroy your kingdom.",
    es_title: "TU REINO",
    es_content: "Para establecer el Reino de los Cielos en esta Tierra, Cristo debe destruir vuestro reino.",
    fr_title: "VOTRE ROYAUME",
    fr_content: "Pour établir le Royaume des Cieux sur cette Terre, le Christ doit détruire votre royaume.",
    hi_title: "आपका साम्राज्य",
    hi_content: "इस पृथ्वी पर स्वर्ग का राज्य स्थापित करने के लिए, मसीह को आपके राज्य को नष्ट करना होगा।",
    zh_title: "nǐ de wáng guó",
    zh_content: "wèi le zài dì qiú shàng jiàn lì tiān guó ， jī dū bì xū cuī huǐ nǐ men de wáng guó 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.YOUR_KINGDOM" AND c.name = "content.YOUR_KINGDOM"
MERGE (t)-[:HAS_CONTENT {name: "edge.YOUR_KINGDOM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.YOUR_KINGDOM"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->YOUR_KINGDOM"}]->(child);
```
