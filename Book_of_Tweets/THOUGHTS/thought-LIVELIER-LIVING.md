---
type: THOUGHT
name: "thought.LIVELIER LIVING"
alias: "Thought: Livelier Living"
parent: "topic.SPIRITUALITY"
en_content: "Soap makes water wetter; Jesus Christ makes living livelier!"
tags: ["jesus", "life", "joy", "spirituality", "character"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012h)
CREATE (t:THOUGHT {    name: "thought.LIVELIER LIVING",
    alias: "Thought: Livelier Living",
    parent: "topic.SPIRITUALITY",
    tags: ['jesus', 'life', 'joy', 'spirituality', 'character'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.LIVELIER LIVING",
    ctype: "THOUGHT",
    en_title: "Livelier Living",
    en_content: "Soap makes water wetter; Jesus Christ makes living livelier!",
    es_title: "Vivir Más Vivo",
    es_content: "El jabón hace el agua más húmeda; ¡Jesucristo hace el vivir más vivo!",
    fr_title: "Vivre Plus Vivant",
    fr_content: "Le savon rend l'eau plus mouillante ; Jésus-Christ rend la vie plus vivante !",
    hi_title: "जीवंत जीवन",
    hi_content: "साबुन पानी को और गीला बनाता है; यीशु मसीह जीवन को और जीवंत बनाते हैं!",
    zh_title: "Geng Huo Yue De Sheng Huo",
    zh_content: "Fei Zao Shi Shui Geng Shi Run; Ye Su Ji Du Shi Sheng Huo Geng Huo Yue!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIVELIER LIVING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->LIVELIER LIVING"
RETURN t, parent;
```
