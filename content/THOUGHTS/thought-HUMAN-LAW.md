---
type: THOUGHT
name: "thought.HUMAN LAW"
alias: "Thought: Human Law"
parent: "topic.LAW"
en_content: "Without accountability, there is no foundation for human law or human hope."
tags: ["humanity", "god", "accountable", "law", "hope"]
ptopic: "[[topic-LAW]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HUMAN LAW",
    alias: "Thought: Human Law",
    parent: "topic.LAW",
    tags: ["humanity", "god", "accountable", "law", "hope"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HUMAN LAW",
    ctype: "THOUGHT",
    en_title: "Human Law",
    en_content: "Without accountability, there is no foundation for human law or human hope.",
    es_title: "LEY HUMANA",
    es_content: "Sin rendición de cuentas, no hay fundamento para la ley humana ni para la esperanza humana.",
    fr_title: "DROIT HUMAIN",
    fr_content: "Sans responsabilité, il n’y a pas de fondement à la loi humaine ni à l’espoir humain.",
    hi_title: "मानव कानून",
    hi_content: "जवाबदेही के बिना, मानव कानून या मानवीय आशा का कोई आधार नहीं है।",
    zh_title: "rén lèi fǎ",
    zh_content: "méi yǒu wèn zé zhì ， rén lèi fǎ lǜ huò rén lèi xī wàng jiù méi yǒu jī chǔ 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HUMAN LAW"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LAW"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LAW->HUMAN LAW"
RETURN t, parent;
```
