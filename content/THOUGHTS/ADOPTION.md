---
name: thought.ADOPTION
alias: "Thought: ADOPTION"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- adoption
- abba
- father
- childofgod
- everlasting
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ADOPTION",
    alias: "Thought: ADOPTION",
    parent: "topic.THE-GOSPEL",
    tags: ["adoption", "abba", "father", "childofgod", "everlasting"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ADOPTION",
    en_title: "ADOPTION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ADOPTION" AND c.name = "content.ADOPTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.ADOPTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.ADOPTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->ADOPTION"}]->(child);
```