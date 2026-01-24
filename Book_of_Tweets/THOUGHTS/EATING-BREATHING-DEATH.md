---
name: "thought.EATING BREATHING DEATH"
alias: "Thought: Eating Breathing Death"
type: THOUGHT
en_content: "We insist on eating and breathing death (meat and cigarettes) and then wonder why we get sick and die so fast and why healthcare costs are so high!"
parent: "topic.MORALITY"
tags:
- health
- body
- death
- morality
- healthcare
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.EATING BREATHING DEATH",
    alias: "Thought: Eating Breathing Death",
    parent: "topic.MORALITY",
    tags: ['health', 'body', 'death', 'morality', 'healthcare'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.EATING BREATHING DEATH",
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

MATCH (t:THOUGHT {name: "thought.EATING BREATHING DEATH"})
MATCH (c:CONTENT {name: "content.EATING BREATHING DEATH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.EATING BREATHING DEATH" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.EATING BREATHING DEATH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->EATING BREATHING DEATH" }]->(child);
```
