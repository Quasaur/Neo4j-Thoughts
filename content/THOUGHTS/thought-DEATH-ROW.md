---
type: THOUGHT
name: "thought.DEATH ROW"
alias: "Thought: Death Row"
parent: "topic.THE-GOSPEL"
en_content: "The whole world is on Death Row. A FULL PARDON is being offered by Jesus...take it!"
tags: ["condemnation", "world", "pardon", "receive", "jesus"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEATH ROW",
    alias: "Thought: Death Row",
    parent: "topic.THE-GOSPEL",
    tags: ["condemnation", "world", "pardon", "receive", "jesus"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEATH ROW",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEATH ROW"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE-GOSPEL->DEATH ROW"
RETURN t, parent;
```
