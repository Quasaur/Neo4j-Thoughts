---
name: "thought.PRIDE OF SATAN"
alias: "Thought: Pride Of Satan"
type: THOUGHT
en_content: "\"I'm the center of my universe...why can't I be the center of everyone else's?\" -- The Devil"
parent: "topic.EVIL"
tags:
- pride
- devil
- evil
- selfishness
- deception
level: 4
neo4j: false
ptopic: "[[topic-EVIL]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.PRIDE OF SATAN",
    alias: "Thought: Pride Of Satan",
    parent: "topic.EVIL",
    tags: ['pride', 'devil', 'evil', 'selfishness', 'deception'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIDE OF SATAN",
    en_title: "Pride Of Satan",
    en_content: "\"I'm the center of my universe...why can't I be the center of everyone else's?\" -- The Devil",
    es_title: "Orgullo de satanás",
    es_content: "«Soy el centro de mi universo... ¿por qué no puedo ser el centro del universo de los demás?» — El Diablo",
    fr_title: "Fierté de Satan",
    fr_content: "« Je suis le centre de mon univers... pourquoi ne serais-je pas le centre de l'univers de tous les autres ? » — Le Diable",
    hi_title: "शैतान का गौरव",
    hi_content: "\"मैं अपने ब्रह्मांड का केंद्र हूँ...मैं बाकी सबके ब्रह्मांड का केंद्र क्यों नहीं हो सकता?\" -- शैतान",
    zh_title: "Sādàn de àomàn",
    zh_content: "\“wǒ shì wǒ yǔzhòu de zhōngxīn……wèishéme wǒ bùnéng chéngwéi qítā suǒyǒu rén de zhōngxīn?”\——Móguǐ"
});

MATCH (t:THOUGHT {name: "thought.PRIDE OF SATAN"})
MATCH (c:CONTENT {name: "content.PRIDE OF SATAN"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.PRIDE OF SATAN" }]->(c);

MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:THOUGHT {name: "thought.PRIDE OF SATAN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.EVIL->PRIDE OF SATAN" }]->(child);
```
