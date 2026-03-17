---
type: THOUGHT
name: "thought.THE LAST WORD"
alias: "Thought: The Last Word"
parent: "topic.THE-GOSPEL"
en_content: "Yehoshua Ha Meshiach: Jesus The Christ: The Living Word...The Last Word!"
tags: ["gospel", "jesus_christ", "livingword", "lastword", "word_of_god"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.THE LAST WORD",
    alias: "Thought: The Last Word",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "jesus_christ", "livingword", "lastword", "word_of_god"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE LAST WORD",
    ctype: "THOUGHT",
    en_title: "The Last Word",
    en_content: "Yehoshua Ha Meshiach: Jesus The Christ: The Living Word...The Last Word!",
    es_title: "LA ÚLTIMA PALABRA",
    es_content: "Yehoshua Ha Meshiach: Jesús El Cristo: La Palabra Viva... ¡La Última Palabra!",
    fr_title: "LE DERNIER MOT",
    fr_content: "Yehoshua Ha Meshiach : Jésus le Christ : La Parole vivante... La Dernière Parole !",
    hi_title: "आखिरी शब्द",
    hi_content: "येहोशुआ हा मेशियाच: जीसस द क्राइस्ट: द लिविंग वर्ड...द लास्ट वर्ड!",
    zh_title: "zuì hòu yī jù huà",
    zh_content: "Yehoshua Ha Meshiach： yē sū jī dū ： huó shēng shēng de dào …… zuì hòu de dào ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.THE LAST WORD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE-GOSPEL->THE LAST WORD"
RETURN t, parent;
```
