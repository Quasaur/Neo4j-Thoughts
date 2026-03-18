---
type: THOUGHT
name: "thought.EATING BREATHING DEATH"
alias: "Thought: Eating Breathing Death"
parent: "topic.MORALITY"
en_content: "We insist on eating and breathing death (meat and cigarettes) and then wonder why we get sick and die so fast and why healthcare costs are so high!"
tags: ["health", "body", "death", "morality", "healthcare"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013a)
CREATE (t:THOUGHT {    name: "thought.EATING BREATHING DEATH",
    alias: "Thought: Eating Breathing Death",
    parent: "topic.MORALITY",
    tags: ['health', 'body', 'death', 'morality', 'healthcare'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.EATING BREATHING DEATH",
    ctype: "THOUGHT",
    en_title: "Eating Breathing Death",
    en_content: "We insist on eating and breathing death (meat and cigarettes) and then wonder why we get sick and die so fast and why healthcare costs are so high!",
    es_title: "Comiendo y Respirando Muerte",
    es_content: "¡Insistimos en comer y respirar muerte (carne y cigarrillos) y luego nos preguntamos por qué nos enfermamos y morimos tan rápido y por qué los costos de atención médica son tan altos!",
    fr_title: "Manger et Respirer la Mort",
    fr_content: "Nous insistons pour manger et respirer la mort (viande et cigarettes) et ensuite nous nous demandons pourquoi nous tombons malades et mourons si vite et pourquoi les coûts des soins de santé sont si élevés !",
    hi_title: "मृत्यु को खाना और सांस लेना",
    hi_content: "हम मृत्यु को खाने और सांस लेने (मांस और सिगरेट) पर जोर देते हैं और फिर आश्चर्य करते हैं कि हम इतनी जल्दी बीमार क्यों पड़ते हैं और मर जाते हैं और स्वास्थ्य सेवा की लागत इतनी अधिक क्यों है!",
    zh_title: "Chi Si He Xi Si",
    zh_content: "Women jianchi chi si he xi si (rou lei he xiangyan), ranhou qiguai weishenme women shengbing he siwang de name kuai, weishenme yiliao feiyong name gao!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EATING BREATHING DEATH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->EATING BREATHING DEATH"
RETURN t, parent;
```
