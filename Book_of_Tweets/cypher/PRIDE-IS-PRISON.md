---
name: "thought.PRIDE IS PRISON"
alias: "Thought: Pride Is Prison"
type: THOUGHT
en_content: Pride is a prison, and Unconditional Love the only Liberator.
parent: topic.EVIL
tags:
  - pride
  - love
  - freedom
  - attitude
  - liberation
level: 3
neo4j: true
ptopic: "[[topic-EVIL]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.PRIDE IS PRISON",
    alias: "Thought: Pride Is Prison",
    parent: "topic.ATTITUDE",
    tags: ['pride', 'love', 'freedom', 'attitude', 'liberation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PRIDE IS PRISON",
    en_title: "Pride Is Prison",
    en_content: "Pride is a prison, and Unconditional Love the only Liberator.",
    es_title: "El Orgullo Es Prisión",
    es_content: "El orgullo es una prisión, y el Amor Incondicional el único Libertador.",
    fr_title: "L'Orgueil Est Prison",
    fr_content: "L'orgueil est une prison, et l'Amour Inconditionnel le seul Libérateur.",
    hi_title: "अहंकार कारागार है",
    hi_content: "अहंकार एक कारागार है, और निःशर्त प्रेम ही एकमात्र मुक्तिदाता है।",
    zh_title: "Jiāo'ào Shì Jiānyù",
    zh_content: "Jiāo'ào shì yīzuò jiānyù, ér Wútiáojiàn de Ài shì wéiyī de Jiětuō zhě."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRIDE IS PRISON" AND c.name = "content.PRIDE IS PRISON"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRIDE IS PRISON" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.PRIDE IS PRISON"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >PRIDE IS PRISON" }]->(child);
```
