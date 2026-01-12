---
name: "thought.NO ANGER SELFLESSNESS"
alias: "Thought: No Anger Selflessness"
type: THOUGHT
en_content: There is no anger in selflessness.
parent: topic.ATTITUDE
tags:
  - selflessness
  - anger
  - attitude
  - peace
  - character
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.NO ANGER SELFLESSNESS",
    alias: "Thought: No Anger Selflessness",
    parent: "topic.ATTITUDE",
    tags: ['selflessness', 'anger', 'attitude', 'peace', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NO ANGER SELFLESSNESS",
    en_title: "No Anger Selflessness",
    en_content: "There is no anger in selflessness.",
    es_title: "No Hay Ira en el Desinterés",
    es_content: "No hay ira en el desinterés.",
    fr_title: "Pas de Colère dans le Désintéressement",
    fr_content: "Il n'y a pas de colère dans le désintéressement.",
    hi_title: "निःस्वार्थता में कोई क्रोध नहीं",
    hi_content: "निःस्वार्थता में कोई क्रोध नहीं होता।",
    zh_title: "Wú sī zhōng méiyǒu fènnù 无私中没有愤怒",
    zh_content: "Wú sī zhōng méiyǒu fènnù. 无私中没有愤怒。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NO ANGER SELFLESSNESS" AND c.name = "content.NO ANGER SELFLESSNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NO ANGER SELFLESSNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.NO ANGER SELFLESSNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >NO ANGER SELFLESSNESS" }]->(child);
```
