---
name: "thought.LEGALITY OF ATONEMENT"
alias: "Thought: Legality Of Atonement"
type: THOUGHT
en_content: "IT'S NOT LEGAL for you AND Jesus to suffer for the same sin!"
parent: "topic.GRACE"
tags:
- atonement
- sin
- suffering
- legality
- jesus
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jul-2012b)
CREATE (t:THOUGHT {
    name: "thought.LEGALITY OF ATONEMENT",
    alias: "Thought: Legality Of Atonement",
    parent: "topic.GRACE",
    tags: ['atonement', 'sin', 'suffering', 'legality', 'jesus'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LEGALITY OF ATONEMENT",
    en_title: "Legality Of Atonement",
    en_content: "IT'S NOT LEGAL for you AND Jesus to suffer for the same sin!",
    es_title: "Legalidad de la Expiación",
    es_content: "¡NO ES LEGAL que tú Y Jesús sufran por el mismo pecado!",
    fr_title: "Légalité de l'Expiation",
    fr_content: "Ce N'EST PAS LÉGAL que toi ET Jésus souffriez pour le même péché !",
    hi_title: "प्रायश्चित्त की वैधता",
    hi_content: "तुम्हारे और यीशु दोनों का एक ही पाप के लिए कष्ट उठाना कानूनी नहीं है!",
    zh_title: "Shú zuì de hé fǎ xìng",
    zh_content: "Nǐ hé Yēsū dōu wéi tóng yī zuì 'é shòu kǔ shì bù hé fǎ de!"
});

MATCH (t:THOUGHT {name: "thought.LEGALITY OF ATONEMENT"})
MATCH (c:CONTENT {name: "content.LEGALITY OF ATONEMENT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LEGALITY OF ATONEMENT" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.LEGALITY OF ATONEMENT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LEGALITY OF ATONEMENT" }]->(child);
```
