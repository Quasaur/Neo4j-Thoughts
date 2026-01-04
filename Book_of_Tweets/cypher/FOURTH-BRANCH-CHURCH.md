---
name: "thought.FOURTH BRANCH CHURCH"
alias: "Thought: Fourth Branch Church"
type: THOUGHT
en_content: "The true power of the Church is demonstrated by its tax-free status AND that no one's willing to ADMIT it's the 4th Branch of the U.S. Gov."
parent: "topic.RELIGION"
tags:
- church
- government
- politics
- religion
- society
level: 3
neo4j: true
insert: true
---
# Fourth Branch Church

> [!Thought-en]
> The true power of the Church is demonstrated by its tax-free status AND that no one's willing to ADMIT it's the 4th Branch of the U.S. Gov.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.FOURTH BRANCH CHURCH",
    alias: "Thought: Fourth Branch Church",
    parent: "topic.RELIGION",
    tags: ['church', 'government', 'politics', 'religion', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FOURTH BRANCH CHURCH",
    en_title: "Fourth Branch Church",
    en_content: "The true power of the Church is demonstrated by its tax-free status AND that no one's willing to ADMIT it's the 4th Branch of the U.S. Gov.",
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
WHERE t.name = "thought.FOURTH BRANCH CHURCH" AND c.name = "content.FOURTH BRANCH CHURCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FOURTH BRANCH CHURCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.FOURTH BRANCH CHURCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >FOURTH BRANCH CHURCH" }]->(child);
```