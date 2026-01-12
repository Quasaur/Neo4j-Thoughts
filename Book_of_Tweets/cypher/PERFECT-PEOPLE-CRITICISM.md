---
name: "thought.PERFECT PEOPLE CRITICISM"
alias: "Thought: Perfect People Criticism"
type: THOUGHT
en_content: Have you ever noticed that perfect people don't respond well to criticism?
parent: topic.ATTITUDE
tags:
  - perfection
  - criticism
  - response
  - attitude
  - character
level: 3
neo4j: false
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2013a)
CREATE (t:THOUGHT {
    name: "thought.PERFECT PEOPLE CRITICISM",
    alias: "Thought: Perfect People Criticism",
    parent: "topic.ATTITUDE",
    tags: ['perfection', 'criticism', 'response', 'attitude', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PERFECT PEOPLE CRITICISM",
    en_title: "Perfect People Criticism",
    en_content: "Have you ever noticed that perfect people don't respond well to criticism?",
    es_title: "Crítica a las Personas Perfectas",
    es_content: "¿Alguna vez has notado que las personas perfectas no responden bien a las críticas?",
    fr_title: "Critique des Personnes Parfaites",
    fr_content: "Avez-vous déjà remarqué que les personnes parfaites ne répondent pas bien aux critiques ?",
    hi_title: "पूर्ण लोगों की आलोचना",
    hi_content: "क्या आपने कभी देखा है कि पूर्ण लोग आलोचना का अच्छा जवाब नहीं देते?",
    zh_title: "Wanmei de Ren de Piping",
    zh_content: "Ni you mei you zhuyi dao wanmei de ren dui piping fan ying bu hao?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PERFECT PEOPLE CRITICISM" AND c.name = "content.PERFECT PEOPLE CRITICISM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PERFECT PEOPLE CRITICISM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.PERFECT PEOPLE CRITICISM"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >PERFECT PEOPLE CRITICISM" }]->(child);
```
