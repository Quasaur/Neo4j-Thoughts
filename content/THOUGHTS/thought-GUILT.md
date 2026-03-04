---
type: THOUGHT
name: "thought.GUILT"
alias: "Thought: Guilt"
parent: "topic.PSYCHOLOGY"
tags: ["guilt", "expression", "ego", "self", "conscience"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GUILT",
    alias: "Thought: Guilt",
    parent: "topic.PSYCHOLOGY",
    tags: ["guilt", "expression", "ego", "self", "conscience"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GUILT",
    ctype: "THOUGHT",
    en_title: "Guilt",
 es_title: "CULPA",
 fr_title: "CULPABILITÉ",
 hi_title: "अपराध",
 zh_title: "yǒu zuì",
    en_content: "",
 es_content: "La culpa es sólo otra expresión del ego.",
 fr_content: "La culpabilité n'est qu'une autre expression de l'ego.",
 hi_content: "अपराध बोध अहंकार की ही एक और अभिव्यक्ति है।",
 zh_content: "nèi jiù zhǐ shì zì wǒ de lìng yī zhǒng biǎo dá 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GUILT" AND c.name = "content.GUILT"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.GUILT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.GUILT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->GUILT"}]->(child);
```