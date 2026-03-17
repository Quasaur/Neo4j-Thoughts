---
type: THOUGHT
name: "thought.REPARATIONS"
alias: "Thought: Reparations"
parent: "topic.JUSTICE"
tags: ["reparations", "slavery", "blackamericans", "compensation", "justice"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.REPARATIONS",
    alias: "Thought: Reparations",
    parent: "topic.JUSTICE",
    tags: ["reparations", "slavery", "blackamericans", "compensation", "justice"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.REPARATIONS",
    ctype: "THOUGHT",
    en_title: "Reparations",
    en_content: "",
    es_title: "INDEMNIZACIÓN",
    es_content: "Reparaciones razonables a los descendientes de esclavos negros: esos descendientes deben estar EXENTOS DE IMPUESTOS FEDERALES Y ESTATALES.",
    fr_title: "RÉPARATIONS",
    fr_content: "Réparations raisonnables aux descendants d’esclaves noirs : ces descendants devraient être EXEMPTÉS D’IMPÔTS FÉDÉRAUX ET D’ÉTAT.",
    hi_title: "मुआवज़ा",
    hi_content: "काले दासों के वंशजों को उचित मुआवज़ा: उन वंशजों को संघीय और राज्य कर-मुक्त होना चाहिए।",
    zh_title: "péi cháng",
    zh_content: "duì hēi rén nú lì de hòu dài de hé lǐ péi cháng ： zhè xiē hòu dài yīng gāi xiǎng shòu lián bāng hé zhōu miǎn shuì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.REPARATIONS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.JUSTICE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.JUSTICE->REPARATIONS"
RETURN t, parent;
```
