---
name: "thought.REASON TO BE ALIVE"
alias: "Thought: Reason To Be Alive"
type: THOUGHT
en_content: "The only reason we are alive is to find Jesus that He may take away our sin."
parent: "topic.SPIRITUALITY"
tags:
- jesus
- life
- purpose
- sin
- spirituality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013c)
CREATE (t:THOUGHT {
    name: "thought.REASON TO BE ALIVE",
    alias: "Thought: Reason To Be Alive",
    parent: "topic.SPIRITUALITY",
    tags: ['jesus', 'life', 'purpose', 'sin', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.REASON TO BE ALIVE",
    en_title: "Reason To Be Alive",
    en_content: "The only reason we are alive is to find Jesus that He may take away our sin.",
    es_title: "Razón Para Estar Vivos",
    es_content: "La única razón por la que estamos vivos es encontrar a Jesús para que Él pueda quitar nuestro pecado.",
    fr_title: "Raison d'Être Vivant",
    fr_content: "La seule raison pour laquelle nous sommes vivants est de trouver Jésus afin qu'Il puisse enlever notre péché.",
    hi_title: "जीवित रहने का कारण",
    hi_content: "हमारे जीवित रहने का एकमात्र कारण यीशु को खोजना है ताकि वह हमारे पाप को दूर कर सकें।",
    zh_title: "Huózhe de Lǐyóu",
    zh_content: "Wǒmen huózhe de wéiyī lǐyóu jiùshì zhǎodào Yēsū, shǐ Tā néng chúqù wǒmen de zuì."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REASON TO BE ALIVE" AND c.name = "content.REASON TO BE ALIVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REASON TO BE ALIVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.REASON TO BE ALIVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >REASON TO BE ALIVE" }]->(child);
```
