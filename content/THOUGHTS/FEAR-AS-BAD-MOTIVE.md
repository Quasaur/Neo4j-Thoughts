---
name: "thought.FEAR AS BAD MOTIVE"
alias: "Thought: Fear As Bad Motive"
type: THOUGHT
en_content: Fear is rarely a good motive for any action.
parent: topic.ATTITUDE
tags:
  - fear
  - motive
  - action
  - attitude
  - character
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.FEAR AS BAD MOTIVE",
    alias: "Thought: Fear As Bad Motive",
    parent: "topic.ATTITUDE",
    tags: ['fear', 'motive', 'action', 'attitude', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FEAR AS BAD MOTIVE",
    en_title: "Fear As Bad Motive",
    en_content: "Fear is rarely a good motive for any action.",
    es_title: "El Miedo Como Mal Motivo",
    es_content: "El miedo rara vez es un buen motivo para cualquier acción.",
    fr_title: "La Peur Comme Mauvaise Motivation",
    fr_content: "La peur est rarement une bonne motivation pour toute action.",
    hi_title: "बुरी प्रेरणा के रूप में भय",
    hi_content: "भय शायद ही कभी किसी भी कार्य के लिए एक अच्छी प्रेरणा होता है।",
    zh_title: "Kǒngjù Zuòwéi Bùliáng Dòngjī",
    zh_content: "Kǒngjù hěn shǎo shì rènhé xíngdòng de hǎo dòngjī."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FEAR AS BAD MOTIVE" AND c.name = "content.FEAR AS BAD MOTIVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FEAR AS BAD MOTIVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.FEAR AS BAD MOTIVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->FEAR AS BAD MOTIVE" }]->(child);
```
