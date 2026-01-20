---
name: thought.ATOMS IN CELL
alias: "Thought: Atoms In Cell"
type: THOUGHT
en_content: The average human cell is made of approx. 100 trillion atoms...God is great!
parent: topic.BIOLOGY
tags:
  - creation
  - atoms
  - biology
  - cell
  - majesty
level: 6
neo4j: false
ptopic: "[[topic-BIOLOGY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.ATOMS IN CELL",
    alias: "Thought: Atoms In Cell",
    parent: "topic.BIOLOGY",
    tags: ['creation', 'atoms', 'biology', 'cell', 'majesty'],
    notes: "",
    level: 6
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
    zh_title: "Xìbāo zhōng yuánzǐ",
    zh_content: "Píngjūn měi gè rénlèi xìbāo yóu dàyuē èrbǎi wànyì gè yuánzǐ zǔchéng... shén shì wěidà de!"
});

MATCH (t:THOUGHT {name: "thought.ATOMS IN CELL"})
MATCH (c:CONTENT {name: "content.ATOMS IN CELL"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATOMS IN CELL" }]->(c);

MATCH (parent:TOPIC {name: "topic.CREATION"})
MATCH (child:THOUGHT {name: "thought.ATOMS IN CELL"})
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION->ATOMS IN CELL" }]->(child);
```
