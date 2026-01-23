---
name: "thought.MLK MURDERED GOOD DEEDS"
alias: "Thought: Mlk Murdered Good Deeds"
type: THOUGHT
en_content: "Remember: Martin Luther King Jr. was murdered -- not for his crimes, but for his good deeds."
parent: "topic.MORALITY"
tags:
- mlk
- justice
- murder
- deeds
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.MLK MURDERED GOOD DEEDS",
    alias: "Thought: Mlk Murdered Good Deeds",
    parent: "topic.MORALITY",
    tags: ['mlk', 'justice', 'murder', 'deeds', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MLK MURDERED GOOD DEEDS",
    en_title: "Mlk Murdered Good Deeds",
    en_content: "Remember: Martin Luther King Jr. was murdered -- not for his crimes, but for his good deeds.",
    es_title: "MLK Asesinado Por Buenas Obras",
    es_content: "Recuerda: Martin Luther King Jr. fue asesinado -- no por sus crímenes, sino por sus buenas obras.",
    fr_title: "MLK Assassiné Pour Ses Bonnes Œuvres",
    fr_content: "Souviens-toi : Martin Luther King Jr. a été assassiné -- non pas pour ses crimes, mais pour ses bonnes œuvres.",
    hi_title: "एमएलके की अच्छे कर्मों के लिए हत्या",
    hi_content: "याद रखें: मार्टिन लूथर किंग जूनियर की हत्या की गई थी -- उनके अपराधों के लिए नहीं, बल्कि उनके अच्छे कर्मों के लिए।",
    zh_title: "MLK Bei Sha Yin Wei Shan Xing",
    zh_content: "Ji Zhu: Ma Ding Lu De Jin Bo Shi Bei Sha Hai De -- Bu Shi Yin Wei Ta De Zui Xing, Er Shi Yin Wei Ta De Shan Xing."
});

MATCH (t:THOUGHT {name: "thought.MLK MURDERED GOOD DEEDS"})
MATCH (c:CONTENT {name: "content.MLK MURDERED GOOD DEEDS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MLK MURDERED GOOD DEEDS" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.MLK MURDERED GOOD DEEDS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >MLK MURDERED GOOD DEEDS" }]->(child);
```
