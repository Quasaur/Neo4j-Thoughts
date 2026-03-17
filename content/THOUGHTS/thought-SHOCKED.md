---
type: THOUGHT
name: "thought.SHOCKED"
alias: "Thought: Shocked"
parent: "topic.EVIL"
en_content: "It's a strange thing: we are all sinners, but we are \"shocked\" and \"appalled\" when one of us sins!"
tags: ["hypocrisy", "shocked", "appalled", "sinner", "sinning"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SHOCKED",
    alias: "Thought: Shocked",
    parent: "topic.EVIL",
    tags: ["hypocrisy", "shocked", "appalled", "sinner", "sinning"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SHOCKED",
    ctype: "THOUGHT",
    en_title: "Shocked",
    en_content: "It's a strange thing: we are all sinners, but we are \\\"shocked\\\" and \\\"appalled\\\" when one of us sins!",
    es_title: "Conmocionado",
    es_content: "Es extraño: todos somos pecadores, pero nos sentimos “conmocionados” y “horrorizados” cuando alguno de nosotros peca.",
    fr_title: "Choqués",
    fr_content: "C'est étrange : nous sommes tous pécheurs, mais nous sommes « choqués » et « consternés » quand l'un d'entre nous pèche !",
    hi_title: "हैरान",
    hi_content: "यह एक अजीब बात है: हम सभी पापी हैं, लेकिन जब हममें से कोई पाप करता है तो हम \\\"हैरान\\\" और \\\"हैरान\\\" हो जाते हैं!",
    zh_title: "Zhènjīng",
    zh_content: "zhè hěn qíguài: Wǒmen dōu shì zuìrén, dàn dāng wǒmen zhōng yǒurén fànzuì shí, wǒmen què gǎndào \\“zhènjīng\\” hé \\“fènkǎi\\”!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SHOCKED"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->SHOCKED"
RETURN t, parent;
```
