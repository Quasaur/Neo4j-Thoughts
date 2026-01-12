---
name: "thought.GODS GENIUS LOVE HATE"
alias: "Thought: Gods Genius Love Hate"
type: THOUGHT
en_content: "What identifies God's Genius is the ability to hate evil while simultaneously loving evil people."
parent: "topic.THE GODHEAD"
tags:
- genius
- love
- hate
- evil
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013c)
CREATE (t:THOUGHT {
    name: "thought.GODS GENIUS LOVE HATE",
    alias: "Thought: Gods Genius Love Hate",
    parent: "topic.THE GODHEAD",
    tags: ['genius', 'love', 'hate', 'evil', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS GENIUS LOVE HATE",
    en_title: "Gods Genius Love Hate",
    en_content: "What identifies God's Genius is the ability to hate evil while simultaneously loving evil people.",
    es_title: "El Genio del Amor y Odio de Dios",
    es_content: "Lo que identifica el Genio de Dios es la capacidad de odiar el mal mientras simultáneamente ama a las personas malvadas.",
    fr_title: "Le Génie Divin d'Amour et de Haine",
    fr_content: "Ce qui identifie le Génie de Dieu est la capacité de haïr le mal tout en aimant simultanément les personnes mauvaises.",
    hi_title: "परमेश्वर की प्रतिभा प्रेम घृणा",
    hi_content: "परमेश्वर की प्रतिभा की पहचान यह है कि वह बुराई से घृणा करने की क्षमता रखता है और साथ ही साथ बुरे लोगों से प्रेम भी करता है।",
    zh_title: "Shén de Tiāncái Ài Hèn",
    zh_content: "Shénmíng tiāncái de tèzhēng shì nénggòu hènwù è'è, tóngshí yòu ài zhe zuò'è de rén."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS GENIUS LOVE HATE" AND c.name = "content.GODS GENIUS LOVE HATE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS GENIUS LOVE HATE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS GENIUS LOVE HATE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS GENIUS LOVE HATE" }]->(child);
```
