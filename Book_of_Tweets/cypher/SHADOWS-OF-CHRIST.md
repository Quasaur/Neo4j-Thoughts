---
name: "thought.SHADOWS OF CHRIST"
alias: "Thought: Shadows Of Christ"
type: THOUGHT
en_content: "That which is most precious to us...and those whom we love more than life are but shadows of the Figure of Christ!"
parent: "topic.THE GODHEAD"
tags:
- christ
- shadows
- reality
- love
- figure
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.SHADOWS OF CHRIST",
    alias: "Thought: Shadows Of Christ",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'shadows', 'reality', 'love', 'figure'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.SHADOWS OF CHRIST",
    en_title: "Shadows Of Christ",
    en_content: "That which is most precious to us...and those whom we love more than life are but shadows of the Figure of Christ!",
    es_title: "Sombras de Cristo",
    es_content: "¡Aquello que es más preciado para nosotros...y aquellos a quienes amamos más que la vida no son sino sombras de la Figura de Cristo!",
    fr_title: "Ombres du Christ",
    fr_content: "Ce qui nous est le plus précieux...et ceux que nous aimons plus que la vie ne sont que des ombres de la Figure du Christ !",
    hi_title: "मसीह की छायाएँ",
    hi_content: "जो हमारे लिए सबसे बहुमूल्य है...और जिन्हें हम जीवन से भी अधिक प्रेम करते हैं वे केवल मसीह की आकृति की छायाएँ हैं!",
    zh_title: "Jī dū de Yǐng zi",
    zh_content: "Duì wǒmen lái shuō zuì zhēn guì de...hé nàxiē wǒmen ài de chāo guò shēng mìng de rén dōu zhǐ bùguò shì Jī dū xíng xiàng de yǐng zi!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SHADOWS OF CHRIST" AND c.name = "content.SHADOWS OF CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHADOWS OF CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.SHADOWS OF CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >SHADOWS OF CHRIST" }]->(child);
```
