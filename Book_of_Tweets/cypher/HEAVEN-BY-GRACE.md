---
name: "thought.HEAVEN BY GRACE"
alias: "Thought: Heaven By Grace"
type: THOUGHT
parent: "topic.GRACE"
tags:
- grace
- heaven
- salvation
- power
- merit
level: 3
neo4j: true
insert: true
---
# Heaven By Grace

> [!Thought-en]
> I know I have no business being in Heaven--but I'm going...such is the Power of Divine Grace!

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Dec-2011a)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN BY GRACE",
    alias: "Thought: Heaven By Grace",
    parent: "topic.GRACE",
    tags: ['grace', 'heaven', 'salvation', 'power', 'merit'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HEAVEN BY GRACE",
    en_title: "Heaven By Grace",
    en_content: "I know I have no business being in Heaven--but I'm going...such is the Power of Divine Grace!",
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
WHERE t.name = "thought.HEAVEN BY GRACE" AND c.name = "content.HEAVEN BY GRACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN BY GRACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.HEAVEN BY GRACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >HEAVEN BY GRACE" }]->(child);
```