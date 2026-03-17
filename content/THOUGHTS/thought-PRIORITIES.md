---
type: THOUGHT
name: "thought.PRIORITIES"
alias: "Thought: Priorities"
parent: "topic.WISDOM"
tags: ["priorities", "seekyefirst", "divine_will", "god", "faith"]
ptopic: "[[topic-WISDOM]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PRIORITIES",
    alias: "Thought: Priorities",
    parent: "topic.WISDOM",
    tags: ["priorities", "seekyefirst", "divine_will", "god", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIORITIES",
    ctype: "THOUGHT",
    en_title: "Priorities",
    en_content: "",
    es_title: "PRIORIDADES",
    es_content: "La verdad es que la Voluntad de Dios no es lo suficientemente importante para ninguno de nosotros.",
    fr_title: "PRIORITÉS",
    fr_content: "La vérité est que la Volonté de Dieu n’est pas assez importante pour aucun d’entre nous.",
    hi_title: "वरीयताओं",
    hi_content: "सच तो यह है कि ईश्वर की इच्छा हममें से किसी के लिए भी उतनी महत्वपूर्ण नहीं है।",
    zh_title: "yōu xiān shì xiàng",
    zh_content: "shì shí shàng ， shàng dì de zhǐ yì duì wǒ men rèn hé rén lái shuō dōu bù gòu zhòng yào 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRIORITIES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->PRIORITIES"
RETURN t, parent;
```
