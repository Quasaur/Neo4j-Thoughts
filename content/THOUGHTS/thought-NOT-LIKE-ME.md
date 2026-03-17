---
type: THOUGHT
name: "thought.NOT LIKE ME"
alias: "Thought: Not-like-me"
parent: "topic.MERCY"
en_content: "I was wrong about God; He's not in any way near as vindictive, judgmental or self-righteous as I am."
tags: ["idolatry", "divine", "superior", "fruit_of_the_spirit", "grace"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.NOT LIKE ME",
    alias: "Thought: Not-like-me",
    parent: "topic.MERCY",
    tags: ["idolatry", "divine", "superior", "fruit_of_the_spirit", "grace"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.NOT LIKE ME",
    ctype: "THOUGHT",
    en_title: "Not-like-me",
    en_content: "I was wrong about God; He's not in any way near as vindictive, judgmental or self-righteous as I am.",
    es_title: "NO COMO YO",
    es_content: "Me equivoqué acerca de Dios; Él no es de ninguna manera tan vengativo, crítico o moralista como yo.",
    fr_title: "PAS-COMME-MOI",
    fr_content: "J'avais tort à propos de Dieu ; Il n’est en aucun cas aussi vindicatif, critique ou pharisaïque que moi.",
    hi_title: "मेरे जैसा नहीं",
    hi_content: "मैं भगवान के बारे में गलत था; वह किसी भी तरह से मेरे जितना प्रतिशोधी, आलोचनात्मक या आत्मतुष्ट नहीं है।",
    zh_title: "bù xiàng wǒ",
    zh_content: "wǒ duì shàng dì de kàn fǎ shì cuò wù de ； tā gēn běn bù xiàng wǒ nà yàng yǒu bào fù xīn 、 ài píng pàn bié rén huò zì yǐ wéi shì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOT LIKE ME"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MERCY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MERCY->NOT LIKE ME"
RETURN t, parent;
```
