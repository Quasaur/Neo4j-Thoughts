---
type: THOUGHT
name: "thought.PSYCHOPATHIC CORPORATIONS"
alias: "Thought: Psychopathic Corporations"
parent: "topic.MORALITY"
en_content: "The corporation as a legal \"person\" is demonstrably psychopathic."
tags: ["morality", "corporations", "society", "ethics", "justice"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011b)
CREATE (t:THOUGHT {    name: "thought.PSYCHOPATHIC CORPORATIONS",
    alias: "Thought: Psychopathic Corporations",
    parent: "topic.MORALITY",
    tags: ['morality', 'corporations', 'society', 'ethics', 'justice'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.PSYCHOPATHIC CORPORATIONS",
    ctype: "THOUGHT",
    en_title: "Psychopathic Corporations",
    en_content: "The corporation as a legal \"person\" is demonstrably psychopathic.",
    es_title: "Corporaciones psicopáticas",
    es_content: "La corporación como entidad legal.",
    fr_title: "Sociétés psychopathes",
    fr_content: "La société en tant que personne morale",
    hi_title: "मनोरोगी निगम",
    hi_content: "एक कानूनी के रूप में निगम \",
    zh_title: "jīng shén bìng tài de gōng sī",
    zh_content: "gāi gōng sī zuò wéi yí gè hé fǎ de \"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PSYCHOPATHIC CORPORATIONS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->PSYCHOPATHIC CORPORATIONS"
RETURN t, parent;
```
