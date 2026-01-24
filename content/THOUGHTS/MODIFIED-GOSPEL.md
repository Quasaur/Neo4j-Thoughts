---
name: "thought.MODIFIED_GOSPEL"
alias: "Thought: MODIFIED GOSPEL"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- gospel
- human
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MODIFIED_GOSPEL",
    alias: "Thought: MODIFIED GOSPEL",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "human"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.MODIFIED_GOSPEL",
    en_title: "MODIFIED GOSPEL",
    en_content: "Christians LOVE to inject their \"wisdom\" into the Gospel; nowhere does this happen more than in the American church.",
    es_title: "EVANGELIO MODIFICADO",
    es_content: "A los cristianos les ENCANTA inyectar su \"sabiduría\" en el Evangelio; En ningún lugar esto sucede más que en la iglesia estadounidense.",
    fr_title: "ÉVANGILE MODIFIÉ",
    fr_content: "Les chrétiens AIMENT injecter leur « sagesse » dans l’Évangile ; Cela ne se produit nulle part plus que dans l’Église américaine.",
    hi_title: "संशोधित सुसमाचार",
    hi_content: "ईसाई सुसमाचार में अपनी \"बुद्धि\" डालना पसंद करते हैं; अमेरिकी चर्च से ज्यादा ऐसा कहीं नहीं होता।",
    zh_title: "gǎi liáng fú yīn",
    zh_content: "jī dū tú xǐ huān jiāng tā men de “ zhì huì ” zhù rù fú yīn zhōng ； zhè zhǒng qíng kuàng zài měi guó jiào huì zhōng zuì wèi cháng jiàn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MODIFIED_GOSPEL" AND c.name = "content.MODIFIED_GOSPEL"
MERGE (t)-[:HAS_CONTENT {name: "edge.MODIFIED_GOSPEL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.MODIFIED_GOSPEL"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->MODIFIED_GOSPEL"}]->(child);
```
