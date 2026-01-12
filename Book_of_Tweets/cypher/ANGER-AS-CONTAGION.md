---
name: thought.ANGER AS CONTAGION
alias: "Thought: Anger As Contagion"
type: THOUGHT
en_content: Anger is a contagion that easily leaps from soul to soul where there is an absence of reason.
parent: topic.ATTITUDE
tags:
  - anger
  - reason
  - soul
  - attitude
  - character
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2012a)
CREATE (t:THOUGHT {
    name: "thought.ANGER AS CONTAGION",
    alias: "Thought: Anger As Contagion",
    parent: "topic.ATTITUDE",
    tags: ['anger', 'reason', 'soul', 'attitude', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ANGER AS CONTAGION",
    en_title: "Anger As Contagion",
    en_content: "Anger is a contagion that easily leaps from soul to soul where there is an absence of reason.",
    es_title: "La Ira como Contagio",
    es_content: "La ira es un contagio que salta fácilmente de alma en alma donde hay ausencia de razón.",
    fr_title: "La Colère comme Contagion",
    fr_content: "La colère est une contagion qui saute facilement d'âme en âme là où la raison est absente.",
    hi_title: "संक्रमण के रूप में क्रोध",
    hi_content: "क्रोध एक संक्रमण है जो आसानी से एक आत्मा से दूसरी आत्मा में कूद जाता है जहां तर्क की अनुपस्थिति होती है।",
    zh_title: "愤怒如同传染病",
    zh_content: "愤怒是一种传染病，在缺乏理性的地方很容易从一个灵魂跳到另一个灵魂。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANGER AS CONTAGION" AND c.name = "content.ANGER AS CONTAGION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ANGER AS CONTAGION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ANGER AS CONTAGION"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >ANGER AS CONTAGION" }]->(child);
```
