---
type: THOUGHT
name: "thought.SENTIENCE"
alias: "Thought: Sentience"
parent: "topic.SPIRITS"
tags: ["spirits", "sentience", "god", "selfaware", "iam"]
ptopic: "[[topic-SPIRITS]]"
level: 3
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SENTIENCE",
    alias: "Thought: Sentience",
    parent: "topic.SPIRITS",
    tags: ["spirits", "sentience", "god", "selfaware", "iam"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SENTIENCE",
    ctype: "THOUGHT",
    en_title: "Sentience",
 es_title: "SENTENCIA",
 fr_title: "SENTIENCE",
 hi_title: "चेतना",
 zh_title: "zhī jué",
    en_content: "",
 es_content: "¡Qué maravilla es la sensibilidad: no sólo soy para Dios, sino que lo soy para mí mismo!",
 fr_content: "Quelle merveille que la sensibilité : non seulement je suis pour Dieu, mais je le suis pour moi-même !",
 hi_content: "भावना क्या आश्चर्य है: न केवल मैं ईश्वर के प्रति हूँ, बल्कि मैं स्वयं के प्रति भी हूँ!",
 zh_content: "zhī jué shì duō me qí miào a ： wǒ bù jǐn duì shàng dì ér yán ， ér qiě duì wǒ zì jǐ yě rú cǐ ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SENTIENCE" AND c.name = "content.SENTIENCE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.SENTIENCE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITS" AND child.name = "thought.SENTIENCE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITS->SENTIENCE"}]->(child);
```