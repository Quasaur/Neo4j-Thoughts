---
title: "Thought: THE ULTIMATE"
draft: false
type: THOUGHT
mling: false
tags:
  - humanity
  - self_worship
  - god
  - judgement
  - accountable
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_ULTIMATE",
    alias: "Thought: THE ULTIMATE",
    parent: "topic.THE-GODHEAD",
    tags: ["humanity", "self_worship", "god", "judgement", "accountable"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE_ULTIMATE",
    en_title: "THE ULTIMATE",
    en_content: "That which is Ultimate cannot be Ultimate unless \"it\" (He) is also PERSONAL.",
    es_title: "LO ÚLTIMO",
    es_content: "Aquello que es Último no puede ser Último a menos que \"eso\" (Él) sea también PERSONAL.",
    fr_title: "L'ULTIME",
    fr_content: "Ce qui est Ultime ne peut pas être Ultime à moins que « cela » (Il) ne soit également PERSONNEL.",
    hi_title: "अंतिम",
    hi_content: "जो परम है वह परम नहीं हो सकता जब तक कि \"वह\" भी व्यक्तिगत न हो।",
    zh_title: "zhōng jí",
    zh_content: "chú fēi “ tā ”（ tā ） yě shì gè rén de ， fǒu zé zhōng jí bù kě néng shì zhōng jí de 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_ULTIMATE" AND c.name = "content.THE_ULTIMATE"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_ULTIMATE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GODHEAD" AND child.name = "thought.THE_ULTIMATE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GODHEAD->THE_ULTIMATE"}]->(child);
```
