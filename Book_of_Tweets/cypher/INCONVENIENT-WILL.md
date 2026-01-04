---
name: "thought.INCONVENIENT WILL"
alias: "Thought: Inconvenient Will"
type: THOUGHT
en_content: "Accomplishing God's Will is rarely convenient."
parent: "topic.SPIRITUALITY"
tags:
- will
- obedience
- spirituality
- sacrifice
- convenience
level: 2
neo4j: true
insert: true
---
# Inconvenient Will

> [!Thought-en]
> Accomplishing God's Will is rarely convenient.

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.INCONVENIENT WILL",
    alias: "Thought: Inconvenient Will",
    parent: "topic.SPIRITUALITY",
    tags: ['will', 'obedience', 'spirituality', 'sacrifice', 'convenience'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INCONVENIENT WILL",
    en_title: "Inconvenient Will",
    en_content: "Accomplishing God's Will is rarely convenient.",
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
WHERE t.name = "thought.INCONVENIENT WILL" AND c.name = "content.INCONVENIENT WILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INCONVENIENT WILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.INCONVENIENT WILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >INCONVENIENT WILL" }]->(child);
```