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
neo4j: true
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
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CORPORATE MONEY WORSHIP" AND c.name = "content.CORPORATE MONEY WORSHIP"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CORPORATE MONEY WORSHIP" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CORPORATE MONEY WORSHIP"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CORPORATE MONEY WORSHIP" }]->(child);
```
