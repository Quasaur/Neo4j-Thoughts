---
name: "thought.FALSE RELIGION TWIN"
alias: "Thought: False Religion Twin"
type: THOUGHT
en_content: "The Twin of Wickedness is False Religion."
parent: "topic.RELIGION"
tags:
- religion
- wickedness
- evil
- truth
- character
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.FALSE RELIGION TWIN",
    alias: "Thought: False Religion Twin",
    parent: "topic.RELIGION",
    tags: ['religion', 'wickedness', 'evil', 'truth', 'character'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FALSE RELIGION TWIN",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FALSE RELIGION TWIN" AND c.name = "content.FALSE RELIGION TWIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FALSE RELIGION TWIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.FALSE RELIGION TWIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >FALSE RELIGION TWIN" }]->(child);
```
