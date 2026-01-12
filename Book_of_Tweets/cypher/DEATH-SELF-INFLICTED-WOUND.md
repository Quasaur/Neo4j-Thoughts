---
name: "thought.DEATH SELF INFLICTED WOUND"
alias: "Thought: Death Self Inflicted Wound"
type: THOUGHT
en_content: "Death is not natural; it's a self-inflicted wound we incurred when we separated ourselves from God through disobedience."
parent: "topic.HUMANITY"
tags:
- death
- disobedience
- separation
- humanity
- nature
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.DEATH SELF INFLICTED WOUND",
    alias: "Thought: Death Self Inflicted Wound",
    parent: "topic.HUMANITY",
    tags: ['death', 'disobedience', 'separation', 'humanity', 'nature'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEATH SELF INFLICTED WOUND",
    en_title: "Death Self Inflicted Wound",
    en_content: "Death is not natural; it's a self-inflicted wound we incurred when we separated ourselves from God through disobedience.",
    es_title: "Muerte Herida Auto Infligida",
    es_content: "La muerte no es natural; es una herida auto infligida que sufrimos cuando nos separamos de Dios a través de la desobediencia.",
    fr_title: "Mort Blessure Auto-Infligée",
    fr_content: "La mort n'est pas naturelle ; c'est une blessure auto-infligée que nous avons subie lorsque nous nous sommes séparés de Dieu par la désobéissance.",
    hi_title: "मौत आत्म-प्रेरित घाव",
    hi_content: "मौत प्राकृतिक नहीं है; यह एक आत्म-प्रेरित घाव है जो हमें तब लगा जब हमने अवज्ञा के माध्यम से परमेश्वर से खुद को अलग कर लिया।",
    zh_title: "Sǐwáng Zìshāng Zhī Shāng",
    zh_content: "Sǐwáng bù shì zìrán de; Tā shì wǒmen tōngguò wéifǎn ér líkāi Shàngdì shí zìshāng de shāngkǒu."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEATH SELF INFLICTED WOUND" AND c.name = "content.DEATH SELF INFLICTED WOUND"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEATH SELF INFLICTED WOUND" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.DEATH SELF INFLICTED WOUND"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >DEATH SELF INFLICTED WOUND" }]->(child);
```
