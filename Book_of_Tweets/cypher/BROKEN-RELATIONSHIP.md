---
name: "thought.BROKEN RELATIONSHIP"
alias: "Thought: Fruit of Obedience"
type: THOUGHT
tags:
- obedience
- submission
- spirit_fruit
- commitment
- worship
en_content: "A relationship with Christ that does not bear fruit in submission, worship and obedience is either broken or non-existent."
parent: topic.WORSHIP
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.BROKEN RELATIONSHIP",
    alias: "Thought: BROKEN RELATIONSHIP",
    parent: "topic.WORSHIP",
    tags: ["obedience", "submission", "spirit_fruit", "commitment", "worship"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BROKEN RELATIONSHIP",
    en_title: "BROKEN RELATIONSHIP",
    en_content: "A relationship with Christ that does not bear fruit in submission, worship and obedience is either broken or non-existent.",
    es_title: "RELACIÓN ROTA",
    es_content: "Una relación con Cristo que no da frutos en sumisión, adoración y obediencia está rota o es inexistente.",
    fr_title: "RELATION BRISÉE",
    fr_content: "Une relation avec le Christ qui ne porte pas de fruits de soumission, d'adoration et d'obéissance est soit brisée, soit inexistante.",
    hi_title: "टूटा हुआ रिश्ता",
    hi_content: "मसीह के साथ एक रिश्ता जो समर्पण, आराधना और आज्ञाकारिता में फल नहीं देता है, वह या तो टूटा हुआ है या अस्तित्वहीन है।"
    zh_title: "Pòsuì de guānxì",
    zh_content: "yī gè yǔ jī dū de guān xì ， rú guǒ bù néng zài fú cóng 、 qìng bài hé fú cóng zhōng jié chū guǒ shí ， nà tā bù shì pò suì de jiù shì bù cún zài de 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BROKEN RELATIONSHIP" AND c.name = "content.BROKEN RELATIONSHIP"
MERGE (t)-[:HAS_CONTENT {name: "edge.BROKEN RELATIONSHIP"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WORSHIP" AND child.name = "thought.BROKEN RELATIONSHIP"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.WORSHIP->BROKEN RELATIONSHIP"}]->(child);
```
