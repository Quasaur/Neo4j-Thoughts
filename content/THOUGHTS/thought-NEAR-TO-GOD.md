---
type: THOUGHT
name: "thought.NEAR TO GOD"
alias: "Thought: Near to God"
parent: "topic.EVIL"
en_content: "No one comes near to God who is not called by God to do so (John 6:44)."
tags: ["access", "calling", "desire", "predestined", "foreknowledge"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.NEAR TO GOD",
    alias: "Thought: Near to God",
    parent: "topic.EVIL",
    tags: ["access", "calling", "desire", "predestined", "foreknowledge"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NEAR TO GOD",
    ctype: "THOUGHT",
    en_title: "Near to God",
    en_content: "No one comes near to God who is not called by God to do so (John 6:44).",
    es_title: "CERCA DE DIOS",
    es_content: "Nadie se acerca a Dios si no es llamado por Dios a hacerlo (Juan 6:44).",
    fr_title: "PROCHE DE DIEU",
    fr_content: "Personne ne s’approche de Dieu s’il n’est appelé par Dieu à le faire (Jean 6 :44).",
    hi_title: "भगवान के निकट",
    hi_content: "कोई भी व्यक्ति परमेश्वर के निकट नहीं आता जिसे परमेश्वर ने ऐसा करने के लिए नहीं बुलाया है (यूहन्ना 6:44)।",
    zh_title: "qīn jìn shén",
    zh_content: "méi yǒu bèi shén hū zhào de rén jiù méi yǒu rén néng qīn jìn shén （ yuē hàn fú yīn  6:44）。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NEAR TO GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->NEAR TO GOD"
RETURN t, parent;
```
