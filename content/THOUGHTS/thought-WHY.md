---
type: THOUGHT
name: "thought.WHY"
alias: "Thought: Why"
parent: "topic.PSYCHOLOGY"
tags: ["children", "adults", "demanded", "cause", "why"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.WHY",
    alias: "Thought: Why",
    parent: "topic.PSYCHOLOGY",
    tags: ["children", "adults", "demanded", "cause", "why"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.WHY",
    ctype: "THOUGHT",
    en_title: "Why",
 es_title: "POR QUÉ",
 fr_title: "POURQUOI",
 hi_title: "क्यों",
 zh_title: "wèi shén me",
    en_content: "",
 es_content: "¿Qué es lo que los niños suelen pasar por alto pero que los adultos exigen con frecuencia?
Una explicación.",
 fr_content: "Qu'est-ce qui est souvent négligé par les enfants mais fréquemment exigé par les adultes ?
Une explication.",
 hi_content: "वह कौन सी चीज़ है जिसे अक्सर बच्चे नज़रअंदाज़ कर देते हैं लेकिन बड़े लोग अक्सर उसकी मांग करते हैं?
एक स्पष्टीकरण.",
 zh_content: "shén me shì hái zi men cháng cháng hū shì dàn dà rén cháng cháng yāo qiú de ？
 yí gè jiě shì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WHY" AND c.name = "content.WHY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.WHY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.WHY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->WHY"}]->(child);
```