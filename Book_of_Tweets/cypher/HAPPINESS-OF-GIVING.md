---
name: "thought.HAPPINESS OF GIVING"
alias: "Thought: Happiness Of Giving"
type: THOUGHT
en_content: "God is happier than everyone else because He gives more than anyone else."
parent: "topic.THE GODHEAD"
tags:
- giving
- happiness
- god
- character
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Nov-2011b)
CREATE (t:THOUGHT {
    name: "thought.HAPPINESS OF GIVING",
    alias: "Thought: Happiness Of Giving",
    parent: "topic.THE GODHEAD",
    tags: ['giving', 'happiness', 'god', 'character', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.HAPPINESS OF GIVING",
    en_title: "Happiness Of Giving",
    en_content: "God is happier than everyone else because He gives more than anyone else.",
    es_title: "La Felicidad de Dar",
    es_content: "Dios es más feliz que todos los demás porque Él da más que cualquier otro.",
    fr_title: "Le Bonheur de Donner",
    fr_content: "Dieu est plus heureux que tous les autres parce qu'Il donne plus que quiconque.",
    hi_title: "देने की खुशी",
    hi_content: "परमेश्वर सबसे अधिक खुश है क्योंकि वह सबसे अधिक देता है।",
    zh_title: "Gěi Yǔ De Kuài Lè",
    zh_content: "Shàng Dì bǐ qí tā rèn hé rén dōu gèng kuài lè, yīn wèi Tā bǐ rèn hé rén dōu gěi de gèng duō."
});

MATCH (t:THOUGHT {name: "thought.HAPPINESS OF GIVING"})
MATCH (c:CONTENT {name: "content.HAPPINESS OF GIVING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.HAPPINESS OF GIVING" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.HAPPINESS OF GIVING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >HAPPINESS OF GIVING" }]->(child);
```
