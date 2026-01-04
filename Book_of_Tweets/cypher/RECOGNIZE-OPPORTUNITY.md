---
name: "thought.RECOGNIZE OPPORTUNITY"
alias: "Thought: Recognize Opportunity"
type: THOUGHT
en_content: "The tragedy is that African American men do not recognize opportunity when they see it."
parent: "topic.WISDOM"
tags:
- opportunity
- wisdom
- tragedy
- recognition
- race
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012a)
CREATE (t:THOUGHT {
    name: "thought.RECOGNIZE OPPORTUNITY",
    alias: "Thought: Recognize Opportunity",
    parent: "topic.WISDOM",
    tags: ['opportunity', 'wisdom', 'tragedy', 'recognition', 'race'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RECOGNIZE OPPORTUNITY",
    en_title: "Recognize Opportunity",
    en_content: "The tragedy is that African American men do not recognize opportunity when they see it.",
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
WHERE t.name = "thought.RECOGNIZE OPPORTUNITY" AND c.name = "content.RECOGNIZE OPPORTUNITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RECOGNIZE OPPORTUNITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.RECOGNIZE OPPORTUNITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >RECOGNIZE OPPORTUNITY" }]->(child);
```
