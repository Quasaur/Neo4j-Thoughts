---
name: "thought.HUMAN DESTRUCTIVENESS"
alias: "Thought: Human Nature"
type: THOUGHT
en_content: "BP Oil Spill: we humans are amazingly self-destructive."
parent: "topic.HUMANITY"
tags:
- human_nature
- destruction
- environment
- self_harm
- awareness
level: 3
neo4j: false
ptopic: 
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMAN DESTRUCTIVENESS",
    alias: "Thought: Human Nature",
    parent: "topic.HUMANITY",
    tags: ["human_nature", "destruction", "environment", "self_harm", "awareness"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMAN DESTRUCTIVENESS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN DESTRUCTIVENESS" AND c.name = "content.HUMAN DESTRUCTIVENESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.HUMAN DESTRUCTIVENESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.HUMAN DESTRUCTIVENESS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMANITY >HUMAN DESTRUCTIVENESS"}]->(child);
```
