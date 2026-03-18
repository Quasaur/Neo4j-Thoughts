---
type: THOUGHT
name: "thought.TRANSFORMING POWER LOVE"
alias: "Thought: Transforming Power Love"
parent: "topic.THE GODHEAD"
en_content: "God's Love is frighteningly powerful: turning dirt into flesh, flesh into spirit, sin into righteousness and death into life."
tags: ["love", "transformation", "power", "god", "life"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Dec-2011b)
CREATE (t:THOUGHT {    name: "thought.TRANSFORMING POWER LOVE",
    alias: "Thought: Transforming Power Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'transformation', 'power', 'god', 'life'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.TRANSFORMING POWER LOVE",
    ctype: "THOUGHT",
    en_title: "Transforming Power Love",
    en_content: "God's Love is frighteningly powerful: turning dirt into flesh, flesh into spirit, sin into righteousness and death into life.",
    es_title: "El Poder Transformador del Amor",
    es_content: "El Amor de Dios es tremendamente poderoso: convirtiendo el polvo en carne, la carne en espíritu, el pecado en justicia y la muerte en vida.",
    fr_title: "Le Pouvoir Transformateur de l'Amour",
    fr_content: "L'Amour de Dieu est terriblement puissant : transformant la poussière en chair, la chair en esprit, le péché en justice et la mort en vie.",
    hi_title: "प्रेम की रूपांतरणकारी शक्ति",
    hi_content: "परमेश्वर का प्रेम भयावह रूप से शक्तिशाली है: मिट्टी को मांस में, मांस को आत्मा में, पाप को धार्मिकता में और मृत्यु को जीवन में बदल देता है।",
    zh_title: "Ài de Zhuǎnhuà Lìliàng",
    zh_content: "Shàngdì de ài jùyǒu kěpà de lìliàng: bǎ chéntǔ biànchéng xuèròu, bǎ xuèròu biànchéng línghún, bǎ zuì'è biànchéng gōngyì, bǎ sǐwáng biànchéng shēngmìng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TRANSFORMING POWER LOVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->TRANSFORMING POWER LOVE"
RETURN t, parent;
```
