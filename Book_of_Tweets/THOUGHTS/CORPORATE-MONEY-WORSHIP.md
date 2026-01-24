---
name: "thought.CORPORATE MONEY WORSHIP"
alias: "Thought: Corporate Money Worship"
type: THOUGHT
en_content: "The corporation as a legal \"person\" worships money."
parent: "topic.MORALITY"
tags:
- morality
- wealth
- corporations
- idolatry
- society
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.CORPORATE MONEY WORSHIP",
    alias: "Thought: Corporate Money Worship",
    parent: "topic.MORALITY",
    tags: ['morality', 'wealth', 'corporations', 'idolatry', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CORPORATE MONEY WORSHIP",
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

MATCH (t:THOUGHT {name: "thought.CORPORATE MONEY WORSHIP"})
MATCH (c:CONTENT {name: "content.CORPORATE MONEY WORSHIP"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CORPORATE MONEY WORSHIP" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.CORPORATE MONEY WORSHIP"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->CORPORATE MONEY WORSHIP" }]->(child);
```
