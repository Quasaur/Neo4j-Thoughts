---
name: thought.AWESOME GOD
alias: "Thought: Divine Majesty"
parent: topic.THE GODHEAD
tags:
  - divine_majesty
  - holiness
  - awe_wonder
  - worship
  - gods_children
level: 1
neo4j: true
insert: true
type: THOUGHT
---
# Awesome God

> [!Thought-en]
> To His children God is AWESOME.

```Cypher
CREATE (t:THOUGHT {
    name: "thought.AWESOME GOD",
    alias: "Thought: Divine Majesty",
    parent: "topic.THE GODHEAD",
    tags: ["divine_majesty", "holiness", "awe_wonder", "worship", "gods_children"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.AWESOME GOD",
    en_title: "Awesome God",
    en_content: "To His children God is AWESOME.",
    es_title: "Dios es asombroso",
    es_content: "Para Sus hijos, Dios es ASOMBROSO.",
    fr_title: "Dieu est génial",
    fr_content: "Pour Ses enfants, Dieu est GÉNIAL.",
    hi_title: "bhagavaan adbhut hai",
    hi_content: "अपने बच्चों के लिए भगवान अद्भुत है।",
    zh_title: "lìng rén jìng wèi",
    zh_content: "duì tā de ér nǚ lái shuō, shàng dì shì lìng rén jìng wèi de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AWESOME GOD" AND c.name = "content.AWESOME GOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.AWESOME GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.AWESOME GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD >AWESOME GOD"}]->(child);
```
