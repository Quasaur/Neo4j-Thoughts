---
name: "thought.PAYCHECK VS SOUL"
alias: "Thought: Paycheck Vs Soul"
type: THOUGHT
en_content: "Stop living like your paycheck is worth more than the dignity of your SOUL! Matthew 16:26"
parent: "topic.MORALITY"
tags:
- soul
- dignity
- wealth
- morality
- character
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012d_2)
CREATE (t:THOUGHT {
    name: "thought.PAYCHECK VS SOUL",
    alias: "Thought: Paycheck Vs Soul",
    parent: "topic.MORALITY",
    tags: ['soul', 'dignity', 'wealth', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PAYCHECK VS SOUL",
    en_title: "Paycheck Vs Soul",
    en_content: "Stop living like your paycheck is worth more than the dignity of your SOUL! Matthew 16:26",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PAYCHECK VS SOUL" AND c.name = "content.PAYCHECK VS SOUL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PAYCHECK VS SOUL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PAYCHECK VS SOUL"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PAYCHECK VS SOUL" }]->(child);
```
