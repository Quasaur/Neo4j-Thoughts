---
type: THOUGHT
name: "thought.WANTING DECEPTION"
alias: "Thought: Wanting Deception"
parent: "topic.TRUTH"
en_content: "The Bible says that Satan has deceived us all...and we want to be deceived!"
tags: ["deception", "satan", "bible", "humanity", "truth"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Dec-2012)
CREATE (t:THOUGHT {    name: "thought.WANTING DECEPTION",
    alias: "Thought: Wanting Deception",
    parent: "topic.TRUTH",
    tags: ['deception', 'satan', 'bible', 'humanity', 'truth'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.WANTING DECEPTION",
    ctype: "THOUGHT",
    en_title: "Wanting Deception",
    en_content: "The Bible says that Satan has deceived us all...and we want to be deceived!",
    es_title: "Deseando el Engaño",
    es_content: "La Biblia dice que Satanás nos ha engañado a todos...¡y queremos ser engañados!",
    fr_title: "Désirer la Tromperie",
    fr_content: "La Bible dit que Satan nous a tous trompés...et nous voulons être trompés !",
    hi_title: "धोखा चाहना",
    hi_content: "बाइबल कहती है कि शैतान ने हम सभी को धोखा दिया है...और हम धोखा खाना चाहते हैं!",
    zh_title: "Xiang Yao Bei Qi Pian",
    zh_content: "Sheng Jing shuo Sa Dan qi pian le wo men suo you ren...er wo men xiang yao bei qi pian!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WANTING DECEPTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->WANTING DECEPTION"
RETURN t, parent;
```
