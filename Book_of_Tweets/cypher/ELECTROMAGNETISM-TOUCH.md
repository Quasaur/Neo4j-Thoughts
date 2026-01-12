---
name: "thought.ELECTROMAGNETISM TOUCH"
alias: "Thought: Electromagnetism Touch"
type: THOUGHT
en_content: "Under normal circumstances, electromagnetism prevents any 2 surfaces from touching...God is great!"
parent: "topic.CREATION"
tags:
- science
- physics
- creation
- design
- power
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.ELECTROMAGNETISM TOUCH",
    alias: "Thought: Electromagnetism Touch",
    parent: "topic.CREATION",
    tags: ['science', 'physics', 'creation', 'design', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ELECTROMAGNETISM TOUCH",
    en_title: "Electromagnetism Touch",
    en_content: "Under normal circumstances, electromagnetism prevents any 2 surfaces from touching...God is great!",
    es_title: "Toque Electromagnético",
    es_content: "En circunstancias normales, el electromagnetismo impide que cualquier 2 superficies se toquen...¡Dios es grande!",
    fr_title: "Toucher Électromagnétique",
    fr_content: "Dans des circonstances normales, l'électromagnétisme empêche 2 surfaces de se toucher...Dieu est grand !",
    hi_title: "विद्युत चुम्बकीय स्पर्श",
    hi_content: "सामान्य परिस्थितियों में, विद्युत चुम्बकत्व किसी भी 2 सतहों को छूने से रोकता है...परमेश्वर महान है!",
    zh_title: "Dianci Chumo",
    zh_content: "Zai zhengchang qingkuang xia, dianci zu zhi renhe liang ge biaomian xiangchu...Shangdi shi weida de!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ELECTROMAGNETISM TOUCH" AND c.name = "content.ELECTROMAGNETISM TOUCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ELECTROMAGNETISM TOUCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.ELECTROMAGNETISM TOUCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >ELECTROMAGNETISM TOUCH" }]->(child);
```
