---
type: THOUGHT
name: "thought.FALSE RELIGION TWIN"
alias: "Thought: False Religion Twin"
parent: "topic.RELIGION"
en_content: "The Twin of Wickedness is False Religion."
tags: ["religion", "wickedness", "evil", "truth", "character"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Sep-2012)
CREATE (t:THOUGHT {    name: "thought.FALSE RELIGION TWIN",
    alias: "Thought: False Religion Twin",
    parent: "topic.RELIGION",
    tags: ['religion', 'wickedness', 'evil', 'truth', 'character'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.FALSE RELIGION TWIN",
    ctype: "THOUGHT",
    en_title: "False Religion Twin",
    en_content: "The Twin of Wickedness is False Religion.",
    es_title: "Gemelo de la Religión Falsa",
    es_content: "El Gemelo de la Maldad es la Religión Falsa.",
    fr_title: "Jumeau de la Fausse Religion",
    fr_content: "Le Jumeau de la Méchanceté est la Fausse Religion.",
    hi_title: "मिथ्या धर्म का जुड़वा",
    hi_content: "दुष्टता का जुड़वा मिथ्या धर्म है।",
    zh_title: "Jiǎ Zōngjiào Shuāngbāotāi",
    zh_content: "Xiéè de Shuāngbāotāi shì Jiǎ Zōngjiào."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FALSE RELIGION TWIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->FALSE RELIGION TWIN"
RETURN t, parent;
```
