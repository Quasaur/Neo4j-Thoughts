---
type: PASSAGE
name: "passage.FREEDOM OF DEATH"
alias: "Passage: The Freedom of Death"
parent: "topic.FREEDOM"
sortedsource: "Romans 06:07"
en_content: "For he that is dead is freed from sin."
tags: ["freedom", "death", "sin", "the_cross", "jesus_christ"]
ptopic: "[[topic-FREEDOM]]"
level: 5
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.FREEDOM OF DEATH",
    parent: "topic.FREEDOM",
    alias: "Passage: The Freedom of Death",
    tags: ["freedom", "death", "sin", "the_cross", "jesus_christ"],
    source: "Romans 6:7",
    sortedsource: "Romans 06:07",
    biblelink: "https://www.biblegateway.com/passage/?search=Romans+6:7&version=KJV",
    level: 5
})

CREATE (c:CONTENT {
    
    
    name: "content.FREEDOM OF DEATH",
    ctype: "PASSAGE",
    en_title: "Passage: The Freedom of Death",
    en_content: "For he that is dead is freed from sin.",
 es_title: "Pasaje: La libertad de la muerte",
 es_content: "Porque el que está muerto queda libre del pecado.",
 fr_title: "Passage : La liberté de mourir",
 fr_content: "Car celui qui est mort est libéré du péché.",
 hi_title: "परिच्छेद: मृत्यु की स्वतंत्रता",
 hi_content: "क्योंकि जो मर गया वह पाप से मुक्त हो गया।",
 zh_title: "duàn luò : sǐ wáng de zì yóu",
 zh_content: "yīn wèi sǐ zhě jiù tuō lí le zuì niè 。"
})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.FREEDOM OF DEATH"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.FREEDOM"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.FREEDOM->FREEDOM OF DEATH"
RETURN b, parent;
```
