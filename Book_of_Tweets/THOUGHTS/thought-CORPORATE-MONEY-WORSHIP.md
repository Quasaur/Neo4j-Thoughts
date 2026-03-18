---
type: THOUGHT
name: "thought.CORPORATE MONEY WORSHIP"
alias: "Thought: Corporate Money Worship"
parent: "topic.MORALITY"
en_content: "The corporation as a legal \"person\" worships money."
tags: ["morality", "wealth", "corporations", "idolatry", "society"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011b)
CREATE (t:THOUGHT {    name: "thought.CORPORATE MONEY WORSHIP",
    alias: "Thought: Corporate Money Worship",
    parent: "topic.MORALITY",
    tags: ['morality', 'wealth', 'corporations', 'idolatry', 'society'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CORPORATE MONEY WORSHIP",
    ctype: "THOUGHT",
    en_title: "Corporate Money Worship",
    en_content: "The corporation as a legal \"person\" worships money.",
    es_title: "Adoración Corporativa al Dinero",
    es_content: "La corporación como \"persona\" legal adora el dinero.",
    fr_title: "Adoration Corporative de l'Argent",
    fr_content: "La corporation en tant que \"personne\" légale adore l'argent.",
    hi_title: "निगम धन पूजा",
    hi_content: "निगम कानूनी \"व्यक्ति\" के रूप में धन की पूजा करता है।",
    zh_title: "Gōngsī Duì Jīnqián de Chóngbài",
    zh_content: "Gōngsī zuòwéi fǎlǜ \"rén\" chóngbài jīnqián."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CORPORATE MONEY WORSHIP"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->CORPORATE MONEY WORSHIP"
RETURN t, parent;
```
