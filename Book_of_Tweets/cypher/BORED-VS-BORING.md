---
name: "thought.BORED VS BORING"
alias: "Thought: Bored Vs Boring"
type: THOUGHT
en_content: Better to be bored than to be boring.
parent: topic.ATTITUDE
tags:
  - boredom
  - personality
  - attitude
  - character
  - irony
level: 3
neo4j: false
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.BORED VS BORING",
    alias: "Thought: Bored Vs Boring",
    parent: "topic.ATTITUDE",
    tags: ['boredom', 'personality', 'attitude', 'character', 'irony'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BORED VS BORING",
    en_title: "Bored Vs Boring",
    en_content: "Better to be bored than to be boring.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BORED VS BORING" AND c.name = "content.BORED VS BORING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BORED VS BORING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.BORED VS BORING"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >BORED VS BORING" }]->(child);
```
