---
type: THOUGHT
name: "thought.DIALOGUE"
alias: "Thought: DIALOGUE"
parent: "topic.EVIL"
tags: ["devil", "ego", "slave", "sin", "tongue"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DIALOGUE",
    alias: "Thought: DIALOGUE",
    parent: "topic.EVIL",
    tags: ["devil", "ego", "slave", "sin", "tongue"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DIALOGUE",
    ctype: "THOUGHT",
    en_title: "DIALOGUE",
 es_title: "DIÁLOGO",
 fr_title: "DIALOGUE",
 hi_title: "वार्ता",
 zh_title: "duì huà",
    en_content: "",
 es_content: "Discutir con el Diablo es extremadamente peligroso porque con demasiada frecuencia compartimos su punto de vista.",
 fr_content: "Discuter avec le Diable est extrêmement dangereux car bien trop souvent nous partageons son point de vue.",
 hi_content: "शैतान के साथ बहस करना बेहद खतरनाक है क्योंकि अक्सर हम उसका दृष्टिकोण साझा करते हैं।",
 zh_content: "yǔ mó guǐ zhēng lùn shì jí qí wēi xiǎn de ， yīn wèi wǒ men cháng cháng tóng yì tā de guān diǎn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DIALOGUE" AND c.name = "content.DIALOGUE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DIALOGUE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.DIALOGUE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->DIALOGUE"}]->(child);
```