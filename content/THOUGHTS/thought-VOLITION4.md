---
type: THOUGHT
name: "thought.VOLITION4"
alias: "Thought: Fourth Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["freedom", "volition", "free_will", "hell", "damnation"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VOLITION4",
    alias: "Thought: Fourth Volition",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "free_will", "hell", "damnation"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION4",
    ctype: "THOUGHT",
    en_title: "Fourth Volition",
 es_title: "CUARTA VOLICIÓN",
 fr_title: "QUATRIÈME VOLITION",
 hi_title: "चौथी इच्छा",
 zh_title: "dì sì cì yì yuàn",
    en_content: "",
 es_content: "Si el libre albedrío te lleva al infierno, ¿cuál era el punto?",
 fr_content: "Si le Libre Arbitre vous met en Enfer, à quoi ça sert ???",
 hi_content: "यदि स्वतंत्र इच्छा आपको नर्क में डाल देती है, तो बात क्या थी???",
 zh_content: "rú guǒ zì yóu yì zhì ràng nǐ xià dì yù ， nà hái yǒu shén me yì yì ？？？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION4" AND c.name = "content.VOLITION4"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.VOLITION4"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION4"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->VOLITION4"}]->(child);
```