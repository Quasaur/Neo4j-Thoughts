---
type: PASSAGE
name: "passage.REMOVING ALL THINGS"
alias: "Passage: Removing All Things"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "I will completely remove all things from the face of the earth."
tags: ["judgment", "sovereignty", "bible", "earth", "prophecy"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 't' and 'c' as variables to keep them in memory
CREATE (t:PASSAGE {
    name: "passage.REMOVING ALL THINGS",
    parent: "topic.DIVINE SOVEREIGNTY",
    alias: "Passage: Removing All Things",
    tags: ["judgment", "sovereignty", "bible", "earth", "prophecy"],
    level: 2
})

CREATE (c:CONTENT {
    name: "content.REMOVING ALL THINGS",
    ctype: "PASSAGE",
    en_title: "Removing All Things",
    en_content: "I will completely remove all things from the face of the earth.",
    es_title: "Eliminando todas las cosas",
    es_content: "«Eliminaré por completo todas las cosas de la faz de la tierra», — Dios",
    fr_title: "Suppression de toutes choses",
    fr_content: "« Je supprimerai complètement toutes choses de la surface de la terre », — Dieu",
    hi_title: "सभी चीज़ों को हटाना",
    hi_content: "मैं धरती की सतह से सभी चीज़ों को पूरी तरह हटा दूँगा, — ईश्वर",
    zh_title: "Qīngchú wànwù",
    zh_content: "wǒ bì jiāng dìshàng de yīqiè chèdǐ qīngchú.——Shàngdì"
})

// 2. Link Content to Passage using the variables 't' and 'c'
MERGE (t)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.REMOVING ALL THINGS"

// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(t)
ON CREATE SET r2.name = "p.edge.DIVINE SOVEREIGNTY->REMOVING ALL THINGS"
RETURN t, parent;
```
