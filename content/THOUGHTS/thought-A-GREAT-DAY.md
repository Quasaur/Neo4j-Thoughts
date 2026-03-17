---
type: THOUGHT
name: "thought.A GREAT DAY"
alias: "Thought: A Great Day"
parent: "topic.HUMOR"
en_content: "Today was great--except for the sleeping, eating and working."
tags: ["daily_routine", "eating", "sleeping", "working", "humor"]
ptopic: "[[topic-HUMOR]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.A GREAT DAY",
    alias: "Thought: A Great Day",
    parent: "topic.HUMOR",
    tags: ["daily_routine", "eating", "sleeping", "working", "humor"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.A GREAT DAY",
    ctype: "THOUGHT",
    en_title: "A Great Day",
    en_content: "Today was great--except for the sleeping, eating and working.",
    es_title: "Un gran día",
    es_content: "Hoy estuvo genial, excepto por dormir, comer y trabajar.",
    fr_title: "Une belle journée",
    fr_content: "Aujourd'hui, c'était génial, sauf pour dormir, manger et travailler.",
    hi_title: "एक महान दिन",
    hi_content: "आज का दिन बहुत अच्छा था--सोने, खाने और काम करने के अलावा।",
    zh_title: "měi hǎo de yī tiān",
    zh_content: "jīn tiān guò dé hěn hǎo —— chú le shuì jiào 、 chī fàn hé gōng zuò 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.A GREAT DAY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMOR"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMOR->A GREAT DAY"
RETURN t, parent;
```
