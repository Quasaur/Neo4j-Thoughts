---
type: THOUGHT
name: "thought.RESURRECTION BIRTH"
alias: "Thought: Eternal Life"
parent: "topic.THE GOSPEL"
en_content: "This life is my womb...The Resurrection is my birth."
tags: ["resurrection", "birth", "eternity", "hope", "mystery"]
ptopic:
level: 2
neo4j: false
---

```Cypher
CREATE (t:THOUGHT {    name: "thought.RESURRECTION BIRTH",
    alias: "Thought: Eternal Life",
    parent: "topic.THE GOSPEL",
    tags: ["resurrection", "birth", "eternity", "hope", "mystery"],
    level: 2});

CREATE (c:CONTENT {
    name: "content.RESURRECTION BIRTH",
    ctype: "THOUGHT",
    en_title: "Resurrection Birth",
    en_content: "This life is my womb...The Resurrection is my birth.",
    es_title: "Nacimiento resurrección",
    es_content: "Esta vida es mi vientre... La Resurrección es mi nacimiento.",
    fr_title: "Naissance résurrection",
    fr_content: "Cette vie est mon utérus... La Résurrection est ma naissance.",
    hi_title: "punarutthaan janm",
    hi_content: "यह जीवन मेरा गर्भ है... पुनरुत्थान मेरा जन्म है।",
    zh_title: "fù huó chū shēng",
    zh_content: "zhè gè shēng mìng shì wǒ de zǐ gōng... fù huó shì wǒ de chū shēng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RESURRECTION BIRTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GOSPEL->RESURRECTION BIRTH"
RETURN t, parent;
```
