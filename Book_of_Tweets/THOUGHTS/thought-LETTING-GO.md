---
type: THOUGHT
name: "thought.LETTING GO"
alias: "Thought: Unlearning"
parent: "topic.UNDERSTANDING"
en_content: "One of the hardest things in life to do is to let go of what you Think you know."
tags: ["unlearning", "humility", "wisdom", "truth", "change"]
ptopic:
level: 3
neo4j: false
---

```Cypher
CREATE (t:THOUGHT {    name: "thought.LETTING GO",
    alias: "Thought: Unlearning",
    parent: "topic.UNDERSTANDING",
    tags: ["unlearning", "humility", "wisdom", "truth", "change"],
    level: 3});

CREATE (c:CONTENT {
    name: "content.LETTING GO",
    ctype: "THOUGHT",
    en_title: "Letting Go",
    en_content: "One of the hardest things in life to do is to let go of what you Think you know.",
    es_title: "Soltando ideas",
    es_content: "Una de las cosas más difíciles de hacer en la vida es soltar lo que Crees que sabes.",
    fr_title: "Lâcher prise",
    fr_content: "L'une des choses les plus difficiles à faire dans la vie est de lâcher ce que vous PENSEZ savoir.",
    hi_title: "jaane dena",
    hi_content: "जीवन में सबसे कठिन कामों में से एक है उसे छोड़ना जो आप सोचते हैं कि आप जानते हैं।",
    zh_title: "fàng shǒu",
    zh_content: "shēng huó zhōng zuì nán zuò dì shì zhī yī jiù shì fàng xià nǐ yǐ wéi nǐ zhī dào de dōng xī."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LETTING GO"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.UNDERSTANDING->LETTING GO"
RETURN t, parent;
```
