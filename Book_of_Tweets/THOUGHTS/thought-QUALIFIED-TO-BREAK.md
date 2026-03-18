---
type: THOUGHT
name: "thought.QUALIFIED TO BREAK"
alias: "Thought: Qualified To Break"
parent: "topic.THE GODHEAD"
en_content: "The only Person qualified to break me is The One Who has demonstrated Their LOVE for me."
tags: ["love", "surrender", "character", "god", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2012c)
CREATE (t:THOUGHT {    name: "thought.QUALIFIED TO BREAK",
    alias: "Thought: Qualified To Break",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'surrender', 'character', 'god', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.QUALIFIED TO BREAK",
    ctype: "THOUGHT",
    en_title: "Qualified To Break",
    en_content: "The only Person qualified to break me is The One Who has demonstrated Their LOVE for me.",
    es_title: "Calificado Para Quebrantar",
    es_content: "La única Persona calificada para quebrantarme es Aquella que ha demostrado Su AMOR por mí.",
    fr_title: "Qualifié Pour Briser",
    fr_content: "La seule Personne qualifiée pour me briser est Celle qui a démontré Son AMOUR pour moi.",
    hi_title: "तोड़ने के लिए योग्य",
    hi_content: "मुझे तोड़ने के लिए योग्य एकमात्र व्यक्ति वह है जिसने मेरे लिए अपना प्रेम प्रदर्शित किया है।",
    zh_title: "You Zi Ge Da Po",
    zh_content: "Wei yi you zi ge da po wo de Na Wei, shi yi jing xiang wo zheng ming le Ta de AI de Na Yi Wei."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.QUALIFIED TO BREAK"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->QUALIFIED TO BREAK"
RETURN t, parent;
```
