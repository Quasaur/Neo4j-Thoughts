---
name: "thought.ALL THINGS FOR HIM"
alias: "Thought: All Things For Him"
type: THOUGHT
en_content: "All things are from, to and for Him; this is fitting, for He is worthy."
parent: "topic.THE GODHEAD"
tags:
- worthyship
- glory
- divinity
- creation
- worship
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011b)
CREATE (t:THOUGHT {
    name: "thought.ALL THINGS FOR HIM",
    alias: "Thought: All Things For Him",
    parent: "topic.THE GODHEAD",
    tags: ['worthyship', 'glory', 'divinity', 'creation', 'worship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ALL THINGS FOR HIM",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ALL THINGS FOR HIM" AND c.name = "content.ALL THINGS FOR HIM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALL THINGS FOR HIM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ALL THINGS FOR HIM"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ALL THINGS FOR HIM" }]->(child);
```
