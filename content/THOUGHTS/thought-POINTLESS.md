---
type: THOUGHT
name: "thought.POINTLESS"
alias: "Thought: POINTLESS"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["pointless", "purpose", "meaning", "god", "sovereignty"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.POINTLESS",
    alias: "Thought: POINTLESS",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["pointless", "purpose", "meaning", "god", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.POINTLESS",
    ctype: "THOUGHT",
    en_title: "POINTLESS",
 es_title: "INÚTIL",
 fr_title: "INUTILE",
 hi_title: "व्यर्थ",
 zh_title: "wú yì yì",
    en_content: "",
 es_content: "Una vida sin Dios es verdaderamente inútil.",
 fr_content: "Une vie sans Dieu est vraiment inutile.",
 hi_content: "ईश्वर-विहीन जीवन वास्तव में व्यर्थ है।",
 zh_content: "méi yǒu shén de shēng huó què shí háo wú yì yì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.POINTLESS" AND c.name = "content.POINTLESS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.POINTLESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.POINTLESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->POINTLESS"}]->(child);
```