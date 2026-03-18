---
type: THOUGHT
name: "thought.UNPATRIOTIC CORPORATIONS"
alias: "Thought: Unpatriotic Corporations"
parent: "topic.MORALITY"
en_content: "The corporation as a legal \"person\" is unpatriotic."
tags: ["morality", "corporations", "society", "patriotism", "justice"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011c)
CREATE (t:THOUGHT {    name: "thought.UNPATRIOTIC CORPORATIONS",
    alias: "Thought: Unpatriotic Corporations",
    parent: "topic.MORALITY",
    tags: ['morality', 'corporations', 'society', 'patriotism', 'justice'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.UNPATRIOTIC CORPORATIONS",
    ctype: "THOUGHT",
    en_title: "Unpatriotic Corporations",
    en_content: "The corporation as a legal \"person\" is unpatriotic.",
    es_title: "Corporaciones antipatrióticas",
    es_content: "La corporación como entidad legal.",
    fr_title: "Entreprises antipatriotiques",
    fr_content: "La société en tant que personne morale",
    hi_title: "देशद्रोही निगम",
    hi_content: "एक कानूनी के रूप में निगम \",
    zh_title: "bù ài guó de gōng sī",
    zh_content: "gāi gōng sī zuò wéi yí gè hé fǎ de \"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNPATRIOTIC CORPORATIONS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->UNPATRIOTIC CORPORATIONS"
RETURN t, parent;
```
