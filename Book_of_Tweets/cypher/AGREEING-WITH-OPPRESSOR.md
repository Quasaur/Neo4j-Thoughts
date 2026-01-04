---
name: "thought.AGREEING WITH OPPRESSOR"
alias: "Thought: Agreeing With Oppressor"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- oppression
- dignity
- money
- morality
- society
level: 3
neo4j: true
insert: true
---
# Agreeing With Oppressor

> [!Thought-en]
> Every day we do things to let the Opressor know that we AGREE that his money is worth more than justice, dignity, equity and honor.

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012e)
CREATE (t:THOUGHT {
    name: "thought.AGREEING WITH OPPRESSOR",
    alias: "Thought: Agreeing With Oppressor",
    parent: "topic.MORALITY",
    tags: ['oppression', 'dignity', 'money', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AGREEING WITH OPPRESSOR",
    en_title: "Agreeing With Oppressor",
    en_content: "Every day we do things to let the Opressor know that we AGREE that his money is worth more than justice, dignity, equity and honor.",
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
WHERE t.name = "thought.AGREEING WITH OPPRESSOR" AND c.name = "content.AGREEING WITH OPPRESSOR"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AGREEING WITH OPPRESSOR" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.AGREEING WITH OPPRESSOR"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >AGREEING WITH OPPRESSOR" }]->(child);
```