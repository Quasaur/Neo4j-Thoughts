---
name: "thought.IDENTITY IN GOD"
alias: "Thought: Identity In God"
type: THOUGHT
en_content: "The only reason anyone would want to be \"normal\" or \"like everyone else\" is that they do not know who they are in God!"
parent: "topic.SPIRITUALITY"
tags:
- identity
- normal
- god
- character
- value
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.IDENTITY IN GOD",
    alias: "Thought: Identity In God",
    parent: "topic.SPIRITUALITY",
    tags: ['identity', 'normal', 'god', 'character', 'value'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IDENTITY IN GOD",
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

MATCH (t:THOUGHT {name: "thought.IDENTITY IN GOD"})
MATCH (c:CONTENT {name: "content.IDENTITY IN GOD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.IDENTITY IN GOD" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.IDENTITY IN GOD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >IDENTITY IN GOD" }]->(child);
```
