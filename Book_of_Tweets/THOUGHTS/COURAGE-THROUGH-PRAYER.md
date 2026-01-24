---
name: "thought.COURAGE THROUGH PRAYER"
alias: "Thought: Courage Through Prayer"
type: THOUGHT
en_content: "Prayer is where I find Courage and Perseverance."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- courage
- perseverance
- spirituality
- strength
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013g)
CREATE (t:THOUGHT {
    name: "thought.COURAGE THROUGH PRAYER",
    alias: "Thought: Courage Through Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'courage', 'perseverance', 'spirituality', 'strength'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.COURAGE THROUGH PRAYER",
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

MATCH (t:THOUGHT {name: "thought.COURAGE THROUGH PRAYER"})
MATCH (c:CONTENT {name: "content.COURAGE THROUGH PRAYER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.COURAGE THROUGH PRAYER" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.COURAGE THROUGH PRAYER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->COURAGE THROUGH PRAYER" }]->(child);
```
