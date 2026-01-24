---
name: "thought.TRANSFORMING POWER LOVE"
alias: "Thought: Transforming Power Love"
type: THOUGHT
en_content: "God's Love is frighteningly powerful: turning dirt into flesh, flesh into spirit, sin into righteousness and death into life."
parent: "topic.THE GODHEAD"
tags:
- love
- transformation
- power
- god
- life
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Dec-2011b)
CREATE (t:THOUGHT {
    name: "thought.TRANSFORMING POWER LOVE",
    alias: "Thought: Transforming Power Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'transformation', 'power', 'god', 'life'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.TRANSFORMING POWER LOVE",
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

MATCH (t:THOUGHT {name: "thought.TRANSFORMING POWER LOVE"})
MATCH (c:CONTENT {name: "content.TRANSFORMING POWER LOVE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRANSFORMING POWER LOVE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.TRANSFORMING POWER LOVE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->TRANSFORMING POWER LOVE" }]->(child);
```
