---
name: "thought.DEATH_ROW"
alias: "Thought: DEATH ROW"
type: THOUGHT
parent: "topic.THE-GOSPEL"
en_content: "The whole world is on Death Row. A FULL PARDON is being offered by Jesus...take it!"
tags:
- condemnation
- world
- pardon
- receive
- jesus
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DEATH_ROW",
    alias: "Thought: DEATH ROW",
    parent: "topic.THE-GOSPEL",
    tags: ["condemnation", "world", "pardon", "receive", "jesus"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEATH_ROW",
    en_title: "Death Row",
    en_content: "The whole world is on Death Row. A FULL PARDON is being offered by Jesus...take it!",
	es_title: "corredor de la muerte",
    es_content: "El mundo entero está en el corredor de la muerte. Jesús ofrece UN PERDÓN COMPLETO... ¡tómalo!",
    fr_title: "Couloir de la mort",
    fr_content: "Le monde entier est dans le couloir de la mort. UN PARDON COMPLET est offert par Jésus... prenez-le !",
    hi_title: "मृत्यु कक्षों की कतार",
    hi_content: "पूरी दुनिया मौत की कतार में है. यीशु द्वारा पूर्ण क्षमा की पेशकश की जा रही है...इसे लें!",
    zh_title: "sǐ qiú qū",
    zh_content: "quán shì jiè de rén dōu bèi pàn sǐ xíng 。 yē sū zhèng zài tí gōng quán miàn shè miǎn …… jiē shòu ba ！"
});    

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEATH_ROW" AND c.name = "content.DEATH_ROW"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DEATH_ROW"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.DEATH_ROW"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->DEATH_ROW"}]->(child);
```
