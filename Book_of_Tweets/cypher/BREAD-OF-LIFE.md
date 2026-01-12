---
name: "thought.BREAD OF LIFE"
alias: "Thought: Bread Of Life"
type: THOUGHT
en_content: "We overeat in our attempt to feed our starving spirit with natural food instead of The BREAD of LIFE which is Christ."
parent: "topic.THE GODHEAD"
tags:
- christ
- bread
- life
- overeat
- spirit
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.BREAD OF LIFE",
    alias: "Thought: Bread Of Life",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'bread', 'life', 'overeat', 'spirit'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.BREAD OF LIFE",
    en_title: "Bread Of Life",
    en_content: "We overeat in our attempt to feed our starving spirit with natural food instead of The BREAD of LIFE which is Christ.",
    es_title: "Pan de Vida",
    es_content: "Comemos en exceso en nuestro intento de alimentar nuestro espíritu hambriento con comida natural en lugar del PAN de VIDA que es Cristo.",
    fr_title: "Pain de Vie",
    fr_content: "Nous mangeons trop dans notre tentative de nourrir notre esprit affamé avec de la nourriture naturelle au lieu du PAIN de VIE qui est le Christ.",
    hi_title: "जीवन की रोटी",
    hi_content: "हम अपनी भूखी आत्मा को प्राकृतिक भोजन से खिलाने के प्रयास में अत्यधिक खाते हैं, जीवन की रोटी जो मसीह है, के बजाय।",
    zh_title: "Shēngmìng zhī liáng 生命之粮",
    zh_content: "Wǒmen bàoshí shì shì wèi le yòng zìrán shíwù wèiyǎng wǒmen jīè de línghún, ér bù shì yòng shēngmìng zhī liáng--Jīdū. 我们暴食是为了用自然食物喂养我们饥饿的灵魂，而不是用生命之粮--基督。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BREAD OF LIFE" AND c.name = "content.BREAD OF LIFE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BREAD OF LIFE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.BREAD OF LIFE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >BREAD OF LIFE" }]->(child);
```
