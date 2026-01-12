---
name: "thought.LETTING GO"
alias: "Thought: Unlearning"
type: THOUGHT
en_content: "One of the hardest things in life to do is to let go of what you Think you know."
parent: "topic.UNDERSTANDING"
tags:
- unlearning
- humility
- wisdom
- truth
- change
level: 3
neo4j: true
ptopic: 
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LETTING GO",
    alias: "Thought: Unlearning",
    parent: "topic.UNDERSTANDING",
    tags: ["unlearning", "humility", "wisdom", "truth", "change"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LETTING GO",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LETTING GO" AND c.name = "content.LETTING GO"
MERGE (t)-[:HAS_CONTENT {name: "edge.LETTING GO"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "thought.LETTING GO"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.UNDERSTANDING >LETTING GO"}]->(child);
```
