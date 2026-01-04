---
name: "thought.DIVINE CONSISTENCY"
alias: "Thought: God is Consistent"
type: THOUGHT
tags:
- divine_character
- consistency
- truth
- divinity
- godhead
en_content: "God is not schizophrenic."
parent: topic.THE-GODHEAD
level: 1
neo4j: true
insert: true
---
# Thought: DIVINE CONSISTENCY
> [!Thought-en]
> God is not schizophrenic.

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.DIVINE CONSISTENCY",
    alias: "Thought: DIVINE CONSISTENCY",
    parent: "topic.THE GODHEAD",
    tags: ["divine_character", "consistency", "truth", "divinity", "godhead"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.DIVINE CONSISTENCY",
    en_title: "DIVINE CONSISTENCY",
    en_content: "God is not schizophrenic.",
    es_title: "CONSISTENCIA DIVINA",
    es_content: "Dios no es esquizofrénico.",
    fr_title: "CONSISTANCE DIVINE",
    fr_content: "Dieu n'est pas schizophrène.",
    hi_title: "ईश्वरीय निरंतरता",
    hi_content: "ईश्वर सिज़ोफ्रेनिक नहीं है।"
    zh_title: "shén dì yī zhì xìng",
    zh_content: "shàng dì bú shì jīng shén fēn liè zhè 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DIVINE CONSISTENCY" AND c.name = "content.DIVINE CONSISTENCY"
MERGE (t)-[:HAS_CONTENT {name: "edge.DIVINE CONSISTENCY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.DIVINE CONSISTENCY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD >DIVINE CONSISTENCY"}]->(child);
```
