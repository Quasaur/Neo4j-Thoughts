---
type: THOUGHT
name: "thought.SOL VELOCITY"
alias: "Thought: Sol Velocity"
parent: "topic.CREATION"
en_content: "Creation Wonder: Our Sun is moving at 600,000 miles per hour around the center of the Milky Way galaxy, or 100,000 m.p.h. faster than past calculations!"
tags: ["sol", "sun", "star", "velocity", "speed"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SOL VELOCITY",
    alias: "Thought: Sol Velocity",
    parent: "topic.CREATION",
    tags: ["sol", "sun", "star", "velocity", "speed"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SOL VELOCITY",
    ctype: "THOUGHT",
    en_title: "Sol Velocity",
    en_content: "Creation Wonder: Our Sun is moving at 600,000 miles per hour around the center of the Milky Way galaxy, or 100,000 m.p.h. faster than past calculations!",
    es_title: "VELOCIDAD SOLAR",
    es_content: "Maravilla de la creación: Nuestro Sol se mueve a 600.000 millas por hora alrededor del centro de la Vía Láctea, o 100.000 mph. ¡Más rápido que los cálculos anteriores!",
    fr_title: "VITESSE DU SOL",
    fr_content: "Merveille de création : Notre Soleil se déplace à 600 000 milles à l'heure autour du centre de la Voie lactée, soit 100 000 mph. plus rapide que les calculs précédents !",
    hi_title: "एसओएल वेग",
    hi_content: "सृजन का आश्चर्य: हमारा सूर्य आकाशगंगा के केंद्र के चारों ओर 600,000 मील प्रति घंटे या 100,000 मील प्रति घंटे की गति से घूम रहा है। पिछली गणनाओं से तेज़!",
    zh_title: "róng jiāo sù dù",
    zh_content: "chuàng shì qí jì ： wǒ men de tài yáng zhèng yǐ měi xiǎo shí  600,000  yīng lǐ de sù dù rào zhe yín hé xì zhōng xīn yí dòng ， jí měi xiǎo shí  100,000  yīng lǐ 。 bǐ guò qù de jì suàn sù dù gèng kuài ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SOL VELOCITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->SOL VELOCITY"
RETURN t, parent;
```
