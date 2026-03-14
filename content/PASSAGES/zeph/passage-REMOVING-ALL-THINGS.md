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
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 't' and 'c' as variables to keep them in memory
CREATE (t:PASSAGE {
    name: "passage.REMOVING ALL THINGS",
    parent: "topic.DIVINE SOVEREIGNTY",
    alias: "Passage: Removing All Things",
    tags: ["judgment", "sovereignty", "bible", "earth", "prophecy"],
    source: "Proverbs 21:1",
    sortedsource: "Proverbs 21:01",
    biblelink: "https://www.biblegateway.com/passage/?search=Zephaniah%201&version=NASB",
    level: 2
})

CREATE (c:CONTENT {
    name: "content.REMOVING ALL THINGS",
    ctype: "PASSAGE",
    en_title: "Passage: Removing All Things",
    en_content: "I will completely remove all things from the face of the earth.",
    es_title: "Pasaje: Quitar todas las cosas",
    es_content: "Eliminaré por completo todas las cosas de la faz de la tierra.",
    fr_title: "Passage : Supprimer toutes choses",
    fr_content: "Je supprimerai complètement toutes choses de la surface de la terre.",
    hi_title: "परिच्छेद: सभी चीजों को हटाना",
    hi_content: "मैं पृथ्वी पर से सब कुछ पूरी तरह मिटा दूँगा।",
    zh_title: "duàn luò : yí chú suǒ yǒu dōng xī",
    zh_content: "wǒ jiāng chè dǐ qīng chú dì qiú biǎo miàn de yī qiè ."
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
