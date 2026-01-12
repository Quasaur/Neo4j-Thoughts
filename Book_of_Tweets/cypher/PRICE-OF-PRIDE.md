---
name: "thought.PRICE OF PRIDE"
alias: "Thought: Price Of Pride"
type: THOUGHT
en_content: "At what point in history did African American men decide that pride was worth the price of killing each other??"
parent: "topic.MORALITY"
tags:
- pride
- killing
- price
- race
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012e)
CREATE (t:THOUGHT {
    name: "thought.PRICE OF PRIDE",
    alias: "Thought: Price Of Pride",
    parent: "topic.MORALITY",
    tags: ['pride', 'killing', 'price', 'race', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PRICE OF PRIDE",
    en_title: "Price Of Pride",
    en_content: "At what point in history did African American men decide that pride was worth the price of killing each other??",
    es_title: "Precio del orgullo",
    es_content: "¿En qué momento de la historia los hombres afroamericanos decidieron que el orgullo valía el precio de matarse unos a otros?",
    fr_title: "Le prix de la fierté",
    fr_content: "À quel moment de l’histoire les hommes afro-américains ont-ils décidé que la fierté valait le prix à payer pour s’entre-tuer ?",
    hi_title: "गौरव की कीमत",
    hi_content: "इतिहास में किस मोड़ पर अफ़्रीकी-अमेरिकी पुरुषों ने निर्णय लिया कि गर्व के लिए एक-दूसरे को मारने की कीमत चुकानी होगी??",
    zh_title: "骄傲的代价",
    zh_content: "历史上的哪个时刻，非裔美国男人决定为了骄傲而付出互相残杀的代价？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRICE OF PRIDE" AND c.name = "content.PRICE OF PRIDE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRICE OF PRIDE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PRICE OF PRIDE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PRICE OF PRIDE" }]->(child);
```
