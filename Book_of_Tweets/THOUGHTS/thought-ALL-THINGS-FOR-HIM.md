---
type: THOUGHT
name: "thought.ALL THINGS FOR HIM"
alias: "Thought: All Things For Him"
parent: "topic.THE GODHEAD"
en_content: "All things are from, to and for Him; this is fitting, for He is worthy."
tags: ["worthyship", "glory", "divinity", "creation", "worship"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011b)
CREATE (t:THOUGHT {    name: "thought.ALL THINGS FOR HIM",
    alias: "Thought: All Things For Him",
    parent: "topic.THE GODHEAD",
    tags: ['worthyship', 'glory', 'divinity', 'creation', 'worship'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.ALL THINGS FOR HIM",
    ctype: "THOUGHT",
    en_title: "All Things For Him",
    en_content: "All things are from, to and for Him; this is fitting, for He is worthy.",
    es_title: "Todas las Cosas Para Él",
    es_content: "Todas las cosas son de, para y por Él; esto es apropiado, porque Él es digno.",
    fr_title: "Toutes Choses Pour Lui",
    fr_content: "Toutes choses sont de, pour et par Lui ; ceci est convenable, car Il est digne.",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सब कुछ उससे, उसके लिए और उसके द्वारा है; यह उचित है, क्योंकि वह योग्य है।",
    zh_title: "Wànwù wèile tā",
    zh_content: "Wànwù dōu shì cóng tā, guīyú tā, wèile tā; zhè shì héyí de, yīnwèi tā pèidé."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ALL THINGS FOR HIM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->ALL THINGS FOR HIM"
RETURN t, parent;
```
