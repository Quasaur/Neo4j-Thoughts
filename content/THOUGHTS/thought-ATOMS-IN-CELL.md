---
type: THOUGHT
name: "thought.ATOMS IN CELL"
alias: "Thought: Atoms In Cell"
parent: "topic.BIOLOGY"
en_content: "The average human cell is made of approx. 100 trillion atoms...God is great!"
tags: ["creation", "atoms", "biology", "cell", "majesty"]
ptopic: "[[topic-BIOLOGY]]"
level: 6
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ATOMS IN CELL",
    alias: "Thought: Atoms In Cell",
    parent: "topic.BIOLOGY",
    tags: ['creation', 'atoms', 'biology', 'cell', 'majesty'],
    level: 6
});

CREATE (c:CONTENT {
    name: "content.ATOMS IN CELL",
    ctype: "THOUGHT",
    en_title: "Atoms In Cell",
    en_content: "The average human cell is made of approx. 200 trillion atoms...God is great!",
    es_title: "Átomos en una Célula",
    es_content: "La célula humana promedio está compuesta por aprox. 200 billones de átomos... ¡Dios es grande!",
    fr_title: "Atomes dans une Cellule",
    fr_content: "La cellule humaine moyenne est composée d'environ 200 trillions d'atomes... Dieu est grand !",
    hi_title: "कोशिका में परमाणु",
    hi_content: "औसत मानव कोशिका लगभग 200 ट्रिलियन परमाणुओं से बनी होती है... परमेश्वर महान है!",
    zh_title: "Xìbāo zhōng yuánzǐ",
    zh_content: "Píngjūn měi gè rénlèi xìbāo yóu dàyuē èrbǎi wànyì gè yuánzǐ zǔchéng... shén shì wěidà de!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ATOMS IN CELL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->ATOMS IN CELL"
RETURN t, parent;
```
