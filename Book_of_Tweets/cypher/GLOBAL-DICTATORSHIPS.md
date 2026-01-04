---
name: "thought.GLOBAL DICTATORSHIPS"
alias: "Thought: Global Dictatorships"
type: THOUGHT
en_content: "2 billion of the 7 billion people on this planet live under dictatorships."
parent: "topic.MORALITY"
tags:
- dictatorship
- society
- justice
- politics
- humanity
level: 3
neo4j: true
insert: true
---
# Global Dictatorships

> [!Thought-en]
> 2 billion of the 7 billion people on this planet live under dictatorships.

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Dec-2011a)
CREATE (t:THOUGHT {
    name: "thought.GLOBAL DICTATORSHIPS",
    alias: "Thought: Global Dictatorships",
    parent: "topic.MORALITY",
    tags: ['dictatorship', 'society', 'justice', 'politics', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GLOBAL DICTATORSHIPS",
    en_title: "Global Dictatorships",
    en_content: "2 billion of the 7 billion people on this planet live under dictatorships.",
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
WHERE t.name = "thought.GLOBAL DICTATORSHIPS" AND c.name = "content.GLOBAL DICTATORSHIPS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLOBAL DICTATORSHIPS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.GLOBAL DICTATORSHIPS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >GLOBAL DICTATORSHIPS" }]->(child);
```