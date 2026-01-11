---
name: "thought.ATOMS IN CELL"
alias: "Thought: Atoms In Cell"
type: THOUGHT
en_content: "The average human cell is made of approx. 200 trillion atoms...God is great!"
parent: "topic.CREATION"
tags:
- creation
- atoms
- biology
- science
- majesty
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.ATOMS IN CELL",
    alias: "Thought: Atoms In Cell",
    parent: "topic.CREATION",
    tags: ['creation', 'atoms', 'biology', 'science', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ATOMS IN CELL",
    en_title: "Atoms In Cell",
    en_content: "The average human cell is made of approx. 200 trillion atoms...God is great!",
    es_title: "Átomos en una Célula",
    es_content: "La célula humana promedio está compuesta por aprox. 200 billones de átomos... ¡Dios es grande!",
    fr_title: "Atomes dans une Cellule",
    fr_content: "La cellule humaine moyenne est composée d'environ 200 trillions d'atomes... Dieu est grand !",
    hi_title: "कोशिका में परमाणु",
    hi_content: "औसत मानव कोशिका लगभग 200 ट्रिलियन परमाणुओं से बनी होती है... परमेश्वर महान है!",
    zh_title: "细胞中的原子",
    zh_content: "平均每个人类细胞由大约200万亿个原子组成...神是伟大的！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ATOMS IN CELL" AND c.name = "content.ATOMS IN CELL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATOMS IN CELL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.ATOMS IN CELL"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >ATOMS IN CELL" }]->(child);
```
