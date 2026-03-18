---
type: THOUGHT
name: "thought.IDENTITY IN GOD"
alias: "Thought: Identity In God"
parent: "topic.SPIRITUALITY"
en_content: "The only reason anyone would want to be \"normal\" or \"like everyone else\" is that they do not know who they are in God!"
tags: ["identity", "normal", "god", "character", "value"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Oct-2012)
CREATE (t:THOUGHT {    name: "thought.IDENTITY IN GOD",
    alias: "Thought: Identity In God",
    parent: "topic.SPIRITUALITY",
    tags: ['identity', 'normal', 'god', 'character', 'value'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.IDENTITY IN GOD",
    ctype: "THOUGHT",
    en_title: "Identity In God",
    en_content: "The only reason anyone would want to be \"normal\" or \"like everyone else\" is that they do not know who they are in God!",
    es_title: "Identidad En Dios",
    es_content: "La única razón por la que alguien querría ser",
    fr_title: "Identité En Dieu",
    fr_content: "La seule raison pour laquelle quelqu'un voudrait être",
    hi_title: "परमेश्वर में पहचान",
    hi_content: "कोई भी व्यक्ति होना चाहेगा इसका एकमात्र कारण",
    zh_title: "Zai Shen Li De Shen Fen",
    zh_content: "Ren Men Xiang Yao Cheng Wei De Wei Yi Yuan Yin"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.IDENTITY IN GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->IDENTITY IN GOD"
RETURN t, parent;
```
