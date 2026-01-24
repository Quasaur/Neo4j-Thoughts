---
name: "thought.NOT_LIKE_ME"
alias: "Thought: NOT-LIKE-ME"
type: THOUGHT
parent: topic.MERCY
tags:
- idolatry
- divine
- superior
- fruitofthespirit
- grace
neo4j: true
ptopic: "[[topic-MERCY]]"
level: 5
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.NOT_LIKE_ME",
    alias: "Thought: NOT-LIKE-ME",
    parent: "topic.MERCY",
    tags: ["idolatry", "divine", "superior", "fruitofthespirit", "grace"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.NOT_LIKE_ME",
    en_title: "NOT-LIKE-ME",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOT_LIKE_ME" AND c.name = "content.NOT_LIKE_ME"
MERGE (t)-[:HAS_CONTENT {name: "edge.NOT_LIKE_ME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.NOT_LIKE_ME"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MERCY->NOT_LIKE_ME"}]->(child);
```
