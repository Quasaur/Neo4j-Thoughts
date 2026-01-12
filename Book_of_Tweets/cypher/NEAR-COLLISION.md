---
name: "thought.NEAR COLLISION"
alias: "Thought: Near Collision"
type: THOUGHT
en_content: "An AA jet had a near collision with a United over AL...my sister was on the AA plane and could read the writing on the other plane."
parent: "topic.SPIRITUALITY"
tags:
- providence
- protection
- safety
- miracle
- spirituality
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.NEAR COLLISION",
    alias: "Thought: Near Collision",
    parent: "topic.SPIRITUALITY",
    tags: ['providence', 'protection', 'safety', 'miracle', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NEAR COLLISION",
    en_title: "Near Collision",
    en_content: "An AA jet had a near collision with a United over AL...my sister was on the AA plane and could read the writing on the other plane.",
    es_title: "Casi colisión",
    es_content: "Un avión AA estuvo a punto de colisionar con un United sobre AL... mi hermana estaba en el avión AA y podía leer la escritura en el otro avión.",
    fr_title: "Quasi-collision",
    fr_content: "Un avion à réaction AA a failli entrer en collision avec un United au-dessus d'AL... ma sœur était dans l'avion AA et pouvait lire les écrits sur l'autre avion.",
    hi_title: "टक्कर के निकट",
    hi_content: "एक एए जेट की एएल के ऊपर युनाइटेड से सीधी टक्कर हो गई...मेरी बहन एए विमान में थी और दूसरे विमान में लिखा पढ़ सकती थी।",
    zh_title: "险些发生碰撞",
    zh_content: "一架 AA 喷气式飞机在 AL 上与一架联合航空差点相撞……我姐姐在 AA 飞机上，可以阅读另一架飞机上的文字。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NEAR COLLISION" AND c.name = "content.NEAR COLLISION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NEAR COLLISION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.NEAR COLLISION"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >NEAR COLLISION" }]->(child);
```
