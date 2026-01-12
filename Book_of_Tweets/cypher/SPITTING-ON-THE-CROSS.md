---
name: "thought.SPITTING ON THE CROSS"
alias: "Thought: Spitting On The Cross"
type: THOUGHT
en_content: "Jesus has been punished for the sin you have committed against me; if I don't forgive you I have spit on The Cross of Christ."
parent: "topic.GRACE"
tags:
- forgiveness
- cross
- atonement
- grace
- pride
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.SPITTING ON THE CROSS",
    alias: "Thought: Spitting On The Cross",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'cross', 'atonement', 'grace', 'pride'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SPITTING ON THE CROSS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SPITTING ON THE CROSS" AND c.name = "content.SPITTING ON THE CROSS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPITTING ON THE CROSS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.SPITTING ON THE CROSS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >SPITTING ON THE CROSS" }]->(child);
```
