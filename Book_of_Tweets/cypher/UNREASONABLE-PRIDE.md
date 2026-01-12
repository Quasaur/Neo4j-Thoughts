---
name: "thought.UNREASONABLE PRIDE"
alias: "Thought: Unreasonable Pride"
type: THOUGHT
en_content: Self Pride is always unreasonable.
parent: topic.EVIL
tags:
  - pride
  - attitude
  - reason
  - character
  - arrogance
level: 3
neo4j: true
ptopic: "[[topic-EVIL]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Dec-2011c)
CREATE (t:THOUGHT {
    name: "thought.UNREASONABLE PRIDE",
    alias: "Thought: Unreasonable Pride",
    parent: "topic.ATTITUDE",
    tags: ['pride', 'attitude', 'reason', 'character', 'arrogance'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNREASONABLE PRIDE",
    en_title: "Unreasonable Pride",
    en_content: "Self Pride is always unreasonable.",
    es_title: "Orgullo Irrazonable",
    es_content: "El orgullo propio siempre es irrazonable.",
    fr_title: "Orgueil Déraisonnable",
    fr_content: "L'orgueil de soi est toujours déraisonnable.",
    hi_title: "अनुचित गर्व",
    hi_content: "स्वयं का गर्व हमेशा अनुचित होता है।",
    zh_title: "Bu He Li De Jiao Ao",
    zh_content: "Zi Wo Jiao Ao Zong Shi Bu He Li De."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNREASONABLE PRIDE" AND c.name = "content.UNREASONABLE PRIDE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNREASONABLE PRIDE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.UNREASONABLE PRIDE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >UNREASONABLE PRIDE" }]->(child);
```
