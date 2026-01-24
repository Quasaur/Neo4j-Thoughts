---
name: "thought.WANTING DECEPTION"
alias: "Thought: Wanting Deception"
type: THOUGHT
en_content: "The Bible says that Satan has deceived us all...and we want to be deceived!"
parent: "topic.TRUTH"
tags:
- deception
- satan
- bible
- humanity
- truth
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.WANTING DECEPTION",
    alias: "Thought: Wanting Deception",
    parent: "topic.TRUTH",
    tags: ['deception', 'satan', 'bible', 'humanity', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WANTING DECEPTION",
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

MATCH (t:THOUGHT {name: "thought.WANTING DECEPTION"})
MATCH (c:CONTENT {name: "content.WANTING DECEPTION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.WANTING DECEPTION" }]->(c);

MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:THOUGHT {name: "thought.WANTING DECEPTION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH->WANTING DECEPTION" }]->(child);
```
