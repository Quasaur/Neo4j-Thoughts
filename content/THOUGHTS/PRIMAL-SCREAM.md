---
name: "thought.PRIMAL_SCREAM"
alias: "Thought: PRIMAL SCREAM"
type: THOUGHT
parent: topic.HUMOR
tags:
- painting
- expression
- humor
- comedy
- faith
neo4j: true
ptopic: "[[topic-HUMOR]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PRIMAL_SCREAM",
    alias: "Thought: PRIMAL SCREAM",
    parent: "topic.HUMOR",
    tags: ["painting", "expression", "humor", "comedy", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIMAL_SCREAM",
    en_title: "PRIMAL SCREAM",
    en_content: "I believe in the Primal Scream.",
    es_title: "GRITO PRIMARIO",
    es_content: "Creo en el Grito Primordial.",
    fr_title: "CRI PRIMAL",
    fr_content: "Je crois au Primal Scream.",
    hi_title: "प्रारंभिक चीख",
    hi_content: "मैं प्राइमल स्क्रीम में विश्वास करता हूं।",
    zh_title: "yuán shǐ jiān jiào",
    zh_content: "wǒ xiāng xìn yuán shǐ jiān jiào 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRIMAL_SCREAM" AND c.name = "content.PRIMAL_SCREAM"
MERGE (t)-[:HAS_CONTENT {name: "edge.PRIMAL_SCREAM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMOR" AND child.name = "thought.PRIMAL_SCREAM"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HUMOR->PRIMAL_SCREAM"}]->(child);
```
