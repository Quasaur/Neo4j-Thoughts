---
type: THOUGHT
name: "thought.MEANINGLESS LIFE LIE"
alias: "Thought: Meaningless Life Lie"
parent: "topic.PHILOSOPHY"
en_content: "Religion: if no one's right, and everyone's wrong, then life is both meaningless AND a lie."
tags: ["philosophy", "meaning", "religion", "truth", "skepticism"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jan-2012b)
CREATE (t:THOUGHT {    name: "thought.MEANINGLESS LIFE LIE",
    alias: "Thought: Meaningless Life Lie",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'meaning', 'religion', 'truth', 'skepticism'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.MEANINGLESS LIFE LIE",
    ctype: "THOUGHT",
    en_title: "Meaningless Life Lie",
    en_content: "Religion: if no one's right, and everyone's wrong, then life is both meaningless AND a lie.",
    es_title: "Mentira de Vida Sin Sentido",
    es_content: "Religión: si nadie tiene razón, y todos están equivocados, entonces la vida es tanto sin sentido COMO una mentira.",
    fr_title: "Mensonge de Vie Dénuée de Sens",
    fr_content: "Religion : si personne n'a raison, et que tout le monde a tort, alors la vie est à la fois dénuée de sens ET un mensonge.",
    hi_title: "अर्थहीन जीवन झूठ",
    hi_content: "धर्म: यदि कोई भी सही नहीं है, और सभी गलत हैं, तो जीवन अर्थहीन है और एक झूठ भी है।",
    zh_title: "Wu Yi Yi Sheng Ming Huang Yan",
    zh_content: "Zong Jiao: ru guo mei you ren shi dui de, er mei ge ren dou shi cuo de, na me sheng ming ji shi wu yi yi de YOU shi huang yan."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MEANINGLESS LIFE LIE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->MEANINGLESS LIFE LIE"
RETURN t, parent;
```
