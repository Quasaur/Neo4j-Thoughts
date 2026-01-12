---
name: "thought.MEANINGLESS LIFE LIE"
alias: "Thought: Meaningless Life Lie"
type: THOUGHT
en_content: "Religion: if no one's right, and everyone's wrong, then life is both meaningless AND a lie."
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- meaning
- religion
- truth
- skepticism
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.MEANINGLESS LIFE LIE",
    alias: "Thought: Meaningless Life Lie",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'meaning', 'religion', 'truth', 'skepticism'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MEANINGLESS LIFE LIE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MEANINGLESS LIFE LIE" AND c.name = "content.MEANINGLESS LIFE LIE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MEANINGLESS LIFE LIE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.MEANINGLESS LIFE LIE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >MEANINGLESS LIFE LIE" }]->(child);
```
