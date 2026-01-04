---
name: "thought.NOT BEING GOD"
alias: "Thought: Not Being God"
type: THOUGHT
parent: "topic.HUMANITY"
tags:
- humility
- humanity
- god
- identity
- joy
level: 3
neo4j: true
insert: true
---
# Not Being God

> [!Thought-en]
> I am not God; and I'm so glad that I don't have to be!

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.NOT BEING GOD",
    alias: "Thought: Not Being God",
    parent: "topic.HUMANITY",
    tags: ['humility', 'humanity', 'god', 'identity', 'joy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOT BEING GOD",
    en_title: "Not Being God",
    en_content: "I am not God; and I'm so glad that I don't have to be!",
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
WHERE t.name = "thought.NOT BEING GOD" AND c.name = "content.NOT BEING GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOT BEING GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.NOT BEING GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >NOT BEING GOD" }]->(child);
```