---
name: "thought.CONGRESS HOUSE LORDS"
alias: "Thought: Congress House Lords"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- congress
- america
- aristocracy
- morality
- society
level: 3
neo4j: true
insert: true
---
# Congress House Lords

> [!Thought-en]
> Both houses of this American Congress have become a House of Lords.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.CONGRESS HOUSE LORDS",
    alias: "Thought: Congress House Lords",
    parent: "topic.MORALITY",
    tags: ['congress', 'america', 'aristocracy', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONGRESS HOUSE LORDS",
    en_title: "Congress House Lords",
    en_content: "Both houses of this American Congress have become a House of Lords.",
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
WHERE t.name = "thought.CONGRESS HOUSE LORDS" AND c.name = "content.CONGRESS HOUSE LORDS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONGRESS HOUSE LORDS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CONGRESS HOUSE LORDS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CONGRESS HOUSE LORDS" }]->(child);
```