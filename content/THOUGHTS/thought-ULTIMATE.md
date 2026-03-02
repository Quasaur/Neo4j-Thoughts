---
type: THOUGHT
name: "thought.ULTIMATE"
alias: "Thought: THE ULTIMATE"
parent: "topic.THE GODHEAD"
en_content: "That which is Ultimate cannot be Ultimate unless \"it\" (He) is also PERSONAL."
tags: ["humanity", "self_worship", "god", "judgement", "accountable"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ULTIMATE",
    alias: "Thought: THE ULTIMATE",
    parent: "topic.THE GODHEAD",
    tags: ["humanity", "self_worship", "god", "judgement", "accountable"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ULTIMATE",
    ctype: "THOUGHT",
    en_title: "ULTIMATE",
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
WHERE t.name = "thought.ULTIMATE" AND c.name = "content.ULTIMATE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ULTIMATE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ULTIMATE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->ULTIMATE"}]->(child);
```
