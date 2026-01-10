---
name: "thought.SANHEDRIN CONCERNS"
alias: "Thought: Sanhedrin Concerns"
type: THOUGHT
en_content: "The Sanhedrin was more concerned about their authority and money than about serving God or God's people."
parent: "topic.MORALITY"
tags:
- authority
- money
- morality
- church
- history
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.SANHEDRIN CONCERNS",
    alias: "Thought: Sanhedrin Concerns",
    parent: "topic.MORALITY",
    tags: ['authority', 'money', 'morality', 'church', 'history'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SANHEDRIN CONCERNS",
    en_title: "Sanhedrin Concerns",
    en_content: "The Sanhedrin was more concerned about their authority and money than about serving God or God's people.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SANHEDRIN CONCERNS" AND c.name = "content.SANHEDRIN CONCERNS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SANHEDRIN CONCERNS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SANHEDRIN CONCERNS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SANHEDRIN CONCERNS" }]->(child);
```
