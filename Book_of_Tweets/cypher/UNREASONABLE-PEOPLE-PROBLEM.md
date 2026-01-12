---
name: "thought.UNREASONABLE PEOPLE PROBLEM"
alias: "Thought: Unreasonable People Problem"
type: THOUGHT
en_content: "Life would be perfect but for the presence of unreasonable people."
parent: "topic.ATTITUDE"
tags:
- people
- reason
- life
- attitude
- problem
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2013a)
CREATE (t:THOUGHT {
    name: "thought.UNREASONABLE PEOPLE PROBLEM",
    alias: "Thought: Unreasonable People Problem",
    parent: "topic.ATTITUDE",
    tags: ['people', 'reason', 'life', 'attitude', 'problem'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNREASONABLE PEOPLE PROBLEM",
    en_title: "Unreasonable People Problem",
    en_content: "Life would be perfect but for the presence of unreasonable people.",
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
WHERE t.name = "thought.UNREASONABLE PEOPLE PROBLEM" AND c.name = "content.UNREASONABLE PEOPLE PROBLEM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNREASONABLE PEOPLE PROBLEM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.UNREASONABLE PEOPLE PROBLEM"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >UNREASONABLE PEOPLE PROBLEM" }]->(child);
```
