---
name: "thought.SPIRIT VS MATTER"
alias: "Thought: Spirit Vs Matter"
type: THOUGHT
en_content: "SPIRIT is far older, stronger and eternally more powerful than matter."
parent: "topic.PHILOSOPHY"
tags:
- spirit
- matter
- eternity
- philosophy
- power
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2011d)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT VS MATTER",
    alias: "Thought: Spirit Vs Matter",
    parent: "topic.PHILOSOPHY",
    tags: ['spirit', 'matter', 'eternity', 'philosophy', 'power'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SPIRIT VS MATTER",
    en_title: "Spirit Vs Matter",
    en_content: "SPIRIT is far older, stronger and eternally more powerful than matter.",
    es_title: "Espíritu Vs Materia",
    es_content: "El ESPÍRITU es mucho más antiguo, más fuerte y eternamente más poderoso que la materia.",
    fr_title: "Esprit Vs Matière",
    fr_content: "L'ESPRIT est bien plus ancien, plus fort et éternellement plus puissant que la matière.",
    hi_title: "आत्मा बनाम पदार्थ",
    hi_content: "आत्मा पदार्थ से कहीं अधिक पुरानी, मजबूत और अनन्त रूप से अधिक शक्तिशाली है।",
    zh_title: "Ling Hun Dui Wu Zhi",
    zh_content: "LING HUN bi wu zhi geng jiu yuan, geng qiang da, bing qie yong heng de geng you li liang."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SPIRIT VS MATTER" AND c.name = "content.SPIRIT VS MATTER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPIRIT VS MATTER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.SPIRIT VS MATTER"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >SPIRIT VS MATTER" }]->(child);
```
