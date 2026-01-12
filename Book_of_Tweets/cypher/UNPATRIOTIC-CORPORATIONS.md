---
name: "thought.UNPATRIOTIC CORPORATIONS"
alias: "Thought: Unpatriotic Corporations"
type: THOUGHT
en_content: "The corporation as a legal \"person\" is unpatriotic."
parent: "topic.MORALITY"
tags:
- morality
- corporations
- society
- patriotism
- justice
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011c)
CREATE (t:THOUGHT {
    name: "thought.UNPATRIOTIC CORPORATIONS",
    alias: "Thought: Unpatriotic Corporations",
    parent: "topic.MORALITY",
    tags: ['morality', 'corporations', 'society', 'patriotism', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNPATRIOTIC CORPORATIONS",
    en_title: "Unpatriotic Corporations",
    en_content: "The corporation as a legal \"person\" is unpatriotic.",
    es_title: "Corporaciones antipatrióticas",
    es_content: "La corporación como entidad legal.",
    fr_title: "Entreprises antipatriotiques",
    fr_content: "La société en tant que personne morale",
    hi_title: "देशद्रोही निगम",
    hi_content: "एक कानूनी के रूप में निगम \",
    zh_title: "不爱国的公司",
    zh_content: "该公司作为一个合法的\"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNPATRIOTIC CORPORATIONS" AND c.name = "content.UNPATRIOTIC CORPORATIONS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNPATRIOTIC CORPORATIONS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.UNPATRIOTIC CORPORATIONS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >UNPATRIOTIC CORPORATIONS" }]->(child);
```
