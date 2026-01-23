---
name: "thought.QUALIFIED TO BREAK"
alias: "Thought: Qualified To Break"
type: THOUGHT
en_content: "The only Person qualified to break me is The One Who has demonstrated Their LOVE for me."
parent: "topic.THE GODHEAD"
tags:
- love
- surrender
- character
- god
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.QUALIFIED TO BREAK",
    alias: "Thought: Qualified To Break",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'surrender', 'character', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.QUALIFIED TO BREAK",
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

MATCH (t:THOUGHT {name: "thought.QUALIFIED TO BREAK"})
MATCH (c:CONTENT {name: "content.QUALIFIED TO BREAK"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.QUALIFIED TO BREAK" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.QUALIFIED TO BREAK"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >QUALIFIED TO BREAK" }]->(child);
```
