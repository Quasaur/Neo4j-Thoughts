---
name: "thought.DEFINE PERFECT LOVE"
alias: "Thought: Define Perfect Love"
type: THOUGHT
en_content: "Love: the blurring of identity between two or more persons. The Love among the Members of The Godhead is such: to see One is to see All."
parent: "topic.PHILOSOPHY"
tags:
- love
- identity
- trinity
- philosophy
- unity
level: 4
neo4j: true
insert: true
---
# Define Perfect Love

> [!Thought-en]
> Love: the blurring of identity between two or more persons. The Love among the Members of The Godhead is such: to see One is to see All.

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.DEFINE PERFECT LOVE",
    alias: "Thought: Define Perfect Love",
    parent: "topic.PHILOSOPHY",
    tags: ['love', 'identity', 'trinity', 'philosophy', 'unity'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE PERFECT LOVE",
    en_title: "Define Perfect Love",
    en_content: "Love: the blurring of identity between two or more persons. The Love among the Members of The Godhead is such: to see One is to see All.",
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
WHERE t.name = "thought.DEFINE PERFECT LOVE" AND c.name = "content.DEFINE PERFECT LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE PERFECT LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.DEFINE PERFECT LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >DEFINE PERFECT LOVE" }]->(child);
```