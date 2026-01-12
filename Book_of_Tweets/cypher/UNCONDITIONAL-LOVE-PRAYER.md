---
name: "thought.UNCONDITIONAL LOVE PRAYER"
alias: "Thought: Unconditional Love Prayer"
type: THOUGHT
en_content: "Prayer is where I am loved unconditionally."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- love
- acceptance
- spirituality
- presence
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013f)
CREATE (t:THOUGHT {
    name: "thought.UNCONDITIONAL LOVE PRAYER",
    alias: "Thought: Unconditional Love Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'love', 'acceptance', 'spirituality', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL LOVE PRAYER",
    en_title: "Unconditional Love Prayer",
    en_content: "Prayer is where I am loved unconditionally.",
    es_title: "Oración de Amor Incondicional",
    es_content: "La oración es donde soy amado incondicionalmente.",
    fr_title: "Prière d'Amour Inconditionnel",
    fr_content: "La prière est où je suis aimé inconditionnellement.",
    hi_title: "निःशर्त प्रेम की प्रार्थना",
    hi_content: "प्रार्थना वह स्थान है जहाँ मुझे निःशर्त प्रेम मिलता है।",
    zh_title: "Wú tiáo jiàn ài de qí dǎo",
    zh_content: "Qí dǎo shì wǒ dé dào wú tiáo jiàn zhī ài de dì fāng."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNCONDITIONAL LOVE PRAYER" AND c.name = "content.UNCONDITIONAL LOVE PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNCONDITIONAL LOVE PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.UNCONDITIONAL LOVE PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >UNCONDITIONAL LOVE PRAYER" }]->(child);
```
