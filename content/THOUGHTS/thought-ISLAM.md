---
type: THOUGHT
name: "thought.ISLAM"
alias: "Thought: Islam"
parent: "topic.RELIGION"
tags: ["islam", "religion", "antichrist", "demonic", "deception"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ISLAM",
    alias: "Thought: Islam",
    parent: "topic.RELIGION",
    tags: ["islam", "religion", "antichrist", "demonic", "deception"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ISLAM",
    ctype: "THOUGHT",
    en_title: "Islam",
 es_title: "ISLAM",
 fr_title: "ISLAM",
 hi_title: "इस्लाम",
 zh_title: "yī sī lán jiào",
    en_content: "",
 es_content: "NO hay armonía posible entre El Evangelio de Jesucristo (que es la única Barrera entre la humanidad y El Lago de Fuego y Azufre) y la Religión de Mahoma.",
 fr_content: "Il n’y a AUCUNE harmonie possible entre l’Évangile de Jésus-Christ (qui est la seule barrière entre l’humanité et l’étang de feu et de soufre) et la religion de Mahomet.",
 hi_content: "ईसा मसीह के सुसमाचार (जो मानवता और आग और गंधक की झील के बीच एकमात्र बाधा है) और मोहम्मद के धर्म के बीच कोई सामंजस्य संभव नहीं है।",
 zh_content: "yē sū jī dū de fú yīn （ zhè shì rén lèi yǔ huǒ liú hú zhī jiān de wéi yī zhàng ài ） yǔ mù hǎn mò dé de zōng jiào zhī jiān bù kě néng yǒu hé xié 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ISLAM" AND c.name = "content.ISLAM"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ISLAM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.ISLAM"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.RELIGION->ISLAM"}]->(child);
```