---
type: THOUGHT
name: "thought.ANGER AS CONTAGION"
alias: "Thought: Anger As Contagion"
parent: "topic.ATTITUDE"
en_content: "Anger is a contagion that easily leaps from soul to soul where there is an absence of reason."
tags: ["anger", "reason", "soul", "attitude", "character"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ANGER AS CONTAGION",
    alias: "Thought: Anger As Contagion",
    parent: "topic.ATTITUDE",
    tags: ['anger', 'reason', 'soul', 'attitude', 'character'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ANGER AS CONTAGION",
    ctype: "THOUGHT",
    en_title: "Anger As Contagion",
    en_content: "Anger is a contagion that easily leaps from soul to soul where there is an absence of reason.",
    es_title: "La Ira como Contagio",
    es_content: "La ira es un contagio que salta fácilmente de alma en alma donde hay ausencia de razón.",
    fr_title: "La Colère comme Contagion",
    fr_content: "La colère est une contagion qui saute facilement d'âme en âme là où la raison est absente.",
    hi_title: "संक्रमण के रूप में क्रोध",
    hi_content: "क्रोध एक संक्रमण है जो आसानी से एक आत्मा से दूसरी आत्मा में कूद जाता है जहां तर्क की अनुपस्थिति होती है।",
    zh_title: "Fènnù rú chuánrǎnbìng",
    zh_content: "Fènnù shì yī zhǒng chuánrǎnbìng, zài quēfá lǐxìng de dìfāng hěn róngyì cóng yīgè línghún tiào dào lìng yīgè línghún."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ANGER AS CONTAGION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->ANGER AS CONTAGION"
RETURN t, parent;
```
