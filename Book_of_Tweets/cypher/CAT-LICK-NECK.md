---
name: "thought.CAT LICK NECK"
alias: "Thought: Cat Lick Neck"
type: THOUGHT
en_content: "My cat can lick its own neck...God is great!"
parent: topic.BIOLOGY
tags:
  - creation
  - nature
  - design
  - cat
  - humor
level: 6
neo4j: false
ptopic: "[[topic-BIOLOGY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.CAT LICK NECK",
    alias: "Thought: Cat Lick Neck",
    parent: "topic.BIOLOGY",
    tags: ['creation', 'nature', 'design', 'cat', 'humor'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.CAT LICK NECK",
    en_title: "Cat Lick Neck",
    en_content: "My cat can lick its own neck...God is great!",
    es_title: "El Gato Lame su Cuello",
    es_content: "Mi gato puede lamerse su propio cuello... ¡Dios es grande!",
    fr_title: "Le Chat Lèche son Cou",
    fr_content: "Mon chat peut lécher son propre cou... Dieu est grand !",
    hi_title: "बिल्ली अपनी गर्दन चाटती है",
    hi_content: "मेरी बिल्ली अपनी गर्दन चाट सकती है... भगवान महान हैं!",
    zh_title: "Māo Tiǎn Bózi",
    zh_content: "Wǒ de māo kěyǐ tiǎn zìjǐ de bózi... Shàngdì shì wěidà de!"
});

MATCH (t:THOUGHT {name: "thought.CAT LICK NECK"})
MATCH (c:CONTENT {name: "content.CAT LICK NECK"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CAT LICK NECK" }]->(c);

MATCH (parent:TOPIC {name: "topic.BIOLOGY"})
MATCH (child:THOUGHT {name: "thought.CAT LICK NECK"})
MERGE (parent)-[:HAS_THOUGHT { "name": "BIOLOGY->CAT LICK NECK" }]->(child);
```
