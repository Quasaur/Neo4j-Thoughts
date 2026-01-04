---
name: "thought.LIVING IN CHRISTS RIGHTEOUSNESS"
alias: "Thought: Living In Christs Righteousness"
type: THOUGHT
parent: "topic.GRACE"
tags:
- righteousness
- grace
- christ
- life
- salvation
level: 3
neo4j: true
insert: true
---
# Living In Christs Righteousness

> [!Thought-en]
> I live--not with my own righteousness but with Christ's; for God placed me in Christ when He obeyed...now He obeys in me!

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.LIVING IN CHRISTS RIGHTEOUSNESS",
    alias: "Thought: Living In Christs Righteousness",
    parent: "topic.GRACE",
    tags: ['righteousness', 'grace', 'christ', 'life', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LIVING IN CHRISTS RIGHTEOUSNESS",
    en_title: "Living In Christs Righteousness",
    en_content: "I live--not with my own righteousness but with Christ's; for God placed me in Christ when He obeyed...now He obeys in me!",
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
WHERE t.name = "thought.LIVING IN CHRISTS RIGHTEOUSNESS" AND c.name = "content.LIVING IN CHRISTS RIGHTEOUSNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIVING IN CHRISTS RIGHTEOUSNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LIVING IN CHRISTS RIGHTEOUSNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LIVING IN CHRISTS RIGHTEOUSNESS" }]->(child);
```