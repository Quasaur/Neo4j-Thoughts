---
name: "thought.TERRIBLE SECRETS"
alias: "Thought: Terrible Secrets"
type: THOUGHT
en_content: Secrets can be terrible things.
parent: topic.PSYCHOLOGY
tags:
  - secrets
  - fear
  - character
  - attitude
  - truth
level: 3
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Mar-2012c)
CREATE (t:THOUGHT {
    name: "thought.TERRIBLE SECRETS",
    alias: "Thought: Terrible Secrets",
    parent: "topic.ATTITUDE",
    tags: ['secrets', 'fear', 'character', 'attitude', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TERRIBLE SECRETS",
    en_title: "Terrible Secrets",
    en_content: "Secrets can be terrible things.",
    es_title: "Secretos Terribles",
    es_content: "Los secretos pueden ser cosas terribles.",
    fr_title: "Secrets Terribles",
    fr_content: "Les secrets peuvent être des choses terribles.",
    hi_title: "भयानक रहस्य",
    hi_content: "रहस्य भयानक चीज़ें हो सकते हैं।",
    zh_title: "kě pà de mì mì",
    zh_content: "mì mì kě néng shì kě pà de shì qíng."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TERRIBLE SECRETS" AND c.name = "content.TERRIBLE SECRETS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TERRIBLE SECRETS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.TERRIBLE SECRETS"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->TERRIBLE SECRETS" }]->(child);
```
