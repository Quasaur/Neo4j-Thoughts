---
type: THOUGHT
name: "thought.RESULTS"
alias: "Thought: RESULTS"
parent: "topic.PSYCHOLOGY"
tags: ["gunviolence", "massshootings", "gunlaws", "nra", "uscongress"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.RESULTS",
    alias: "Thought: RESULTS",
    parent: "topic.PSYCHOLOGY",
    tags: ["gunviolence", "massshootings", "gunlaws", "nra", "uscongress"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.RESULTS",
    ctype: "THOUGHT",
    en_title: "RESULTS",
 es_title: "RESULTADOS",
 fr_title: "RÉSULTATS",
 hi_title: "परिणाम",
 zh_title: "jié guǒ",
    en_content: "",
 es_content: "Los resultados hablan por sí solos: la NRA y el Congreso de los Estados Unidos quieren que nos MATREMOS UNOS A OTROS... para su beneficio y a nuestra costa.",
 fr_content: "Les résultats parlent d’eux-mêmes : la NRA et le Congrès américain veulent que nous nous entretuions… pour leur profit et à nos dépens.",
 hi_content: "परिणाम स्वयं बोलते हैं: एनआरए और अमेरिकी कांग्रेस चाहते हैं कि हम एक-दूसरे को मार डालें...अपने लाभ के लिए और अपने खर्च पर।",
 zh_content: "jié guǒ bù yán ér yù ： quán guó bù qiāng xié huì hé měi guó guó huì xī wàng wǒ men hù xiāng cán shā …… wèi le tā men de lì yì ， ér wǒ men què fù chū dài jià 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.RESULTS" AND c.name = "content.RESULTS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.RESULTS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.RESULTS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->RESULTS"}]->(child);
```