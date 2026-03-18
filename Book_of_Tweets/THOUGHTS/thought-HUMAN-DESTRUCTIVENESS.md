---
type: THOUGHT
name: "thought.HUMAN DESTRUCTIVENESS"
alias: "Thought: Human Nature"
parent: "topic.HUMANITY"
en_content: "BP Oil Spill: we humans are amazingly self-destructive."
tags: ["human_nature", "destruction", "environment", "self_harm", "awareness"]
ptopic:
level: 3
neo4j: false
---

```Cypher
CREATE (t:THOUGHT {    name: "thought.HUMAN DESTRUCTIVENESS",
    alias: "Thought: Human Nature",
    parent: "topic.HUMANITY",
    tags: ["human_nature", "destruction", "environment", "self_harm", "awareness"],
    level: 3});

CREATE (c:CONTENT {
    name: "content.HUMAN DESTRUCTIVENESS",
    ctype: "THOUGHT",
    en_title: "Self Destructive Humans",
    en_content: "BP Oil Spill: we humans are amazingly self-destructive.",
    es_title: "Humanos autodestructivos",
    es_content: "Derrame de petróleo de BP: nosotros los humanos somos increíblemente autodestructivos.",
    fr_title: "Humains autodestructeurs",
    fr_content: "Marée noire de BP : nous, les humains, sommes étonnamment autodestructeurs.",
    hi_title: "aatmanaashee maanava",
    hi_content: "बीपी तेल रिसाव: हम इंसान आश्चर्यजनक रूप से आत्मघाती हैं।",
    zh_title: "zì wǒ huǐ miè",
    zh_content: "BP shí yóu xiè lòu : wǒ men rén lèi jīng rén de zì wǒ huǐ miè."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HUMAN DESTRUCTIVENESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->HUMAN DESTRUCTIVENESS"
RETURN t, parent;
```
