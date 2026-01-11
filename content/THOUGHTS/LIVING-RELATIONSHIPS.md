---
name: "thought.LIVING_RELATIONSHIPS"
alias: "Thought: LIVING RELATIONSHIP"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- live
- relationships
- people
- jesuschrist
- god
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LIVING_RELATIONSHIPS",
    alias: "Thought: LIVING RELATIONSHIP",
    parent: "topic.PSYCHOLOGY",
    tags: ["live", "relationships", "people", "jesuschrist", "god"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LIVING_RELATIONSHIPS",
    en_title: "LIVING RELATIONSHIP",
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
WHERE t.name = "thought.LIVING_RELATIONSHIPS" AND c.name = "content.LIVING_RELATIONSHIPS"
MERGE (t)-[:HAS_CONTENT {name: "edge.LIVING_RELATIONSHIPS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.LIVING_RELATIONSHIPS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->LIVING_RELATIONSHIPS"}]->(child);
```
