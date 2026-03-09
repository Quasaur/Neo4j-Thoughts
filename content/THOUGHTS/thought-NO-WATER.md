---
type: THOUGHT
name: "thought.NO WATER"
alias: "Thought: No Water"
parent: "topic.PHILOSOPHY"
en_content: "How can a fish say there is no water? Yet men say there is no God!"
tags: ["evolution", "science", "religion", "evidence", "faith"]
ptopic: "[[topic-PHILOSOPHY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.NO WATER",
    alias: "Thought: No Water",
    parent: "topic.PHILOSOPHY",
    tags: ["evolution", "science", "religion", "evidence", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NO WATER",
    ctype: "THOUGHT",
    en_title: "No Water",
    en_content: "How can a fish say there is no water? Yet men say there is no God!",
    es_title: "SIN AGUA",
    es_content: "¿Cómo puede un pez decir que no hay agua? ¡Sin embargo, los hombres dicen que no hay Dios!",
    fr_title: "PAS D'EAU",
    fr_content: "Comment un poisson peut-il dire qu’il n’y a pas d’eau ? Pourtant les hommes disent que Dieu n’existe pas !",
    hi_title: "पानी नहीं",
    hi_content: "मछली कैसे कह सकती है कि पानी नहीं है? फिर भी मनुष्य कहते हैं कि कोई ईश्वर नहीं है!",
    zh_title: "méi yǒu shuǐ",
    zh_content: "yú zěn me néng shuō méi yǒu shuǐ ne ？ rán ér rén què shuō méi yǒu shén ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NO WATER" AND c.name = "content.NO WATER"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.NO WATER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.NO WATER"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PHILOSOPHY->NO WATER"}]->(child);
```
