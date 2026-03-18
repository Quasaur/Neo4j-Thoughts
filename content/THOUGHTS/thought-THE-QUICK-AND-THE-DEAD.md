---
type: THOUGHT
name: "thought.THE QUICK AND THE DEAD"
alias: "Thought: The Quick And The Dead"
parent: "topic.SPIRITUALITY"
en_content: |
  You are either alive to God and dead to self…or you are alive to self and dead to God.
  Luke 14:26"
tags: ["eternal_life", "immortality", "spirituality", "god", "jesus_christ"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "\"thought.THE QUICK AND THE DEAD\"",
    alias: "Thought: The Quick And The Dead",
    parent: "\"topic.SPIRITUALITY\"",
    tags: ["eternal_life", "immortality", "spirituality", "god", "jesus_christ"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE QUICK AND THE DEAD",
    ctype: "THOUGHT",
    en_title: "The Quick and the Dead",
    en_content: "You are either alive to God and dead to self…or you are alive to self and dead to God.
Luke 14:26",
    es_title: "LOS VIVOS Y LOS MUERTOS",
    es_content: "O estás vivo para Dios y muerto para ti mismo... o estás vivo para ti mismo y muerto para Dios.
Lucas 14:26",
    fr_title: "LES RAPIDES ET LES MORTS",
    fr_content: "Soit vous êtes vivant pour Dieu et mort pour vous-même… soit vous êtes vivant pour vous-même et mort pour Dieu.
Luc 14:26",
    hi_title: "त्वरित और मृत",
    hi_content: "आप या तो ईश्वर के लिए जीवित हैं और स्वयं के लिए मृत हैं...या आप स्वयं के लिए जीवित हैं और ईश्वर के लिए मृत हैं।
लूका 14:26",
    zh_title: "kuài zhě yǔ sǐ zhě",
    zh_content: "nǐ yào me xiàng shén huó zhe ， xiàng zì jǐ sǐ …… yào me xiàng zì jǐ huó zhe ， xiàng shén sǐ 。
 lù jiā fú yīn  14:26"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.'"thought.THE QUICK AND THE DEAD"'"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->THE QUICK AND THE DEAD"thought.THE QUICK AND THE DEAD"'"
RETURN t, parent;
```
