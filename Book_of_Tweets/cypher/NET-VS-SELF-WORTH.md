---
name: "thought.NET VS SELF WORTH"
alias: "Thought: Net Vs Self Worth"
type: THOUGHT
parent: "topic.HUMANITY"
tags:
- wealth
- value
- self_worth
- humanity
- confusion
level: 3
neo4j: true
insert: true
---
# Net Vs Self Worth

> [!Thought-en]
> Don't confuse net worth with self-worth.

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.NET VS SELF WORTH",
    alias: "Thought: Net Vs Self Worth",
    parent: "topic.HUMANITY",
    tags: ['wealth', 'value', 'self_worth', 'humanity', 'confusion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NET VS SELF WORTH",
    en_title: "Net Vs Self Worth",
    en_content: "Don't confuse net worth with self-worth.",
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
WHERE t.name = "thought.NET VS SELF WORTH" AND c.name = "content.NET VS SELF WORTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NET VS SELF WORTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.NET VS SELF WORTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >NET VS SELF WORTH" }]->(child);
```