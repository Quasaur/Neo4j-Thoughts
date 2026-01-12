---
name: "thought.TWO TYPES CHURCHES"
alias: "Thought: Two Types Churches"
type: THOUGHT
en_content: "There are two churches: (1) the institutionalized church, and (2) the REAL church elected by God; one is temporary, one is eternal."
parent: "topic.RELIGION"
tags:
- church
- eternity
- election
- religion
- institutions
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.TWO TYPES CHURCHES",
    alias: "Thought: Two Types Churches",
    parent: "topic.RELIGION",
    tags: ['church', 'eternity', 'election', 'religion', 'institutions'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TWO TYPES CHURCHES",
    en_title: "Two Types Churches",
    en_content: "There are two churches: (1) the institutionalized church, and (2) the REAL church elected by God; one is temporary, one is eternal.",
    es_title: "Dos Tipos de Iglesias",
    es_content: "Hay dos iglesias: (1) la iglesia institucionalizada, y (2) la iglesia VERDADERA elegida por Dios; una es temporal, una es eterna.",
    fr_title: "Deux Types d'Églises",
    fr_content: "Il y a deux églises : (1) l'église institutionnalisée, et (2) la VRAIE église élue par Dieu ; l'une est temporaire, l'une est éternelle.",
    hi_title: "दो प्रकार की कलीसियाएं",
    hi_content: "दो कलीसियाएं हैं: (१) संस्थागत कलीसिया, और (२) परमेश्वर द्वारा चुनी गई वास्तविक कलीसिया; एक अस्थायी है, एक अनन्त है।",
    zh_title: "Liǎng Zhǒng Jiàohuì",
    zh_content: "Yǒu liǎng gè jiàohuì: (1) zhìdùhuà de jiàohuì, hé (2) Shàngdì xuǎnzhòng de zhēnzhèng jiàohuì; yī gè shì línshí de, yī gè shì yǒnghéng de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TWO TYPES CHURCHES" AND c.name = "content.TWO TYPES CHURCHES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TWO TYPES CHURCHES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.TWO TYPES CHURCHES"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >TWO TYPES CHURCHES" }]->(child);
```
