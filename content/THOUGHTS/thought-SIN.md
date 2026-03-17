---
type: THOUGHT
name: "thought.SIN"
alias: "Thought: Sin"
parent: "topic.GRACE"
tags: ["grace", "gospel", "love", "power", "jesus_christ"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SIN",
    alias: "Thought: Sin",
    parent: "topic.GRACE",
    tags: ["grace", "gospel", "love", "power", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN",
    ctype: "THOUGHT",
    en_title: "Sin",
    en_content: "",
    es_title: "PECADO",
    es_content: "La gracia no es que DIOS sea débil ante el pecado; ¡La gracia es DIOS haciéndote más fuerte que el pecado!",
    fr_title: "PÉCHÉ",
    fr_content: "La grâce n’est pas que DIEU soit faible envers le péché ; La grâce, c'est DIEU qui vous rend plus fort que le péché !",
    hi_title: "पाप",
    hi_content: "पाप के प्रति ईश्वर का कमजोर होना अनुग्रह नहीं है; ईश्वर की कृपा ही आपको पाप से अधिक मजबूत बनाती है!",
    zh_title: "zuì",
    zh_content: "ēn diǎn bú shì shén duì zuì de ruǎn ruò ； ér shì shén duì zuì de ruǎn ruò 。 ēn diǎn shì shén ràng nǐ bǐ zuì gèng qiáng dà ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->SIN"
RETURN t, parent;
```
