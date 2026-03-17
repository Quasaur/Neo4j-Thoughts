---
type: THOUGHT
name: "thought.CONTENTMENT"
alias: "Thought: Contentment"
parent: "topic.ATTITUDE"
tags: ["contentment", "acceptance", "carefree", "failure", "faith"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.CONTENTMENT",
    alias: "Thought: Contentment",
    parent: "topic.ATTITUDE",
    tags: ["contentment", "acceptance", "carefree", "failure", "faith"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONTENTMENT",
    ctype: "THOUGHT",
    en_title: "Contentment",
    en_content: "",
    es_title: "CONTENTAMIENTO",
    es_content: "Juego mi mejor ajedrez cuando no me importa ganar... o mejor dicho, cuando no tengo ansiedad por cometer errores.",
    fr_title: "CONTENTEMENT",
    fr_content: "Je joue de mon mieux aux échecs quand je ne me soucie pas de gagner… ou plutôt, quand je n’ai aucune angoisse à l’idée de faire des erreurs.",
    hi_title: "संतोष",
    hi_content: "मैं अपना सर्वश्रेष्ठ शतरंज तब खेलता हूं जब मुझे जीत की परवाह नहीं होती... या यूँ कहें कि, जब मुझे गलतियाँ करने की कोई चिंता नहीं होती।",
    zh_title: "mǎn yì",
    zh_content: "dāng wǒ bù guān xīn shèng lì shí ， huò zhě gèng què qiè dì shuō ， dāng wǒ bù dān xīn fàn cuò wù shí ， wǒ huì xià zuì hǎo de qí 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CONTENTMENT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->CONTENTMENT"
RETURN t, parent;
```
