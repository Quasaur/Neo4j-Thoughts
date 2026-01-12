---
name: "thought.RESPECT AND AFFECTION"
alias: "Thought: Respect And Affection"
type: THOUGHT
en_content: "Respect breeds affection."
parent: "topic.MORALITY"
tags:
- respect
- affection
- relationship
- morality
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.RESPECT AND AFFECTION",
    alias: "Thought: Respect And Affection",
    parent: "topic.MORALITY",
    tags: ['respect', 'affection', 'relationship', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RESPECT AND AFFECTION",
    en_title: "Respect And Affection",
    en_content: "Respect breeds affection.",
    es_title: "Respeto Y Afecto",
    es_content: "El respeto engendra afecto.",
    fr_title: "Respect Et Affection",
    fr_content: "Le respect engendre l'affection.",
    hi_title: "सम्मान और स्नेह",
    hi_content: "सम्मान स्नेह को जन्म देता है।",
    zh_title: "Zun Zhong Yu Ai Qing",
    zh_content: "Zun zhong zi yang ai qing."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.RESPECT AND AFFECTION" AND c.name = "content.RESPECT AND AFFECTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RESPECT AND AFFECTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.RESPECT AND AFFECTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >RESPECT AND AFFECTION" }]->(child);
```
