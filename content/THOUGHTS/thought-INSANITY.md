---
type: THOUGHT
name: "thought.INSANITY"
alias: "Thought: Insanity"
parent: "topic.PSYCHOLOGY"
tags: ["insanity", "madness", "delusion", "narcissism", "fooliishness"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.INSANITY",
    alias: "Thought: Insanity",
    parent: "topic.PSYCHOLOGY",
    tags: ["insanity", "madness", "delusion", "narcissism", "fooliishness"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INSANITY",
    ctype: "THOUGHT",
    en_title: "Insanity",
    en_content: "",
    es_title: "LOCURA",
    es_content: "¡Lucifer tuvo el descaro absoluto de pedirle a su CREADOR que lo adorara!
En la Corte del Cielo la locura y el pecado son lo mismo.",
    fr_title: "FOLIE",
    fr_content: "Lucifer a eu le culot absolu de demander à son CRÉATEUR de l'adorer !
Dans la Cour du Ciel, la folie et le péché ne font qu'un.",
    hi_title: "पागलपन",
    hi_content: "लूसिफ़ेर के पास अपने निर्माता से उसकी पूजा करने के लिए कहने का अदम्य साहस था!
स्वर्ग के दरबार में पागलपन और पाप एक ही हैं।",
    zh_title: "fēng kuáng",
    zh_content: "lù xī fǎ jìng rán hòu yán wú chǐ dì yāo qiú tā de chuàng zào zhě chóng bài tā ！
 zài tiān tíng lǐ ， fēng kuáng hé zuì è shì yī huí shì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INSANITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->INSANITY"
RETURN t, parent;
```
