---
name: "thought.LIFE IN PRAYER"
alias: "Thought: Life In Prayer"
type: THOUGHT
en_content: "There is no life outside of Prayer."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- life
- spirituality
- essence
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Feb-2014)
CREATE (t:THOUGHT {
    name: "thought.LIFE IN PRAYER",
    alias: "Thought: Life In Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'life', 'spirituality', 'essence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIFE IN PRAYER",
    en_title: "Life In Prayer",
    en_content: "There is no life outside of Prayer.",
    es_title: "Vida en Oración",
    es_content: "No hay vida fuera de la Oración.",
    fr_title: "Vie dans la Prière",
    fr_content: "Il n'y a pas de vie en dehors de la Prière.",
    hi_title: "प्रार्थना में जीवन",
    hi_content: "प्रार्थना के बाहर कोई जीवन नहीं है।",
    zh_title: "Qídǎo zhōng de Shēngmìng",
    zh_content: "Méiyǒu qídǎo jiù méiyǒu shēngmìng."
});

MATCH (t:THOUGHT {name: "thought.LIFE IN PRAYER"})
MATCH (c:CONTENT {name: "content.LIFE IN PRAYER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIFE IN PRAYER" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.LIFE IN PRAYER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >LIFE IN PRAYER" }]->(child);
```
