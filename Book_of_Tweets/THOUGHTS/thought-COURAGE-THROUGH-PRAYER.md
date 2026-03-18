---
type: THOUGHT
name: "thought.COURAGE THROUGH PRAYER"
alias: "Thought: Courage Through Prayer"
parent: "topic.SPIRITUALITY"
en_content: "Prayer is where I find Courage and Perseverance."
tags: ["prayer", "courage", "perseverance", "spirituality", "strength"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013g)
CREATE (t:THOUGHT {    name: "thought.COURAGE THROUGH PRAYER",
    alias: "Thought: Courage Through Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'courage', 'perseverance', 'spirituality', 'strength'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.COURAGE THROUGH PRAYER",
    ctype: "THOUGHT",
    en_title: "Courage Through Prayer",
    en_content: "Prayer is where I find Courage and Perseverance.",
    es_title: "Valor a Través de la Oración",
    es_content: "La oración es donde encuentro valor y perseverancia.",
    fr_title: "Courage par la Prière",
    fr_content: "La prière est où je trouve le courage et la persévérance.",
    hi_title: "प्रार्थना के माध्यम से साहस",
    hi_content: "प्रार्थना वहीं है जहां मुझे साहस और दृढ़ता मिलती है।",
    zh_title: "Tōngguò Dǎogào Zhǎodào Yǒngqì",
    zh_content: "Dǎogào shì wǒ zhǎodào yǒngqì hé jiānchí de dìfāng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.COURAGE THROUGH PRAYER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->COURAGE THROUGH PRAYER"
RETURN t, parent;
```
