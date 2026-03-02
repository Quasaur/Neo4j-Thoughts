---
type: THOUGHT
name: "thought.FAIRNESS"
alias: "Thought: FAIRNESS"
parent: "topic.JUSTICE"
tags: ["justice", "fairness", "mercy", "forgiveness", "compassion"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FAIRNESS",
    alias: "Thought: FAIRNESS",
    parent: "topic.JUSTICE",
    tags: ["justice", "fairness", "mercy", "forgiveness", "compassion"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FAIRNESS",
    ctype: "THOUGHT",
    en_title: "FAIRNESS",
 es_title: "JUSTICIA",
 fr_title: "JUSTICE",
 hi_title: "फेयरनेस",
 zh_title: "gōng píng xìng",
    en_content: "",
 es_content: "La misericordia nunca es justa.",
 fr_content: "La miséricorde n'est jamais juste.",
 hi_content: "दया कभी भी उचित नहीं होती.",
 zh_content: "lián mǐn cóng lái dōu bú shì gōng píng de 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FAIRNESS" AND c.name = "content.FAIRNESS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FAIRNESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.FAIRNESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.JUSTICE->FAIRNESS"}]->(child);
```