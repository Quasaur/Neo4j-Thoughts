---
name: "thought.THE NEXT LIFE IMPORTANCE"
alias: "Thought: The Next Life Importance"
type: THOUGHT
en_content: "There's NOTHING in this life that's more important than The Next Life!"
parent: "topic.SPIRITUALITY"
tags:
- life
- eternity
- importance
- spirituality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-May-2014)
CREATE (t:THOUGHT {
    name: "thought.THE NEXT LIFE IMPORTANCE",
    alias: "Thought: The Next Life Importance",
    parent: "topic.SPIRITUALITY",
    tags: ['life', 'eternity', 'importance', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE NEXT LIFE IMPORTANCE",
    en_title: "The Next Life Importance",
    en_content: "There's NOTHING in this life that's more important than The Next Life!",
    es_title: "La Importancia de la Próxima Vida",
    es_content: "¡NO hay NADA en esta vida que sea más importante que La Próxima Vida!",
    fr_title: "L'Importance de la Vie Future",
    fr_content: "Il n'y a RIEN dans cette vie qui soit plus important que La Vie Future !",
    hi_title: "अगले जीवन का महत्व",
    hi_content: "इस जीवन में कुछ भी अगले जीवन से अधिक महत्वपूर्ण नहीं है!",
    zh_title: "Lai Shi De Zhong Yao Xing",
    zh_content: "Zai Zhe Ge Shi Jie Shang Mei You Ren He Shi Qing Bi Lai Shi Geng Zhong Yao!"
});

MATCH (t:THOUGHT {name: "thought.THE NEXT LIFE IMPORTANCE"})
MATCH (c:CONTENT {name: "content.THE NEXT LIFE IMPORTANCE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE NEXT LIFE IMPORTANCE" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.THE NEXT LIFE IMPORTANCE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->THE NEXT LIFE IMPORTANCE" }]->(child);
```
