---
type: THOUGHT
name: "thought.PRIDE OF SATAN"
alias: "Thought: Pride Of Satan"
parent: "topic.EVIL"
en_content: "I'm the center of my universe...why can't I be the center of everyone else's? -- The Devil"
tags: ["pride", "devil", "evil", "selfishness", "deception"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PRIDE OF SATAN",
    alias: "Thought: Pride Of Satan",
    parent: "topic.EVIL",
    tags: ['pride', 'devil', 'evil', 'selfishness', 'deception'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIDE OF SATAN",
    ctype: "THOUGHT",
    en_title: "Pride Of Satan",
    en_content: "I'm the center of my universe...why can't I be the center of everyone else's? -- The Devil",
    es_title: "Orgullo de satanás",
    es_content: "«Soy el centro de mi universo... ¿por qué no puedo ser el centro del universo de los demás?» — El Diablo",
    fr_title: "Fierté de Satan",
    fr_content: "« Je suis le centre de mon univers... pourquoi ne serais-je pas le centre de l'univers de tous les autres ? » — Le Diable",
    hi_title: "शैतान का गौरव",
    hi_content: "मैं अपने ब्रह्मांड का केंद्र हूँ...मैं बाकी सबके ब्रह्मांड का केंद्र क्यों नहीं हो सकता? -- शैतान",
    zh_title: "Sādàn de àomàn",
    zh_content: "\\“wǒ shì wǒ yǔzhòu de zhōngxīn……wèishéme wǒ bùnéng chéngwéi qítā suǒyǒu rén de zhōngxīn?”\\——Móguǐ"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRIDE OF SATAN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->PRIDE OF SATAN"
RETURN t, parent;
```
