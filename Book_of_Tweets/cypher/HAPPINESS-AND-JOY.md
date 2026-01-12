---
name: "thought.HAPPINESS AND JOY"
alias: "Thought: Happiness And Joy"
type: THOUGHT
en_content: "Happiness: pleasing God. Joy: being pleased by God."
parent: "topic.SPIRITUALITY"
tags:
- happiness
- joy
- spirituality
- obedience
- blessing
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2010a)
CREATE (t:THOUGHT {
    name: "thought.HAPPINESS AND JOY",
    alias: "Thought: Happiness And Joy",
    parent: "topic.SPIRITUALITY",
    tags: ['happiness', 'joy', 'spirituality', 'obedience', 'blessing'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HAPPINESS AND JOY",
    en_title: "Happiness And Joy",
    en_content: "Happiness: pleasing God. Joy: being pleased by God.",
    es_title: "Felicidad y alegría",
    es_content: "Felicidad: agradar a Dios.Alegría: agradarse a Dios.",
    fr_title: "Bonheur et joie",
    fr_content: "Bonheur : plaire à Dieu.Joie : être satisfait de Dieu.",
    hi_title: "खुशी और मस्ती",
    hi_content: "ख़ुशी: भगवान को प्रसन्न करना.ख़ुशी: भगवान से प्रसन्न होना।",
    zh_title: "幸福与快乐",
    zh_content: "幸福：讨神喜悦。喜乐：蒙神喜悦。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HAPPINESS AND JOY" AND c.name = "content.HAPPINESS AND JOY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HAPPINESS AND JOY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HAPPINESS AND JOY"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HAPPINESS AND JOY" }]->(child);
```
