---
name: "thought.CARNALITY AND STRIFE"
alias: "Thought: Carnality And Strife"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- morality
- carnality
- strife
- church
- bible
level: 3
neo4j: true
insert: true
---
# Carnality And Strife

> [!Thought-en]
> 1 Corinthians 3:3: "...for whereas there is among you envying, and strife, and divisions, are ye not carnal, and walk as men?"

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.CARNALITY AND STRIFE",
    alias: "Thought: Carnality And Strife",
    parent: "topic.MORALITY",
    tags: ['morality', 'carnality', 'strife', 'church', 'bible'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CARNALITY AND STRIFE",
    en_title: "Carnality And Strife",
    en_content: "1 Corinthians 3:3: \"...for whereas there is among you envying, and strife, and divisions, are ye not carnal, and walk as men?\"",
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
WHERE t.name = "thought.CARNALITY AND STRIFE" AND c.name = "content.CARNALITY AND STRIFE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CARNALITY AND STRIFE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CARNALITY AND STRIFE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CARNALITY AND STRIFE" }]->(child);
```