---
type: THOUGHT
name: "thought.FAITH IN SELF VS CREATOR"
alias: "Thought: Faith In Self Vs Creator"
parent: "topic.FAITH"
en_content: "We have more faith in ourselves than we have in our Creator; this is a recipe for disaster."
tags: ["faith", "self", "creator", "disaster", "trust"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FAITH IN SELF VS CREATOR",
    alias: "Thought: Faith In Self Vs Creator",
    parent: "topic.FAITH",
    tags: ['faith', 'self', 'creator', 'disaster', 'trust'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH IN SELF VS CREATOR",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FAITH IN SELF VS CREATOR"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITH->FAITH IN SELF VS CREATOR"
RETURN t, parent;
```
