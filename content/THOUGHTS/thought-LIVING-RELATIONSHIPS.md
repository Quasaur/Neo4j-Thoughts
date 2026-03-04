---
type: THOUGHT
name: "thought.LIVING RELATIONSHIPS"
alias: "Thought: Living Relationship"
parent: "topic.PSYCHOLOGY"
en_content: "Life is all about relationships."
tags: ["live", "relationships", "people", "jesus_christ", "god"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LIVING RELATIONSHIPS",
    alias: "Thought: Living Relationship",
    parent: "topic.PSYCHOLOGY",
    tags: ["live", "relationships", "people", "jesus_christ", "god"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LIVING RELATIONSHIPS",
    ctype: "THOUGHT",
    en_title: "Living Relationship",
    en_content: "Life is all about relationships.",
    es_title: "RELACIÓN DE VIDA",
    es_content: "La vida se trata de relaciones.",
    fr_title: "RELATION VIVANTE",
    fr_content: "La vie est une question de relations.",
    hi_title: "जीवित संबंध",
    hi_content: "जीवन रिश्तों के बारे में है।",
    zh_title: "shēng huó guān xì",
    zh_content: "shēng huó jiù shì guān xì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIVING RELATIONSHIPS" AND c.name = "content.LIVING RELATIONSHIPS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.LIVING RELATIONSHIPS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.LIVING RELATIONSHIPS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->LIVING RELATIONSHIPS"}]->(child);
```
