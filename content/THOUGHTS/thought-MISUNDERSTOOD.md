---
type: THOUGHT
name: "thought.MISUNDERSTOOD"
alias: "Thought: Misunderstood"
parent: "topic.UNDERSTANDING"
tags: ["misunderfstood", "understanding", "communication", "fellowship", "intimacy"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MISUNDERSTOOD",
    alias: "Thought: Misunderstood",
    parent: "topic.UNDERSTANDING",
    tags: ["misunderfstood", "understanding", "communication", "fellowship", "intimacy"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MISUNDERSTOOD",
    ctype: "THOUGHT",
    en_title: "Misunderstood",
 es_title: "INCOMPRENDIDO",
 fr_title: "MAL COMPRIS",
 hi_title: "गलत समझा",
 zh_title: "bèi wù jiě",
    en_content: "",
 es_content: "Una de las mayores agonías de la vida es la de ser incomprendido.",
 fr_content: "L'une des plus grandes souffrances de la vie est celle d'être mal comprise.",
 hi_content: "जीवन की सबसे बड़ी पीड़ाओं में से एक है गलत समझा जाना।",
 zh_content: "rén shēng zuì dà de tòng kǔ zhī yī jiù shì bèi wù jiě 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MISUNDERSTOOD" AND c.name = "content.MISUNDERSTOOD"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.MISUNDERSTOOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "thought.MISUNDERSTOOD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.UNDERSTANDING->MISUNDERSTOOD"}]->(child);
```