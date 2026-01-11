---
name: "thought.SOL_VELOCITY"
alias: "Thought: SOL VELOCITY"
type: THOUGHT
parent: topic.CREATION
tags:
- sol
- sun
- star
- velocity
- speed
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SOL_VELOCITY",
    alias: "Thought: SOL VELOCITY",
    parent: "topic.CREATION",
    tags: ["sol", "sun", "star", "velocity", "speed"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SOL_VELOCITY",
    en_title: "SOL VELOCITY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SOL_VELOCITY" AND c.name = "content.SOL_VELOCITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.SOL_VELOCITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SOL_VELOCITY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->SOL_VELOCITY"}]->(child);
```
