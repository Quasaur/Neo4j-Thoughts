---
name: "thought.NOT BEING GOD"
alias: "Thought: Not Being God"
type: THOUGHT
en_content: "I am not God; and I'm so glad that I don't have to be!"
parent: "topic.HUMANITY"
tags:
- humility
- humanity
- god
- identity
- joy
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.NOT BEING GOD",
    alias: "Thought: Not Being God",
    parent: "topic.HUMANITY",
    tags: ['humility', 'humanity', 'god', 'identity', 'joy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOT BEING GOD",
    en_title: "Not Being God",
    en_content: "I am not God; and I'm so glad that I don't have to be!",
    es_title: "No Ser Dios",
    es_content: "¡Yo no soy Dios; y estoy tan agradecido de no tener que serlo!",
    fr_title: "Ne Pas Être Dieu",
    fr_content: "Je ne suis pas Dieu ; et je suis si heureux de ne pas avoir à l'être !",
    hi_title: "ईश्वर न होना",
    hi_content: "मैं ईश्वर नहीं हूं; और मैं बहुत खुश हूं कि मुझे ईश्वर होने की आवश्यकता नहीं है!",
    zh_title: "Bú Shì Shàngdì",
    zh_content: "Wǒ bú shì Shàngdì; wǒ hěn qìngxìng wǒ bú bìxū chéngwéi Shàngdì!"
});

MATCH (t:THOUGHT {name: "thought.NOT BEING GOD"})
MATCH (c:CONTENT {name: "content.NOT BEING GOD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOT BEING GOD" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.NOT BEING GOD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >NOT BEING GOD" }]->(child);
```
