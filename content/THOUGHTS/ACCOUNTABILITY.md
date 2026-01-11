---
name: thought.ACCOUNTABILITY
alias: "Thought: ACCOUNTABILITY"
type: THOUGHT
parent: topic.HUMANITY
tags:
- god
- lord
- judgment
- accountable
- responsible
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ACCOUNTABILITY",
    alias: "Thought: ACCOUNTABILITY",
    parent: "topic.HUMANITY",
    tags: ["god", "lord", "judgment", "accountable", "responsible"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ACCOUNTABILITY",
    en_title: "ACCOUNTABILITY",
    en_content: "The idea of God introduces the concept of accountability.",
    es_title: "RESPONSABILIDAD",
    es_content: "La idea de Dios introduce el concepto de responsabilidad.",
    fr_title: "RESPONSABILITÉ",
    fr_content: "L'idée de Dieu introduit le concept de responsabilité.",
    hi_title: "जवाबदेही",
    hi_content: "ईश्वर का विचार जवाबदेही की अवधारणा का परिचय देता है।",
    zh_title: "zé rèn",
    zh_content: "shàng dì de guān niàn yǐn rù le zé rèn de gài niàn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACCOUNTABILITY" AND c.name = "content.ACCOUNTABILITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.ACCOUNTABILITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.ACCOUNTABILITY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMANITY->ACCOUNTABILITY"}]->(child);
```