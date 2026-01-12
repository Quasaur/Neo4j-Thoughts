---
name: "thought.SIMPLE AND DEEP"
alias: "Thought: Simple And Deep"
type: THOUGHT
en_content: "The simplest things are the most deep; the deepest things are the most simple."
parent: "topic.WISDOM"
tags:
- wisdom
- simplicity
- depth
- truth
- philosophy
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.SIMPLE AND DEEP",
    alias: "Thought: Simple And Deep",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'simplicity', 'depth', 'truth', 'philosophy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIMPLE AND DEEP",
    en_title: "Simple And Deep",
    en_content: "The simplest things are the most deep; the deepest things are the most simple.",
    es_title: "Simple y Profundo",
    es_content: "Las cosas más simples son las más profundas; las cosas más profundas son las más simples.",
    fr_title: "Simple et Profond",
    fr_content: "Les choses les plus simples sont les plus profondes ; les choses les plus profondes sont les plus simples.",
    hi_title: "सरल और गहरा",
    hi_content: "सबसे सरल बातें सबसे गहरी होती हैं; सबसे गहरी बातें सबसे सरल होती हैं।",
    zh_title: "Jiǎn Dān Ér Shēn Kè",
    zh_content: "Zuì jiǎn dān de shì qíng shì zuì shēn kè de; zuì shēn kè de shì qíng shì zuì jiǎn dān de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SIMPLE AND DEEP" AND c.name = "content.SIMPLE AND DEEP"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIMPLE AND DEEP" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.SIMPLE AND DEEP"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >SIMPLE AND DEEP" }]->(child);
```
