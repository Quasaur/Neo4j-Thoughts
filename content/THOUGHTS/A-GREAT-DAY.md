---
name: "thought.A GREAT DAY"
alias: "Thought: A Great Day"
type: THOUGHT
parent: topic.HUMOR
tags:
- daily_routine
- eating
- sleeping
- working
- humor
neo4j: true
ptopic: "[[topic-HUMOR]]"
level: 5
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.A GREAT DAY",
    alias: "Thought: A Great Day",
    parent: "topic.HUMOR",
    tags: ["dailyroutine", "eating", "sleeping", "working", "humor"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.A_GREAT_DAY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.A GREAT DAY" AND c.name = "content.A GREAT DAY"
MERGE (t)-[:HAS_CONTENT {name: "edge.A GREAT DAY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMOR" AND child.name = "thought.A GREAT DAY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMOR->A GREAT DAY"}]->(child);
```