---
name: "thought.LIVELIER LIVING"
alias: "Thought: Livelier Living"
type: THOUGHT
en_content: "Soap makes water wetter; Jesus Christ makes living livelier!"
parent: "topic.SPIRITUALITY"
tags:
- jesus
- life
- joy
- spirituality
- character
level: 2
neo4j: true
insert: true
---
# Livelier Living

> [!Thought-en]
> Soap makes water wetter; Jesus Christ makes living livelier!

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012h)
CREATE (t:THOUGHT {
    name: "thought.LIVELIER LIVING",
    alias: "Thought: Livelier Living",
    parent: "topic.SPIRITUALITY",
    tags: ['jesus', 'life', 'joy', 'spirituality', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIVELIER LIVING",
    en_title: "Livelier Living",
    en_content: "Soap makes water wetter; Jesus Christ makes living livelier!",
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
WHERE t.name = "thought.LIVELIER LIVING" AND c.name = "content.LIVELIER LIVING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIVELIER LIVING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.LIVELIER LIVING"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >LIVELIER LIVING" }]->(child);
```