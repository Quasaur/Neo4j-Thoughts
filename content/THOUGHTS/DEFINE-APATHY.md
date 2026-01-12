---
name: "thought.DEFINE APATHY"
alias: "Thought: Define Apathy"
type: THOUGHT
en_content: Love & hate are not opposites...they are 2 halves of the same coin; the opposite of love / hate is Apathy.
parent: topic.ATTITUDE
tags:
  - love
  - hate
  - apathy
  - attitude
  - philosophy
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Mar-2011)
CREATE (t:THOUGHT {
    name: "thought.DEFINE APATHY",
    alias: "Thought: Define Apathy",
    parent: "topic.ATTITUDE",
    tags: ['love', 'hate', 'apathy', 'attitude', 'philosophy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE APATHY",
    en_title: "Define Apathy",
    en_content: "Love & hate are not opposites...they are 2 halves of the same coin; the opposite of love / hate is Apathy.",
    es_title: "Definir Apatía",
    es_content: "El amor y el odio no son opuestos... son 2 mitades de la misma moneda; el opuesto del amor / odio es la Apatía.",
    fr_title: "Définir l'Apathie",
    fr_content: "L'amour et la haine ne sont pas des opposés... ils sont les 2 moitiés de la même pièce ; l'opposé de l'amour / haine est l'Apathie.",
    hi_title: "उदासीनता को परिभाषित करें",
    hi_content: "प्रेम और घृणा विपरीत नहीं हैं... वे एक ही सिक्के के दो हिस्से हैं; प्रेम/घृणा का विपरीत उदासीनता है।",
    zh_title: "Dìngyì Mòbùguān xīn",
    zh_content: "Ài yǔ hèn bù shì duìlì de... Tāmen shì tóng yī méibì de 2 bàn; Ài/hèn de duìlì miàn shì Mòbùguān xīn."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINE APATHY" AND c.name = "content.DEFINE APATHY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE APATHY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.DEFINE APATHY"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >DEFINE APATHY" }]->(child);
```
