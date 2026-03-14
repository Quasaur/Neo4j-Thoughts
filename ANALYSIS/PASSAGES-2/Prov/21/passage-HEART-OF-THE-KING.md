---
type: PASSAGE
name: "passage.HEART OF THE KING"
alias: "Passage: The Heart of the King"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "The king’s heart is like channels of water in the Hand of the LORD; He turns it wherever He pleases."
tags: ["heart", "king", "divine_sovereignty", "water_streams", "free_will"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 3
neo4j: true
verified: true
---

```cypher
// 1. Create the Passage and Content nodes
// We use the variables 'b' and 'c' to link them later without re-searching
CREATE (b:PASSAGE {
    name: "passage.HEART OF THE KING",
    alias: "Passage: The Heart of the King", 
    tags: ["heart", "king", "divine_sovereignty", "water_streams", "free_will"], 
    source: "Proverbs 21:1",
    sortedsource: "Proverbs 21:01",
    biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+21%3A1&version=NASB",
    level: 3
})
CREATE (c:CONTENT {
    name: "content.HEART OF THE KING", 
    ctype: "PASSAGE",
    en_title: "Passage: The Heart of the King", 
    en_content: "The king’s heart is like channels of water in the Hand of the LORD; He turns it wherever He pleases.", 
    es_title: "Pasaje: El Corazón del Rey", 
    es_content: "El corazón del rey es como canales de agua en la mano del Señor; Él lo inclina a donde quiere.", 
    fr_title: "Passage : Le Cœur du Roi", 
    fr_content: "Le cœur du roi est comme un courant d’eau dans la main de l’Éternel ; il le dirige où il veut.", 
    hi_title: "मार्ग: राजा का हृदय", 
    hi_content: "राजा का हृदय यहोवा के हाथ में जल की नालियों के समान है; वह उसे जिधर चाहता है उधर मोड़ देता है।", 
    zh_title: "duàn luò : Wáng de xīn", 
    zh_content: "wáng de xīn zài yēhéhuá shǒuzhōng hǎoxiàng gōuqú de shuǐ, tā kěyǐ suíyì liúzhuàn."
})

// 2. Create the relationship between Passage and Content immediately
// Using 'r1' as a variable for the relationship
MERGE (b)-[r1:HAS_CONTENT]->(c) 
ON CREATE SET r1.name = "p.edge.HEART OF THE KING"

// 3. Use WITH to pass the 'b' variable to the next block
// Then find the Parent and link it
WITH b
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.DIVINE SOVEREIGNTY->HEART OF THE KING"

RETURN b, parent;
```
