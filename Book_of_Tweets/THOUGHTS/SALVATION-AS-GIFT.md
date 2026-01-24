---
name: "thought.SALVATION AS GIFT"
alias: "Thought: Salvation"
type: THOUGHT
en_content: "Salvation is neither a formula, methodology nor incantation...it's a Gift!"
parent: "topic.THE GOSPEL"
tags:
- salvation
- divine_gift
- grace
- gospel
- faith
level: 2
neo4j: false
ptopic: 
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SALVATION AS GIFT",
    alias: "Thought: Salvation",
    parent: "topic.THE GOSPEL",
    tags: ["salvation", "divine_gift", "grace", "gospel", "faith"],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SALVATION AS GIFT",
    en_title: "Salvation is Gift",
    en_content: "Salvation is neither a formula, methodology nor incantation...it's a Gift!",
    es_title: "Salvación es regalo",
    es_content: "La salvación no es una fórmula, metodología ni encantamiento... ¡es un Regalo!",
    fr_title: "Salut est cadeau",
    fr_content: "Le salut n'est ni une formule, ni une méthodologie, ni une incantation... c'est un Cadeau !",
    hi_title: "mukti ek upahaar",
    hi_content: "मुक्ति न तो कोई सूत्र है, न कार्यप्रणाली और न ही कोई मंत्र... यह एक उपहार है!",
    zh_title: "jiù ēn lǐ wù",
    zh_content: "jiù ēn jì bú shì gōng shì, yě bú shì fāng fǎ lùn huò zhǒu yǔ... tā shì lǐ wù!"
});

MATCH (t:THOUGHT {name: "thought.SALVATION AS GIFT"})
MATCH (c:CONTENT {name: "content.SALVATION AS GIFT"})
MERGE (t)-[:HAS_CONTENT {name: "edge.SALVATION AS GIFT"}]->(c);

MATCH (parent:TOPIC {name: "topic.THE GOSPEL"})
MATCH (child:THOUGHT {name: "thought.SALVATION AS GIFT"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GOSPEL->SALVATION AS GIFT"}]->(child);
```
