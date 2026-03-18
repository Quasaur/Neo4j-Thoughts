---
type: THOUGHT
name: "thought.INVISIBLE IN IMPOSSIBLE"
alias: "Thought: Invisible In Impossible"
parent: "topic.THE GODHEAD"
en_content: "God is invisible except in the impossible."
tags: ["god", "miracle", "invisible", "impossible", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Apr-2013)
CREATE (t:THOUGHT {    name: "thought.INVISIBLE IN IMPOSSIBLE",
    alias: "Thought: Invisible In Impossible",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'miracle', 'invisible', 'impossible', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.INVISIBLE IN IMPOSSIBLE",
    ctype: "THOUGHT",
    en_title: "Invisible In Impossible",
    en_content: "God is invisible except in the impossible.",
    es_title: "Invisible En Lo Imposible",
    es_content: "Dios es invisible excepto en lo imposible.",
    fr_title: "Invisible Dans L'Impossible",
    fr_content: "Dieu est invisible sauf dans l'impossible.",
    hi_title: "असंभव में अदृश्य",
    hi_content: "परमेश्वर असंभव के अलावा अदृश्य है।",
    zh_title: "Zai Bu Ke Neng Zhong De Bu Ke Jian",
    zh_content: "Chu Le Zai Bu Ke Neng De Shi Qing Shang, Shang Di Shi Bu Ke Jian De."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INVISIBLE IN IMPOSSIBLE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->INVISIBLE IN IMPOSSIBLE"
RETURN t, parent;
```
