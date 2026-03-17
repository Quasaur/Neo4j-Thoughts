---
type: THOUGHT
name: "thought.THE LAKE OF FIRE AND SULFUR"
alias: "Thought: The Lake of Fire and Sulfur"
parent: "topic.JUSTICE"
en_content: "Finding yourself foundering alone and helpless in the Ocean of GOD's Wrath for all Eternity...it is now TOO LATE to finally start taking the direction of your lifestyle seriously."
tags: ["lake_of_fire", "wrath_of_god", "hell", "regret", "eternity"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.THE LAKE OF FIRE AND SULFUR",
    alias: "Thought: The Lake of Fire and Sulfur",
    parent: "topic.JUSTICE",
    tags: ["lake_of_fire", "wrath_of_god", "hell", "regret", "eternity"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.THE LAKE OF FIRE AND SULFUR",
    ctype: "THOUGHT",
    en_title: "The Lake of Fire and Sulfur",
    en_content: "Finding yourself foundering alone and helpless in the Ocean of GOD's Wrath for all Eternity...it is now TOO LATE to finally start taking the direction of your lifestyle seriously.",
    es_title: "EL LAGO DE FUEGO Y AZUFRE",
    es_content: "Al encontrarte hundido solo e indefenso en el Océano de la Ira de DIOS por toda la Eternidad... ahora es DEMASIADO TARDE para finalmente comenzar a tomar en serio la dirección de tu estilo de vida.",
    fr_title: "LE LAC DE FEU ET DE SOUFRE",
    fr_content: "Vous retrouver seul et impuissant dans l’océan de la colère de DIEU pour toute l’éternité… il est maintenant TROP TARD pour enfin commencer à prendre au sérieux l’orientation de votre style de vie.",
    hi_title: "आग और गंधक की झील",
    hi_content: "अपने आप को अनंत काल तक ईश्वर के क्रोध के सागर में अकेला और असहाय पाते हुए... अब अंततः अपनी जीवनशैली की दिशा को गंभीरता से लेना शुरू करने में बहुत देर हो चुकी है।",
    zh_title: "huǒ yǔ liú huáng hú",
    zh_content: "fā xiàn zì jǐ zài shàng dì yǒng héng de fèn nù hǎi yáng zhōng gū dú wú zhù dì chén mò …… xiàn zài kāi shǐ rèn zhēn duì dài nǐ de shēng huó fāng shì de fāng xiàng yǐ jīng tài wǎn le 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.THE LAKE OF FIRE AND SULFUR"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.JUSTICE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.JUSTICE->THE LAKE OF FIRE AND SULFUR"
RETURN t, parent;
```
