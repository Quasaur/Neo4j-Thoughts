---
type: THOUGHT
name: "thought.ACCOUNTABILITY"
alias: "Thought: Accountability"
parent: "topic.HUMANITY"
en_content: "The idea of God introduces the concept of accountability."
tags: ["god", "lord", "judgment", "accountable", "responsible"]
ptopic: "[[topic-HUMANITY]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ACCOUNTABILITY",
    alias: "Thought: Accountability",
    parent: "topic.HUMANITY",
    tags: ["god", "lord", "judgment", "accountable", "responsible"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ACCOUNTABILITY",
    ctype: "THOUGHT",
    en_title: "Accountability",
    en_content: "The idea of God introduces the concept of accountability.",
    es_title: "Responsabilidad",
    es_content: "Dios no te libra de las consecuencias de mis acciones.",
    fr_title: "Responsabilité",
    fr_content: "Dieu ne t'épargne pas les conséquences de mes actions.",
    hi_title: "जवाबदेही",
    hi_content: "भगवान आपको मेरे कार्यों के परिणामों से नहीं बचाते।",
    zh_title: "问责制",
    zh_content: "上帝不会让你免受我行为的后果。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACCOUNTABILITY" AND c.name = "content.ACCOUNTABILITY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ACCOUNTABILITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.ACCOUNTABILITY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HUMANITY->ACCOUNTABILITY"}]->(child);
```