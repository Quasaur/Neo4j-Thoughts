---
name: "thought.BETTER NOT EASIER"
alias: "Thought: Better Not Easier"
type: THOUGHT
en_content: "Jesus did not come to make our lives easier; Christ came to make our lives better!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- better
- easier
- life
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.BETTER NOT EASIER",
    alias: "Thought: Better Not Easier",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'better', 'easier', 'life'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.BETTER NOT EASIER",
    en_title: "Better Not Easier",
    en_content: "Jesus did not come to make our lives easier; Christ came to make our lives better!",
    es_title: "Mejor, No Más Fácil",
    es_content: "Jesús no vino para hacer nuestras vidas más fáciles; ¡Cristo vino para hacer nuestras vidas mejores!",
    fr_title: "Meilleur, Pas Plus Facile",
    fr_content: "Jésus n'est pas venu pour rendre nos vies plus faciles ; Christ est venu pour rendre nos vies meilleures !",
    hi_title: "बेहतर, आसान नहीं",
    hi_content: "यीशु हमारे जीवन को आसान बनाने के लिए नहीं आए; मसीह हमारे जीवन को बेहतर बनाने के लिए आए!",
    zh_title: "Gèng hǎo, bù shì gèng róngyì 更好，不是更容易",
    zh_content: "Yēsū lái bùshì wèile ràng wǒmen de shēnghuó gèng róngyì; Jīdū lái shì wèile ràng wǒmen de shēnghuó gèng hǎo! 耶稣来不是为了让我们的生活更容易；基督来是为了让我们的生活更好！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BETTER NOT EASIER" AND c.name = "content.BETTER NOT EASIER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BETTER NOT EASIER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.BETTER NOT EASIER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >BETTER NOT EASIER" }]->(child);
```
