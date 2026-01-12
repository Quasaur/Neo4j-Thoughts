---
name: "thought.PSYCHOPATHIC CORPORATIONS"
alias: "Thought: Psychopathic Corporations"
type: THOUGHT
en_content: "The corporation as a legal \"person\" is demonstrably psychopathic."
parent: "topic.MORALITY"
tags:
- morality
- corporations
- society
- ethics
- justice
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.PSYCHOPATHIC CORPORATIONS",
    alias: "Thought: Psychopathic Corporations",
    parent: "topic.MORALITY",
    tags: ['morality', 'corporations', 'society', 'ethics', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PSYCHOPATHIC CORPORATIONS",
    en_title: "Psychopathic Corporations",
    en_content: "The corporation as a legal \"person\" is demonstrably psychopathic.",
    es_title: "Corporaciones psicopáticas",
    es_content: "La corporación como entidad legal.",
    fr_title: "Sociétés psychopathes",
    fr_content: "La société en tant que personne morale",
    hi_title: "मनोरोगी निगम",
    hi_content: "एक कानूनी के रूप में निगम \",
    zh_title: "精神病态的公司",
    zh_content: "该公司作为一个合法的\"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PSYCHOPATHIC CORPORATIONS" AND c.name = "content.PSYCHOPATHIC CORPORATIONS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PSYCHOPATHIC CORPORATIONS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PSYCHOPATHIC CORPORATIONS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PSYCHOPATHIC CORPORATIONS" }]->(child);
```
