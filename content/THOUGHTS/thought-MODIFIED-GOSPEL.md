---
type: THOUGHT
name: "thought.MODIFIED GOSPEL"
alias: "Thought: Modified Gospel"
parent: "topic.THE-GOSPEL"
en_content: "Christians LOVE to inject their \"wisdom\" into the Gospel; nowhere does this happen more than in the American church."
tags: ["gospel", "human"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.MODIFIED GOSPEL",
    alias: "Thought: Modified Gospel",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "human"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.MODIFIED GOSPEL",
    ctype: "THOUGHT",
    en_title: "Modified Gospel",
    en_content: "Christians LOVE to inject their \\\"wisdom\\\" into the Gospel; nowhere does this happen more than in the American church.",
    es_title: "EVANGELIO MODIFICADO",
    es_content: "A los cristianos les ENCANTA inyectar su \\\"sabiduría\\\" en el Evangelio; En ningún lugar esto sucede más que en la iglesia estadounidense.",
    fr_title: "ÉVANGILE MODIFIÉ",
    fr_content: "Les chrétiens AIMENT injecter leur « sagesse » dans l’Évangile ; Cela ne se produit nulle part plus que dans l’Église américaine.",
    hi_title: "संशोधित सुसमाचार",
    hi_content: "ईसाई सुसमाचार में अपनी \\\"बुद्धि\\\" डालना पसंद करते हैं; अमेरिकी चर्च से ज्यादा ऐसा कहीं नहीं होता।",
    zh_title: "gǎi liáng fú yīn",
    zh_content: "jī dū tú xǐ huān jiāng tā men de “ zhì huì ” zhù rù fú yīn zhōng ； zhè zhǒng qíng kuàng zài měi guó jiào huì zhōng zuì wèi cháng jiàn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MODIFIED GOSPEL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE-GOSPEL->MODIFIED GOSPEL"
RETURN t, parent;
```
