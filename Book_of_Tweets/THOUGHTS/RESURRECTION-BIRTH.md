---
name: "thought.RESURRECTION BIRTH"
alias: "Thought: Eternal Life"
type: THOUGHT
en_content: "This life is my womb...The Resurrection is my birth."
parent: "topic.THE GOSPEL"
tags:
- resurrection
- birth
- eternity
- hope
- mystery
level: 2
neo4j: false
ptopic: 
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.RESURRECTION BIRTH",
    alias: "Thought: Eternal Life",
    parent: "topic.THE GOSPEL",
    tags: ["resurrection", "birth", "eternity", "hope", "mystery"],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.RESURRECTION BIRTH",
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

MATCH (t:THOUGHT {name: "thought.RESURRECTION BIRTH"})
MATCH (c:CONTENT {name: "content.RESURRECTION BIRTH"})
MERGE (t)-[:HAS_CONTENT {name: "edge.RESURRECTION BIRTH"}]->(c);

MATCH (parent:TOPIC {name: "topic.THE GOSPEL"})
MATCH (child:THOUGHT {name: "thought.RESURRECTION BIRTH"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GOSPEL->RESURRECTION BIRTH"}]->(child);
```
