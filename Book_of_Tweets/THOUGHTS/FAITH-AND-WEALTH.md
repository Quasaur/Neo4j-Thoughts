---
name: "thought.FAITH AND WEALTH"
alias: "Thought: Faith And Wealth"
type: THOUGHT
en_content: "Faith is the closest we can get to free wealth."
parent: "topic.FAITH"
tags:
- faith
- wealth
- spiritual_riches
- provision
- belief
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.FAITH AND WEALTH",
    alias: "Thought: Faith And Wealth",
    parent: "topic.FAITH",
    tags: ["faith", "wealth", "spiritual_riches", "provision", "belief"],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH AND WEALTH",
    en_title: "Faith And Wealth",
    en_content: "Faith is the closest we can get to free wealth.",
    es_title: "Fe Y Riqueza",
    es_content: "La fe es lo más cerca que podemos llegar de la riqueza gratuita.",
    fr_title: "Foi Et Richesse",
    fr_content: "La foi est ce qui nous rapproche le plus de la richesse gratuite.",
    hi_title: "विश्वास और धन",
    hi_content: "विश्वास निःशुल्क धन के सबसे करीब हम पहुँच सकते हैं।",
    zh_title: "Xinyang Yu Caifu",
    zh_content: "Xinyang shi women zui jiejin mianfei caifu de fangshi."
});

MATCH (t:THOUGHT {name: "thought.FAITH AND WEALTH"})
MATCH (c:CONTENT {name: "content.FAITH AND WEALTH"})
MERGE (t)-[:HAS_CONTENT {name: "edge.FAITH AND WEALTH"}]->(c);

MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:THOUGHT {name: "thought.FAITH AND WEALTH"})
MERGE (parent)-[:HAS_THOUGHT {name: "FAITH >FAITH AND WEALTH"}]->(child);
```
