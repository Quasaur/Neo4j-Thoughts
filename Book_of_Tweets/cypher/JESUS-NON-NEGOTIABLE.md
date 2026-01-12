---
name: "thought.JESUS NON NEGOTIABLE"
alias: "Thought: Jesus Non Negotiable"
type: THOUGHT
en_content: "I must have Jesus...everything else is negotiable."
parent: "topic.SPIRITUALITY"
tags:
- jesus
- priority
- spirituality
- commitment
- devotion
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.JESUS NON NEGOTIABLE",
    alias: "Thought: Jesus Non Negotiable",
    parent: "topic.SPIRITUALITY",
    tags: ['jesus', 'priority', 'spirituality', 'commitment', 'devotion'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.JESUS NON NEGOTIABLE",
    en_title: "Jesus Non Negotiable",
    en_content: "I must have Jesus...everything else is negotiable.",
    es_title: "Jesús No Negociable",
    es_content: "Debo tener a Jesús...todo lo demás es negociable.",
    fr_title: "Jésus Non Négociable",
    fr_content: "Je dois avoir Jésus...tout le reste est négociable.",
    hi_title: "यीशु अपरिवर्तनीय",
    hi_content: "मुझे यीशु चाहिए...बाकी सब कुछ परिवर्तनीय है।",
    zh_title: "Yesu Buke Tanpan",
    zh_content: "Wo bixu yongyou Yesu...qita yiqie dou keyi tanpan."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.JESUS NON NEGOTIABLE" AND c.name = "content.JESUS NON NEGOTIABLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JESUS NON NEGOTIABLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.JESUS NON NEGOTIABLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >JESUS NON NEGOTIABLE" }]->(child);
```
