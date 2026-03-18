---
type: THOUGHT
name: "thought.VOLITION2"
alias: "Thought: Second Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["freedom", "volition", "free_will", "misused", "abused"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.VOLITION2",
    alias: "Thought: Second Volition",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "free_will", "misused", "abused"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION2",
    ctype: "THOUGHT",
    en_title: "Second Volition",
    en_content: "",
    es_title: "SEGUNDA VOLICIÓN",
    es_content: "¿Será que Dios le dio a la humanidad catorce mil años de libre albedrío; para que cuando Él nos lo quite... ¿no lo extrañemos?",
    fr_title: "DEUXIÈME VOLITION",
    fr_content: "Se pourrait-il que Dieu ait donné à l’humanité quatorze mille ans de libre arbitre ; pour que quand Il l'enlèvera... nous ne le manquerons pas ?",
    hi_title: "दूसरी इच्छा",
    hi_content: "क्या ऐसा हो सकता है कि ईश्वर ने मानवता को चौदह हजार वर्ष की स्वतंत्र इच्छा दी हो; ताकि जब वह इसे ले जाए...हम इसे चूक न जाएँ?",
    zh_title: "dì èr cì yì yuàn",
    zh_content: "nán dào shàng dì gěi le rén lèi yī wàn sì qiān nián de zì yóu yì zhì ？ zhè yàng dāng tā bǎ tā ná zǒu shí …… wǒ men jiù bú huì cuò guò tā ？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.VOLITION2"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->VOLITION2"
RETURN t, parent;
```
