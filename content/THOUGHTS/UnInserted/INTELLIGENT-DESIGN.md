---
name: thought.INTELLIGENT_DESIGN
alias: "Thought: INTELLIGENT DESIGN"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- monalisa
- leonardo
- evolutionists
- pseudoscience
- creationism
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INTELLIGENT_DESIGN",
    alias: "Thought: INTELLIGENT DESIGN",
    parent: "topic.COSMOLOGY",
    tags: ["monalisa", "leonardo", "evolutionists", "pseudoscience", "creationism"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT_DESIGN",
    en_title: "INTELLIGENT DESIGN",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INTELLIGENT_DESIGN" AND c.name = "content.INTELLIGENT_DESIGN"
MERGE (t)-[:HAS_CONTENT {name: "edge.INTELLIGENT_DESIGN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.INTELLIGENT_DESIGN"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->INTELLIGENT_DESIGN"}]->(child);
```