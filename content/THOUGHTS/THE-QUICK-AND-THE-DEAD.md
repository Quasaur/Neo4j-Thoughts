---
name: "thought.THE_QUICK_AND_THE_DEAD"
alias: "Thought: THE QUICK AND THE DEAD"
type: THOUGHT
parent: topic.SPIRITUALITY
tags:
- eternallife
- immortality
- spirituality
- god
- jesuschrist
neo4j: true
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_QUICK_AND_THE_DEAD",
    alias: "Thought: THE QUICK AND THE DEAD",
    parent: "topic.SPIRITUALITY",
    tags: ["eternallife", "immortality", "spirituality", "god", "jesuschrist"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE_QUICK_AND_THE_DEAD",
    en_title: "THE QUICK AND THE DEAD",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_QUICK_AND_THE_DEAD" AND c.name = "content.THE_QUICK_AND_THE_DEAD"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_QUICK_AND_THE_DEAD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.THE_QUICK_AND_THE_DEAD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.SPIRITUALITY->THE_QUICK_AND_THE_DEAD"}]->(child);
```
