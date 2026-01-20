---
name: "thought.INTELLIGENT DESIGN"
alias: "Thought: Intelligent Design"
type: THOUGHT
en_content: "INTELLIGENT DESIGN!"
parent: "topic.CREATION"
tags:
- creation
- design
- intelligence
- truth
- science
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.INTELLIGENT DESIGN",
    alias: "Thought: Intelligent Design",
    parent: "topic.CREATION",
    tags: ['creation', 'design', 'intelligence', 'truth', 'science'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT DESIGN",
    en_title: "Intelligent Design",
    en_content: "INTELLIGENT DESIGN!",
    es_title: "Diseño Inteligente",
    es_content: "¡DISEÑO INTELIGENTE!",
    fr_title: "Conception Intelligente",
    fr_content: "CONCEPTION INTELLIGENTE !",
    hi_title: "बुद्धिमान डिज़ाइन",
    hi_content: "बुद्धिमान डिज़ाइन!",
    zh_title: "Zhìhuì shèjì 智慧设计",
    zh_content: "Zhìnéng shèjì! 智能设计！"
});

MATCH (t:THOUGHT {name: "thought.INTELLIGENT DESIGN"})
MATCH (c:CONTENT {name: "content.INTELLIGENT DESIGN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.INTELLIGENT DESIGN" }]->(c);

MATCH (parent:TOPIC {name: "topic.CREATION"})
MATCH (child:THOUGHT {name: "thought.INTELLIGENT DESIGN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >INTELLIGENT DESIGN" }]->(child);
```
