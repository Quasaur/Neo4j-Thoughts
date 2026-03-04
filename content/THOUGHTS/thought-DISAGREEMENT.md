---
type: THOUGHT
name: "thought.DISAGREEMENT"
alias: "Thought: Disagreement"
parent: "topic.FAITH"
tags: ["faith", "doctrine", "apostasy", "heresy", "conflict"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DISAGREEMENT",
    alias: "Thought: Disagreement",
    parent: "topic.FAITH",
    tags: ["faith", "doctrine", "apostasy", "heresy", "conflict"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DISAGREEMENT",
    ctype: "THOUGHT",
    en_title: "Disagreement",
    en_content: "Arguing with the Devil is extremely dangerous because far too often we share his point of view.",
 es_title: "DESACUERDO",
 es_content: "Discutir con el Diablo es extremadamente peligroso porque con demasiada frecuencia compartimos su punto de vista.",
 fr_title: "DÉSACCORD",
 fr_content: "Discuter avec le Diable est extrêmement dangereux car bien trop souvent nous partageons son point de vue.",
 hi_title: "बहस",
 hi_content: "शैतान के साथ बहस करना बेहद खतरनाक है क्योंकि अक्सर हम उसका दृष्टिकोण साझा करते हैं।",
 zh_title: "fēn qí",
 zh_content: "yǔ mó guǐ zhēng lùn shì jí qí wēi xiǎn de ， yīn wèi wǒ men cháng cháng tóng yì tā de guān diǎn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DISAGREEMENT" AND c.name = "content.DISAGREEMENT"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DISAGREEMENT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.DISAGREEMENT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITH->DISAGREEMENT"}]->(child);
```