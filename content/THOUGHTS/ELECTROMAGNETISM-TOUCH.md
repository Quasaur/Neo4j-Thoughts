---
name: "thought.ELECTROMAGNETISM TOUCH"
alias: "Thought: Electromagnetism Touch"
type: THOUGHT
en_content: "Under normal circumstances, electromagnetism prevents any 2 surfaces from touching...God is great!"
parent: "topic.PHYSICS"
tags:
- science
- physics
- creation
- design
- power
level: 6
neo4j: true
ptopic: "[[topic-PHYSICS]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.ELECTROMAGNETISM TOUCH",
    alias: "Thought: Electromagnetism Touch",
    parent: "topic.PHYSICS",
    tags: ['science', 'physics', 'creation', 'design', 'power'],
    notes: "",
    level: 6
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

MATCH (t:THOUGHT {name: "thought.ELECTROMAGNETISM TOUCH"})
MATCH (c:CONTENT {name: "content.ELECTROMAGNETISM TOUCH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ELECTROMAGNETISM TOUCH" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHYSICS"})
MATCH (child:THOUGHT {name: "thought.ELECTROMAGNETISM TOUCH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHYSICS >ELECTROMAGNETISM TOUCH" }]->(child);
```
