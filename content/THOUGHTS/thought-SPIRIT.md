---
type: THOUGHT
name: "thought.SPIRIT"
alias: "Thought: SPIRIT"
parent: "topic.SPIRITS"
tags: ["holy_spirit", "spirit_of_christ", "spirit_of_truth", "spirit_of_grace", "jesus_christ"]
ptopic: "[[topic-SPIRITS]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SPIRIT",
    alias: "Thought: SPIRIT",
    parent: "topic.SPIRITS",
    tags: ["holy_spirit", "spirit_of_christ", "spirit_of_truth", "spirit_of_grace", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SPIRIT",
    en_title: "SPIRIT",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SPIRIT" AND c.name = "content.SPIRIT"
MERGE (t)-[:HAS_CONTENT {name: "edge.SPIRIT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITS" AND child.name = "thought.SPIRIT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITS->SPIRIT"}]->(child);
```