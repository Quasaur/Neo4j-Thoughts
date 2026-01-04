---
name: "thought.LIFE SHOULD BE PAIN"
alias: "Thought: Life Should Be Pain"
type: THOUGHT
en_content: "Many will tell you life is pain; not many will say it should be. It should be."
parent: "topic.PHILOSOPHY"
tags:
- pain
- life
- philosophy
- suffering
- truth
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013d)
CREATE (t:THOUGHT {
    name: "thought.LIFE SHOULD BE PAIN",
    alias: "Thought: Life Should Be Pain",
    parent: "topic.PHILOSOPHY",
    tags: ['pain', 'life', 'philosophy', 'suffering', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LIFE SHOULD BE PAIN",
    en_title: "Life Should Be Pain",
    en_content: "Many will tell you life is pain; not many will say it should be. It should be.",
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
WHERE t.name = "thought.LIFE SHOULD BE PAIN" AND c.name = "content.LIFE SHOULD BE PAIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIFE SHOULD BE PAIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.LIFE SHOULD BE PAIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >LIFE SHOULD BE PAIN" }]->(child);
```
