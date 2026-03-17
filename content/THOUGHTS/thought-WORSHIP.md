---
type: THOUGHT
name: "thought.WORSHIP"
alias: "Thought: Worship"
parent: "topic.SPIRITUALITY"
tags: ["worship", "praise", "prayer", "fellowship", "eternalfather"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.WORSHIP",
    alias: "Thought: Worship",
    parent: "topic.SPIRITUALITY",
    tags: ["worship", "praise", "prayer", "fellowship", "eternalfather"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WORSHIP",
    ctype: "THOUGHT",
    en_title: "Worship",
    en_content: "",
    es_title: "CULTO",
    es_content: "Una vida de oración sin adoración siempre será incompleta; un niño nacido muerto.",
    fr_title: "CULTE",
    fr_content: "Une vie de prière sans culte sera toujours incomplète ; un enfant mort-né.",
    hi_title: "पूजा",
    hi_content: "आराधना के बिना प्रार्थना जीवन सदैव अधूरा रहेगा; एक मृत बच्चा.",
    zh_title: "chóng bài",
    zh_content: "méi yǒu jìng bài de dǎo gào shēng huó yǒng yuǎn shì bù wán zhěng de ； méi yǒu jìng bài de dǎo gào shēng huó yǒng yuǎn shì bù wán zhěng de 。 yí gè sǐ chǎn de hái zi"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WORSHIP"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->WORSHIP"
RETURN t, parent;
```
