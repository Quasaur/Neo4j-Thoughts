---
type: THOUGHT
name: "thought.FOSSIL AMINO ACIDS"
alias: "Thought: Fossil Amino Acids"
parent: "topic.GEOLOGY"
en_content: "Why is it that amino acids are still found in fossils and are not broken down after hundreds of millions of years?"
tags: ["science", "biology", "fossils", "creation", "time"]
ptopic: "[[topic-GEOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FOSSIL AMINO ACIDS",
    alias: "Thought: Fossil Amino Acids",
    parent: "topic.GEOLOGY",
    tags: ['science', 'biology', 'fossils', 'creation', 'time'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FOSSIL AMINO ACIDS",
    ctype: "THOUGHT",
    en_title: "Fossil Amino Acids",
    en_content: "Why is it that amino acids are still found in fossils and are not broken down after hundreds of millions of years?",
    es_title: "Aminoácidos Fósiles",
    es_content: "¿Por qué es que los aminoácidos todavía se encuentran en los fósiles y no se descomponen después de cientos de millones de años?",
    fr_title: "Acides Aminés Fossiles",
    fr_content: "Pourquoi les acides aminés se trouvent-ils encore dans les fossiles et ne se décomposent-ils pas après des centaines de millions d'années?",
    hi_title: "जीवाश्म अमीनो अम्ल",
    hi_content: "ऐसा क्यों है कि अमीनो अम्ल अभी भी जीवाश्मों में पाए जाते हैं और सैकड़ों मिलियन वर्षों बाद भी विघटित नहीं होते हैं?",
    zh_title: "Huashi Anjisuan",
    zh_content: "Weishenme anjisuan rengran zai huashi zhong beizhao dao, zai ji yi nian hou ye mei you fenjie?"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FOSSIL AMINO ACIDS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GEOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GEOLOGY->FOSSIL AMINO ACIDS"
RETURN t, parent;
```
