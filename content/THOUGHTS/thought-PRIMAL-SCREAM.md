---
type: THOUGHT
name: "thought.PRIMAL SCREAM"
alias: "Thought: Primal Scream"
parent: "topic.HUMOR"
en_content: "I believe in the Primal Scream."
tags: ["painting", "expression", "humor", "comedy", "faith"]
ptopic: "[[topic-HUMOR]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PRIMAL SCREAM",
    alias: "Thought: Primal Scream",
    parent: "topic.HUMOR",
    tags: ["painting", "expression", "humor", "comedy", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIMAL SCREAM",
    ctype: "THOUGHT",
    en_title: "Primal Scream",
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
WHERE t.name = "thought.PRIMAL SCREAM" AND c.name = "content.PRIMAL SCREAM"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.PRIMAL SCREAM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMOR" AND child.name = "thought.PRIMAL SCREAM"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HUMOR->PRIMAL SCREAM"}]->(child);
```
