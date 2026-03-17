---
type: THOUGHT
name: "thought.RESPECTING OUR BODIES"
alias: "Thought: Respecting Our Bodies"
parent: "topic.ATTITUDE"
en_content: "We don't respect our own bodies yet we want others to respect us!"
tags: ["respect", "body", "attitude", "character", "integrity"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.RESPECTING OUR BODIES",
    alias: "Thought: Respecting Our Bodies",
    parent: "topic.ATTITUDE",
    tags: ['respect', 'body', 'attitude', 'character', 'integrity'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RESPECTING OUR BODIES",
    ctype: "THOUGHT",
    en_title: "Respecting Our Bodies",
    en_content: "We don't respect our own bodies yet we want others to respect us!",
    es_title: "Respetando Nuestros Cuerpos",
    es_content: "¡No respetamos nuestros propios cuerpos pero queremos que otros nos respeten!",
    fr_title: "Respecter Nos Corps",
    fr_content: "Nous ne respectons pas nos propres corps mais nous voulons que les autres nous respectent !",
    hi_title: "अपने शरीर का सम्मान करना",
    hi_content: "हम अपने शरीर का सम्मान नहीं करते फिर भी चाहते हैं कि दूसरे हमारा सम्मान करें!",
    zh_title: "Zun Zhong Wo Men De Shen Ti",
    zh_content: "Wo men bu zun zhong zi ji de shen ti, que yao qiu bie ren zun zhong wo men!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RESPECTING OUR BODIES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->RESPECTING OUR BODIES"
RETURN t, parent;
```
