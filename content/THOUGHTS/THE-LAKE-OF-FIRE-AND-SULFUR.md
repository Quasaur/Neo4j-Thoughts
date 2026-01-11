---
name: "thought.THE_LAKE_OF_FIRE_AND_SULFUR"
alias: "Thought: THE LAKE OF FIRE AND SULFUR"
type: THOUGHT
parent: topic.JUSTICE
tags:
- lakeoffire
- wrathofgod
- hell
- regret
- eternity
neo4j: true
ptopic: "[[topic-JUSTICE]]"
level: 5
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_LAKE_OF_FIRE_AND_SULFUR",
    alias: "Thought: THE LAKE OF FIRE AND SULFUR",
    parent: "topic.JUSTICE",
    tags: ["lakeoffire", "wrathofgod", "hell", "regret", "eternity"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.THE_LAKE_OF_FIRE_AND_SULFUR",
    en_title: "THE LAKE OF FIRE AND SULFUR",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_LAKE_OF_FIRE_AND_SULFUR" AND c.name = "content.THE_LAKE_OF_FIRE_AND_SULFUR"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_LAKE_OF_FIRE_AND_SULFUR"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.THE_LAKE_OF_FIRE_AND_SULFUR"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.JUSTICE->THE_LAKE_OF_FIRE_AND_SULFUR"}]->(child);
```
