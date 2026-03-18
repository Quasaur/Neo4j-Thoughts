---
type: THOUGHT
name: "thought.POWER OF CREATIVE LOVE"
alias: "Thought: Power Of Creative Love"
parent: "topic.THE GODHEAD"
en_content: "Love is not weak. Love created this insanely huge universe by simply SPEAKING!"
tags: ["love", "creation", "power", "universe", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Jan-2012a)
CREATE (t:THOUGHT {    name: "thought.POWER OF CREATIVE LOVE",
    alias: "Thought: Power Of Creative Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'creation', 'power', 'universe', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.POWER OF CREATIVE LOVE",
    ctype: "THOUGHT",
    en_title: "Power Of Creative Love",
    en_content: "Love is not weak. Love created this insanely huge universe by simply SPEAKING!",
    es_title: "El Poder del Amor Creativo",
    es_content: "El amor no es débil. ¡El amor creó este universo increíblemente inmenso simplemente HABLANDO!",
    fr_title: "Le Pouvoir de l'Amour Créateur",
    fr_content: "L'amour n'est pas faible. L'amour a créé cet univers incroyablement immense en PARLANT simplement !",
    hi_title: "सृजनशील प्रेम की शक्ति",
    hi_content: "प्रेम कमजोर नहीं है। प्रेम ने इस अविश्वसनीय रूप से विशाल ब्रह्मांड को केवल बोलकर ही बनाया!",
    zh_title: "Chuàngzào zhī Ài de Lìliàng",
    zh_content: "Ài bùshì ruòxiǎo de. Ài tōngguò jiǎndān de SHUŌHUÀ chuàngzàole zhège jídù pángdà de yǔzhòu!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.POWER OF CREATIVE LOVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->POWER OF CREATIVE LOVE"
RETURN t, parent;
```
