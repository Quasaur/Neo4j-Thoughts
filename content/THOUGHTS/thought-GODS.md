---
type: THOUGHT
name: "thought.GODS"
alias: "Thought: Gods"
parent: "topic.PSYCHOLOGY"
tags: ["behavior", "intelligence", "power", "mercy", "compassion"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GODS",
    alias: "Thought: Gods",
    parent: "topic.PSYCHOLOGY",
    tags: ["behavior", "intelligence", "power", "mercy", "compassion"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GODS",
    ctype: "THOUGHT",
    en_title: "Gods",
 es_title: "GALLINERO",
 fr_title: "DIEUX",
 hi_title: "भगवान",
 zh_title: "shén",
    en_content: "",
 es_content: "No es la inteligencia ni el poder lo que nos convierte en dioses... sino la Misericordia y la Compasión.",
 fr_content: "Ce n'est ni l'intelligence ni le pouvoir qui font de nous des dieux... mais la Miséricorde et la Compassion.",
 hi_content: "यह न तो बुद्धि है और न ही शक्ति जो हमें देवता बनाती है...बल्कि दया और करुणा है।",
 zh_content: "shǐ wǒ men chéng wéi shén de jì bú shì zhì huì ， yě bú shì lì liàng …… ér shì rén cí hé tóng qíng xīn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS" AND c.name = "content.GODS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.GODS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.GODS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->GODS"}]->(child);
```