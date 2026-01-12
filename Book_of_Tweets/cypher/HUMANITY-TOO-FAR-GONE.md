---
name: "thought.HUMANITY TOO FAR GONE"
alias: "Thought: Humanity Too Far Gone"
type: THOUGHT
en_content: "The Bible teaches that humanity is too far gone to have any desire for the One True God; God has to put it in us to save us."
parent: "topic.GRACE"
tags:
- salvation
- humanity
- grace
- god
- desire
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.HUMANITY TOO FAR GONE",
    alias: "Thought: Humanity Too Far Gone",
    parent: "topic.GRACE",
    tags: ['salvation', 'humanity', 'grace', 'god', 'desire'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMANITY TOO FAR GONE",
    en_title: "Humanity Too Far Gone",
    en_content: "The Bible teaches that humanity is too far gone to have any desire for the One True God; God has to put it in us to save us.",
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
WHERE t.name = "thought.HUMANITY TOO FAR GONE" AND c.name = "content.HUMANITY TOO FAR GONE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HUMANITY TOO FAR GONE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.HUMANITY TOO FAR GONE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >HUMANITY TOO FAR GONE" }]->(child);
```
