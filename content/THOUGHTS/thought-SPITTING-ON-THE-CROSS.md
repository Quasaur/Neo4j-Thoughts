---
type: THOUGHT
name: "thought.SPITTING ON THE CROSS"
alias: "Thought: Spitting On The Cross"
parent: "topic.MERCY"
en_content: "Jesus has been punished for the sin you have committed against me; if I don't forgive you I have spit on The Cross of Christ."
tags: ["forgiveness", "cross", "atonement", "grace", "pride"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SPITTING ON THE CROSS",
    alias: "Thought: Spitting On The Cross",
    parent: "topic.MERCY",
    tags: ['forgiveness', 'cross', 'atonement', 'grace', 'pride'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.SPITTING ON THE CROSS",
    ctype: "THOUGHT",
    en_title: "Spitting On The Cross",
    en_content: "Jesus has been punished for the sin you have committed against me; if I don't forgive you I have spit on The Cross of Christ.",
    es_title: "Escupiendo En La Cruz",
    es_content: "Jesús ha sido castigado por el pecado que has cometido contra mí; si no te perdono he escupido en La Cruz de Cristo.",
    fr_title: "Cracher Sur La Croix",
    fr_content: "Jésus a été puni pour le péché que tu as commis contre moi ; si je ne te pardonne pas j'ai craché sur La Croix du Christ.",
    hi_title: "क्रूस पर थूकना",
    hi_content: "यीशु को उस पाप के लिए दंडित किया गया है जो तुमने मेरे विरुद्ध किया है; यदि मैं तुम्हें क्षमा नहीं करता तो मैंने मसीह के क्रूस पर थूका है।",
    zh_title: "Xiang Shizi Jia Tu Tuo",
    zh_content: "Yesu yi wei ni dui wo fan de zui er shou dao le chengfa; ruguo wo bu yuanliang ni, wo jiu shi xiang Jidu de shizi jia tu tuo."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SPITTING ON THE CROSS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->SPITTING ON THE CROSS"
RETURN t, parent;
```
