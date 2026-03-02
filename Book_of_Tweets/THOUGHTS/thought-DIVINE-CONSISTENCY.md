---
type: THOUGHT
name: "thought.DIVINE CONSISTENCY"
alias: "Thought: God is Consistent"
parent: "topic.THE-GODHEAD"
en_content: "God is not schizophrenic."
tags: ["divine_character", "consistency", "truth", "divinity", "godhead"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {    name: "thought.DIVINE CONSISTENCY",
    alias: "Thought: DIVINE CONSISTENCY",
    parent: "topic.THE GODHEAD",
    tags: ["divine_character", "consistency", "truth", "divinity", "godhead"],
    level: 1});

CREATE (c:CONTENT {
    name: "content.DIVINE CONSISTENCY",
    ctype: "THOUGHT",
    en_title: "DIVINE CONSISTENCY",
    en_content: "God is not schizophrenic.",
    es_title: "CONSISTENCIA DIVINA",
    es_content: "Dios no es esquizofrénico.",
    fr_title: "CONSISTANCE DIVINE",
    fr_content: "Dieu n'est pas schizophrène.",
    hi_title: "ईश्वरीय निरंतरता",
    hi_content: "ईश्वर सिज़ोफ्रेनिक नहीं है।"
    zh_title: "Shén de yīzhìxìng",
    zh_content: "shàng dì bú shì jīng shén fēn liè zhè 。"
});

MATCH (t:THOUGHT {name: "thought.DIVINE CONSISTENCY"})
MATCH (c:CONTENT {name: "content.DIVINE CONSISTENCY"})
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DIVINE CONSISTENCY"}]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.DIVINE CONSISTENCY"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->DIVINE CONSISTENCY"}]->(child);
```
