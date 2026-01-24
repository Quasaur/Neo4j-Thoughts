---
name: "thought.FAITH IN SELF VS CREATOR"
alias: "Thought: Faith In Self Vs Creator"
type: THOUGHT
en_content: "We have more faith in ourselves than we have in our Creator; this is a recipe for disaster."
parent: "topic.FAITH"
tags:
- faith
- self
- creator
- disaster
- trust
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011d)
CREATE (t:THOUGHT {
    name: "thought.FAITH IN SELF VS CREATOR",
    alias: "Thought: Faith In Self Vs Creator",
    parent: "topic.FAITH",
    tags: ['faith', 'self', 'creator', 'disaster', 'trust'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH IN SELF VS CREATOR",
    en_title: "Faith In Self Vs Creator",
    en_content: "We have more faith in ourselves than we have in our Creator; this is a recipe for disaster.",
    es_title: "Fe en Uno Mismo Vs el Creador",
    es_content: "Tenemos más fe en nosotros mismos que en nuestro Creador; esta es una receta para el desastre.",
    fr_title: "Foi en Soi Vs le Créateur",
    fr_content: "Nous avons plus de foi en nous-mêmes qu'en notre Créateur ; c'est une recette pour le désastre.",
    hi_title: "स्वयं में विश्वास बनाम सृष्टिकर्ता",
    hi_content: "हमारा अपने सृष्टिकर्ता की अपेक्षा स्वयं में अधिक विश्वास है; यह विनाश की एक विधि है।",
    zh_title: "Dui Ziji de Xinxin Yu Dui Zaowuzhu de Xinxin",
    zh_content: "Women dui ziji de xinxin chaoguo le dui Zaowuzhu de xinxin; zhe shi zainan de peifang."
});

MATCH (t:THOUGHT {name: "thought.FAITH IN SELF VS CREATOR"})
MATCH (c:CONTENT {name: "content.FAITH IN SELF VS CREATOR"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAITH IN SELF VS CREATOR" }]->(c);

MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:THOUGHT {name: "thought.FAITH IN SELF VS CREATOR"})
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH->FAITH IN SELF VS CREATOR" }]->(child);
```
