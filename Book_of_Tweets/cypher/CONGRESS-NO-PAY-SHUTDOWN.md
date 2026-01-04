---
name: "thought.CONGRESS NO PAY SHUTDOWN"
alias: "Thought: Congress No Pay Shutdown"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- congress
- shutdown
- money
- morality
- justice
level: 3
neo4j: true
insert: true
---
# Congress No Pay Shutdown

> [!Thought-en]
> Congress should not get paid as long as the Federal Government is shut down!

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2013b)
CREATE (t:THOUGHT {
    name: "thought.CONGRESS NO PAY SHUTDOWN",
    alias: "Thought: Congress No Pay Shutdown",
    parent: "topic.MORALITY",
    tags: ['congress', 'shutdown', 'money', 'morality', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONGRESS NO PAY SHUTDOWN",
    en_title: "Congress No Pay Shutdown",
    en_content: "Congress should not get paid as long as the Federal Government is shut down!",
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
WHERE t.name = "thought.CONGRESS NO PAY SHUTDOWN" AND c.name = "content.CONGRESS NO PAY SHUTDOWN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONGRESS NO PAY SHUTDOWN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CONGRESS NO PAY SHUTDOWN"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CONGRESS NO PAY SHUTDOWN" }]->(child);
```