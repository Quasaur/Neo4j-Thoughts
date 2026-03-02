---
type: THOUGHT
name: "thought.PERCEPTION"
alias: "Thought: PERCEPTION"
parent: "topic.ATTITUDE"
tags: ["attitude", "seeing", "observing", "perception", "selfimprovement"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PERCEPTION",
    alias: "Thought: PERCEPTION",
    parent: "topic.ATTITUDE",
    tags: ["attitude", "seeing", "observing", "perception", "selfimprovement"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PERCEPTION",
    ctype: "THOUGHT",
    en_title: "PERCEPTION",
 es_title: "PERCEPCIÓN",
 fr_title: "PERCEPTION",
 hi_title: "धारणा",
 zh_title: "dòng chá lì",
    en_content: "",
 es_content: "No siempre podemos cambiar lo que vemos... pero siempre podemos cambiar cómo lo vemos.",
 fr_content: "Nous ne pouvons pas toujours changer ce que nous voyons... mais nous pouvons toujours changer la façon dont nous le voyons.",
 hi_content: "हम जो देखते हैं उसे हमेशा नहीं बदल सकते...लेकिन हम उसे देखने का तरीका हमेशा बदल सकते हैं।",
 zh_content: "wǒ men bù néng zǒng shì gǎi biàn wǒ men suǒ kàn dào de …… dàn wǒ men zǒng shì kě yǐ gǎi biàn wǒ men kàn dài tā de fāng shì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PERCEPTION" AND c.name = "content.PERCEPTION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.PERCEPTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.PERCEPTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->PERCEPTION"}]->(child);
```